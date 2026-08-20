#!/bin/bash
# ==============================================================================
# SCRIPT TỰ ĐỘNG CẤU HÌNH HTTPS (SSL/TLS CERTIFICATE) CHO APACHE2 (LAB 2)
# Tên miền: www.tranduong.com | IP: 192.168.5.2 | Port: 443
# ==============================================================================

if [ "$EUID" -ne 0 ]; then
  echo -e "\e[31mVui lòng chạy script này với quyền root (sudo ./setup_https_server.sh)\e[0m"
  exit 1
fi

DOMAIN="tranduong.com"
WWW_DOMAIN="www.tranduong.com"
SERVER_IP="192.168.5.2"
CERT_DIR="/etc/ssl/certs"
KEY_DIR="/etc/ssl/private"
CERT_FILE="${CERT_DIR}/tranduong.crt"
KEY_FILE="${KEY_DIR}/tranduong.key"

echo -e "\e[36m[1/4] Kích hoạt module SSL trong Apache2...\e[0m"
a2enmod ssl
a2enmod headers

echo -e "\e[36m[2/4] Đang khởi tạo Chứng chỉ SSL Self-Signed cho ${WWW_DOMAIN}...\e[0m"
mkdir -p ${CERT_DIR} ${KEY_DIR}

openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout ${KEY_FILE} \
  -out ${CERT_FILE} \
  -subj "/C=VN/ST=HCM/L=TPHCM/O=IUH/OU=QTMANGB2/CN=${WWW_DOMAIN}" \
  -addext "subjectAltName=DNS:${WWW_DOMAIN},DNS:${DOMAIN},IP:${SERVER_IP}"

# Hạ SECLEVEL xuống 0 trong OpenSSL để hỗ trợ bắt tay TLS 1.0 SHA-1 với Internet Explorer trên Windows 7
sed -i 's/CipherString = DEFAULT:@SECLEVEL=2/CipherString = DEFAULT:@SECLEVEL=0/g' /etc/ssl/openssl.cnf 2>/dev/null
sed -i 's/CipherString = DEFAULT:@SECLEVEL=1/CipherString = DEFAULT:@SECLEVEL=0/g' /etc/ssl/openssl.cnf 2>/dev/null
sed -i 's/SSLProtocol all -SSLv3/SSLProtocol all +TLSv1 +TLSv1.1 +TLSv1.2/g' /etc/apache2/mods-available/ssl.conf 2>/dev/null
sed -i 's/SSLCipherSuite HIGH:!aNULL/SSLCipherSuite ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+EXP:@SECLEVEL=0/g' /etc/apache2/mods-available/ssl.conf 2>/dev/null

chmod 600 ${KEY_FILE}
chmod 644 ${CERT_FILE}

echo -e "\e[36m[3/4] Cấu hình VirtualHost HTTPS (Port 443) cho Apache2...\e[0m"
cat <<EOF > /etc/apache2/sites-available/tranduong-ssl.conf
<IfModule mod_ssl.c>
<VirtualHost *:443>
    ServerAdmin webmaster@${DOMAIN}
    ServerName ${WWW_DOMAIN}
    ServerAlias ${DOMAIN}
    DocumentRoot /var/www/html

    SSLEngine on
    SSLCertificateFile ${CERT_FILE}
    SSLCertificateKeyFile ${KEY_FILE}

    # Tương thích 100% với trình duyệt Internet Explorer trên Windows 7
    SSLProtocol all +TLSv1 +TLSv1.1 +TLSv1.2 +TLSv1.3
    SSLCipherSuite ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+EXP:@SECLEVEL=0

    ErrorLog \${APACHE_LOG_DIR}/tranduong_ssl_error.log
    CustomLog \${APACHE_LOG_DIR}/tranduong_ssl_access.log combined
</VirtualHost>
</IfModule>
EOF

# Cấu hình VirtualHost HTTP (Port 80) hoạt động song song với HTTPS (Port 443)
cat <<EOF > /etc/apache2/sites-available/000-default.conf
<VirtualHost *:80>
    ServerAdmin webmaster@${DOMAIN}
    ServerName ${WWW_DOMAIN}
    ServerAlias ${DOMAIN}
    DocumentRoot /var/www/html

    ErrorLog \${APACHE_LOG_DIR}/error.log
    CustomLog \${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
EOF

echo -e "\e[36m[4/4] Bật cấu hình trang Web SSL và Khởi động lại Apache2...\e[0m"
a2ensite tranduong-ssl.conf
systemctl restart apache2
systemctl enable apache2

echo -e "\e[32m==========================================================\e[0m"
echo -e "\e[32m HOÀN TẤT CẤU HÌNH HTTPS (SSL/TLS) CHO WEBSITE ${WWW_DOMAIN}!\e[0m"
echo -e "\e[32m - Truy cập HTTP thường (Port 80):  http://${WWW_DOMAIN}\e[0m"
echo -e "\e[32m - Truy cập HTTPS bảo mật (Port 443): https://${WWW_DOMAIN}\e[0m"
echo -e "\e[32m==========================================================\e[0m"
