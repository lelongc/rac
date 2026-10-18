# PHÂN TÍCH CHI TIẾT TỪNG Ý HỎI - ĐÁP CỦA THẦY VÀ SINH VIÊN (18/10/2026)
> **Môn học:** Công cụ Phát triển Phần mềm Hướng Dữ liệu / Công nghệ Web  
> **Giảng viên:** Thầy Trương Bá Phúc — IUH  
> **Tài liệu đối chiếu:** [FULL_THOAI_BUOI_HOC_2026_10_18.md](file:///d:/folder/rac/iuh/môn/hk1-4/cc-web-website-hld/ck-luu-y/FULL_THOAI_BUOI_HOC_2026_10_18.md)

---

## 🎯 CHUYÊN ĐỀ 1: LỊCH THI, CỘT ĐIỂM & QUY ĐỊNH BÀI TẬP LỚN

### 1. Phân tích lời dặn của Thầy:
- **Cơ cấu điểm:** Môn học gồm nhiều cột điểm: Chuyên cần/thực hành, kiểm tra giữa kỳ, bài tập lớn và thi cuối kỳ. Điểm giữa kỳ có thấp thì vẫn còn **buổi thực hành cuối** và **Bài tập lớn** để kéo điểm lên.
- **Lịch thi cuối kỳ:** Đã công bố chính thức vào **ngày 22/11/2026** (thi tự luận làm bài trên giấy).
- **Lịch nộp & Báo cáo Bài tập lớn (BTL):**
  - **Phương án 1 (Báo cáo sớm):** Tuần sau (dành cho các nhóm đã hoàn thiện xong sớm).
  - **Phương án 2 (Đa số cả lớp chọn):** Báo cáo vào **Chủ nhật ngày 01/11/2026**.
  - **Địa điểm & Thời gian:** Thầy ngồi chấm tại **Phòng Giáo viên từ 9h30 sáng đến 17h30 chiều**.

### 2. Quy cách làm Báo cáo BTL Thầy yêu cầu:
- **Độ dài quyển báo cáo:** Từ **15 đến 20 trang** (không làm quá dài, không làm quá ngắn sơ sài).
- **Nội dung bắt buộc:**
  1. Mô tả đề tài, phân tích yêu cầu nghiệp vụ.
  2. Thiết kế cơ sở dữ liệu: Sơ đồ ERD, danh sách bảng, khóa chính, khóa ngoại.
  3. Thiết kế kiến trúc: Mô hình MVC, các tầng Controller, Service, Repository.
  4. Trình bày chức năng và chụp ảnh màn hình kết quả chạy (giao diện Web, gọi API Postman).
- ❌ **LƯU Ý CỐT TỬ CỦA THẦY:** **Tuyệt đối KHÔNG copy-paste mã nguồn (source code) vào báo cáo** (vừa tốn trang vừa phản cảm). Source code sẽ được Thầy trực tiếp kiểm tra trên máy tính khi vấn đáp.

---

## 🎯 CHUYÊN ĐỀ 2: PHÂN ĐỊNH FRONT-END VS BACK-END & TẦNG SERVICE

### 1. Thầy hỏi bạn Phan Quốc Khánh:
> **Thầy hỏi:** *"Nhiệm vụ của Front-End trong môn học là gì? Em làm gì?"*  
> **Bạn Khánh đáp:** *"Dạ em làm giao diện, HTML, CSS, JavaScript."*  
> **Thầy hỏi tiếp:** *"Vậy tầng Service là nằm ở bên nào?"*  
> **Sinh viên đáp:** *"Dạ tầng Service là thuộc bên Back-End!"*

### 2. Phân tích học thuật & Câu trả lời chuẩn 10/10:
- **Front-End (Phía Client):**  
  - Chịu trách nhiệm về **Giao diện người dùng (UI - User Interface)** và **Trải nghiệm người dùng (UX)**.
  - Sử dụng: HTML5 (cấu trúc), CSS3 (định dạng, bố cục), JavaScript/Fetch API (gọi HTTP request bất đồng bộ tới server để lấy dữ liệu JSON render ra bảng).
- **Back-End (Phía Server):**  
  - Chịu trách nhiệm về **Xử lý nghiệp vụ (Business Logic)**, **Bảo mật (Security, Authentication)** và **Lưu trữ dữ liệu (Database)**.
  - Tầng **Service** nằm hoàn toàn ở **Back-End**. Nó đóng vai trò trung gian giữa Controller và Repository, chứa các thuật toán tính toán, kiểm tra ràng buộc nghiệp vụ (Validation) và quản lý giao dịch (`@Transactional`).

---

## 🎯 CHUYÊN ĐỀ 3: MÔ HÌNH MVC & VAI TRÒ CỦA MODEL

### 1. Thầy hỏi các bạn trong lớp:
> **Thầy hỏi:** *"Trong kiến trúc MVC, còn nhớ Model là gì không?"*  
> **Bạn học ấp úng:** *"Dạ Model là mô hình... dưỡng cốt..."* (Bị Thầy nhắc nhở vì trả lời lan man).

### 2. Phân tích câu trả lời chuẩn xác:
Trong mô hình **MVC (Model - View - Controller)**:
- **Model:** Là tầng đại diện cho **Dữ liệu và Trạng thái** của hệ thống. Trong Spring Boot, Model gồm:
  1. **Entity (Thực thể):** Ánh xạ trực tiếp với bảng trong CSDL (như `Student`, `Blog`, `User`).
  2. **DTO (Data Transfer Object):** Đối tượng đóng gói dữ liệu truyền nhận giữa Client và Server (như `StudentRequest`).
- **View:** Tầng hiển thị giao diện cho người dùng (Thymeleaf HTML hoặc JSON trả về cho React/SPA).
- **Controller:** Tầng tiếp nhận request từ Client, gọi Service xử lý rồi chuyển dữ liệu Model qua View hiển thị.

---

## 🎯 CHUYÊN ĐỀ 4: DEPENDENCY INJECTION, IMPLICIT VÀ EXPLICIT

### 1. Thầy hỏi bạn Tuấn Kiệt:
> **Thầy hỏi:** *"Trong kiến trúc MVC của Spring Boot có dùng kỹ thuật Injection không?"*  
> **Bạn Kiệt:** Không trả lời được.  
> **Thầy nhấn mạnh:** *"Cái đó là cái chính của Spring Boot. Không có kỹ thuật Injection đó thì MVC của Spring Boot không bao giờ phát triển như ngày nay. Nó là một sự cách tân lớn (Innovation)!"*

### 2. Thầy hỏi tiếp về Implicit và Explicit:
> **Thầy hỏi:** *"Hai tuần trước Thầy có nói về vấn đề Implicit và Explicit. Cái nào là tường minh, cái nào là ngầm định? Spring Boot dùng cái dấu gì để làm việc này?"*  
> **Bạn Nguyễn Văn Tú đáp:** *"Dạ dùng dấu `@` (Annotation)!"*

### 3. Phân tích chuyên sâu (Bản chất kỹ thuật phần mềm Thầy muốn nghe):
1. **Dependency Injection (DI) là gì?**
   - Là kỹ thuật hiện thực hóa nguyên lý **Inversion of Control (IoC - Đảo ngược điều khiển)** và **chữ D trong SOLID (Dependency Inversion Principle)**.
   - Thay vì class tự khởi tạo phụ thuộc bằng từ khóa `new`, Spring IoC Container sẽ tự động tạo Bean và "tiêm" (inject) vào nơi cần dùng.
2. **Implicit (Ngầm định) vs Explicit (Tường minh):**
   - **Explicit Injection (Tường minh):** Lập trình viên phải viết rõ `@Autowired` trên thuộc tính hoặc constructor.
   - **Implicit Constructor Injection (Ngầm định):** Từ Spring 4.3+, nếu class chỉ có **1 constructor duy nhất**, Spring **tự động ngầm hiểu** và inject các dependency mà **không cần gõ `@Autowired`**.
   - **Convention over Configuration (Quy ước hơn cấu hình):** Triết lý ngầm định của Spring Boot giúp tự động cấu hình Tomcat, DataSource, Hibernate mà không cần viết file cấu hình XML tường minh như Spring cũ.

---

## 🎯 CHUYÊN ĐỀ 5: ÁNH XẠ BẢNG JPA & 10 CÔNG CỤ MÔN HỌC

### 1. Thầy hỏi bạn Huỳnh Tấn Phát:
> **Thầy hỏi:** *"Để map với tên bảng trong CSDL thì dùng dấu `@` gì?"*  
> **Bạn Phát đáp:** *"Dạ `@Table`."*  
> **Thầy hỏi:** *"Có thuộc tính gì?"*  
> **Thầy chốt:** *"Có `@Table(name = "...")`."*

### 2. Thầy hỏi về 10 công cụ của môn học:
> **Thầy dặn:** *"Môn học tên là Công cụ phát triển phần mềm hướng dữ liệu. Đi thi hãy cố gắng liệt kê được 10 công cụ. Kể được 5 cái thì chỉ được nửa số điểm!"*

#### 🛠️ Danh sách 10 công cụ chuẩn bài học:
1. **Eclipse IDE** (hoặc STS - Spring Tool Suite): Môi trường phát triển tích hợp viết mã nguồn Java.
2. **MySQL Server:** Hệ quản trị cơ sở dữ liệu quan hệ (RDBMS).
3. **MySQL Workbench:** Công cụ trực quan quản trị CSDL, thiết kế sơ đồ ERD / Reverse Engineer.
4. **Spring Boot:** Framework phát triển ứng dụng Java Backend microservices / REST API.
5. **Spring Initializr:** Công cụ trực tuyến khởi tạo nhanh cấu trúc dự án Spring Boot.
6. **Maven (kèm `pom.xml` / `mvnw`):** Công cụ quản lý thư viện (dependencies) và build dự án tự động.
7. **Postman:** Công cụ gửi HTTP request kiểm thử các RESTful API (GET, POST, PUT, DELETE).
8. **Git & GitHub:** Công cụ quản lý phiên bản mã nguồn (VCS) và lưu trữ trực tuyến.
9. **Thymeleaf:** Template Engine render giao diện HTML Server-Side Rendering (SSR).
10. **Docker** (hoặc **Clever Cloud**): Công cụ ảo hóa container / đám mây lưu trữ và triển khai CSDL MySQL trực tuyến.
*(Lưu ý của Thầy: **Bootstrap** là thư viện CSS/UI, không được tính là công cụ phần mềm!).*
