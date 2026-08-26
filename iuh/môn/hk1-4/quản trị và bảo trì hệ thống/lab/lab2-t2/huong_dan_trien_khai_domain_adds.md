# HƯỚNG DẪN CHI TIẾT TRIỂN KHAI HỆ THỐNG DOMAIN CONTROLLER (AD DS)
## MÔN: QUẢN TRỊ VÀ BẢO TRÌ HỆ THỐNG (IUH) - BÀI THỰC HÀNH TUẦN 2 (LAB 2-T2)

Tài liệu này hướng dẫn chi tiết từng bước (Step-by-step) cấu hình nâng cấp máy **Windows Server 2012 R2 / 2016** thành máy chủ điều khiển vùng **Domain Controller (Active Directory Domain Services - AD DS)**, cấu hình **DNS Server**, tạo tài khoản người dùng trên Domain, cấu hình máy **Client Windows 7 (1)** và **Windows 7 (2)** gia nhập Domain (Join Domain), đăng nhập xác thực tập trung và **bộ quy trình kiểm tra nghiệm thu toàn diện (Verification & Audit)**.

---

# 📋 BẢNG THÔNG SỐ CẤU HÌNH HỆ THỐNG (GIỮ NGUYÊN DẢI MẠNG ĐANG DÙNG)

> 💡 **Quy hoạch mạng đồng bộ với Lab 1 và Lab 2 (1-4):**

| Thiết bị / Máy ảo | Card mạng (VMware) | Địa chỉ IP (IPv4) | Subnet Mask | Default Gateway | Preferred DNS Server | Tên máy / Vai trò |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Windows Server** | `VMnet11` (LAN 1) | **`192.168.11.1`** | `255.255.255.0` | *(Để trống)* | **`127.0.0.1`** (hoặc `192.168.11.1`) | **DC-SERVER** (Domain Controller) |
| **Windows Server** | `VMnet12` (LAN 2) | **`100.100.11.1`** | `255.255.255.0` | *(Để trống)* | *(Để trống)* | Card mạng định tuyến phụ |
| **Client Win 7 (1)** | `VMnet11` | **`192.168.11.2`** | `255.255.255.0` | `192.168.11.1` | **`192.168.11.1`** *(Bắt buộc)* | **WIN7-PC1** (Domain Member) |
| **Client Win 7 (2)** | `VMnet12` | **`100.100.11.2`** | `255.255.255.0` | `100.100.11.1` | **`100.100.11.1`** *(Bắt buộc)* | **WIN7-PC2** (Domain Member) |

---

### 🔑 THÔNG TIN DOMAIN & TÀI KHOẢN:
* **Tên miền gốc (Root Domain Name)**: **`newstar.vn`** (hoặc `iuh.edu.vn` / `lab.local`)
* **Tên NetBIOS Domain**: **`NEWSTAR`**
* **Tài khoản Domain Administrator**:
  * **User**: `Administrator` (hoặc `NEWSTAR\Administrator`)
  * **Password**: `123` (hoặc `Longko0!`)
* **Tài khoản người dùng mẫu trên Domain**:
  * **User**: `hiepdh` (Họ tên: `Hiep Dang`, Logon name: `hiepdh@newstar.vn`)
  * **Password**: `123` (hoặc `abc@123`)

---

# 🌐 SƠ ĐỒ MÔ HÌNH MẠNG LAB

![Sơ đồ mô hình mạng](image/huong_dan_trien_khai_domain/image_01.jpeg)

---

# PHẦN 1: CẤU HÌNH TRÊN MÁY WINDOWS SERVER (NÂNG CẤP DOMAIN CONTROLLER)

### BƯỚC 1: KIỂM TRA ĐẶT IP TĨNH VÀ TRỎ DNS CHO SERVER
1. Mở **Network and Sharing Center** ➔ **Change adapter settings**.
2. Nhấp chuột phải vào card mạng `VMnet11` ➔ Chọn **Properties** ➔ Nhấp đúp vào **Internet Protocol Version 4 (TCP/IPv4)**.
3. Thiết lập thông số:
   * **IP address**: `192.168.11.1`
   * **Subnet mask**: `255.255.255.0`
   * **Preferred DNS server**: **`127.0.0.1`** (hoặc `192.168.11.1` - *Bắt buộc trỏ về chính mình để làm DNS Server*).
4. Nhấn **OK** ➔ **OK**.

![Đặt IP và DNS Server](image/huong_dan_trien_khai_domain/image_02.png)

---

### BƯỚC 2: CÀI ĐẶT ROLE ACTIVE DIRECTORY DOMAIN SERVICES (AD DS)
1. Mở **Server Manager** ➔ Bấm vào **Manage** ở góc phải trên ➔ Chọn **Add Roles and Features**.
2. Bấm **Next** ➔ Chọn **Role-based or feature-based installation** ➔ Bấm **Next**.
3. Chọn Server hiện tại trong danh sách ➔ Bấm **Next**.
4. Tại trang **Server Roles**: Tích chọn vào mục **`Active Directory Domain Services`**.
   * Khi hộp thoại phụ hiện lên, bấm **Add Features** ➔ Bấm **Next**.
5. Các trang tiếp theo bấm **Next** theo mặc định ➔ Tại trang Confirm, bấm **Install**.
6. Chờ quá trình cài đặt hoàn tất (Feature installation succeeded).

![Cài đặt dịch vụ AD DS](image/huong_dan_trien_khai_domain/image_03.jpeg)

---

### BƯỚC 3: NÂNG CẤP SERVER LÊN DOMAIN CONTROLLER (PROMOTE TO DOMAIN CONTROLLER)
1. Trong cửa sổ **Server Manager**, nhấp vào biểu tượng **lá cờ cảnh báo màu vàng** ở góc trên cùng.
2. Bấm vào dòng chữ màu xanh: **`Promote this server to a domain controller`**.

![Promote Server to Domain Controller](image/huong_dan_trien_khai_domain/image_04.png)

3. **Tại trang Deployment Configuration**:
   * Tích chọn vào tùy chọn thứ 3: **`Add a new forest`** *(Tạo một Forest mới)*.
   * Ô **Root domain name**: Điền tên miền: **`newstar.vn`** (hoặc `iuh.edu.vn`).
   * Bấm **Next**.

![Nhập tên Root Domain](image/huong_dan_trien_khai_domain/image_05.jpeg)

4. **Tại trang Domain Controller Options**:
   * Forest functional level & Domain functional level: Để mặc định (*Windows Server 2012 R2*).
   * Đảm bảo đã tích: **Domain Name System (DNS) server** và **Global Catalog (GC)**.
   * **Directory Services Restore Mode (DSRM) password**: Điền mật khẩu khôi phục (ví dụ: `123` hoặc `abc@123`).
   * Bấm **Next**.

5. **Các trang tiếp theo**:
   * **DNS Options**: Bấm **Next** (bỏ qua cảnh báo DNS delegation).
   * **Additional Options**: Chờ hệ thống tự điền NetBIOS domain name là **`NEWSTAR`** ➔ Bấm **Next**.
   * **Paths**: Để mặc định thư mục cơ sở dữ liệu `NTDS` và `SYSVOL` ➔ Bấm **Next**.
   * **Review Options**: Kiểm tra lại thông tin ➔ Bấm **Next**.
   * **Prerequisites Check**: Hệ thống kiểm tra điều kiện cài đặt. Khi thấy dòng chữ xanh *"All prerequisite checks passed successfully"* ➔ Bấm **Install**.

6. Máy Server sẽ tự động cài đặt và **tự động Restart (Khởi động lại)**.
7. Sau khi khởi động lại, màn hình đăng nhập Server sẽ đổi thành: **`NEWSTAR\Administrator`**. Đăng nhập bằng mật khẩu của bạn (`123` hoặc `Longko0!`).

---

### BƯỚC 4: TẠO TÀI KHOẢN NGƯỜI DÙNG TRÊN DOMAIN (DOMAIN USER)
1. Trên Server, mở **Server Manager** ➔ Vào menu **Tools** ở góc phải trên ➔ Chọn **`Active Directory Users and Computers`** (hoặc bấm `Windows + R` gõ `dsa.msc`).
2. Mở rộng cây tên miền **`newstar.vn`** bên cột trái.
3. Nhấp chọn thư mục (OU) **`Users`**.
4. Nhấp chuột phải vào vùng trống ➔ Chọn **`New`** ➔ **`User`**.
5. Nhập thông tin người dùng mẫu:
   * **First name**: `Hiep`
   * **Last name**: `Dang`
   * **Full name**: `Hiep Dang`
   * **User logon name**: **`hiepdh`** `@newstar.vn`
   * Bấm **Next**.
6. Đặt mật khẩu:
   * **Password**: `123` (hoặc `abc@123`)
   * **Confirm password**: `123` (hoặc `abc@123`)
   * **Bỏ tích**: `User must change password at next logon`.
   * **Tích chọn**: `Password never expires`.
   * Bấm **Next** ➔ Bấm **Finish**.

![Tạo tài khoản Domain User](image/huong_dan_trien_khai_domain/image_06.png)

---

# PHẦN 2: CẤU HÌNH TRÊN MÁY CLIENT WIN 7 (1) GIA NHẬP DOMAIN (JOIN DOMAIN)

### BƯỚC 1: KIỂM TRA ĐẶT IP VÀ TRỎ DNS VỀ DOMAIN CONTROLLER
1. Trên máy **Win 7 (1)**, mở `ncpa.cpl` (Network Connections).
2. Chuột phải vào card mạng ➔ **Properties** ➔ **Internet Protocol Version 4 (TCP/IPv4)**.
3. Thiết lập thông số:
   * **IP address**: `192.168.11.2`
   * **Subnet mask**: `255.255.255.0`
   * **Default gateway**: `192.168.11.1`
   * **Preferred DNS server**: **`192.168.11.1`** *(QUAN TRỌNG NHẤT: Bắt buộc phải trỏ đúng về IP của Server để phân giải được tên miền newstar.vn)*.
4. Bấm **OK** ➔ **OK**.
5. Mở CMD trên Win 7, gõ kiểm tra: `ping newstar.vn` ➔ Phải thấy phản hồi từ `192.168.11.1` là chuẩn 100%!

![Đặt IP và trỏ DNS trên Client](image/huong_dan_trien_khai_domain/image_07.png)

---

### BƯỚC 2: ĐỔI TÊN MÁY THÀNH WIN7-PC1 VÀ GIA NHẬP DOMAIN
1. Trên máy **Win 7 (1)**, nhấp chuột phải vào biểu tượng **Computer** ➔ Chọn **`Properties`**.
2. Tại mục *Computer name, domain, and workgroup settings*, bấm vào dòng chữ: **`Change settings`**.
3. Hộp thoại *System Properties* hiện ra, bấm vào nút **`Change...`**.
4. Tại ô **Computer name**: Đặt tên là **`WIN7-PC1`**.
5. Tại mục **Member of**:
   * Tích chọn vào ô: **`Domain`**.
   * Nhập tên miền: **`newstar.vn`**.
   * Bấm nút **OK**.

![Nhập tên miền Join Domain](image/huong_dan_trien_khai_domain/image_08.jpeg)

6. Hộp thoại **Windows Security** hiện lên yêu cầu xác thực:
   * **User name**: **`administrator`** (hoặc `newstar.vn\administrator`)
   * **Password**: **`123`**
   * Bấm **OK**.
7. Khi thấy thông báo: **`Welcome to the newstar.vn domain.`** ➔ Bấm **OK** ➔ Bấm **`Restart Now`**.

---

### BƯỚC 3: ĐĂNG NHẬP BẰNG TÀI KHOẢN DOMAIN TRÊN CLIENT WIN 7 (1)
1. Sau khi máy Win 7 (1) khởi động lại:
2. Nhấn nút **`Switch User`** ➔ Chọn **`Other User`**.
3. Quan sát thấy dòng chữ: **`Log on to: NEWSTAR`**.
4. Nhập thông tin tài khoản Domain:
   * **User name**: **`hiepdh`** (hoặc `newstar\hiepdh`)
   * **Password**: **`123`**
5. Nhấn **Enter** ➔ Máy Win 7 sẽ chuẩn bị màn hình Desktop mới cho tài khoản Domain User!

![Đăng nhập tài khoản Domain hiepdh](image/huong_dan_trien_khai_domain/image_11.jpeg)

---

# PHẦN 3: CẤU HÌNH TRÊN MÁY CLIENT WIN 7 (2) GIA NHẬP DOMAIN

### BƯỚC 1: ĐẶT IP VÀ DNS TRÊN WIN 7 (2) (DẢI MẠNG VMNET12)
1. Trên máy **Win 7 (2)**, mở card mạng đặt IP tĩnh:
   * **IP address**: `100.100.11.2`
   * **Subnet mask**: `255.255.255.0`
   * **Default gateway**: `100.100.11.1`
   * **Preferred DNS server**: **`100.100.11.1`** (hoặc `192.168.11.1`).
2. Mở CMD test: `ping newstar.vn` ➔ Có phản hồi thành công.

![Đặt IP và DNS Client 2](image/huong_dan_trien_khai_domain/image_10.png)

---

### BƯỚC 2: ĐỔI TÊN MÁY THÀNH WIN7-PC2 VÀ JOIN DOMAIN
1. Mở **Computer Properties** ➔ **Change settings** ➔ **Change...**.
2. Tại ô **Computer name**: Đặt tên là **`WIN7-PC2`** *(Bắt buộc khác tên WIN7-PC1 để không bị xung đột SID)*.
3. Tích chọn **Domain**: Nhập `newstar.vn` ➔ Bấm **OK**.
4. Nhập tài khoản quản trị Domain: `administrator` / pass `123`.
5. Báo **Welcome to the newstar.vn domain** ➔ Bấm **OK** ➔ Restart máy.
6. Sau khi khởi động lại, đăng nhập bằng tài khoản:
   * **`hiepdh`** (Mật khẩu: `123`) hoặc **`NEWSTAR\Administrator`** (Mật khẩu: `123`).

![Đăng nhập Administrator Domain trên Client](image/huong_dan_trien_khai_domain/image_12.jpeg)

---

# PHẦN 4: HƯỚNG DẪN CHẠY BỘ SCRIPT TỰ ĐỘNG HÓA 100% (AUTOMATION SCRIPTS)

Bộ script tự động hóa được chuẩn hóa và lưu tại thư mục `lab2-t2`:

| Tên File Script | Nơi thực thi | Chức năng tự động |
| :--- | :--- | :--- |
| **`01_cai_dat_adds_va_promote_dc.ps1`** | **Windows Server** | Cài đặt AD DS, DNS Server và tự động nâng cấp Domain Controller `newstar.vn`. |
| **`02_tao_domain_users_va_groups.ps1`** | **Windows Server** | Tự động tạo tài khoản Domain User `hiepdh` (Pass: `123`, PasswordNeverExpires). |
| **`03_client1_join_domain.bat`** | **Win 7 (1)** | Cấu hình DNS, kiểm tra kết nối, đổi tên `WIN7-PC1` và Join Domain `newstar.vn`. |
| **`03_client2_join_domain.bat`** | **Win 7 (2)** | Cấu hình DNS, kiểm tra kết nối, đổi tên `WIN7-PC2` và Join Domain `newstar.vn`. |
| **`04_kiem_tra_he_thong_toan_dien.ps1`** | **Quản trị / Server** | Tự động quét toàn bộ trạng thái DC, Users, Computers, SPN và Secure Channel. |

### Cách chạy từng script:

1. **Trên Server (Nâng cấp Domain Controller)**:
   ```powershell
   powershell -ExecutionPolicy Bypass -File "d:\folder\rac\iuh\môn\hk1-4\quản trị và bảo trì hệ thống\lab\lab2-t2\01_cai_dat_adds_va_promote_dc.ps1"
   ```

2. **Trên Server (Tạo tài khoản Domain User)**:
   ```powershell
   powershell -ExecutionPolicy Bypass -File "d:\folder\rac\iuh\môn\hk1-4\quản trị và bảo trì hệ thống\lab\lab2-t2\02_tao_domain_users_va_groups.ps1"
   ```

3. **Trên Client Win 7 (1) & Win 7 (2)**:
   * Chuột phải file `03_client1_join_domain.bat` (hoặc `03_client2_join_domain.bat`) ➔ Chọn **Run as administrator**.

4. **Kiểm tra nghiệm thu toàn bộ bài Lab**:
   ```powershell
   powershell -ExecutionPolicy Bypass -File "d:\folder\rac\iuh\môn\hk1-4\quản trị và bảo trì hệ thống\lab\lab2-t2\04_kiem_tra_he_thong_toan_dien.ps1"
   ```

---

# PHẦN 5: CÁC LỆNH VÀ THAO TÁC KIỂM TRA ĐÃ XÁC THỰC THÀNH CÔNG (VERIFICATION & AUDIT)

Để đảm bảo toàn bộ hệ thống đạt điểm tối đa và không có lỗi tiềm ẩn, dưới đây là các phương pháp kiểm tra toàn diện:

### 1. Kiểm tra 1-Click bằng Script tự động `04_kiem_tra_he_thong_toan_dien.ps1`:
Khi chạy script `04_kiem_tra_he_thong_toan_dien.ps1`, toàn bộ hệ thống sẽ được quét và trả về kết quả đạt chuẩn như sau:

```powershell
==========================================================================
     KIEM TRA TOAN DIEN HE THONG DOMAIN CONTROLLER & CLIENTS (LAB 2-T2)  
==========================================================================

1. THONG TIN DOMAIN CONTROLLER:
  - Ten mien (Domain Name)       : newstar.vn
  - NetBIOS Name                 : NEWSTAR
  - Domain Mode                  : Windows2012R2Domain
  - PDC Emulator                 : WIN-P6PG9M9AICK.newstar.vn

2. DANH SACH MAY TINH TRONG ACTIVE DIRECTORY (COMPUTERS):
Name            DNSHostName                Enabled
----            -----------                -------
WIN-P6PG9M9AICK WIN-P6PG9M9AICK.newstar.vn    True
WIN7-PC1        WIN7-PC1.newstar.vn           True
WIN7-PC2        WIN7-PC2.newstar.vn           True

3. DANH SACH NGUOI DUNG TRONG DOMAIN (USERS):
Name          SamAccountName UserPrincipalName Enabled
----          -------------- ----------------- -------
Administrator Administrator                       True
Hiep Dang     hiepdh         hiepdh@newstar.vn    True

4. KIEM TRA KENH BAO MAT (SECURE CHANNEL) TU MAY CLIENT:
  [+] May WIN7-PC1 (192.168.11.2):
      - Ten may thuc te : WIN7-PC1
      - Domain ket noi  : newstar.vn
      - PartOfDomain    : True
      - Secure Channel  : True (HOẠT ĐỘNG HOÀN HẢO)
  [+] May WIN7-PC2 (100.100.11.2):
      - Ten may thuc te : WIN7-PC2
      - Domain ket noi  : newstar.vn
      - PartOfDomain    : True
      - Secure Channel  : True (HOẠT ĐỘNG HOÀN HẢO)

==========================================================================
                     KIEM TRA HOAN TAT! (100% SUCCESS)
==========================================================================
```

---

### 2. Kiểm tra thủ công chi tiết từng thành phần:

#### A. Kiểm tra trên máy chủ Domain Controller (Windows Server):
1. **Kiểm tra 5 vai trò FSMO (Flexible Single Master Operations)**:
   * Mở CMD trên Server gõ:
     ```cmd
     netdom query fsmo
     ```
   * **Kết quả chuẩn**: Cả 5 vai trò (*Schema master, Domain naming master, PDC, RID pool manager, Infrastructure master*) đều trỏ về tên máy chủ DC.
2. **Kiểm tra dịch vụ DNS Server**:
   * Mở CMD gõ:
     ```cmd
     nslookup newstar.vn
     nslookup 192.168.11.1
     ```
   * **Kết quả chuẩn**: Trả về đúng địa chỉ IP `192.168.11.1` của máy chủ DC.
3. **Kiểm tra danh bạ Active Directory**:
   * Mở `dsa.msc` ➔ Thư mục **`Computers`** có cả 2 máy: **`WIN7-PC1`** và **`WIN7-PC2`**.
   * Thư mục **`Users`** có tài khoản **`hiepdh`**.

#### B. Kiểm tra trên các máy Client (Win 7 - 1 và Win 7 - 2):
1. **Kiểm tra thông tin đăng nhập tài khoản Domain**:
   * Mở CMD trên Win 7 gõ:
     ```cmd
     whoami
     ```
   * **Kết quả chuẩn**: Hiển thị **`newstar\hiepdh`** (hoặc `newstar\administrator`).
2. **Kiểm tra thông tin Domain của máy trạm**:
   * Mở CMD gõ:
     ```cmd
     net config workstation
     ```
   * **Kết quả chuẩn**:
     * *Workstation domain*: **`NEWSTAR`**
     * *Logon domain*: **`NEWSTAR`**
     * *Workstation Domain DNS Name*: **`newstar.vn`**
3. **Kiểm tra biến môi trường Logon Server**:
   * Mở CMD gõ:
     ```cmd
     echo %LOGONSERVER%
     ```
   * **Kết quả chuẩn**: Hiển thị tên máy chủ DC (ví dụ: `\\WIN-P6PG9M9AICK` hoặc `\\DC-SERVER`).
4. **Kiểm tra kênh bảo mật tin cậy (Secure Channel)**:
   * Mở PowerShell trên Win 7 gõ:
     ```powershell
     Test-ComputerSecureChannel -Verbose
     ```
   * **Kết quả chuẩn**: Hiển thị dòng chữ:
     `VERBOSE: "The secure channel between 'WIN7-PC1' and 'newstar.vn' is alive and working correctly."`
     `True`

---

# PHẦN 6: CÁC LỖI THỰC TẾ THƯỜNG GẶP VÀ CÁCH XỬ LÝ TRIỆT ĐỂ (TROUBLESHOOTING)

### ❌ LỖI 1: Trùng tên máy tính do Clone từ cùng một máy ảo Win 7 gốc
* **Hiện tượng**: Cả 2 máy Win 7 khi bật lên đều mang tên mặc định ngẫu nhiên giống nhau (ví dụ: `WIN-RKVRS24A9VK`). Khi máy Win 7 (2) gia nhập Domain thì máy Win 7 (1) bị văng và báo lỗi Trust relationship (hoặc ngược lại).
* **Nguyên nhân**: Active Directory quản lý máy tính bằng tài khoản máy (Computer Account - SAMAccountName). Khi 2 máy cùng tên và cùng SID gia nhập Domain, máy sau sẽ đè lên mật khẩu bảo mật (Machine Secret) của máy trước.
* **Cách khắc phục**:
  1. Unjoin máy về `WORKGROUP` trước.
  2. Đổi tên máy thành **`WIN7-PC1`** cho Client 1 và **`WIN7-PC2`** cho Client 2.
  3. Khởi động lại máy rồi mới tiến hành Join Domain `newstar.vn`.

---

### ❌ LỖI 2: "The trust relationship between this workstation and the primary domain failed"
* **Hiện tượng**: Tại màn hình đăng nhập Client, nhập tài khoản `hiepdh` / pass `123` nhưng bị báo lỗi vi phạm quan hệ tin cậy với Domain.
* **Nguyên nhân**: Kênh tin cậy (Secure Channel) giữa Client và Server bị mất đồng bộ mật khẩu máy tính.
* **Cách khắc phục**:
  * Chạy lệnh sửa kênh tin cậy trên Client bằng PowerShell:
    ```powershell
    Test-ComputerSecureChannel -Repair -Credential (Get-Credential)
    ```
  * Hoặc chạy file `03_client1_join_domain.bat` / `03_client2_join_domain.bat` để script tự động tái tạo kết nối sạch.

---

### ❌ LỖI 3: "The security database on the server does not have a computer account for this workstation trust relationship"
* **Hiện tượng**: Không tìm thấy tài khoản máy tính trên cơ sở dữ liệu Domain Controller khi đăng nhập.
* **Nguyên nhân**: Tài khoản máy tính bị thiếu thuộc tính Kerberos SPN (`ServicePrincipalNames`) hoặc `DNSHostName` trên Active Directory.
* **Cách khắc phục**:
  * Trên Server, mở PowerShell chạy lệnh:
    ```powershell
    Set-ADComputer -Identity "WIN7-PC1" -DNSHostName "WIN7-PC1.newstar.vn" -ServicePrincipalNames @{ Add = @("HOST/WIN7-PC1", "HOST/WIN7-PC1.newstar.vn") }
    ```

---

### ❌ LỖI 4: Không thấy nút "Switch User" hoặc "Other User" trên màn hình đăng nhập
* **Hiện tượng**: Màn hình đăng nhập Win 7 chỉ hiện tài khoản cục bộ (`Administrator` / `Neko`), không thấy chỗ gõ User Domain `hiepdh`.
* **Nguyên nhân**: Máy tính đang ở chế độ Workgroup, chưa Join Domain thành công.
* **Cách khắc phục**:
  * Kiểm tra lại Preferred DNS Server trên Client đã trỏ đúng về IP của Server (`192.168.11.1` hoặc `100.100.11.1`) chưa.
  * Mở CMD gõ `ping newstar.vn` xem có phản hồi không.
  * Chạy file `03_client1_join_domain.bat` (hoặc `03_client2_join_domain.bat`) và khởi động lại máy.

---

# PHẦN 7: DANH SÁCH ẢNH MINH CHỨNG BÁO CÁO THỰC HÀNH (ĐIỂM 10)

Để hoàn thiện bài báo cáo nộp giáo viên đạt điểm tối đa, chụp các ảnh sau:

1. **Ảnh 1 (Server)**: Mở `dsa.msc` ➔ Thư mục **`Computers`** hiển thị cả 2 máy **`WIN7-PC1`** và **`WIN7-PC2`**.
2. **Ảnh 2 (Server)**: Mở `dsa.msc` ➔ Thư mục **`Users`** hiển thị tài khoản **`hiepdh`**.
3. **Ảnh 3 (Win 7 - 1)**: Mở CMD gõ `whoami` (kết quả `newstar\hiepdh`) và `ipconfig /all`.
4. **Ảnh 4 (Win 7 - 2)**: Mở CMD gõ `whoami` (kết quả `newstar\hiepdh`) và `ipconfig /all`.
5. **Ảnh 5 (Tổng quan)**: Kết quả chạy script `04_kiem_tra_he_thong_toan_dien.ps1` hiển thị toàn bộ hệ thống `True` (Pass).

---

# PHẦN 8: CHECKLIST NGHIỆM THU ĐIỂM 10 BÀI LAB 2-T2

- [x] **Windows Server** đã nâng cấp thành công Domain Controller `newstar.vn`.
- [x] **DNS Server** hoạt động bình thường, phân giải chính xác `newstar.vn`.
- [x] **Active Directory Users and Computers (`dsa.msc`)** có đủ:
  - Thư mục **`Users`**: Có tài khoản `hiepdh` (và các user theo yêu cầu).
  - Thư mục **`Computers`**: Có cả **`WIN7-PC1`** và **`WIN7-PC2`**.
- [x] **Client Win 7 (1)** (`192.168.11.2`): Đăng nhập thành công tài khoản `hiepdh`, mở CMD gõ `whoami` hiện `newstar\hiepdh`.
- [x] **Client Win 7 (2)** (`100.100.11.2`): Đăng nhập thành công tài khoản `hiepdh`, mở CMD gõ `whoami` hiện `newstar\hiepdh`.
- [x] Cả 2 máy Client đều có `Test-ComputerSecureChannel` = **`True`** (Kênh tin cậy hoạt động hoàn hảo 100%).
