# 📁 TỔNG HỢP SCRIPT & HƯỚNG DẪN THI GIỮA KỲ QUẢN TRỊ DỊCH VỤ MẠNG

Thư mục này chứa toàn bộ các kịch bản cấu hình, batch file và tài liệu hướng dẫn vận hành hệ thống 4 máy ảo (`gk-ubuntu-1`, `gk-ubuntu-2`, `gk-win7-1`, `gk-win7-2`).

---

## 📑 Danh mục tài liệu & Script

1. **[HUONG_DAN_DOI_IP_VA_KET_NOI.md](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/quan-tri-dich-vu-mang/lab/gk_scripts/HUONG_DAN_DOI_IP_VA_KET_NOI.md)**:
   * Bản đồ mạng chi tiết 4 máy ảo và thông tin đăng nhập (`neko`/`conmeo`).
   * Giải thích cơ chế vì sao đổi IP thì SSH/Telnet không bao giờ rớt kết nối (Mạng quản trị ngầm `ens33` VMnet8 NAT: `192.168.1.150` & `192.168.1.151`).
   * Lệnh đổi IP tự động toàn bộ 4 máy trong 3 giây bằng script `/home/neko/change_ip.py`.
   * Checklist các bước đi thi giữa kỳ.

2. **[ON_TAP_LY_THUYET_GIUA_KI_QTDVM.md](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/quan-tri-dich-vu-mang/lab/ON_TAP_LY_THUYET_GIUA_KI_QTDVM.md)**:
   * Tài liệu ôn tập lý thuyết 5 câu hỏi trọng tâm thi giữa kỳ & cuối kỳ (IP Forwarding, BIND9 DNS, isc-dhcp-server, Apache2 VirtualHost & SSL, Samba & NFS).

3. **Các file script tiện ích sẵn có trong thư mục này**:
   * `setup_ubuntu1_router.sh`: Script cấu hình khởi tạo Ubuntu 1 (IP Forwarding, Netplan, DHCP, Apache).
   * `setup_ubuntu2_client.sh`: Script cấu hình Ubuntu 2 (Netplan, Static Route sang LAN 1).
   * `enable_telnet.bat`: Script bật dịch vụ Telnet Server và tắt tường lửa trên Windows 7.
   * `win7_1_set_ip.bat`: Script đặt IP tĩnh cho Win 7 máy 1.
   * `win7_2_set_ip.bat`: Script đặt IP tĩnh cho Win 7 máy 2.
   * `win7_switch_to_dhcp.bat`: Script chuyển Win 7 sang chế độ tự động nhận IP từ DHCP.
   * `test_ping_all.bat`: Script kiểm tra thông mạng giữa các máy.
