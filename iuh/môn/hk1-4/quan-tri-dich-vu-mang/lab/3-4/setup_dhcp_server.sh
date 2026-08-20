#!/bin/bash
# ==============================================================================
# SCRIPT TỰ ĐỘNG CẤU HÌNH DHCP SERVER (ISC-DHCP-SERVER) TRÊN UBUNTU 22.04 (LAB 3)
# Cấp phát IP tự động cho cả 2 mạng LAN 1 (VMnet2) và LAN 2 (VMnet3)
# Domain: tranduong.com | DNS Server: 192.168.5.2
# ==============================================================================

if [ "$EUID" -ne 0 ]; then
  echo -e "\e[31mVui lòng chạy script này với quyền root (sudo ./setup_dhcp_server.sh)\e[0m"
  exit 1
fi

echo -e "\e[36m[1/4] Đang cài đặt gói dịch vụ isc-dhcp-server...\e[0m"
sed -i '/cdrom/s/^/#/' /etc/apt/sources.list 2>/dev/null
apt-get update -y
apt-get install -y isc-dhcp-server

echo -e "\e[36m[2/4] Đang cấu hình Card mạng lắng nghe cấp phát DHCP (/etc/default/isc-dhcp-server)...\e[0m"
cat <<EOF > /etc/default/isc-dhcp-server
# Cấu hình card mạng lắng nghe cấp phát DHCP cho IPv4
INTERFACESv4="ens37 ens38"
INTERFACESv6=""
EOF

echo -e "\e[36m[3/4] Đang tạo file cấu hình cấp phát IP (/etc/dhcp/dhcpd.conf)...\e[0m"
cat <<EOF > /etc/dhcp/dhcpd.conf
# ==============================================================================
# CẤU HÌNH DHCP SERVER CHO BÀI LAB 3 (IUH) - TRẦN DƯƠNG
# ==============================================================================

# Thiết lập thông số mặc định toàn cục
default-lease-time 600;
max-lease-time 7200;
authoritative;

# ------------------------------------------------------------------------------
# 1. KHAI BÁO DẢI CẤP PHÁT CHO MẠNG LAN 1 (VMnet2 - Nối Win7_A qua card ens37)
# ------------------------------------------------------------------------------
subnet 192.168.5.0 netmask 255.255.255.0 {
    # Dải IP cấp động cho các máy Client thuộc LAN 1
    range 192.168.5.10 192.168.5.50;
    
    # Cấu hình Gateway và Subnet Mask
    option routers 192.168.5.2;
    option subnet-mask 255.255.255.0;
    option broadcast-address 192.168.5.255;
    
    # Cấu hình Tên miền và DNS Server trỏ về BIND9 Ubuntu 1
    option domain-name "tranduong.com";
    option domain-name-servers 192.168.5.2, 8.8.8.8;
}

# ------------------------------------------------------------------------------
# 2. KHAI BÁO DẢI CẤP PHÁT CHO MẠNG LAN 2 (VMnet3 - Nối Win7_B & Ubuntu_2 qua card ens38)
# ------------------------------------------------------------------------------
subnet 192.168.6.0 netmask 255.255.255.0 {
    # Dải IP cấp động cho các máy Client thuộc LAN 2
    range 192.168.6.10 192.168.6.50;
    
    # Cấu hình Gateway và Subnet Mask
    option routers 192.168.6.3;
    option subnet-mask 255.255.255.0;
    option broadcast-address 192.168.6.255;
    
    # Cấu hình Tên miền và DNS Server trỏ về BIND9 Ubuntu 1
    option domain-name "tranduong.com";
    option domain-name-servers 192.168.5.2, 8.8.8.8;
}

# ------------------------------------------------------------------------------
# 3. KHAI BÁO SUBMET NAT ĐỂ DHCP SERVER KHÔNG BÁO LỖI KHỞI ĐỘNG (ens33)
# ------------------------------------------------------------------------------
subnet 192.168.1.0 netmask 255.255.255.0 {
    # Để trống, không cấp phát trên card NAT
}
EOF

echo -e "\e[36m[4/4] Kiểm tra cú pháp và Khởi động lại dịch vụ DHCP Server...\e[0m"
dhcpd -t -cf /etc/dhcp/dhcpd.conf

systemctl restart isc-dhcp-server
systemctl enable isc-dhcp-server

echo -e "\e[32m==========================================================\e[0m"
echo -e "\e[32m HOÀN TẤT CẤU HÌNH DHCP SERVER (ISC-DHCP-SERVER)!\e[0m"
echo -e "\e[32m - Dải cấp phát LAN 1 (VMnet2): 192.168.5.10 -> 192.168.5.50 (GW: 192.168.5.2)\e[0m"
echo -e "\e[32m - Dải cấp phát LAN 2 (VMnet3): 192.168.6.10 -> 192.168.6.50 (GW: 192.168.6.3)\e[0m"
echo -e "\e[32m - DNS Server tự động cấp:    192.168.5.2 (tranduong.com)\e[0m"
echo -e "\e[32m==========================================================\e[0m"
