# PHÂN TÍCH CHI TIẾT BÀI GIẢNG & CHỈ ĐẠO CỦA THẦY TRƯƠNG BÁ PHÚC (04/10/2026)

> **Môn học**: Kiến trúc & Thiết kế Phần mềm / Công nghệ Web - Web Service (IUH)  
> **Giảng viên**: Thầy Trương Bá Phúc (Khoa Công nghệ Thông tin - Đại học Công nghiệp TP.HCM)  
> **Video nguồn**: `Videos/2026-10-04 18-01-23.mp4` (Thời lượng: 13 phút 07 giây)  
> **Chủ đề chính**: **Khởi động JPA (Java Persistence API) & Cài đặt / Cấu hình MySQL Server, MySQL Workbench**  
> **Vị trí bài học trong chương trình**: Đây là **nội dung lý thuyết cốt lõi cuối cùng** của môn học trước khi bước vào giai đoạn dồn toàn lực làm Bài tập lớn / Đồ án cuối kỳ.

---

## MỤC LỤC
1. [TỔNG KẾT NHANH 5 CHỈ ĐẠO CỐT TỬ CỦA THẦY TRƯƠNG BÁ PHÚC](#1-tổng-kết-nhanh-5-chỉ-đạo-cốt-tử-của-thầy-trương-bá-phúc)
2. [BẢNG BÓC BĂNG CHI TIẾT TỪNG MỐC THỜI GIAN (TRANSCRIPT ĐỐI CHIẾU)](#2-bảng-bóc-băng-chi-tiết-từng-mốc-thời-gian-transcript-đối-chiếu)
3. [PHÂN TÍCH CHUYÊN SÂU 5 TRỌNG TÂM KIẾN THỨC VÀ YÊU CẦU CỦA THẦY](#3-phân-tích-chuyên-sâu-5-trọng-tâm-kiến-thức-và-yêu-cầu-của-thầy)
   - [Trọng tâm 1: Bức tranh toàn cảnh môn học (Front-End & Back-End đã học gì)](#trọng-tâm-1-bức-tranh-toàn-cảnh-môn-học-front-end--back-end-đã-học-gì)
   - [Trọng tâm 2: JPA - Mắt xích cuối cùng và Lộ trình Bài tập lớn](#trọng-tâm-2-jpa---mắt-xích-cuối-cùng-và-lộ-trình-bài-tập-lớn)
   - [Trọng tâm 3: Hướng dẫn cài đặt MySQL Server & Lưu ý về phiên bản](#trọng-tâm-3-hướng-dẫn-cài-đặt-mysql-server--lưu-ý-về-phiên-bản)
   - [Trọng tâm 4: Hai trường phái quản trị Database (CLI vs GUI Workbench)](#trọng-tâm-4-hai-trường-phái-quản-trị-database-cli-vs-gui-workbench)
   - [Trọng tâm 5: "Quy tắc sống còn": Username root và Password MySQL](#trọng-tâm-5-quy-tắc-sống-còn-username-root-và-password-mysql)
   - [Trọng tâm 6: Hướng dẫn tạo New Schema (Database) trên MySQL Workbench](#trọng-tâm-6-hướng-dẫn-tạo-new-schema-database-trên-mysql-workbench)
4. [ĐỐI CHIẾU VỚI DỰ ÁN BÀI 7 (B7_DEPARTMENT_STAFF_MYSQL) ĐÃ XÂY DỰNG](#4-đối-chiếu-với-dự-án-bài-7-b7_department_staff_mysql-đã-xây-dựng)
5. [CHECKLIST 15 PHÚT HÀNH ĐỘNG ĐỂ KHÔNG BỊ "KHÔNG ĐIỂM" KHI THẦY KIỂM TRA](#5-checklist-15-phút-hành-động-để-không-bị-không-điểm-khi-thầy-kiểm-tra)

---

## 1. TỔNG KẾT NHANH 5 CHỈ ĐẠO CỐT TỬ CỦA THẦY TRƯƠNG BÁ PHÚC

Nếu bạn cần nắm bắt nhanh nội dung bài giảng ngày 04/10/2026, đây là **5 điều thầy Phúc nhấn mạnh**:

1. **JPA là nội dung cuối cùng**: Toàn bộ kiến thức Front-End (HTML/CSS/JS/Thymeleaf) và Back-End (Spring Boot, Controller, Model, REST Web Service) cả lớp đã học xong. JPA (Java Persistence API) là mảnh ghép cuối cùng để lưu trữ dữ liệu vào Cơ sở dữ liệu vật lý thay vì lưu tạm trong RAM.
2. **Dành toàn bộ thời gian còn lại cho Bài tập lớn**: Sau khi hoàn thành bài thực hành JPA này, các tuần tiếp theo sẽ không dạy lý thuyết mới nữa mà sinh viên dùng toàn bộ thời gian trên lớp để làm Bài tập lớn / Đồ án nhóm.
3. **Cài đặt 2 công cụ bắt buộc**:
   - **MySQL Server** (Service chạy ngầm cổng `3306` để quản lý CSDL).
   - **MySQL Workbench** (Phần mềm giao diện đồ họa GUI để thao tác trực quan bằng chuột, tạo bảng, xem dữ liệu).
4. **"MẬT KHẨU ĐẶT CÁI GÌ LÀ PHẢI NHỚ - KHÔNG NHỚ LÀ THUA"**: Thầy nhấn mạnh nhiều lần: Username mặc định là `root`, password đặt cái gì thì phải ghi nhớ chính xác tuyệt đối. Nếu quên password, Spring Boot sẽ không thể kết nối vào Database và toàn bộ bài thi/bài tập lớn sẽ bị đứng cứng ngắc.
5. **Yêu cầu 15 phút thực hành**: Thầy cho cả lớp 15 phút để cài đặt xong MySQL Server, mở MySQL Workbench, vào tab **Schemas** nhấp chuột phải tạo một **New Schema (Database mới)**. Sau 15 phút thầy sẽ quay lại giảng tiếp cách kết nối Spring Boot JPA vào Schema này.

---

## 2. BẢNG BÓC BĂNG CHI TIẾT TỪNG MỐC THỜI GIAN (TRANSCRIPT ĐỐI CHIẾU)

Dưới đây là bảng ghi lại chính xác từng đoạn ghi âm từ video gốc và diễn giải chuẩn hóa ngữ nghĩa chuyên ngành công nghệ thông tin:

| Mốc thời gian | Lời ghi âm của Thầy Trương Bá Phúc | Văn bản diễn giải chuẩn hóa chuyên ngành |
| :--- | :--- | :--- |
| `02:12 - 03:00` | *Cái này có đọc chưa? Cái kênh này xác cài.* | Thầy bắt đầu buổi học, kiểm tra việc sinh viên đã đọc tài liệu hướng dẫn và chuẩn bị môi trường cài đặt chưa. |
| `03:00 - 03:07` | *Hôm nay chúng ta vào về JPA ha. Đây là nội dung cuối của cái môn học này.* | **"Hôm nay chúng ta học về JPA (Java Persistence API) nhé. Đây là nội dung lý thuyết cuối cùng của môn học này."** |
| `03:07 - 03:56` | *Tóm kết lại là chúng ta đã học về Front-End... Chúng ta học được cách tạo Bootstrap, CSS, JavaScript, Thymeleaf... chúng ta biết dùng jQuery để gọi Web Service, lấy dữ liệu bạt nó ra và đưa nó lên giao diện Front-End.* | **Tổng kết khối kiến thức Front-End:**<br>- Giao diện web tĩnh & template động (Bootstrap, CSS, JS, Thymeleaf).<br>- Kỹ thuật gọi REST API bất đồng bộ (jQuery AJAX / Fetch API).<br>- Đọc dữ liệu JSON trả về và binding (đổ) vào Table, Form, Combobox. |
| `03:56 - 04:54` | *Phía bên Back-End chúng ta học được cái gì rồi? Chúng ta dựng được Web App, Web Server dùng Spring Boot... biết cấu hình thư viện, tạo Controller, tạo Model bắn qua Thymeleaf, tạo Web Service luôn, cũng khá là nhiều.* | **Tổng kết khối kiến thức Back-End:**<br>- Dựng ứng dụng trên nền tảng Spring Boot.<br>- Quản lý thư viện phụ thuộc bằng Maven (`pom.xml`).<br>- Viết `Controller` (`@RestController`, `@Controller`).<br>- Viết `Model` (POJO Class) để truyền dữ liệu qua Thymeleaf hoặc serialize thành JSON.<br>- Xây dựng RESTful Web Service chuẩn (GET, POST, PUT, DELETE). |
| `04:54 - 05:18` | *Và phần còn lại là kết nối Database, là nội dung cuối cùng. Sau nội dung này, chúng ta dành phần lớn thời gian cho bài tập lớn.* | **Định hướng học tập:**<br>- Kết nối Database (Cơ sở dữ liệu) thông qua JPA/Hibernate là mắt xích hoàn thiện kiến trúc 3 lớp (3-tier).<br>- Sau buổi hôm nay, sinh viên sẽ vận dụng toàn bộ kiến thức để làm Đồ án / Bài tập lớn nhóm. |
| `05:18 - 05:34` | *Nhiều bạn cơ bản không có mở cam nên thầy sẽ... thầy cho ra ngoài không điểm này. Các bạn đợi thầy chụp...* | **Kỷ luật phòng học:** Thầy kiểm tra chuyên cần, yêu cầu sinh viên bật camera nghiêm túc, chụp màn hình điểm danh, sinh viên vắng mặt hoặc không tập trung sẽ bị trừ điểm/cho ra ngoài. |
| `07:49 - 08:34` | *Bước đầu tiên, bước 1 là chúng ta cài đặt MySQL Server... MySQL Server nó có 2 cái gói... Các bạn tải về, cái gì có chúng ta xài... thường bản mới nó ngon, bản cao. Bạn nào chưa có thì cài, bản thấp thì mới làm sẽ bị không tương thích...* | **Hướng dẫn cài đặt MySQL:**<br>- Bước 1: Cài đặt MySQL Server.<br>- Lưu ý chọn bộ cài đặt phù hợp (bản Community Server x64).<br>- Khuyên dùng phiên bản ổn định, tương thích với JDK/Spring Boot để tránh lỗi driver hoặc xung đột cổng kết nối. |
| `08:34 - 09:21` | *Có những người làm quen rồi thì bản nào cũng chạy được, cấu hình được... rồi MySQL Workbench, ok...* | Với người đã có kinh nghiệm thì phiên bản nào cũng chạy được nhờ biết sửa cấu hình port và driver trong file properties. |
| `09:21 - 10:40` | *Tức là khi mà các bạn cài MySQL Server, có nhiều người giỏi người ta không cần cài giao diện, người ta dùng command line, gõ lệnh create table, drop table, select from where, insert, update... Còn những người không thường làm, dù có thể cũng rất giỏi nhưng không thường làm thì dùng MySQL Workbench nhé, nó lẹ. Cái này giao diện đồ họa, mở ra là xài được, dùng chuột là chính.* | **Phân tích 2 công cụ quản trị CSDL:**<br>1. **Dòng lệnh (CLI)**: Gõ trực tiếp các câu lệnh SQL DDL/DML (`CREATE`, `ALTER`, `DROP`, `SELECT`, `INSERT`, `UPDATE`, `DELETE`). Dành cho DevOps hoặc người làm server headless.<br>2. **Giao diện đồ họa (MySQL Workbench GUI)**: Thao tác bằng chuột, có thanh công cụ trực quan, xem bảng biểu nhanh chóng, cực kỳ tiện lợi cho sinh viên làm bài tập và đồ án. |
| `10:40 - 10:54` | *Các bạn cài, cái user mặc định là root, password đặt cái gì là PHẢI NHỚ. Thầy cho các bạn 15 phút, các bạn làm xong cái này quay lại thầy giảng tiếp. Không có cái này không làm được gì hết. Cài đặt nhé!* | **CẢNH BÁO QUAN TRỌNG NHẤT:**<br>- User quản trị mặc định: `root`.<br>- Password: **Bắt buộc phải nhớ kỹ**.<br>- Thời gian làm bài trên máy: **15 phút**.<br>- Nếu không cài đặt và không có tài khoản Database thì các bước JPA tiếp theo không thể thực hành được. |
| `10:54 - 11:21` | *Cái user, cái tên của user mặc định là root và password là gì là phải nhớ, không nhớ là thua.* | Thầy lặp lại lần 2 để khắc sâu cho sinh viên: Quên password CSDL là không thể kết nối từ Spring Boot. |
| `11:21 - 11:39` | *Sau khi mà làm xong, nhớ làm thêm việc này nữa này: bấm vào cái thẻ Schemas, tạo New Schema, tức là tạo New Database. Tạo sẵn một cái Database trong đó rồi chuẩn bị sẵn sàng.* | **Thao tác chốt hạ trên MySQL Workbench:**<br>1. Mở MySQL Workbench.<br>2. Nhìn cột bên trái, chọn tab **Schemas**.<br>3. Chuột phải chọn **Create Schema...** (tạo mới CSDL).<br>4. Đặt tên Database và nhấn **Apply**. |

---

## 3. PHÂN TÍCH CHUYÊN SÂU 5 TRỌNG TÂM KIẾN THỨC VÀ YÊU CẦU CỦA THẦY

### Trọng tâm 1: Bức tranh toàn cảnh môn học (Front-End & Back-End đã học gì)
Thầy Trương Bá Phúc hệ thống lại toàn bộ kiến trúc ứng dụng web hiện đại gồm 3 tầng (3-Tier Architecture) mà sinh viên đã đi qua:

```
[ FRONT-END (Giao diện) ]
  - HTML5, CSS3, Bootstrap (Layout, Responsive)
  - Thymeleaf (Server-Side Rendering)
  - JavaScript / jQuery / Fetch API (Client-Side Rendering)
           │
           ▼  (HTTP Request / JSON qua REST API)
[ BACK-END (Ứng dụng Spring Boot) ]
  - Web Server (Tomcat nhúng)
  - Controller (@RestController, @Controller): Tiếp nhận request, routing
  - Model (Entity/POJO): Định nghĩa cấu trúc dữ liệu
  - Service (@Service): Xử lý logic nghiệp vụ
           │
           ▼  (JPA / Hibernate / JDBC Driver)
[ DATABASE (Cơ sở dữ liệu - MẮT XÍCH HÔM NAY) ]
  - MySQL Server (Lưu trữ bảng, quan hệ 1-N, khóa ngoại, dữ liệu bền vững)
```

Trước buổi học này, ở các bài tập từ B1 đến B6, toàn bộ dữ liệu mẫu đều được lưu trong bộ nhớ tạm RAM (dùng `ArrayList<T>` bên trong `Service`). Nhược điểm chí mạng là: **Mỗi lần tắt ứng dụng hoặc khởi động lại server là mất sạch dữ liệu!**

---

### Trọng tâm 2: JPA - Mắt xích cuối cùng và Lộ trình Bài tập lớn
- **JPA (Java Persistence API)** là chuẩn của Java giúp lập trình viên thao tác với Cơ sở dữ liệu quan hệ (RDBMS) hoàn toàn thông qua các Class và Object Java, không cần phải viết tay các câu lệnh SQL dài dòng (`SELECT * FROM ...`, `INSERT INTO ...`).
- Cơ chế này gọi là **ORM (Object-Relational Mapping)**:
  - Class Java (`@Entity`) $\longleftrightarrow$ Table trong MySQL.
  - Thuộc tính (`private Long id`, `private String name`) $\longleftrightarrow$ Cột (`Column`) trong MySQL.
  - Quan hệ giữa các Class (`@ManyToOne`, `@OneToMany`) $\longleftrightarrow$ Khóa ngoại (`Foreign Key`) giữa các bảng.
- **Lộ trình đồ án**: Thầy nêu rõ sau buổi thực hành JPA này, môn học chuyển sang giai đoạn sinh viên tự làm **Bài tập lớn / Đồ án môn học**. Sinh viên sẽ áp dụng đúng mô hình này cho đề tài của nhóm mình (ví dụ: Quản lý Phòng ban & Nhân viên, Quản lý Lớp học & Sinh viên, Quản lý Danh mục & Sản phẩm).

---

### Trọng tâm 3: Hướng dẫn cài đặt MySQL Server & Lưu ý về phiên bản
Thầy lưu ý khi cài đặt MySQL trên máy tính cá nhân:
1. **Gói cài đặt**: Tải gói `MySQL Community Server` (bản miễn phí, mã nguồn mở). Thường kèm theo `MySQL Installer` cho Windows.
2. **Cổng mặc định (Port)**: MySQL luôn sử dụng cổng **`3306`**. Nếu máy bạn đã cài XAMPP, WampServer hoặc một phiên bản MySQL khác từ trước, cần kiểm tra để tránh xung đột cổng `3306`.
3. **Tính tương thích**: Khuyên dùng phiên bản MySQL 8.0.x hoặc 8.4.x LTS để tương thích tốt nhất với thư viện `mysql-connector-j` hiện đại của Spring Boot 3.

---

### Trọng tâm 4: Hai trường phái quản trị Database (CLI vs GUI Workbench)
Thầy phân tích rất thực tế cho sinh viên:
- **Dùng Command Line (CLI)**: Người làm hạ tầng mạng hoặc quản trị máy chủ Linux thường dùng lệnh:
  ```bash
  mysql -u root -p
  CREATE DATABASE company_db;
  USE company_db;
  SELECT * FROM staffs WHERE department_id = 1;
  ```
- **Dùng MySQL Workbench (GUI - Khuyên dùng cho sinh viên)**:
  - Có giao diện trực quan, bảng điều khiển xem dữ liệu dưới dạng lưới giống Excel.
  - Có công cụ **EER Diagram (Designer)** giúp xem sơ đồ quan hệ khóa ngoại (Foreign Key) giữa các bảng có đường kẻ nối xanh/đỏ rất trực quan.
  - Thao tác nhanh bằng chuột, tạo Schema chỉ với 2 click chuột.

---

### Trọng tâm 5: "Quy tắc sống còn": Username root và Password MySQL
Đây là điểm thầy nhắc đi nhắc lại với giọng điệu gay gắt nhất:
> *"Cái user mặc định là `root`, password đặt cái gì là **PHẢI NHỚ**. Không nhớ là thua, không làm được gì tiếp!"*

**Tại sao thầy lại nhấn mạnh điều này?**
Bởi vì khi viết ứng dụng Spring Boot, trong file cấu hình `src/main/resources/application.properties`, bạn bắt buộc phải cung cấp thông tin tài khoản để Spring Boot đăng nhập vào MySQL:

```properties
# CẤU HÌNH KẾT NỐI MYSQL LOCAL THEO HƯỚNG DẪN CỦA THẦY:
spring.datasource.url=jdbc:mysql://localhost:3306/ten_database_vua_tao?useSSL=false&serverTimezone=UTC
spring.datasource.username=root
spring.datasource.password=MAT_KHAU_BAN_DA_DAT_LUC_CAI_DAT  <--- KHÔNG NHỚ DÒNG NÀY LÀ SPRING BOOT BÁO LỖI CRASH APP!
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver

# HIBERNATE TỰ ĐỘNG TẠO BẢNG TỪ MODEL:
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
```
Nếu bạn quên mật khẩu `root`, MySQL sẽ từ chối kết nối (`Access denied for user 'root'@'localhost' (using password: YES)`), dẫn đến việc ứng dụng Spring Boot không thể khởi động được.

---

### Trọng tâm 6: Hướng dẫn tạo New Schema (Database) trên MySQL Workbench
Thầy yêu cầu sinh viên thực hiện 4 bước sau trên MySQL Workbench:
1. Mở **MySQL Workbench** $\rightarrow$ Click vào kết nối **Local instance MySQL80** (nhập mật khẩu `root` đã đặt).
2. Tại cột bên trái (thanh Navigator), chuyển sang tab **Schemas**.
3. Nhấp chuột phải vào khoảng trống trong tab Schemas $\rightarrow$ Chọn **Create Schema...**
4. Trong ô **Schema Name**, nhập tên Database muốn tạo (ví dụ: `company_db` hoặc `b7_db`) $\rightarrow$ Bấm nút **Apply** ở góc dưới bên phải $\rightarrow$ Bấm **Apply** một lần nữa để xác nhận câu lệnh SQL $\rightarrow$ Bấm **Finish**.
5. Database mới sẽ xuất hiện trong danh sách Schemas, sẵn sàng để Spring Boot kết nối vào.

---

## 4. ĐỐI CHIẾU VỚI DỰ ÁN BÀI 7 (`B7_DEPARTMENT_STAFF_MYSQL`) ĐÃ XÂY DỰNG

Dự án **Bài 7** nằm tại thư mục [d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\t2\b7_department_staff_mysql](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/bt/t2/b7_department_staff_mysql) mà chúng ta đã hoàn thiện chính là **bài mẫu hoàn hảo 100%** đáp ứng đúng toàn bộ yêu cầu thầy đưa ra trong video này:

| Yêu cầu của Thầy trong video | Hiện trạng triển khai trong dự án Bài 7 |
| :--- | :--- |
| **Học về JPA & Hibernate** | Đã cấu hình `spring-boot-starter-data-jpa` trong `pom.xml`. Sử dụng đầy đủ các annotation `@Entity`, `@Table`, `@Id`, `@GeneratedValue`, `@Column`. |
| **Mô hình thực thể 1 - N** | Entity `Department` (Phòng ban) có `@OneToMany private List<Staff> staffs`. Entity `Staff` (Nhân viên) có `@ManyToOne @JoinColumn(name = "department_id")`. |
| **Kế thừa JpaRepository** | Có `DepartmentRepository` và `StaffRepository` kế thừa `JpaRepository<T, ID>`, không cần viết SQL bằng tay. |
| **Kết nối Database MySQL** | Đã cấu hình kết nối chuẩn trong `application.properties`. Đặc biệt hỗ trợ cả: <br>1. **MySQL Local**: Theo tài khoản `root` của máy trường.<br>2. **MySQL Cloud (Clever Cloud)**: Không cần cài đặt máy trạm, chạy trực tiếp trên mây, có sẵn phpMyAdmin Designer hiển thị sơ đồ khóa ngoại màu xanh lá cây cực đẹp. |
| **Khởi tạo dữ liệu tự động** | Có sẵn `CommandLineRunner initData(...)` trong `DemoApplication.java`: Khi khởi chạy, hệ thống tự động chèn 4 phòng ban và 5 nhân viên mẫu vào MySQL. |
| **Giao diện chuẩn thi giữa kỳ** | Giao diện SPA thuần đơn giản, không emoji lòe loẹt, có Combobox lọc theo phòng ban, ô tìm kiếm theo tên, nút Thêm/Sửa/Xóa kèm Modal pop-up mượt mà. |

---

## 5. CHECKLIST 15 PHÚT HÀNH ĐỘNG ĐỂ KHÔNG BỊ "KHÔNG ĐIỂM" KHI THẦY KIỂM TRA

Khi thầy Phúc đi xuống từng máy để kiểm tra sau 15 phút, bạn hãy thực hiện theo đúng các bước sau:

- [ ] **Bước 1: Mở sẵn MySQL Workbench trên màn hình**:
  - Đăng nhập vào kết nối `Local instance`.
  - Mở tab **Schemas**, chỉ chuột vào Schema vừa tạo (ví dụ: `company_db`).
- [ ] **Bước 2: Ghi nhớ mật khẩu `root`**:
  - Viết nháp mật khẩu vào một file notepad hoặc ghi nhớ trong đầu để khi thầy hỏi *"Mật khẩu database của em là gì?"* là trả lời ngay lập tức.
- [ ] **Bước 3: Mở sẵn Eclipse chứa project `b7_department_staff_mysql`**:
  - Mở file [application.properties](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/bt/t2/b7_department_staff_mysql/src/main/resources/application.properties).
  - Mở file [Department.java](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/bt/t2/b7_department_staff_mysql/src/main/java/com/example/demo/model/Department.java) và [Staff.java](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/bt/t2/b7_department_staff_mysql/src/main/java/com/example/demo/model/Staff.java).
- [ ] **Bước 4: Chạy ứng dụng và trình chiếu giao diện**:
  - Nhấp chuột phải vào [DemoApplication.java](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/bt/t2/b7_department_staff_mysql/src/main/java/com/example/demo/DemoApplication.java) $\rightarrow$ `Run As` $\rightarrow$ `Spring Boot App`.
  - Mở trình duyệt tại: `http://localhost:8080/index.html`.
  - Nếu thầy yêu cầu kiểm tra Database: Mở tab phpMyAdmin Clever Cloud (hoặc MySQL Workbench Local), chạy lệnh `SELECT * FROM staffs;` cho thầy thấy dữ liệu thực sự đã được lưu vào MySQL.
