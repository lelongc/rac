# HƯỚNG DẪN CHI TIẾT BÀI LAB 4: CÀI ĐẶT & CẤU HÌNH NFS FILE SERVER TRÊN UBUNTU 22.04

**Môn học:** Quản trị dịch vụ mạng (IUH)  
**Môi trường thực hành:** Hệ thống máy ảo VMware (Ubuntu 1 đóng vai trò NFS Server, Ubuntu 2 đóng vai trò NFS Client)

---

## 1. TỔNG QUAN VỀ DỊCH VỤ NFS (NETWORK FILE SYSTEM)

### 1.1 NFS là gì và Khác gì với Samba?
- **NFS (Network File System)** là giao thức chia sẻ file phân tán chuẩn mực giữa các hệ điều hành **Unix/Linux với nhau**.
- **So sánh NFS và Samba:**
  - **Samba:** Chuyên dùng để chia sẻ file giữa **Linux và Windows** (giao thức SMB/CIFS, cần tài khoản/mật khẩu hoặc guest).
  - **NFS:** Chuyên dùng để chia sẻ file trực tiếp giữa **Linux và Linux** (giao thức NFS qua RPC port 2049, hiệu năng cực cao, máy Client mount thư mục mạng về máy mình và sử dụng giống hệt như ổ cứng cục bộ).

---

### 1.2 Bảng quy hoạch các thư mục chia sẻ NFS trong bài Lab:

| Tên thư mục trên Server | Dải mạng được phép truy cập | Quyền hạn truy cập | Tùy chọn cấu hình (Options) | Mục đích sử dụng |
| :--- | :--- | :---: | :--- | :--- |
| **`/nfs/share`** | `192.168.5.0/24`<br>`192.168.6.0/24` | Đọc & Ghi (`rw`) | `rw,sync,no_subtree_check,no_root_squash` | Thư mục chia sẻ không phân quyền, mọi máy Linux đọc/ghi tự do |
| **`/nfs/tailieu`** | `192.168.5.0/24`<br>`192.168.6.0/24` | Chỉ đọc (`ro`) | `ro,sync,no_subtree_check` | Thư mục giáo trình / tài liệu (Client chỉ được xem, không được sửa/xóa) |

---

## 2. CÀI ĐẶT & CẤU HÌNH TỰ ĐỘNG 1-CLICK (SCRIPT CHO PHÒNG THI)

Để cấu hình toàn bộ dịch vụ NFS Server chỉ trong **10 giây**:

1. Copy file `setup_nfs_server.sh` vào máy **Ubuntu_1**.
2. Phân quyền và chạy script:
   ```bash
   chmod +x setup_nfs_server.sh
   sudo ./setup_nfs_server.sh
   ```
*Script sẽ tự động cài `nfs-kernel-server`, tạo thư mục `/nfs/share`, `/nfs/tailieu`, phân quyền `777`, cấu hình `/etc/exports`, xuất khẩu tài nguyên và khởi động dịch vụ sẵn sàng 100%!*

---

## 3. HƯỚNG DẪN CẤU HÌNH THỦ CÔNG TỪNG BƯỚC

### 3.1 CẤU HÌNH TRÊN MÁY NFS SERVER (UBUNTU 1)

#### Bước 1: Cài đặt dịch vụ NFS Kernel Server
Mở Terminal trên **Ubuntu_1** gõ:
```bash
sudo apt update
sudo apt install -y nfs-kernel-server rpcbind
```

#### Bước 2: Tạo các thư mục chia sẻ và Phân quyền
1. **Tạo thư mục trên ổ cứng:**
   ```bash
   sudo mkdir -p /nfs/share
   sudo mkdir -p /nfs/tailieu
   ```
2. **Phân quyền truy cập:**
   ```bash
   sudo chmod -R 0777 /nfs/share
   sudo chmod -R 0777 /nfs/tailieu
   sudo chown -R nobody:nogroup /nfs/share
   sudo chown -R nobody:nogroup /nfs/tailieu
   ```
3. **Tạo file mẫu bên trong để thử nghiệm:**
   ```bash
   echo "Chao mung den voi thu muc NFS Share!" | sudo tee /nfs/share/readme_nfs.txt
   echo "Tai lieu giao trinh Quan tri mang (Chi doc)" | sudo tee /nfs/tailieu/giao_trinh.txt
   ```

#### Bước 3: Cấu hình file xuất khẩu tài nguyên `/etc/exports`
Mở file `/etc/exports`:
```bash
sudo nano /etc/exports
```

Thêm cấu hình sau vào cuối file:
```ini
# Thư mục chia sẻ đọc ghi tự do cho cả 2 mạng LAN
/nfs/share    192.168.5.0/24(rw,sync,no_subtree_check,no_root_squash) 192.168.6.0/24(rw,sync,no_subtree_check,no_root_squash)

# Thư mục tài liệu chỉ đọc
/nfs/tailieu  192.168.5.0/24(ro,sync,no_subtree_check) 192.168.6.0/24(ro,sync,no_subtree_check)
```
*(Ý nghĩa các tham số:)*
- `rw`: Cho phép cả Đọc và Ghi (Read/Write).
- `ro`: Chỉ cho phép Đọc (Read-Only).
- `sync`: Ghi dữ liệu đồng bộ ngay lập tức vào ổ cứng trước khi phản hồi (an toàn dữ liệu).
- `no_subtree_check`: Tắt kiểm tra cây thư mục con để tăng tốc độ và độ ổn định.
- `no_root_squash`: Cho phép tài khoản root phía Client có toàn quyền tương đương root phía Server.

Lưu file (`Ctrl+O`, `Enter`, `Ctrl+X`).

#### Bước 4: Xuất khẩu tài nguyên và Khởi động dịch vụ
```bash
# Áp dụng cấu hình exports
sudo exportfs -ra
sudo exportfs -v

# Khởi động lại dịch vụ NFS
sudo systemctl restart rpcbind nfs-kernel-server
sudo systemctl enable rpcbind nfs-kernel-server

# Kiểm tra trạng thái
sudo systemctl status nfs-kernel-server --no-pager
```

---

### 3.2 CẤU HÌNH TRÊN MÁY NFS CLIENT (UBUNTU 2)

#### Bước 1: Cài đặt gói công cụ NFS Client
Mở Terminal trên **Ubuntu_2** gõ:
```bash
sudo apt update
sudo apt install -y nfs-common
```

#### Bước 2: Kiểm tra danh sách thư mục chia sẻ từ Server
Gõ lệnh `showmount -e` kèm IP của máy Server Ubuntu 1:
```bash
showmount -e 192.168.6.3
```
*(Màn hình sẽ hiển thị danh sách 2 thư mục `/nfs/share` và `/nfs/tailieu` được chia sẻ từ Server)*.

#### Bước 3: Tạo thư mục gắn kết (Mount Point) và Mount thư mục NFS
1. **Tạo thư mục trên máy Client:**
   ```bash
   sudo mkdir -p /mnt/nfs_share
   sudo mkdir -p /mnt/nfs_tailieu
   ```

2. **Gắn kết (Mount) thư mục từ Server về Client:**
   ```bash
   # Mount thư mục share đọc/ghi
   sudo mount -t nfs 192.168.6.3:/nfs/share /mnt/nfs_share

   # Mount thư mục tài liệu chỉ đọc
   sudo mount -t nfs 192.168.6.3:/nfs/tailieu /mnt/nfs_tailieu
   ```

3. **Kiểm tra kết quả mount:**
   ```bash
   df -h | grep nfs
   ```
   *(Màn hình hiện rõ dung lượng và đường dẫn ổ đĩa NFS đã gắn vào `/mnt/nfs_share`)*.

#### Bước 4: Cấu hình tự động Mount khi khởi động máy (`/etc/fstab`)
Để khi máy Client Ubuntu 2 khởi động lại không bị mất mount:
Mở file `/etc/fstab`:
```bash
sudo nano /etc/fstab
```
Thêm 2 dòng sau vào cuối file:
```ini
192.168.6.3:/nfs/share    /mnt/nfs_share    nfs    defaults    0    0
192.168.6.3:/nfs/tailieu  /mnt/nfs_tailieu  nfs    defaults    0    0
```
Lưu file (`Ctrl+O`, `Enter`, `Ctrl+X`).

---

## 4. HƯỚNG DẪN CHI TIẾT DEMO CHO THẦY CHẤM ĐIỂM (ĐẠT ĐIỂM 10)

### 🖥️ PHẦN 1: SHOW TRÊN MÁY SERVER (UBUNTU 1) (30 Giây)
1. Show danh sách thư mục đang xuất khẩu:
   ```bash
   sudo exportfs -v
   ```
2. Show trạng thái dịch vụ:
   ```bash
   sudo systemctl status nfs-kernel-server --no-pager
   ```

---

### 🐧 PHẦN 2: DEMO TRÊN MÁY CLIENT (UBUNTU 2) (ĂN ĐIỂM CHÍNH)
1. **Kiểm tra xem file từ Server:**
   ```bash
   ls -la /mnt/nfs_share
   cat /mnt/nfs_share/readme_nfs.txt
   ```
2. **Demo quyền Ghi (Read/Write) trên thư mục `share`:**
   ```bash
   echo "File duoc tao tu Ubuntu 2 Client luc cham diem!" > /mnt/nfs_share/test_from_u2.txt
   ls -la /mnt/nfs_share
   ```
   👉 *(Tạo thành công file `test_from_u2.txt`)*.
3. **Quay lại Server Ubuntu 1 gõ `ls -la /nfs/share`:**
   👉 *(Thấy ngay file `test_from_u2.txt` xuất hiện lập tức trên Server!)*
4. **Demo quyền Chỉ đọc (Read-Only) trên thư mục `tailieu`:**
   ```bash
   echo "Thu sua file" > /mnt/nfs_tailieu/test_fail.txt
   ```
   👉 *(Hệ thống báo lỗi ngay: **`Read-only file system`** -> Chứng minh quyền ro hoạt động chuẩn xác 100%)*.

---

### 🔍 PHẦN 3: GIẢI THÍCH Ý NGHĨA CÁC OUTPUT KHI THẦY HỎI VẤN ĐÁP:

1. **Lệnh `showmount -e 192.168.6.3`:**
   ```text
   Export list for 192.168.6.3:
   /nfs/tailieu 192.168.6.0/24,192.168.5.0/24
   /nfs/share   192.168.6.0/24,192.168.5.0/24
   ```
   👉 *Ý nghĩa:* Cho thấy Server `192.168.6.3` đang xuất khẩu 2 thư mục và mở quyền truy cập cho tất cả các máy thuộc 2 dải mạng LAN 1 (`192.168.5.x`) và LAN 2 (`192.168.6.x`).

2. **Lệnh `df -h | grep nfs`:**
   ```text
   192.168.6.3:/nfs/share    9.8G  3.6G  5.7G  39% /mnt/nfs_share
   192.168.6.3:/nfs/tailieu  9.8G  3.6G  5.7G  39% /mnt/nfs_tailieu
   ```
   👉 *Ý nghĩa:* Cho thấy ổ đĩa từ xa `192.168.6.3:/nfs/share` đã được gắn kết thành công vào thư mục `/mnt/nfs_share` của Client, dùng chung dung lượng lưu trữ của Server.

3. **Lệnh `exportfs -v` trên Server:**
   ```text
   /nfs/share    192.168.6.0/24(sync,wdelay,hide,no_subtree_check,sec=sys,rw,no_root_squash,no_all_squash)
   ```
   👉 *Ý nghĩa các cờ phân quyền:*
   - `rw`: Read/Write (Đọc và ghi dữ liệu tự do).
   - `ro`: Read-Only (Chỉ đọc).
   - `sync`: Ghi đồng bộ ngay vào ổ đĩa.
   - `no_subtree_check`: Tắt kiểm tra cây thư mục con để tăng tốc độ.
   - `no_root_squash`: User `root` của Client có toàn quyền tương đương `root` của Server.


---

## 5. BỘ CẨM NANG XỬ LÝ LỖI NFS (TROUBLESHOOTING)

### 🚨 5.1 Lỗi `mount.nfs: access denied by server while mounting`
- **Nguyên nhân:** Dải mạng của Client chưa được khai báo trong `/etc/exports` trên Server.
- **Khắc phục:** Mở `/etc/exports` thêm đúng dải mạng `192.168.6.0/24` và chạy lại lệnh `sudo exportfs -ra`.

### 🚨 5.2 Lỗi `mount.nfs: Connection refused` hoặc `Connection timed out`
- **Nguyên nhân:** Dịch vụ NFS hoặc RPC chưa bật, hoặc tường lửa UFW đang chặn.
- **Khắc phục:** Trên Server gõ: `sudo ufw disable` và `sudo systemctl restart rpcbind nfs-kernel-server`.

### 🚨 5.3 Cách tháo gắn kết (Unmount) khi muốn dọn dẹp
```bash
sudo umount /mnt/nfs_share
sudo umount /mnt/nfs_tailieu
```
*(Nếu báo `target is busy`, gõ `sudo umount -l /mnt/nfs_share` để unmount cưỡng bức)*.
