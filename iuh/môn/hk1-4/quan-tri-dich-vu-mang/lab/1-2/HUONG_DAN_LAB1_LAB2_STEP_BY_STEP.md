# HƯỚNG DẪN CHI TIẾT BÀI LAB 1 & LAB 2: MẠNG NÂNG CAO & DNS SERVER BIND9

**Môn học:** Quản trị dịch vụ mạng (IUH)
**Môi trường thử nghiệm:** Chuẩn **4 máy ảo** (2 Máy ảo Windows 7 + 2 Máy ảo Ubuntu 22.04 LTS Server)

---

## 1. TỔNG QUAN DANH SÁCH 4 MÁY ÁO & SƠ ĐỒ MẠNG

Hệ thống gồm đúng **4 máy ảo** chạy trên VMware Workstation:

1. **Win7_A (Host A):** Windows 7 SP1 - Client thuộc dải mạng LAN 1 (`192.168.5.0/24`).
2. **Ubuntu_1 (LinuxA):** Ubuntu 22.04 LTS Server - Đóng vai trò **Router** + **DNS Server BIND9** (Gồm 2 card mạng nối LAN 1 và LAN 2).
3. **Ubuntu_2 (LinuxB):** Ubuntu 22.04 LTS Server - Đóng vai trò **Client/Slave** (Gồm 1 card mạng gán **IP Alias** 2 IP để thuộc cả 2 mạng).
4. **Win7_B (Host B):** Windows 7 SP1 - Client thuộc dải mạng LAN 2 (`192.168.6.0/24`).

### Sơ đồ mạng tổng thể 4 máy:

```text
 [ Win7_A (Host A) ] (IP: 192.168.5.1/24)
          │
          ├────────────────────────── LAN 1 (VMnet2: 192.168.5.0/24) ──────────────────────────┐
          │                                                                                   │
 [ Ubuntu_1 (LinuxA) ] (ens33: 192.168.5.2)                                          [ Ubuntu_2 (LinuxB) ]
 (ens37: 192.168.6.3) ──┐                                                            (ens33:0 IP Alias: 192.168.5.3)
                        │                                                                     │
                        └── LAN 2 (VMnet3: 192.168.6.0/24) ─── [ Ubuntu_2 (ens33: 192.168.6.2) ]
                                                                                              │
                                                                                     [ Win7_B (Host B) ] (IP: 192.168.6.1/24)
```

### Bảng phân bổ thông số IP và Card mạng 4 máy:

| STT | Tên Máy ảo      | Hệ điều hành | Card mạng VMware                                                                          | Tên Interface trong OS                                                                               | Địa chỉ IP / Subnet                                     | Vai trò / Dịch vụ |
| :-- | :----------------- | :--------------- | :----------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- | :--------------------------------------------------------- | :------------------- |
| 1   | **Win7_A**   | Windows 7 SP1    | Custom (`VMnet2`)                                                                        | Local Area Connection                                                                                 | `192.168.5.1/24`                                         | Host A Client        |
| 2   | **Ubuntu_1** | Ubuntu 22.04     | Card 1: NAT (`VMnet8`)<br />Card 2: Custom (`VMnet2`)<br />Card 3: Custom (`VMnet3`) | `ens33`: `192.168.1.150/24`<br />`ens37`: `192.168.5.2/24`<br />`ens38`: `192.168.6.3/24` | LinuxA Router &**DNS Server BIND9** (SSH & Internet) |                      |
| 3   | **Ubuntu_2** | Ubuntu 22.04     | Card 1: Custom (`VMnet3`)                                                                | `ens33`: `192.168.6.2/24`<br />`ens33:0` (Alias): `192.168.5.3/24`                            | LinuxB Client / DNS Client                                 |                      |
| 4   | **Win7_B**   | Windows 7 SP1    | Custom (`VMnet3`)                                                                        | Local Area Connection                                                                                 | `192.168.6.1/24`                                         | Host B Client        |

---

## 2. BÀI LAB 1: CẤU HÌNH KẾT NỐI 4 MÁY TRÊN 2 SUBNET KHÁC NHAU (DUAL NIC & IP ALIAS)

### 2.1 Cấu hình mạng VMware Workstation (VMnet2 & VMnet3)

1. Trên VMware Workstation: Vào **Edit** -> **Virtual Network Editor...** -> Bấm **Change Settings**.
2. **Tạo Mạng LAN 1 (`VMnet2`):**
   - Chọn **Add Network...** -> Chọn **`VMnet2`** -> Chọn kiểu **Host-only** (Custom).
   - Bỏ chọn *Use local DHCP service...*
   - Subnet IP: **`192.168.5.0`**, Mask: `255.255.255.0`.
3. **Tạo Mạng LAN 2 (`VMnet3`):**
   - Chọn **Add Network...** -> Chọn **`VMnet3`** -> Chọn kiểu **Host-only** (Custom).
   - Bỏ chọn *Use local DHCP service...*
   - Subnet IP: **`192.168.6.0`**, Mask: `255.255.255.0`.
4. **Gán Card mạng vào 4 máy:**
   - **Win7_A**: Gán vào **`VMnet2`**.
   - **Ubuntu_1 (LinuxA)**: Gán Card 1 vào **NAT (`VMnet8`)**, Card 2 vào **`VMnet2`**, Card 3 vào **`VMnet3`**.
   - **Ubuntu_2 (LinuxB)**: Gán Card 1 vào **`VMnet3`**.
   - **Win7_B**: Gán vào **`VMnet3`**.

---

### 2.2 Cấu hình 2 máy Windows 7 (Win7_A & Win7_B)

#### Trên máy Win7_A (Host A):

1. Vào **Control Panel** -> **Network and Sharing Center** -> **Change adapter settings**.
2. Chuột phải vào **Local Area Connection** -> **Properties** -> Chọn **Internet Protocol Version 4 (TCP/IPv4)**.
3. Nhập IP:
   - **IP address**: `192.168.5.1`
   - **Subnet mask**: `255.255.255.0`
   - **Default gateway**: `192.168.5.2`
   - **Preferred DNS server**: `192.168.5.2`

#### Trên máy Win7_B (Host B):

1. Thao tác tương tự trên máy Win7_B.
2. Nhập IP:
   - **IP address**: `192.168.6.1`
   - **Subnet mask**: `255.255.255.0`
   - **Default gateway**: `192.168.6.2` (hoặc `192.168.6.3`)
   - **Preferred DNS server**: `192.168.5.2`

---

### 2.3 Cấu hình Ubuntu_1 (LinuxA) - 3 Card Mạng (NAT + Dual NIC Router + DNS Server)

Trên **Ubuntu_1 (LinuxA)**, máy đóng vai trò làm **Router kết nối 2 dải mạng** + **DNS Server BIND9**:

- **Card 1 (`ens33`)**: Nối **NAT (`VMnet8`)** - IP `192.168.1.150/24` (Dùng để kết nối SSH từ máy thật Windows `ssh neko@192.168.1.150` và tải gói ứng dụng từ Internet).
- **Card 2 (`ens37`)**: Nối **LAN 1 (`VMnet2`)** - IP tĩnh `192.168.5.2/24` (Nối Win7_A).
- **Card 3 (`ens38`)**: Nối **LAN 2 (`VMnet3`)** - IP tĩnh `192.168.6.3/24` (Nối Win7_B & Ubuntu_2).

---

#### 📝 FILE CẤU HÌNH NETPLAN CHUẨN HOÀN CHỈNH CHO UBUNTU_1:

Mở file Netplan trên màn hình Ubuntu_1:

```bash
sudo nano /etc/netplan/00-installer-config.yaml
```

Nhập nội dung cấu hình chuẩn bên dưới:

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    # --- CARD 1 (ens33): NAT (VMnet8) - DÙNG CHO SSH VÀ INTERNET ---
    ens33:
      dhcp4: no
      addresses:
        - 192.168.1.150/24
      routes:
        - to: default
          via: 192.168.1.2
      nameservers:
        addresses: [8.8.8.8, 1.1.1.1]

    # --- CARD 2 (ens37): LAN 1 (VMnet2) - IP NỐI WIN7_A ---
    ens37:
      dhcp4: no
      addresses:
        - 192.168.5.2/24

    # --- CARD 3 (ens38): LAN 2 (VMnet3) - IP NỐI WIN7_B & UBUNTU_2 ---
    ens38:
      dhcp4: no
      addresses:
        - 192.168.6.3/24
```

Lưu file (`Ctrl+O`, `Enter`, `Ctrl+X`) rồi áp dụng:

```bash
sudo chmod 600 /etc/netplan/00-installer-config.yaml
sudo netplan apply
```

---

#### 🛠️ BẬT DỊCH VỤ SSH VÀ IP FORWARDING TRÊN UBUNTU_1:

Gõ các lệnh sau trên Ubuntu_1:

```bash
# Bật SSH và tắt tường lửa
sudo apt update && sudo apt install -y openssh-server
sudo ufw disable
sudo systemctl enable --now ssh

# Bật định tuyến IP Forwarding để 2 mạng LAN 1 và LAN 2 thông nhau
sudo sysctl -w net.ipv4.ip_forward=1
echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

---

#### 💻 KẾT NỐI SSH TỪ WINDOWS MÁY THẬT VÀO UBUNTU_1:

Mở cửa sổ **PowerShell** trên máy tính thật Windows của bạn và gõ:

```powershell
ssh neko@192.168.1.150
```

*(Nhập mật khẩu: `conmeo` hoặc mật khẩu máy Ubuntu của bạn).*

---

### 2.4 Cấu hình Ubuntu_2 (LinuxB) - Dual Card Mạng & Chuẩn hóa 1 Card khi Nộp bài

---

#### 📌 GIAI ĐOẠN 1: KHI CẦN TẢI PHẦN MỀM & SSH TỪ MÁY THẬT (DÙNG 2 CARD)

Trong quá trình thực hành ban đầu, Ubuntu_2 cần kết nối Internet để tải các gói bổ trợ và kết nối SSH từ máy thật:
- **Card 1 (`ens33`)**: NAT (`VMnet8`) - IP `192.168.1.151/24` (Dùng cho SSH máy thật & Internet).
- **Card 2 (`ens37`)**: Custom (`VMnet3` - LAN 2) - Gán 2 IP:
  - **IP chính**: `192.168.6.2/24` (Client dải LAN 2)
  - **IP Alias**: `192.168.5.3/24` (IP phụ dải LAN 1 để kết nối thẳng với Win7_A `192.168.5.1`)

**File Netplan Giai đoạn 1 (`/etc/netplan/00-installer-config.yaml`):**
```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    # --- CARD 1 (ens33): NAT (VMnet8) - DÙNG CHO SSH VÀ INTERNET ---
    ens33:
      dhcp4: no
      addresses:
        - 192.168.1.151/24
      routes:
        - to: default
          via: 192.168.1.2
      nameservers:
        addresses: [192.168.5.2, 8.8.8.8]

    # --- CARD 2 (ens37): LAN 2 (VMnet3) - IP CHÍNH VÀ IP ALIAS ---
    ens37:
      dhcp4: no
      addresses:
        - 192.168.6.2/24 # IP chính dải LAN 2
        - 192.168.5.3/24 # IP Alias (phụ) dải LAN 1
```

Áp dụng: `sudo chmod 600 /etc/netplan/00-installer-config.yaml && sudo netplan apply`

---

#### 🏆 GIAI ĐOẠN 2: CẤU HÌNH LẠI SAU KHI XÓA CARD NAT (CHUẨN 100% NỘP BÀI CHO THẦY)

Theo đúng sơ đồ đề bài Lab của giảng viên, **Ubuntu_2 chỉ có DUY NHẤT 1 card mạng nội bộ LAN 2** mang 2 IP (IP chính `192.168.6.2` + IP Alias `192.168.5.3`).

##### Bước 1: Xóa Card NAT trên VMware Workstation
1. Chuột phải vào máy ảo **Ubuntu_2** trên VMware -> Chọn **Settings...**
2. Chọn **Network Adapter** (Card 1 - NAT `VMnet8`).
3. Bấm nút **Remove** ở góc dưới cùng -> Bấm **OK**.

##### Bước 2: Kiểm tra tên card thực tế trên màn hình Ubuntu_2
Mở terminal Ubuntu_2 gõ:
```bash
ip a
```
*(Kiểm tra xem card mạng hiển thị là `ens37` hay `ens33`)*.

##### Bước 3: Cập nhật file Netplan chuẩn 1 Card duy nhất
Mở file:
```bash
sudo nano /etc/netplan/00-installer-config.yaml
```

Nhập cấu hình sạch đẹp chuẩn 100% đề bài:
```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    # Card mạng nội bộ duy nhất (Nếu ip a hiện ens33 thì đổi ens37 thành ens33)
    ens37:
      dhcp4: no
      addresses:
        - 192.168.6.2/24 # IP chính dải LAN 2
        - 192.168.5.3/24 # IP Alias dải LAN 1
      nameservers:
        addresses: [192.168.6.3] # Trỏ trực tiếp về DNS Server Ubuntu 1
        search: [tranduong.com]
```

Lưu file (`Ctrl+O`, `Enter`, `Ctrl+X`) rồi áp dụng:
```bash
sudo chmod 600 /etc/netplan/00-installer-config.yaml
sudo netplan apply
echo "nameserver 192.168.6.3" | sudo tee /etc/resolv.conf
```

##### Bước 4: Kiểm tra phân giải tên miền và SSH Jump
1. **Kiểm tra DNS:** `nslookup www.tranduong.com` -> Trả về `192.168.5.2` thành công!
2. **Quản lý SSH Jump từ Windows máy thật:**
   - SSH vào Router Ubuntu_1: `ssh neko@192.168.1.150`
   - Từ trong Ubuntu_1, SSH nhảy sang Ubuntu_2: `ssh neko@192.168.6.2` (hoặc `ssh neko@192.168.5.3`).

---

### 2.5 Bật định tuyến IP Forwarding & Kiểm tra Ping 4 máy

1. Bật định tuyến gói tin trên cả **Ubuntu_1** và **Ubuntu_2**:

   ```bash
   sudo sysctl -w net.ipv4.ip_forward=1
   echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf
   sudo sysctl -p
   ```
2. **Kiểm tra ping giữa 4 máy:**

   - Từ **Ubuntu_2** (`192.168.1.151`): `ping 192.168.6.3` (Ubuntu_1) -> Kết quả: `0% packet loss` (Thành công thông suốt!).
   - Từ **Win7_A** (`192.168.5.1`): `ping 192.168.5.2` (Ubuntu_1) -> `ping 192.168.5.3` (IP Alias Ubuntu_2) -> `ping 192.168.6.1` (Win7_B).
   - Tất cả 4 máy ping thấy nhau thông suốt là hoàn thành **BÀI LAB 1**.

---

## 3. BÀI LAB 2: CÀI ĐẶT VÀ CẤU HÌNH DNS SERVER BIND9 (PHÂN GIẢI DOMAIN `tranduong.com`)

Trong bài này, máy **Ubuntu_1** (`192.168.5.2` / `192.168.6.3`) đóng vai trò **DNS Server BIND9** phân giải tên miền **`tranduong.com`**.

### 3.1 Cài đặt BIND9 tự động bằng 1 dòng lệnh (Script 1-Click)

Trên máy **Ubuntu_1**, tải và chạy script tự động cấu hình BIND9:

```bash
sudo ./setup_dns_server.sh
```

```bash
sudo apt update
sudo apt install -y bind9 bind9utils bind9-doc dnsutils
```

*(Nếu dùng gói đĩa offline `.deb` trong phòng thực hành: `cd /mnt/DNS/ && sudo dpkg -i *.deb`)*

---

### 3.2 Cấu hình khai báo Zone `tranduong.com` (`named.conf.default-zones`)

Mở file khai báo zone chính của BIND9:

```bash
sudo nano /etc/bind/named.conf.default-zones
```

Thêm đoạn khai báo Zone phân giải xuôi cho tên miền **`tranduong.com`** vào cuối file:

```named
zone "tranduong.com" {
    type master;
    file "/etc/bind/db.tranduong.com";
};
```

---

### 3.3 Tạo file dữ liệu Zone `db.tranduong.com` (Bản ghi SOA, NS, A)

1. Sao chép từ file mẫu `db.local`:

   ```bash
   sudo cp /etc/bind/db.local /etc/bind/db.tranduong.com
   ```
2. Mở file để chỉnh sửa các bản ghi DNS:

   ```bash
   sudo nano /etc/bind/db.tranduong.com
   ```
3. Nhập nội dung file theo đúng yêu cầu đề bài:

   ```named
   ;
   ; BIND data file for zone tranduong.com
   ;
   $TTL    604800
   @       IN      SOA     ns.tranduong.com. root.tranduong.com. (
                                 2         ; Serial
                            604800         ; Refresh
                             86400         ; Retry
                           2419200         ; Expire
                            604800 )       ; Negative Cache TTL
   ;
   ; Khai báo Name Server
   @       IN      NS      ns.tranduong.com.

   ; Khai báo các bản ghi A (Tên miền -> Địa chỉ IP)
   ns      IN      A       192.168.5.2
   www     IN      A       192.168.5.2
   ftp     IN      A       10.10.10.1
   mail    IN      A       192.168.5.2
   win7a   IN      A       192.168.5.1
   win7b   IN      A       192.168.6.1
   ubuntu2 IN      A       192.168.6.2
   ```

*(Lưu ý: Nếu đề bài trên lớp yêu cầu dùng dải IP `192.168.1.20` thì bạn chỉ cần đổi số IP `192.168.5.2` thành `192.168.1.20` tương ứng).*

---

### 3.4 Khởi động dịch vụ và kiểm tra bằng `named-checkzone`

1. **Kiểm tra cú pháp file cấu hình (không hiện lỗi là OK):**

   ```bash
   sudo named-checkconf
   sudo named-checkzone tranduong.com /etc/bind/db.tranduong.com
   ```

   *(Kết quả báo: `zone tranduong.com/IN: loaded serial 2 - OK`)*
2. **Khởi động lại dịch vụ BIND9:**

   ```bash
   sudo systemctl restart bind9
   sudo systemctl enable bind9
   ```
3. **Kiểm tra trạng thái:**

   ```bash
   sudo systemctl status bind9
   ```

---

### 3.5 Cấu hình DNS Client trên Ubuntu_2 & 2 máy Win 7 để Test (`nslookup`)

#### 1. Trên máy Ubuntu_2 (LinuxB):

Sửa file Netplan `/etc/netplan/00-installer-config.yaml`, trỏ `nameservers` về IP của **Ubuntu_1** (`192.168.5.2`):

```yaml
nameservers:
  addresses: [192.168.5.2]
  search: [tranduong.com]
```

Áp dụng: `sudo netplan apply`

Mở Terminal trên **Ubuntu_2** gõ lệnh kiểm tra phân giải tên miền:

```bash
nslookup ns.tranduong.com
```

**Kết quả màn hình hiển thị thành công:**

```text
Server:         192.168.5.2
Address:        192.168.5.2#53

Name:   ns.tranduong.com
Address: 192.168.5.2
```

#### 2. Trên 2 máy Windows 7 (Win7_A & Win7_B):

Mở **cmd** gõ:

```cmd
nslookup ns.tranduong.com
ping ns.tranduong.com
ping www.tranduong.com
```

Kết quả: Cả 2 máy Win 7 đều phân giải thành công từ tên miền `ns.tranduong.com` ra địa chỉ IP `192.168.5.2` của máy DNS Server!

---

## 4. BỘ SCRIPT TỰ ĐỘNG CẤU HÌNH 1-CLICK (LOCAL SCRIPTS)

Để giúp bạn cấu hình nhanh chóng toàn bộ Server **Ubuntu_1** (`192.168.5.2`) chỉ bằng 1 dòng lệnh mà không lo gõ sai cú pháp:

### 4.1 Script tự động cấu hình DNS Server BIND9 (`setup_dns_server.sh`)
```bash
chmod +x setup_dns_server.sh
sudo ./setup_dns_server.sh
```
*Script sẽ tự động cài đặt BIND9, tạo file zone `tranduong.com`, thêm các bản ghi `ns`, `www`, `ftp`, `mail` và restart dịch vụ hoàn toàn tự động!*

### 4.2 Script tự động cấu hình Apache2 Web Server HTTP (`setup_web_server.sh`)
```bash
chmod +x setup_web_server.sh
sudo ./setup_web_server.sh
```
*Script sẽ tự động cài đặt Apache2, làm sạch nguồn apt, tạo trang Web mẫu tuyệt đẹp cho `www.tranduong.com` và bật dịch vụ Web Server sẵn sàng cho bài Lab!*

### 4.3 Script tự động cấu hình Apache2 HTTPS SSL/TLS (`setup_https_server.sh`)
```bash
chmod +x setup_https_server.sh
sudo ./setup_https_server.sh
```
*Script sẽ tự động tạo chứng chỉ SSL Self-Signed 2048-bit, bật VirtualHost Port 443 HTTPS, và tự động chuyển hướng (Redirect 301) tất cả truy cập từ HTTP (Port 80) sang HTTPS (Port 443)!*

### 4.4 Script tự động cấu hình Bảo mật Mật khẩu Web (`setup_auth_web_server.sh`)
```bash
chmod +x setup_auth_web_server.sh
sudo ./setup_auth_web_server.sh
```
*Script sẽ tự động cài gói `apache2-utils`, khởi tạo file mã hóa `.htpasswd` chứa 2 tài khoản thử nghiệm (`admin`/`123456` và `tranduong`/`123456`), tạo khu vực bảo mật `/var/www/html/private/` và bắt buộc người dùng nhập đúng tài khoản mật khẩu mới được phép truy cập!*

---

## 5. HƯỚNG DẪN CẤU HÌNH HTTPS (SSL/TLS CERTIFICATE) CHO APACHE2 WEB SERVER

### 5.1 Khái niệm Chứng chỉ SSL Self-Signed
Trong môi trường Lab nội bộ, chúng ta tự tạo **Chứng chỉ SSL Self-Signed (Tự ký)** bằng công cụ `openssl` để mã hóa toàn bộ dữ liệu trao đổi giữa Trình duyệt Web client và Apache2 Server qua giao thức mã hóa **HTTPS (Port 443)**.

### 5.2 Các bước cấu hình thủ công:

1. **Kích hoạt module SSL và cấu hình OpenSSL hỗ trợ TLS cho mọi Client:**
   ```bash
   sudo a2enmod ssl
   sudo a2enmod headers
   # Hạ SECLEVEL xuống 0 để hỗ trợ cả Internet Explorer trên Windows 7
   sudo sed -i 's/CipherString = DEFAULT:@SECLEVEL=2/CipherString = DEFAULT:@SECLEVEL=0/g' /etc/ssl/openssl.cnf
   sudo sed -i 's/SSLProtocol all -SSLv3/SSLProtocol all +TLSv1 +TLSv1.1 +TLSv1.2/g' /etc/apache2/mods-available/ssl.conf
   sudo sed -i 's/SSLCipherSuite HIGH:!aNULL/SSLCipherSuite ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+EXP:@SECLEVEL=0/g' /etc/apache2/mods-available/ssl.conf
   ```

2. **Tạo Chứng chỉ SSL Self-Signed 2048-bit cho domain `www.tranduong.com`:**
   ```bash
   sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
     -keyout /etc/ssl/private/tranduong.key \
     -out /etc/ssl/certs/tranduong.crt \
     -subj "/C=VN/ST=HCM/L=TPHCM/O=IUH/OU=QTMANGB2/CN=www.tranduong.com" \
     -addext "subjectAltName=DNS:www.tranduong.com,DNS:tranduong.com,IP:192.168.5.2"
   sudo chmod 600 /etc/ssl/private/tranduong.key
   sudo chmod 644 /etc/ssl/certs/tranduong.crt
   ```

3. **Cấu hình VirtualHost HTTPS (Port 443) `/etc/apache2/sites-available/tranduong-ssl.conf`:**
   ```apache
   <IfModule mod_ssl.c>
   <VirtualHost *:443>
       ServerAdmin webmaster@tranduong.com
       ServerName www.tranduong.com
       ServerAlias tranduong.com
       DocumentRoot /var/www/html

       SSLEngine on
       SSLCertificateFile /etc/ssl/certs/tranduong.crt
       SSLCertificateKeyFile /etc/ssl/private/tranduong.key

       # Tương thích 100% với các phiên bản Internet Explorer trên Windows 7
       SSLProtocol all +TLSv1 +TLSv1.1 +TLSv1.2 +TLSv1.3
       SSLCipherSuite ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+EXP:@SECLEVEL=0

       ErrorLog ${APACHE_LOG_DIR}/tranduong_ssl_error.log
       CustomLog ${APACHE_LOG_DIR}/tranduong_ssl_access.log combined
   </VirtualHost>
   </IfModule>
   ```

4. **Cấu hình VirtualHost HTTP (Port 80) hoạt động song song:**
   Trong file `/etc/apache2/sites-available/000-default.conf`:
   ```apache
   <VirtualHost *:80>
       ServerAdmin webmaster@tranduong.com
       ServerName www.tranduong.com
       ServerAlias tranduong.com
       DocumentRoot /var/www/html

       ErrorLog ${APACHE_LOG_DIR}/error.log
       CustomLog ${APACHE_LOG_DIR}/access.log combined
   </VirtualHost>
   ```

5. **Kích hoạt trang SSL và Khởi động lại dịch vụ:**
   ```bash
   sudo a2ensite tranduong-ssl.conf
   sudo systemctl restart apache2
   ```

### 5.3 Kiểm tra kết quả từ Trình duyệt Web (Client):
- Mở trình duyệt gõ: `http://www.tranduong.com` -> Hệ thống tự nhảy sang `https://www.tranduong.com`.
- Trình duyệt sẽ hiển thị cảnh báo *"Your connection is not private"* (do dùng chứng chỉ tự ký Self-Signed). 
- Bấm **Advanced (Nâng cao)** -> Chọn **Proceed to www.tranduong.com (Tiếp tục truy cập)** -> Trang Web bảo mật HTTPS sẽ hiển thị thành công!

---

## 6. HƯỚNG DẪN CẤU HÌNH BẢO MẬT WEBSITE CẦN TÀI KHOẢN MẬT KHẨU (HTTP BASIC AUTHENTICATION)

### 6.1 Khái niệm HTTP Basic Authentication (.htpasswd)
HTTP Basic Authentication là cơ chế bảo mật cấp Server của Apache2. Khi người dùng truy cập vào thư mục được bảo vệ (ví dụ: `https://www.tranduong.com/private/`), trình duyệt sẽ bật khung Popup bắt buộc người dùng nhập đúng **Username** và **Password** mới cho phép xem nội dung.

### 6.2 Các bước cấu hình thủ công:

1. **Cài đặt gói công cụ quản lý mật khẩu `apache2-utils` và bật module Authentication:**
   ```bash
   sudo apt update && sudo apt install -y apache2-utils
   sudo a2enmod auth_basic authn_core authn_file authz_user
   ```

2. **Tạo file lưu trữ tài khoản mật khẩu mã hóa `/etc/apache2/.htpasswd`:**
   ```bash
   # Tạo file mới và thêm user admin (Mật khẩu: 123456)
   sudo htpasswd -b -c /etc/apache2/.htpasswd admin 123456

   # Thêm user thứ 2 tranduong (Mật khẩu: 123456)
   sudo htpasswd -b /etc/apache2/.htpasswd tranduong 123456

   # Phân quyền an toàn cho file mật khẩu
   sudo chmod 640 /etc/apache2/.htpasswd
   sudo chown root:www-data /etc/apache2/.htpasswd
   ```

3. **Tạo thư mục nội bộ và trang Web bảo mật `/var/www/html/private/index.html`:**
   ```bash
   sudo mkdir -p /var/www/html/private
   echo "<h1>🔒 KHU VỰC BẢO MẬT - ĐÃ XÁC THỰC THÀNH CÔNG!</h1>" | sudo tee /var/www/html/private/index.html
   ```

4. **Cấu hình Apache2 áp dụng bảo mật cho thư mục `/private/`:**
   Tạo file `/etc/apache2/conf-available/private-auth.conf`:
   ```apache
   <Directory "/var/www/html/private">
       AuthType Basic
       AuthName "Khu Vuc Bao Mat - Vui Long Nhap Tai Khoan Va Mat Khau"
       AuthUserFile /etc/apache2/.htpasswd
       Require valid-user
   </Directory>
   ```

5. **Kích hoạt cấu hình bảo mật và Khởi động lại Apache2:**
   ```bash
   sudo a2enconf private-auth.conf
   sudo systemctl restart apache2
   ```

### 6.3 Kiểm tra kết quả từ Trình duyệt Web (Client):
- Mở trình duyệt gõ: `https://www.tranduong.com/private/`
- Trình duyệt sẽ xuất hiện cửa sổ Popup nhỏ yêu cầu đăng nhập:
  - **Tên đăng nhập:** `admin` (hoặc `tranduong`)
  - **Mật khẩu:** `123456`
- Nhập đúng -> Màn hình hiển thị trang Web bảo mật nội bộ thành công!
- Nhập sai hoặc chọn Cancel -> Trình duyệt trả về lỗi `401 Unauthorized`.

---

## 7. BỘ CẨM NANG BẮT BỆNH LỖI MẠNG & THỦ THUẬT THỰC HÀNH (TROUBLESHOOTING)

### 🚨 7.1 Lỗi Trùng IP (IP Conflict) trên VMware & Mẹo vàng đuôi `.254`
- **Hiện tượng:** Máy ảo báo đụng IP `192.168.5.1` hoặc `192.168.6.1` không ra mạng được, hoặc gõ `ip a` bị mất địa chỉ IP.
- **Nguyên nhân:** Card mạng ảo của VMware trên Windows máy thật (`VMware Network Adapter VMnet2` / `VMnet3`) mặc định tự chiếm giữ địa chỉ `.1`.
- **💡 MẸO SỬA LỖI CỰC NHANH (MẸO ĐUÔI `.254`):**
  1. Trên Windows máy thật: Mở **Control Panel** -> **Network Connections** (Change adapter settings).
  2. Chuột phải vào card ảo **VMware Network Adapter VMnet2** (hoặc `VMnet3`) -> Chọn **Properties** -> Đúp chuột vào **TCP/IPv4**.
  3. Chọn *Use the following IP address* và đổi IP của máy thật sang đuôi **`.254`**:
     - Card `VMnet2`: Đổi thành **`192.168.5.254`** (Subnet Mask: `255.255.255.0`)
     - Card `VMnet3`: Đổi thành **`192.168.6.254`** (Subnet Mask: `255.255.255.0`)
  4. Bấm **OK**.
  👉 **KẾT QUẢ:** Địa chỉ `.1` (`192.168.5.1` / `192.168.6.1`) lập tức được giải phóng hoàn toàn cho 2 máy ảo **Win7_A** và **Win7_B**, xóa sạch 100% lỗi đụng độ IP!

---

### 🚨 7.2 Lỗi Connection Timed Out khi kết nối SSH vào Ubuntu
- **Nguyên nhân:** Máy Ubuntu chưa cài dịch vụ SSH Server (`openssh-server`), dịch vụ bị dừng, hoặc tường lửa UFW đang chặn port 22.
- **Khắc phục:** Gõ 3 lệnh sau trên màn hình đen Ubuntu:
  ```bash
  sudo apt update && sudo apt install -y openssh-server
  sudo ufw disable
  sudo systemctl enable --now ssh
  ```

---

### 🚨 7.3 Lỗi `Unreachable gateway` khi chạy `netplan apply`
- **Nguyên nhân:** Khai báo dải IP của gateway (`via: ...`) lệch dải Subnet của card mạng đó (Ví dụ: card đặt IP `192.168.5.2/24` nhưng lại khai báo `via: 192.168.1.1`).
- **Khắc phục:** Xóa bỏ dòng `via` gateway sai, hoặc chỉ khai báo `via` gateway thuộc đúng dải mạng IP của card đó.

---

### 🚨 7.4 Lỗi Ping sang Windows 7 bị Timeout
- **Nguyên nhân:** Tường lửa (Windows Firewall) trên Windows 7 mặc định bật chặn tất cả gói tin ICMP Ping.
- **Khắc phục:** Trên máy Windows 7 -> Vào **Control Panel** -> **Windows Firewall** -> Chọn **Turn Windows Firewall on or off** -> Chọn **Turn off Windows Firewall**.

---

### 🚨 7.5 Lỗi `Destination Host Unreachable` khi Ping IP Alias `192.168.5.3`
- **Nguyên nhân:** Card mạng chứa IP Alias trên máy ảo cắm lầm công tắc ảo (VD: card cắm ở `VMnet3` nhưng IP lại đặt dải `VMnet2`).
- **Khắc phục:** Vào VMware Virtual Machine Settings -> Chỉnh Card mạng chứa IP Alias sang đúng **`VMnet2`**.

---

### 🚨 7.6 Lỗi `nslookup` trên Ubuntu 2 gửi nhầm sang `8.8.8.8` (network unreachable)
- **Nguyên nhân:** File `/etc/resolv.conf` trên Ubuntu 2 đang dính DNS mặc định `8.8.8.8` của Google mà máy không có kết nối NAT ngoài.
- **Khắc phục:** Sửa file `/etc/resolv.conf` trên Ubuntu 2 trỏ về đúng IP DNS Server Ubuntu 1:
  ```bash
  echo "nameserver 192.168.6.3" | sudo tee /etc/resolv.conf
  ```

---

### 💡 7.7 Thủ thuật quản lý SSH bằng Router Jump Server
Để máy ảo **Ubuntu_2** đạt chuẩn nộp bài Lab (chỉ có 1 Card mạng nội bộ, không dùng Card NAT):
1. Từ Windows máy thật: SSH vào Router **Ubuntu_1**:
   ```powershell
   ssh neko@192.168.1.150
   ```
2. Từ bên trong cửa sổ Ubuntu_1, SSH nhảy tiếp sang **Ubuntu_2**:
   ```bash
   ssh neko@192.168.6.2
   ```
   *(Hoặc `ssh neko@192.168.5.3`)*
👉 Quản lý cả hệ thống cực kỳ an toàn, gọn gàng và chuẩn kiến trúc mạng!

---

### 🚨 7.8 Lỗi Internet Explorer trên Windows 7 không mở được HTTPS (TLS Handshake)
- **Hiện tượng:** Truy cập `https://www.tranduong.com` trên Internet Explorer 8 (Windows 7) báo *"Internet Explorer cannot display the webpage"*.
- **Nguyên nhân:** OpenSSL 3.0 trên Ubuntu 22.04 mặc định đặt mức bảo mật cao (`SECLEVEL=2`), tự động từ chối thuật toán bắt tay mã hóa SHA-1 / TLS 1.0 của IE8.
- **Khắc phục trên Server Ubuntu_1:**
  1. Hạ mức bảo mật OpenSSL xuống `SECLEVEL=0`:
     ```bash
     sudo sed -i 's/CipherString = DEFAULT:@SECLEVEL=2/CipherString = DEFAULT:@SECLEVEL=0/g' /etc/ssl/openssl.cnf
     sudo sed -i 's/SSLProtocol all -SSLv3/SSLProtocol all +TLSv1 +TLSv1.1 +TLSv1.2/g' /etc/apache2/mods-available/ssl.conf
     sudo sed -i 's/SSLCipherSuite HIGH:!aNULL/SSLCipherSuite ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+EXP:@SECLEVEL=0/g' /etc/apache2/mods-available/ssl.conf
     sudo systemctl restart apache2
     ```
- **Cấu hình trên Client Windows 7 (Internet Explorer):**
  1. Mở IE -> Chọn **Tools** -> **Internet Options** -> Thẻ **Advanced**.
  2. Kéo xuống mục **Security**, tích chọn:
     - ☑ **Use TLS 1.0**
     - ☑ **Use TLS 1.1**
     - ☑ **Use TLS 1.2**
     - *(Bỏ tích Use SSL 2.0 và Use SSL 3.0)*
  3. Bấm **Apply** -> **OK**. Tải lại trang và bấm *"Continue to this website (not recommended)"* là vào HTTPS thành công 100%!
