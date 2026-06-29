import os
import json
import time
import paramiko
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

EVE_IP = "192.168.2.128"
EVE_SSH_USER = "root"
EVE_SSH_PASS = "eve"
EVE_API_USER = "admin"
EVE_API_PASS = "eve"

EVE_MASTER_SCRIPT = """#!/usr/bin/env python3
import json, sys, telnetlib, time, os, uuid

IMG_L3 = "L3-ADVENTERPRISEK9-M-15.4-2T.bin"
IMG_L2 = "L2-ADVENTERPRISEK9-M-15.2-IRON-20151103.bin"

def get_interface_id(if_name):
    if if_name == "eth0": return 0
    slot = int(if_name[1:].split('/')[0])
    port = int(if_name.split('/')[1])
    return slot * 16 + port

def mask_to_cidr(mask):
    try:
        return sum([bin(int(x)).count("1") for x in mask.split(".")])
    except:
        return mask

def build_lab(json_file):
    with open(json_file, 'r') as f: data = json.load(f)
    lab_name = data.get("lab_name", "Auto_Lab")
    nodes = data.get("nodes", [])
    ip_table = data.get("ip_table", [])
    
    xml = '<?xml version="1.0" encoding="UTF-8"?>\\n'
    xml += '<lab name="{}" id="35d7b51b-4228-40b4-93e8-5b1216d62f90" version="1" scripttimeout="300" lock="0">\\n'.format(lab_name)
    xml += '  <topology>\\n    <nodes>\\n'
    
    node_map = {}
    for idx, node in enumerate(nodes):
        node_map[node["name"]] = idx + 1
        
    network_map = {}
    net_counter = 1
    
    for idx, node in enumerate(nodes):
        node_id = idx + 1
        ntype = node.get("type", "router")
        if ntype == "router":
            xml += '      <node id="{}" name="{}" type="iol" template="iol" image="{}" ethernet="1" nvram="1024" ram="1024" serial="1" console="" delay="0" icon="Router.png" config="0" left="{}" top="{}">\\n'.format(node_id, node["name"], IMG_L3, node.get("left", 200), node.get("top", 200))
        elif ntype == "switch":
            xml += '      <node id="{}" name="{}" type="iol" template="iol" image="{}" ethernet="1" nvram="1024" ram="1024" serial="0" console="" delay="0" icon="Switch.png" config="0" left="{}" top="{}">\\n'.format(node_id, node["name"], IMG_L2, node.get("left", 200), node.get("top", 200))
        elif ntype == "vpcs":
            xml += '      <node id="{}" name="{}" type="vpcs" template="vpcs" image="vpcs" ethernet="1" delay="0" icon="Desktop.png" config="0" left="{}" top="{}">\\n'.format(node_id, node["name"], node.get("left", 200), node.get("top", 200))
            
        for iface in node.get("interfaces", []):
            if_id = get_interface_id(iface["name"])
            if "network" in iface:
                if iface["network"] not in network_map:
                    network_map[iface["network"]] = net_counter
                    net_counter += 1
                itype = "serial" if iface["name"].startswith("s") else "ethernet"
                xml += '        <interface id="{}" name="{}" type="{}" network_id="{}"/>\\n'.format(if_id, iface["name"], itype, network_map[iface["network"]])
        xml += '      </node>\\n'
        
    xml += '    </nodes>\\n    <networks>\\n'
    for net_name, net_id in network_map.items():
        xml += '      <network id="{}" type="bridge" name="{}" left="300" top="300" visibility="0"/>\\n'.format(net_id, net_name)
    xml += '    </networks>\\n'
    
    xml += '    <textobjects>\\n'
    text_id = 1
    import base64
    for row in ip_table:
        device_name = row.get("device")
        iface_name = row.get("interface")
        ip = row.get("ip")
        subnet = row.get("subnet", "")
        
        cidr = mask_to_cidr(subnet) if subnet else ""
        label_text = "{}: {}/{}".format(iface_name, ip, cidr) if cidr else "{}: {}".format(iface_name, ip)
        b64_label = base64.b64encode(label_text.encode('utf-8')).decode('utf-8')
        
        left, top = 200, 200
        for node in nodes:
            if node.get("name") == device_name:
                left = int(node.get("left", 200))
                top = int(node.get("top", 200))
                break
                
        if "s" in iface_name.lower():
            left += 70
            top += 20
        else:
            left += 20
            top += 70
            
        xml += '      <textobject id="{}" name="t{}" type="text" left="{}" top="{}">\\n'.format(text_id, text_id, left, top)
        xml += '        <data>{}</data>\\n'.format(b64_label)
        xml += '      </textobject>\\n'
        text_id += 1
        
    xml += '    </textobjects>\\n'
    xml += '  </topology>\\n'
    xml += '</lab>'
    
    out = "/opt/unetlab/labs/{}.unl".format(lab_name)
    with open(out, "w") as f: f.write(xml)
    os.system("/opt/unetlab/wrappers/unl_wrapper -a fixpermissions")

def push_config(json_file):
    with open(json_file, 'r') as f: data = json.load(f)
    for i, node in enumerate(data.get("nodes", [])):
        cmds = node.get("config", [])
        if not cmds: continue
        port = 32768 + i + 1
        try:
            tn = telnetlib.Telnet("127.0.0.1", port, timeout=5)
            if node["type"] in ["router", "switch"]:
                ready = False
                for _ in range(40):
                    tn.write(b"\\r\\n"); time.sleep(1)
                    out = tn.read_very_eager().decode('ascii', errors='ignore')
                    if "yes/no" in out or "initial configuration" in out: tn.write(b"no\\r\\n")
                    if ">" in out or "#" in out: ready = True; break
                if not ready: continue
            else:
                tn.write(b"\\r\\n\\r\\n"); time.sleep(1)
            for cmd in cmds:
                tn.write(cmd.encode('ascii') + b"\\r\\n"); time.sleep(0.2)
            time.sleep(1)
            tn.write(b"write memory\\r\\n" if node["type"] in ["router", "switch"] else b"save\\r\\n")
            time.sleep(1); tn.close()
        except Exception as e: pass

def verify_lab(json_file):
    with open(json_file, 'r') as f: data = json.load(f)
    report = "/root/report_{}.txt".format(data.get("lab_name", "Auto"))
    with open(report, "w") as f: f.write("========== BAO CAO TOAN DIEN ==========\\n\\n")
    for i, node in enumerate(data.get("nodes", [])):
        port = 32768 + i + 1
        try:
            tn = telnetlib.Telnet("127.0.0.1", port, timeout=5)
            if node["type"] in ["router", "switch"]:
                tn.write(b"\\r\\n\\r\\n"); time.sleep(0.5); tn.write(b"enable\\r\\n"); time.sleep(0.5)
                out = tn.read_very_eager().decode('ascii', errors='ignore')
                if "Password:" in out or "User Access Verification" in out:
                    tn.write(b"08092023console\\r\\n"); time.sleep(0.5)
                    tn.write(b"enable\\r\\n"); time.sleep(0.5)
                    out2 = tn.read_very_eager().decode('ascii', errors='ignore')
                    if "Password:" in out2: tn.write(b"1012enable\\r\\n"); time.sleep(0.5)
                tn.write(b"terminal length 0\\r\\n"); time.sleep(0.5)
                tn.write(b"show ip interface brief\\r\\n"); time.sleep(1)
                tn.write(b"show ip route\\r\\n"); time.sleep(1)
                tn.write(b"show running-config\\r\\n"); time.sleep(2)
                output = out + tn.read_very_eager().decode('ascii', errors='ignore')
            else:
                tn.write(b"\\r\\n\\r\\n"); time.sleep(0.5); tn.write(b"show ip\\r\\n"); time.sleep(1)
                output = tn.read_very_eager().decode('ascii', errors='ignore')
            tn.close()
            with open(report, "a") as f: f.write("========== {} ==========\\n{}\\n\\n".format(node["name"], output))
        except Exception as e: pass

if __name__ == "__main__":
    cmd, fjson = sys.argv[1], sys.argv[2]
    if cmd == "build": build_lab(fjson)
    elif cmd == "push": push_config(fjson)
    elif cmd == "verify": verify_lab(fjson)
"""

def ssh_execute(client, command):
    stdin, stdout, stderr = client.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()
    out = stdout.read().decode()
    err = stderr.read().decode()
    return exit_status, out, err

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/deploy', methods=['POST'])
def deploy():
    try:
        lab_config = request.json
        lab_name = lab_config.get("lab_name", "Auto_Lab")
        json_str = json.dumps(lab_config)
        
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(EVE_IP, username=EVE_SSH_USER, password=EVE_SSH_PASS, timeout=10)
        
        print(f"Deploying Lab: {lab_name}")
        
        sftp = client.open_sftp()
        with sftp.file('/root/autoeve_master.py', 'w') as f: f.write(EVE_MASTER_SCRIPT)
        with sftp.file(f'/root/{lab_name}.json', 'w') as f: f.write(json_str)
        sftp.close()
        
        ssh_execute(client, f"python3 /root/autoeve_master.py build /root/{lab_name}.json")
        
        # Start nodes via API
        session = requests.Session()
        login = session.post(f"http://{EVE_IP}/api/auth/login", json={"username": EVE_API_USER, "password": EVE_API_PASS, "html5": "-1"})
        if login.status_code == 200:
            nodes_res = session.get(f"http://{EVE_IP}/api/labs/{lab_name}.unl/nodes")
            if nodes_res.status_code == 200:
                for node_id in nodes_res.json().get("data", {}).keys():
                    session.get(f"http://{EVE_IP}/api/labs/{lab_name}.unl/nodes/{node_id}/start")
            
        # Wait for nodes to boot
        time.sleep(45)
        
        ssh_execute(client, f"python3 /root/autoeve_master.py push /root/{lab_name}.json")
        ssh_execute(client, f"python3 /root/autoeve_master.py verify /root/{lab_name}.json")
        
        _, report_text, _ = ssh_execute(client, f"cat /root/report_{lab_name}.txt")
        client.close()
        
        return jsonify({"success": True, "report": report_text})
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
