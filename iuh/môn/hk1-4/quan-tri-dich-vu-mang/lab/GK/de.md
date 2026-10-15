# ĐỀ THI GIỮA KỲ & LỜI GIẢI CHI TIẾT (LÝ THUYẾT + THỰC HÀNH)

## MÔN: QUẢN TRỊ DỊCH VỤ MẠNG - KHOA CNTT - ĐH CÔNG NGHIỆP TP.HCM (IUH)

---

# PHẦN 1: NỘI DUNG NGUYÊN VĂN ĐỀ THI

```text
TRƯỜNG ĐẠI HỌC CÔNG NGHIỆP THÀNH PHỐ HỒ CHÍ MINH
KHOA: CNTT
Mẫu 3a: Đề tự luận giữa kỳ
ĐỀ THI GIỮA KỲ
Môn thi: Quản trị dịch vụ mạng
Lớp/Lớp học phần: DHCNTT19A
Thời gian làm bài: 60 phút (Không kể thời gian phát đề)
(Đề thi được sử dụng tài liệu giấy)
```

### **Câu 1: (3 điểm, CLO 2)** Cho mô hình mạng như sau:

```text
       [Host A Windows] (192.168.5.1)
              |
=== Mạng 192.168.5.0/24 (LAN 1) =========================
         |                                  |
     (eth0: 192.168.5.2)                (eth1: 192.168.5.3)
      [ Linux A ]                        [ Linux B ]
     (eth1: 192.168.6.3)                (eth0: 192.168.6.2)
         |                                  |
=== Mạng 192.168.6.0/24 (LAN 2) =========================
              |
       [Host B Windows] (192.168.6.1)
```

**Xây dựng hệ thống mạng với yêu cầu sau:**

- **a.** Máy chủ tên Ubuntu server, địa chỉ IP là `192.168.6.3/24` (ping thông các máy).
- **b.** Ubuntu server là máy điều khiển miền `abc.edu.vn` đồng thời làm máy chủ phân giải tên miền.

---

### **Câu 2: (7 điểm)**

Công ty abc có 100 người làm việc trong 3 phòng ban gồm: Phòng kế toán, phòng nhân sự, phòng đào tạo, trang thiết bị mạng của công ty gồm có: 2 server, 100 máy tính để bàn, 15 máy tính xách tay, 10 máy in, 2 máy photo, scan, cùng một số thiết bị Switch, Router... và công ty đã thực hiện kết nối mạng nội bộ (mạng LAN). Sử dụng địa chỉ mạng là `192.168.6.0/24` (trong đề ghi `192.168.6.3/24`) và dãy địa chỉ dành riêng cho các Server và giám đốc từ `192.168.6.3` đến `192.168.6.40`.

Hệ thống mạng LAN của công ty được mở rộng thêm network thứ 2 (LAN 2) với địa chỉ mạng là `10.10.10.0/24` và được kết nối với hệ thống LAN ban đầu (LAN 1) thông qua một Router mềm. DHCP Server trên LAN 1 không cấp được IP cho các máy trong LAN 2.

**Yêu cầu:**

- **a. (2 điểm, CLO 1)** Hãy đưa ra giải pháp phù hợp để cấp địa chỉ IP động cho hệ thống mạng LAN.
- **b. (2 điểm, CLO 1)** Giải thích đầy đủ nguyên lý hoạt động của dịch vụ DHCP được sử dụng trong giải pháp bạn chọn.
- **c. (3 điểm, CLO 2)** Cài đặt và triển khai DHCP relay agent mà đã đưa ra giải pháp (*câu c làm trên máy tính*).

---

---

# PHẦN 2: BÀI LÀM LÝ THUYẾT (CHÉP VÀO GIẤY THI - GỌN & ĐỦ Ý ĂN TRỌN ĐIỂM)

## CÂU 2a: GIẢI PHÁP CẤP PHÁT IP ĐỘNG CHO HỆ THỐNG MẠNG (2 ĐIỂM)

### 1. Nguyên nhân lỗi:

- Gói tin xin IP ban đầu (`DHCP Discover`) của máy trạm là gói **Broadcast** (`255.255.255.255`).
- Router mềm có vai trò phân tách Broadcast Domain để chống bão mạng nên **mặc định sẽ chặn (drop) toàn bộ gói Broadcast**, khiến DHCP Server ở LAN 1 không nhận được yêu cầu từ LAN 2.

### 2. Giải pháp lựa chọn:

- **Chọn giải pháp:** Cài đặt dịch vụ **DHCP Relay Agent** trên Router mềm nối giữa LAN 1 và LAN 2.
- **Lý do lựa chọn:**
  - **Tiết kiệm chi phí:** Tận dụng ngay Router mềm sẵn có, không cần đầu tư thêm máy chủ DHCP vật lý cho LAN 2.
  - **Quản trị tập trung:** Toàn bộ dải IP của các chi nhánh đều cấu hình và kiểm soát tập trung tại một DHCP Server duy nhất ở LAN 1.

### 3. Phân chia dải IP theo yêu cầu đề bài:

* **Mạng LAN 1 (`192.168.6.0/24`):**
  - Gateway / DNS Server: `192.168.6.3`
  - Dải IP tĩnh (dành riêng Server & Giám đốc): `192.168.6.3` đến `192.168.6.40`
  - Dải IP cấp phát động DHCP: `192.168.6.41` đến `192.168.6.254`
* **Mạng mở rộng LAN 2 (`10.10.10.0/24`):**
  - Gateway: `10.10.10.1` (IP interface của Router mềm ở LAN 2)
  - DNS Server: `192.168.6.3`
  - Dải IP cấp phát động DHCP qua Relay: `10.10.10.10` đến `10.10.10.250`

---

## CÂU 2b: NGUYÊN LÝ HOẠT ĐỘNG CỦA DHCP VÀ DHCP RELAY AGENT (2 ĐIỂM)

### 1. Cổng giao thức:

- Sử dụng giao thức **UDP**: Cổng **UDP 67** (DHCP Server & Relay Agent), cổng **UDP 68** (DHCP Client).

### 2. Sơ đồ chuyển đổi Broadcast -> Unicast qua Relay Agent:

```text
[ Client (LAN 2) ]          [ DHCP Relay Agent (Router) ]          [ DHCP Server (LAN 1) ]
       |                                  |                                  |
       |--- 1. DHCP Discover (Broadcast)->|                                  |
       |    (UDP 68 -> UDP 67)            |--- 1b. Gắn giaddr & Unicast ---->|
       |                                  |    (UDP 67 -> UDP 67)            |
       |                                  |                                  |
       |                                  |<-- 2. DHCP Offer (Unicast) ------|
       |<-- 2b. Chuyển tiếp Offer --------|                                  |
       |                                  |                                  |
       |--- 3. DHCP Request (Broadcast) ->|                                  |
       |                                  |--- 3b. Gắn giaddr & Unicast ---->|
       |                                  |                                  |
       |                                  |<-- 4. DHCP ACK (Unicast) --------|
       |<-- 4b. Chuyển tiếp ACK ----------|                                  |
       | (Nhận IP, GW, DNS hoàn tất)      |                                  |
```

### 3. Nguyên lý hoạt động 4 bước (D-O-R-A):

1. **Bước 1 - Khám phá (DHCP Discover):**Client gửi gói tin **Broadcast** tìm Server. Relay Agent trên Router chặn gói tin, ghi địa chỉ IP interface của mình (`10.10.10.1`) vào trường **`giaddr` (Gateway IP Address)**, rồi đóng gói thành **Unicast** gửi thẳng tới DHCP Server (`192.168.6.3`).
2. **Bước 2 - Đề nghị (DHCP Offer):**DHCP Server nhận gói tin, đọc trường `giaddr = 10.10.10.1` nên biết Client thuộc dải `10.10.10.0/24`. Server chọn một IP trống trong dải này và gửi **Unicast** trả về cho Relay Agent -> Relay Agent chuyển tiếp xuống Client.
3. **Bước 3 - Yêu cầu (DHCP Request):**Client gửi gói Request chấp nhận IP. Relay Agent tiếp tục bắt gói, chèn `giaddr` và gửi **Unicast** lên DHCP Server.
4. **Bước 4 - Xác nhận (DHCP ACK):**
   DHCP Server lưu thông tin cấp phát và gửi gói DHCP ACK (**Unicast**) về cho Relay Agent -> Relay Agent chuyển tiếp xuống Client để Client chính thức sử dụng IP.

---

# PHẦN 3: HƯỚNG DẪN CẤU HÌNH THỰC HÀNH TỪNG BƯỚC (CÂU 1 & CÂU 2c)

## BƯỚC 1: CẤU HÌNH IP VÀ BẬT ĐỊNH TUYẾN ROUTER (CÂU 1a)

### 1. Trên máy Ubuntu Server (Ubuntu 1 - `192.168.6.3` / `192.168.5.2`)

- **Kiểm tra card mạng:**
  - `ens37` (LAN 1): IP `192.168.5.2/24`
  - `ens41` (LAN 2): IP `192.168.6.3/24`
- **Bật tính năng Router (IP Forwarding):**
  ```bash
  sudo sysctl -w net.ipv4.ip_forward=1
  # Lưu vĩnh viễn vào /etc/sysctl.conf
  sudo sed -i 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/' /etc/sysctl.conf
  ```

---

## BƯỚC 2: CẤU HÌNH DNS SERVER BIND9 CHO MIỀN `abc.edu.vn` (CÂU 1b)

### 1. Khai báo Zone trong `/etc/bind/named.conf.local`:

```bash
sudo nano /etc/bind/named.conf.local
```

Nội dung:

```named
// Forward Zone: abc.edu.vn
zone "abc.edu.vn" {
    type master;
    file "/etc/bind/db.abc.edu.vn";
};

// Reverse Zone: 192.168.6.x
zone "6.168.192.in-addr.arpa" {
    type master;
    file "/etc/bind/db.192.168.6";
};
```

### 2. Tạo File cơ sở dữ liệu Forward `/etc/bind/db.abc.edu.vn`:

```named
$TTL    604800
@       IN      SOA     ns.abc.edu.vn. admin.abc.edu.vn. (
                              2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@       IN      NS      ns.abc.edu.vn.
ns      IN      A       192.168.6.3
server  IN      A       192.168.6.3
@       IN      A       192.168.6.3
www     IN      CNAME   abc.edu.vn.
mail    IN      A       192.168.6.3
router  IN      A       192.168.6.3
```

### 3. Tạo File cơ sở dữ liệu Reverse `/etc/bind/db.192.168.6`:

```named
$TTL    604800
@       IN      SOA     ns.abc.edu.vn. admin.abc.edu.vn. (
                              2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@       IN      NS      ns.abc.edu.vn.
3       IN      PTR     ns.abc.edu.vn.
3       IN      PTR     server.abc.edu.vn.
3       IN      PTR     abc.edu.vn.
```

### 4. Kiểm tra cú pháp và khởi động lại DNS Server:

```bash
sudo named-checkconf
sudo named-checkzone abc.edu.vn /etc/bind/db.abc.edu.vn
sudo named-checkzone 6.168.192.in-addr.arpa /etc/bind/db.192.168.6
sudo systemctl restart bind9
```

### 5. Kiểm thử phân giải tên miền:

```bash
nslookup abc.edu.vn 127.0.0.1
nslookup www.abc.edu.vn 127.0.0.1
nslookup 192.168.6.3 127.0.0.1
```

---

## BƯỚC 3: CẤU HÌNH DHCP SERVER & DHCP RELAY AGENT (CÂU 2c)

### 1. Cấu hình DHCP Server (Trên máy Ubuntu 1 - `192.168.6.3`)

Mở file `/etc/dhcp/dhcpd.conf`:

```bash
sudo nano /etc/dhcp/dhcpd.conf
```

Nội dung cấu hình chuẩn:

```dhcpd
default-lease-time 600;
max-lease-time 7200;
authoritative;

# ==========================================
# 1. SUBNET LAN 1 (192.168.6.0/24)
# ==========================================
subnet 192.168.6.0 netmask 255.255.255.0 {
    # Dãy cấp phát động (tránh dải tĩnh 192.168.6.3 -> 192.168.6.40)
    range 192.168.6.41 192.168.6.254;
    option subnet-mask 255.255.255.0;
    option routers 192.168.6.3;
    option domain-name-servers 192.168.6.3, 8.8.8.8;
    option domain-name "abc.edu.vn";
}

# ==========================================
# 2. SUBNET LAN 2 (10.10.10.0/24) QUA RELAY
# ==========================================
subnet 10.10.10.0 netmask 255.255.255.0 {
    range 10.10.10.10 10.10.10.250;
    option subnet-mask 255.255.255.0;
    option routers 10.10.10.1;
    option domain-name-servers 192.168.6.3, 8.8.8.8;
    option domain-name "abc.edu.vn";
}

# Subnet phụ mạng NAT nếu có (để dhcpd không báo lỗi thiếu subnet ens33)
subnet 192.168.1.0 netmask 255.255.255.0 {
}

# Subnet phụ LAN 5 nếu có card ens37
subnet 192.168.5.0 netmask 255.255.255.0 {
    range 192.168.5.10 192.168.5.50;
    option routers 192.168.5.2;
}
```

Khai báo card mạng lắng nghe trong `/etc/default/isc-dhcp-server`:

```bash
sudo sed -i 's/INTERFACESv4=.*/INTERFACESv4="ens37 ens41"/' /etc/default/isc-dhcp-server
sudo systemctl restart isc-dhcp-server
```

---

### 2. Cấu hình DHCP Relay Agent (Trên Router Mềm / Ubuntu 2)

Cài đặt gói:

```bash
sudo apt update && sudo apt install -y isc-dhcp-relay
```

Cấu hình file `/etc/default/isc-dhcp-relay`:

```bash
# Địa chỉ IP của máy chủ DHCP Server chính
SERVERS="192.168.6.3"

# Các card mạng tham gia Relay (card nối tới DHCP Server và card nối tới Client)
INTERFACES="ens37 ens41"

OPTIONS=""
```

Khởi động lại dịch vụ:

```bash
sudo systemctl restart isc-dhcp-relay
sudo systemctl enable isc-dhcp-relay
```

Bật IP Forwarding trên Router:

```bash
sudo sysctl -w net.ipv4.ip_forward=1
```

---

### 3. Kiểm thử trên máy Client (Windows 7 hoặc Ubuntu Client)

- **Trên Windows 7:**
  ```cmd
  ipconfig /release
  ipconfig /renew
  ipconfig /all
  nslookup abc.edu.vn 192.168.6.3
  ping abc.edu.vn
  ```
- **Trên Ubuntu Client:**
  ```bash
  sudo dhclient -r
  sudo dhclient -v
  ip a
  dig @192.168.6.3 abc.edu.vn
  ```

---

---
