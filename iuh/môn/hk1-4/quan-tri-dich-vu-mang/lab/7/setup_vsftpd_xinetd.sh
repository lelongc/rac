#!/bin/bash
# ==============================================================================
# SCRIPT CHUYỂN ĐỔI VSFTPD SANG QUẢN LÝ BẰNG XINETD (BÀI LAB 7 DEMO 2)
# Thực hiện trên: Ubuntu_1 (LinuxA - 192.168.1.150 / 192.168.6.3 / 192.168.5.2)
# ==============================================================================

set -e

echo "[+] 1. Đổi cấu hình vsftpd.conf: tắt chế độ tự lắng nghe (listen=NO)..."
sudo sed -i 's/^listen=YES/listen=NO/' /etc/vsftpd.conf
sudo sed -i 's/^listen_ipv6=YES/listen_ipv6=NO/' /etc/vsftpd.conf

echo "[+] 2. Dừng và vô hiệu hóa dịch vụ Standalone vsftpd..."
sudo systemctl stop vsftpd 2>/dev/null || true
sudo systemctl disable vsftpd 2>/dev/null || true

echo "[+] 3. Tạo file cấu hình dịch vụ FTP cho Xinetd (/etc/xinetd.d/vsftpd)..."
sudo bash -c 'cat << "EOF" > /etc/xinetd.d/vsftpd
service ftp
{
    socket_type     = stream
    protocol        = tcp
    wait            = no
    user            = root
    server          = /usr/sbin/vsftpd
    server_args     = /etc/vsftpd.conf
    disable         = no
}
EOF'

echo "[+] 4. Khởi động lại dịch vụ super-server Xinetd..."
sudo systemctl restart xinetd

echo "[+] 5. Kiểm tra cổng 21 hiện tại (Phải hiển thị tiến trình xinetd quản lý)..."
sudo ss -tlnp | grep :21 || sudo netstat -tlpn | grep :21

echo "=============================================================================="
echo "[SUCCESS] VSFTPD đã được chuyển sang chế độ quản lý qua XINETD thành công!"
echo "Port 21 hiện do daemon xinetd quản lý lắng nghe thay cho vsftpd standalone."
echo "Kiểm tra kết nối từ Client: ftp 192.168.6.3"
echo "=============================================================================="
