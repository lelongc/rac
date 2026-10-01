#!/bin/bash
# ==============================================================================
# SCRIPT CẤU HÌNH VSFTPD SERVER - CHẾ ĐỘ STANDALONE (BÀI LAB 7 DEMO 1)
# Thực hiện trên: Ubuntu_1 (LinuxA - 192.168.1.150 / 192.168.6.3 / 192.168.5.2)
# ==============================================================================

set -e

echo "[+] 1. Cài đặt vsftpd..."
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y vsftpd ftp

echo "[+] 2. Đảm bảo dịch vụ xinetd không chiếm cổng 21..."
if [ -f /etc/xinetd.d/vsftpd ]; then
    sudo rm -f /etc/xinetd.d/vsftpd
    sudo systemctl restart xinetd
fi

echo "[+] 3. Cấu hình /etc/vsftpd.conf ở chế độ Standalone..."
sudo cp /etc/vsftpd.conf /etc/vsftpd.conf.backup.$(date +%F)

sudo bash -c 'cat << "EOF" > /etc/vsftpd.conf
# Chế độ Standalone (Lắng nghe độc lập qua Systemd)
listen=YES
listen_ipv6=NO

# Không cho phép người dùng nặc danh (Anonymous) theo yêu cầu đề bài
anonymous_enable=NO

# Cho phép tài khoản cục bộ hệ thống đăng nhập
local_enable=YES

# Cho phép thực thi lệnh ghi (Upload file, tạo thư mục)
write_enable=YES

# Phân quyền mặc định cho file tạo mới (022 -> 755 cho thư mục, 644 cho file)
local_umask=022

dirmessage_enable=YES
use_localtime=YES
xferlog_enable=YES
connect_from_port_20=YES

# Khóa người dùng vào thư mục cá nhân (Chroot)
chroot_local_user=YES
allow_writeable_chroot=YES

secure_chroot_dir=/var/run/vsftpd/empty
pam_service_name=vsftpd
rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
ssl_enable=NO
EOF'

echo "[+] 4. Kích hoạt và khởi động lại dịch vụ vsftpd..."
sudo systemctl enable vsftpd
sudo systemctl restart vsftpd

echo "[+] 5. Kiểm tra cổng 21 (FTP) đang mở bởi vsftpd..."
sudo ss -tlnp | grep :21 || sudo netstat -tlpn | grep :21

echo "=============================================================================="
echo "[SUCCESS] VSFTPD ở chế độ Standalone đã được khởi tạo thành công!"
echo "- anonymous_enable = NO (Cấm anonymous)"
echo "- local_enable = YES (Cho phép user hệ thống login: neko, testuser1,...)"
echo "- write_enable = YES (Cho phép upload/tạo file)"
echo "- chroot_local_user = YES (Cô lập user trong thư mục riêng)"
echo "=============================================================================="
