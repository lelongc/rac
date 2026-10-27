# HƯỚNG DẪN CẤU HÌNH CHI TIẾT & SHOW THẦY CHẤM ĐIỂM (10/10)
## BÀI KIỂM TRA THƯỜNG KỲ - QUẢN TRỊ VÀ BẢO TRÌ HỆ THỐNG (IUH)

> **Mật khẩu chuẩn thiết lập cho toàn bộ User (`nv1..ns2`)**: **`Abc@12345`**  
> **Mật khẩu tài khoản `Administrator`**: **`123`**  
> **Định dạng cấu hình**: Hệ thống Local Users, Local Security Policy (`secpol.msc`) và NTFS Permissions trên Windows Server 2012 R2 kết nối 2 máy trạm Client Windows 7.

---

## PHẦN 1: TÓM TẮT THÔNG SỐ ĐÃ CẤU HÌNH THEO ĐỀ BÀI

### 1. Bảng IP & Card mạng (Câu 1)
| Máy ảo | Tên Card mạng | Địa chỉ IP | Subnet Mask | Default Gateway |
| :--- | :--- | :--- | :--- | :--- |
| **Server 1** | `vmnet11` (LAN 1) | `192.168.1.2` | `255.255.255.0` | *(Để trống)* |
| | `vmnet12` (LAN 2) | `20.20.1.2` | `255.255.255.0` | *(Để trống)* |
| | `nat` (VMnet8) | `192.168.1.151` | `255.255.255.0` | `192.168.1.2` |
| **Client 1** | `Local Area Connection 2` | `192.168.1.1` | `255.255.255.0` | `192.168.1.2` |
| **Client 2** | `Local Area Connection` | `20.20.1.1` | `255.255.255.0` | `20.20.1.2` |

---

### 2. Cấu trúc Người dùng & Nhóm trên Server 1 (Câu 2)
| Nhóm (Group) | Người dùng (Users) | Mật khẩu | Thuộc tính tài khoản |
| :--- | :--- | :--- | :--- |
| **`nhanvien`** | `nv1`, `nv2` | `Abc@12345` | Password never expires, User cannot change pass |
| **`ketoan`** | `kt1`, `kt2` | `Abc@12345` | Password never expires, User cannot change pass |
| **`nhansu`** | `ns1`, `ns2` | `Abc@12345` | Password never expires, User cannot change pass |

---

### 3. Ma trận Phân quyền Thư mục NTFS (Câu 2)
Thư mục gốc: **`C:\DATACONGTY`** (Đã Share tên `DATACONGTY` với Full Control Everyone).

| Thư mục con | Nhóm `nhanvien` | Nhóm `ketoan` | Nhóm `nhansu` | Administrators / SYSTEM |
| :--- | :--- | :--- | :--- | :--- |
| **`DATANHANVIEN`** | **Full Control** (Allow) | **Modify** (Allow)<br>❌ **Deny Delete** | **Full Control** (Allow) | Full Control (Allow) |
| **`DATAKETOAN`** | ❌ **Deny** (Cấm truy cập) | **Full Control** (Allow) | **Read & Execute** (Allow) | Full Control (Allow) |
| **`DATANHANSU`** | ❌ **Deny** (Cấm truy cập) | **Read & Execute** (Allow) | **Full Control** (Allow) | Full Control (Allow) |

---

### 4. Bảng Chính sách Bảo mật Local Security Policy (Câu 3)
| Mục chính sách | Thiết lập theo đề bài | Ý nghĩa |
| :--- | :--- | :--- |
| **Password complexity** | **Enabled** | Bắt buộc mật khẩu có chữ hoa, chữ thường, số, ký tự đặc biệt |
| **Minimum password length** | **8 characters** | Mật khẩu tối thiểu 8 ký tự |
| **Account lockout threshold** | **5 invalid attempts** | Nhập sai quá 5 lần thì khóa tài khoản |
| **Account lockout duration** | **5 minutes** | Thời gian bị khóa là 5 phút |
| **Reset lockout counter after**| **5 minutes** | Reset bộ đếm số lần sai sau 5 phút |
| **Allow log on locally** | `Administrators`, **`nv1`**, **`kt1`**, **`ns1`** | Chỉ cho phép 3 user này đăng nhập tại Server |
| **Deny log on locally** | **`nv2`**, **`kt2`**, **`ns2`** | Cấm 3 user này đăng nhập trực tiếp tại Server |

---

## PHẦN 2: THAO TÁC CẤU HÌNH NHANH (NẾU CẦN CHỈNH TRỰC TIẾP)

### Cách đặt IP nhanh trên Client 1 và Client 2:
1. **Trên Client 1**:
   - Mở CMD (Run as Administrator) gõ lệnh:
     ```cmd
     netsh interface ip set address "Local Area Connection 2" static 192.168.1.1 255.255.255.0 192.168.1.2
     netsh advfirewall set allprofiles state off
     ```
   *(Hoặc chạy file `CAU1_SET_IP_CLIENT1.bat` có sẵn trong thư mục `TK`)*.
2. **Trên Client 2**:
   - Mở CMD (Run as Administrator) gõ lệnh:
     ```cmd
     netsh interface ip set address "Local Area Connection" static 20.20.1.1 255.255.255.0 20.20.1.2
     netsh advfirewall set allprofiles state off
     ```
   *(Hoặc chạy file `CAU1_SET_IP_CLIENT2.bat` có sẵn trong thư mục `TK`)*.

---

## PHẦN 3: KỊCH BẢN SHOW THẦY CHẤM ĐIỂM (10 ĐIỂM TUYỆT ĐỐI)

Khi thầy giáo đi đến bàn chấm bài, bạn thực hiện lần lượt 3 màn trình diễn sau:

### 🌟 SHOW CÂU 1: ĐỊA CHỈ IP & ĐỊNH TUYẾN 2 MẠNG LAN (3 ĐIỂM)

1. **Bước 1**: Mở CMD trên **Client 1** (`192.168.1.1`), gõ:
   ```cmd
   ipconfig
   ```
   👉 Chỉ cho thầy thấy: IPv4 là `192.168.1.1`, Default Gateway là `192.168.1.2`.

2. **Bước 2**: Mở CMD trên **Client 2** (`20.20.1.1`), gõ:
   ```cmd
   ipconfig
   ```
   👉 Chỉ cho thầy thấy: IPv4 là `20.20.1.1`, Default Gateway là `20.20.1.2`.

3. **Bước 3 (ĐIỂM NHẤN ĂN TIỀN)**: Từ Client 1, gõ lệnh ping xuyên mạng sang Client 2:
   ```cmd
   ping 20.20.1.1
   ```
   👉 Màn hình hiển thị:
   ```text
   Reply from 20.20.1.1: bytes=32 time=1ms TTL=127
   Reply from 20.20.1.1: bytes=32 time=1ms TTL=127
   ```
   🗣️ **Giải thích cho thầy**: *"Dạ thưa thầy, Client 1 ping sang Client 2 thành công 0% loss. Giá trị `TTL = 127` (bị trừ 1 hop từ 128) chứng minh gói tin đã đi xuyên qua Router Server 1 làm nhiệm vụ định tuyến giữa 2 mạng LAN ạ!"*

---

### 🌟 SHOW CÂU 2: USER, GROUP & PHÂN QUYỀN THƯ MỤC NTFS (4 ĐIỂM)

#### A. Show User và Group:
1. Trên Server 1, bấm `Windows + R` gõ: **`lusrmgr.msc`** ➔ Enter.
2. Bấm vào thư mục **`Groups`**:
   - Bấm đúp vào nhóm **`nhanvien`** ➔ Thầy thấy có `nv1`, `nv2`.
   - Bấm đúp vào nhóm **`ketoan`** ➔ Thầy thấy có `kt1`, `kt2`.
   - Bấm đúp vào nhóm **`nhansu`** ➔ Thầy thấy có `ns1`, `ns2`.

#### B. Show Phân quyền NTFS:
1. Mở ổ `C:\DATACONGTY`, thầy thấy có 3 thư mục con: `DATANHANVIEN`, `DATAKETOAN`, `DATANHANSU`.
2. **Show thư mục `DATANHANVIEN`**:
   - Chuột phải `DATANHANVIEN` ➔ Chọn **Properties** ➔ Thẻ **Security** ➔ Bấm nút **Advanced**.
   - 👉 Thầy sẽ thấy:
     - Dòng `nhanvien`: Quyền **Full Control** (Allow).
     - Dòng `nhansu`: Quyền **Full Control** (Allow).
     - Dòng `ketoan`: Quyền **Modify** (Allow).
     - Dòng `ketoan` (Đặc biệt): Quyền **Delete, DeleteSubdirectoriesAndFiles** hiển thị là **Deny** (Cấm xóa)!
   - 🗣️ **Nói với thầy**: *"Dạ theo đúng đề, nhóm kế toán được phép sửa nội dung nhưng bị cấm xóa file, nhóm nhân sự và nhân viên toàn quyền ạ!"*
3. **Show thư mục `DATAKETOAN`**:
   - Chuột phải `DATAKETOAN` ➔ **Properties** ➔ **Security** ➔ **Advanced**.
   - 👉 Thầy thấy:
     - `ketoan`: **Full Control** (Allow).
     - `nhansu`: **Read & Execute** (Allow - chỉ đọc).
     - `nhanvien`: **Deny** (Cấm truy cập hoàn toàn).
4. **Show thư mục `DATANHANSU`**:
   - Chuột phải `DATANHANSU` ➔ **Properties** ➔ **Security** ➔ **Advanced**.
   - 👉 Thầy thấy:
     - `nhansu`: **Full Control** (Allow).
     - `ketoan`: **Read & Execute** (Allow - chỉ đọc).
     - `nhanvien`: **Deny** (Cấm truy cập hoàn toàn).

---

### 🌟 SHOW CÂU 3: CHÍNH SÁCH BẢO MẬT & USER RIGHTS (3 ĐIỂM)

#### A. Show Chính sách trong `secpol.msc`:
1. Trên Server 1, bấm `Windows + R` gõ: **`secpol.msc`** ➔ Enter.
2. **Password Policy**:
   - Cột trái: `Account Policies` ➔ `Password Policy`.
   - 👉 Cột phải chỉ cho thầy thấy:
     - **Password must meet complexity requirements**: `Enabled`.
     - **Minimum password length**: `8 characters`.
3. **Account Lockout Policy**:
   - Cột trái: `Account Policies` ➔ `Account Lockout Policy`.
   - 👉 Cột phải chỉ cho thầy thấy:
     - **Account lockout threshold**: `5 invalid logon attempts`.
     - **Account lockout duration**: `5 minutes`.
     - **Reset account lockout counter after**: `5 minutes`.
4. **User Rights Assignment (Quyền Login Locally)**:
   - Cột trái: `Local Policies` ➔ `User Rights Assignment`.
   - Bấm đúp vào **`Allow log on locally`**:
     - 👉 Danh sách hiển thị: `Administrators`, **`kt1`**, **`ns1`**, **`nv1`**.
   - Bấm đúp vào **`Deny log on locally`**:
     - 👉 Danh sách hiển thị: **`kt2`**, **`ns2`**, **`nv2`**.

#### B. DEMO THỰC TẾ TRỰC TIẾP TRƯỚC MẶT THẦY (CHẮC CHẮN ĐẠT ĐIỂM 10):
1. Trên màn hình Server 1, nhấn phím **`Windows`** ➔ Bấm vào tên `Administrator` ở góc trên bên phải ➔ Chọn **Sign out** (hoặc Switch User).
2. **Test 1 - Đăng nhập tài khoản được phép (`nv1`)**:
   - Chọn *Other user*.
   - Nhập User: **`nv1`** | Mật khẩu: **`Abc@12345`**.
   - ➔ **Kết quả**: Đăng nhập thành công vào màn hình Desktop của Server!
3. **Test 2 - Đăng nhập tài khoản bị cấm (`nv2`)**:
   - Bấm Sign out `nv1`.
   - Chọn *Other user*.
   - Nhập User: **`nv2`** | Mật khẩu: **`Abc@12345`**.
   - ➔ **Kết quả**: Màn hình hiện thông báo đỏ chặn ngay lập tức:
     > *"The sign-in method you're trying to use isn't allowed. For more information, contact your network administrator."*
4. 🗣️ **Nói với thầy**: *"Dạ em đã cấu hình User Rights Assignment chuẩn: user nv1 được phép đăng nhập, còn nv2 bị cấm login locally đúng như đề bài yêu cầu ạ!"*

---

## TỔNG KẾT BẢNG ĐIỂM DỰ KIẾN

| Câu hỏi | Nội dung yêu cầu | Trạng thái thực hiện | Điểm tối đa |
| :---: | :--- | :---: | :---: |
| **Câu 1** | Đổi IP Client 1, Client 2, Server và định tuyến Router ping thông |  Hoàn thành | **3.0 / 3.0** |
| **Câu 2** | Tạo 3 Group, 6 User, thư mục DATACONGTY và phân quyền NTFS chuẩn |  Hoàn thành | **4.0 / 4.0** |
| **Câu 3** | Cấu hình Password Policy, Lockout 5 lần/5p, Allow/Deny Login Locally |  Hoàn thành | **3.0 / 3.0** |
| **TỔNG** | **BÀI THI THƯỜNG KỲ QUẢN TRỊ VÀ BẢO TRÌ HỆ THỐNG** |  **XUẤT SẮC** | **10 / 10** |
