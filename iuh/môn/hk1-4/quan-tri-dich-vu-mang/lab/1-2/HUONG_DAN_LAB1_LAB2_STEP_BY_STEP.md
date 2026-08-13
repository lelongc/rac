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

| STT | Tên Máy ảo | Hệ điều hành | Card mạng VMware | Tên Interface trong OS | Địa chỉ IP / Subnet | Vai trò / Dịch vụ |
| :-- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Win7_A** | Windows 7 SP1 | Custom (`VMnet2`) | Local Area Connection | `192.168.5.1/24` | Host A Client |
| 2 | **Ubuntu_1** | Ubuntu 22.04 | Card 1: NAT (`VMnet8`)<br />Card 2: Custom (`VMnet2`)<br />Card 3: Custom (`VMnet3`) | `ens33`: `192.168.1.150/24`<br />`ens37`: `192.168.5.2/24`<br />`ens38`: `192.168.6.3/24` | LinuxA Router & **DNS Server BIND9** (SSH & Internet) |
| 3 | **Ubuntu_2** | Ubuntu 22.04 | Card 1: Custom (`VMnet3`) | `ens33`: `192.168.6.2/24`<br />`ens33:0` (Alias): `192.168.5.3/24` | LinuxB Client / DNS Client |
| 4 | **Win7_B** | Windows 7 SP1 | Custom (`VMnet3`) | Local Area Connection | `192.168.6.1/24` | Host B Client |

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

### 2.4 Cấu hình Ubuntu_2 (LinuxB) - 1 Card mạng 2 IP (IP Alias)

### 2.4 Cấu hình Ubuntu_2 (LinuxB) - 2 Card Mạng & IP Alias (`192.168.6.2` + `192.168.5.3`)

Trên **Ubuntu_2 (LinuxB)**:
- **Card 1 (`ens33`)**: NAT (`VMnet8`) - IP `192.168.1.151/24` (Dùng để SSH từ máy thật Windows `ssh neko@192.168.1.151` và cài đặt phần mềm).
- **Card 2 (`ens37`)**: Custom (`VMnet3` - LAN 2) - Cấu hình 2 địa chỉ IP trên cùng 1 card:
  - **IP chính**: `192.168.6.2/24` (Client dải LAN 2)
  - **IP Alias**: `192.168.5.3/24` (IP phụ dải LAN 1 để kết nối thẳng với Win7_A `192.168.5.1`)

---

#### 📝 FILE CẤU HÌNH NETPLAN CHUẨN HOÀN CHỈNH CHO UBUNTU_2:

Mở file Netplan trên màn hình Ubuntu_2:
```bash
sudo nano /etc/netplan/00-installer-config.yaml
```

Copy & Nhập nội dung cấu hình chuẩn:

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

    # --- CARD 2 (ens37): LAN 2 (VMnet3) - IP CHÍNH 192.168.6.2 VÀ IP ALIAS 192.168.5.3 ---
    ens37:
      dhcp4: no
      addresses:
        - 192.168.6.2/24 # IP chính dải LAN 2
        - 192.168.5.3/24 # IP Alias (phụ) dải LAN 1
```

Lưu file (`Ctrl+O`, `Enter`, `Ctrl+X`) rồi áp dụng:
```bash
sudo chmod 600 /etc/netplan/00-installer-config.yaml
sudo netplan apply
sudo ufw disable
```

---

#### 🛠️ KẾT NỐI SSH VÀO UBUNTU_2 TỪ WINDOWS POWERSHELL:

```powershell
ssh neko@192.168.1.151
```
*(Nhập mật khẩu: `conmeo` hoặc mật khẩu máy Ubuntu 2 của bạn).*

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

## 4. SỬ DỤNG SCRIPT TỰ ĐỘNG CẤU HÌNH DNS BIND9 (1-CLICK)

Để hỗ trợ bạn chạy cấu hình DNS BIND9 nhanh chóng chỉ bằng 1 dòng lệnh trên **Ubuntu_1**:

1. Tải/Tạo file `setup_dns_server.sh` trên Ubuntu_1.
2. Phân quyền và chạy script:
   ```bash
   chmod +x setup_dns_server.sh
   sudo ./setup_dns_server.sh
   ```

Script sẽ tự động cài đặt BIND9, tạo file zone `tranduong.com`, thêm các bản ghi `ns`, `www`, `ftp`, `mail` và restart dịch vụ hoàn toàn tự động!

---

## 5. BỘ CẨM NANG BẮT BỆNH LỖI MẠNG & THỦ THUẬT THỰC HÀNH (TROUBLESHOOTING)

### 🚨 5.1 Lỗi Trùng IP (IP Conflict) trên VMware & Mẹo vàng đuôi `.254`
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

### 🚨 5.2 Lỗi Connection Timed Out khi kết nối SSH vào Ubuntu
- **Nguyên nhân:** Máy Ubuntu chưa cài dịch vụ SSH Server (`openssh-server`), dịch vụ bị dừng, hoặc tường lửa UFW đang chặn port 22.
- **Khắc phục:** Gõ 3 lệnh sau trên màn hình đen Ubuntu:
  ```bash
  sudo apt update && sudo apt install -y openssh-server
  sudo ufw disable
  sudo systemctl enable --now ssh
  ```

---

### 🚨 5.3 Lỗi `Unreachable gateway` khi chạy `netplan apply`
- **Nguyên nhân:** Khai báo dải IP của gateway (`via: ...`) lệch dải Subnet của card mạng đó (Ví dụ: card đặt IP `192.168.5.2/24` nhưng lại khai báo `via: 192.168.1.1`).
- **Khắc phục:** Xóa bỏ dòng `via` gateway sai, hoặc chỉ khai báo `via` gateway thuộc đúng dải mạng IP của card đó.

---

### 🚨 5.4 Lỗi Ping sang Windows 7 bị Timeout
- **Nguyên nhân:** Tường lửa (Windows Firewall) trên Windows 7 mặc định bật chặn tất cả gói tin ICMP Ping.
- **Khắc phục:** Trên máy Windows 7 -> Vào **Control Panel** -> **Windows Firewall** -> Chọn **Turn Windows Firewall on or off** -> Chọn **Turn off Windows Firewall**.

---

### 🚨 5.5 Lỗi `Destination Host Unreachable` khi Ping IP Alias `192.168.5.3`
- **Nguyên nhân:** Card mạng chứa IP Alias trên máy ảo cắm lầm công tắc ảo (VD: card cắm ở `VMnet3` nhưng IP lại đặt dải `VMnet2`).
- **Khắc phục:** Vào VMware Virtual Machine Settings -> Chỉnh Card mạng chứa IP Alias sang đúng **`VMnet2`**.

---

### 💡 5.6 Thủ thuật quản lý SSH bằng Router Jump Server
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
