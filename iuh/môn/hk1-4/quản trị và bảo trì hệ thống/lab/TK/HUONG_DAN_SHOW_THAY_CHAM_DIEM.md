# HƯỚNG DẪN CHI TIẾT SHOW CHO GIẢNG VIÊN CHẤM ĐIỂM (10/10)
## Đề bài: Xây dựng Domain `fit.iuh.edu.vn` & Quản trị Client dải IP `192.168.10.x`

---

### 📌 THÔNG SỐ TOÀN BỘ HỆ THỐNG ĐÃ CẤU HÌNH SẴN:

| Máy ảo | Địa chỉ IP | Vai trò trong hệ thống | Tên hiển thị trong Domain | Mật khẩu chuẩn |
| :--- | :--- | :--- | :--- | :--- |
| **Server 1** | **`192.168.10.1`** | **Domain Controller (DC)** | `WIN-P6PG9M9AICK.fit.iuh.edu.vn` | **`Admin@123`** |
| **Client 1** | **`192.168.10.2`** | **Domain Member** | `WIN7-PC1.fit.iuh.edu.vn` | **`Admin@123`** |
| **Client 2** | **`192.168.10.3`** | **Domain Member** | `WIN7-PC2.fit.iuh.edu.vn` | **`Admin@123`** |

- **Tên miền Domain:** `fit.iuh.edu.vn` (NetBIOS: `FIT`).
- **Chính sách mật khẩu (Password Policy):** Độ dài tối thiểu **8 ký tự**, bắt buộc độ phức tạp (chữ hoa, chữ thường, số, ký tự đặc biệt).
- **Chính sách khóa tài khoản (Account Lockout Policy):** Nhập sai **3 lần** thì bị khóa (ban) trong **15 phút**.

---

## 🎯 CÁCH SHOW CHO THẦY XEM (3 BƯỚC ĐƠN GIẢN):

---

### BƯỚC 1: TRÊN MÁY SERVER (`192.168.10.1`)

#### 👉 Cách 1 (Nhanh nhất - 1 Click chuột):
1. Trên màn hình Desktop của Server, click đúp vào file: **`SHOW_KET_QUA_CHO_THAY.bat`**.
2. Cửa sổ màu đen hiện lên viền xanh lá cây cực đẹp, in ra toàn bộ bảng chứng minh:
   - Tên miền: `fit.iuh.edu.vn`
   - Bảng Active Directory có đủ cả 3 máy: `WIN-P6PG9M9AICK`, `WIN7-PC1`, `WIN7-PC2`
   - Chính sách mật khẩu: `MinPasswordLength: 8`, `Complexity: True`, `LockoutThreshold: 3`
   - Kết quả Ping sang cả 2 Client đều đạt **0% loss**.

#### 👉 Cách 2 (Show bằng giao diện đồ họa GUI chuẩn công nghệ):
Khi thầy đứng cạnh và bảo *"Mở Active Directory cho tôi xem"*:
1. Vào **Server Manager** $\rightarrow$ bấm menu **Tools** ở góc trên bên phải $\rightarrow$ chọn **Active Directory Users and Computers**.
2. Bấm vào mũi tên mở rộng `fit.iuh.edu.vn`:
   - Click vào thư mục **`Computers`** $\rightarrow$ Chỉ cho thầy thấy 2 máy: **`WIN7-PC1`** và **`WIN7-PC2`** đang nằm ở đây.
   - Click vào thư mục **`Domain Controllers`** $\rightarrow$ Chỉ cho thầy máy chủ **`WIN-P6PG9M9AICK`**.
3. Vào lại **Tools** $\rightarrow$ chọn **DNS**:
   - Mở rộng `WIN-P6PG9M9AICK` $\rightarrow$ **Forward Lookup Zones** $\rightarrow$ click vào **`fit.iuh.edu.vn`**.
   - Chỉ cho thầy thấy các bản ghi IP: `192.168.10.1`, `192.168.10.2`, `192.168.10.3`.

---

### BƯỚC 2: TRÊN CẢ 2 MÁY CLIENT 1 & CLIENT 2

#### 👉 Cách 1 (Nhanh nhất - 1 Click chuột):
1. Trên màn hình Desktop của Client 1 (hoặc Client 2), click đúp vào file: **`SHOW_KET_QUA_CHO_THAY.bat`**.
2. Màn hình in ra chứng cứ không thể chối cãi:
   - `Domain: fit.iuh.edu.vn`
   - `User Name: FIT\Administrator` (chứng minh đang đăng nhập bằng quyền quản trị miền)
   - `The secure channel status to fit.iuh.edu.vn: Success`
   - `Ping 192.168.10.1: TTL=128 (Thông mạng)`

#### 👉 Cách 2 (Show qua System Properties cổ điển):
Khi thầy bảo *"Mở xem máy này đã vào Domain chưa"*:
1. Bấm chuột phải vào biểu tượng **Computer** trên Desktop $\rightarrow$ chọn **Properties**.
2. Kéo xuống mục **Computer name, domain, and workgroup settings**:
   - **Computer name:** `WIN7-PC1` *(hoặc `WIN7-PC2`)*
   - **Domain:** **`fit.iuh.edu.vn`** *(Chữ Domain thay thế hoàn toàn chữ WORKGROUP)*.

#### 👉 Cách 3 (Show quyền quản trị Domain Admin):
Khi thầy hỏi *"Tài khoản này có quyền gì trên máy trạm?"*:
1. Mở cửa sổ **Command Prompt (CMD)**, gõ:
   ```cmd
   whoami
   ```
   $\rightarrow$ Kết quả hiện: **`fit\administrator`**.
2. Gõ tiếp lệnh kiểm tra nhóm quyền:
   ```cmd
   net localgroup administrators
   ```
   $\rightarrow$ Trong danh sách thành viên sẽ có **`FIT\Domain Admins`** và **`FIT\Administrator`**.  
   *Giải thích với thầy: "Thưa thầy, tài khoản này thuộc nhóm Domain Admins của miền `fit.iuh.edu.vn` nên có Full Control quản trị toàn bộ máy Client."*

---

### BƯỚC 3: SHOW CHÍNH SÁCH MẬT KHẨU & TEST KHÓA TÀI KHOẢN (LOCKOUT)

Khi thầy yêu cầu *"Chứng minh chính sách mật khẩu 8 ký tự và sai 3 lần bị khóa"*:

1. **Show thông số chính sách trên Server:**
   - Mở PowerShell trên Server gõ:
     ```powershell
     Get-ADDefaultDomainPasswordPolicy
     ```
   - Chỉ cho thầy 4 dòng quan trọng nhất:
     - `MinPasswordLength : 8` (Độ dài tối thiểu 8 ký tự)
     - `ComplexityEnabled : True` (Bắt buộc mật khẩu mạnh)
     - `LockoutThreshold  : 3` (Nhập sai 3 lần là bị khóa)
     - `LockoutDuration   : 00:15:00` (Thời gian khóa 15 phút)

2. **Thực hành Test khóa tài khoản trực tiếp (Nếu thầy muốn kiểm chứng):**
   - Trên Server, mở CMD tạo nhanh 1 user để thử:
     ```cmd
     net user test1 Admin@123 /add /domain
     ```
   - Qua máy **Client 1**, chọn **Switch User** $\rightarrow$ gõ user: `FIT\test1`.
   - Nhập **sai mật khẩu 3 lần liên tiếp** (ví dụ gõ: `abc`, `123`, `xyz`).
   - Đến lần thứ 4, Windows sẽ hiện thông báo màu đỏ ngay trên màn hình:
     > *"The referenced account is currently locked out and may not be logged on to."*  
     *(Tài khoản đã bị khóa do vi phạm chính sách đăng nhập sai 3 lần).*
   - Thầy thấy thông báo này là chấm điểm tối đa 10/10 ngay lập tức!

---

### BƯỚC 4: SHOW QUYỀN CHO PHÉP USER1 LOGON VÀO SERVER (ALLOW LOG ON LOCALLY)

Khi thầy yêu cầu *"Chứng minh user1 được phép logon vào máy chủ Server"*:

1. **Thông tin tài khoản đã tạo:**
   - **Tên đăng nhập:** `user1` (hoặc `FIT\user1`)
   - **Mật khẩu:** **`Admin@123`**
   - **Quyền hạn:** Đã được cấp quyền **`Allow log on locally`** (`SeInteractiveLogonRight`) trong chính sách quản trị Domain Controller.

2. **Cách 1: Show trực tiếp bằng giao diện GPO (Để thầy xem cấu hình)**
   - Vào **Server Manager** $\rightarrow$ **Tools** $\rightarrow$ **Group Policy Management**.
   - Mở rộng: `fit.iuh.edu.vn` $\rightarrow$ **`Domain Controllers`** $\rightarrow$ Chuột phải vào **`Default Domain Controllers Policy`** $\rightarrow$ chọn **Edit**.
   - Đi theo nhánh:
     `Computer Configuration` $\rightarrow$ `Policies` $\rightarrow$ `Windows Settings` $\rightarrow$ `Security Settings` $\rightarrow$ `Local Policies` $\rightarrow$ click vào **`User Rights Assignment`**.
   - Ở khung bên phải, click đúp vào dòng **`Allow log on locally`**:
     👉 Thầy sẽ thấy tài khoản **`FIT\user1`** nằm ngay trong danh sách được phép đăng nhập trực tiếp tại Server!

3. **Cách 2: Đăng nhập thực tế trên màn hình Server (Khẳng định kết quả 100%)**
   - Trên máy ảo **Server**, bấm tổ hợp phím **`Ctrl + Alt + Del`** (hoặc nút bấm trên thanh công cụ VMware) $\rightarrow$ chọn **Switch User** (hoặc Sign out).
   - Chọn **Other User**:
     - User name: **`FIT\user1`** *(hoặc `user1`)*
     - Password: **`Admin@123`**
   - Nhấn **Enter** $\rightarrow$ **Đăng nhập vào thẳng Desktop của Server thành công!**  
     *(Nếu là một user thường khác không được cấp quyền này, Server sẽ chặn lại ngay với thông báo: "The sign-in method you're trying to use isn't allowed").*

---

### 💡 LỜI KHUYÊN KHI TRẢ LỜI CÂU HỎI CỦA THẦY:
- **Nếu thầy hỏi:** *"Tại sao em không dùng IP cũ 192.168.11.x mà dùng 192.168.10.x?"*  
  $\rightarrow$ **Trả lời:** *"Dạ em cấu hình hoàn toàn chuẩn xác theo đúng địa chỉ IP yêu cầu của đề bài: Server là `192.168.10.1`, Client 1 là `192.168.10.2` và Client 2 là `192.168.10.3` ạ."*
- **Nếu thầy hỏi:** *"Mật khẩu quản trị của hệ thống là gì?"*  
  $\rightarrow$ **Trả lời:** *"Dạ mật khẩu chuẩn là `Admin@123`, đáp ứng đúng chính sách tối thiểu 8 ký tự và độ phức tạp cao ạ."*
- **Nếu thầy hỏi:** *"User thường có được đăng nhập vào Server không?"*  
  $\rightarrow$ **Trả lời:** *"Dạ mặc định trên Domain Controller thì user thường bị chặn hoàn toàn. Nhưng theo yêu cầu đề bài, em đã cấu hình quyền Allow log on locally trong Default Domain Controllers Policy để cấp phép riêng cho user1 được đăng nhập vào Server ạ."*

