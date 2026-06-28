# SIÊU CÔNG CỤ: AutoEVE (ALL-IN-ONE)
Đúng như bạn mong muốn, đây là công cụ **Python tối thượng** dùng để giải mọi bài tập môn Định Tuyến Chuyển Mạch trên EVE-NG. 

Nguyên lý hoạt động: Bạn chỉ cần viết yêu cầu của bài Lab vào một file `JSON` vô cùng dễ đọc. Sau đó dùng chung một Script `eve_master.py` để ra lệnh:
- Lệnh `build`: Tự động tính toán các cổng, tự động nối cáp, vẽ sơ đồ và sinh ra file bài tập EVE-NG.
- Lệnh `push`: Tự động chờ thiết bị bật lên và bắn cấu hình hàng loạt.
- Lệnh `verify`: Tự động thu thập báo cáo nghiệm thu từ tất cả thiết bị.

## BƯỚC 1: TẠO SIÊU CÔNG CỤ (eve_master.py)
Trên màn hình EVE-NG Console (SSH), gõ `nano eve_master.py`, dán đoạn code dưới đây vào và lưu lại (`Ctrl+O` -> `Enter` -> `Ctrl+X`). Bạn chỉ cần tạo file này **1 lần duy nhất trong đời**:

```python
#!/usr/bin/env python3
import json
import sys
import telnetlib
import time
import os
import uuid

IMG_L3 = "L3-ADVENTERPRISEK9-M-15.4-2T.bin"
IMG_L2 = "L2-ADVENTERPRISEK9-M-15.2-IRON-20151103.bin"

def get_interface_id(if_name):
    if if_name == "eth0": return 0
    slot = int(if_name[1:].split('/')[0])
    port = int(if_name.split('/')[1])
    return port * 16 + slot

def build_lab(json_file):
    with open(json_file, 'r') as f: data = json.load(f)
    lab_name = data.get("lab_name", "Auto_Lab")
    nodes = data.get("nodes", [])
    
    node_map = {}
    for i, node in enumerate(nodes):
        node["_id"] = i + 1
        node_map[node["name"]] = node["_id"]
        
    network_map = {}; net_counter = 1
    xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    xml += '<lab name="{}" id="{}" version="1" scripttimeout="300" lock="0">\n  <topology>\n    <nodes>\n'.format(lab_name, str(uuid.uuid4()))
    
    for node in nodes:
        ntype = node.get("type", "router")
        image = IMG_L3 if ntype == "router" else (IMG_L2 if ntype == "switch" else "")
        template = "iol" if ntype in ["router", "switch"] else "vpcs"
        xml += '      <node id="{}" name="{}" type="{}" template="{}" image="{}" ethernet="1" nvram="1024" ram="1024" serial="{}" console="" delay="0" icon="{}" config="0" left="{}" top="{}">\n'.format(
            node["_id"], node["name"], "iol" if ntype in ["router", "switch"] else "vpcs", template, image, "1" if ntype == "router" else "0", "Router.png" if ntype == "router" else ("Switch.png" if ntype == "switch" else "Desktop.png"), node.get("left", 200), node.get("top", 200)
        )
        for iface in node.get("interfaces", []):
            if_id = get_interface_id(iface["name"])
            if "network" in iface:
                if iface["network"] not in network_map:
                    network_map[iface["network"]] = net_counter
                    net_counter += 1
                xml += '        <interface id="{}" name="{}" type="ethernet" network_id="{}"/>\n'.format(if_id, iface["name"], network_map[iface["network"]])
            elif "remote_node" in iface:
                r_id = node_map.get(iface["remote_node"])
                xml += '        <interface id="{}" type="serial" name="{}" remote_id="{}" remote_if="{}"/>\n'.format(if_id, iface["name"], r_id, get_interface_id(iface["remote_if"]))
        xml += '      </node>\n'
        
    xml += '    </nodes>\n    <networks>\n'
    for net_name, net_id in network_map.items():
        xml += '      <network id="{}" type="bridge" name="{}" left="0" top="0" visibility="0"/>\n'.format(net_id, net_name)
    xml += '    </networks>\n  </topology>\n</lab>'
    
    out = "/opt/unetlab/labs/{}.unl".format(lab_name)
    with open(out, "w") as f: f.write(xml)
    os.system("/opt/unetlab/wrappers/unl_wrapper -a fixpermissions")
    print("=> TẠO LAB THÀNH CÔNG: {}".format(out))

def push_config(json_file):
    with open(json_file, 'r') as f: data = json.load(f)
    print("=> BẮT ĐẦU BẮN CẤU HÌNH HÀNG LOẠT...")
    for i, node in enumerate(data.get("nodes", [])):
        cmds = node.get("config", [])
        if not cmds: continue
        port = 32768 + i + 1
        try:
            tn = telnetlib.Telnet("127.0.0.1", port, timeout=5)
            if node["type"] in ["router", "switch"]:
                ready = False
                for _ in range(30):
                    tn.write(b"\r\n"); time.sleep(1)
                    out = tn.read_very_eager().decode('ascii', errors='ignore')
                    if "yes/no" in out or "initial configuration" in out: tn.write(b"no\r\n")
                    if ">" in out or "#" in out: ready = True; break
                if not ready: continue
            else:
                tn.write(b"\r\n\r\n"); time.sleep(1)
            for cmd in cmds:
                tn.write(cmd.encode('ascii') + b"\r\n"); time.sleep(0.2)
            time.sleep(1)
            tn.write(b"write memory\r\n" if node["type"] in ["router", "switch"] else b"save\r\n")
            time.sleep(1); tn.close()
            print("   [+] Đã cấu hình xong: {}".format(node["name"]))
        except Exception as e: print("   [-] Lỗi {}: {}".format(node["name"], e))

def verify_lab(json_file):
    with open(json_file, 'r') as f: data = json.load(f)
    report = "report_{}.txt".format(data.get("lab_name", "Auto"))
    with open(report, "w") as f: f.write("========== BÁO CÁO TOÀN DIỆN ==========\n\n")
    print("=> BẮT ĐẦU TRÍCH XUẤT BÁO CÁO...")
    for i, node in enumerate(data.get("nodes", [])):
        port = 32768 + i + 1
        try:
            tn = telnetlib.Telnet("127.0.0.1", port, timeout=5)
            if node["type"] in ["router", "switch"]:
                tn.write(b"\r\n\r\n"); time.sleep(0.5); tn.write(b"enable\r\n"); time.sleep(0.5)
                out = tn.read_very_eager().decode('ascii', errors='ignore')
                if "Password:" in out or "User Access Verification" in out:
                    tn.write(b"08092023console\r\n"); time.sleep(0.5)
                    tn.write(b"enable\r\n"); time.sleep(0.5)
                    out2 = tn.read_very_eager().decode('ascii', errors='ignore')
                    if "Password:" in out2: tn.write(b"1012enable\r\n"); time.sleep(0.5)
                tn.write(b"terminal length 0\r\n"); time.sleep(0.5)
                tn.write(b"show ip interface brief\r\n"); time.sleep(1)
                tn.write(b"show ip route\r\n"); time.sleep(1)
                tn.write(b"show running-config\r\n"); time.sleep(2)
                output = out + tn.read_very_eager().decode('ascii', errors='ignore')
            else:
                tn.write(b"\r\n\r\n"); time.sleep(0.5); tn.write(b"show ip\r\n"); time.sleep(1)
                output = tn.read_very_eager().decode('ascii', errors='ignore')
            tn.close()
            with open(report, "a") as f: f.write("========== {} ==========\n{}\n\n".format(node["name"], output))
            print("   [+] Đã lưu thông tin: {}".format(node["name"]))
        except Exception as e: pass
    print("=> HOÀN TẤT! Đã lưu báo cáo tại: {}".format(report))

if __name__ == "__main__":
    if len(sys.argv) < 3: print("Dùng lệnh: python3 eve_master.py [build | push | verify] <file.json>"); sys.exit(1)
    cmd, fjson = sys.argv[1], sys.argv[2]
    if cmd == "build": build_lab(fjson)
    elif cmd == "push": push_config(fjson)
    elif cmd == "verify": verify_lab(fjson)
```

## BƯỚC 2: TẠO FILE JSON (Cho Bài Tập Mới)
Mỗi bài tập mới, bạn không cần đụng vào code Python nữa. Bạn chỉ việc tạo 1 file text ví dụ `bai5.json`. Code JSON rất dễ hiểu (đây là full code cho bài 5):

Gõ lệnh: `nano bai5.json`, dán code sau:
```json
{
  "lab_name": "Bai5_JSON_Master",
  "nodes": [
    {
      "name": "West", "type": "router", "left": 200, "top": 200,
      "interfaces": [
        {"name": "e0/0", "network": "Net4"},
        {"name": "s1/0", "remote_node": "Central", "remote_if": "s1/0"}
      ],
      "config": [
        "enable", "configure terminal", "hostname West",
        "interface Ethernet0/0", "ip address 192.168.0.1 255.255.255.0", "no shutdown", "exit",
        "interface Serial1/0", "ip address 10.0.0.1 255.255.255.0", "no shutdown", "exit",
        "ip route 0.0.0.0 0.0.0.0 10.0.0.2", "ip route 10.0.1.0 255.255.255.0 10.0.0.2",
        "ip route 192.168.1.0 255.255.255.0 10.0.0.2", "ip route 192.168.2.0 255.255.255.0 10.0.0.2", "end"
      ]
    },
    {
      "name": "Central", "type": "router", "left": 450, "top": 200,
      "interfaces": [
        {"name": "e0/0", "network": "Net5"},
        {"name": "s1/0", "remote_node": "West", "remote_if": "s1/0"},
        {"name": "s1/1", "remote_node": "East", "remote_if": "s1/1"},
        {"name": "s1/2", "remote_node": "Internet", "remote_if": "s1/0"}
      ],
      "config": [
        "enable", "configure terminal", "hostname Central",
        "interface Ethernet0/0", "ip address 192.168.1.1 255.255.255.0", "no shutdown", "exit",
        "interface Serial1/0", "ip address 10.0.0.2 255.255.255.0", "no shutdown", "exit",
        "interface Serial1/1", "ip address 10.0.1.1 255.255.255.0", "no shutdown", "exit",
        "interface Serial1/2", "ip address 10.0.2.1 255.255.255.0", "no shutdown", "exit",
        "ip route 0.0.0.0 0.0.0.0 10.0.2.2", "ip route 192.168.0.0 255.255.255.0 10.0.0.1", "ip route 192.168.2.0 255.255.255.0 10.0.1.2", "end"
      ]
    },
    {
      "name": "East", "type": "router", "left": 700, "top": 200,
      "interfaces": [
        {"name": "e0/0", "network": "Net6"},
        {"name": "s1/1", "remote_node": "Central", "remote_if": "s1/1"}
      ],
      "config": [
        "enable", "configure terminal", "hostname East",
        "service password-encryption", "enable password 08092023enable", "enable secret 1012enable",
        "username svhk1012 privilege 15 secret Tel1012@ssh",
        "interface Ethernet0/0", "ip address 192.168.2.1 255.255.255.0", "no shutdown", "exit",
        "interface Serial1/1", "ip address 10.0.1.2 255.255.255.0", "no shutdown", "exit",
        "ip route 0.0.0.0 0.0.0.0 10.0.1.1", "ip route 10.0.0.0 255.255.255.0 10.0.1.1",
        "ip route 192.168.0.0 255.255.255.0 10.0.1.1", "ip route 192.168.1.0 255.255.255.0 10.0.1.1",
        "line console 0", "password 08092023console", "login", "exec-timeout 3 0", "exit",
        "line vty 0 4", "login local", "password Tel@ssh", "transport input ssh telnet", "exit", "ip ssh authentication-retries 3", "end"
      ]
    },
    {
      "name": "Internet", "type": "router", "left": 450, "top": 50,
      "interfaces": [
        {"name": "e0/0", "network": "Net7"},
        {"name": "s1/0", "remote_node": "Central", "remote_if": "s1/2"}
      ],
      "config": [
        "enable", "configure terminal", "hostname Internet",
        "interface Ethernet0/0", "ip address 192.168.3.1 255.255.255.0", "no shutdown", "exit",
        "interface Serial1/0", "ip address 10.0.2.2 255.255.255.0", "no shutdown", "exit",
        "ip route 10.0.0.0 255.255.0.0 10.0.2.1", "ip route 192.168.0.0 255.255.0.0 10.0.2.1", "end"
      ]
    },
    {
      "name": "SW4", "type": "switch", "left": 200, "top": 350,
      "interfaces": [{"name": "e0/0", "network": "Net4"}, {"name": "e0/1", "network": "Net8"}]
    },
    {
      "name": "SW5", "type": "switch", "left": 450, "top": 350,
      "interfaces": [{"name": "e0/0", "network": "Net5"}, {"name": "e0/1", "network": "Net9"}]
    },
    {
      "name": "SW6", "type": "switch", "left": 700, "top": 350,
      "interfaces": [{"name": "e0/0", "network": "Net6"}, {"name": "e0/1", "network": "Net10"}]
    },
    {
      "name": "SW7", "type": "switch", "left": 600, "top": 50,
      "interfaces": [{"name": "e0/0", "network": "Net7"}, {"name": "e0/1", "network": "Net11"}]
    },
    {
      "name": "PC1", "type": "vpcs", "left": 200, "top": 500,
      "interfaces": [{"name": "eth0", "network": "Net8"}], "config": ["ip 192.168.0.5/24 192.168.0.1"]
    },
    {
      "name": "PC2", "type": "vpcs", "left": 450, "top": 500,
      "interfaces": [{"name": "eth0", "network": "Net9"}], "config": ["ip 192.168.1.5/24 192.168.1.1"]
    },
    {
      "name": "PC3", "type": "vpcs", "left": 700, "top": 500,
      "interfaces": [{"name": "eth0", "network": "Net10"}], "config": ["ip 192.168.2.5/24 192.168.2.1"]
    },
    {
      "name": "C4", "type": "vpcs", "left": 750, "top": 50,
      "interfaces": [{"name": "eth0", "network": "Net11"}], "config": ["ip 192.168.3.5/24 192.168.3.1"]
    }
  ]
}
```

## BƯỚC 3: CÁCH DÙNG
Quy trình làm mọi bài tập từ nay về sau:
1. Vẽ XML tự động:
   `python3 eve_master.py build bai5.json`
2. Lên Web EVE-NG, bật thiết bị, đợi 1-2 phút.
3. Bắn toàn bộ cấu hình:
   `python3 eve_master.py push bai5.json`
4. Lấy báo cáo nghiệm thu nộp bài:
   `python3 eve_master.py verify bai5.json`

(Ghi chú: Lệnh verify tôi đã thêm sẵn tính năng nhập password `08092023console` và `1012enable` vào để nó đi xuyên qua Router East luôn rồi đó!). 
Mời bạn trải nghiệm phép màu Automation chuẩn DevSecOps!
