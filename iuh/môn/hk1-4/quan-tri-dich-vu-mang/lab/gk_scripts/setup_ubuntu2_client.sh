#!/bin/bash
# ==============================================================================
# SCRIPT CẤU HÌNH UBUNTU 2 (CLIENT LAN 2 / RELAY AGENT + NAT SSH)
# ==============================================================================
echo "=== ĐANG CẤU HÌNH NETPLAN CHO UBUNTU 2 ==="

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
        - 192.168.6.2/24
      routes:
        - to: 192.168.5.0/24
          via: 192.168.6.3
EOF

sudo chmod 600 /etc/netplan/00-installer-config.yaml
sudo netplan apply
sudo ufw disable

echo "=== HOÀN TẤT CẤU HÌNH UBUNTU 2! ==="
ip -brief addr
