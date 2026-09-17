# 🚀 HƯỚNG DẪN QUẢN TRỊ MẠNG, ĐỔI IP TỰ ĐỘNG & CƠ CHẾ KẾT NỐI (GIỮA KỲ QTDVM)

Tài liệu này ghi nhớ toàn bộ kiến trúc 4 máy ảo, cơ chế giữ kết nối SSH/Telnet khi đổi IP và hướng dẫn sử dụng công cụ **tự động đổi toàn bộ dải IP 4 máy trong 3 giây**.

---

## 📌 1. KIẾN TRÚC MẠNG & THÔNG TIN 4 MÁY ẢO

Hệ thống được thiết kế theo đúng mô hình chuẩn bài thi & bài lab Quản trị dịch vụ mạng:

```
                  [ MÁY THẬT (HOST WINDOWS) ]
                               │
                VMnet8 (NAT - 192.168.1.0/24)
          ┌────────────────────┴────────────────────┐
          │ (ens33: 192.168.1.150)                  │ (ens33: 192.168.1.151)
   ┌──────┴──────┐                           ┌──────┴──────┐
   │ gk-ubuntu-1 │                           │ gk-ubuntu-2 │
   │   (Router)  │                           │  (Client)   │
   └──────┬──────┘                           └──────┬──────┘
          │ (ens37: 192.168.5.2)                    │ (ens37: 192.168.6.2)
          │                                         │
   VMnet2 (LAN 1)                            VMnet3 (LAN 2)
          │                                         │
          │ (ens41: 192.168.6.3)                    │
          └───────────────────┬─────────────────────┘
                              │
          ┌───────────────────┴─────────────────────┐
          │                                         │
   ┌──────┴──────┐                           ┌──────┴──────┐
   │  gk-win7-1  │                           │  gk-win7-2  │
   │   (LAN 1)   │                           │   (LAN 2)   │
   │192.168.5.11 │                           │192.168.6.10 │
   └─────────────┘                           └─────────────┘
```

### Thông tin đăng nhập & Cấu hình mạng chi tiết:

| Máy ảo | Card mạng | Kết nối VMnet | Địa chỉ IP mặc định | Tài khoản / Mật khẩu | Dịch vụ đang chạy |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **gk-ubuntu-1**<br>*(Router/Server)* | `ens33`<br>`ens37`<br>`ens41` | VMnet8 (NAT)<br>VMnet2 (LAN 1)<br>VMnet3 (LAN 2) | `192.168.1.150`<br>`192.168.5.2`<br>`192.168.6.3` | `neko` / `conmeo`<br>(Sudo: `conmeo`) | - SSH (Port 22)<br>- DHCP Server (`isc-dhcp-server`)<br>- Apache Web Portal (Port 80)<br>- IP Routing Forwarding (`1`) |
| **gk-ubuntu-2**<br>*(Linux Client)* | `ens33`<br>`ens37` | VMnet8 (NAT)<br>VMnet3 (LAN 2) | `192.168.1.151`<br>`192.168.6.2` | `neko` / `conmeo`<br>(Sudo: `conmeo`) | - SSH (Port 22)<br>- Route tĩnh sang LAN 1 qua `192.168.6.3` |
| **gk-win7-1**<br>*(Win Client 1)* | Card 1 | VMnet2 (LAN 1) | `192.168.5.11` (DHCP) | Windows 7 | - Telnet Server (Port 23)<br>- Firewall: OFF |
| **gk-win7-2**<br>*(Win Client 2)* | Card 1 | VMnet3 (LAN 2) | `192.168.6.10` (DHCP) | Windows 7 | - Telnet Server (Port 23)<br>- Firewall: OFF |

---

## ❓ 2. VÌ SAO KHI ĐỔI IP THÌ SSH & TELNET VẪN KẾT NỐI ĐƯỢC?

### A. Đối với Ubuntu 1 & Ubuntu 2 (SSH không bao giờ mất)
* Cả 2 máy Ubuntu đều có **Card mạng quản trị ngầm riêng biệt (`ens33` nối VMnet8 NAT)**:
  * Ubuntu 1: `192.168.1.150`
  * Ubuntu 2: `192.168.1.151`
* Khi vào phòng thi giáo viên yêu cầu đổi IP dải mạng bài thi (trên các card `ens37`, `ens41` ví dụ sang `172.16.x.x` hay `10.x.x.x`), **Card `ens33` hoàn toàn không bị thay đổi**.
* 👉 **Máy thật / AI vẫn SSH vào 150 và 151 thông suốt 100%**, giữ quyền điều khiển máy chủ mà không bao giờ sợ bị rớt mạng.

### B. Đối với 2 máy Windows 7 (Telnet vào IP mới trong 1 giây)
* Hai máy Win 7 nằm trong LAN 1 và LAN 2.
* **Ubuntu 1** đóng vai trò là Router kiêm DHCP Server:
  * Khi Win 7 nhận dải IP mới, Ubuntu 1 lập tức lưu IP đó vào `/var/lib/dhcp/dhcpd.leases` và bảng phân giải MAC `arp -n`.
  * AI hoặc người quản trị chỉ cần gõ lệnh sau trên Ubuntu 1 để thấy ngay IP mới của Win 7:
    ```bash
    cat /var/lib/dhcp/dhcpd.leases | grep "lease "
    # hoặc
    arp -n
    ```
  * Sau khi có IP mới, AI / Ubuntu 1 kết nối thẳng Telnet vào Win 7 qua cổng 23 để đẩy lệnh cấu hình.

---

## ⚡ 3. CÔNG CỤ TỰ ĐỘNG ĐỔI IP TRONG 3 GIÂY (`change_ip.py`)

Công cụ đã được cài sẵn trên Ubuntu 1 tại: `/home/neko/change_ip.py`.

### Cú pháp lệnh:
```bash
sudo python3 /home/neko/change_ip.py \
  --lan1-net <ĐỊA_CHỈ_MẠNG_LAN1> \
  --lan1-u1  <IP_UBUNTU1_TRÊN_LAN1> \
  --lan2-net <ĐỊA_CHỈ_MẠNG_LAN2> \
  --lan2-u1  <IP_UBUNTU1_TRÊN_LAN2> \
  --lan2-u2  <IP_UBUNTU2_TRÊN_LAN2>
```

### Ví dụ thực chiến khi đi thi:
Giả sử giáo viên phát đề bắt cấu hình dải mạng:
* **LAN 1**: `172.16.10.0/24` (IP Router Ubuntu 1: `172.16.10.1`)
* **LAN 2**: `172.16.20.0/24` (IP Router Ubuntu 1: `172.16.20.1`, IP Ubuntu 2: `172.16.20.2`)

Chỉ cần gõ **ĐÚNG 1 LỆNH**:
```bash
sudo python3 /home/neko/change_ip.py \
  --lan1-net 172.16.10.0 --lan1-u1 172.16.10.1 \
  --lan2-net 172.16.20.0 --lan2-u1 172.16.20.1 --lan2-u2 172.16.20.2
```

### Script sẽ tự động thực hiện 4 công việc sau:
1. **Sửa Netplan Ubuntu 1**: Gán IP mới cho `ens37` và `ens41` rồi gọi `netplan apply`.
2. **Sửa Netplan Ubuntu 2**: SSH ngầm qua `192.168.1.151`, gán IP mới cho `ens37` trên Ubuntu 2 và cập nhật route trỏ sang LAN 1 mới.
3. **Cập nhật DHCP Server**: Sửa file cấu hình `/etc/dhcp/dhcpd.conf` cấp dải IP mới và tự động khởi động lại `isc-dhcp-server`.
4. **Cập nhật Web Portal**: Tự tạo lại các file `.bat` cấu hình IP tĩnh trên cổng web `http://<IP_Ubuntu>/`.

---

## 💻 4. CÁCH ĐỔI IP TRÊN WINDOWS 7

### Trường hợp A: Đề bài yêu cầu dùng DHCP (Tự động)
* Không cần làm gì cả! Sau khi Ubuntu 1 đổi dải DHCP, Win 7 sẽ tự động nhận dải IP mới.
* Nếu muốn nhận ngay lập tức, vào CMD trên Win 7 gõ:
  ```cmd
  ipconfig /release
  ipconfig /renew
  ```

### Trường hợp B: Đề bài yêu cầu đặt IP TĨNH (Static IP)
Có 2 cách siêu nhanh không cần bấm chuột:

* **Cách 1 (Từ xa qua Telnet)**:
  Trên Ubuntu 1 hoặc máy Host, kết nối Telnet vào Win 7 và chạy:
  ```cmd
  netsh interface ip set address "Local Area Connection" static <IP_MỚI> <SUBNET_MASK> <GATEWAY>
  netsh interface ip set dns "Local Area Connection" static <DNS_SERVER>
  ```
* **Cách 2 (Qua trình duyệt Web Portal)**:
  Mở trình duyệt IE trên Win 7, truy cập vào IP của Ubuntu 1 (ví dụ: `http://192.168.5.2/`), tải file `set_static_w1.bat` hoặc `set_static_w2.bat` về và bấm chạy.

---

## 🎯 5. CHECKLIST ĐI THI GIỮA KỲ (1 PHÚT LÀ XONG TOÀN BỘ)

1. **Khởi động 4 máy ảo** trong VMware Workstation.
2. **Đọc đề bài**: Xác định dải mạng LAN 1, LAN 2 và IP của từng máy theo yêu cầu của đề.
3. **Chạy script đổi IP**:
   * Nhắn cho Antigravity hoặc mở terminal trên Ubuntu 1 chạy `sudo python3 /home/neko/change_ip.py ...`.
4. **Kiểm tra thông mạng 100%**:
   * Từ Ubuntu 1 gõ:
     ```bash
     ping -c 2 <IP_Ubuntu_2>
     ping -c 2 <IP_Win7_1>
     ping -c 2 <IP_Win7_2>
     ```
   * Từ Ubuntu 2 gõ:
     ```bash
     ping -c 2 <IP_Win7_1>
     ```
5. **Tiến hành làm tiếp các dịch vụ khác của đề thi** (DNS BIND9, Web Apache, Samba, NFS,...). Mọi thứ đều đã có nền tảng mạng vững chắc!
