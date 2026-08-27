#!/bin/bash
# ==============================================================================
# SCRIPT TỰ ĐỘNG CẤU HÌNH SAMBA FILE SERVER TRÊN UBUNTU 22.04 (LAB 4 IUH)
# Chia sẻ file cho 3 Client: Win7_A (192.168.5.1), Win7_B (192.168.6.1), Ubuntu_2 (192.168.6.2)
# ==============================================================================

if [ "$EUID" -ne 0 ]; then
  echo -e "\e[31mVui lòng chạy script này với quyền root (sudo ./setup_samba_server.sh)\e[0m"
  exit 1
fi

echo -e "\e[36m[1/5] Đang cài đặt gói dịch vụ Samba...\e[0m"
sed -i '/cdrom/s/^/#/' /etc/apt/sources.list 2>/dev/null
apt-get update -y
apt-get install -y samba samba-common smbclient

echo -e "\e[36m[2/5] Đang tạo các thư mục chia sẻ trên Server...\e[0m"
mkdir -p /samba/public
mkdir -p /samba/private
mkdir -p /samba/tailieu

# Tạo nhóm chung cho các user bảo mật
groupadd -f sambausers

# Phân quyền thư mục công cộng (Public)
chmod -R 0777 /samba/public
chown -R nobody:nogroup /samba/public

# Phân quyền thư mục tài liệu (TaiLieu)
chmod -R 0777 /samba/tailieu

# Tạo các file văn bản mẫu
cat <<'EOF' > /samba/public/chao_mung_public.txt
============================================================
CHÀO MỪNG BẠN ĐẾN VỚI THƯ MỤC CÔNG CỘNG (PUBLIC SHARE)!
- Server: Ubuntu 1 (tranduong.com)
- Quyền hạn: Mọi máy Win 7 và Ubuntu đều có thể đọc/ghi tự do.
============================================================
EOF

cat <<'EOF' > /samba/private/thong_tin_bao_mat.txt
============================================================
THƯ MỤC BẢO MẬT NỘI BỘ (RESTRICTED AREA - LAB 4)
- Đăng nhập thành công với tài khoản: tranduong / admin
- Mật khẩu: 123456
============================================================
EOF

cat <<'EOF' > /samba/tailieu/giao_trinh_mang.txt
============================================================
TÀI LIỆU MÔN HỌC QUẢN TRỊ DỊCH VỤ MẠNG - IUH
- Chế độ: Chỉ đọc (Read-only cho Guest, Toàn quyền cho Admin)
============================================================
EOF

echo -e "\e[36m[3/5] Đang tạo người dùng và mật khẩu Samba...\e[0m"
# Tạo user hệ thống nếu chưa có
id -u tranduong &>/dev/null || useradd -m -s /bin/bash tranduong
id -u admin &>/dev/null || useradd -m -s /bin/bash admin
id -u cseuser &>/dev/null || useradd -m -s /bin/bash cseuser

usermod -aG sambausers tranduong
usermod -aG sambausers admin
usermod -aG sambausers cseuser

# Phân quyền bảo mật chặt chẽ cho thư mục Private (Chỉ User & Group được vào)
chown -R tranduong:sambausers /samba/private
chmod -R 0770 /samba/private

# Đặt mật khẩu Samba cho các tài khoản
(echo "123456"; echo "123456") | smbpasswd -a -s tranduong
(echo "123456"; echo "123456") | smbpasswd -a -s admin
(echo "cseuser"; echo "cseuser") | smbpasswd -a -s cseuser
(echo "conmeo"; echo "conmeo") | smbpasswd -a -s neko 2>/dev/null

echo -e "\e[36m[4/5] Đang cấu hình file /etc/samba/smb.conf...\e[0m"
# Sao lưu file gốc
cp /etc/samba/smb.conf /etc/samba/smb.conf.bak 2>/dev/null

cat <<EOF > /etc/samba/smb.conf
# ==============================================================================
# CẤU HÌNH SAMBA FILE SERVER - LAB 4 & LAB BỔ SUNG (IUH) - TRẦN DƯƠNG
# ==============================================================================

[global]
   workgroup = WORKGROUP
   server string = Samba File Server tranduong.com
   netbios name = UBUNTU1
   security = user
   map to guest = bad user
   dns proxy = no

   # Cho phép kết nối từ cả 2 dải mạng LAN 1 và LAN 2
   hosts allow = 192.168.5. 192.168.6. 192.168.1. 127.

   # Tương thích 100% với Windows 7 (SMBv1 / SMBv2 / SMBv3)
   client min protocol = NT1
   server min protocol = NT1

# ------------------------------------------------------------------------------
# 1. THƯ MỤC CHIA SẺ CÔNG CỘNG (PUBLIC - KHÔNG CẦN MẬT KHẨU)
# ------------------------------------------------------------------------------
[Public]
   comment = Thu muc chia se Cong cong cho moi Client
   path = /samba/public
   browseable = yes
   read only = no
   guest ok = yes
   writable = yes
   create mask = 0777
   directory mask = 0777

# ------------------------------------------------------------------------------
# 2. THƯ MỤC BẢO MẬT NỘI BỘ (PRIVATE - CẦN TÀI KHOẢN & MẬT KHẨU)
# ------------------------------------------------------------------------------
[Private]
   comment = Thu muc Bao mat Noi bo (Yeu cau User & Pass)
   path = /samba/private
   browseable = yes
   read only = no
   guest ok = no
   invalid users = nobody
   valid users = admin, tranduong, cseuser, neko
   writable = yes
   create mask = 0770
   directory mask = 0770

# ------------------------------------------------------------------------------
# 3. THƯ MỤC TÀI LIỆU HỌC TẬP (READ-ONLY CHO GUEST, WRITE CHO ADMIN)
# ------------------------------------------------------------------------------
[TaiLieu]
   comment = Thu muc Giao trinh Hoc tap (Chi doc)
   path = /samba/tailieu
   browseable = yes
   read only = yes
   guest ok = yes
   write list = admin, tranduong

# ------------------------------------------------------------------------------
# 4. THƯ MỤC SHAREDATA_1 (BÀI TẬP 5 BỔ SUNG IUH - CSEUSER)
# ------------------------------------------------------------------------------
[sharedata_1]
   comment = data share
   path = /tmp
   browseable = yes
   read only = no
   guest ok = yes
   writable = yes
   valid users = cseuser, admin, tranduong
EOF

echo -e "\e[36m[5/5] Đang kiểm tra cú pháp và Khởi động lại dịch vụ Samba...\e[0m"
testparm -s /etc/samba/smb.conf

systemctl restart smbd nmbd
systemctl enable smbd nmbd

echo -e "\e[32m==========================================================\e[0m"
echo -e "\e[32m HOÀN TẤT CẤU HÌNH SAMBA FILE SERVER CHO CẢ 3 CLIENT!\e[0m"
echo -e "\e[32m - Từ Windows 7 (Win7_A / Win7_B): Bấm Windows + R gõ:\e[0m"
echo -e "\e[32m     \\\\192.168.5.2 hoặc \\\\192.168.6.3 hoặc \\\\www.tranduong.com\e[0m"
echo -e "\e[32m - Tài khoản đăng nhập thư mục Private:\e[0m"
echo -e "\e[32m     1) User: tranduong | Pass: 123456\e[0m"
echo -e "\e[32m     2) User: admin     | Pass: 123456\e[0m"
echo -e "\e[32m==========================================================\e[0m"
