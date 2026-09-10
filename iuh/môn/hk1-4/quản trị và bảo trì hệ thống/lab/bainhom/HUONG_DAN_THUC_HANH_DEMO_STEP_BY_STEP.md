# CẨM NANG THỰC HÀNH CHI TIẾT & KỊCH BẢN QUAY 6 VIDEO DEMO
## BÀI TẬP NHÓM: CÀI ĐẶT & CẤU HÌNH ACTIVE DIRECTORY DOMAIN SERVICES (AD DS)
**Môn học: Quản trị và bảo trì hệ thống (IUH)**  
**Thành viên thực hiện:**
- **Đỗ Hữu Châu (24688491)**
- **Phan Thanh Đô (24700621)**
- **Lê Thành Long (23630851)**

---

## 🎯 TẠI SAO CHIA THÀNH 6 VIDEO LÀ PHƯƠNG ÁN TỐI ƯU NHẤT?
1. **Khớp 100% từng yêu cầu trong đề bài** của giảng viên (mỗi video giải quyết dứt điểm 1 gạch đầu dòng).
2. **Dễ quay, không sợ nói vấp:** Mỗi video chỉ dài từ **1 đến 3 phút**. Nếu lỡ bấm nhầm hay nói nhịu thì chỉ cần quay lại đúng 1 video ngắn đó, không cần phải quay lại cả bài dài 15 phút!
3. **Nộp bài chuyên nghiệp:** Nhóm có thể nộp thư mục gồm 6 video đánh số thứ tự từ `Video_1` đến `Video_6`, hoặc dùng CapCut / Camtasia ghép lại thành 1 video duy nhất có tiêu đề từng phần cực kỳ đẹp mắt.

---

## 📋 THÔNG SỐ CẤU HÌNH MẠNG THỰC TẾ (SẴN SÀNG TRÊN MÁY ẢO)

| Máy tính | Tên máy (Hostname) | Card mạng ảo | Địa chỉ IP | Subnet Mask | Preferred DNS |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Máy chủ Server** | `WIN-P6PG9M9AICK` | `VMnet11` | `192.168.11.1` | `255.255.255.0` | `192.168.11.1` *(Trỏ về chính mình)* |
| **Máy trạm Client** | `WIN7-PC1` | `VMnet11` | `192.168.11.2` | `255.255.255.0` | `192.168.11.1` *(Trỏ về IP Server)* |

* **Tên miền Domain dự kiến:** `nhom1.vn` (hoặc `iuh.local`)
* **Mật khẩu quản trị mặc định:** `123` (hoặc `P@ssword123!`)
* **Mật khẩu DSRM (Khôi phục AD):** `123456` (hoặc `P@ssword123!`)

---

# 🎬 KỊCH BẢN QUAY CHI TIẾT TỪNG VIDEO (TỪ VIDEO 1 ĐẾN VIDEO 6)

---

### 🎥 VIDEO 1: THIẾT LẬP IP TĨNH, DNS & KIỂM TRA THÔNG MẠNG (Thời lượng: ~2 phút)
> **Mục tiêu đề bài:** *"Thiết lập địa chỉ IP cho card mạng của server hoặc bạn có thể thiết lập địa chỉ IP của các DNS Server trong hệ thống."*

#### 1. Thao tác trên màn hình (Action on screen)
1. **Trên máy Windows Server:**
   * Mở cửa sổ card mạng `VMnet11` (Network and Sharing Center ➔ Change adapter settings).
   * Chuột phải vào card mạng ➔ **Properties** ➔ Chọn **Internet Protocol Version 4 (TCP/IPv4)** ➔ **Properties**.
   * Chỉ chuột cho người xem thấy:
     - IP address: `192.168.11.1`
     - Subnet mask: `255.255.255.0`
     - Preferred DNS server: `192.168.11.1` *(Nhấn mạnh điểm này: Bắt buộc phải trỏ về chính mình)*.
   * Bấm **OK** ➔ **Close**.
2. **Kiểm tra thông tuyến sang Client:**
   * Mở **Command Prompt (CMD)** trên Server.
   * Gõ lệnh:
     ```cmd
     ping 192.168.11.2
     ```
   * Màn hình trả về `Reply from 192.168.11.2: bytes=32 time<1ms` (Thông mạng hoàn hảo).

#### 2. Lời thoại thuyết minh (Voice Speech)
> *"Kính chào thầy và các bạn, em là Đỗ Hữu Châu, đại diện Nhóm 1. Ở Video đầu tiên này, nhóm em tiến hành chuẩn bị môi trường mạng cho bài thực hành. Trên máy chủ Windows Server kết nối vào card mạng nội bộ VMnet11, nhóm em đã thiết lập địa chỉ IP tĩnh là 192.168.11.1, Subnet mask 255.255.255.0 và Preferred DNS server trỏ về chính địa chỉ 192.168.11.1 vì máy chủ này sẽ đóng vai trò là DNS Server đầu tiên của hệ thống. Đồng thời, nhóm em thực hiện lệnh ping sang máy trạm Windows 7 tại địa chỉ 192.168.11.2, kết quả tín hiệu phản hồi ổn định dưới 1 mili-giây. Môi trường mạng đã sẵn sàng để cài đặt dịch vụ."*

---

### 🎥 VIDEO 2: CÀI ĐẶT ROLE ACTIVE DIRECTORY DOMAIN SERVICES (Thời lượng: ~2 phút)
> **Mục tiêu đề bài:** *"quá trình cài đặt AD DS..."*

#### 1. Thao tác trên màn hình (Action on screen)
1. Trên Windows Server, mở **Server Manager** từ thanh Taskbar.
2. Bấm vào menu **Manage** ở góc trên bên phải ➔ Chọn **Add Roles and Features**.
3. Bấm **Next** tại màn hình *Before You Begin*.
4. Màn hình *Installation Type*: Giữ mặc định **Role-based or feature-based installation** ➔ Bấm **Next**.
5. Màn hình *Server Selection*: Chọn đúng máy chủ `WIN-P6PG9M9AICK (192.168.11.1)` ➔ Bấm **Next**.
6. Màn hình *Server Roles*:
   * Tích chọn vào ô: **Active Directory Domain Services**.
   * Cửa sổ pop-up hiện lên ➔ Bấm **Add Features**.
   * Bấm **Next**.
7. Màn hình *Features*: Để mặc định ➔ Bấm **Next**.
8. Màn hình *AD DS*: Bấm **Next**.
9. Màn hình *Confirmation*: Bấm nút **Install**.
10. Đợi thanh tiến trình chạy hoàn tất, xuất hiện dòng thông báo *"Configuration required. Installation succeeded"* ➔ Bấm **Close**.

#### 2. Lời thoại thuyết minh (Voice Speech)
> *"Chào thầy, em là Phan Thanh Đô. Tiếp nối Video 1, ở Video thứ 2 này em sẽ tiến hành cài đặt Role Active Directory Domain Services trên Windows Server 2012. Em mở trình quản lý Server Manager, chọn Add Roles and Features, tại danh mục Server Roles em tích chọn tính năng Active Directory Domain Services và chấp nhận thêm các tính năng bổ trợ Add Features. Sau đó em tiến hành Install. Quá trình cài đặt các file nhị phân của dịch vụ AD DS đã hoàn tất thành công."*

---

### 🎥 VIDEO 3: PROMOTE SERVER LÊN DOMAIN CONTROLLER ĐẦU TIÊN & TÍCH HỢP DNS (Thời lượng: ~3 phút)
> **Mục tiêu đề bài:** *"Nếu server này là Domain Controller và DNS Server đầu tiên, quá trình cài đặt AD DS sẽ bao gồm cả việc cài đặt DNS Server. Xây dựng các DNS Server trong hệ thống mạng nếu có, trong quá trình cài đặt AD DS sẽ có cài đặt DNS Server"*

#### 1. Thao tác trên màn hình (Action on screen)
1. Trên Server Manager, bấm vào biểu tượng **Lá cờ vàng có dấu chấm than (Notifications)** ➔ Bấm vào dòng chữ xanh: **Promote this server to a domain controller**.
2. Cửa sổ **AD DS Configuration Wizard** xuất hiện:
   * **Deployment Configuration:**
     - Tích chọn mục thứ 3: **Add a new forest** (Tạo một rừng mới hoàn toàn).
     - Ô **Root domain name**: Gõ tên miền `nhom1.vn` (hoặc `iuh.local`).
     - Bấm **Next**.
   * **Domain Controller Options:**
     - Giữ nguyên Forest/Domain functional level là `Windows Server 2012 R2`.
     - **Chỉ chuột vào ô "Domain Name System (DNS) server"**: Cho thấy ô này đã được hệ thống tự động tích chọn và làm mờ (chứng minh yêu cầu đề bài: cài DC đầu tiên luôn đi kèm cài DNS Server).
     - Nhập mật khẩu khôi phục DSRM: `123456` (Confirm: `123456`).
     - Bấm **Next**.
   * **DNS Options:** Bỏ qua cảnh báo DNS Delegation ➔ Bấm **Next**.
   * **Additional Options:** NetBIOS domain name tự nhận là `NHOM1` ➔ Bấm **Next**.
   * **Paths:** Giữ nguyên các thư mục `C:\Windows\NTDS` và `C:\Windows\SYSVOL` ➔ Bấm **Next**.
   * **Review Options:** Bấm **Next**.
   * **Prerequisites Check:** Chờ vài giây xuất hiện dòng chữ xanh *"All prerequisite checks passed successfully"* ➔ Bấm nút **Install**.
3. Hệ thống cấu hình tự động và khởi động lại.
4. Khi khởi động lại xong, bấm `Ctrl + Alt + Del` ➔ Màn hình đăng nhập hiện rõ: **`NHOM1\Administrator`** ➔ Nhập mật khẩu `123` để đăng nhập.

#### 2. Lời thoại thuyết minh (Voice Speech)
> *"Chào thầy, em tiếp tục thực hiện Video 3: Nâng cấp máy chủ lên Domain Controller đầu tiên. Sau khi cài Role, em bấm vào lá cờ thông báo để Promote Server. Vì đây là hệ thống mới hoàn toàn, em chọn Add a new forest và đặt tên miền gốc là nhom1.vn. Đúng như yêu cầu trong đề bài, ở màn hình Domain Controller Options, tính năng Domain Name System (DNS) server đã được hệ thống tự động tích chọn vì máy DC đầu tiên bắt buộc phải có DNS Server để quản lý các bản ghi phân giải định danh SRV. Em đặt mật khẩu khôi phục DSRM là 123456 và tiến hành Install. Máy chủ tự động khởi động lại và hiện tại em đã đăng nhập thành công vào quyền quản trị miền NHOM1\\Administrator."*

---

### 🎥 VIDEO 4: THỰC THI & GIẢI THÍCH 3 LỆNH ADPREP MỞ RỘNG HẠ TẦNG (Thời lượng: ~2 phút)
> **Mục tiêu đề bài:**
> - *"Nếu muốn bổ sung server này vào một forest đã tồn tại trên Windows Server 2000, 2003 bạn phải cập nhật thông tin về forest bằng lệnh `adprep /forestprep`"*
> - *"Nếu muốn bổ sung server này vào một domain đã tồn tại trên Windows Server 2000, 2003 bạn phải cập nhập thông tin về domain và group policy bằng lệnh `adprep /domainprep /gpprep`"*
> - *"Nếu muốn cài đặt một Read-Only Domain Controller, bạn phải chuẩn bị forest bằng lệnh `adprep /rodcprep`"*

#### 1. Thao tác trên màn hình (Action on screen)
1. Trên Windows Server, bấm phím Start ➔ Gõ `cmd` ➔ Chuột phải chọn **Run as administrator**.
2. **Lệnh 1:** Gõ lệnh và nhấn Enter:
   ```cmd
   adprep /forestprep
   ```
   *(Màn hình hiển thị thông tin Schema hiện tại).*
3. **Lệnh 2:** Gõ tiếp lệnh và nhấn Enter:
   ```cmd
   adprep /domainprep /gpprep
   ```
   *(Màn hình xác nhận thông tin Domain và Group Policy).*
4. **Lệnh 3:** Gõ tiếp lệnh và nhấn Enter:
   ```cmd
   adprep /rodcprep
   ```
   *(Màn hình chạy thông báo chuẩn bị phân vùng DNS cho RODC).*

#### 2. Lời thoại thuyết minh (Voice Speech)
> *"Kính thưa thầy, em là Lê Thành Long. Trong Video 4 này, em xin trình bày và giải thích 3 lệnh ADPREP theo đúng yêu cầu bài tập khi triển khai nâng cấp hệ sinh thái máy chủ cũ thời Windows 2000 và 2003:  
> 1. Đầu tiên là lệnh `adprep /forestprep`: Lệnh này dùng để mở rộng và cập nhật cấu trúc Schema trên toàn bộ Forest, bổ sung các lớp đối tượng và thuộc tính mới mà Windows Server phiên bản mới yêu cầu.  
> 2. Thứ hai là lệnh `adprep /domainprep /gpprep`: Lệnh này dùng để cập nhật các quyền bảo mật cấp Domain và chuẩn bị các phân vùng đối tượng chính sách nhóm Group Policy (SYSVOL) từ Domain cũ.  
> 3. Thứ ba là lệnh `adprep /rodcprep`: Khi doanh nghiệp có các chi nhánh nhỏ cần lắp đặt Read-Only Domain Controller để chống nguy cơ bị chiếm máy chủ vật lý, lệnh này sẽ cập nhật phân quyền bảo mật cho các phân vùng ứng dụng DNS trên toàn Forest, giúp RODC có quyền sao chép bản ghi DNS một cách an toàn."*

---

### 🎥 VIDEO 5: KHẢO SÁT & KIỂM TRA HOẠT ĐỘNG CỦA AD DS & DNS SERVER (Thời lượng: ~2 phút)
> **Mục tiêu đề bài:** Kiểm tra và nghiệm thu các thành phần cốt lõi của Active Directory và DNS Server sau khi cài đặt.

#### 1. Thao tác trên màn hình (Action on screen)
1. **Kiểm tra Active Directory:**
   * Vào **Server Manager** ➔ **Tools** ➔ Mở **Active Directory Users and Computers**.
   * Mở rộng tên miền `nhom1.vn` ➔ Cho xem các thư mục `Builtin`, `Computers`, `Domain Controllers` (có máy `WIN-P6PG9M9AICK`), `Users`.
   * Thao tác tạo thử: Chuột phải `nhom1.vn` ➔ **New** ➔ **Organizational Unit** ➔ Đặt tên là `KHOA-CNTT`.
   * Trong `KHOA-CNTT` ➔ Chuột phải ➔ **New** ➔ **User** ➔ Đặt tên `sv1`, logon name: `sv1@nhom1.vn`, Password: `P@ssword123!`.
2. **Kiểm tra DNS Server:**
   * Vào **Tools** ➔ Mở **DNS**.
   * Mở rộng **Forward Lookup Zones** ➔ Bấm vào `nhom1.vn` và `_msdcs.nhom1.vn`.
   * Cho thấy các bản ghi dịch vụ SRV (`_ldap`, `_kerberos`) đều trỏ chính xác về IP `192.168.11.1`.
3. **Kiểm tra thư mục chia sẻ mặc định:**
   * Mở CMD gõ:
     ```cmd
     net share
     ```
   * Màn hình hiển thị 2 thư mục chia sẻ hệ thống: `NETLOGON` và `SYSVOL`.

#### 2. Lời thoại thuyết minh (Voice Speech)
> *"Chào thầy, ở Video thứ 5, em tiến hành kiểm tra nghiệm thu hoạt động của AD DS và DNS Server. Trong cửa sổ Active Directory Users and Computers, cấu trúc miền nhom1.vn đã hoạt động hoàn chỉnh, em đã tạo thành công một Đơn vị tổ chức OU tên là KHOA-CNTT cùng tài khoản người dùng sv1. Tiếp theo trong công cụ DNS Manager, vùng phân giải thuận đã tự động sinh ra các bản ghi định danh SRV của dịch vụ Kerberos và LDAP trong nhánh _msdcs. Cuối cùng qua lệnh net share, 2 thư mục chia sẻ bắt buộc của Domain Controller là NETLOGON và SYSVOL đã sẵn sàng phục vụ toàn bộ máy trạm."*

---

### 🎥 VIDEO 6: CẤU HÌNH CLIENT WIN 7 TRỎ DNS, JOIN DOMAIN & ĐĂNG NHẬP NGHIỆM THU (Thời lượng: ~3 phút)
> **Mục tiêu đề bài:** Minh chứng thực tế Active Directory và DNS Server quản lý thành công máy trạm trong mạng.

#### 1. Thao tác trên màn hình (Action on screen)
1. **Chuyển sang máy trạm Windows 7 (`WIN7-PC1`):**
   * Mở card mạng ➔ **Properties** ➔ **IPv4** ➔ Đảm bảo:
     - IP address: `192.168.11.2`
     - Subnet mask: `255.255.255.0`
     - **Preferred DNS server:** `192.168.11.1` *(Trỏ chính xác về IP Server)*.
   * Bấm **OK**.
2. **Kiểm tra phân giải tên miền:**
   * Mở CMD trên Win 7 gõ:
     ```cmd
     ping nhom1.vn
     ```
   * Thấy phân giải đúng về IP `192.168.11.1`.
3. **Thực hiện Join Domain:**
   * Chuột phải vào biểu tượng **Computer** trên Desktop ➔ Chọn **Properties**.
   * Tại mục *Computer name, domain, and workgroup settings* ➔ Bấm **Change settings**.
   * Cửa sổ System Properties hiện ra ➔ Bấm nút **Change...**.
   * Tại mục **Member of**, tích chọn vào **Domain** ➔ Nhập vào: `nhom1.vn` ➔ Bấm **OK**.
   * Cửa sổ yêu cầu xác thực hiện ra:
     - Username: `Administrator`
     - Password: `123`
     - Bấm **OK**.
   * Chờ vài giây, hộp thoại xuất hiện:  
     🎉 **"Welcome to the nhom1.vn domain."** ➔ Bấm **OK**.
   * Bấm **Restart Now** để khởi động lại máy trạm.
4. **Đăng nhập kiểm thử trên Client:**
   * Sau khi máy khởi động lại ➔ Bấm `Ctrl + Alt + Del` ➔ Chọn **Switch User** ➔ **Other User**.
   * Nhập:
     - Username: `nhom1\sv1` (hoặc `sv1@nhom1.vn`)
     - Password: `P@ssword123!`
   * Đăng nhập thành công vào Windows 7 với tài khoản người dùng miền!
   * Mở CMD gõ lệnh:
     ```cmd
     whoami
     ```
   * Màn hình in ra: **`nhom1\sv1`**. Nghiệm thu thành công 100%!

#### 2. Lời thoại thuyết minh (Voice Speech)
> *"Để khép lại phần báo cáo thực hành, ở Video số 6 nhóm em kiểm thử gia nhập máy trạm Windows 7 vào Domain. Trên máy WIN7-PC1, em cấu hình Preferred DNS trỏ chính xác về IP máy chủ 192.168.11.1 và kiểm tra lệnh ping nhom1.vn thành công. Sau đó em tiến hành Join Domain nhom1.vn bằng tài khoản Administrator. Hộp thoại chào mừng Welcome to domain đã xuất hiện. Sau khi khởi động lại máy, em sử dụng tài khoản sv1 vừa tạo trên máy chủ để đăng nhập trực tiếp vào Windows 7, lệnh whoami xác nhận định danh nhom1\\sv1. Toàn bộ các yêu cầu cài đặt, cấu hình AD DS, tích hợp DNS Server và lệnh adprep của bài tập nhóm đã được hoàn thành xuất sắc. Nhóm 1 xin chân thành cảm ơn thầy đã theo dõi!"*
