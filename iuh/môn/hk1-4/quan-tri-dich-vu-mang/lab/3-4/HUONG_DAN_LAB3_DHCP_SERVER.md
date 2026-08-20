# HƯỚNG DẪN CHI TIẾT BÀI LAB 3: CÀI ĐẶT & CẤU HÌNH DHCP SERVER (ISC-DHCP-SERVER)

**Môn học:** Quản trị dịch vụ mạng (IUH)  
**Môi trường thực hành:** Hệ thống 4 máy ảo VMware (Ubuntu 1 đóng vai trò DHCP Server, Win7_A, Win7_B và Ubuntu_2 đóng vai trò DHCP Client)

---

## 1. TỔNG QUAN VỀ DỊCH VỤ DHCP SERVER

### 1.1 DHCP là gì và Mục đích của bài Lab?
- **DHCP (Dynamic Host Configuration Protocol)** là giao thức tự động cấu hình và cấp phát các thông số mạng (Địa chỉ IP, Subnet Mask, Default Gateway, DNS Server, Domain name) cho các máy trạm (Client) khi chúng khởi động hoặc kết nối vào mạng.
- **Mục đích bài Lab:** Biến máy **Ubuntu_1 (Router LinuxA)** thành **DHCP Server** để tự động cấp phát IP cho cả 2 dải mạng **LAN 1 (`VMnet2`)** và **LAN 2 (`VMnet3`)**, giúp các máy con **Win7_A, Win7_B, Ubuntu_2** không cần phải gõ IP tĩnh bằng tay mà vẫn tự nhận IP chuẩn và vào được Web `www.tranduong.com`!

### 1.2 Bảng quy hoạch dải cấp phát IP (DHCP Scope / Pool):

| Mạng LAN | Card mạng Server | Dải mạng (Subnet) | Dải IP cấp động (Range) | Default Gateway | DNS Server cấp kèm | Tên miền (Domain) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **LAN 1 (VMnet2)** | `ens37` | `192.168.5.0/24` | `192.168.5.10` - `192.168.5.50` | `192.168.5.2` | `192.168.5.2`, `8.8.8.8` | `tranduong.com` |
| **LAN 2 (VMnet3)** | `ens38` | `192.168.6.0/24` | `192.168.6.10` - `192.168.6.50` | `192.168.6.3` | `192.168.5.2`, `8.8.8.8` | `tranduong.com` |

---

## 2. CÀI ĐẶT & CẤU HÌNH TỰ ĐỘNG 1-CLICK (SCRIPT NHANH CHO PHÒNG THI)

Để cấu hình toàn bộ dịch vụ DHCP Server chỉ trong **10 giây**:

1. Copy file `setup_dhcp_server.sh` vào máy **Ubuntu_1**.
2. Phân quyền và chạy script:
   ```bash
   chmod +x setup_dhcp_server.sh
   sudo ./setup_dhcp_server.sh
   ```
*Script sẽ tự động cài đặt `isc-dhcp-server`, cấu hình card lắng nghe `ens37 ens38`, tạo dải cấp phát cho cả 2 mạng LAN, kiểm tra cú pháp và bật dịch vụ sẵn sàng 100%!*

---

## 3. HƯỚNG DẪN CẤU HÌNH THỦ CÔNG TỪNG BƯỚC TRÊN UBUNTU_1

### Bước 1: Cài đặt gói dịch vụ `isc-dhcp-server`
Mở Terminal trên **Ubuntu_1** gõ:
```bash
sudo apt update
sudo apt install -y isc-dhcp-server
```

---

### Bước 2: Khai báo các card mạng lắng nghe DHCP
Mở file `/etc/default/isc-dhcp-server`:
```bash
sudo nano /etc/default/isc-dhcp-server
```

Tìm dòng `INTERFACESv4` và điền tên 2 card mạng nối vào 2 mạng LAN:
```ini
INTERFACESv4="ens37 ens38"
INTERFACESv6=""
```
*(Lưu ý: `ens37` nối LAN 1, `ens38` nối LAN 2. Không điền card NAT `ens33` vào đây).*

Lưu file (`Ctrl+O`, `Enter`, `Ctrl+X`).

---

### Bước 3: Cấu hình dải cấp phát IP trong `/etc/dhcp/dhcpd.conf`
Mở file cấu hình chính:
```bash
sudo nano /etc/dhcp/dhcpd.conf
```

Nhập nội dung cấu hình chuẩn bên dưới:

```ini
# Thiết lập thời gian thuê IP (tính bằng giây)
default-lease-time 600;
max-lease-time 7200;
authoritative;

# ------------------------------------------------------------------------------
# 1. DẢI CẤP PHÁT MẠNG LAN 1 (VMnet2 - ens37)
# ------------------------------------------------------------------------------
subnet 192.168.5.0 netmask 255.255.255.0 {
    range 192.168.5.10 192.168.5.50;
    option routers 192.168.5.2;
    option subnet-mask 255.255.255.0;
    option broadcast-address 192.168.5.255;
    option domain-name "tranduong.com";
    option domain-name-servers 192.168.5.2, 8.8.8.8;
}

# ------------------------------------------------------------------------------
# 2. DẢI CẤP PHÁT MẠNG LAN 2 (VMnet3 - ens38)
# ------------------------------------------------------------------------------
subnet 192.168.6.0 netmask 255.255.255.0 {
    range 192.168.6.10 192.168.6.50;
    option routers 192.168.6.3;
    option subnet-mask 255.255.255.0;
    option broadcast-address 192.168.6.255;
    option domain-name "tranduong.com";
    option domain-name-servers 192.168.5.2, 8.8.8.8;
}

# ------------------------------------------------------------------------------
# 3. SUBSET NAT ĐỂ DHCP SERVER KHÔNG BÁO LỖI KHỞI ĐỘNG (ens33)
# ------------------------------------------------------------------------------
subnet 192.168.1.0 netmask 255.255.255.0 {
}
```

---

### Bước 4: Cấu hình gán IP cố định theo MAC (DHCP Reservation - Nếu thầy yêu cầu)
Nếu thầy yêu cầu: *"Cấu hình máy Win7_A khi xin IP tự động luôn nhận đúng địa chỉ `192.168.5.100`"*:
1. Mở CMD trên Win7_A gõ `getmac` (hoặc `ipconfig /all`) để lấy địa chỉ MAC vật lý (VD: `00:0c:29:aa:bb:cc`).
2. Thêm đoạn sau vào cuối file `/etc/dhcp/dhcpd.conf`:
   ```ini
   host win7a {
       hardware ethernet 00:0c:29:aa:bb:cc;
       fixed-address 192.168.5.100;
   }
   ```

---

### Bước 5: Kiểm tra cú pháp và Khởi động lại dịch vụ DHCP
1. Kiểm tra cú pháp (nếu không hiện lỗi là OK):
   ```bash
   sudo dhcpd -t -cf /etc/dhcp/dhcpd.conf
   ```
2. Khởi động lại dịch vụ:
   ```bash
   sudo systemctl restart isc-dhcp-server
   sudo systemctl enable isc-dhcp-server
   ```
3. Xem trạng thái dịch vụ:
   ```bash
   sudo systemctl status isc-dhcp-server
   ```
   *(Trạng thái báo `active (running)` màu xanh là thành công 100%)*.

---

## 4. HƯỚNG DẪN TEST NHẬN IP ĐỘNG TRÊN CÁC MÁY CLIENT (CHẤM ĐIỂM)

### 4.1 Thử nghiệm trên máy Windows 7 (Win7_A / Win7_B):

1. **Chuyển sang nhận IP tự động:**
   - Vào **Control Panel** -> **Network and Sharing Center** -> **Change adapter settings**.
   - Chuột phải **Local Area Connection** -> Chọn **Properties** -> Đúp chuột vào **Internet Protocol Version 4 (TCP/IPv4)**.
   - Chọn ô tròn thứ nhất: **`Obtain an IP address automatically`**.
   - Chọn tiếp: **`Obtain DNS server address automatically`**.
   - Bấm **OK** -> Bấm **OK**.

2. **Mở Command Prompt (cmd) trên Windows 7 để xin IP:**
   ```cmd
   ipconfig /release
   ipconfig /renew
   ipconfig /all
   ```

3. **Kiểm tra kết quả trên màn hình cmd:**
   - **IPv4 Address:** Tự nhận một IP trong dải `192.168.5.10` (đối với Win7_A) hoặc `192.168.6.10` (đối với Win7_B).
   - **Default Gateway:** `192.168.5.2` (hoặc `192.168.6.3`).
   - **DNS Servers:** `192.168.5.2`.
   - **DHCP Server:** `192.168.5.2` (hoặc `192.168.6.3`).

4. **Kiểm tra lướt Web:**
   - Mở Internet Explorer gõ `http://www.tranduong.com` -> Vào Web thành công mượt mà!

---

### 4.2 Thử nghiệm trên máy Ubuntu_2 (Linux Client):

1. Mở file Netplan trên Ubuntu_2:
   ```bash
   sudo nano /etc/netplan/00-installer-config.yaml
   ```
2. Chuyển card `ens37` (hoặc `ens33`) sang nhận DHCP:
   ```yaml
   network:
     version: 2
     renderer: networkd
     ethernets:
       ens37:
         dhcp4: yes
   ```
3. Áp dụng:
   ```bash
   sudo netplan apply
   ip a
   ```
   *(Kiểm tra card `ens37` sẽ tự động nhận một IP động trong dải `192.168.6.x`)*.

---

### 4.3 Cách quay trở lại IP Tĩnh cũ sau khi chấm điểm xong (5 giây):

- **Trên Windows 7:** Vào lại TCP/IPv4, chọn **Use the following IP address** và nhập lại IP cũ `192.168.5.1` (Gateway `192.168.5.2`, DNS `192.168.5.2`) -> Bấm OK.
- **Trên Ubuntu 2:** Mở lại file Netplan, dán lại cấu hình IP tĩnh cũ (`addresses: [192.168.6.2/24, 192.168.5.3/24]`) -> `sudo netplan apply`.

---

## 5. BỘ CẨM NANG XỬ LÝ LỖI DHCP SERVER (TROUBLESHOOTING)

### 🚨 5.1 Lỗi `Job for isc-dhcp-server.service failed` khi khởi động
- **Nguyên nhân 1:** Chưa khai báo card mạng trong `/etc/default/isc-dhcp-server`.
  - **Sửa:** Thêm `INTERFACESv4="ens37 ens38"`.
- **Nguyên nhân 2:** Quên khai báo subnet của card NAT (`192.168.1.0/24`) trong `dhcpd.conf` khiến DHCP Server từ chối chạy vì có card mạng chưa được định nghĩa subnet.
  - **Sửa:** Thêm đoạn `subnet 192.168.1.0 netmask 255.255.255.0 {}` vào cuối file `dhcpd.conf`.
- **Nguyên nhân 3:** Lỗi cú pháp (thiếu dấu chấm phẩy `;` ở cuối mỗi dòng).
  - **Kiểm tra:** Chạy lệnh `dhcpd -t -cf /etc/dhcp/dhcpd.conf` để xem chính xác dòng bị lỗi.

---

### 🚨 5.2 Lỗi Windows 7 nhận IP lạ `169.254.x.x` (APIPA)
- **Hiện tượng:** Gõ `ipconfig` trên Win 7 nhưng ra IP `169.254.x.x`.
- **Nguyên nhân:** Windows 7 không gửi được gói DHCP Discover tới Server (do sai card mạng VMware `VMnet2`/`VMnet3` hoặc DHCP Server chưa bật).
- **Khắc phục:**
  1. Kiểm tra máy Win 7 đã gắn đúng card `VMnet2` trong VMware Settings chưa.
  2. Trên Ubuntu 1 kiểm tra xem dịch vụ đã chạy chưa: `sudo systemctl status isc-dhcp-server`.

---

### 🔍 5.3 Cách xem danh sách các IP đã được cấp phát trên Ubuntu Server
Để xem máy nào vừa xin IP từ DHCP Server:
```bash
cat /var/lib/dhcp/dhcpd.leases
```
*(Màn hình sẽ hiển thị chi tiết IP đã cấp, địa chỉ MAC của máy xin IP, tên máy client và thời gian thuê IP).*
