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
    return port * 16 + slot

def get_eve_if_name(if_name):
    if if_name == "eth0": return "eth0"
    slot = int(if_name[1:].split('/')[0])
    port = int(if_name.split('/')[1])
    return "e{}/{}".format(slot, port)

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
    
    import hashlib
    lab_uuid = str(uuid.UUID(hashlib.md5(lab_name.encode()).hexdigest()))
    
    # Collect all network endpoints
    network_endpoints = {}
    for i, node in enumerate(nodes):
        node_id = i + 1
        for iface in node.get("interfaces", []):
            net = iface.get("network")
            if not net: continue
            if net not in network_endpoints:
                network_endpoints[net] = []
            network_endpoints[net].append((node_id, iface["name"], get_interface_id(iface["name"])))
    
    # Serial pairs: 2 serial endpoints on same network -> point-to-point
    serial_pairs = {}
    bridge_networks = {}
    net_counter = 1
    
    for net_name, endpoints in network_endpoints.items():
        is_serial = any(ep[1].startswith("s") for ep in endpoints)
        if is_serial and len(endpoints) == 2:
            n1, _, i1 = endpoints[0]
            n2, _, i2 = endpoints[1]
            serial_pairs[(n1, i1)] = (n2, i2)
            serial_pairs[(n2, i2)] = (n1, i1)
        else:
            bridge_networks[net_name] = net_counter
            net_counter += 1
    
    xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\\n'
    xml += '<lab name="{}" id="{}" version="1" scripttimeout="300" lock="0">\\n  <topology>\\n    <nodes>\\n'.format(lab_name, lab_uuid)
    
    for i, node in enumerate(nodes):
        node_id = i + 1
        ntype = node.get("type", "router")
        if ntype == "router":
            xml += '      <node id="{}" name="{}" type="iol" template="iol" image="{}" ethernet="1" nvram="1024" ram="1024" serial="1" console="" delay="0" icon="Router.png" config="0" left="{}" top="{}">\\n'.format(node_id, node["name"], IMG_L3, node.get("left", 200), node.get("top", 200))
        elif ntype == "switch":
            xml += '      <node id="{}" name="{}" type="iol" template="iol" image="{}" ethernet="1" nvram="1024" ram="1024" serial="0" console="" delay="0" icon="Switch.png" config="0" left="{}" top="{}">\\n'.format(node_id, node["name"], IMG_L2, node.get("left", 200), node.get("top", 200))
        elif ntype == "vpcs":
            xml += '      <node id="{}" name="{}" type="vpcs" template="vpcs" image="vpcs" ethernet="1" delay="0" icon="Desktop.png" config="0" left="{}" top="{}">\\n'.format(node_id, node["name"], node.get("left", 200), node.get("top", 200))
            
        for iface in node.get("interfaces", []):
            if_id = get_interface_id(iface["name"])
            net = iface.get("network")
            if not net: continue
            
            if (node_id, if_id) in serial_pairs:
                rem_node, rem_if = serial_pairs[(node_id, if_id)]
                xml += '        <interface id="{}" name="{}" type="serial" remote_id="{}" remote_if="{}"/>\\n'.format(if_id, get_eve_if_name(iface["name"]), rem_node, rem_if)
            elif net in bridge_networks:
                xml += '        <interface id="{}" name="{}" type="ethernet" network_id="{}"/>\\n'.format(if_id, get_eve_if_name(iface["name"]), bridge_networks[net])
        xml += '      </node>\\n'
        
    xml += '    </nodes>\\n    <networks>\\n'
    for net_name, net_id in bridge_networks.items():
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
        for n in nodes:
            if n.get("name") == device_name:
                left = int(n.get("left", 200))
                top = int(n.get("top", 200))
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
    xml += '  </topology>\\n</lab>'
    
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
        json_str = json.dumps(lab_config, indent=2)
        print(f"RECEIVED JSON:\n{json_str}")
        
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(EVE_IP, username=EVE_SSH_USER, password=EVE_SSH_PASS, timeout=10)
        
        print(f"Deploying Lab: {lab_name}")
        
        # 1. Stop and wipe via SSH CLI (100% reliable)
        print("Stopping and wiping existing nodes via CLI...")
        ssh_execute(client, f"/opt/unetlab/wrappers/unl_wrapper -a stop -T 0 -F /opt/unetlab/labs/{lab_name}.unl")
        time.sleep(3)
        ssh_execute(client, f"/opt/unetlab/wrappers/unl_wrapper -a wipe -T 0 -F /opt/unetlab/labs/{lab_name}.unl")
        time.sleep(2)
        
        # 2. Upload and Build new XML
        sftp = client.open_sftp()
        with sftp.file('/root/autoeve_master.py', 'w') as f: f.write(EVE_MASTER_SCRIPT)
        with sftp.file(f'/root/{lab_name}.json', 'w') as f: f.write(json_str)
        sftp.close()
        
        exit_code, build_out, build_err = ssh_execute(client, f"python3 /root/autoeve_master.py build /root/{lab_name}.json")
        print(f"BUILD exit={exit_code}")
        if build_err: print(f"BUILD stderr: {build_err}")
        
        # 3. Start nodes via CLI
        print("Starting nodes via CLI...")
        ssh_execute(client, f"/opt/unetlab/wrappers/unl_wrapper -a start -T 0 -F /opt/unetlab/labs/{lab_name}.unl")
        
        # Wait for nodes to boot
        time.sleep(45)
        
        ssh_execute(client, f"python3 /root/autoeve_master.py push /root/{lab_name}.json")
        
        # Wait for dynamic routing protocols (like RIP) to converge
        print("Waiting 30s for RIP convergence...")
        time.sleep(30)
        
        ssh_execute(client, f"python3 /root/autoeve_master.py verify /root/{lab_name}.json")
        
        _, report_text, _ = ssh_execute(client, f"cat /root/report_{lab_name}.txt")
        client.close()
        
        return jsonify({"success": True, "report": report_text})
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
