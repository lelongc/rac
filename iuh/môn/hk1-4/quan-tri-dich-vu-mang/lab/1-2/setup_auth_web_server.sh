#!/bin/bash
# ==============================================================================
# SCRIPT TỰ ĐỘNG CẤU HÌNH BẢO MẬT BẰNG TÀI KHOẢN/MẬT KHẨU (HTTP BASIC AUTH)
# Website: www.tranduong.com | Khu vực bảo mật: /private/
# Tai khoan: admin | Mat khau: 123456
# Tai khoan 2: tranduong | Mat khau: 123456
# ==============================================================================

if [ "$EUID" -ne 0 ]; then
  echo -e "\e[31mVui lòng chạy script này với quyền root (sudo ./setup_auth_web_server.sh)\e[0m"
  exit 1
fi

echo -e "\e[36m[1/4] Cài đặt gói công cụ apache2-utils & Kích hoạt các module Authentication...\e[0m"
apt-get update -y
apt-get install -y apache2-utils

a2enmod auth_basic
a2enmod authn_core
a2enmod authn_file
a2enmod authz_user
a2enmod authz_core

echo -e "\e[36m[2/4] Đang tạo thư mục bảo mật /var/www/html/private & File tài khoản mật khẩu...\e[0m"
mkdir -p /var/www/html/private

# Tạo file chứa tài khoản mật khẩu mã hóa .htpasswd
PASSWD_FILE="/etc/apache2/.htpasswd"
htpasswd -b -c ${PASSWD_FILE} admin 123456
htpasswd -b ${PASSWD_FILE} tranduong 123456

chmod 640 ${PASSWD_FILE}
chown root:www-data ${PASSWD_FILE}

echo -e "\e[36m[3/4] Đang tạo trang Web nội bộ bí mật tại /private/index.html...\e[0m"
cat <<'EOF' > /var/www/html/private/index.html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Khu Vực Bảo Mật - Trần Dương</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0f172a; color: white; text-align: center; padding-top: 60px; margin: 0; }
        .container { background: #1e293b; display: inline-block; padding: 40px 60px; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid #ef4444; }
        h1 { color: #f87171; font-size: 30px; margin-bottom: 10px; }
        p { font-size: 18px; color: #cbd5e1; line-height: 1.6; }
        .auth-badge { background: rgba(239, 68, 68, 0.2); color: #fca5a5; border: 1px solid #ef4444; padding: 10px 20px; border-radius: 30px; font-weight: bold; font-size: 18px; display: inline-block; margin: 15px 0; }
        .table-info { margin: 20px auto 0 auto; text-align: left; border-collapse: collapse; }
        .table-info td { padding: 8px 16px; color: #e2e8f0; font-size: 16px; }
        .table-info td.label { font-weight: bold; color: #94a3b8; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔒 KHU VỰC BẢO MẬT NỘI BỘ (RESTRICTED AREA)</h1>
        <div class="auth-badge">🔐 ĐÃ XÁC THỰC TÀI KHOẢN THÀNH CÔNG!</div>
        <p>Chào mừng bạn đã đăng nhập thành công vào hệ thống quản trị Web Server Trần Dương.</p>
        <table class="table-info">
            <tr>
                <td class="label">Trạng thái bảo mật:</td>
                <td><span style="color:#4ade80; font-weight:bold;">HTTP Basic Authentication Active (.htpasswd)</span></td>
            </tr>
            <tr>
                <td class="label">Tài khoản truy cập:</td>
                <td>admin / tranduong</td>
            </tr>
            <tr>
                <td class="label">Đường dẫn bảo mật:</td>
                <td>https://www.tranduong.com/private/</td>
            </tr>
        </table>
    </div>
</body>
</html>
EOF

echo -e "\e[36m[4/4] Cấu hình Apache2 bắt buộc Đăng nhập khi truy cập /private/...\e[0m"
cat <<EOF > /etc/apache2/conf-available/private-auth.conf
<Directory "/var/www/html/private">
    AuthType Basic
    AuthName "Khu Vuc Bao Mat - Vui Long Nhap Tai Khoan Va Mat Khau"
    AuthUserFile /etc/apache2/.htpasswd
    Require valid-user
</Directory>
EOF

a2enconf private-auth.conf
systemctl restart apache2

echo -e "\e[32m==========================================================\e[0m"
echo -e "\e[32m HOÀN TẤT CẤU HÌNH BẢO MẬT WEBSITE CẦN TÀI KHOẢN MẬT KHẨU!\e[0m"
echo -e "\e[32m Tài khoản thử nghiệm:\e[0m"
echo -e "\e[32m   1) Username: admin     | Password: 123456\e[0m"
echo -e "\e[32m   2) Username: tranduong | Password: 123456\e[0m"
echo -e "\e[32m Thử truy cập từ trình duyệt:\e[0m"
echo -e "\e[32m   https://www.tranduong.com/private/\e[0m"
echo -e "\e[32m==========================================================\e[0m"
