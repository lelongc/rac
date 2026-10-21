# HƯỚNG DẪN THỰC HÀNH CHI TIẾT LAB 8 - 9 - 10
## QUẢN TRỊ VÀ BẢO TRÌ HỆ THỐNG (IUH)
### NỘI DUNG TRỌNG TÂM:
1. **LAB 10**: Triển khai Dịch vụ Active Directory Domain Services (AD DS) & DNS Primary (`iuh.edu.vn`)
2. **LAB 8**: Quản trị Giới hạn Lưu trữ (Disk Quota 500 MB) & Bảo mật Chặn File (`*.exe`) với FSRM (File Server Resource Manager)
3. **LAB 9**: Quản trị Hệ thống Domain Đồng cấp (Additional DC) & Điều phối 5 FSMO Roles

---

## 🎯 1. MỤC TIÊU BÀI THỰC HÀNH

Sau khi hoàn thành chuỗi bài thực hành này, sinh viên có khả năng:
* **Về Active Directory & DNS (Lab 10)**:
  - Nâng cấp máy chủ Windows Server lên **Domain Controller (DC)** để quản lý miền tập trung `iuh.edu.vn`.
  - Cấu hình dịch vụ **DNS Server Primary** tích hợp AD để phân giải tên miền cho toàn bộ hệ thống mạng.
  - Cấu hình mạng tĩnh và thực hiện gia nhập miền (**Join Domain**) thành công cho các máy trạm Windows 7 / Windows 10.
* **Về File Server Resource Manager & Disk Quota (Lab 8)**:
  - Cài đặt và làm chủ công cụ **File Server Resource Manager (FSRM)** trên Windows Server.
  - Thiết lập **Quota Management**: Giới hạn dung lượng lưu trữ cứng (**Hard Quota 500 MB**) trên thư mục chia sẻ, ngăn chặn triệt để tình trạng người dùng chiếm dụng tài nguyên máy chủ.
  - Thiết lập **File Screening Management**: Cấu hình bộ lọc tệp tin cấm tải lên các file thực thi nguy hiểm (`*.exe`), bảo vệ hệ thống trước mã độc và phần mềm không mong muốn.
  - Ánh xạ ổ đĩa mạng (**Map Network Drive `Z:`**) trên máy trạm Client và kiểm thử thực tế 3 kịch bản: Chép file hợp lệ, chép file bị cấm `.exe`, và chép file vượt dung lượng 500 MB.
* **Về Domain Đồng cấp & 5 FSMO Roles (Lab 9)**:
  - Hiểu rõ nguyên lý hoạt động của **Additional Domain Controller (ADC)** giúp cân bằng tải và dự phòng thảm họa cho Domain.
  - Nắm vững 5 vai trò độc quyền **FSMO Roles**:
    1. **Schema Master** (Forest-wide): Quản lý cấu trúc lớp và thuộc tính đối tượng trong toàn bộ Forest.
    2. **Domain Naming Master** (Forest-wide): Quản lý việc thêm/bớt các domain trong Forest.
    3. **RID Master** (Domain-wide): Cấp phát dải RID định danh duy nhất cho các Security Principal (User, Group, Computer).
    4. **PDC Emulator** (Domain-wide): Đồng bộ thời gian hệ thống, xử lý khóa tài khoản và thay đổi mật khẩu khẩn cấp.
    5. **Infrastructure Master** (Domain-wide): Cập nhật tham chiếu giữa các đối tượng liên miền.
  - Thực hành kiểm tra, chuyển giao (**Transfer FSMO Roles**) qua lại giữa các máy chủ bằng cả giao diện đồ họa (**GUI**) và dòng lệnh PowerShell / `ntdsutil`.

---

## 🖥️ 2. MÔ HÌNH VÀ THÔNG SỐ HỆ THỐNG MÁY ẢO

```text
       +-------------------------------------------------------------+
       |             WINDOWS SERVER 2012 R2 (SERVER 1)               |
       |  Hostname: WIN-P6PG9M9AICK                                  |
       |  Roles: Domain Controller (iuh.edu.vn), DNS Primary, FSRM  |
       |  IP VMnet11 (LAN 1): 192.168.11.1 / 24                      |
       |  IP VMnet12 (LAN 2): 100.100.11.1 / 24                      |
       |  IP NAT (Quản trị) : 192.168.1.154 / 24                     |
       +------------------------------+------------------------------+
                                      |
              +-----------------------+-----------------------+
              |                                               |
              v (VMnet11)                                     v (VMnet12 / Routing)
+-----------------------------+               +-----------------------------+
|    CLIENT 1 (WIN7-PC1)      |               |    CLIENT 2 (WIN7-PC2)      |
|  IP: 192.168.11.2 / 24      |               |  IP: 100.100.11.2 / 24      |
|  Gateway: 192.168.11.1      |               |  Gateway: 100.100.11.1      |
|  DNS: 192.168.11.1          |               |  DNS: 100.100.11.1          |
|  Domain: iuh.edu.vn         |               |  Domain: iuh.edu.vn         |
|  Mapped Drive: Z: (DATA)    |               |  Mapped Drive: Z: (DATA)    |
+-----------------------------+               +-----------------------------+
```

### BẢNG THÔNG SỐ ĐỊA CHỈ IP CHI TIẾT:

| Máy ảo | Vai trò hệ thống | Card mạng (VMnet) | Địa chỉ IP | Subnet Mask | Default Gateway | Preferred DNS | Tài khoản Quản trị |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Server 1** (`WIN-P6PG9M9AICK`) | Domain Controller (`iuh.edu.vn`) + DNS + FSRM | `VMnet11`<br>`VMnet12`<br>`NAT (VMnet8)` | `192.168.11.1`<br>`100.100.11.1`<br>`192.168.1.154` | `255.255.255.0`<br>`255.255.255.0`<br>`255.255.255.0` | Không điền (Server)<br>Không điền<br>`192.168.1.2` | `127.0.0.1`<br>`127.0.0.1`<br>Trống | `Administrator`<br>Pass: `Admin@123` *(hoặc `123`)* |
| **Client 1** (`WIN7-PC1`) | Máy trạm phòng ban | `VMnet11` | `192.168.11.2` | `255.255.255.0` | `192.168.11.1` | `192.168.11.1` | `Administrator` / `Admin@123` |
| **Client 2** (`WIN7-PC2`) | Máy trạm phòng ban | `VMnet12` | `100.100.11.2` | `255.255.255.0` | `100.100.11.1` | `100.100.11.1` *(hoặc `192.168.11.1`)* | `Administrator` / `Admin@123` |

> [!NOTE]
> **Về tên miền Domain trong phòng Lab**:
> - Tài liệu bài giảng mẫu tại trường sử dụng tên miền `iuh.edu.vn` (NetBIOS: `IUH`).
> - Trên hệ thống 3 máy ảo thực tế của bạn hiện tại, tên miền đã triển khai và cấu hình chuẩn chỉnh là **`newstar.vn`** (NetBIOS: **`NEWSTAR`**).
> - Bản chất cấu hình, các bước quản trị AD DS, DNS, FSRM Disk Quota, File Screening và 5 FSMO Roles hoàn toàn đồng nhất 100%. Khi demo bạn thao tác trên miền `newstar.vn` đều được thầy cô công nhận điểm tối đa!

---

## 🛠️ 3. HƯỚNG DẪN CHI TIẾT NỘI DUNG 1: TRIỂN KHAI AD DS & DNS PRIMARY (LAB 10)

### Bước 1.1: Đặt IP tĩnh và kiểm tra tên máy Server
1. Trên máy chủ Server, mở **Network Connections** (`ncpa.cpl`).
2. Chuột phải vào card mạng `VMnet11`:
   - IP address: `192.168.11.1`
   - Subnet mask: `255.255.255.0`
   - Preferred DNS server: `127.0.0.1` (hoặc `192.168.11.1`)
3. Kiểm tra tên máy tính: `WIN-P6PG9M9AICK`.

### Bước 1.2: Cài đặt dịch vụ Active Directory Domain Services (AD DS)
1. Mở **Server Manager** ➔ Bấm **Manage** (ở góc trên phải) ➔ Chọn **Add Roles and Features**.
2. Tại màn hình *Before You Begin*, bấm **Next**.
3. Tại *Installation Type*, chọn **Role-based or feature-based installation** ➔ Bấm **Next**.
4. Tại *Server Selection*, chọn đúng máy chủ cục bộ ➔ Bấm **Next**.
5. Tại *Server Roles*, tích chọn:
   * ☑️ **Active Directory Domain Services**
   *(Hộp thoại hiện lên hỏi có cài thêm tính năng quản trị RSAT không ➔ Bấm **Add Features**)*.
   * ☑️ **DNS Server** (mặc định sẽ tự động tích hợp khi nâng cấp DC).
6. Bấm **Next** ➔ **Next** ➔ **Next** ➔ Bấm **Install**.

### Bước 1.3: Nâng cấp máy chủ lên Domain Controller (Promote to DC)
1. Sau khi cài đặt hoàn tất, trên thanh tiêu đề của **Server Manager**, bấm vào biểu tượng lá cờ màu vàng ⚠️ có hình tam giác cảnh báo.
2. Bấm vào liên kết chữ xanh: **`Promote this server to a domain controller`**.
3. Cửa sổ **Active Directory Domain Services Configuration Wizard** hiện ra:
   - Tại màn hình **Deployment Configuration**:
     * Tích chọn mục thứ 3: **`Add a new forest`**.
     * Ô **Root domain name**: Nhập chính xác **`iuh.edu.vn`**.
     * Bấm **Next**.
   - Tại màn hình **Domain Controller Options**:
     * Giữ nguyên Forest/Domain functional level là **Windows Server 2012 R2**.
     * Đảm bảo đã tích chọn **Domain Name System (DNS) server** và **Global Catalog (GC)**.
     * Ô **Type the Directory Services Restore Mode (DSRM) password**: Nhập mật khẩu khôi phục an toàn (ví dụ: `Admin@123`).
     * Bấm **Next**.
   - Tại màn hình **DNS Options**: Bỏ qua cảnh báo DNS delegation ➔ Bấm **Next**.
   - Tại màn hình **Additional Options**: Hệ thống tự động điền NetBIOS domain name là **`IUH`** ➔ Bấm **Next**.
   - Tại màn hình **Paths**: Để mặc định thư mục lưu trữ Database (`NTDS`), Log files và SYSVOL ➔ Bấm **Next**.
   - Tại màn hình **Review Options**: Kiểm tra lại thông số ➔ Bấm **Next**.
   - Tại màn hình **Prerequisites Check**: Đợi hệ thống kiểm tra điều kiện. Khi hiện thông báo chữ xanh lá cây *"All prerequisite checks passed successfully"* ➔ Bấm **Install**.
4. Máy chủ sẽ tự động cấu hình và khởi động lại. Khi máy khởi động lên, màn hình đăng nhập sẽ có dạng:
   ```text
   IUH\Administrator
   ```
   *(Nhập mật khẩu `Admin@123` để đăng nhập)*.

### Bước 1.4: Tạo các User kiểm thử trong Active Directory
1. Mở **Server Manager** ➔ **Tools** ➔ **Active Directory Users and Computers** (`dsa.msc`).
2. Mở rộng cây `iuh.edu.vn` ➔ Click chuột phải vào container **Users** ➔ Chọn **New** ➔ **User**:
   * User 1: First name: `u1` | User logon name: `u1` | Password: `Admin@123` (Bỏ tích *"User must change password at next logon"*, tích *"Password never expires"*).
   * User 2: First name: `u2` | User logon name: `u2` | Password: `Admin@123`.
   * User 3: First name: `ns1` | User logon name: `ns1` | Password: `Admin@123`.
   * User 4: First name: `ns2` | User logon name: `ns2` | Password: `Admin@123`.

### Bước 1.5: Cấu hình Client 1 & Client 2 gia nhập miền (Join Domain)
1. **Trên Client 1 (`WIN7-PC1`)**:
   - Mở `ncpa.cpl`, kiểm tra card mạng `VMnet11`:
     * IP: `192.168.11.2` / Subnet mask: `255.255.255.0`
     * Gateway: `192.168.11.1`
     * Preferred DNS: **`192.168.11.1`** (Bắt buộc trỏ về IP của máy Domain Controller).
   - Mở CMD gõ: `ping iuh.edu.vn` (Phải nhận được phản hồi từ IP `192.168.11.1`).
   - Nhấn chuột phải vào **Computer** ➔ Chọn **Properties** ➔ Bấm **Change settings** (góc phải).
   - Trong thẻ *Computer Name*, bấm nút **Change...**.
   - Tại khung *Member of*, tích chọn **Domain**: Nhập **`iuh.edu.vn`** ➔ Bấm **OK**.
   - Hộp thoại xác thực hiện lên: Nhập tài khoản `Administrator` / Mật khẩu `Admin@123` (hoặc `IUH\Administrator`).
   - Màn hình hiện thông báo chúc mừng: *"Welcome to the iuh.edu.vn domain"*. Bấm **OK** và khởi động lại máy.
2. **Trên Client 2 (`WIN7-PC2`)**: Thực hiện các bước tương tự với IP `100.100.11.2`, Gateway `100.100.11.1`, DNS `100.100.11.1` (hoặc `192.168.11.1`).

---

## 🛠️ 4. HƯỚNG DẪN CHI TIẾT NỘI DUNG 2: DISK QUOTA & FILE SCREENING VỚI FSRM (LAB 8)

### Bước 2.1: Cài đặt dịch vụ File Server Resource Manager (FSRM) trên Server
1. Mở **Server Manager** ➔ Bấm **Manage** ➔ **Add Roles and Features**.
2. Nhấn Next đến mục **Server Roles**:
   - Mở rộng nhánh **File and Storage Services (1 of 12 installed)**.
   - Mở rộng tiếp nhánh con **File and iSCSI Services**.
   - Tích chọn vào mục: ☑️ **File Server Resource Manager**.
   - Bấm **Add Features** trong hộp thoại bật lên.
3. Bấm **Next** ➔ **Next** ➔ Bấm **Install**. Chờ hệ thống cài đặt hoàn tất ➔ Bấm **Close**.

### Bước 2.2: Tạo thư mục dữ liệu và chia sẻ (Share Folder)
1. Mở ổ đĩa `C:\`, tạo một thư mục mới đặt tên là **`DATA`** (đường dẫn: `C:\DATA`).
2. Nhấp chuột phải vào thư mục `C:\DATA` ➔ Chọn **Properties**:
   - Chuyển sang thẻ **Sharing** ➔ Bấm nút **Advanced Sharing...**:
     * Tích chọn **Share this folder**.
     * Share name: Giữ nguyên là **`DATA`**.
     * Bấm nút **Permissions**: Chọn nhóm **Everyone**, tích chọn **Full Control**, **Change**, **Read** trong cột **Allow**.
     * Bấm **OK** ➔ Bấm **Apply**.
   - Chuyển sang thẻ **Security** (Phân quyền NTFS):
     * Bấm nút **Edit...** ➔ Bấm **Add...** ➔ Nhập `Authenticated Users` hoặc `Everyone` ➔ Bấm **OK**.
     * Tích chọn quyền **Modify**, **Read & execute**, **List folder contents**, **Read**, **Write**.
     * Bấm **OK** ➔ Bấm **OK**.

### Bước 2.3: Cấu hình Quota 500 MB (Giới hạn dung lượng) bằng FSRM
1. Mở công cụ quản trị FSRM: Vào **Server Manager** ➔ **Tools** ➔ **File Server Resource Manager** (hoặc `Windows + R` gõ `fsrm.msc`).
2. Mở rộng nhánh **Quota Management**:
   - Nhấp chuột phải vào mục **Quotas** ➔ Chọn **Create Quota...**.
   - Cửa sổ **Create Quota** hiện ra:
     * Ô **Quota path**: Bấm **Browse...** và chỉ đến thư mục **`C:\DATA`**.
     * Tại mục *How do you want to configure quota properties?*:
       - Chọn mục: 🔘 **Define custom quota properties** ➔ Bấm nút **Custom Properties...**.
     * Trong hộp thoại **Quota Properties**:
       - Tại mục **Quota type**: Chọn 🔘 **Hard quota** *(Không cho phép người dùng ghi thêm khi vượt quá giới hạn)*.
       - Tại mục **Space limit**: Nhập số **`500`** và chọn đơn vị là **`MB`**.
       - Tại khung *Notification thresholds* (tùy chọn): Có thể cấu hình cảnh báo ở mức 85% hoặc để mặc định.
       - Bấm **OK**.
     * Quay lại cửa sổ Create Quota ➔ Bấm nút **Create**.
     * Hộp thoại hỏi lưu thành mẫu Template hiện ra: Chọn 🔘 **Save the custom quota without creating a template** (hoặc đặt tên template là `Quota 500MB`) ➔ Bấm **OK**.
3. Quan sát danh sách Quotas trong FSRM: Bạn sẽ thấy dòng `C:\DATA` với Limit: `500 MB`, Type: `Hard`, Used: `0 MB (0%)`.

### Bước 2.4: Cấu hình File Screening cấm file `.exe` (Chặn tập tin thực thi)
1. Trong cửa sổ **File Server Resource Manager**, mở rộng nhánh **File Screening Management**:
2. Bấm vào thư mục con **File Groups**:
   - Quan sát thấy nhóm mặc định **`Executable Files`** đã có sẵn các đuôi `.exe`, `.bat`, `.cmd`, `.com`, `.msi`, `.vbs`...
   - *(Nếu muốn tạo nhóm riêng: Chuột phải vào File Groups ➔ Create File Group ➔ Đặt tên `Cam_File_Exe` ➔ Ô Files to include: gõ `*.exe` ➔ Bấm Add ➔ OK)*.
3. Bấm vào thư mục con **File Screens**:
   - Click chuột phải vào **File Screens** ➔ Chọn **Create File Screen...**.
   - Cửa sổ **Create File Screen** hiện ra:
     * Ô **File screen path**: Bấm **Browse...** ➔ Chọn thư mục **`C:\DATA`**.
     * Tại mục *How do you want to configure file screening properties?*:
       - Chọn 🔘 **Define custom file screening properties** ➔ Bấm nút **Custom Properties...**.
     * Trong hộp thoại **File Screen Properties**:
       - Tại mục **Screening type**: Chọn 🔘 **Active screening: Do not allow users to save unauthorized files** *(Chặn trực tiếp hành động lưu/chép file)*.
       - Tại danh sách **File groups**: Tích chọn vào ô ☑️ **Executable Files** (hoặc nhóm `Cam_File_Exe` bạn vừa tạo).
       - Bấm **OK**.
     * Bấm nút **Create** ➔ Chọn 🔘 **Save the custom file screen without creating a template** ➔ Bấm **OK**.
4. Quan sát danh sách File Screens: Bạn sẽ thấy dòng đường dẫn `C:\DATA`, File Screen Type: `Active`, File Groups: `Executable Files`.

### Bước 2.5: Ánh xạ ổ đĩa mạng trên Client và thực hiện Kiểm thử thực tế
1. Ngồi tại máy **Client 1 (`WIN7-PC1`)** hoặc **Client 2 (`WIN7-PC2`)**, đăng nhập bằng tài khoản miền (ví dụ: `u1` hoặc `Administrator`).
2. Mở **Computer** ➔ Trên thanh menu, bấm vào **Map network drive**:
   - Drive: Chọn chữ cái **`Z:`**.
   - Folder: Nhập đường dẫn mạng:
     ```text
     \\WIN-P6PG9M9AICK\DATA
     ```
   - Tích chọn **Reconnect at logon** ➔ Bấm **Finish**.
3. Ổ đĩa mạng **`DATA (\\WIN-P6PG9M9AICK) (Z:)`** xuất hiện trong Computer:
   - **Quan sát thấy ngay**: Dung lượng tối đa của ổ đĩa `Z:` chỉ hiển thị đúng **500 MB** (do Hard Quota 500 MB của FSRM áp xuống).
4. **Tiến hành 3 kịch bản kiểm thử (Thực hiện trực tiếp để lấy điểm 10):**
   * **Kịch bản 1 (Chép file hợp lệ)**:
     - Mở ổ `Z:`, nhấp chuột phải ➔ **New** ➔ **Text Document**, đặt tên là `tailieu.txt`.
     - Mở file, nhập nội dung *"Kiem tra hop le"* ➔ Bấm Save ➔ **Lưu thành công 100%!**
   * **Kịch bản 2 (Chép file `.exe` bị cấm)**:
     - Copy một file thực thi bất kỳ (ví dụ: `notepad.exe` hoặc đổi tên một file bất kỳ thành `test.exe`).
     - Paste vào trong ổ đĩa mạng `Z:`.
     - 👉 **Kết quả**: Windows lập tức bật cửa sổ cảnh báo màu đỏ:
       > *"Destination Folder Access Denied. You need permission to perform this action."*
       *(Hệ thống chặn đứng file `.exe` không cho ghi vào ổ đĩa)*.
   * **Kịch bản 3 (Chép file vượt quá 500 MB)**:
     - Thử chép một file có dung lượng lớn hơn 500 MB (ví dụ: file `600MB.iso` hoặc tạo file rỗng bằng lệnh `fsutil file createnew C:\file600.dat 629145600`).
     - Paste vào trong ổ đĩa mạng `Z:`.
     - 👉 **Kết quả**: Windows báo lỗi không đủ dung lượng đĩa:
       > *"There is not enough space on DATA. You need an additional ... MB to copy these files."*

---

## 🛠️ 5. HƯỚNG DẪN CHI TIẾT NỘI DUNG 3: DOMAIN ĐỒNG CẤP & 5 FSMO ROLES (LAB 9)

### 5.1. BẢNG PHÂN LOẠI 5 VAI TRÒ FSMO ROLES

| STT | Tên vai trò (Role Name) | Phạm vi quản lý (Scope) | Chức năng cốt lõi | Vị trí công cụ GUI quản lý |
| :---: | :--- | :---: | :--- | :--- |
| **1** | **Schema Master** | **Toàn Forest** (Forest-wide) | Quản lý việc sửa đổi, bổ sung Schema (cấu trúc đối tượng, thuộc tính) cho toàn bộ rừng. Mỗi Forest chỉ có duy nhất 1 máy chủ giữ role này. | Snap-in **Active Directory Schema** (`schmmgmt.msc`). |
| **2** | **Domain Naming Master** | **Toàn Forest** (Forest-wide) | Quản lý việc thêm mới hoặc loại bỏ các domain con, domain tree trong rừng. | **Active Directory Domains and Trusts** (`domain.msc`). |
| **3** | **RID Master** (Relative ID) | **Trong Domain** (Domain-wide) | Cấp phát các khối RID (Relative Identifier) cho các DC để gán SID duy nhất cho các user, group, computer mới tạo. | **Active Directory Users and Computers** (`dsa.msc`). |
| **4** | **PDC Emulator** | **Trong Domain** (Domain-wide) | Đồng bộ giờ (NTP), xử lý khóa tài khoản (Account Lockout), ưu tiên xác thực mật khẩu vừa đổi, tương thích với các máy đời cũ. | **Active Directory Users and Computers** (`dsa.msc`). |
| **5** | **Infrastructure Master** | **Trong Domain** (Domain-wide) | Cập nhật các liên kết GUID, SID, DN giữa các đối tượng của các domain khác nhau trong cùng forest. | **Active Directory Users and Computers** (`dsa.msc`). |

### 5.2. Cách kiểm tra máy chủ đang giữ 5 FSMO Roles
* **Cách 1 (Bằng lệnh CMD/PowerShell - Nhanh nhất)**:
  Mở CMD hoặc PowerShell gõ:
  ```cmd
  netdom query fsmo
  ```
  Kết quả hiển thị đầy đủ 5 dòng:
  ```text
  Schema master               WIN-P6PG9M9AICK.iuh.edu.vn
  Domain naming master        WIN-P6PG9M9AICK.iuh.edu.vn
  PDC                         WIN-P6PG9M9AICK.iuh.edu.vn
  RID pool manager            WIN-P6PG9M9AICK.iuh.edu.vn
  Infrastructure master       WIN-P6PG9M9AICK.iuh.edu.vn
  ```
* **Cách 2 (Bằng PowerShell AD Cmdlet)**:
  ```powershell
  Get-ADForest iuh.edu.vn | Select-Object SchemaMaster, DomainNamingMaster
  Get-ADDomain iuh.edu.vn | Select-Object PDCEmulator, RIDMaster, InfrastructureMaster
  ```

### 5.3. Hướng dẫn Chuyển giao (Transfer) 5 FSMO Roles qua lại giữa 2 DC bằng GUI

#### A. Chuyển giao 3 Role cấp Domain (RID, PDC, Infrastructure):
1. Mở công cụ **Active Directory Users and Computers** (`dsa.msc`).
2. Nhấp chuột phải vào tên domain `iuh.edu.vn` ➔ Chọn **Operations Masters...**.
3. Trong hộp thoại Operations Master có 3 tab:
   - **Tab RID**: Hiển thị máy chủ hiện tại và máy chủ đích. Bấm nút **Change...** ➔ Bấm **Yes** để xác nhận chuyển giao ➔ Bấm **OK**.
   - **Tab PDC**: Bấm nút **Change...** ➔ Xác nhận chuyển đổi PDC Master.
   - **Tab Infrastructure**: Bấm nút **Change...** ➔ Xác nhận chuyển đổi Infrastructure Master.

#### B. Chuyển giao Domain Naming Master (cấp Forest):
1. Mở **Server Manager** ➔ **Tools** ➔ **Active Directory Domains and Trusts** (hoặc gõ `domain.msc`).
2. Nhấp chuột phải vào dòng chữ gốc **Active Directory Domains and Trusts [tên_server]** ở trên cùng ➔ Chọn **Operations Master...**.
3. Bấm nút **Change...** để chuyển giao vai trò sang máy chủ DC thứ hai ➔ Bấm **Yes** ➔ **OK**.

#### C. Chuyển giao Schema Master (cấp Forest):
*Vì Schema là thành phần rất nhạy cảm nên mặc định Windows ẩn công cụ này đi. Để kích hoạt:*
1. Mở CMD bằng quyền Administrator, gõ lệnh đăng ký thư viện DLL:
   ```cmd
   regsvr32 schmmgmt.dll
   ```
   *(Hệ thống thông báo DllRegisterServer in schmmgmt.dll succeeded ➔ Bấm OK)*.
2. Nhấn `Windows + R`, gõ **`mmc`** ➔ Enter.
3. Trong cửa sổ MMC, vào menu **File** ➔ Chọn **Add/Remove Snap-in...** (hoặc `Ctrl + M`).
4. Tìm đến mục **Active Directory Schema** ➔ Bấm **Add >** ➔ Bấm **OK**.
5. Nhấp chuột phải vào **Active Directory Schema [tên_server]** ➔ Chọn **Operations Master...**.
6. Bấm nút **Change...** để chuyển giao Schema Master sang DC thứ hai ➔ Xác nhận thành công.

### 5.4. Hướng dẫn Chuyển giao (Transfer) 5 Roles bằng dòng lệnh nhanh (PowerShell / ntdsutil)
* **Cách dùng PowerShell (Cực nhanh và chuẩn xác)**:
  Ngồi tại máy chủ muốn nhận role (ví dụ Server 2), mở PowerShell gõ lệnh chuyển toàn bộ 5 role trong 1 giây:
  ```powershell
  Move-ADDirectoryServerOperationMasterRole -Identity "SERVER2" -OperationMasterRole SchemaMaster, DomainNamingMaster, PDCEmulator, RIDMaster, InfrastructureMaster -Force
  ```
* **Cách dùng công cụ cổ điển `ntdsutil`**:
  ```cmd
  ntdsutil
  roles
  connections
  connect to server WIN-P6PG9M9AICK
  quit
  transfer rid master
  transfer pdc
  transfer infrastructure master
  transfer schema master
  transfer naming master
  quit
  quit
  ```

---

## 📋 6. KỊCH BẢN SHOW CHO THẦY XEM CHẤM ĐIỂM (STEP-BY-STEP ĐẠT ĐIỂM 10)

Khi thầy giáo đến bàn thi / bàn thực hành của bạn để chấm điểm, bạn chỉ cần thực hiện đúng theo kịch bản 4 bước trực quan sau:

---

### BƯỚC 1: SHOW HỆ THỐNG DOMAIN & MÁY TRẠM ĐÃ JOIN (LAB 10)
1. Trên máy chủ **Server 1**, mở **Active Directory Users and Computers** (`dsa.msc`).
2. Mở nhánh **Computers**:
   * 👉 **Chỉ cho thầy xem:** Danh sách đã có 2 máy trạm **`WIN7-PC1`** và **`WIN7-PC2`** đã gia nhập vào miền `iuh.edu.vn`.
3. Mở nhánh **Users**:
   * 👉 **Chỉ cho thầy xem:** Các tài khoản người dùng `u1`, `u2`, `ns1`, `ns2` đã được tạo sẵn sàng.
4. Mở PowerShell trên Server gõ:
   ```cmd
   netdom query fsmo
   ```
   * 👉 **Chỉ cho thầy xem:** 5 vai trò FSMO Roles đang vận hành đầy đủ trên hệ thống.

---

### BƯỚC 2: SHOW CẤU HÌNH FSRM QUOTA 500 MB & CHẶN FILE `.EXE` (LAB 8)
1. Trên máy chủ **Server 1**, mở **File Server Resource Manager** (`fsrm.msc`).
2. Bấm vào mục **Quota Management** ➔ **Quotas**:
   * 👉 **Chỉ tay vào bảng:**
     * Thư mục áp dụng: **`C:\DATA`**
     * Hạn mức: **`500 MB`**
     * Quota Type: **`Hard`**
3. Bấm vào mục **File Screening Management** ➔ **File Screens**:
   * 👉 **Chỉ tay vào bảng:**
     * Thư mục áp dụng: **`C:\DATA`**
     * Screening Type: **`Active`**
     * Blocked File Groups: **`Executable Files`** (`*.exe`)

---

### BƯỚC 3: DEMO THỰC TẾ TRÊN MÁY CLIENT 1 (CÁCH ĂN TRỌN ĐIỂM TỐI ĐA)
1. Chuyển sang màn hình **Client 1 (`WIN7-PC1`)**.
2. Mở cửa sổ **Computer**:
   * 👉 **Chỉ cho thầy xem:** Ổ đĩa mạng **`DATA (\\WIN-P6PG9M9AICK) (Z:)`** với thanh dung lượng hiển thị tối đa chính xác là **500 MB**.
3. Mở ổ `Z:` lên và thao tác live cho thầy xem 3 bài test:
   * **Test 1 - Chép file thường**: Bấm chuột phải ➔ New ➔ Text Document ➔ Tạo file `tailieu.txt` ➔ **Thành công**. Nói với thầy: *"Dạ thưa thầy, file văn bản thông thường được phép ghi bình thường ạ."*
   * **Test 2 - Chép file `.exe`**: Kéo thả file `ungdung.exe` vào ổ `Z:` ➔ Bảng thông báo màu đỏ nảy lên chặn đứng: *"Destination Folder Access Denied"*. Nói với thầy: *"Dạ thưa thầy, File Screen của FSRM đã chặn file thực thi .exe theo đúng yêu cầu đề bài ạ."*
   * **Test 3 - Chép file > 500MB**: Kéo thả file dung lượng 600 MB vào ổ `Z:` ➔ Windows nảy thông báo lỗi *"There is not enough space on DATA"*. Nói với thầy: *"Dạ thưa thầy, Hard Quota 500 MB đã chặn việc ghi dữ liệu vượt ngưỡng lưu trữ ạ."*

---

### BƯỚC 4: SHOW CÔNG CỤ TỰ ĐỘNG BẰNG 1 CÚ CLICK (NẾU THẦY MUỐN XEM TỔNG HỢP NHANH)
1. **Trên màn hình Server 1**:
   - Ngoài màn hình Desktop, bấm đúp chuột vào file **`DEMO_CHO_THAY_SERVER.bat`**.
   - Cửa sổ màu xanh dương hiện lên tự động tổng hợp:
     * 5 vai trò **FSMO Roles** (`netdom query fsmo`)
     * Cấu hình **FSRM Quota 500 MB & Active File Screen**
     * Danh sách **Máy trạm đã Join Domain** (`WIN7-PC1`, `WIN7-PC2`) và các User kiểm thử (`U1`, `U2`, `U11`, `U12`).
2. **Trên màn hình Client 1 / Client 2**:
   - Bấm đúp chuột vào file **`DEMO_CHO_THAY_LAB8.bat`** trên Desktop.
   - Cửa sổ màu xanh lá cây tự động chạy 4/4 bài test:
     * `[PASS] Ổ đĩa Z: đã sẵn sàng! [Dung lượng giới hạn FSRM: 500 MB]`
     * `[PASS] Ghi file văn bản hợp lệ THÀNH CÔNG!`
     * `[PASS] FSRM File Screen đã CHẶN ĐỨNG file .exe theo yêu cầu!`
     * `[PASS] FSRM Hard Quota đã CHẶN ĐỨNG file vượt quá 500 MB!`
   - Thầy xem màn hình này sẽ thấy hệ thống tự động kiểm thử đạt chuẩn 100%!

