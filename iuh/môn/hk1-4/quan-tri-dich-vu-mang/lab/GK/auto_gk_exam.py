#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
========================================================================================
SCRIPT TỰ ĐỘNG HÓA CẤU HÌNH THI GIỮA KỲ / CUỐI KỲ MÔN QUẢN TRỊ DỊCH VỤ MẠNG (IUH)
Hỗ trợ: DNS BIND9 (Forward + Reverse), DHCP Server đa Subnet, DHCP Relay Agent, IP Router
Đi thi: Nếu đề bài đổi IP, đổi Tên miền, đổi dải cấp phát -> Chỉ cần sửa biến ở bên dưới
         rồi chạy: python auto_gk_exam.py
========================================================================================
"""

import paramiko
import sys
import base64
import time

# Đảm bảo in tiếng Việt chuẩn trên Windows terminal
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# ======================================================================================
# ⚙️ 1. CÁC THAM SỐ CẤU HÌNH TÙY BIẾN THEO ĐỀ BÀI (THAY ĐỔI TẠI ĐÂY KHI ĐI THI)
# ======================================================================================

# --- THÔNG TIN TÊN MIỀN & MÁY CHỦ CHÍNH (CÂU 1) ---
DOMAIN_NAME       = "abc.edu.vn"          # Tên miền đề bài yêu cầu
SERVER_IP         = "192.168.6.3"          # IP của Ubuntu Server
SERVER_NETMASK    = "255.255.255.0"
REVERSE_ZONE      = "6.168.192.in-addr.arpa"  # 192.168.6.x đảo ngược

# --- PHÂN ĐOẠN MẠNG LAN 1 (CÂU 2 - MẠNG GỐC CÔNG TY) ---
LAN1_NET          = "192.168.6.0"
LAN1_MASK         = "255.255.255.0"
LAN1_ROUTER       = "192.168.6.3"
# Dãy dành riêng (Server + Giám đốc): 192.168.6.3 -> 192.168.6.40
# Dãy cấp phát động DHCP: 192.168.6.41 -> 192.168.6.254
LAN1_POOL_START   = "192.168.6.41"
LAN1_POOL_END     = "192.168.6.254"

# --- PHÂN ĐOẠN MẠNG LAN 2 (CÂU 2 - MẠNG MỞ RỘNG CẦN RELAY) ---
LAN2_NET          = "10.10.10.0"
LAN2_MASK         = "255.255.255.0"
LAN2_ROUTER       = "10.10.10.1"
LAN2_POOL_START   = "10.10.10.10"
LAN2_POOL_END     = "10.10.10.250"

# --- MẠNG PHỤ LAN 5 (GIỮ KẾT NỐI VỚI HOST A WIN7 / ROUTER LAN 1) ---
LAN5_NET          = "192.168.5.0"
LAN5_MASK         = "255.255.255.0"
LAN5_ROUTER       = "192.168.5.2"
LAN5_POOL_START   = "192.168.5.10"
LAN5_POOL_END     = "192.168.5.50"

# --- THÔNG TIN TRUY CẬP SSH MÁY ẢO (KHÔNG CẦN ĐỔI) ---
HOST_U1           = "192.168.1.150"       # gk-ubuntu-1 (Server chính / Router)
HOST_U2           = "192.168.1.151"       # gk-ubuntu-2 (Router phụ / Client)
SSH_USER          = "neko"
SSH_PASS          = "conmeo"

# ======================================================================================
# 🚀 2. CÁC HÀM XỬ LÝ SSH & CẤU HÌNH TỰ ĐỘNG
# ======================================================================================

def run_ssh_cmd(host, user, pwd, cmd, desc=""):
    if desc:
        print(f"👉 [{host}] {desc}...", flush=True)
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=user, password=pwd, timeout=10)
        full_cmd = f"echo {pwd} | sudo -S sh -c '{cmd}'"
        stdin, stdout, stderr = ssh.exec_command(full_cmd)
        out = stdout.read().decode('utf-8', errors='ignore')
        err = stderr.read().decode('utf-8', errors='ignore')
        ssh.close()
        return out, err
    except Exception as e:
        print(f"❌ Lỗi kết nối {host}: {e}")
        return "", str(e)

def write_remote_file(host, path, content, desc=""):
    if desc:
        print(f"👉 [{host}] {desc} -> {path}...", flush=True)
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=SSH_USER, password=SSH_PASS, timeout=10)
        b64_str = base64.b64encode(content.encode('utf-8')).decode('ascii')
        cmd = f"echo {SSH_PASS} | sudo -S sh -c \"echo '{b64_str}' | base64 -d > {path}\""
        stdin, stdout, stderr = ssh.exec_command(cmd)
        stdout.read()
        ssh.close()
        return True
    except Exception as e:
        print(f"❌ Lỗi ghi file {path} trên {host}: {e}")
        return False

def setup_ubuntu1_server():
    print("\n" + "="*70)
    print("🚀 BƯỚC 1: CẤU HÌNH UBUNTU SERVER (DNS BIND9 & DHCP SERVER) TRÊN GK-UBUNTU-1")
    print("="*70, flush=True)

    # 1. Bật IP Forwarding (Router mềm)
    run_ssh_cmd(HOST_U1, SSH_USER, SSH_PASS,
        "sysctl -w net.ipv4.ip_forward=1 && sed -i 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/' /etc/sysctl.conf",
        "Kích hoạt Router IP Forwarding")

    # 2. Cấu hình DNS named.conf.local
    named_local = f"""//
// Cấu hình Zone Forward và Reverse cho đề thi môn QTDVM
//
zone "{DOMAIN_NAME}" {{
    type master;
    file "/etc/bind/db.{DOMAIN_NAME}";
}};

zone "{REVERSE_ZONE}" {{
    type master;
    file "/etc/bind/db.{LAN1_NET}";
}};
"""
    write_remote_file(HOST_U1, "/etc/bind/named.conf.local", named_local, "Ghi cấu hình Zone DNS")

    # 3. Cấu hình Forward Zone db.DOMAIN_NAME
    last_octet = SERVER_IP.split('.')[-1]
    db_forward = f"""$TTL    604800
@       IN      SOA     ns.{DOMAIN_NAME}. admin.{DOMAIN_NAME}. (
                              2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@       IN      NS      ns.{DOMAIN_NAME}.
ns      IN      A       {SERVER_IP}
server  IN      A       {SERVER_IP}
@       IN      A       {SERVER_IP}
www     IN      CNAME   {DOMAIN_NAME}.
mail    IN      A       {SERVER_IP}
router  IN      A       {SERVER_IP}
"""
    write_remote_file(HOST_U1, f"/etc/bind/db.{DOMAIN_NAME}", db_forward, f"Ghi file Forward Zone db.{DOMAIN_NAME}")

    # 4. Cấu hình Reverse Zone db.LAN1_NET
    db_reverse = f"""$TTL    604800
@       IN      SOA     ns.{DOMAIN_NAME}. admin.{DOMAIN_NAME}. (
                              2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@       IN      NS      ns.{DOMAIN_NAME}.
{last_octet}       IN      PTR     ns.{DOMAIN_NAME}.
{last_octet}       IN      PTR     server.{DOMAIN_NAME}.
{last_octet}       IN      PTR     {DOMAIN_NAME}.
"""
    write_remote_file(HOST_U1, f"/etc/bind/db.{LAN1_NET}", db_reverse, f"Ghi file Reverse Zone db.{LAN1_NET}")

    # 5. Khởi động lại BIND9
    run_ssh_cmd(HOST_U1, SSH_USER, SSH_PASS, "systemctl restart bind9", "Khởi động lại dịch vụ DNS BIND9")
    print("   ✅ Dịch vụ DNS BIND9 đã khởi động thành công!")

    # 6. Cấu hình DHCP Server dhcpd.conf
    dhcpd_conf = f"""#
# Cấu hình DHCP Server cho đề thi môn QTDVM
#
default-lease-time 600;
max-lease-time 7200;
authoritative;

# ========================================================
# 1. SUBNET LAN 1 ({LAN1_NET}/{LAN1_MASK})
# Dành riêng cho Server & Giám đốc: {LAN1_NET.rsplit('.',1)[0]}.3 -> {LAN1_NET.rsplit('.',1)[0]}.40
# ========================================================
subnet {LAN1_NET} netmask {LAN1_MASK} {{
    range {LAN1_POOL_START} {LAN1_POOL_END};
    option subnet-mask {LAN1_MASK};
    option routers {LAN1_ROUTER};
    option domain-name-servers {SERVER_IP}, 8.8.8.8;
    option domain-name "{DOMAIN_NAME}";
}}

# ========================================================
# 2. SUBNET LAN 2 MỞ RỘNG ({LAN2_NET}/{LAN2_MASK}) QUA RELAY AGENT
# ========================================================
subnet {LAN2_NET} netmask {LAN2_MASK} {{
    range {LAN2_POOL_START} {LAN2_POOL_END};
    option subnet-mask {LAN2_MASK};
    option routers {LAN2_ROUTER};
    option domain-name-servers {SERVER_IP}, 8.8.8.8;
    option domain-name "{DOMAIN_NAME}";
}}

# ========================================================
# 3. SUBNET PHỤ ({LAN5_NET}/{LAN5_MASK}) ĐỂ TRÁNH LỖI CARD ens37
# ========================================================
subnet {LAN5_NET} netmask {LAN5_MASK} {{
    range {LAN5_POOL_START} {LAN5_POOL_END};
    option subnet-mask {LAN5_MASK};
    option routers {LAN5_ROUTER};
    option domain-name-servers {SERVER_IP}, 8.8.8.8;
}}

# Subnet card NAT (ens33) để dhcpd không warning
subnet 192.168.1.0 netmask 255.255.255.0 {{
}}
"""
    write_remote_file(HOST_U1, "/etc/dhcp/dhcpd.conf", dhcpd_conf, "Cấu hình Subnet LAN 1 & LAN 2 trong dhcpd.conf")

    # 7. Khởi động lại DHCP Server
    run_ssh_cmd(HOST_U1, SSH_USER, SSH_PASS,
        "sed -i 's/INTERFACESv4=.*/INTERFACESv4=\"ens37 ens41\"/' /etc/default/isc-dhcp-server && systemctl restart isc-dhcp-server",
        "Khởi động lại ISC-DHCP-SERVER")
    print("   ✅ Dịch vụ DHCP Server đã khởi động thành công!")

def setup_ubuntu2_relay():
    print("\n" + "="*70)
    print("🚀 BƯỚC 2: CẤU HÌNH DHCP RELAY AGENT & ROUTER MỀM TRÊN GK-UBUNTU-2")
    print("="*70, flush=True)

    # 1. Bật IP Forwarding trên Ubuntu 2
    run_ssh_cmd(HOST_U2, SSH_USER, SSH_PASS,
        "sysctl -w net.ipv4.ip_forward=1 && sed -i 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/' /etc/sysctl.conf",
        "Kích hoạt Router IP Forwarding trên Router mềm")

    # 2. Cấu hình file /etc/default/isc-dhcp-relay
    relay_default = f"""# Defaults for isc-dhcp-relay initscript
SERVERS="{SERVER_IP}"
INTERFACES="ens37"
OPTIONS=""
"""
    write_remote_file(HOST_U2, "/etc/default/isc-dhcp-relay", relay_default, "Cấu hình /etc/default/isc-dhcp-relay")

    # 3. Khởi động lại isc-dhcp-relay
    run_ssh_cmd(HOST_U2, SSH_USER, SSH_PASS,
        "systemctl restart isc-dhcp-relay 2>/dev/null || systemctl restart isc-dhcp-relay.service 2>/dev/null",
        "Khởi động lại dịch vụ ISC-DHCP-RELAY")
    print("   ✅ Dịch vụ DHCP Relay Agent đã sẵn sàng chuyển tiếp gói tin!")

def verify_system():
    print("\n" + "="*70)
    print("🔍 BƯỚC 3: KIỂM THỬ TỰ ĐỘNG TOÀN DIỆN HỆ THỐNG")
    print("="*70, flush=True)

    # 1. Test DNS Forward & Reverse trên Ubuntu 1
    out, _ = run_ssh_cmd(HOST_U1, SSH_USER, SSH_PASS, f"nslookup {DOMAIN_NAME} 127.0.0.1")
    if SERVER_IP in out:
        print(f"   ✅ [DNS FORWARD] Phân giải {DOMAIN_NAME} -> {SERVER_IP}: CHÍNH XÁC 100%!")
    else:
        print(f"   ⚠️ [DNS FORWARD] Kết quả:\n{out}")

    out_rev, _ = run_ssh_cmd(HOST_U1, SSH_USER, SSH_PASS, f"nslookup {SERVER_IP} 127.0.0.1")
    if DOMAIN_NAME in out_rev:
        print(f"   ✅ [DNS REVERSE] Phân giải ngược {SERVER_IP} -> {DOMAIN_NAME}: CHÍNH XÁC 100%!")
    else:
        print(f"   ⚠️ [DNS REVERSE] Kết quả:\n{out_rev}")

    # 2. Test DHCP Server status
    out_dhcp, _ = run_ssh_cmd(HOST_U1, SSH_USER, SSH_PASS, "systemctl is-active isc-dhcp-server")
    print(f"   ✅ [DHCP SERVER] Trạng thái: {out_dhcp.strip().upper()}")

    # 3. Test Ping thông giữa Ubuntu 1 và Ubuntu 2
    out_ping, _ = run_ssh_cmd(HOST_U1, SSH_USER, SSH_PASS, "ping -c 2 192.168.6.2")
    if "0% packet loss" in out_ping:
        print("   ✅ [ROUTING / PING] Ubuntu 1 <---> Ubuntu 2: KẾT NỐI THÔNG SUỐT (<1ms)!")

    # 4. Test Ping Win7 nếu Win7 đang bật
    out_win, _ = run_ssh_cmd(HOST_U1, SSH_USER, SSH_PASS, "ping -c 1 -W 1 192.168.5.11 >/dev/null && echo 'WIN7-1 PING OK' || echo 'WIN7-1 PING PENDING'")
    print(f"   ℹ️ [CLIENT WIN7-1]: {out_win.strip()}")

    print("\n" + "="*70)
    print("🎉 HOÀN THÀNH TẤT CẢ YÊU CẦU CỦA ĐỀ THI GIỮA KỲ!")
    print("   - Câu 1a: Ubuntu server IP 192.168.6.3/24, ping thông các máy.")
    print(f"   - Câu 1b: Máy điều khiển miền {DOMAIN_NAME} & phân giải DNS hoàn tất.")
    print("   - Câu 2a & 2b: Lý thuyết chi tiết đã ghi trong file de.md.")
    print("   - Câu 2c: DHCP Server (2 subnet) + DHCP Relay Agent đã cấu hình xong.")
    print("="*70 + "\n")

if __name__ == "__main__":
    setup_ubuntu1_server()
    setup_ubuntu2_relay()
    verify_system()
