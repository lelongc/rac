#!/bin/bash
# ==============================================================================
# SCRIPT TỰ ĐỘNG CẤU HÌNH NFS SERVER (NETWORK FILE SYSTEM) TRÊN UBUNTU 22.04 (LAB 4 IUH)
# Chia sẻ thư mục qua giao thức NFS cho máy Client Linux (Ubuntu 2: 192.168.6.2 / 192.168.5.3)
# ==============================================================================

if [ "$EUID" -ne 0 ]; then
  echo -e "\e[31mVui lòng chạy script này với quyền root (sudo ./setup_nfs_server.sh)\e[0m"
  exit 1
fi

echo -e "\e[36m[1/4] Đang cài đặt gói dịch vụ NFS Kernel Server...\e[0m"
sed -i '/cdrom/s/^/#/' /etc/apt/sources.list 2>/dev/null
apt-get update -y
apt-get install -y nfs-kernel-server rpcbind

echo -e "\e[36m[2/4] Đang tạo các thư mục chia sẻ NFS trên Server...\e[0m"
mkdir -p /nfs/share
mkdir -p /nfs/tailieu

# Phân quyền truy cập cho thư mục chia sẻ (Toàn quyền đọc/ghi không phân quyền)
chmod -R 0777 /nfs/share
chmod -R 0777 /nfs/tailieu
chown -R nobody:nogroup /nfs/share
chown -R nobody:nogroup /nfs/tailieu

# Tạo file mẫu để kiểm tra
cat <<'EOF' > /nfs/share/chao_mung_nfs.txt
============================================================
CHÀO MỪNG BẠN ĐẾN VỚI DỊCH VỤ CHIA SẺ FILE NFS - IUH LAB 4
- Server: Ubuntu 1 (192.168.5.2 / 192.168.6.3)
- Giao thức: Network File System (NFSv4)
- Trạng thái: Đọc / Ghi tự do (Read/Write)
============================================================
EOF

cat <<'EOF' > /nfs/tailieu/giao_trinh_nfs.txt
============================================================
TÀI LIỆU HỌC TẬP QUA NFS - CHẾ ĐỘ READ ONLY
- Server: Ubuntu 1
- Quyền hạn: Chỉ đọc (ro)
============================================================
EOF

echo -e "\e[36m[3/4] Đang cấu hình file xuất khẩu tài nguyên (/etc/exports)...\e[0m"
# Sao lưu file gốc
cp /etc/exports /etc/exports.bak 2>/dev/null

cat <<'EOF' > /etc/exports
# ==============================================================================
# CẤU HÌNH NFS EXPORTS - LAB 4 (IUH) - TRẦN DƯƠNG
# ==============================================================================

# 1. Thư mục chia sẻ không phân quyền (Đọc & Ghi - rw) cho cả 2 mạng LAN
/nfs/share    192.168.5.0/24(rw,sync,no_subtree_check,no_root_squash) 192.168.6.0/24(rw,sync,no_subtree_check,no_root_squash)

# 2. Thư mục tài liệu (Chỉ đọc - ro) cho các máy Client
/nfs/tailieu  192.168.5.0/24(ro,sync,no_subtree_check) 192.168.6.0/24(ro,sync,no_subtree_check)
EOF

echo -e "\e[36m[4/4] Đang áp dụng cấu hình và Khởi động lại dịch vụ NFS...\e[0m"
# Áp dụng cấu hình exports
exportfs -ra
exportfs -v

# Bật và khởi động dịch vụ
systemctl restart rpcbind nfs-kernel-server
systemctl enable rpcbind nfs-kernel-server

echo -e "\e[32m==========================================================\e[0m"
echo -e "\e[32m HOÀN TẤT CẤU HÌNH NFS SERVER!\e[0m"
echo -e "\e[32m - Danh sách thư mục chia sẻ:\e[0m"
echo -e "\e[32m     1) /nfs/share    (Quyền: rw - Đọc & Ghi toàn quyền)\e[0m"
echo -e "\e[32m     2) /nfs/tailieu  (Quyền: ro - Chỉ đọc)\e[0m"
echo -e "\e[32m - Hướng dẫn Client Linux (Ubuntu 2) kết nối:\e[0m"
echo -e "\e[32m     1. Cài đặt:   sudo apt install -y nfs-common\e[0m"
echo -e "\e[32m     2. Xem Share: showmount -e 192.168.6.3\e[0m"
echo -e "\e[32m     3. Mount:     sudo mkdir -p /mnt/nfs\e[0m"
echo -e "\e[32m                   sudo mount -t nfs 192.168.6.3:/nfs/share /mnt/nfs\e[0m"
echo -e "\e[32m==========================================================\e[0m"
