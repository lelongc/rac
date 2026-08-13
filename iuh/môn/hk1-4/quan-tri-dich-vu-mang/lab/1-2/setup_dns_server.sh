#!/bin/bash
# ==============================================================================
# SCRIPT TỰ ĐỘNG CẤU HÌNH DNS SERVER BIND9 TRÊN UBUNTU 22.04 (LAB 2)
# ==============================================================================

if [ "$EUID" -ne 0 ]; then
  echo -e "\e[31mVui lòng chạy script này với quyền root (sudo ./setup_dns_server.sh)\e[0m"
  exit 1
fi

DOMAIN="tranduong.com"
SERVER_IP="192.168.5.2"

echo -e "\e[36m[1/4] Đang cập nhật và cài đặt dịch vụ BIND9 DNS Server...\e[0m"
apt-get update -y
apt-get install -y bind9 bind9utils bind9-doc dnsutils

echo -e "\e[36m[2/4] Đang khai báo Zone $DOMAIN vào /etc/bind/named.conf.default-zones...\e[0m"

# Tránh ghi trùng zone nếu chạy lại nhiều lần
if ! grep -q "zone \"$DOMAIN\"" /etc/bind/named.conf.default-zones; then
cat <<EOF >> /etc/bind/named.conf.default-zones

zone "$DOMAIN" {
    type master;
    file "/etc/bind/db.$DOMAIN";
};
EOF
fi

echo -e "\e[36m[3/4] Đang tạo file cơ sở dữ liệu Zone /etc/bind/db.$DOMAIN...\e[0m"
cat <<EOF > /etc/bind/db.$DOMAIN
\$TTL    604800
@       IN      SOA     ns.$DOMAIN. root.$DOMAIN. (
                                 2         ; Serial
                            604800         ; Refresh
                             86400         ; Retry
                           2419200         ; Expire
                            604800 )
;
@       IN      NS      ns.$DOMAIN.

ns      IN      A       $SERVER_IP
www     IN      A       $SERVER_IP
ftp     IN      A       10.10.10.1
mail    IN      A       $SERVER_IP
win7a   IN      A       192.168.5.1
win7b   IN      A       192.168.6.1
ubuntuB IN      A       192.168.6.2
EOF

echo -e "\e[36m[4/4] Kiểm tra cú pháp cấu hình và khởi động dịch vụ BIND9...\e[0m"
named-checkconf
named-checkzone $DOMAIN /etc/bind/db.$DOMAIN

systemctl restart bind9
systemctl enable bind9

echo -e "\e[32m==========================================================\e[0m"
echo -e "\e[32m HOÀN TẤT CẤU HÌNH DNS SERVER BIND9 CHO DOMAIN $DOMAIN!\e[0m"
echo -e "\e[32m Bạn có thể kiểm tra bằng lệnh: nslookup ns.$DOMAIN\e[0m"
echo -e "\e[32m==========================================================\e[0m"
