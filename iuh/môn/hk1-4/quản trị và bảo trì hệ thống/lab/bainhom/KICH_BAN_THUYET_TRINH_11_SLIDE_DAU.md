# KỊCH BẢN THUYẾT TRÌNH BÁO CÁO NHÓM 1
## ĐỀ TÀI: ACTIVE DIRECTORY DOMAIN SERVICES (AD DS)
### (Nội dung thuyết trình: 11 Slide đầu - Phần Lý thuyết & Kiến trúc cốt lõi)

---

> [!TIP]
> **HƯỚNG DẪN DÀNH CHO BẠN TRƯỚC KHI LÊN BỤC THUYẾT TRÌNH**:
> - **Tổng thời gian dự kiến cho 11 slide**: Khoảng **7 – 10 phút** (trung bình 45 - 60 giây/slide).
> - **Tư thế & Phong thái**: Nói to, rõ ràng, phong thái tự tin. Không đọc chằm chằm từng chữ trên slide; slide chỉ để chiếu từ khóa, bạn đọc theo **Lời thoại thuyết trình** bên dưới.
> - **Cách dùng tài liệu này**:
>   - Phần **🗣️ Lời thoại gợi ý**: Đọc trực tiếp hoặc biến tấu nhẹ theo cách nói tự nhiên của bạn.
>   - Phần **💡 Ý chính cần nhớ**: Dùng để liếc nhanh từ khóa khi đang đứng thuyết trình.
>   - Phần **❓ Câu hỏi thầy cô hay hỏi xoáy & Cách trả lời**: Giúp bạn tự tin ăn trọn điểm 10 nếu giảng viên ngắt lời phản biện!

---

## 🖥️ SLIDE 1: TRANG TIÊU ĐỀ
* **Tên Slide**: NHÓM 1 - ACTIVE DIRECTORY DOMAIN SERVICES
* **Nội dung trên slide**: Tên đề tài, môn học Quản trị và bảo trì hệ thống, nhóm thực hiện.
* **Thời lượng**: ~30 giây.

### 🗣️ Lời thoại gợi ý:
> *"Kính thưa Thầy (Cô) và toàn thể các bạn sinh viên!*  
> *Hôm nay, em xin đại diện cho **Nhóm 1** trình bày bài báo cáo nghiên cứu chuyên sâu về đề tài: **'Active Directory Domain Services - Nghiên cứu kiến trúc, cơ chế hoạt động, tiện ích ADPREP và triển khai thực hành quản trị trên Windows Server'** trong khuôn khổ môn học Quản trị và bảo trì hệ thống.*  
> *Bài báo cáo của nhóm em được xây dựng bám sát thực tế doanh nghiệp và tiêu chuẩn học thuật của nhà trường. Sau đây, em xin phép được bắt đầu phần thuyết trình!"*

### 💡 Ý chính cần nhớ:
- Chào hỏi trang trọng.
- Nêu rõ tên đề tài và nhóm 1.

---

## 🖥️ SLIDE 2: MỤC LỤC TỔNG QUAN
* **Tên Slide**: MỤC LỤC TỔNG QUAN
* **Nội dung trên slide**: 4 Chương nội dung của đề tài.
* **Thời lượng**: ~45 giây.

### 🗣️ Lời thoại gợi ý:
> *"Để quý Thầy Cô và các bạn tiện theo dõi, toàn bộ nội dung nghiên cứu của nhóm em được chia làm **4 Chương trọng tâm** bao gồm:*  
> - **Chương 1**: Tổng quan, bối cảnh ra đời và các chức năng cốt lõi của Dịch vụ thư mục.  
> - **Chương 2**: Kiến trúc Logic, kiến trúc Vật lý, Schema, Global Catalog và 5 vai trò FSMO.  
> - **Chương 3**: Các tính năng an ninh nâng cao như máy chủ chi nhánh RODC và bộ tiện ích chuẩn bị nâng cấp hạ tầng ADPREP.  
> - **Chương 4**: Triển khai cài đặt thực tế trên hệ thống máy ảo kèm theo kịch bản nghiệm thu 6 Video Demo.  
>  
> *Trong phần trình bày đầu tiên này, em xin phép đi sâu vào **Chương 1 và Chương 2** – đây là hai chương nền tảng cốt lõi định hình nên toàn bộ kiến trúc quản trị của hệ thống Windows Server."*

### 💡 Ý chính cần nhớ:
- Nêu ngắn gọn tên 4 chương.
- Tạo câu nối (transition) hướng sự chú ý vào Chương 1 và 2.

---

## 🖥️ SLIDE 3: 1.1. BỐI CẢNH VÀ SỰ CẦN THIẾT CỦA DIRECTORY SERVICE
* **Tên Slide**: BỐI CẢNH VÀ SỰ CẦN THIẾT CỦA DỊCH VỤ THƯ MỤC
* **Nội dung trên slide**: Mô hình Workgroup ➔ Doanh nghiệp mở rộng ➔ Vấn đề phát sinh ➔ Nhu cầu Directory Service.
* **Thời lượng**: ~50 giây.

### 🗣️ Lời thoại gợi ý:
> *"Đầu tiên, chúng ta cùng nhìn lại bối cảnh lịch sử: **Tại sao doanh nghiệp bắt buộc phải cần đến Dịch vụ thư mục?***  
> *Ở thời kỳ đầu, các mạng máy tính thường hoạt động theo mô hình **Workgroup** (mạng ngang hàng). Trong mô hình này, mỗi máy tính tự quản lý tài khoản người dùng của riêng mình trong cơ sở dữ liệu SAM cục bộ.*  
> *Mô hình này chỉ chạy tốt khi văn phòng có dưới 10 máy tính. Nhưng khi doanh nghiệp phát triển lên hàng trăm, hàng nghìn nhân viên với nhiều chi nhánh, một 'cơn ác mộng' quản trị xuất hiện: Mỗi khi có nhân viên mới hay nhân viên đổi mật khẩu, người quản trị IT phải đến từng máy tính để tạo hoặc sửa thủ công. Dữ liệu phân tán, bảo mật lỏng lẻo và chi phí vận hành tăng vọt.*  
> *Chính vì thế, nhu cầu cấp bách là phải có một hệ thống **quản trị định danh và tài nguyên tập trung**. Và đó là lý do **Directory Service (Dịch vụ thư mục)** ra đời!"*

### 💡 Ý chính cần nhớ:
- Workgroup = tự quản lý riêng lẻ (file SAM cục bộ), chỉ hợp mạng nhỏ <10 máy.
- Doanh nghiệp lớn = quản lý phân tán, chi phí cao, dễ lộ lọt bảo mật.
- Directory Service ra đời để quản lý tập trung toàn bộ người dùng và tài nguyên.

---

## 🖥️ SLIDE 4: 1.2. SO SÁNH MÔ HÌNH WORKGROUP VÀ DOMAIN
* **Tên Slide**: SO SÁNH MÔ HÌNH WORKGROUP VÀ DOMAIN (ACTIVE DIRECTORY)
* **Nội dung trên slide**: Bảng so sánh 7 tiêu chuẩn kỹ thuật giữa Workgroup và Domain.
* **Thời lượng**: ~1 phút 15 giây.

### 🗣️ Lời thoại gợi ý:
> *"Để thấy rõ sự vượt trội của giải pháp, slide số 4 tóm tắt bảng so sánh giữa **Workgroup** và **Domain (Active Directory)** qua 7 tiêu chí cốt lõi:*  
> 1. **Về cơ chế lưu trữ**: Workgroup lưu phân tán ở file SAM của từng máy; còn Domain lưu trữ tập trung tại cơ sở dữ liệu `ntds.dit` trên máy chủ Domain Controller.  
> 2. **Về xác thực**: Workgroup xác thực cục bộ; còn Domain xác thực tập trung thông qua giao thức bảo mật hiện đại **Kerberos v5**.  
> 3. **Về đăng nhập một lần (SSO)**: Workgroup không hỗ trợ, truy cập máy nào phải nhớ mật khẩu máy đó; Domain hỗ trợ SSO hoàn hảo – nhân viên chỉ cần 1 tài khoản là đăng nhập được vào mọi máy tính và dịch vụ được cấp phép.  
> 4. **Về chính sách an ninh**: Workgroup phải chỉnh thủ công từng máy; còn Domain triển khai đồng loạt hàng nghìn máy chỉ trong tích tắc nhờ **Group Policy (GPO)**.  
> 5. **Về khả năng mở rộng**: Workgroup rất kém (dưới 10 máy); Domain hỗ trợ từ hàng trăm đến hàng triệu đối tượng.  
> 6. **Về phân quyền**: Workgroup chỉ có quyền Admin hoặc User cục bộ; còn Domain cho phép **ủy quyền quản trị linh hoạt (Delegation)** theo từng phòng ban (OU).  
> 7. **Về dự phòng sự cố**: Workgroup không có dự phòng; Domain hỗ trợ cơ chế đồng bộ đa chiều (**Multi-Master Replication**) giữa nhiều Domain Controller, một máy hỏng hệ thống vẫn hoạt động thông suốt.*"

### 💡 Ý chính cần nhớ:
- Workgroup: SAM cục bộ, không có SSO, cấu hình thủ công, không dự phòng.
- Domain: Database tập trung (`ntds.dit`), xác thực Kerberos, có SSO, quản trị bằng GPO, chịu lỗi bằng Multi-Master Replication.

### ❓ Câu hỏi Thầy/Cô hay hỏi xoáy:
* **Hỏi**: *"Cơ sở dữ liệu người dùng của Domain tên là gì và nằm ở đâu?"*
* **Đáp**: *"Dạ thưa Thầy/Cô, cơ sở dữ liệu của Active Directory là tệp tin **`ntds.dit`**, mặc định nằm tại đường dẫn `C:\Windows\NTDS\ntds.dit` trên máy chủ Domain Controller."*

---

## 🖥️ SLIDE 5: 1.3. LỊCH SỬ PHÁT TRIỂN CỦA ACTIVE DIRECTORY
* **Tên Slide**: LỊCH SỬ PHÁT TRIỂN CỦA ACTIVE DIRECTORY QUA CÁC THẾ HỆ WINDOWS SERVER
* **Nội dung trên slide**: Dòng thời gian từ Windows 2000 Server đến Windows Server 2022.
* **Thời lượng**: ~50 giây.

### 🗣️ Lời thoại gợi ý:
> *"Tiếp theo là hành trình hơn 20 năm tiến hóa của Active Directory:*  
> - **Năm 2000 (Windows 2000 Server)**: Đánh dấu sự ra đời lịch sử của Active Directory thay thế hoàn toàn mô hình NT 4.0 cũ, chính thức đặt nền móng cho cấu trúc Domain, Tree, Forest, OU và các chuẩn công nghiệp như LDAP, Kerberos.  
> - **Windows Server 2003**: Bổ sung tính năng liên kết tin cậy giữa các Rừng (**Forest Trust**), đổi tên miền (**Domain Rename**) và giới thiệu bộ công cụ nâng cấp **ADPREP**.  
> - **Windows Server 2008 & 2008 R2**: Bước nhảy vọt về an ninh với máy chủ chi nhánh **RODC**, chính sách mật khẩu chi tiết (**Fine-Grained Password Policy**) và thùng rác phục hồi **AD Recycle Bin**.  
> - **Windows Server 2012 & 2012 R2**: Đơn giản hóa triển khai (chính thức khai tử lệnh `dcpromo` chuyển sang Server Manager/PowerShell), hỗ trợ ảo hóa Domain Controller an toàn với VM-Generation ID và kiểm soát truy cập động DAC.  
> - **Từ Windows Server 2016 đến 2022 nay**: Microsoft tập trung mạnh mẽ vào xu thế **Hybrid Identity** – kết nối Active Directory nội bộ với đám mây Microsoft Entra ID (Azure AD) và bảo mật quản trị đặc quyền PAM.*"

### 💡 Ý chính cần nhớ:
- 2000: Khai sinh AD (LDAP, Kerberos).
- 2003: Forest Trust, ADPREP.
- 2008/R2: RODC (chi nhánh), AD Recycle Bin.
- 2012/R2: Bỏ `dcpromo`, tối ưu ảo hóa DC.
- 2016-2022: Hybrid Cloud (Azure AD/Entra ID).

---

## 🖥️ SLIDE 6: 1.4. BỐN CHỨC NĂNG CỐT LÕI CỦA DIRECTORY SERVICE
* **Tên Slide**: BỐN CHỨC NĂNG CỐT LÕI CỦA DIRECTORY SERVICE
* **Nội dung trên slide**: 1. Quản trị tập trung, 2. Mở rộng & phân cấp, 3. Tra cứu tài nguyên, 4. Bảo mật & kiểm soát truy cập.
* **Thời lượng**: ~50 giây.

### 🗣️ Lời thoại gợi ý:
> *"Thưa Thầy Cô, một Dịch vụ thư mục tiêu chuẩn như Active Directory đứng vững dựa trên **4 trụ cột chức năng cốt lõi**:*  
> 1. **Quản trị tập trung (Centralized Administration)**: Toàn bộ danh tính người dùng, máy tính, nhóm và tài nguyên mạng được gom về quản lý tại một trung tâm dữ liệu duy nhất.  
> 2. **Khả năng mở rộng và phân cấp (Scalability & Hierarchy)**: Cho phép doanh nghiệp tổ chức cấu trúc dữ liệu theo sơ đồ hình cây logic (Forest ➔ Domain ➔ OU), giúp mở rộng quy mô kinh doanh không giới hạn mà không làm vỡ cấu trúc mạng.  
> 3. **Tra cứu tài nguyên nhanh chóng (Resource Locating)**: Đóng vai trò như một cuốn danh bạ điện tử thông minh, cho phép người dùng và ứng dụng tìm kiếm máy in, thư mục chia sẻ dễ dàng thông qua giao thức chuẩn **LDAP**.  
> 4. **Bảo mật và kiểm soát truy cập (Security & Access Control)**: Mỗi đối tượng được gắn một định danh an ninh duy nhất gọi là **SID** (Security Identifier) và kiểm soát truy cập thông qua danh sách **ACL** (Access Control List), đảm bảo đúng người, đúng quyền và đúng tài nguyên.*"

### 💡 Ý chính cần nhớ:
- 4 chức năng: Quản trị tập trung, Phân cấp mở rộng, Tra cứu bằng LDAP, Bảo mật bằng SID & ACL.

---

## 🖥️ SLIDE 7: 1.5. MỤC ĐÍCH CHIẾN LƯỢC KHI TRIỂN KHAI ACTIVE DIRECTORY
* **Tên Slide**: MỤC ĐÍCH CHIẾN LƯỢC KHI TRIỂN KHAI ACTIVE DIRECTORY
* **Nội dung trên slide**: SSO, Group Policy (GPO), Delegation of Control, Fault Tolerance.
* **Thời lượng**: ~50 giây.

### 🗣️ Lời thoại gợi ý:
> *"Vậy khi một doanh nghiệp quyết định đầu tư triển khai Active Directory, họ hướng đến **4 mục đích chiến lược** sau:*  
> 1. **Đăng nhập một lần (Single Sign-On - SSO)**: Giúp tăng tối đa trải nghiệm người dùng. Nhân viên chỉ cần nhớ một tài khoản duy nhất là có thể truy cập trơn tru từ máy tính, email, chia sẻ file cho đến các phần mềm nội bộ.  
> 2. **Tự động hóa quản trị qua Group Policy (GPO)**: Quản trị viên có thể áp đặt chính sách an ninh, cấu hình tường lửa, triển khai phần mềm hay khóa cổng USB cho hàng loạt máy tính chỉ bằng một cú nhấp chuột.  
> 3. **Ủy quyền quản trị linh hoạt (Delegation of Control)**: Cho phép chia nhỏ quyền quản trị theo từng phòng ban hoặc chi nhánh (ví dụ: cấp quyền reset mật khẩu cho IT chi nhánh mà không cần phải giao mật khẩu Domain Admin tối cao).  
> 4. **Đảm bảo tính sẵn sàng và chịu lỗi cao (Fault Tolerance)**: Thông qua việc dựng nhiều máy chủ Domain Controller chạy song song và đồng bộ dữ liệu liên tục, nếu một máy chủ gặp sự cố phần cứng, toàn bộ hệ thống đăng nhập vẫn hoạt động bình thường, không làm gián đoạn sản xuất kinh doanh.*"

### 💡 Ý chính cần nhớ:
- 4 lợi ích lớn: SSO (tiện cho user), GPO (tự động hóa quản trị), Delegation (phân quyền an toàn), Fault Tolerance (dự phòng chịu lỗi).

---

## 🖥️ SLIDE 8: 2.1. CẤU TRÚC LOGIC CỦA ACTIVE DIRECTORY
* **Tên Slide**: CHƯƠNG 2: KIẾN TRÚC VÀ CƠ CHẾ HOẠT ĐỘNG - CẤU TRÚC LOGIC
* **Nội dung trên slide**: 1. Objects, 2. OU, 3. Domain, 4. Tree & Forest.
* **Thời lượng**: ~1 phút.

### 🗣️ Lời thoại gợi ý:
> *"Bước sang **Chương 2**, chúng ta sẽ tìm hiểu về Kiến trúc của Active Directory. Cần phân biệt rõ: Active Directory có 2 cấu trúc hoàn toàn tách biệt: **Cấu trúc Logic** và **Cấu trúc Vật lý**.*  
> *Đầu tiên là **Cấu trúc Logic** – đây là cách AD tổ chức dữ liệu theo góc nhìn quản trị, độc lập với vị trí địa lý thực tế. Cấu trúc này chia làm 4 tầng từ nhỏ đến lớn:*  
> - **Tầng 1: Objects (Đối tượng)**: Đơn vị nhỏ nhất, đại diện cho thực thể thực tế như User, Computer, Group, Printer. Mỗi object có các thuộc tính cụ thể như Tên, Email, Số điện thoại.  
> - **Tầng 2: Organizational Unit (OU - Đơn vị tổ chức)**: Là một 'thùng chứa' logic dùng để gom nhóm các đối tượng theo phòng ban (như OU Kế Toán, OU Nhân Sự). *Đặc biệt: OU là cấp nhỏ nhất có thể liên kết trực tiếp chính sách GPO và phân quyền ủy quyền.*  
> - **Tầng 3: Domain (Miền)**: Là đơn vị quản lý và bảo mật chính. Tất cả tài khoản trong cùng 1 Domain chia sẻ chung cơ sở dữ liệu và chính sách mật khẩu.  
> - **Tầng 4: Tree và Forest (Cây và Rừng)**:  
>   + **Tree** là tập hợp các Domain có không gian tên liên tục (ví dụ: `iuh.edu.vn` và con của nó là `cntt.iuh.edu.vn`).  
>   + **Forest** là tập hợp nhiều Tree có thể khác nhau về tên miền nhưng cùng chia sẻ chung Schema, Cấu hình và Global Catalog. *Forest chính là ranh giới an ninh tối cao (Security Boundary) của toàn hệ thống.*"

### 💡 Ý chính cần nhớ:
- 4 cấp Logic: Object ➔ OU (cấp nhỏ nhất gắn GPO) ➔ Domain (ranh giới bảo mật) ➔ Tree & Forest (Forest là ranh giới an ninh tối cao).

### ❓ Câu hỏi Thầy/Cô hay hỏi xoáy:
* **Hỏi**: *"Ranh giới an ninh tối cao (Security Boundary) trong Active Directory là Domain hay Forest?"*
* **Đáp**: *"Dạ thưa Thầy/Cô, là **Forest** ạ! Vì tài khoản quản trị Domain Admins chỉ có toàn quyền trong 1 Domain, nhưng tài khoản **Enterprise Admins** ở cấp Forest mới nắm giữ toàn quyền trên toàn bộ cấu trúc hạ tầng của mọi Domain."*

---

## 🖥️ SLIDE 9: 2.2. CẤU TRÚC VẬT LÝ CỦA ACTIVE DIRECTORY
* **Tên Slide**: CẤU TRÚC VẬT LÝ CỦA ACTIVE DIRECTORY
* **Nội dung trên slide**: 1. Domain Controller (DC), 2. Sites & Subnets (Ví dụ: TP.HCM 192.168.10.0/24 | Hà Nội 172.16.0.0/24).
* **Thời lượng**: ~50 giây.

### 🗣️ Lời thoại gợi ý:
> *"Trái ngược với cấu trúc Logic, **Cấu trúc Vật lý** mô tả vị trí triển khai phần cứng máy chủ và topology đường truyền mạng thực tế. Cấu trúc vật lý gồm 2 thành phần chính:*  
> 1. **Domain Controller (DC)**: Là các máy chủ vật lý hoặc máy ảo cài đặt hệ điều hành Windows Server và kích hoạt dịch vụ AD DS. Mỗi DC lưu trữ bản sao cơ sở dữ liệu `ntds.dit` và thư mục chia sẻ `SYSVOL`, trực tiếp xử lý các yêu cầu đăng nhập, tìm kiếm của người dùng.  
> 2. **Sites và Subnets**:  
>    - **Subnet** là dải địa chỉ mạng IP thực tế của từng văn phòng (ví dụ: Hội sở TP.HCM là `192.168.10.0/24`, Chi nhánh Hà Nội là `172.16.0.0/24`).  
>    - **Site** là ranh giới địa lý đại diện cho một mạng cục bộ LAN tốc độ cao kết nối các Subnet.  
>    - **Ý nghĩa kỹ thuật sống còn của Site**:  
>      + Thứ nhất: Giúp **tối ưu hóa lưu lượng sao chép (Replication)**. Thay vì sao chép liên tục gây nghẽn đường truyền WAN đắt đỏ, quản trị viên có thể lên lịch đồng bộ giữa các Site vào ban đêm.  
>      + Thứ hai: Giúp **tối ưu hóa quá trình đăng nhập (Logon Optimization)**. Máy trạm ở TP.HCM sẽ luôn ưu tiên tìm và đăng nhập vào DC ở TP.HCM, không gửi yêu cầu ra tận Hà Nội làm chậm mạng.*"

### 💡 Ý chính cần nhớ:
- DC: Máy chủ chạy AD DS chứa `ntds.dit` và `SYSVOL`.
- Site & Subnet: Nhóm dải IP theo vị trí địa lý.
- Lợi ích của Site: Giảm nghẽn đường truyền WAN khi đồng bộ và giúp Client đăng nhập vào DC gần nhất.

---

## 🖥️ SLIDE 10: 2.3. SCHEMA VÀ GLOBAL CATALOG (GC)
* **Tên Slide**: SCHEMA VÀ GLOBAL CATALOG (GC)
* **Nội dung trên slide**: 1. Active Directory Schema, 2. Global Catalog (Cổng TCP 3268 / 3269).
* **Thời lượng**: ~1 phút.

### 🗣️ Lời thoại gợi ý:
> *"Để đảm bảo tính nhất quán trên quy mô toàn bộ Rừng (Forest), Active Directory sử dụng 2 thành phần đặc biệt:*  
> 1. **Active Directory Schema**:  
>    - Được xem là **Bản thiết kế (Blueprint)** định nghĩa bộ quy tắc chung cho toàn bộ Forest.  
>    - Schema quy định: Hệ thống được phép có những loại đối tượng nào (**Class Schema**, ví dụ: User, Computer) và mỗi đối tượng có những trường thông tin nào (**Attribute Schema**, ví dụ: họ tên, email, số điện thoại).  
>    - *Quy tắc bất di bất dịch: Trong toàn bộ Forest chỉ có DUY NHẤT một Schema dùng chung.*  
> 2. **Global Catalog (GC)**:  
>    - Là một máy chủ Domain Controller đóng vai trò như **'Cuốn danh bạ vàng'** của toàn bộ Forest.  
>    - Nó lưu trữ toàn bộ thông tin đối tượng của Domain sở tại, cộng với một bản sao rút gọn (**Partial Attribute Set - PAS**) gồm các thuộc tính tra cứu phổ biến nhất (như Tên, Email, Chức vụ) của **TẤT CẢ các đối tượng trong mọi Domain thuộc Forest**.  
>    - Global Catalog hoạt động trên cổng **TCP 3268** (và bảo mật **3269**). Nhờ có Global Catalog, một nhân viên ở TP.HCM có thể tìm kiếm thông tin email của đồng nghiệp ở chi nhánh Đà Nẵng hay Hà Nội ngay tức thì mà không cần phải gửi truy vấn sang từng Domain Controller từ xa!*"

### 💡 Ý chính cần nhớ:
- Schema: Bản thiết kế quy định Class & Attribute, duy nhất 1 Schema cho toàn Forest.
- Global Catalog (GC): Cuốn danh bạ lưu thuộc tính rút gọn của toàn Forest, cổng TCP 3268/3269, giúp tìm kiếm xuyên miền siêu tốc.

### ❓ Câu hỏi Thầy/Cô hay hỏi xoáy:
* **Hỏi**: *"Global Catalog lắng nghe trên cổng (port) nào và lưu những thông tin gì?"*
* **Đáp**: *"Dạ thưa Thầy/Cô, Global Catalog lắng nghe trên cổng **TCP 3268** (hoặc **3269** nếu mã hóa SSL/TLS). Nó lưu đầy đủ đối tượng của Domain nó quản lý và một bản sao thuộc tính rút gọn gọi là **Partial Attribute Set (PAS)** của tất cả đối tượng trong Forest để phục vụ tìm kiếm nhanh và đăng nhập UPN."*

---

## 🖥️ SLIDE 11: 2.4. NĂM VAI TRÒ FSMO (OPERATIONS MASTER ROLES)
* **Tên Slide**: NĂM VAI TRÒ FSMO (OPERATIONS MASTER ROLES)
* **Nội dung trên slide**: Bảng 5 vai trò FSMO (Schema Master, Domain Naming Master, PDC Emulator, RID Master, Infrastructure Master).
* **Thời lượng**: ~1 phút 30 giây (Slide cực kỳ quan trọng!).

### 🗣️ Lời thoại gợi ý:
> *"Thưa Thầy Cô, mặc dù Active Directory hoạt động theo cơ chế **Multi-Master** (cho phép ghi dữ liệu đồng thời ở bất kỳ DC nào), nhưng để tránh xung đột dữ liệu chết người, Microsoft quy định có **5 nhiệm vụ nhạy cảm đặc biệt chỉ được phép do DUY NHẤT MỘT Domain Controller đảm nhận** tại một thời điểm. Đó chính là 5 vai trò **FSMO (Flexible Single Master Operation)**:*  
>  
> *5 vai trò này được phân bố ở 2 cấp độ:*  
>  
> 🌟 **CẤP ĐỘ 1: TOÀN FOREST (Mỗi Forest chỉ có duy nhất 1 máy nắm giữ - Forest-Wide)**:  
> 1. **Schema Master**: Là máy chủ duy nhất có quyền ghi và thay đổi cấu trúc Schema (ví dụ: cài đặt Microsoft Exchange Server mở rộng thuộc tính email).  
> 2. **Domain Naming Master**: Là máy chủ duy nhất có quyền thêm mới, xóa bỏ hoặc đổi tên một Domain trong Forest.  
>  
> 🌟 **CẤP ĐỘ 2: TỪNG DOMAIN (Mỗi Domain trong Forest có 1 bộ riêng - Domain-Wide)**:  
> 3. **PDC Emulator**: Được mệnh danh là **'Nhạc trưởng'** của Domain. Đảm nhận 3 việc quan trọng nhất: đồng bộ thời gian mạng (Time Sync / NTP), xử lý đổi mật khẩu khẩn cấp và làm máy chủ master ưu tiên chỉnh sửa Group Policy (GPO).  
> 4. **RID Master (Relative ID)**: Có nhiệm vụ cấp phát từng khối 500 định danh con (gọi là RID Pool) cho các DC khác. Khi một DC tạo User hay Computer mới, nó sẽ lấy một số RID trong kho này ghép với SID của Domain để tạo ra một SID duy nhất toàn cầu cho đối tượng.  
> 5. **Infrastructure Master**: Chuyên cập nhật và duy trì tính nhất quán của các tham chiếu đối tượng liên miền (Cross-domain references), ví dụ khi một User ở Domain A được thêm vào Group của Domain B.*  
>  
> *(Kết lời chuyển ý)*: *'Thưa Thầy Cô, trên máy Domain Controller đầu tiên được cài đặt trong hệ thống, mặc định nó sẽ nắm giữ toàn bộ cả 5 vai trò FSMO này. Đây cũng chính là nội dung khép lại 2 chương lý thuyết nền tảng. Tiếp theo, nhóm em xin chuyển sang phần các cơ chế mở rộng, bảo mật và kịch bản thực hành demo...'* "

### 💡 Ý chính cần nhớ:
- FSMO = Flexible Single Master Operations (5 vai trò độc quyền).
- Cấp Forest (2 roles): Schema Master (sửa schema), Domain Naming Master (thêm/xóa domain).
- Cấp Domain (3 roles): PDC Emulator (đồng bộ giờ NTP, đổi pass, GPO), RID Master (cấp khối RID tạo SID), Infrastructure Master (tham chiếu chéo liên miền).
- Mặc định DC đầu tiên của Forest sẽ ôm trọn cả 5 vai trò FSMO.

### ❓ Câu hỏi Thầy/Cô hay hỏi xoáy:
* **Hỏi**: *"Trong 5 vai trò FSMO, vai trò nào bận rộn nhất và quan trọng nhất đối với hoạt động hàng ngày của người dùng?"*
* **Đáp**: *"Dạ thưa Thầy/Cô, đó là **PDC Emulator** ạ! Vì nếu PDC Emulator gặp sự cố, việc đồng bộ thời gian mạng bị sai lệch dẫn đến lỗi xác thực vé Kerberos, việc đổi mật khẩu của người dùng không được cập nhật ngay lập tức và các ứng dụng cũ sẽ bị gián đoạn."*
* **Hỏi**: *"Khi RID Master bị chết (offline), các Domain Controller khác có tạo được User mới ngay lập tức không?"*
* **Đáp**: *"Dạ vẫn tạo được bình thường ạ! Vì mỗi DC đã được cấp sẵn một kho dự trữ 500 RID (RID Pool). Chỉ khi nào DC đó dùng hết sạch 500 RID mà không liên lạc được với RID Master để xin cấp tiếp thì lúc đó mới bị chặn không cho tạo đối tượng mới."*

---

## 🎯 TỔNG KẾT BẢNG TRA CỨU NHANH CHO 11 SLIDE

| Slide | Chủ đề cốt lõi | Từ khóa kỹ thuật cần nói bật lên |
| :---: | :--- | :--- |
| **1** | Trang bìa & Giới thiệu | Nhóm 1, Active Directory Domain Services, Windows Server |
| **2** | Mục lục tổng quan | 4 Chương: Lý thuyết ➔ Kiến trúc ➔ ADPREP/RODC ➔ Demo thực hành |
| **3** | Bối cảnh ra đời | Workgroup (SAM cục bộ, <10 máy) ➔ Doanh nghiệp mở rộng ➔ Nhu cầu Directory Service |
| **4** | So sánh Workgroup vs Domain | SAM cục bộ vs `ntds.dit`; Kerberos v5; Single Sign-On (SSO); GPO tập trung; Multi-Master |
| **5** | Lịch sử phát triển | Win 2000 (AD khai sinh) ➔ 2003 (ADPREP) ➔ 2008 (RODC) ➔ 2012 (bỏ dcpromo) ➔ 2022 (Hybrid Cloud) |
| **6** | 4 Chức năng cốt lõi | Quản trị tập trung; Mở rộng phân cấp; Tra cứu bằng LDAP; Bảo mật bằng SID & ACL |
| **7** | 4 Mục đích chiến lược | Đăng nhập 1 lần (SSO); Tự động hóa GPO; Ủy quyền (Delegation); Chịu lỗi (Fault Tolerance) |
| **8** | Cấu trúc Logic | Object ➔ OU (nhỏ nhất gán GPO) ➔ Domain (ranh giới bảo mật) ➔ Tree & Forest (an ninh tối cao) |
| **9** | Cấu trúc Vật lý | Domain Controller (`ntds.dit`, `SYSVOL`); Site & Subnet (tối ưu đường truyền WAN, đăng nhập DC gần nhất) |
| **10** | Schema & Global Catalog | Schema (Blueprint duy nhất Forest); Global Catalog (danh bạ toàn Forest, port TCP 3268/3269, PAS) |
| **11** | 5 Vai trò FSMO | Forest: Schema Master, Domain Naming; Domain: PDC Emulator (giờ NTP, pass), RID Master (RID pool), Infrastructure |
