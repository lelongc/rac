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

### 1.3 Quy trình 4 bước bắt tay cấp IP của DHCP (Quy tắc D.O.R.A - Câu hỏi thi vấn đáp):

Khi một máy Client bật lên hoặc cắm cáp mạng, quá trình xin cấp IP diễn ra qua 4 bước:

1. **`D` - DHCP DISCOVER (Broadcast):** Máy Client gửi gói tin broadcast (`255.255.255.255`) hỏi: *"Có DHCP Server nào trong mạng không, cho tôi xin 1 IP?"*.
2. **`O` - DHCP OFFER (Unicast/Broadcast):** DHCP Server nhận được và đề nghị một gói thông số: *"Tôi có IP 192.168.5.10 kèm Gateway và DNS này, bạn dùng không?"*.
3. **`R` - DHCP REQUEST (Broadcast):** Client phản hồi xác nhận: *"Tôi đồng ý thuê IP 192.168.5.10 này nhé!"*.
4. **`A` - DHCP ACKNOWLEDGE (Unicast):** DHCP Server chốt hợp đồng và phản hồi: *"Xác nhận! Bạn được phép dùng IP này trong thời gian thuê (Lease Time)!"*.

---

### 1.4 So sánh DHCP Thường (Direct) và DHCP Relay Agent:

| Tiêu chí | DHCP Thường (Direct DHCP) | DHCP Relay Agent |
| :--- | :--- | :--- |
| **Vị trí Server & Client** | Cùng chung một mạng LAN / Subnet | Khác mạng LAN, ngăn cách bởi Router |
| **Loại gói tin** | Toàn bộ là gói **Broadcast** | Chuyển đổi từ **Broadcast sang Unicast** |
| **Dịch vụ cài đặt** | `isc-dhcp-server` trên Server | Cài thêm `isc-dhcp-relay` trên Router |
| **Mục đích sử dụng** | Cấp phát trực tiếp trong mạng nội bộ | Dùng 1 DHCP Server tập trung cấp cho nhiều chi nhánh |


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

---

## 6. BỘ SCRIPT 1-CLICK TỰ ĐỘNG HÓA CHO CLIENT WINDOWS 7 (LOCAL SCRIPTS)

Để giúp bạn thao tác nhanh chóng và chính xác 100% trong phòng thi mà không cần nhớ lệnh mạng hay phải gõ tay:

### 6.1 Danh sách các file script tự động (`.bat`):
1. **[win7_switch_to_dhcp.bat](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/quan-tri-dich-vu-mang/lab/3-4/win7_switch_to_dhcp.bat)**:
   - **Chức năng:** Tự động chuyển card mạng sang DHCP, gửi lệnh `ipconfig /renew` để nhận IP từ Ubuntu 1 và in bảng IP mới ra màn hình.
   - **Cách dùng:** Click đúp chuột -> Bấm **Yes** khi UAC hỏi quyền Administrator.

2. **[win7_A_static.bat](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/quan-tri-dich-vu-mang/lab/3-4/win7_A_static.bat)** (Dành riêng cho máy Win7_A):
   - **Chức năng:** Tự động khôi phục IP tĩnh chuẩn cho Win7_A (`IP: 192.168.5.1`, `Subnet: 255.255.255.0`, `Gateway: 192.168.5.2`, `DNS: 192.168.5.2`).
   - **Cách dùng:** Click đúp chuột -> Bấm **Yes**.

3. **[win7_B_static.bat](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/quan-tri-dich-vu-mang/lab/3-4/win7_B_static.bat)** (Dành riêng cho máy Win7_B):
   - **Chức năng:** Tự động khôi phục IP tĩnh chuẩn cho Win7_B (`IP: 192.168.6.1`, `Subnet: 255.255.255.0`, `Gateway: 192.168.6.3`, `DNS: 192.168.5.2`).
   - **Cách dùng:** Click đúp chuột -> Bấm **Yes**.

4. **[win7_switch_to_static.bat](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/quan-tri-dich-vu-mang/lab/3-4/win7_switch_to_static.bat)** (Script tổng hợp có Menu lựa chọn):
   - **Chức năng:** Menu bấm phím `1` (cho Win7_A) hoặc phím `2` (cho Win7_B).

5. **[enable_telnet.bat](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/quan-tri-dich-vu-mang/lab/3-4/enable_telnet.bat)**:
   - **Chức năng:** Mở Telnet Server trên Windows 7 để điều khiển và kiểm tra từ xa.

---

### 6.2 Vị trí file trên màn hình Windows 7:
Tất cả các file script trên đã được đặt sẵn tại:
- **Desktop** và thư mục **Downloads** của tài khoản người dùng hiện tại.
- Thư mục gốc **`C:\Scripts\`** và **`C:\Users\Public\Documents\`**.
- Có thể tải lại bất kỳ lúc nào từ trình duyệt qua địa chỉ: `http://192.168.5.2/<tên_file>.bat`.

---

## 7. BÀI TOÁN NÂNG CAO: CẤU HÌNH DHCP RELAY AGENT (BÀI TẬP 6 IUH)

### 7.1 Tại sao cần DHCP Relay Agent? (Nguyên lý hoạt động)
- **Vấn đề thực tế:** Khi một doanh nghiệp có nhiều mạng con (Subnet A: `192.168.5.0/24`, Subnet B: `192.168.6.0/24`) ngăn cách nhau bởi Router, máy Client khi xin IP sẽ gửi gói tin **Broadcast (`255.255.255.255`)**. Theo nguyên tắc định tuyến, **Router sẽ chặn hoàn toàn các gói tin Broadcast**, khiến Client ở Subnet B không thể nhận IP từ DHCP Server đặt tại Subnet A.
- **Giải pháp:** Cài đặt dịch vụ **DHCP Relay Agent (`isc-dhcp-relay`)** ngay trên Router (hoặc một máy trung gian). Agent sẽ "nghe trộm" gói Broadcast của Client ở Subnet B, chuyển đổi nó thành gói **Unicast** rồi gửi thẳng đến địa chỉ IP của DHCP Server tại Subnet A, sau đó nhận kết quả IP trả ngược lại cho Client!

---

### 7.2 Hướng dẫn Cấu hình DHCP Relay Agent từng bước trên Router:

#### Bước 1: Cài đặt gói `isc-dhcp-relay` trên Router
Mở Terminal trên máy Router gõ:
```bash
sudo apt update
sudo apt install -y isc-dhcp-relay
```
*(Trong quá trình cài, nếu màn hình hỏi IP của DHCP Server thì điền IP của máy DHCP Server: `192.168.5.2`)*.

#### Bước 2: Cấu hình file `/etc/default/isc-dhcp-relay`
Mở file cấu hình:
```bash
sudo nano /etc/default/isc-dhcp-relay
```
Điền các thông số:
```ini
# Địa chỉ IP của máy DHCP Server
SERVERS="192.168.5.2"

# Danh sách các card mạng cần lắng nghe và chuyển tiếp (card nối subnet A và subnet B)
INTERFACES="ens37 ens38"

# Các tham số bổ sung (để trống)
OPTIONS=""
```
Lưu file (`Ctrl+O`, `Enter`, `Ctrl+X`).

#### Bước 3: Đảm bảo tính năng Định tuyến IP (IP Forwarding) đã bật
```bash
sudo sysctl -w net.ipv4.ip_forward=1
```

#### Bước 4: Khởi động và kiểm tra dịch vụ Relay
```bash
sudo systemctl restart isc-dhcp-relay
sudo systemctl enable isc-dhcp-relay
sudo systemctl status isc-dhcp-relay --no-pager
```

---

### 7.3 Kiểm tra kết quả xin cấp IP xuyên Router:
1. **Trên Client Windows (ở Subnet B):**
   ```cmd
   ipconfig /release
   ipconfig /renew
   ipconfig /all
   ```
   *(Kiểm tra máy nhận đúng IP trong dải Subnet B: `192.168.6.x` và DHCP Server hiển thị đúng IP `192.168.5.2`)*.

2. **Trên Client Linux (ở Subnet B):**
   ```bash
   sudo dhclient -r
   sudo dhclient -v
   ip a
   ```

---

### 7.4 Bảng đối chiếu 1-1 giữa Đề bài Word và Hệ thống 4 máy ảo thực tế của bạn:

| Thành phần trong Đề bài 6 | Dải IP ví dụ trong Đề Word | **DẢI IP CHUẨN CỦA BẠN (GIỮ NGUYÊN 100%)** | Máy ảo tương ứng |
| :--- | :--- | :--- | :--- |
| **Mạng Subnet A** | `192.168.1.0/24` (VMnet1) | **`192.168.5.0/24` (VMnet2)** | Mạng **LAN 1** |
| **Mạng Subnet B** | `10.10.10.0/24` (VMnet2) | **`192.168.6.0/24` (VMnet3)** | Mạng **LAN 2** |
| **DHCP Server** | IP: `192.168.1.1` | **IP: `192.168.5.2`** | **Ubuntu 1** |
| **Gateway Subnet A** | `192.168.1.254` | **`192.168.5.2`** (Card `ens37`) | **Ubuntu 1 (Router)** |
| **Gateway Subnet B** | `10.10.10.254` | **`192.168.6.3`** (Card `ens38`) | **Ubuntu 1 (Router)** |
| **DNS Server** | `203.113.131.1` | **`192.168.5.2`** | **DNS BIND9 trên Ubuntu 1** |
| **Domain Name** | `cse.hui.edu.vn` | **`tranduong.com`** | **Domain của bạn** |
| **Client Subnet A** | Host Windows / Linux A | **`Win7_A`** (IP tĩnh `192.168.5.1` hoặc DHCP) | Máy Win 7 1 |
| **Client Subnet B** | Host Windows / Linux B | **`Win7_B` & `Ubuntu 2`** (nhận `192.168.6.x`) | Máy Win 7 2 & LinuxB |
| **DHCP Relay (Mục 8)** | Cài trên Router | **Đã cài `isc-dhcp-relay` trên Ubuntu 1!** | Router Ubuntu 1 |



