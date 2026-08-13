#!/bin/bash
# ==========================================================
# SCRIPT TỰ ĐỘNG CẤU HÌNH GMAIL CHO ASTERISK VOICEMAIL
# Lệnh chạy: sudo ./setup_gmail.sh <email> <app_password>
# ==========================================================

if [ "$EUID" -ne 0 ]; then
  echo -e "\e[31mVui lòng chạy script này với quyền root (sudo ./setup_gmail.sh)\e[0m"
  exit 1
fi

if [ "$#" -ne 2 ]; then
    echo -e "\e[33mCÁCH SỬ DỤNG:\e[0m"
    echo "sudo ./setup_gmail.sh <địa_chỉ_gmail_của_bạn> <app_password_của_bạn>"
    echo ""
    echo "Ví dụ: sudo ./setup_gmail.sh sv.iuh.demo@gmail.com abcdefghijklmnop"
    echo ""
    echo "Lưu ý: App Password là mật khẩu ứng dụng 16 ký tự tạo trong tài khoản Google (không phải mật khẩu đăng nhập bình thường)."
    exit 1
fi

GMAIL_USER=$1
GMAIL_PASS=$2

echo -e "\e[36m[1/3] Đang tạo cấu hình kết nối msmtp cho email: $GMAIL_USER...\e[0m"

cat <<EOF > /etc/msmtprc
defaults
auth           on
tls            on
tls_trust_file /etc/ssl/certs/ca-certificates.crt
logfile        /var/log/msmtp.log

account        gmail
host           smtp.gmail.com
port           587
from           $GMAIL_USER
user           $GMAIL_USER
password       $GMAIL_PASS

account default : gmail
EOF

chmod 640 /etc/msmtprc
chown root:asterisk /etc/msmtprc 2>/dev/null || chown root:root /etc/msmtprc
touch /var/log/msmtp.log
chown asterisk:asterisk /var/log/msmtp.log 2>/dev/null || true
chmod 666 /var/log/msmtp.log # Để ai chạy msmtp cũng ghi log được


echo -e "\e[36m[2/3] Đang cập nhật hòm thư nhận Voicemail sang $GMAIL_USER...\e[0m"
# Đổi địa chỉ nhận voicemail trong Asterisk sang email vừa nhập luôn để tiện test
sed -i "s/sv.iuh.demo@gmail.com/$GMAIL_USER/g" /etc/asterisk/voicemail.conf 2>/dev/null || true

echo -e "\e[36m[3/3] Đang gửi 1 email thử nghiệm (Test Email) đến $GMAIL_USER...\e[0m"
echo -e "Subject: [IUH-VoIP] Test cau hinh Voicemail Asterisk Thanh Cong\n\nChuc mung! He thong tong dai Asterisk cua ban da duoc ket noi thanh cong voi tai khoan Gmail nay. Tu bay gio moi cuoc goi nho se duoc gui vao day." | msmtp -t "$GMAIL_USER"

if [ $? -eq 0 ]; then
    echo -e "\e[32m-> XONG! Email test đã gửi thành công.\e[0m"
    echo -e "\e[32m-> Hãy kiểm tra hộp thư (hoặc mục Spam) của $GMAIL_USER.\e[0m"
else
    echo -e "\e[31m-> Gửi email thất bại!\e[0m"
    echo "Hãy kiểm tra lại:"
    echo "1. Máy ảo Ubuntu có internet không (ping google.com)."
    echo "2. App Password có chính xác không (không có khoảng trắng)."
    echo "3. Google có khóa tài khoản tạm thời không."
fi

# Restart lại Asterisk để nhận cấu hình hộp thư mới
systemctl restart asterisk
echo -e "\e[32m================ HOÀN TẤT ===================\e[0m"
