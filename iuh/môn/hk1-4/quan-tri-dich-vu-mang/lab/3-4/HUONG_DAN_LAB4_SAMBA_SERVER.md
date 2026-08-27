# HƯỚNG DẪN CHI TIẾT BÀI LAB 4: CÀI ĐẶT & CẤU HÌNH SAMBA FILE SERVER TRÊN UBUNTU 22.04

**Môn học:** Quản trị dịch vụ mạng (IUH)  
**Môi trường thực hành:** Hệ thống 4 máy ảo VMware (Ubuntu 1 đóng vai trò Samba File Server, chia sẻ tài nguyên cho Win7_A, Win7_B và Ubuntu_2)

---

## 1. TỔNG QUAN VỀ DỊCH VỤ SAMBA FILE SERVER

### 1.1 Samba là gì và Mục đích của bài Lab?
- **Samba** là dịch vụ mạng mã nguồn mở triển khai giao thức **SMB/CIFS (Server Message Block / Common Internet File System)**, cho phép hệ điều hành **Linux (Ubuntu)** chia sẻ tệp tin (File Sharing) và máy in một cách liền mạch với các máy tính chạy **Windows (Windows 7, 8, 10, 11)** và các máy **Linux khác**.
- **Mục đích bài Lab 4:** Biến máy **Ubuntu_1 (Router LinuxA)** thành **Máy chủ lưu trữ và chia sẻ file (File Server)** tập trung, cho phép cả 3 máy Client trong hệ thống kết nối vào trao đổi dữ liệu:
  1. **Win7_A (LAN 1 - `192.168.5.1`)**: Kết nối qua IP `\\192.168.5.2`.
  2. **Win7_B (LAN 2 - `192.168.6.1`)**: Kết nối qua IP `\\192.168.6.3`.
  3. **Ubuntu_2 (LAN 2 - `192.168.6.2`)**: Kết nối qua lệnh `smbclient` hoặc `mount.cifs`.

---

### 1.2 Bảng quy hoạch 4 loại thư mục chia sẻ trong bài Lab (kèm Bài tập 5 bổ sung):

| Tên Share | Đường dẫn trên Server | Loại thư mục | Quyền hạn truy cập | Tài khoản / Mật khẩu | Mục đích sử dụng |
| :--- | :--- | :---: | :--- | :--- | :--- |
| **`[Public]`** | `/samba/public` | Công cộng (Guest) | Đọc + Ghi (Read/Write) | Không cần mật khẩu (`guest ok = yes`) | Chia sẻ dữ liệu chung, trao đổi file tự do |
| **`[Private]`** | `/samba/private` | Bảo mật (User) | Đọc + Ghi (Read/Write) | `tranduong` / `123456`<br>`admin` / `123456`<br>`cseuser` / `cseuser` | Dữ liệu nội bộ phòng ban, cần xác thực |
| **`[TaiLieu]`** | `/samba/tailieu` | Giáo trình (Read-Only) | Khách: Chỉ đọc (Read)<br>Admin: Đọc + Ghi | Khách: Xem tự do<br>Admin: `admin` / `123456` | Lưu giáo trình, đề thi (Chống bị sửa/xóa) |
| **`[sharedata_1]`** | `/tmp` | Bài tập 5 bổ sung | Đọc + Ghi cho user | `cseuser` / `cseuser` | Thư mục chia sẻ theo đề bài 5 IUH |

---

### 1.3 Quy tắc vàng so sánh giữa SAMBA và NFS (Câu hỏi thi vấn đáp):

👉 **SAMBA là cầu nối chia sẻ giữa LINUX ↔ WINDOWS (và Linux ↔ Linux)**  
👉 **NFS là cầu nối chia sẻ chuyên dụng nội bộ giữa LINUX ↔ LINUX**

| Tiêu chí | SAMBA (SMB/CIFS) | NFS (Network File System) |
| :--- | :--- | :--- |
| **Đối tượng Client** | **Windows 7 / 10 / 11** (`\\192.168.5.2`) | **Ubuntu 2 Client** (`mount -t nfs ...`) |
| **Cơ chế xác thực** | Bắt buộc nhập **Username & Mật khẩu** (`smbpasswd`) | Dựa trên **Địa chỉ IP của Client** và UID/GID |
| **Giao diện trải nghiệm** | Hiện cửa sổ thư mục như USB / Ổ đĩa mạng | Mount thẳng vào cây thư mục (`/mnt/share`) |
| **File cấu hình** | `/etc/samba/smb.conf` | `/etc/exports` |
| **Cổng mạng (Port)** | Port `139`, `445` (TCP/UDP) | Port `2049` (NFS), Port `111` (RPC) |
| **Tốc độ / Hiệu năng** | Đa năng, độ trễ vừa phải | **Cực nhanh, tối ưu cho hệ thống máy chủ Linux** |


---

## 2. CÀI ĐẶT & CẤU HÌNH TỰ ĐỘNG 1-CLICK (SCRIPT CHO PHÒNG THI)

Để cấu hình toàn bộ dịch vụ Samba Server chỉ trong **15 giây**:

1. Copy file `setup_samba_server.sh` vào máy **Ubuntu_1**.
2. Phân quyền và chạy script:
   ```bash
   chmod +x setup_samba_server.sh
   sudo ./setup_samba_server.sh
   ```
*Script sẽ tự động cài đặt `samba`, tạo 3 thư mục chia sẻ, tạo sẵn 2 user `tranduong` & `admin` (pass `123456`), cấu hình file `smb.conf` chuẩn 100% tương thích Windows 7 và khởi động lại dịch vụ!*

---

## 3. HƯỚNG DẪN CẤU HÌNH THỦ CÔNG TỪNG BƯỚC TRÊN UBUNTU_1

### Bước 1: Cài đặt gói dịch vụ Samba
Mở Terminal trên **Ubuntu_1** gõ:
```bash
sudo apt update
sudo apt install -y samba samba-common smbclient
```

---

### Bước 2: Tạo các thư mục chia sẻ và Phân quyền Linux
1. **Tạo 3 thư mục trên ổ cứng Ubuntu:**
   ```bash
   sudo mkdir -p /samba/public
   sudo mkdir -p /samba/private
   sudo mkdir -p /samba/tailieu
   ```

2. **Phân quyền truy cập thư mục:**
   ```bash
   # Thư mục Public cho phép mọi người toàn quyền
   sudo chmod -R 0777 /samba/public
   sudo chown -R nobody:nogroup /samba/public

   # Thư mục Private và TaiLieu
   sudo chmod -R 0777 /samba/private
   sudo chmod -R 0777 /samba/tailieu
   ```

3. **Tạo file văn bản mẫu bên trong để kiểm tra:**
   ```bash
   echo "Chao mung den voi thu muc PUBLIC!" | sudo tee /samba/public/readme_public.txt
   echo "Du lieu BAO MAT - Chi danh cho Admin/TranDuong!" | sudo tee /samba/private/bi_mat.txt
   echo "Giao trinh Quan tri mang IUH (Chi doc)" | sudo tee /samba/tailieu/giao_trinh.txt
   ```

---

### Bước 3: Tạo người dùng hệ thống & Mật khẩu Samba
Trong Linux, để một User có thể đăng nhập vào Samba thì User đó phải tồn tại trong hệ thống Linux trước:

1. **Tạo tài khoản Linux (nếu chưa có):**
   ```bash
   sudo useradd -m -s /bin/bash tranduong
   sudo useradd -m -s /bin/bash admin
   sudo useradd -m -s /bin/bash cseuser
   ```

2. **Tạo mật khẩu Samba cho các User:**
   ```bash
   sudo smbpasswd -a tranduong
   # (Nhập mật khẩu: 123456 và xác nhận lại: 123456)

   sudo smbpasswd -a admin
   # (Nhập mật khẩu: 123456 và xác nhận lại: 123456)

   sudo smbpasswd -a cseuser
   # (Nhập mật khẩu: cseuser và xác nhận lại: cseuser - theo yêu cầu Bài tập 5 bổ sung)
   ```

---

### Bước 4: Soạn thảo file cấu hình chính `/etc/samba/smb.conf`
Mở file cấu hình:
```bash
sudo nano /etc/samba/smb.conf
```

Xóa hoặc thêm đoạn cấu hình chuẩn sau vào cuối file:

```ini
# ==============================================================================
# CẤU HÌNH TOÀN CỤC (GLOBAL SETTINGS)
# ==============================================================================
[global]
   workgroup = WORKGROUP
   server string = Samba File Server tranduong.com
   netbios name = UBUNTU1
   security = user
   map to guest = bad user
   dns proxy = no

   # Cho phép tất cả các máy trong dải mạng 5.x và 6.x truy cập
   hosts allow = 192.168.5. 192.168.6. 192.168.1. 127.

   # Tương thích với giao thức mạng của Windows 7 SP1
   client min protocol = NT1
   server min protocol = NT1

# ------------------------------------------------------------------------------
# 1. SHARE CÔNG CỘNG (PUBLIC - KHÔNG CẦN MẬT KHẨU)
# ------------------------------------------------------------------------------
[Public]
   comment = Thu muc chia se Cong cong
   path = /samba/public
   browseable = yes
   read only = no
   guest ok = yes
   writable = yes
   create mask = 0777
   directory mask = 0777

# ------------------------------------------------------------------------------
# 2. SHARE BẢO MẬT (PRIVATE - BẮT BUỘC ĐĂNG NHẬP)
# ------------------------------------------------------------------------------
[Private]
   comment = Thu muc Bao mat Noi bo
   path = /samba/private
   browseable = yes
   read only = no
   guest ok = no
   invalid users = nobody
   valid users = admin, tranduong, cseuser, neko
   writable = yes
   create mask = 0770
   directory mask = 0770

# ------------------------------------------------------------------------------
# 3. SHARE TÀI LIỆU (TAILIEU - CHỈ ĐỌC CHO KHÁCH)
# ------------------------------------------------------------------------------
[TaiLieu]
   comment = Thu muc Giao trinh (Chi doc)
   path = /samba/tailieu
   browseable = yes
   read only = yes
   guest ok = yes
   write list = admin, tranduong

# ------------------------------------------------------------------------------
# 4. SHARE DATA (SHAREDATA_1 - BÀI TẬP 5 BỔ SUNG IUH)
# ------------------------------------------------------------------------------
[sharedata_1]
   comment = data share
   path = /tmp
   browseable = yes
   read only = no
   guest ok = yes
   writable = yes
   valid users = cseuser, admin, tranduong
```

Lưu file (`Ctrl+O`, `Enter`, `Ctrl+X`).

---

### Bước 5: Kiểm tra cú pháp và Khởi động lại dịch vụ
1. **Kiểm tra cú pháp file cấu hình (Không báo lỗi là OK):**
   ```bash
   testparm
   ```
2. **Khởi động lại 2 dịch vụ của Samba (`smbd` và `nmbd`):**
   ```bash
   sudo systemctl restart smbd nmbd
   sudo systemctl enable smbd nmbd
   ```
3. **Xem trạng thái:**
   ```bash
   sudo systemctl status smbd --no-pager
   ```
   *(Trạng thái báo `active (running)` màu xanh là thành công 100%)*.

---

## 4. HƯỚNG DẪN CHI TIẾT DEMO CHO THẦY CHẤM ĐIỂM (ĐẠT ĐIỂM 10 TỐI ĐA)

Để bài Lab được chấm điểm cao nhất và nhanh nhất, bạn thực hiện theo đúng **3 Bước trình diễn chuyên nghiệp** sau:

---

### 🖥️ BƯỚC 1: SHOW CẤU HÌNH & TRẠNG THÁI TRÊN SERVER (UBUNTU 1) (30 Giây)

Mở Terminal trên **Ubuntu 1**, gõ 3 lệnh sau cho Thầy xem:

1. **Show cấu hình các Share (Public, Private, TaiLieu):**
   ```bash
   testparm -s /etc/samba/smb.conf
   ```
   👉 *(Chỉ Thầy xem 3 Share đã được định nghĩa rõ ràng: Public không cần pass, Private valid users `admin, tranduong`, TaiLieu chỉ đọc)*.

2. **Show danh sách User Samba đã tạo:**
   ```bash
   sudo pdbedit -L
   ```
   👉 *(Màn hình hiện danh sách các User: `tranduong`, `admin`, `neko`)*.

3. **Show trạng thái dịch vụ đang hoạt động:**
   ```bash
   sudo systemctl status smbd --no-pager
   ```
   👉 *(Hiện dòng chữ xanh lá cây **`active (running)`**)*.

---

### 🌐 BƯỚC 2: DEMO THỰC TẾ TRÊN MÁY CLIENT (WINDOWS 7) (ĂN ĐIỂM CHÍNH)

Chuyển sang màn hình máy ảo **Win7_A** (hoặc Win7_B) thực hiện lần lượt 3 thao tác:

1. **Mở kết nối tới Samba Server:**
   - Bấm tổ hợp phím **`Windows + R`** -> Gõ:
     - Trên **Win7_A**: **`\\192.168.5.2`** (hoặc `\\www.tranduong.com`).
     - Trên **Win7_B**: **`\\192.168.6.3`** (hoặc `\\www.tranduong.com`).
   - Bấm **OK** -> Màn hình Windows 7 xuất hiện 3 thư mục: `Public`, `Private`, `TaiLieu`.

2. **Demo 1 - Thư mục Công cộng `Public` (Không mật khẩu + Toàn quyền):**
   - Click đúp vào thư mục **`Public`** -> Mở ra ngay lập tức.
   - Chuột phải -> **New -> Text Document** -> Đặt tên `test_win7.txt` -> Lưu thành công (chứng minh quyền Ghi `writable = yes`).

3. **Demo 2 - Thư mục Bảo mật `Private` (Bắt buộc Đăng nhập):**
   - Click đúp vào thư mục **`Private`** -> Windows 7 **bật bảng Popup "Enter Network Password"**:
     - *User name:* **`tranduong`** (hoặc `admin`)
     - *Password:* **`123456`**
   - Bấm **OK** -> Mở thư mục thành công và xem được file bí mật bên trong!

4. **Demo 3 - Thư mục Giáo trình `TaiLieu` (Chỉ đọc - Read Only):**
   - Click đúp vào thư mục **`TaiLieu`** -> Mở xem file `giao_trinh_mang.txt`.
   - Thử chỉnh sửa nội dung và bấm Save -> Windows 7 báo lỗi: *"Access is denied"* (chứng minh quyền Chỉ đọc `read only = yes` hoạt động chuẩn 100%).

---

### 💡 BƯỚC 3: MẸO XÓA CACHE ĐĂNG NHẬP ĐỂ DEMO LẠI NHIỀU LẦN (NẾU CẦN)

Nếu bạn vừa đăng nhập xong và muốn xóa nhớ mật khẩu để biểu diễn lại popup cho Thầy xem từ đầu:
- Mở **cmd** trên Windows 7 gõ:
  ```cmd
  net use * /delete /y
  ```
- Sau đó mở lại `\\192.168.5.2\Private` -> Windows sẽ lập tức hiện lại bảng Popup hỏi tài khoản/mật khẩu mới!

---

### 🐧 BƯỚC 4: DEMO TRUY CẬP TỪ LINUX CLIENT (UBUNTU 2) (NẾU THẦY YÊU CẦU)

Trên màn hình **Ubuntu_2**, gõ các lệnh kiểm tra:
1. **Liệt kê danh sách thư mục chia sẻ:**
   ```bash
   smbclient -L 192.168.6.3 -N
   ```
2. **Truy cập vào thư mục Public:**
   ```bash
   smbclient //192.168.6.3/Public -N
   ```
   *(Gõ `ls` để xem file, gõ `exit` để thoát)*.

---

## 5. BỘ CẨM NANG XỬ LÝ LỖI SAMBA SERVER (TROUBLESHOOTING)

### 🚨 5.1 Lỗi Windows 7 báo *"Windows cannot access \\192.168.5.2"* (Error code: 0x80004005 / 0x80070035)
- **Nguyên nhân 1:** Tường lửa UFW trên Ubuntu 1 đang chặn các port của Samba (Port 139, 445).
  - **Khắc phục:** `sudo ufw disable` trên Ubuntu 1.
- **Nguyên nhân 2:** Dòng `hosts allow` trong `smb.conf` chưa khai báo dải mạng của Client.
  - **Khắc phục:** Sửa `hosts allow = 192.168.5. 192.168.6. 192.168.1. 127.`
- **Nguyên nhân 3:** Windows 7 dùng giao thức SMBv1 nhưng Ubuntu 22.04 mặc định chỉ bật SMBv2/v3.
  - **Khắc phục:** Bổ sung `server min protocol = NT1` và `client min protocol = NT1` vào mục `[global]` trong file `smb.conf`.

---

### 🚨 5.2 Lỗi đăng nhập vào thư mục Private bị báo *"Access is denied"*
- **Nguyên nhân:** Chưa đặt mật khẩu Samba cho User bằng lệnh `smbpasswd`.
- **Khắc phục:** Chạy lệnh: `sudo smbpasswd -a tranduong` và nhập mật khẩu `123456`.

---

### 🚨 5.3 Lỗi vào được thư mục Public nhưng không tạo / sửa được file
- **Nguyên nhân:** Quyền trên hệ thống file Linux (`chmod`) chưa cho phép User `nobody` hoặc `others` ghi file.
- **Khắc phục:** Chạy lệnh: `sudo chmod -R 0777 /samba/public` trên Ubuntu 1.
