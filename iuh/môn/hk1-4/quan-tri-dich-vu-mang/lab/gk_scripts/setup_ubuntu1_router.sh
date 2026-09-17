#!/bin/bash
# ==============================================================================
# SCRIPT CẤU HÌNH UBUNTU 1 (ROUTER LIÊN MẠNG LAN 1 & LAN 2 + NAT SSH)
# ==============================================================================
echo "=== ĐANG CẤU HÌNH NETPLAN CHO UBUNTU 1 (ROUTER) ==="

cat << 'EOF' | sudo tee /etc/netplan/00-installer-config.yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    ens33:
      dhcp4: true
    ens37:
      dhcp4: no
      addresses:
        - 192.168.5.2/24
    ens38:
      dhcp4: no
      addresses:
        - 192.168.6.3/24
EOF

sudo chmod 600 /etc/netplan/00-installer-config.yaml
sudo netplan apply

echo "=== BẬT IP FORWARDING & TẮT TƯỜNG LỬA ==="
sudo sysctl -w net.ipv4.ip_forward=1
echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
sudo ufw disable

echo "=== HOÀN TẤT CẤU HÌNH UBUNTU 1! ==="
ip -brief addr
