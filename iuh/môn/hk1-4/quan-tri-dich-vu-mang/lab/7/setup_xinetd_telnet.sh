#!/bin/bash
# ==============================================================================
# SCRIPT CẤU HÌNH XINETD & TELNET SERVER (BÀI LAB 7)
# Thực hiện trên: Ubuntu_1 (LinuxA - 192.168.1.150 / 192.168.6.3 / 192.168.5.2)
# ==============================================================================

set -e

echo "[+] 1. Cài đặt các gói xinetd và telnetd..."
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y xinetd telnetd

echo "[+] 2. Tạo file cấu hình dịch vụ Telnet quản lý bởi Xinetd (/etc/xinetd.d/telnet)..."
sudo bash -c 'cat << "EOF" > /etc/xinetd.d/telnet
service telnet
{
    flags           = REUSE
    socket_type     = stream
    protocol        = tcp
    wait            = no
    user            = root
    server          = /usr/sbin/in.telnetd
    log_on_failure  += USERID
    disable         = no
}
EOF'

echo "[+] 3. Kích hoạt và khởi động lại dịch vụ xinetd..."
sudo systemctl enable xinetd
sudo systemctl restart xinetd

echo "[+] 4. Kiểm tra trạng thái cổng 23 (Telnet) do xinetd quản lý..."
sudo ss -tlnp | grep :23 || sudo netstat -tlpn | grep :23

echo "=============================================================================="
echo "[SUCCESS] Dịch vụ Telnet qua Xinetd đã được khởi tạo và sẵn sàng lắng nghe!"
echo "Kiểm tra từ Client bằng lệnh: telnet 192.168.6.3 23"
echo "=============================================================================="
