#!/bin/bash
# ==========================================================
# SCRIPT DỌN DẸP SẠCH SẼ ASTERISK TRÊN UBUNTU
# Mục đích: Xóa mọi thứ để test chạy lại setup_voip_ubuntu.sh
# ==========================================================

# Yêu cầu quyền root
if [ "$EUID" -ne 0 ]; then
  echo "Vui lòng chạy script này với quyền root (sudo ./clean_asterisk.sh)"
  exit 1
fi

echo "=========================================================="
echo " ĐANG DỌN DẸP HỆ THỐNG ASTERISK..."
echo "=========================================================="

# 1. Dừng dịch vụ Asterisk
echo "[1/3] Đang dừng dịch vụ Asterisk..."
systemctl stop asterisk 2>/dev/null
systemctl disable asterisk 2>/dev/null
killall -9 asterisk 2>/dev/null

# 2. Gỡ cài đặt triệt để các gói phần mềm
echo "[2/3] Đang gỡ bỏ các gói phần mềm Asterisk..."
apt-get purge -y asterisk asterisk-core-sounds-en asterisk-core-sounds-en-wav asterisk-core-sounds-en-g722 asterisk-modules asterisk-voicemail asterisk-config
apt-get autoremove -y
apt-get clean

# 3. Xóa toàn bộ file cấu hình và dữ liệu rác
echo "[3/3] Đang xóa toàn bộ file cấu hình, log và dữ liệu..."
rm -rf /etc/asterisk
rm -rf /var/lib/asterisk
rm -rf /var/log/asterisk
rm -rf /var/spool/asterisk
rm -rf /usr/lib/asterisk
rm -rf /var/run/asterisk

echo "=========================================================="
echo " XÓA HOÀN TẤT! Máy ảo Ubuntu đã trở về trạng thái sạch."
echo " Bạn đã có thể chạy lại file setup_voip_ubuntu.sh"
echo "=========================================================="
