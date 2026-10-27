# HƯỚNG DẪN JOIN DOMAIN 2 CLIENT VÀO SERVER & DEMO THẦY CHẤM 10 ĐIỂM

---

## TỔNG QUAN HỆ THỐNG
- **Tên miền Domain Controller**: `abc.com` (NetBIOS: `ABC`)
- **Server 1**:
  - IP LAN 1 (`vmnet11`): `192.168.1.2` (DNS nội bộ: `127.0.0.1`)
  - IP LAN 2 (`vmnet12`): `20.20.1.2`
- **Client 1**:
  - IP: `192.168.1.1` | Gateway: `192.168.1.2` | **DNS: `192.168.1.2`**
- **Client 2**:
  - IP: `20.20.1.1` | Gateway: `20.20.1.2` | **DNS: `20.20.1.2`**
- **Tài khoản Administrator Domain**: `Administrator` / Mật khẩu: `123` (hoặc `Abc@12345`)

---

## CÁCH 1: LÀM TỰ ĐỘNG BẰNG FILE SCRIPT (CỰC NHANH - 3 PHÚT XONG HẾT)

### Bước 1: Trên máy Server 1
1. Mở thư mục bài thi, chuột phải vào file **[SERVER1_NANG_CAP_DC_ABC.bat](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/qu%E1%BA%A3n%20tr%E1%BB%8B%20v%C3%A0%20b%E1%BA%A3o%20tr%C3%AC%20h%E1%BB%87%20th%E1%BB%91ng/lab/TK/SERVER1_NANG_CAP_DC_ABC.bat)** $\rightarrow$ chọn **Run as Administrator**.
2. Script sẽ tự cài đặt Active Directory Domain Services và khởi tạo Forest `abc.com`.
3. Sau khi chạy xong, Server 1 sẽ **tự động khởi động lại** (khoảng 1 - 2 phút).
4. Khi Server bật lên màn hình đăng nhập, bạn đăng nhập vào với mật khẩu cũ (`123`).
5. Tiếp tục chuột phải vào file **[SERVER1_TAO_USER_GROUP_SAU_KHI_LEN_DC.bat](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/qu%E1%BA%A3n%20tr%E1%BB%8B%20v%C3%A0%20b%E1%BA%A3o%20tr%C3%AC%20h%E1%BB%87%20th%E1%BB%91ng/lab/TK/SERVER1_TAO_USER_GROUP_SAU_KHI_LEN_DC.bat)** $\rightarrow$ chọn **Run as Administrator**.
   - Script tự tạo 3 nhóm Domain: `nhanvien`, `ketoan`, `nhansu`.
   - Script tự tạo 6 user Domain: `nv1..ns2` (Pass: `Abc@12345`).
   - Tự động gán quyền NTFS trên `C:\DATACONGTY` chuẩn 100%.

### Bước 2: Trên máy Client 1
1. Chuột phải vào file **[CLIENT1_JOIN_DOMAIN_ABC.bat](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/qu%E1%BA%A3n%20tr%E1%BB%8B%20v%C3%A0%20b%E1%BA%A3o%20tr%C3%AC%20h%E1%BB%87%20th%E1%BB%91ng/lab/TK/CLIENT1_JOIN_DOMAIN_ABC.bat)** $\rightarrow$ chọn **Run as Administrator**.
2. Script tự động trỏ DNS về `192.168.1.2` $\rightarrow$ kiểm tra thông mạng `abc.com` $\rightarrow$ gia nhập Domain $\rightarrow$ tự restart sau 5 giây.

### Bước 3: Trên máy Client 2
1. Chuột phải vào file **[CLIENT2_JOIN_DOMAIN_ABC.bat](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/qu%E1%BA%A3n%20tr%E1%BB%8B%20v%C3%A0%20b%E1%BA%A3o%20tr%C3%AC%20h%E1%BB%87%20th%E1%BB%91ng/lab/TK/CLIENT2_JOIN_DOMAIN_ABC.bat)** $\rightarrow$ chọn **Run as Administrator**.
2. Script tự động trỏ DNS về `20.20.1.2` $\rightarrow$ kiểm tra thông mạng `abc.com` $\rightarrow$ gia nhập Domain $\rightarrow$ tự restart sau 5 giây.

---

## CÁCH 2: LÀM BẰNG TAY (GUI) NẾU THẦY BẮT LÀM TRỰC TIẾP

### 1. Trên máy Server 1:
- Nếu Server chưa lên Domain:
  - Mở **Server Manager** $\rightarrow$ **Manage** $\rightarrow$ **Add Roles and Features**.
  - Tích chọn **Active Directory Domain Services** $\rightarrow$ Next đến hết $\rightarrow$ **Install**.
  - Cài xong bấm vào lá cờ vàng có dấu chấm than ở trên cùng góc phải $\rightarrow$ Chọn **Promote this server to a domain controller**.
  - Chọn **Add a new forest** $\rightarrow$ Root domain name: **`abc.com`** $\rightarrow$ Next.
  - Nhập DSRM Password: **`Abc@12345`** $\rightarrow$ Next đến hết $\rightarrow$ Bấm **Install** (Server tự reboot).

### 2. Trên máy Client 1:
1. **Trỏ DNS**:
   - Bấm `Win + R` $\rightarrow$ gõ `ncpa.cpl` $\rightarrow$ Enter.
   - Chuột phải vào card mạng đang kết nối $\rightarrow$ chọn **Properties**.
   - Click đúp vào **Internet Protocol Version 4 (TCP/IPv4)**.
   - Phần **Preferred DNS server**: Gõ **`192.168.1.2`** $\rightarrow$ bấm OK $\rightarrow$ OK.
2. **Gia nhập Domain**:
   - Bấm nút **Start** $\rightarrow$ Chuột phải vào **Computer** $\rightarrow$ chọn **Properties**.
   - Ở mục *Computer name, domain, and workgroup settings*, bấm vào dòng màu xanh **Change settings** (bên phải).
   - Ở tab *Computer Name*, bấm nút **Change...**.
   - Ở mục *Member of*, click chọn nút tròn **Domain** $\rightarrow$ gõ: **`abc.com`** $\rightarrow$ bấm **OK**.
   - Hộp thoại đăng nhập hiện ra:
     - User name: **`Administrator`** (hoặc `abc\Administrator`)
     - Password: **`123`** (nếu không được gõ `Abc@12345`)
   - Xuất hiện thông báo: **"Welcome to the abc.com domain."** $\rightarrow$ bấm OK $\rightarrow$ chọn **Restart Now**.

### 3. Trên máy Client 2:
- Thực hiện hoàn toàn tương tự Client 1, chỉ khác duy nhất:
  - **Preferred DNS server**: Gõ **`20.20.1.2`** *(IP của Server 1 trên dải VMnet12)*.

---

## KỊCH BẢN SHOW CHO THẦY CHẤM ĐIỂM SAU KHI ĐÃ JOIN DOMAIN

### Show 1: Kiểm tra 2 Client đã nằm trong Domain
- Trên Server 1, bấm `Win + R` $\rightarrow$ gõ **`dsa.msc`** (Active Directory Users and Computers) $\rightarrow$ Enter.
- Mở rộng nhánh **`abc.com`** $\rightarrow$ click vào thư mục **`Computers`**:
  - Chỉ cho thầy thấy: Cả 2 máy Client (ví dụ `WIN7-PC1` và `WIN7-PC2`) đều đã xuất hiện ở đây!

### Show 2: Demo thực tế Câu 2 từ máy Client (CỰC KỲ ẤN TƯỢNG)
- Đứng trên máy Client 1 hoặc Client 2:
  - Bấm `Win + R` $\rightarrow$ gõ: **`\\192.168.1.2\DATACONGTY`** (hoặc `\\20.20.1.2\DATACONGTY`) $\rightarrow$ Enter.
  - Khi hỏi tài khoản:
    1. Nhập **`ABC\nv1`** / mật khẩu **`Abc@12345`**:
       - Mở thư mục `DATANHANVIEN`: Mở bình thường, tạo/sửa file được (Full control).
       - Bấm thử vào `DATAKETOAN` hoặc `DATANHANSU`: Lập tức hiện bảng **"Windows cannot access... Access is denied"** $\rightarrow$ Đúng 100% yêu cầu cấm truy cập!
    2. Đổi sang tài khoản **`ABC\kt1`** / mật khẩu **`Abc@12345`**:
       - Mở `DATAKETOAN`: Mở bình thường (Full control).
       - Mở `DATANHANSU`: Mở đọc file được, nhưng tạo file mới báo Access Denied (Chỉ đọc).
       - Mở `DATANHANVIEN`: Sửa file mẫu được, nhưng bấm `Delete` thì bị cấm!
- Thầy nhìn thấy phân quyền hoạt động trực tiếp qua mạng từ Client sang Server là **10 ĐIỂM TUYỆT ĐỐI**!
