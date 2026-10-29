# HƯỚNG DẪN DEMO THI THƯỜNG KỲ (TK) THỰC TẾ BẰNG TAY (CHỈ TỪNG THAO TÁC)
## MÔN: QUẢN TRỊ DỊCH VỤ MẠNG - KHOA CNTT - ĐH CÔNG NGHIỆP TP.HCM (IUH)

---

> [!IMPORTANT]
> **HƯỚNG DẪN THAO TÁC THỰC TẾ BẰNG CHUỘT VÀ BÀN PHÍM:**  
> Tài liệu này dành cho tình huống **giảng viên đứng ngay bên cạnh yêu cầu bạn tự tay thao tác** (bấm chuột, gõ lệnh Run, mở Explorer, gõ lệnh CMD) chứ không cho chạy script tự động. Hãy làm theo đúng từng bước bên dưới!

---

# 📌 BÀI 1: DEMO DỊCH VỤ DHCP & DHCP RELAY AGENT (THAO TÁC TAY)

Thầy sẽ yêu cầu chứng minh:
1. Máy Win 7-1 (Subnet A) nhận IP động từ DHCP Server.
2. Máy Win 7-2 (Subnet B) nhận IP động thông qua Relay Agent (Ubuntu 2).

---

### 👉 BƯỚC 1.1: Chuyển Win 7-1 sang DHCP bằng tay
1. Trên máy **Win 7-1**, bấm tổ hợp phím **`Windows + R`** -> Gõ **`ncpa.cpl`** -> Bấm **Enter** (để mở Network Connections).
2. Chuột phải vào biểu tượng **`Local Area Connection`** -> Chọn **`Properties`**.
3. Nhấp đúp vào dòng **`Internet Protocol Version 4 (TCP/IPv4)`**.
4. Chọn 2 dấu chấm tròn:
   * 🔘 **Obtain an IP address automatically**
   * 🔘 **Obtain DNS server address automatically**
5. Bấm **OK** -> Bấm tiếp **OK**.

---

### 👉 BƯỚC 1.2: Kiểm tra IP máy Win 7-1 cho thầy xem
1. Bấm **`Windows + R`** -> Gõ **`cmd`** -> Bấm **Enter**.
2. Gõ lệnh:
   ```cmd
   ipconfig /all
   ```
3. **Chỉ tay vào màn hình cho thầy xem:**
   * **IPv4 Address:** `192.168.1.10` (hoặc trong dải `.10` đến `.100`).
   * **Default Gateway:** `192.168.1.254` (Router R).
   * **DHCP Server:** `192.168.1.1` (Server Ubuntu 1).
   * **DNS Servers:** `192.168.1.1`.
4. Gõ lệnh ping kiểm tra thông mạng:
   ```cmd
   ping 192.168.1.1
   ping 192.168.1.254
   ```
   *(Thấy in ra `Reply from ... bytes=32 time<1ms TTL=64` là thông mạng hoàn toàn)*.

---

### 👉 BƯỚC 1.3: Chuyển Win 7-2 sang DHCP & Chứng minh nhận qua Relay Agent
1. Chuyển sang máy **Win 7-2**.
2. Làm tương tự: Bấm **`Windows + R`** -> Gõ **`ncpa.cpl`** -> Chuột phải `Local Area Connection` -> `Properties` -> Chọn IPv4 -> Chọn **Obtain an IP address automatically** -> Bấm **OK**.
3. Mở CMD trên Win 7-2 gõ:
   ```cmd
   ipconfig /all
   ```
4. **Chỉ tay vào màn hình cho thầy xem:**
   * **IPv4 Address:** `10.10.10.10` (hoặc trong dải `10.10.10.x`).
   * **Default Gateway:** `10.10.10.254` (Router R cổng Subnet B).
   * **DHCP Server:** `192.168.1.1` (Nhận từ Server Subnet A).
   * **DNS Servers:** `192.168.1.1`.
5. **Nói với thầy:**  
   *"Dạ thưa thầy, Win 7-2 thuộc Subnet B (10.10.10.0/24) đã nhận được IP từ DHCP Server 192.168.1.1 thông qua DHCP Relay Agent Ubuntu 2 (10.10.10.1) ạ."*
6. Gõ lệnh ping kiểm tra liên mạng:
   ```cmd
   ping 10.10.10.254
   ping 10.10.10.1
   ping 192.168.1.1
   ```
   *(Tất cả đều Reply thành công 0% packet loss)*.

---

# 📌 BÀI 2: DEMO SAMBA SERVER & PHÂN QUYỀN SHARED BẰNG TAY

Thầy sẽ yêu cầu chứng minh:
* Thư mục `student`: Sinh viên `sv1` và Giáo viên `gv1` đều Đọc/Ghi được.
* Thư mục `softwares`: Mọi người chỉ được ĐỌC (Read-only), cố tình ghi sẽ BỊ CHẶN.
* Thư mục `teacher$` (Share ẩn): Sinh viên `sv1` BỊ CẤM, Giáo viên `gv1` và Bảo trì `baotri` vào được.

---

> [!TIP]
> **MẸO QUAN TRỌNG KHI DEMO SAMBA TRÊN WINDOWS:**  
> Windows có cơ chế ghi nhớ tài khoản đã đăng nhập mạng. Khi muốn đổi từ tài khoản `sv1` sang `gv1`, bạn mở CMD gõ lệnh:  
> `net use * /delete /y`  
> Lệnh này sẽ xóa sạch phiên đăng nhập cũ để Windows hiện lại hộp thoại bắt nhập tài khoản mới!

---

### 👉 THAO TÁC 2.1: Demo thư mục `student` (Đọc/Ghi)
1. Trên máy Windows, bấm **`Windows + R`** -> Gõ:
   ```text
   \\192.168.1.1
   ```
   -> Bấm **Enter**.
2. Thầy sẽ thấy cửa sổ hiện ra 2 thư mục: **`student`** và **`softwares`** (riêng `teacher$` là share ẩn nên KHÔNG hiển thị ở đây!).
3. Nhấp đúp vào thư mục **`student`**:
   * Windows hiện hộp thoại đòi tài khoản.
   * Nhập **User name**: `sv1`
   * Nhập **Password**: `123`
   * Bấm **OK**.
4. Vào được bên trong thư mục `student`:
   * Đã có sẵn file `student_info.txt`.
   * **Thử Ghi bằng tay:** Chuột phải vào khoảng trắng -> Chọn **New** -> Chọn **Text Document** -> Đặt tên `bai_tap_sv1.txt`.
   * Mở file vừa tạo gõ chữ: `Sinh vien 1 nop bai` -> Bấm `Ctrl + S` lưu lại.
   * **Chỉ cho thầy xem:** File tạo và lưu thành công -> Chứng minh tài khoản sinh viên có quyền **Read/Write**!

---

### 👉 THAO TÁC 2.2: Demo thư mục `softwares` (Chỉ đọc - Cấm ghi)
1. Cũng trong cửa sổ `\\192.168.1.1`, nhấp đúp vào thư mục **`softwares`**:
   * Đang ở tài khoản `sv1` nên vào được ngay.
   * Mở file `soft_readme.txt` lên đọc bình thường.
2. **Thử Ghi bằng tay để chứng minh bị cấm:**
   * Chuột phải vào khoảng trắng -> Chọn **New** -> Chọn **Text Document**.
   * Windows sẽ bật ngay bảng thông báo lỗi:
     > **"Destination Folder Access Denied"**  
     > *You need permission to perform this action.*
   * Bấm **Cancel**.
   * **Nói với thầy:** *"Dạ thưa thầy, tài khoản sv1 chỉ có quyền Read-only trong thư mục softwares, khi cố tình tạo file hệ thống sẽ báo Access Denied ạ."*

---

### 👉 THAO TÁC 2.3: Demo thư mục ẩn `teacher$` (SV bị cấm - GV vào được)

#### Bước A: Chứng minh sinh viên `sv1` KHÔNG VÀO ĐƯỢC
1. Bấm **`Windows + R`** -> Gõ chính xác:
   ```text
   \\192.168.1.1\teacher$
   ```
   -> Bấm **Enter**.
2. Vì đang lưu phiên đăng nhập của `sv1`, Windows sẽ bật ngay hộp thoại báo lỗi:
   > **"Windows cannot access \\192.168.1.1\teacher$"**  
   > *You do not have permission to access \\192.168.1.1\teacher$. Contact your network administrator to request access.*
3. **Chỉ cho thầy xem:** Sinh viên `sv1` bị từ chối truy cập hoàn toàn!

#### Bước B: Chứng minh giáo viên `gv1` VÀO ĐƯỢC VÀ GHI ĐƯỢC
1. Mở CMD gõ lệnh xóa phiên cũ:
   ```cmd
   net use * /delete /y
   ```
2. Bấm **`Windows + R`** -> Gõ lại:
   ```text
   \\192.168.1.1\teacher$
   ```
   -> Bấm **Enter**.
3. Windows hiện hộp thoại đăng nhập:
   * **User name**: `gv1`
   * **Password**: `123`
   * Bấm **OK**.
4. Cửa sổ mở ra thành công!
   * Thấy file `teacher_exam.txt`.
   * Chuột phải -> **New** -> **Text Document** -> Đặt tên `de_thi_gv1.txt`.
   * File được tạo thành công!
5. **Nói với thầy:** *"Dạ thưa thầy, share ẩn teacher$ chỉ có giáo viên gv1 và bảo trì mới vào được và có quyền Ghi, sinh viên hoàn toàn bị chặn ạ."*

---

# 📌 BÀI 3: DEMO DỊCH VỤ FTP & DNS (fit.iuh.edu.vn) BẰNG TAY

Thầy sẽ yêu cầu chứng minh:
1. Phân giải tên miền `fit.iuh.edu.vn` ra IP server `192.168.1.1`.
2. Truy cập được FTP site bằng địa chỉ: `ftp://fit.iuh.edu.vn`.
3. Tài khoản `giaovien` và `sinhvien` vào 2 thư mục khác nhau, thay đổi nội dung được, và bị cô lập (Chroot).

---

### 👉 THAO TÁC 3.1: Kiểm tra DNS bằng tay
1. Mở CMD trên máy Windows gõ lệnh:
   ```cmd
   nslookup fit.iuh.edu.vn
   ```
2. Thầy sẽ thấy kết quả:
   ```text
   Server:   fit.iuh.edu.vn
   Address:  192.168.1.1

   Name:     fit.iuh.edu.vn
   Address:  192.168.1.1
   ```
   *(Chứng minh DNS Server BIND9 đã phân giải chuẩn 100%)*.

---

### 👉 THAO TÁC 3.2: Demo FTP trực quan trên Windows Explorer
1. Mở **Computer** (hoặc nhấn `Windows + E`).
2. Trên thanh địa chỉ (Address Bar) ở trên cùng, gõ:
   ```text
   ftp://fit.iuh.edu.vn
   ```
   -> Bấm **Enter**.
3. Hộp thoại **Log On As** hiện ra:
   * **User name:** `giaovien`
   * **Password:** `123`
   * Bấm nút **Log On**.
4. **Kiểm tra quyền của Giáo viên:**
   * Thấy file `tailieu_giaovien.txt`.
   * Kéo thả một file bất kỳ từ Desktop vào cửa sổ FTP -> Thả thành công (Có quyền Ghi/Upload).
   * Nhìn vào thanh địa chỉ: Thư mục hiển thị là `/` -> Thử bấm lùi hoặc gõ `..` không thể ra ngoài được (Tính năng **Chroot User Isolation** thành công).

---

### 👉 THAO TÁC 3.3: Demo FTP tài khoản `sinhvien` qua CMD (Thầy rất thích xem)
1. Mở cửa sổ CMD mới, gõ lệnh:
   ```cmd
   ftp fit.iuh.edu.vn
   ```
2. Nhập thông tin:
   * `User (fit.iuh.edu.vn:(none)):` gõ **`sinhvien`** -> Enter.
   * `Password:` gõ **`123`** -> Enter.
   * Hiện thông báo: `230 Login successful.`
3. Gõ các lệnh kiểm tra:
   * Gõ **`ls`** -> Thấy file: `baitap_sinhvien.txt` (Khác hoàn toàn với thư mục của giáo viên).
   * Gõ **`pwd`** -> Hiện: `257 "/" is current directory.` (Đang bị giam ở gốc).
   * Gõ **`cd ..`** -> Vẫn ở `/` (Không xem trộm được file hệ thống).
   * Gõ **`quit`** để thoát.

---

# 🖥️ PHẦN 4: NẾU THẦY BẢO SANG MÁY UBUNTU MỞ FILE CẤU HÌNH CHO THẦY XEM

Thầy có thể đứng ở máy **Ubuntu 1** hoặc **Ubuntu 2** và bảo bạn mở file cấu hình. Bạn gõ đúng các lệnh sau:

### 1. Trên Ubuntu 1 (DHCP Server & Router R):
* **Xem file cấu hình cấp IP DHCP (Câu 1):**
  ```bash
  cat /etc/dhcp/dhcpd.conf
  ```
  *(Chỉ thầy xem khối `subnet 192.168.1.0` cấp dải .10 - .100 và khối `subnet 10.10.10.0` cấp dải .10 - .100)*.
* **Xem danh sách máy đã xin IP:**
  ```bash
  cat /var/lib/dhcp/dhcpd.leases
  ```
* **Xem cấu hình Samba (/data) (Câu 2):**
  ```bash
  tail -n 35 /etc/samba/smb.conf
  ```
  *(Chỉ thầy xem `[student]`, `[teacher$]`, `[softwares]`)*.
* **Xem cấu hình FTP vsftpd (Câu 3):**
  ```bash
  grep -E "(max_clients|chroot)" /etc/vsftpd.conf
  ```
  *(In ra `max_clients=2000`, `chroot_local_user=YES`)*.
* **Xem file vùng DNS BIND9 (Câu 3):**
  ```bash
  cat /etc/bind/db.fit.iuh.edu.vn
  ```

### 2. Trên Ubuntu 2 (DHCP Relay Agent):
* **Xem cấu hình Relay Agent:**
  ```bash
  cat /etc/default/isc-dhcp-relay
  ```
  *(Chỉ thầy xem: `SERVERS="192.168.1.1 10.10.10.254"` và `INTERFACES="ens37"`)*.
* **Xem trạng thái hoạt động:**
  ```bash
  systemctl status isc-dhcp-relay
  ```

---

# 🏆 TỔNG KẾT BẢNG TÀI KHOẢN & MẬT KHẨU TOÀN HỆ THỐNG

| Dịch vụ | Tài khoản | Mật khẩu | Quyền hạn |
| :--- | :--- | :--- | :--- |
| **Samba Sinh viên** | `sv1`, `sv2`, `sv3` | `123` | • `student`: Đọc/Ghi<br>• `softwares`: Chỉ đọc<br>• `teacher$`: Bị cấm |
| **Samba Giáo viên** | `gv1`, `gv2`, `gv3` | `123` | • `student`: Đọc/Ghi<br>• `softwares`: Chỉ đọc<br>• `teacher$`: Đọc/Ghi |
| **Samba Bảo trì** | `baotri` | `123` | Toàn quyền trên cả 3 thư mục |
| **FTP Giáo viên** | `giaovien` | `123` | Thư mục `/data/QTM/giaovien` (Đọc/Ghi, Chroot) |
| **FTP Sinh viên** | `sinhvien` | `123` | Thư mục `/data/QTM/sinhvien` (Đọc/Ghi, Chroot) |
| **Linux Ubuntu** | `neko` | `conmeo` | Toàn quyền sudo |
| **Windows 7** | `Neko` | `conmeo` | Administrator |
