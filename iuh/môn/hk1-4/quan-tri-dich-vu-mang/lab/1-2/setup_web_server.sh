#!/bin/bash
# ==============================================================================
# SCRIPT TỰ ĐỘNG CẤU HÌNH APACHE2 WEB SERVER TRÊN UBUNTU 22.04 (LAB 2)
# Tên miền: www.tranduong.com (IP Server: 192.168.5.2)
# ==============================================================================

if [ "$EUID" -ne 0 ]; then
  echo -e "\e[31mVui lòng chạy script này với quyền root (sudo ./setup_web_server.sh)\e[0m"
  exit 1
fi

echo -e "\e[36m[1/3] Đang làm sạch nguồn apt và cài đặt Apache2 Web Server...\e[0m"
sed -i '/cdrom/s/^/#/' /etc/apt/sources.list 2>/dev/null
apt-get update -y
apt-get install -y apache2

echo -e "\e[36m[2/3] Đang tạo giao diện trang Web mẫu cho www.tranduong.com...\e[0m"
cat <<'EOF' > /var/www/html/index.html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Trần Dương - Lab 2 Web Server</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0f172a; color: white; text-align: center; padding-top: 60px; margin: 0; }
        .container { background: #1e293b; display: inline-block; padding: 40px 60px; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid #334155; }
        h1 { color: #38bdf8; font-size: 32px; margin-bottom: 10px; }
        p { font-size: 18px; color: #94a3b8; line-height: 1.6; }
        .success-badge { background: rgba(74, 222, 128, 0.15); color: #4ade80; border: 1px solid #4ade80; padding: 10px 20px; border-radius: 30px; font-weight: bold; font-size: 18px; display: inline-block; margin: 15px 0; }
        .info-table { margin: 20px auto 0 auto; border-collapse: collapse; text-align: left; }
        .info-table td { padding: 8px 16px; color: #cbd5e1; font-size: 16px; }
        .info-table td.label { font-weight: bold; color: #94a3b8; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌐 WEBSITE TRANDUONG.COM</h1>
        <div class="success-badge">✓ CẤU HÌNH DNS BIND9 & APACHE2 WEB SERVER THÀNH CÔNG!</div>
        <table class="info-table">
            <tr>
                <td class="label">Tên miền (Domain):</td>
                <td><strong>www.tranduong.com</strong></td>
            </tr>
            <tr>
                <td class="label">Địa chỉ IP Server:</td>
                <td><strong>192.168.5.2</strong></td>
            </tr>
            <tr>
                <td class="label">Dịch vụ Web:</td>
                <td>Apache2 HTTP Server (Port 80)</td>
            </tr>
            <tr>
                <td class="label">Môn học:</td>
                <td>Quản trị dịch vụ mạng - IUH</td>
            </tr>
        </table>
    </div>
</body>
</html>
EOF

echo -e "\e[36m[3/3] Đang khởi động và kích hoạt dịch vụ Apache2...\e[0m"
systemctl restart apache2
systemctl enable apache2

echo -e "\e[32m==========================================================\e[0m"
echo -e "\e[32m HOÀN TẤT CẤU HÌNH APACHE2 WEB SERVER CHO DOMAIN tranduong.com!\e[0m"
echo -e "\e[32m Từ máy Win 7 hoặc Ubuntu Client, mở trình duyệt gõ:\e[0m"
echo -e "\e[32m http://www.tranduong.com hoặc http://192.168.5.2\e[0m"
echo -e "\e[32m==========================================================\e[0m"
