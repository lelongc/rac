#!/bin/bash
# ==============================================================================
# SCRIPT CẤU HÌNH BẢO MẬT OPENSSH SERVER (BÀI LAB 7)
# Thực hiện trên: Ubuntu_1 (LinuxA - 192.168.1.150 / 192.168.6.3 / 192.168.5.2)
# ==============================================================================

set -e

echo "[+] 1. Đảm bảo OpenSSH Server đã được cài đặt..."
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y openssh-server openssh-client

echo "[+] 2. Tạo 2 người dùng thử nghiệm: testuser1 (Được phép) & testuser2 (Bị chặn)..."
id testuser1 2>/dev/null || sudo useradd -m -s /bin/bash testuser1
echo "testuser1:123" | sudo chpasswd

id testuser2 2>/dev/null || sudo useradd -m -s /bin/bash testuser2
echo "testuser2:123" | sudo chpasswd

echo "[+] 3. Cấu hình bảo mật trong /etc/ssh/sshd_config..."
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup.$(date +%F)

# Bỏ cấu hình cũ nếu có
sudo sed -i '/^AllowUsers/d' /etc/ssh/sshd_config
sudo sed -i '/^PermitRootLogin/d' /etc/ssh/sshd_config

# Thêm quy tắc: Chỉ cho phép user neko và testuser1 đăng nhập, cấm root đăng nhập trực tiếp
sudo bash -c 'cat << "EOF" >> /etc/ssh/sshd_config

# Lab 7: OpenSSH Access Control
PermitRootLogin no
AllowUsers neko testuser1
EOF'

echo "[+] 4. Kiểm tra cú pháp cấu hình sshd và khởi động lại dịch vụ..."
sudo sshd -t
sudo systemctl restart ssh

echo "=============================================================================="
echo "[SUCCESS] Cấu hình bảo mật OpenSSH hoàn tất!"
echo "- User neko: ĐƯỢC PHÉP đăng nhập (Pass: conmeo)"
echo "- User testuser1: ĐƯỢC PHÉP đăng nhập (Pass: 123)"
echo "- User testuser2: BỊ TỪ CHỐI truy cập (Pass: 123)"
echo "- User root: BỊ CẤM đăng nhập trực tiếp"
echo "=============================================================================="
