# CẨM NANG ÔN TẬP TOÀN DIỆN 10 BÀI LAB - THI THƯỜNG KỲ QTBTHT (IUH)

> **Môn học**: Quản trị và Bảo trì Hệ thống  
> **Trường**: Đại học Công nghiệp TP.HCM (IUH)  
> **Môi trường phòng thi**: 3 máy ảo gồm **Windows Server 2012** + **Client 1 (Win 7)** + **Client 2 (Win 7)**  
> **Mật khẩu chuẩn toàn hệ thống**: `123` (cho cả Server Administrator và Client)

---

## MỤC LỤC 10 BÀI LAB

1. [LAB 1: Cấu hình Định tuyến Router (RRAS) trên Windows Server 2012](#lab-1-cấu-hình-định-tuyến-router-rras)
2. [LAB 2 (Phần 1): Quản trị Local User, Local Group, Security Policy, Share & NTFS](#lab-2-phần-1-quản-trị-local-user-group-security-policy-share--ntfs)
3. [LAB 2 (Phần 2): Nâng cấp Domain Controller (AD DS), Cấu hình DNS & Join Domain](#lab-2-phần-2-nâng-cấp-domain-controller-ad-ds-cấu-hình-dns--join-domain)
4. [LAB 3: Quản trị các Đối tượng trong AD DS (OU, Group, User, Delegation)](#lab-3-quản-trị-các-đối-tượng-trong-ad-ds)
5. [LAB 4: Bảo mật AD DS & Chính sách Người dùng (Password, Lockout, Audit Policy)](#lab-4-bảo-mật-ad-ds--chính-sách-người-dùng)
6. [LAB 5: Quản trị Chia sẻ, Phân quyền Phức hợp (NTFS + Share) & ABE](#lab-5-quản-trị-chia-sẻ-phân-quyền-phức-hợp-ntfs--share--abe)
7. [LAB 6: Triển khai Quản lý Group Policy (GPO Nâng cao)](#lab-6-triển-khai-quản-lý-group-policy-gpo-nâng-cao)
8. [LAB 7: Triển khai Quản lý Hồ sơ Người dùng (User Profile, Roaming, Home Folder)](#lab-7-triển-khai-quản-lý-hồ-sơ-người-dùng-user-profile)
9. [LAB 8: Quản trị Dung lượng Đĩa cứng (Disk Quota) & FSRM File Screening](#lab-8-quản-trị-dung-lượng-đĩa-cứng-disk-quota--fsrm)
10. [LAB 9: Triển khai Domain Đồng cấp (Secondary DC / FSMO Roles / Replication)](#lab-9-triển-khai-domain-đồng-cấp-secondary-dc--fsmo-roles)
11. [LAB 10: Tối ưu hóa Dịch vụ Active Directory & Reverse DNS Lookup](#lab-10-tối-ưu-hóa-dịch-vụ-active-directory--reverse-dns-lookup)

---

## BẢNG THÔNG SỐ MẠNG CHUẨN CỦA 3 MÁY PHÒNG THI

| Máy ảo | Card mạng (VMnet) | Địa chỉ IP | Subnet Mask | Default Gateway | DNS Server |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Server 1** | `VMnet11` (LAN 1) | `192.168.11.1` | `255.255.255.0` | *(Để trống)* | `127.0.0.1` |
| | `VMnet12` (LAN 2) | `100.100.11.1` | `255.255.255.0` | *(Để trống)* | `127.0.0.1` |
| | `NAT / VMnet8` | `192.168.1.151` | `255.255.255.0` | DHCP / NAT Host | *(Để kết nối Host)* |
| **Client 1** | `VMnet11` | `192.168.11.2` | `255.255.255.0` | `192.168.11.1` | `192.168.11.1` |
| **Client 2** | `VMnet12` | `100.100.11.2` | `255.255.255.0` | `100.100.11.1` | `100.100.11.1` |

> **Quy tắc vàng định tuyến**: Máy con thuộc LAN nào thì trỏ Default Gateway về đúng IP của Server tại LAN đó.  
> Khi Client 1 ping Client 2 thành công, giá trị **`TTL = 127`** (giảm 1 qua Router Server) chứng minh định tuyến hoạt động 100%.

---

## LAB 1: CẤU HÌNH ĐỊNH TUYẾN ROUTER (RRAS)

### 1. Mục tiêu & Lý thuyết
- Cấu hình Windows Server 2012 làm Router kết nối 2 phân đoạn mạng LAN 1 (`192.168.11.0/24`) và LAN 2 (`100.100.11.0/24`).
- Tính năng: **Routing and Remote Access (RRAS)**.

### 2. Các bước cấu hình GUI
1. **Server Manager** -> **Add Roles and Features** -> Chọn Role **Remote Access** -> Chọn Role Services: **Routing** (hệ thống tự chọn kèm DirectAccess and VPN).
2. Mở công cụ: **Tools** -> **Routing and Remote Access**.
3. Chuột phải vào tên Server -> Chọn **Configure and Enable Routing and Remote Access**.
4. Chọn **Custom Configuration** -> Tích chọn **LAN routing** -> Next -> Finish -> Nhấn **Start service**.

### 3. Lệnh PowerShell cấu hình siêu tốc
```powershell
Install-WindowsFeature Routing -IncludeManagementTools
Set-Service RemoteAccess -StartupType Automatic
Start-Service RemoteAccess
netsh routing ip add interface "vmnet11"
netsh routing ip add interface "vmnet12"
```

### 4. Kiểm tra nghiệm thu
- Trên Client 1: `ping 100.100.11.2` -> Nhận phản hồi với `TTL=127` (0% loss).
- Trên Client 2: `ping 192.168.11.2` -> Nhận phản hồi với `TTL=127` (0% loss).

---

## LAB 2 (PHẦN 1): QUẢN TRỊ LOCAL USER, GROUP, SECURITY POLICY, SHARE & NTFS

### 1. Quản trị Local User & Group (lusrmgr.msc)
- Tạo User: `net user <TenUser> <MatKhau> /add`
- Tạo Group: `net localgroup <TenNhom> /add`
- Thêm User vào Group: `net localgroup <TenNhom> <TenUser> /add`
- Thiết lập cấm đổi mật khẩu: `net user <TenUser> /passwordchg:no`
- Thiết lập mật khẩu không bao giờ hết hạn: `WMIC USERACCOUNT WHERE "Name='<TenUser>'" SET PasswordExpires=FALSE`

### 2. Local Security Policy (secpol.msc)
- **Account Policies** -> **Password Policy**:
  - `Minimum password length`: Độ dài mật khẩu tối thiểu (ví dụ: 6 hoặc 8 ký tự).
  - `Password must meet complexity requirements`: Bật/Tắt yêu cầu độ phức tạp (chữ hoa, thường, số, ký tự đặc biệt).
  - `Maximum password age`: Thời gian tồn tại tối đa của mật khẩu (ví dụ 30 ngày, 0 = không hết hạn).
- **Account Lockout Policy**:
  - `Account lockout threshold`: Số lần đăng nhập sai thì khóa tài khoản (ví dụ: 3 lần).
  - `Account lockout duration`: Thời gian bị khóa (ví dụ: 15 hoặc 30 phút).

### 3. Phân biệt Quyền Share và Quyền NTFS
| Tiêu chí | Share Permission | NTFS Permission |
| :--- | :--- | :--- |
| **Phạm vi** | Chỉ áp dụng khi truy cập qua mạng (`\\IP\Share`) | Áp dụng cả khi đăng nhập tại chỗ lẫn qua mạng |
| **Định dạng ổ đĩa** | FAT32, NTFS, ReFS | Bắt buộc phải là định dạng **NTFS** |
| **Mức độ chi tiết** | 3 quyền cơ bản: Read, Change, Full Control | Rất chi tiết: Read, Write, Modify, Full Control, List, Traverse... |
| **Quy tắc kết hợp** | **Càng thắt chặt càng ưu tiên (Most Restrictive)**: Nếu Share = Read mà NTFS = Full Control -> Người dùng chỉ có quyền Read qua mạng! |
| **Quy tắc Deny** | **Deny luôn luôn thắng (Deny overrides Allow)**. |

---

## LAB 2 (PHẦN 2): NÂNG CẤP DOMAIN CONTROLLER (AD DS) & JOIN DOMAIN

### 1. Cài đặt AD DS & Promote Domain Controller
```powershell
# 1. Cài đặt Role AD DS
Install-WindowsFeature AD-Domain-Services -IncludeManagementTools

# 2. Nâng cấp thành DC mới trong Forest mới (Domain ví dụ: fit.iuh.edu.vn)
Import-Module ADDSDeployment
Install-ADDSForest `
    -DomainName "fit.iuh.edu.vn" `
    -SafeModeAdministratorPassword (ConvertTo-SecureString "123" -AsPlainText -Force) `
    -InstallDns:$true `
    -Force:$true
```
*(Server sẽ tự động khởi động lại sau khi hoàn tất)*

### 2. Cấu hình máy trạm Windows 7 Join Domain
1. Đặt DNS máy trạm trỏ về IP của Server: `192.168.11.1`.
2. Chuột phải **Computer** -> **Properties** -> **Change settings** -> **Change...**
3. Tích chọn **Domain** -> Nhập tên domain: `fit.iuh.edu.vn`.
4. Nhập user: `Administrator` và pass: `123`.
5. Thông báo: *"Welcome to the fit.iuh.edu.vn domain"* -> Khởi động lại máy trạm.

---

## LAB 3: QUẢN TRỊ CÁC ĐỐI TƯỢNG TRONG AD DS (OU, GROUP, USER, DELEGATION)

### 1. Phân loại Group trong Active Directory
- **Phân loại theo Group Type**:
  - **Security Group**: Dùng để gán quyền truy cập tài nguyên (NTFS, Share, GPO).
  - **Distribution Group**: Chỉ dùng để gửi email nhóm (Exchange), không dùng để phân quyền.
- **Phân loại theo Group Scope**:
  - **Domain Local Group**: Dùng để gom tài nguyên tại Domain hiện tại (quyền hạn chỉ có giá trị trên domain đó).
  - **Global Group**: Dùng để gom người dùng có cùng chức năng (ví dụ: `G_KeToan`, `G_NhanSu`).
  - **Universal Group**: Chứa thành viên từ mọi domain trong Forest.
- **Quy tắc chuẩn phân quyền Microsoft: A-G-DL-P**:
  `Accounts` -> đưa vào `Global Group` -> đưa vào `Domain Local Group` -> gán `Permission` (NTFS/Share).

### 2. Các lệnh PowerShell quản trị AD DS
```powershell
# Tạo OU
New-ADOrganizationalUnit -Name "PhongBan" -Path "DC=fit,DC=iuh,DC=edu,DC=vn"

# Tạo User
New-ADUser -Name "Nguyen Van A" -SamAccountName "nva" -UserPrincipalName "nva@fit.iuh.edu.vn" `
    -Path "OU=PhongBan,DC=fit,DC=iuh,DC=edu,DC=vn" `
    -AccountPassword (ConvertTo-SecureString "123" -AsPlainText -Force) -Enabled $true

# Tạo Group
New-ADGroup -Name "G_KeToan" -GroupScope Global -GroupCategory Security `
    -Path "OU=PhongBan,DC=fit,DC=iuh,DC=edu,DC=vn"

# Thêm User vào Group
Add-ADGroupMember -Identity "G_KeToan" -Members "nva"
```

### 3. Delegation of Control (Ủy quyền quản trị)
- Chuột phải vào OU -> Chọn **Delegate Control...** -> Next.
- Chọn User/Group muốn ủy quyền (ví dụ Trưởng phòng).
- Chọn các quyền thông dụng:
  - *Reset user passwords and force password change at next logon*
  - *Create, delete, and manage user accounts*
  - *Modify the membership of a group*

---

## LAB 4: BẢO MẬT AD DS & CHÍNH SÁCH NGƯỜI DÙNG (GPO SECURITY)

### 1. Default Domain Policy
- Mở **Group Policy Management** (`gpmc.msc`).
- Chuột phải **Default Domain Policy** -> **Edit...**
- Đường dẫn: `Computer Configuration` -> `Policies` -> `Windows Settings` -> `Security Settings` -> `Account Policies`:
  - **Password Policy**:
    - `Enforce password history`: Nhớ số mật khẩu cũ (ngăn dùng lại).
    - `Maximum password age`: Hạn sử dụng mật khẩu.
    - `Minimum password length`: Chiều dài mật khẩu tối thiểu.
  - **Account Lockout Policy**:
    - `Account lockout threshold`: Số lần nhập sai tối đa.
    - `Reset account lockout counter after`: Thời gian reset bộ đếm lần sai.

### 2. Audit Policy (Chính sách giám sát & ghi log)
- Đường dẫn: `Security Settings` -> `Local Policies` -> `Audit Policy`:
  - `Audit logon events`: Ghi log sự kiện đăng nhập (Success & Failure).
  - `Audit account logon events`: Ghi log xác thực tài khoản qua Kerberos.
- Xem log: Mở **Event Viewer** (`eventvwr.msc`) -> **Windows Logs** -> **Security**:
  - Event ID **4624**: Đăng nhập thành công.
  - Event ID **4625**: Đăng nhập thất bại (sai mật khẩu/bị khóa).

---

## LAB 5: QUẢN TRỊ CHIA SẺ, PHÂN QUYỀN PHỨC HỢP (NTFS + SHARE) & ABE

### 1. Mô hình Phân quyền Chuẩn
- **Thư mục dùng chung**: `C:\DuLieu`
  - Share Permission: `Everyone` = **Change** (hoặc Full Control).
  - NTFS Permission:
    - `Administrators`: Full Control.
    - `G_GiamDoc`: Full Control / Modify.
    - `G_NhanVien`: Read & Execute, List folder contents, Read.
    - `CREATOR OWNER`: Full Control (để người tạo file nào thì có toàn quyền sửa/xóa chính file đó).

### 2. Access-Based Enumeration (ABE) - Ẩn thư mục không có quyền
- **Mục đích**: Người dùng chỉ nhìn thấy các thư mục/file mà họ có quyền đọc. Các thư mục họ không có quyền sẽ bị ẩn hoàn toàn, tránh tò mò và tăng tính bảo mật.
- **Cách bật qua GUI**:
  - Mở **Server Manager** -> **File and Storage Services** -> **Shares**.
  - Chuột phải vào Thư mục Share -> Chọn **Properties**.
  - Chọn thẻ **Settings** -> Tích chọn **Enable access-based enumeration** -> OK.

---

## LAB 6: TRIỂN KHAI QUẢN LÝ GROUP POLICY (GPO NÂNG CAO)

### 1. GPO Người dùng phổ biến (User Configuration -> Policies -> Administrative Templates)
- **Cấm Control Panel**: `Control Panel` -> `Prohibit access to Control Panel and PC settings` = **Enabled**.
- **Cấm Task Manager**: `System` -> `Ctrl+Alt+Del Options` -> `Remove Task Manager` = **Enabled**.
- **Cấm Command Prompt (cmd)**: `System` -> `Prevent access to the command prompt` = **Enabled** (chọn No ở Disable cmd script processing để cho phép script chạy ngầm).
- **Cấm đổi hình nền Desktop**: `Desktop` -> `Desktop Wallpaper` = **Enabled** (nhập đường dẫn ảnh `\\Server\Share\wallpaper.jpg`).

### 2. GPO Preferences: Tự động Ánh xạ Ổ đĩa Mạng (Drive Mapping)
- Đường dẫn: `User Configuration` -> `Preferences` -> `Windows Settings` -> `Drive Maps`.
- Chuột phải -> **New** -> **Mapped Drive**:
  - Action: **Update** (hoặc Create).
  - Location: `\\192.168.11.1\DuLieu`
  - Reconnect: Tích chọn.
  - Label as: `O dia Du Lieu Cong Ty`
  - Drive Letter: Chọn chữ cái (ví dụ: `Z:`).
- Lệnh cập nhật chính sách ngay lập tức trên máy trạm:
  ```cmd
  gpupdate /force
  ```

---

## LAB 7: TRIỂN KHAI QUẢN LÝ HỒ SƠ NGƯỜI DÙNG (USER PROFILE)

### 1. Home Folder (Thư mục cá nhân độc lập)
- Trên Server tạo thư mục: `C:\HomeFolder`, Share với tên `Home$` (thêm ký tự `$` để ẩn share trong mạng).
- NTFS trên `C:\HomeFolder`:
  - Tắt kế thừa (Disable Inheritance) -> Bỏ quyền Users thường.
  - Gán `Administrators` = Full Control.
  - Gán `Authenticated Users` = Read & Execute, Create Folders / Append Data (This folder only).
  - Gán `CREATOR OWNER` = Full Control (Subfolders and files only).
- Gán Home Folder cho User trong AD:
  - Mở **ADAC** hoặc **dsa.msc** -> Chuột phải User -> **Properties** -> Thẻ **Profile**.
  - Khung Home folder: Tích **Connect** -> Chọn ổ đĩa (ví dụ `H:`) -> To: `\\Server\Home$\%username%`.
  - Hệ thống sẽ tự tạo thư mục riêng mang tên user với quyền bảo mật tuyệt đối.

### 2. Roaming Profile (Hồ sơ di động)
- Tạo thư mục `C:\Profiles`, Share tên `Profiles$`.
- Trong thẻ Profile của User -> Khung **Profile path**: Nhập `\\Server\Profiles$\%username%`.
- Khi user đăng xuất ở Client 1, toàn bộ Desktop, Documents, AppData được tải lên Server; khi đăng nhập ở Client 2, dữ liệu tự đồng bộ xuống.

### 3. Folder Redirection (Chuyển hướng Thư mục qua GPO)
- Đường dẫn GPO: `User Configuration` -> `Policies` -> `Windows Settings` -> `Folder Redirection`.
- Chuột phải **Documents** (hoặc Desktop) -> **Properties**:
  - Setting: **Basic - Redirect everyone's folder to the same location**.
  - Target folder location: **Create a folder for each user under the root path**.
  - Root Path: `\\Server\Redirection$`.

---

## LAB 8: QUẢN TRỊ DUNG LƯỢNG ĐĨA CỨNG (DISK QUOTA) & FSRM

### 1. NTFS Disk Quota (Cơ bản)
- Chuột phải vào ổ đĩa (ví dụ `C:` hoặc `D:`) -> **Properties** -> Thẻ **Quota** -> Nhấn **Show Quota Settings**.
- Tích chọn:
  - `Enable quota management`
  - `Deny disk space to users exceeding quota limit` (chặn không cho ghi tiếp khi quá hạn ngạch).
  - Đặt Limit (ví dụ: 100 MB) và Warning level (ví dụ: 80 MB).
- **Quota Entries**: Đặt hạn ngạch riêng biệt cho từng tài khoản cụ thể.

### 2. File Server Resource Manager (FSRM - Nâng cao)
- Cài đặt Feature:
  ```powershell
  Install-WindowsFeature FS-Resource-Manager -IncludeManagementTools
  ```
- **Quota Management**:
  - **Hard Quota**: Chặn đứng tuyệt đối không cho ghi file mới khi chạm mức quota.
  - **Soft Quota**: Cho phép ghi tiếp nhưng gửi cảnh báo/ghi event log khi vượt ngưỡng.
- **File Screening Management (Chặn loại file cấm)**:
  - Chọn thư mục muốn áp dụng (ví dụ: `C:\DuLieu`).
  - Chọn File Screen Template: **Block Audio and Video Files** hoặc **Block Executable Files** (`*.exe`, `*.bat`, `*.com`, `*.vbs`...).
  - Kết quả: Khi người dùng cố copy hoặc tải file đuôi cấm vào thư mục share, hệ thống báo lỗi *"Access Denied"* ngay lập tức!

---

## LAB 9: TRIỂN KHAI DOMAIN ĐỒNG CẤP (SECONDARY DC / FSMO ROLES)

### 1. Khái niệm Domain Đồng cấp (Additional Domain Controller - ADC)
- Là máy chủ DC thứ 2 cùng tham gia vào một Domain sẵn có để:
  - Cân bằng tải xác thực đăng nhập người dùng.
  - Dự phòng thảm họa (Fault Tolerance): Khi DC chính sập, ADC vẫn phục vụ người dùng bình thường.

### 2. 5 Vai trò FSMO (Flexible Single Master Operations)
1. **Schema Master** (Cấp Forest): Quản lý định nghĩa cấu trúc đối tượng trong AD.
2. **Domain Naming Master** (Cấp Forest): Quản lý việc thêm/xóa tên domain trong Forest.
3. **PDC Emulator** (Cấp Domain): Đồng bộ giờ toàn mạng, xử lý đổi mật khẩu, tương thích máy trạm cũ.
4. **RID Master** (Cấp Domain): Cấp phát dải RID (Relative ID) để tạo SID định danh đối tượng.
5. **Infrastructure Master** (Cấp Domain): Cập nhật tham chiếu chéo giữa các domain.

### 3. Lệnh Quản trị & Chuyển giao FSMO bằng PowerShell
```powershell
# Xem Server nào đang giữ 5 vai trò FSMO
netdom query fsmo

# Chuyển giao (Transfer) 5 vai trò sang DC mới khi DC cũ còn hoạt động:
Move-ADDirectoryServerOperationMasterRole -Identity "TEN-DC-MOI" -OperationMasterRole 0,1,2,3,4 -Force

# Cướp quyền (Seize) vai trò khi DC cũ bị hỏng hoàn toàn:
Move-ADDirectoryServerOperationMasterRole -Identity "TEN-DC-MOI" -OperationMasterRole 0,1,2,3,4 -Force
```

---

## LAB 10: TỐI ƯU HÓA DỊCH VỤ ACTIVE DIRECTORY & REVERSE DNS LOOKUP

### 1. Reverse DNS Lookup Zone (Phân giải IP thành Tên máy)
- **Mục đích**: Hầu hết các ứng dụng quản trị, dịch vụ Mail, `nslookup`, `ping -a` cần Reverse DNS Zone để phân giải địa chỉ IP ngược lại FQDN (Fully Qualified Domain Name). Thiếu Reverse Zone sẽ khiến lệnh `nslookup` báo lỗi *"Default Server: Unknown"*.
- **Cách tạo Reverse Lookup Zone**:
  ```powershell
  # Tạo Reverse Zone cho mạng LAN 1 (192.168.11.0/24)
  Add-DnsServerPrimaryZone -NetworkId "192.168.11.0/24" -ReplicationScope "Domain"
  
  # Tạo Reverse Zone cho mạng LAN 2 (100.100.11.0/24)
  Add-DnsServerPrimaryZone -NetworkId "100.100.11.0/24" -ReplicationScope "Domain"
  ```
- **Tạo bản ghi con trỏ PTR**:
  ```powershell
  Add-DnsServerResourceRecordPtr -ZoneName "11.168.192.in-addr.arpa" -Name "1" -PtrDomainName "WIN-P6PG9M9AICK.fit.iuh.edu.vn"
  Add-DnsServerResourceRecordPtr -ZoneName "11.100.100.in-addr.arpa" -Name "1" -PtrDomainName "WIN-P6PG9M9AICK.fit.iuh.edu.vn"
  ```

### 2. Kiểm tra phân giải tên miền hoàn hảo
```cmd
nslookup 192.168.11.1
nslookup fit.iuh.edu.vn
```
Kết quả hiển thị chính xác tên Server và IP, không còn bất kỳ dòng lỗi Unknown nào!

---

## HƯỚNG DẪN TRẢ LỜI CÂU HỎI VẤN ĐÁP KHI THẦY CHẤM ĐIỂM (10 ĐIỂM)

1. **Thầy hỏi**: *"Tại sao máy con ping máy chủ được nhưng không join được Domain?"*
   - **Trả lời**: Do DNS trên máy con chưa trỏ về IP của máy chủ Domain Controller, hoặc Firewall trên Server đang chặn cổng Kerberos (88) / RPC (135) / DNS (53).

2. **Thầy hỏi**: *"Khi phân quyền Share là Change mà NTFS là Read, người dùng từ máy trạm truy cập qua mạng có xóa được file không?"*
   - **Trả lời**: Dạ không được, vì nguyên tắc kết hợp giữa Share và NTFS qua mạng là **Most Restrictive (Càng thắt chặt càng ưu tiên)**, do đó quyền hiệu lực cuối cùng là **Read**.

3. **Thầy hỏi**: *"Creator Owner có vai trò gì trong phân quyền thư mục dùng chung?"*
   - **Trả lời**: Dạ Creator Owner đại diện cho người tạo ra tập tin hoặc thư mục con. Khi gán Creator Owner = Full Control trên thư mục cha, bất kỳ nhân viên nào tạo file trong đó thì chỉ người đó mới có quyền chỉnh sửa, đổi tên hoặc xóa file của mình, người khác chỉ có quyền đọc.

4. **Thầy hỏi**: *"Làm sao để người dùng không nhìn thấy các thư mục mà họ không có quyền?"*
   - **Trả lời**: Dạ bật tính năng **Access-Based Enumeration (ABE)** trong thuộc tính của Shared Folder trên Server.

5. **Thầy hỏi**: *"Làm thế nào để áp dụng GPO ngay lập tức mà không cần khởi động lại máy?"*
   - **Trả lời**: Dạ mở CMD chạy lệnh `gpupdate /force`.
