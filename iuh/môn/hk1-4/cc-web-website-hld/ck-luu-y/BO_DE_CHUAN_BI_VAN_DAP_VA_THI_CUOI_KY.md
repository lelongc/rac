# 🎓 ĐẠI CẨM NANG TOÀN THƯ: CHUẨN BỊ VẤN ĐÁP BTL & ÔN THI TỰ LUẬN CUỐI KỲ
## MÔN: CÔNG NGHỆ WEB VÀ WEBSITE HƯỚNG DỮ LIỆU — TRƯỜNG ĐH CÔNG NGHIỆP TP.HCM (IUH)
**Giảng viên:** Thầy Trương Bá Phúc  
**Dự án BTL:** Website Blog & Nền tảng Viết bài trực tuyến đa người dùng (`blog-website-main`)  
**Thành viên thực hiện:**
1. **24743991 — Hoàng Đại Dương**
2. **24000905 — Nguyễn Trung Dũng**
3. **23630851 — Lê Thành Long**

---

# 📌 MỤC LỤC TỔNG QUAN

- [PHẦN 0: LỊCH THI, LỊCH VẤN ĐÁP & QUY TẮC BẮT BUỘC TỪ THẦY PHÚC](#phần-0-lịch-thi-lịch-vấn-đáp--quy-tắc-bắt-buộc-từ-thầy-phúc)
- [PHẦN I: TRỌN VẸN LÝ THUYẾT CỐT LÕI MÔN HỌC & ĐỀ THI TỰ LUẬN TRÊN GIẤY (22/11/2026)](#phần-i-trọn-vẹn-lý-thuyết-cốt-lõi-môn-học--đề-thi-tự-luận-trên-giấy-22112026)
  - [Chuyên đề 1: Kiến trúc MVC & Vòng đời HTTP Request (Request Lifecycle)](#chuyên-đề-1-kiến-trúc-mvc--vòng-đời-http-request-request-lifecycle)
  - [Chuyên đề 2: Tầng Model trong thực tế (Entity vs DTO vs Service)](#chuyên-đề-2-tầng-model-trong-thực-tế-entity-vs-dto-vs-service)
  - [Chuyên đề 3: Inversion of Control (IoC) & Dependency Injection (DI) Chuyên Sâu](#chuyên-đề-3-inversion-of-control-ioc--dependency-injection-di-chuyên-sâu)
  - [Chuyên đề 4: Cơ Chế Dynamic Proxy Trong Spring Boot & JPA](#chuyên-đề-4-cơ-chế-dynamic-proxy-trong-spring-boot--jpa)
  - [Chuyên đề 5: Toàn Bộ Annotation JPA & Hibernate Ánh Xạ CSDL](#chuyên-đề-5-toàn-bộ-annotation-jpa--hibernate-ánh-xạ-csdl)
  - [Chuyên đề 6: Toàn Bộ Annotation Spring Boot, Spring MVC & Lombok](#chuyên-đề-6-toàn-bộ-annotation-spring-boot-spring-mvc--lombok)
  - [Chuyên đề 7: Quản Lý Giao Dịch @Transactional & Tính Chất ACID](#chuyên-đề-7-quản-lý-giao-dịch-transactional--tính-chất-acid)
  - [Chuyên đề 8: Bảo Mật Stateless JWT & Spring Security 6 vs Session Cookie](#chuyên-đề-8-bảo-mật-stateless-jwt--spring-security-6-vs-session-cookie)
  - [Chuyên đề 9: So Sánh Server-Side Rendering (SSR) vs Client-Side Rendering (CSR)](#chuyên-đề-9-so-sánh-server-side-rendering-ssr-vs-client-side-rendering-csr)
  - [Chuyên đề 10: 10 Công Cụ Cốt Lõi Trong Môn Học Của Thầy Phúc](#chuyên-đề-10-10-công-cụ-cốt-lõi-trong-môn-học-của-thầy-phúc)
- [PHẦN II: THIẾT KẾ CƠ SỞ DỮ LIỆU & QUAN HỆ 12 BẢNG TRONG BTL BLOG WEBSITE](#phần-ii-thiết-kế-cơ-sở-dữ-liệu--quan-hệ-12-bảng-trong-btl-blog-website)
- [PHẦN III: PHÂN TÍCH TỪNG DÒNG CODE & MỌI CHỨC NĂNG TRONG DỰ ÁN BTL](#phần-iii-phân-tích-từng-dòng-code--mọi-chức-năng-trong-dự-án-btl)
  - [Mục 1: Tầng Cấu Hình (Configuration Package)](#mục-1-tầng-cấu-hình-configuration-package)
  - [Mục 2: Tầng Thực Thể (Entity Package - 10 Entities)](#mục-2-tầng-thực-thể-entity-package---10-entities)
  - [Mục 3: Tầng Truy Xuất Dữ Liệu (Repository Package & Phân Tích JPQL)](#mục-3-tầng-truy-xuất-dữ-liệu-repository-package--phân-tích-jpql)
  - [Mục 4: Tầng Nghiệp Vụ (Service Package - Phân Tích Từng Phương Thức)](#mục-4-tầng-nghiệp-vụ-service-package---phân-tích-từng-phương-thức)
  - [Mục 5: Tầng Điều Khiển (Controller Package - Phân Tích Từng Endpoint)](#mục-5-tầng-điều-khiển-controller-package---phân-tích-từng-endpoint)
  - [Mục 6: Xử Lý Ngoại Lệ & Tiện Ích (Exception & SlugUtils)](#mục-6-xử-lý-ngoại-lệ--tiện-ích-exception--slugutils)
  - [Mục 7: Tầng Giao Diện & Frontend JavaScript Giao Tiếp API](#mục-7-tầng-giao-diện--frontend-javascript-giao-tiếp-api)
- [PHẦN IV: BỘ 25 CÂU HỎI VẤN ĐÁP "XOÁY TẬN TỪNG DÒNG CODE" & KỊCH BẢN ĐẠT ĐIỂM 10](#phần-iv-bộ-25-câu-hỏi-vấn-đáp-xoáy-tận-từng-dòng-code--kịch-bản-đạt-điểm-10)

---

# PHẦN 0: LỊCH THI, LỊCH VẤN ĐÁP & QUY TẮC BẮT BUỘC TỪ THẦY PHÚC

### 1. Lịch Vấn Đáp Báo Cáo Bài Tập Lớn (BTL)
- **Nhóm xong sớm**: Có thể đăng ký báo cáo vào tuần sau (25/10/2026).
- **Ngày báo cáo chính thức chung**: **Chủ Nhật, ngày 01/11/2026**.
- **Địa điểm**: **Phòng Giáo viên** (Khoa CNTT - IUH).
- **Khung giờ**: Từ **9h30 sáng đến 17h30 chiều** (Thầy ngồi chấm cả ngày, nhóm đến trình diện, bật máy chạy demo và Thầy sẽ gọi từng thành viên lên hỏi vấn đáp).
- **Quy cách chấm**: Chạy demo trực tiếp trên máy + Thầy lật mã nguồn hỏi bất kỳ dòng nào + Thầy hỏi cấu trúc CSDL và các khái niệm kỹ thuật phần mềm.

### 2. Quy Cách Quyển Báo Cáo In Nộp (In Giấy A4)
- **Độ dài**: Bắt buộc trong khoảng **15 đến 20 trang** (Không ngắn hơn 15 trang, không dài quá 20 trang).
- **Bố cục bắt buộc**:
  1. *Mô tả bài toán / Nghiệp vụ*: Mục tiêu đề tài, phân vai người dùng (Khách, Thành viên, Quản trị viên).
  2. *Sơ đồ CSDL*: Sơ đồ ERD rõ nét, bảng đặc tả 12 bảng (tên bảng, cột, kiểu dữ liệu, khóa chính, khóa ngoại, ràng buộc).
  3. *Kiến trúc hệ thống*: Mô hình phân tầng (MVC / 3-tier: Controller $\rightarrow$ Service $\rightarrow$ Repository), giải thích luồng dữ liệu.
  4. *Giao diện chức năng*: Chụp màn hình các tính năng chính kèm chú thích ngắn.
- ⚠️ **LỜI DẶN ĐẶC BIỆT CỦA THẦY PHÚC**: **TUYỆT ĐỐI KHÔNG DÁN SOURCE CODE VÀO QUYỂN BÁO CÁO!** Báo cáo là tài liệu phân tích thiết kế, không phải chỗ in code. Nhóm nào dán code vào sẽ bị trừ điểm nặng!

### 3. Lịch & Quy Chế Thi Cuối Kỳ
- **Ngày thi**: **Chủ Nhật, ngày 22/11/2026**.
- **Hình thức thi**: **TỰ LUẬN TRÊN GIẤY** (Không dùng máy tính, không mở tài liệu).
- **Cách chấm thi của Thầy**: Thầy chấm cực kỳ chuẩn xác theo từ khóa (keywords) và bản chất kỹ thuật phần mềm. Trả lời đúng trọng tâm, gãy gọn, có sơ đồ minh họa sẽ đạt điểm 9-10. Trả lời lan man, chép sai bản chất hoặc "chém gió" sẽ bị 0 điểm câu đó.

---

# PHẦN I: TRỌN VẸN LÝ THUYẾT CỐT LÕI MÔN HỌC & ĐỀ THI TỰ LUẬN TRÊN GIẤY (22/11/2026)

## Chuyên đề 1: Kiến trúc MVC & Vòng đời HTTP Request (Request Lifecycle)

### 1.1. Bản chất kiến trúc MVC trong Spring Boot
Mô hình MVC (Model - View - Controller) tách biệt ứng dụng thành 3 tầng độc lập:
- **Model**: Đại diện cho trạng thái dữ liệu và quy tắc nghiệp vụ. Trong Spring Boot hiện đại, Model được phân rã thành:
  - *Entity*: Ánh xạ cấu trúc bảng CSDL (Hibernate ORM).
  - *DTO (Data Transfer Object)*: Vận chuyển dữ liệu ra/vào API, lọc các trường nhạy cảm.
  - *Service Layer*: Thực thi logic nghiệp vụ, tính toán, kiểm tra quyền hạn, quản lý `@Transactional`.
  - *Repository Layer*: Thực hiện các câu lệnh SQL/JPQL giao tiếp với Database.
- **View**: Tầng giao diện người dùng. Có 2 dạng:
  - *Server-Side View*: File template (Thymeleaf `.html`, JSP) được máy chủ render sẵn thành mã HTML trước khi gửi về Client.
  - *Client-Side View*: Trình duyệt (Browser / SPA như React, Vue, HTML/JS thuần) tự render giao diện sau khi nhận dữ liệu thô dạng JSON từ REST API.
- **Controller**: Đóng vai trò điều phối (Traffic Router). Tiếp nhận HTTP Request từ Client, gọi Service tương ứng xử lý, và đóng gói dữ liệu vào Model để trả về View (HTML) hoặc Response Body (JSON).

### 1.2. Luồng xử lý chi tiết của một HTTP Request trong Spring Boot (Vòng đời hoàn chỉnh)
Khi một Client gửi một Request (ví dụ `POST /blogs` với header `Authorization: Bearer <token>`), luồng thực thi đi qua 8 bước tuần tự:

```text
[Browser / Postman]
       │
       ▼  (1. HTTP Request: Method + URL + Headers + Body)
[Tomcat Embedded Web Server] (Cổng 8080)
       │
       ▼  (2. Chuỗi lọc Security & CORS)
[SecurityFilterChain] ──> [CorsFilter] ──> [JwtAuthenticationFilter] ──> [CsrfFilter]
       │ (Kiểm tra Token hợp lệ -> Nạp Authentication vào SecurityContextHolder)
       ▼
[DispatcherServlet] (Front Controller trung tâm của Spring MVC)
       │
       ├──> (3. Tra cứu) ──> [HandlerMapping]: Xác định BlogController.createBlog() xử lý URL
       ├──> (4. Gọi hàm) ──> [HandlerAdapter]: Chuyển đổi Request Body JSON thành Java Object (qua HttpMessageConverter/Jackson)
       │
       ▼
[BlogController] (@RestController)
       │ (5. Gọi tầng nghiệp vụ)
       ▼
[BlogService] (@Service - @Transactional)
       │ ├── Lấy user từ SecurityContextHolder
       │ ├── Kiểm tra logic, map DTO -> Entity qua MapStruct
       │ └── Gọi tầng truy xuất dữ liệu
       ▼
[BlogRepository] (@Repository - Spring Data JPA Dynamic Proxy)
       │ (6. Sinh SQL thông qua Hibernate Session/EntityManager)
       ▼
[MySQL Database] (Thực thi INSERT INTO blogs... và lưu trữ bền vững)
       │
       ▼  (7. Entity trả về -> Service đóng gói thành BlogResponse DTO)
[BlogController]
       │
       ▼  (8. Đóng gói kết quả trả về)
   ├── Nếu là @RestController: Jackson chuyển BlogResponse -> JSON String trả về HTTP Body kèm Status Code (200/201).
   └── Nếu là @Controller: ViewResolver tìm file template Thymeleaf (.html), merge dữ liệu và render mã HTML gửi về Browser.
```

---

## Chuyên đề 2: Tầng Model trong thực tế (Entity vs DTO vs Service)

### 2.1. Phân biệt rõ rệt giữa Entity, DTO và Service
1. **Entity (Domain Model)**:
   - Được đánh dấu bằng `@Entity`, ánh xạ trực tiếp 1-1 với bảng trong CSDL.
   - Chứa các ràng buộc CSDL: `@Id`, `@Column`, `@ManyToOne`, `@ManyToMany`.
   - **Mục đích**: Đại diện cho trạng thái lưu trữ bền vững của hệ thống.
2. **DTO (Data Transfer Object)**:
   - Các class Java thuần túy (POJO) chỉ chứa các thuộc tính, Getter, Setter (thường dùng Lombok `@Data`, `@Builder`).
   - Phân loại:
     - `*Request DTO` (ví dụ `BlogCreationRequest`): Hứng dữ liệu từ Client gửi lên, có gắn các Annotation kiểm tra hợp lệ (`@NotBlank`, `@Size`, `@Email`).
     - `*Response DTO` (ví dụ `BlogResponse`, `UserResponse`): Định hình dữ liệu chuẩn gửi về cho Client, chỉ chứa các trường cần hiển thị.
3. **Service (Business Model)**:
   - Được đánh dấu bằng `@Service`, chứa các phương thức nghiệp vụ thực tế của bài toán.
   - Quản lý giao dịch dữ liệu `@Transactional`.

### 2.2. Tại sao CẤM TUYỆT ĐỐI việc dùng trực tiếp Entity làm Model ở tầng API/View?
1. **Chống tấn công Over-posting / Mass Assignment Vulnerability**:
   - Nếu Controller nhận trực tiếp `User entity` từ Client: Hacker có thể cố tình chèn thêm trường JSON `{"roles": ["ADMIN"]}` hoặc `{"isVerified": true}` vào request đăng ký. Spring sẽ tự động nạp trường đó vào Entity và ghi đè quyền Admin trong DB!
   - Khi dùng `UserCreatetionRequest` DTO, DTO chỉ có 2 trường `username` và `password`. Hacker có gửi thêm `roles` thì hệ thống cũng tự động bỏ qua.
2. **Ngăn chặn lỗi đệ quy vô tận (Infinite Recursion - Circular Dependency)**:
   - Trong quan hệ 2 chiều (`User` có danh sách `Blog`, mỗi `Blog` lại chứa đối tượng `User author`).
   - Khi Jackson chuyển Entity sang JSON: `User` gọi `Blog`, `Blog` gọi lại `User`, lặp vô hạn $\rightarrow$ Tràn bộ nhớ ngăn xếp `StackOverflowError` gây sập server. DTO giúp cắt đứt vòng lặp này hoàn toàn.
3. **Che giấu thông tin nhạy cảm (Data Privacy)**:
   - Entity `User` chứa trường `password` (chuỗi băm BCrypt). Nếu trả Entity trực tiếp về cho View, chuỗi băm mật khẩu sẽ bị lộ trên mạng. `UserResponse` DTO hoàn toàn không có thuộc tính `password`.
4. **Tối ưu hóa hiệu năng (Decoupling & Lazy Loading)**:
   - View chỉ cần hiển thị `title` và `authorName`. DTO chỉ load đúng 2 trường đó, tránh kích hoạt tải toàn bộ dữ liệu quan hệ nặng (`FetchType.LAZY`) gây ra lỗi `LazyInitializationException` ngoài transaction.

---

## Chuyên đề 3: Inversion of Control (IoC) & Dependency Injection (DI) Chuyên Sâu

### 3.1. Bản chất IoC và DI
- **Inversion of Control (IoC - Đảo ngược điều khiển)**: Là một triết lý thiết kế phần mềm. Thay vì class tự khởi tạo đối tượng phụ thuộc bằng từ khóa `new` (kiểm soát xuôi), việc khởi tạo và quản lý vòng đời của đối tượng được trao lại cho Framework (Spring IoC Container kiểm soát ngược lại).
- **Dependency Injection (DI - Tiêm phụ thuộc)**: Là một kỹ thuật hiện thực hóa IoC. Các Dependency (các class phụ thuộc) được Spring Container tự động "bơm" (inject) vào class cần dùng thông qua Constructor, Setter hoặc Field tại thời điểm Runtime.
- **Nguyên lý SOLID tương ứng**: **DIP (Dependency Inversion Principle - Nguyên lý đảo ngược phụ thuộc)**: Các module cấp cao không nên phụ thuộc trực tiếp vào module cấp thấp; cả hai nên phụ thuộc vào Abstraction (Interface).

### 3.2. So sánh toàn diện: Implicit Injection (Ngầm định) vs Explicit Injection (Tường minh)

| Tiêu chí | Implicit Injection (Tiêm Ngầm Định) | Explicit Injection (Tiêm Tường Minh) |
| :--- | :--- | :--- |
| **Định nghĩa** | Spring Framework tự động phát hiện và tiêm Bean vào điểm cần dùng mà **không cần gắn annotation `@Autowired`**. | Lập trình viên phải khai báo rõ ràng bằng annotation hoặc code cấu hình để chỉ định Bean cần tiêm. |
| **Cơ chế hoạt động** | **Từ Spring 4.3 trở đi**: Nếu một Class chỉ có **duy nhất một Constructor**, Spring IoC Container mặc định hiểu constructor đó là điểm inject và tự động tìm nạp tất cả các Bean tham số truyền vào mà không cần viết `@Autowired`. Kết hợp hoàn hảo với `@RequiredArgsConstructor` của Lombok. | Dùng `@Autowired` trực tiếp trên thuộc tính (Field Injection), trên phương thức Setter, hoặc dùng `@Qualifier("tên_bean")` khi có nhiều bean cùng loại, hoặc viết phương thức gắn `@Bean` trong class `@Configuration`. |
| **Minh họa code** | ```java<br>@Service<br>@RequiredArgsConstructor<br>public class BlogService {<br>    // Khai báo final -> Lombok sinh constructor<br>    // Spring tự ngầm định inject<br>    private final BlogRepository blogRepo;<br>    private final UserMapper userMapper;<br>}<br>``` | ```java<br>@Service<br>public class BlogService {<br>    @Autowired // Chỉ định tường minh<br>    @Qualifier("mysqlBlogRepo")<br>    private BlogRepository blogRepo;<br>}<br>``` |
| **Đánh giá & Khuyến nghị** | **Chuẩn mực tốt nhất hiện nay (Best Practice)**: Cho phép khai báo biến `final` (bảo đảm tính bất biến Immutability, an toàn đa luồng Thread-safe). Giúp viết Unit Test cực kỳ dễ dàng (chỉ cần gọi constructor và truyền Mock object vào mà không cần khởi động Spring Container nặng nề). | **Field Injection bị coi là Anti-Pattern**: Vi phạm tính đóng gói (Encapsulation), không thể khai báo `final`, dễ gây lỗi `NullPointerException` nếu khởi tạo ngoài Container, khó Unit Test. |

---

## Chuyên đề 4: Cơ Chế Dynamic Proxy Trong Spring Boot & JPA

### 4.1. Câu hỏi kinh điển: "Vì sao `BlogRepository` chỉ là một Interface không có class `implements` mà vẫn chạy được câu lệnh CSDL?"
- **Bản chất**: Nhờ vào **Cơ chế Dynamic Proxy (Ủy quyền động)** của Java và Spring Data JPA.
- **Quy trình hoạt động tại Runtime**:
  1. Khi ứng dụng khởi động, Spring Boot quét các interface kế thừa `JpaRepository<T, ID>`.
  2. Spring sử dụng **JDK Dynamic Proxy** (nếu là Interface) hoặc thư viện **CGLIB** (nếu là Class) để tự động sinh ra một bytecode class ẩn trong bộ nhớ RAM, class này hiện thực hóa interface đó (mặc định là `SimpleJpaRepository`).
  3. Lớp Proxy này chặn toàn bộ các lời gọi hàm (Method Interception). Khi bạn gọi `blogRepository.findByTitle("Java")`, Proxy phân tích tên hàm, chuyển thành câu lệnh SQL `SELECT * FROM blogs WHERE title = ?`, nạp tham số và chuyển xuống `EntityManager` của Hibernate để thực thi truy vấn tới MySQL.

### 4.2. Cơ chế Dynamic Proxy trong `@Transactional`
- Khi một phương thức Service được gắn `@Transactional`, Spring AOP sẽ bọc phương thức đó bằng một Proxy:
  ```text
  Client Gọi Method -> [Proxy bắt chặn] -> Mở Database Connection
                                       -> Set AutoCommit = false (Bắt đầu Transaction)
                                       -> Thực thi logic trong method
                                       -> Nếu thành công: Gọi Connection.commit()
                                       -> Nếu có RuntimeException: Gọi Connection.rollback()
                                       -> Đóng Connection
  ```

---

## Chuyên đề 5: Toàn Bộ Annotation JPA & Hibernate Ánh Xạ CSDL

| Annotation | Vị trí đặt | Ý nghĩa học thuật & Bản chất kỹ thuật | Ứng dụng trong dự án BTL Blog |
| :--- | :--- | :--- | :--- |
| **`@Entity`** | Trên Class | Khai báo class Java là một thực thể ORM được quản lý bởi Hibernate Persistence Context. | `@Entity public class User` |
| **`@Table`** | Trên Class | Chỉ định tên bảng thật trong MySQL, các chỉ mục (`indexes`) và ràng buộc duy nhất (`uniqueConstraints`). | `@Table(name="blogs")` |
| **`@Id`** | Thuộc tính | Định danh Khóa chính (Primary Key) của bảng. | `@Id UUID id;` |
| **`@GeneratedValue`** | Thuộc tính | Chiến lược sinh khóa chính: `IDENTITY` (Auto-increment), `UUID` (Chuỗi ngẫu nhiên 128-bit). | `@GeneratedValue(strategy = GenerationType.UUID)` |
| **`@Column`** | Thuộc tính | Cấu hình chi tiết cột trong DB: `name`, `nullable`, `unique`, `length`, `columnDefinition = "TEXT" / "LONGTEXT"`. | `@Column(columnDefinition = "LONGTEXT") String content;` |
| **`@ManyToOne`** | Thuộc tính | Mối quan hệ Nhiều - Một (N - 1). Bên sở hữu khóa ngoại. Luôn dùng kèm `fetch = FetchType.LAZY` để tối ưu truy vấn. | Nhiều bài viết thuộc về 1 tác giả (`User author`). |
| **`@OneToMany`** | Thuộc tính | Mối quan hệ Một - Nhiều (1 - N). Phải khai báo thuộc tính `mappedBy` trỏ về tên biến bên `@ManyToOne` để không bị sinh bảng phụ không mong muốn. | 1 tác giả có danh sách nhiều bài viết (`List<Blog> blogs`). |
| **`@ManyToMany`** | Thuộc tính | Mối quan hệ Nhiều - Nhiều (N - N). Bắt buộc phải phối hợp với `@JoinTable` để tạo bảng trung gian nối 2 khóa ngoại. | Quan hệ giữa `Blog` và `Tag` qua bảng phụ `blog_tags`. |
| **`@JoinColumn`** | Thuộc tính | Chỉ định rõ tên cột khóa ngoại (Foreign Key Column) sẽ được tạo ra trong bảng vật lý. | `@JoinColumn(name = "author_id", nullable = false)` |
| **`@JoinTable`** | Thuộc tính | Định nghĩa cấu hình bảng trung gian cho quan hệ N-N: tên bảng (`name`), cột khóa ngoại của mình (`joinColumns`), cột khóa ngoại của đối tác (`inverseJoinColumns`). | `@JoinTable(name="blog_tags", joinColumns=@JoinColumn(name="blog_id"), inverseJoinColumns=@JoinColumn(name="tag_id"))` |
| **`@ElementCollection`** | Thuộc tính | Dùng khi một thực thể chứa một tập hợp kiểu dữ liệu cơ bản (String, Integer) hoặc Enum mà không cần tạo riêng một Entity class. | Tập hợp quyền `Set<String> roles` của User. |
| **`@CollectionTable`** | Thuộc tính | Cấu hình tên bảng lưu trữ cho `@ElementCollection`. | `@CollectionTable(name="user_roles", joinColumns=@JoinColumn(name="user_id"))` |
| **`@Transient`** | Thuộc tính | Khai báo trường dữ liệu chỉ dùng trong bộ nhớ Java để tính toán tạm thời, Hibernate sẽ bỏ qua và không tạo cột trong CSDL. | Dùng cho các cờ trạng thái tạm thời. |
| **`@PrePersist`** | Phương thức | Callback được kích hoạt tự động trước khi bản ghi được `INSERT` lần đầu vào CSDL. Thường dùng set thời gian tạo. | Gán tự động `createdAt = LocalDateTime.now()`. |
| **`@PreUpdate`** | Phương thức | Callback được kích hoạt tự động trước khi bản ghi được `UPDATE` vào CSDL. Thường dùng cập nhật thời gian sửa đổi. | Gán tự động `updatedAt = LocalDateTime.now()`. |

---

## Chuyên đề 6: Toàn Bộ Annotation Spring Boot, Spring MVC & Lombok

### 6.1. Nhóm Spring Stereotypes & Architecture
- `@SpringBootApplication`: Annotation tổng hợp gồm `@Configuration`, `@EnableAutoConfiguration` và `@ComponentScan`.
- `@RestController`: Bằng `@Controller` + `@ResponseBody`. Toàn bộ dữ liệu trả về từ các method sẽ được Jackson chuyển thành chuỗi JSON thay vì render file view HTML.
- `@Controller`: Trả về tên file View Template (Thymeleaf `.html`) để ViewResolver render mã HTML.
- `@Service`: Đánh dấu tầng nghiệp vụ (Business Logic Layer).
- `@Repository`: Đánh dấu tầng truy xuất dữ liệu (DAO Layer), hỗ trợ bắt lỗi và chuyển đổi các lỗi SQL thành Spring DataAccessException.
- `@Configuration` & `@Bean`: Khai báo class chứa cấu hình tạo Bean thủ công đưa vào Spring ApplicationContext.

### 6.2. Nhóm Định Tuyến HTTP & Tham Số (Request Mapping)
- `@RequestMapping("/url")`: Định nghĩa tiền tố đường dẫn chung cho toàn bộ Controller.
- `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping`: Ánh xạ các phương thức HTTP tương ứng.
- `@PathVariable`: Lấy giá trị biến trực tiếp từ URL đường dẫn (ví dụ: `/blogs/{id}` $\rightarrow$ `@PathVariable UUID id`).
- `@RequestParam`: Lấy tham số truy vấn sau dấu `?` trong URL (ví dụ: `/blogs/search?keyword=java` $\rightarrow$ `@RequestParam String keyword`).
- `@RequestBody`: Bắt Spring đọc toàn bộ phần thân (Body) của HTTP Request và chuyển từ chuỗi JSON sang đối tượng Java.
- `@Valid`: Kích hoạt cơ chế kiểm tra tính hợp lệ dữ liệu (Jakarta Validation) dựa trên các annotation gắn trong DTO (như `@NotBlank`, `@Size`).

### 6.3. Nhóm Lombok Tối Ưu Mã Nguồn
- `@Getter` / `@Setter`: Tự động sinh getter/setter tại thời điểm biên dịch, giảm boilerplate code.
- `@NoArgsConstructor`: Tự động tạo Constructor không tham số (Bắt buộc phải có để Hibernate khởi tạo Entity qua Reflection).
- `@AllArgsConstructor`: Tự động tạo Constructor chứa đầy đủ mọi thuộc tính.
- `@Builder`: Cung cấp Builder Pattern giúp khởi tạo đối tượng sạch sẽ, linh hoạt: `Blog.builder().title("...").build()`.
- `@RequiredArgsConstructor`: Tự động tạo Constructor chứa tất cả các thuộc tính có từ khóa `final` $\rightarrow$ **Cơ chế cốt lõi để thực hiện Implicit Dependency Injection**.
- `@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)`: Tự động gắn thuộc tính `private final` cho toàn bộ các biến trong class.
- `@Slf4j`: Tự động tiêm đối tượng Logger `log` của thư viện Logback/SLF4J để ghi nhật ký hệ thống.

---

## Chuyên đề 7: Quản Lý Giao Dịch @Transactional & Tính Chất ACID

### 7.1. Bốn tính chất ACID của giao dịch
1. **Atomicity (Tính nguyên tử)**: "Tất cả hoặc không gì cả". Mọi câu lệnh SQL trong method phải thành công trọn vẹn. Nếu 1 câu lỗi, toàn bộ các câu trước đó bị rollback hủy bỏ.
2. **Consistency (Tính nhất quán)**: Dữ liệu luôn chuyển từ trạng thái hợp lệ này sang trạng thái hợp lệ khác, không vi phạm ràng buộc toàn vẹn CSDL.
3. **Isolation (Tính cô lập)**: Các giao dịch diễn ra đồng thời không được can thiệp hoặc nhìn thấy dữ liệu dở dang của nhau.
4. **Durability (Tính bền vững)**: Một khi transaction đã commit thành công, dữ liệu được ghi vĩnh viễn vào ổ đĩa, kể cả server mất điện ngay sau đó dữ liệu vẫn an toàn.

### 7.2. Vì sao `@Transactional` nên đặt ở tầng Service?
- Tầng Service là nơi phối hợp nhiều thao tác ghi dữ liệu từ nhiều Repository khác nhau trong cùng một nghiệp vụ (ví dụ: lưu bài viết, cập nhật tag, gửi thông báo). Đặt `@Transactional` tại Service bảo đảm nếu lưu bài viết được nhưng tạo tag lỗi thì bài viết cũng được rollback, không sinh ra dữ liệu rác mồ côi trong DB.

---

## Chuyên đề 8: Bảo Mật Stateless JWT & Spring Security 6 vs Session Cookie

| Tiêu chí | Stateless JWT (Dự án BTL đang dùng) | Stateful Session Cookie (Mô hình truyền thống) |
| :--- | :--- | :--- |
| **Cơ chế lưu trữ** | **Phi trạng thái (Stateless)**: Server hoàn toàn không lưu phiên đăng nhập trên RAM. Chuỗi Token được gửi về cho Client lưu tại `localStorage` của trình duyệt. | **Có trạng thái (Stateful)**: Server tạo đối tượng `HttpSession` lưu trong bộ nhớ RAM của máy chủ, trả về cho Client mã `JSESSIONID` qua Cookie. |
| **Cơ chế xác thực** | Mỗi request Client tự gắn Header `Authorization: Bearer <token>`. Server chỉ cần dùng khóa bí mật `SIGNER_KEY` để giải mã kiểm tra chữ ký số (Signature). | Client gửi Cookie kèm theo. Server phải tìm kiếm session ID trong RAM để đối chiếu thông tin user. |
| **Khả năng mở rộng (Scalability)** | **Cực kỳ xuất sắc**: Phù hợp triển khai hệ thống Microservices hoặc cụm nhiều server (Load Balancer) mà không cần đồng bộ bộ nhớ. | **Kém**: Khi nhân rộng nhiều server, phải cấu hình chia sẻ session (Redis Session Clustering), nếu không user đăng nhập server A sẽ bị mất session khi bị điều hướng sang server B. |
| **Chống tấn công CSRF** | **Miễn nhiễm với CSRF**: Vì Token không được trình duyệt tự động đính kèm như Cookie, hacker trên website độc hại không thể tự ý kích hoạt request giả mạo. | Dễ bị tấn công CSRF nếu không có CSRF Token bảo vệ. |

---

## Chuyên đề 9: So Sánh Server-Side Rendering (SSR) vs Client-Side Rendering (CSR)

- **SSR (Server-Side Rendering - với Thymeleaf/JSP)**:
  - Máy chủ nhận request $\rightarrow$ Lấy dữ liệu $\rightarrow$ Trộn dữ liệu vào file HTML template $\rightarrow$ Trả về mã HTML hoàn chỉnh cho trình duyệt hiển thị.
  - *Ưu điểm*: Tốt cho SEO (Google bot đọc được nội dung ngay), tải trang đầu tiên nhanh.
  - *Nhược điểm*: Mỗi lần bấm chuyển trang hoặc lọc dữ liệu thì trang web phải reload lại từ đầu, tiêu tốn băng thông máy chủ.
- **CSR (Client-Side Rendering - với REST API + JS Fetch)**:
  - Máy chủ chỉ trả về khung HTML tĩnh và file JavaScript. Trình duyệt tải JS về, sau đó JS tự động gửi `fetch()` lên các API JSON để nhận dữ liệu thô và tự vẽ ra giao diện (DOM Manipulation).
  - *Ưu điểm*: Trải nghiệm người dùng mượt mà (Single Page App - không bao giờ bị chớp màn hình trắng khi tải lại trang), giảm tải tối đa cho máy chủ backend.
  - *Nhược điểm*: SEO ban đầu khó hơn nếu không có tiền xử lý.
- **Kiến trúc kết hợp của BTL Nhóm**: Áp dụng mô hình **Hybrid thông minh**: Dùng `ViewController` của Thymeleaf phân phối layout HTML ban đầu, sau đó toàn bộ tương tác người dùng (đăng nhập, like, bình luận, viết bài, tìm kiếm) đều được điều khiển bằng **JavaScript Fetch API bất đồng bộ** giao tiếp với các **RestController JSON**.

---

## Chuyên đề 10: 10 Công Cụ Cốt Lõi Trong Môn Học Của Thầy Phúc

1. **Java 21 (LTS)**: Ngôn ngữ lập trình chính, sử dụng các tính năng mới nhất: Pattern Matching, Record, Virtual Threads.
2. **Spring Boot 3.5.11**: Framework phát triển ứng dụng web doanh nghiệp theo chuẩn Production-ready.
3. **Apache Maven**: Công cụ quản lý vòng đời dự án (Build tool) và tự động kéo các thư viện phụ thuộc từ Maven Central Repository thông qua file `pom.xml`.
4. **MySQL Server Local (Cổng 3306)** & **MySQL Workbench**: Hệ quản trị cơ sở dữ liệu quan hệ (RDBMS) bền vững công nghiệp và công cụ trực quan hóa sơ đồ bảng.
5. **Hibernate ORM 6.6 & Spring Data JPA**: Cầu nối ánh xạ giữa đối tượng Java và bảng quan hệ CSDL, tự động sinh mã SQL tối ưu.
6. **Thymeleaf & RESTful API**: Công nghệ giao diện kết hợp giữa Template Engine phía máy chủ và chuẩn giao tiếp truyền tải dữ liệu JSON.
7. **Postman**: Công cụ gửi HTTP Request giả lập chuyên nghiệp dùng để kiểm thử độc lập (Test API) toàn bộ các đầu API Backend trước khi ghép giao diện.
8. **Git & GitHub**: Hệ thống quản lý phiên bản phân tán (VCS) giúp các thành viên nhóm làm việc cộng tác, phân nhánh, merge code và theo dõi lịch sử commit.
9. **Project Lombok**: Thư viện plugin tiền xử lý mã nguồn (Annotation Processor) loại bỏ hàng trăm dòng code thừa (Getter, Setter, Constructor, Builder).
10. **VS Code / IntelliJ IDEA**: Môi trường phát triển tích hợp (IDE) chuyên nghiệp, hỗ trợ gỡ lỗi (Debugging), cấu hình máy chủ và quản lý project.

---

# PHẦN II: THIẾT KẾ CƠ SỞ DỮ LIỆU & QUAN HỆ 12 BẢNG TRONG BTL BLOG WEBSITE

Hệ cơ sở dữ liệu `blog_website_db` gồm **12 bảng quan hệ** đạt chuẩn hóa **3NF (Dạng chuẩn 3)**:

```text
┌──────────────┐          ┌──────────────┐          ┌──────────────┐
│  categories  │          │    users     │          │    roles     │
│  (id, name)  │          │ (id, pass...)│          │ (role_name)  │
└──────┬───────┘          └──────┬───────┘          └──────┬───────┘
       │ 1                       │ 1                       │ N
       │                         │                         │
       │ N                       │ N                       │ M
┌──────┴───────┐          ┌──────┴───────┐          ┌──────┴───────┐
│    blogs     ├──────────┤  user_roles  │          │  user_roles  │
│(id,title...) │          │(user_id,role)│          │(user_id,role)│
└──────┬───────┘          └──────────────┘          └──────────────┘
       │ 1                │ 1                │ 1            │ 1
       ├──────────────────┼──────────────────┼──────────────┤
       │ N                │ N                │ N            │ N
┌──────┴───────┐   ┌──────┴───────┐   ┌──────┴───────┐┌─────┴──────────┐
│  blog_tags   │   │  blog_likes  │   │  bookmarks   ││  user_follows  │
│(blog_id,tag) │   │(blog_id,user)│   │(blog_id,user)││(follower,follow│
└──────┬───────┘   └──────────────┘   └──────────────┘└────────────────┘
       │ N                │ 1                │ 1
┌──────┴───────┐   ┌──────┴───────┐   ┌──────┴───────┐
│     tags     │   │   comments   │   │notifications │
│  (id, name)  │   │(id, blog...) │   │(id, user_id) │
└──────────────┘   └──────────────┘   └──────────────┘
```

### Chi tiết 12 Bảng CSDL:
1. **`users`**: Lưu thông tin cá nhân tài khoản (`id` UUID, `username`, `password` BCrypt, `email`, `bio`, `avatar_url`, `created_at`).
2. **`roles` / `user_roles`**: Bảng phụ giải quyết quan hệ N-N giữa User và Quyền hạn (`user_id`, `role`: `USER`, `ADMIN`).
3. **`categories`**: Lưu danh mục bài viết (`id` UUID, `name` UNIQUE).
4. **`tags`**: Lưu các thẻ phân loại nội dung (`id` UUID, `name` UNIQUE).
5. **`blogs`**: Bảng trung tâm lưu bài viết (`id` UUID, `title`, `banner`, `description`, `content`, `draft`, `draft_content`, `draft_banner`, `author_id`, `category_id`, `created_at`, `updated_at`, `published_at`).
6. **`blog_tags`**: Bảng trung gian giải quyết quan hệ N-N giữa `blogs` và `tags` (`blog_id`, `tag_id`). Có Unique Constraint chống trùng lặp.
7. **`comments`**: Lưu bình luận phân cấp (`id` UUID, `blog_id`, `user_id`, `parent_id` trỏ ngược lại chính `comments` để reply, `content`, `created_at`).
8. **`blog_likes`**: Lưu tương tác thả tim (`id` UUID, `blog_id`, `user_id`, `created_at`). Khóa phức hợp Unique `(user_id, blog_id)` chống like 2 lần.
9. **`bookmarks`**: Lưu bài viết yêu thích (`id` UUID, `blog_id`, `user_id`, `created_at`). Khóa phức hợp Unique `(user_id, blog_id)`.
10. **`blog_views`**: Lưu lịch sử lượt đọc bài viết (`id` UUID, `blog_id`, `user_id`, `ip_address`, `viewed_at`) hỗ trợ đếm view cho cả khách vãng lai.
11. **`user_follows`**: Lưu quan hệ theo dõi tác giả (`id` UUID, `follower_id`, `following_id`, `created_at`). Khóa phức hợp Unique `(follower_id, following_id)`.
12. **`notifications`**: Lưu thông báo hoạt động (`id` UUID, `user_id`, `message`, `target_url`, `is_read`, `type`, `created_at`).

---

# PHẦN III: PHÂN TÍCH TỪNG DÒNG CODE & MỌI CHỨC NĂNG TRONG DỰ ÁN BTL

*(Phần này đi qua từng file mã nguồn, phân tích mục đích, vị trí và công năng từng hàm để bạn trả lời mọi câu hỏi của Thầy)*

## Mục 1: Tầng Cấu Hình (Configuration Package)

### 1.1. `SecurityConfig.java` — Trái tim bảo mật hệ thống
- **Vị trí**: `com.group.blog.config.SecurityConfig.java`
- **Công dụng**: Cấu hình Spring Security 6 theo kiến trúc Stateless JWT.
- **Phân tích từng thành phần**:
  - `PUBLIC_POST_ENDPOINTS`: Các đường dẫn `POST` không cần đăng nhập (`/users` để đăng ký, `/auth/login` để lấy token, `/auth/introspect` kiểm tra token).
  - `PUBLIC_GET_ENDPOINTS`: Toàn bộ các trang HTML giao diện, các file tĩnh CSS/JS, và API xem bài viết công khai (`/categories`, `/tags`, `/blogs/**`).
  - `ADMIN_ENDPOINTS = {"/api/admin/**"}`: Các API dữ liệu thống kê quản trị chỉ cho phép tài khoản có quyền `ROLE_ADMIN` gọi.
  - `filterChain(HttpSecurity httpSecurity)`:
    - `.cors()`: Bật hỗ trợ truy cập đa nguồn từ trình duyệt.
    - `.headers(headers -> headers.frameOptions(frame -> frame.disable()))`: Cho phép nhúng iframe nếu cần.
    - `.authorizeHttpRequests(...)`: Định tuyến phân quyền chi tiết cho từng phương thức HTTP.
    - `.oauth2ResourceServer(...)`: Tự động giải mã Bearer Token trong Header HTTP thông qua `jwtDecoder()`.
    - `.csrf(AbstractHttpConfigurer::disable)`: **Tắt CSRF vì hệ thống dùng Token JWT, không dùng Cookie nên miễn nhiễm với CSRF**.
    - `.sessionManagement(session -> session.sessionCreationPolicy(SessionCreationPolicy.STATELESS))`: **Yêu cầu Spring không lưu Session trên RAM**.
  - `jwtAuthenticationConverter()`: Trích xuất trường `scope` trong Token (ví dụ `"ADMIN"`) và tự động thêm tiền tố `"ROLE_"` thành `"ROLE_ADMIN"` để phương thức `.hasRole("ADMIN")` của Spring nhận diện được.
  - `jwtDecoder()`: Sử dụng thuật toán băm cực mạnh `HmacSHA512` kết hợp `SIGNER_KEY` để giải mã và kiểm tra chữ ký số của token.
  - `passwordEncoder()`: Khởi tạo Bean `BCryptPasswordEncoder(10)` phục vụ băm mật khẩu một chiều với 10 vòng lặp muối (salt rounds).

### 1.2. `ApplicationInitConfig.java` — Tự động khởi tạo dữ liệu mẫu khi khởi động
- **Vị trí**: `com.group.blog.config.ApplicationInitConfig.java`
- **Công dụng**: Sử dụng `ApplicationRunner` để kiểm tra xem tài khoản `admin` đã có trong MySQL chưa. Nếu chưa có (chạy lần đầu):
  - Tự động tạo 1 tài khoản quản trị `admin` (`password: 123456`, quyền `ADMIN` và `USER`).
  - Tự động tạo 3 tài khoản cho 3 thành viên nhóm: `duonghd` (24743991), `dungnt` (24000905), `longlt` (23630851).
  - Tự động tạo 4 Danh mục mẫu (`Technology`, `Programming`, `Web Design`, `Life & Tips`).
  - Tự động tạo 5 Thẻ Tag mẫu (`Java`, `SpringBoot`, `Bootstrap`, `Thymeleaf`, `AI`).
  - Tự động tạo 3 Bài viết Blog mẫu kèm hình ảnh banner, tác giả, danh mục và thẻ tag.

### 1.3. `CloudinaryConfig.java` & `CloudinaryService.java` — Quản lý tải ảnh đám mây
- **Vị trí**: `com.group.blog.config.CloudinaryConfig.java` và `com.group.blog.service.CloudinaryService.java`
- **Công dụng**:
  - Dùng Annotation `@Value("${cloudinary.cloud-name}")` để nạp thông số kết nối từ file `application-secret.yml`.
  - Khởi tạo Bean `Cloudinary` đưa vào Spring Context.
  - Phương thức `uploadImage(MultipartFile file)` nhận mảng byte nhị phân của file ảnh tải lên từ form, gửi lên dịch vụ Cloudinary và trả về đường link URL công khai (`https://res.cloudinary.com/...`).

---

## Mục 2: Tầng Thực Thể (Entity Package - 10 Entities)

### 2.1. `User.java` (Bảng `users`)
- Khóa chính `@Id @GeneratedValue(strategy = GenerationType.UUID) UUID id`: Khóa chính định dạng UUID ngẫu nhiên 128-bit chống dò quét ID.
- `@Column(nullable = false, unique = true, length = 100) String username`: Tên đăng nhập không được trùng, không được rỗng.
- `@Column(nullable = false, length = 255) String password`: Lưu chuỗi băm BCrypt dài 60 ký tự.
- `@ElementCollection(fetch = FetchType.EAGER) @CollectionTable(name = "user_roles", joinColumns = @JoinColumn(name = "user_id")) Set<String> roles`: Tạo bảng phụ `user_roles` lưu danh sách vai trò (`ROLE_USER`, `ROLE_ADMIN`). Tải EAGER để kiểm tra quyền hạn ngay lập tức khi đăng nhập.
- `@OneToMany(mappedBy = "author", cascade = CascadeType.ALL) List<Blog> blogs`: Một user có thể viết nhiều bài.
- `@PrePersist void prePersist()`: Tự động điền ngày tạo `createdAt = LocalDateTime.now()` trước khi lưu xuống DB.

### 2.2. `Blog.java` (Bảng `blogs`)
- `String title`, `String banner`, `String description`: Tiêu đề, ảnh bìa và mô tả ngắn bài viết.
- `@Column(columnDefinition = "LONGTEXT") String content`: Nội dung bài viết chính thức đã xuất bản, lưu trữ bằng kiểu `LONGTEXT` trong MySQL (chứa được đến 4GB dữ liệu văn bản/HTML).
- `boolean draft`: Cờ đánh dấu trạng thái (true: bản nháp, false: bài đã xuất bản công khai).
- `@Column(columnDefinition = "LONGTEXT") String draftContent` & `draftBanner`: **Cơ chế lưu nháp bài viết đang sửa**. Cho phép tác giả sửa bài đã public mà người đọc bên ngoài vẫn đọc bản cũ; khi nào bấm Publish thì nội dung từ `draftContent` mới đổ sang `content`.
- `@ManyToOne(fetch = FetchType.LAZY) @JoinColumn(name = "author_id") User author`: Khóa ngoại trỏ về tác giả bài viết.
- `@ManyToOne(fetch = FetchType.LAZY) @JoinColumn(name = "category_id") Category category`: Khóa ngoại trỏ về danh mục bài viết.
- `@ManyToMany @JoinTable(name = "blog_tags", joinColumns = @JoinColumn(name = "blog_id"), inverseJoinColumns = @JoinColumn(name = "tag_id")) Set<Tag> tags`: Quan hệ N-N tạo bảng trung gian `blog_tags`.
- `@PreUpdate void preUpdate()`: Tự động cập nhật `updatedAt = LocalDateTime.now()` mỗi khi có chỉnh sửa.

### 2.3. `Comment.java` (Bảng `comments`)
- `@Table(name="comments", indexes = {@Index(name="idx_comment_blog", columnList="blog_id"), @Index(name="idx_comment_parent", columnList="parent_id")})`: Đánh chỉ mục Index trên cột `blog_id` và `parent_id` để tăng tốc độ truy vấn bình luận của bài viết.
- `@ManyToOne(fetch = FetchType.LAZY) @JoinColumn(name = "parent_id") Comment parent`: **Quan hệ tự tham chiếu (Self-referencing)**. Trỏ về bình luận cha nếu đây là một phản hồi (reply).
- `@OneToMany(mappedBy = "parent", cascade = CascadeType.ALL, orphanRemoval = true) @OrderBy("createdAt ASC") List<Comment> replies`: Danh sách các reply con của bình luận này, tự động sắp xếp theo thứ tự thời gian tăng dần.

### 2.4. `BlogLike.java` & `Bookmark.java`
- Khóa phức hợp duy nhất `@Table(name="blog_likes", uniqueConstraints = {@UniqueConstraint(columnNames = {"user_id","blog_id"})})`: Ngăn chặn tuyệt đối việc một người dùng bấm like hoặc bookmark một bài viết 2 lần ở tầng CSDL.
- `@OnDelete(action = OnDeleteAction.CASCADE)`: Khi bài viết gốc bị xóa, toàn bộ lượt like và bookmark liên quan sẽ tự động bị xóa theo (xóa tầng CSDL, không gây lỗi khóa ngoại).

### 2.5. `UserFollow.java` (Bảng `user_follows`)
- `@ManyToOne User follower`: Người đi theo dõi.
- `@ManyToOne User following`: Tác giả được theo dõi.
- Ràng buộc `@UniqueConstraint(columnNames = {"follower_id", "following_id"})`: Chặn theo dõi trùng lặp.

### 2.6. `Notification.java` (Bảng `notifications`)
- Lưu các thông báo người dùng (`LIKE`, `COMMENT`, `REPLY`, `FOLLOW`).
- `String targetUrl`: Đường dẫn trang web kèm tham số (ví dụ: `post.html?id=java-slug&openComments=true`) để khi người dùng click vào thông báo sẽ tự động nhảy đến đúng bài viết và tự mở khung bình luận.

---

## Mục 3: Tầng Truy Xuất Dữ Liệu (Repository Package & Phân Tích JPQL)

### 3.1. Phân tích truy vấn JPQL phức tạp trong `BlogRepository.java`
```java
@Query("""
   SELECT b, COUNT(DISTINCT v.id), COUNT(DISTINCT l.id), COUNT(DISTINCT c.id)
   FROM Blog b
   LEFT JOIN BlogLike l ON l.blog = b
   LEFT JOIN BlogView v ON v.blog = b
   LEFT JOIN Comment c ON c.blog = b
   WHERE b.draft = false
   GROUP BY b
   ORDER BY b.publishedAt DESC
""")
List<Object[]> findAllBlogsWithCounts();
```
- **Ý nghĩa câu hỏi vấn đáp**: *"Tại sao phải dùng `LEFT JOIN` và `COUNT(DISTINCT ...)` mà không dùng `COUNT(...)` thông thường?"*
  - **Trả lời**:
    1. Dùng `LEFT JOIN` vì nếu bài viết chưa có lượt like, view hoặc comment nào thì bài viết đó vẫn được lấy ra (nếu dùng `INNER JOIN` thì bài viết mới tạo chưa có like/comment sẽ bị biến mất khỏi trang chủ!).
    2. Phải dùng `COUNT(DISTINCT v.id)` vì khi JOIN 3 bảng quan hệ 1-N cùng lúc, SQL sẽ tạo ra **Tích Đề-các (Cartesian Product)** làm nhân chéo các dòng dữ liệu. Nếu bài viết có 2 views, 3 likes và 4 comments thì số dòng sinh ra sẽ là $2 \times 3 \times 4 = 24$ dòng! Nếu dùng `COUNT(v.id)` thì view sẽ thành 24 (sai thực tế). Dùng `COUNT(DISTINCT v.id)` bảo đảm chỉ đếm các ID view duy nhất, trả về con số chính xác 100%.

---

## Mục 4: Tầng Nghiệp Vụ (Service Package - Phân Tích Từng Phương Thức)

### 4.1. `AuthenticationService.java`
1. `authenticate(AuthenticationRequest request)`:
   - Tìm user theo `username`, nếu không thấy ném ngoại lệ `USER_NOT_EXITED`.
   - Dùng `passwordEncoder.matches(request.getPassword(), user.getPassword())` để so khớp mật khẩu nhập vào với chuỗi băm BCrypt trong CSDL.
   - Nếu khớp, thiết lập hạn sử dụng token là 1 giờ (`Instant.now().plus(1, ChronoUnit.HOURS)`), gọi `generateToken()` sinh chuỗi JWT và trả về `AuthenticationResponse`.
2. `generateToken(User user, Date expiryTime)`:
   - Tạo Header định nghĩa thuật toán `HS512`.
   - Tạo Payload chứa các Claim: `sub` (username), `iss` ("group.com"), `iat` (ngày cấp), `exp` (ngày hết hạn), `scope` (chuỗi quyền, ví dụ `"ADMIN USER"`).
   - Dùng `MACSigner(SIGNER_KEY.getBytes())` ký điện tử và xuất ra chuỗi JWT định dạng `header.payload.signature`.
3. `introspect(IntrospectRequest request)`:
   - Nhận token từ client, kiểm tra tính hợp lệ của chữ ký và thời gian hết hạn (`expirationTime`). Trả về boolean `true`/`false`.

### 4.2. `UserService.java`
1. `createUser(UserCreatetionRequest request)`:
   - Kiểm tra `existsByUsername()`, nếu trùng ném `USER_EXITED`.
   - Dùng `userMapper.toUser(request)` ánh xạ sang Entity.
   - Băm mật khẩu bằng `passwordEncoder.encode()`.
   - Gán quyền mặc định `ROLE_USER` và lưu xuống CSDL MySQL.
2. `getMyProfile()`:
   - Trích xuất username trực tiếp từ `SecurityContextHolder.getContext().getAuthentication().getName()`.
   - Tìm user trong DB và làm giàu dữ liệu qua `followService.enrichUserResponse()` (tính tổng số follower, following).
3. `changePassword(PasswordChangeRequest request)`:
   - Lấy user đang đăng nhập từ SecurityContext.
   - So sánh mật khẩu cũ bằng `passwordEncoder.matches()`.
   - Kiểm tra mật khẩu mới và xác nhận mật khẩu có khớp nhau không.
   - Băm mật khẩu mới và lưu đè vào CSDL.
4. `updateUser(UUID id, UserUpdateRequest request)`:
   - Hàm dành cho Quản trị viên cập nhật thông tin và phân quyền cho người dùng.
   - Dùng `u.getRoles().clear()` xóa toàn bộ quyền cũ và `u.getRoles().addAll(request.getRoles())` nạp danh sách quyền mới (ví dụ thăng cấp User thành Admin).

### 4.3. `BlogService.java`
1. `createBlog(BlogCreationRequest request)`:
   - Lấy tác giả từ SecurityContext.
   - Tìm kiếm Danh mục (Category) nếu người dùng có chọn.
   - Xử lý Tag thông minh: Quét từng tên tag trong danh sách, nếu tag đã có trong DB thì lấy lại, nếu chưa có thì tự động tạo mới vào bảng `tags` (`tagRepository.save(newTag)`).
   - Lưu bài viết và gọi `enrichBlogResponse()` để sinh slug SEO và nạp số lượng view/like/comment.
2. `updateBlog(UUID id, BlogUpdateRequest request)`:
   - Kiểm tra quyền tác giả: Chỉ người tạo bài viết mới được sửa (`blog.getAuthor().getUsername().equals(currentUsername)`), nếu không ném lỗi `UNAUTHORIZED`.
   - **Xử lý luồng Lưu Nháp vs Xuất Bản**:
     - *Nếu user bấm Save Draft (`request.getDraft() == true`)*: Nếu bài đã từng publish trước đó, không được sửa cột `content` công khai mà lưu vào `draftContent` để người đọc bên ngoài không bị ảnh hưởng.
     - *Nếu user bấm Publish (`request.getDraft() == false`)*: Đổ toàn bộ nội dung mới vào cột `content`, xóa rỗng cột `draftContent = null`, set `draft = false`, cập nhật `publishedAt`.
3. `getBlogById(UUID id)`:
   - Lấy bài viết từ DB.
   - Tự động tạo một bản ghi `BlogView` lưu xuống bảng `blog_views` để tăng lượt đọc.
   - Trả về DTO kèm thông tin kiểm tra xem tài khoản đang đăng nhập đã like hoặc bookmark bài này chưa (`likedByCurrentUser`, `bookmarkedByCurrentUser`).
4. `deleteBlog(UUID id)`:
   - Kiểm tra: Người thực hiện phải là **Tác giả bài viết** HOẶC **Quản trị viên (`ROLE_ADMIN`)** mới có quyền xóa. Nếu không ném lỗi `UNAUTHORIZED`.
5. `filterBlogs(String keyword, UUID categoryId)`:
   - Lọc đa điều kiện: Vừa theo từ khóa tìm kiếm (tiêu đề), vừa theo danh mục được chọn.
6. `getSearchSuggestions(String keyword)`:
   - Tìm kiếm nhanh 5 bài viết khớp với từ khóa người dùng đang gõ trên thanh tìm kiếm để hiển thị menu gợi ý tức thì (Live search suggestion) kèm tên tác giả và danh mục.

### 4.4. `InteractionService.java`
1. `toggleLike(UUID blogId)`:
   - Kiểm tra trong bảng `blog_likes`: Nếu đã like rồi thì xóa bản ghi (Unlike); nếu chưa like thì tạo bản ghi mới (Like) và gửi thông báo `LIKE` cho tác giả bài viết qua `notificationService`.
2. `addComment(UUID blogId, CommentRequest request)`:
   - Tạo comment mới. Nếu có `parentId`, tìm comment cha và gán vào quan hệ phân cấp.
   - Gửi thông báo: Nếu là bình luận trực tiếp thì báo cho Tác giả bài viết (`COMMENT`); nếu là reply thì báo cho Chủ comment cha (`REPLY`).
3. `deleteComment(UUID commentId)`:
   - **Bảo mật phân quyền**: Chỉ có **Tác giả của bình luận đó** HOẶC **Chủ sở hữu của bài viết đó** mới có quyền xóa comment.

### 4.5. `FollowService.java`
1. `toggleFollow(String targetUsername)`:
   - Chặn không cho tự follow chính mình: `if (currentUsername.equals(targetUsername)) throw ...`.
   - Nếu đã follow thì xóa bản ghi (Unfollow); nếu chưa thì tạo bản ghi `UserFollow` và gửi thông báo `FOLLOW` đến người được theo dõi.

---

## Mục 5: Tầng Điều Khiển (Controller Package - Phân Tích Từng Endpoint)

| Controller Class | Endpoint URL | HTTP Method | Chức năng nghiệp vụ & Quyền hạn |
| :--- | :--- | :--- | :--- |
| **`AuthenticationController`** | `/auth/login` | `POST` | Tiếp nhận username/password, xác thực và trả về JWT Token. (Public) |
| | `/auth/introspect` | `POST` | Kiểm tra token có hợp lệ không. (Public) |
| **`UserController`** | `/users` | `POST` | Đăng ký tài khoản người dùng mới. (Public) |
| | `/users` | `GET` | Lấy danh sách toàn bộ người dùng trong hệ thống. (Yêu cầu `ROLE_ADMIN`) |
| | `/users/my-profile` | `GET` | Lấy thông tin cá nhân của người đang đăng nhập. (Đã đăng nhập) |
| | `/users/my-profile` | `PUT` | Cập nhật email, bio, avatar của tôi. (Đã đăng nhập) |
| | `/users/my-profile/change-password` | `PUT` | Đổi mật khẩu cá nhân. (Đã đăng nhập) |
| | `/users/profile/{username}` | `GET` | Xem trang hồ sơ công khai của một tác giả bất kỳ. (Public) |
| **`BlogController`** | `/blogs` | `POST` | Tạo bài viết mới. (Đã đăng nhập) |
| | `/blogs` | `GET` | Lấy danh sách bài viết trang chủ kèm lượt xem/thích/bình luận. (Public) |
| | `/blogs/{id}` | `GET` | Xem chi tiết bài viết và tự động tăng view. (Public) |
| | `/blogs/{id}` | `PUT` | Cập nhật bài viết (Tác giả). (Đã đăng nhập) |
| | `/blogs/{id}` | `DELETE` | Xóa bài viết (Tác giả hoặc Admin). (Đã đăng nhập) |
| | `/blogs/category/{categoryId}` | `GET` | Lọc danh sách bài viết theo Danh mục. (Public) |
| | `/blogs/tag/{tagId}` | `GET` | Lọc danh sách bài viết theo Thẻ Tag. (Public) |
| | `/blogs/search` | `GET` | Tìm kiếm bài viết theo từ khóa tiêu đề. (Public) |
| | `/blogs/search/suggestions` | `GET` | Gợi ý top 5 bài viết nhanh khi đang gõ phím. (Public) |
| | `/blogs/filter` | `GET` | Lọc kết hợp từ khóa và danh mục. (Public) |
| | `/blogs/my-blogs` | `GET` | Lấy danh sách bài viết của tôi (kể cả bản nháp). (Đã đăng nhập) |
| **`InteractionController`** | `/blogs/{blogId}/like` | `POST` | Thả tim / Bỏ thả tim bài viết. (Đã đăng nhập) |
| | `/blogs/{blogId}/comments` | `GET` | Lấy danh sách bình luận phân cấp của bài viết. (Public) |
| | `/blogs/{blogId}/comments` | `POST` | Thêm bình luận hoặc phản hồi (reply). (Đã đăng nhập) |
| | `/blogs/comments/{commentId}` | `DELETE` | Xóa bình luận (Tác giả comment hoặc Chủ bài viết). (Đã đăng nhập) |
| | `/blogs/{blogId}/bookmark` | `POST` | Lưu / Bỏ lưu bài viết vào danh sách đọc sau. (Đã đăng nhập) |
| | `/blogs/bookmarks` | `GET` | Lấy danh sách các bài viết tôi đã lưu. (Đã đăng nhập) |
| **`FollowController`** | `/users/{username}/follow` | `POST` | Theo dõi / Bỏ theo dõi tác giả. (Đã đăng nhập) |
| | `/users/{username}/followers` | `GET` | Lấy danh sách người theo dõi của tác giả. (Public) |
| | `/users/{username}/following` | `GET` | Lấy danh sách tác giả mà người này đang theo dõi. (Public) |
| **`NotificationController`** | `/api/notifications` | `GET` | Lấy danh sách thông báo của tôi. (Đã đăng nhập) |
| | `/api/notifications/{id}/read` | `PUT` | Đánh dấu thông báo đã đọc. (Đã đăng nhập) |
| | `/api/notifications/{id}` | `DELETE` | Xóa một thông báo. (Đã đăng nhập) |
| **`AdminController`** | `/api/admin/stats` | `GET` | Lấy số liệu thống kê (Tổng user, tổng post, 5 bài mới nhất) cho trang Dashboard Admin. (Yêu cầu `ROLE_ADMIN`) |
| **`UploadController`** | `/upload/image` | `POST` | Tải file ảnh lên Cloudinary và nhận đường link URL. (Đã đăng nhập) |
| **`ViewController`** | `/`, `/home`, `/login`, `/post`, `/admin/**` | `GET` | Điều hướng hiển thị các file template HTML Thymeleaf. (Public) |

---

## Mục 6: Xử Lý Ngoại Lệ & Tiện Ích (Exception & SlugUtils)

### 6.1. Xử lý ngoại lệ tập trung với `GlobalExceptionHandler.java`
- `@ControllerAdvice`: Bắt chặn mọi Exception xảy ra ở bất kỳ Controller nào trong toàn bộ ứng dụng.
- Phương thức `@ExceptionHandler(value = AppException.class)`:
  - Bắt các lỗi nghiệp vụ do lập trình viên chủ động ném ra (`throw new AppException(ErrorCode.USER_NOT_EXITED)`).
  - Trích xuất mã lỗi `code` và thông điệp `message` từ Enum `ErrorCode` đóng gói vào `ApiResponse` chuẩn trả về cho Client với HTTP Status 400 Bad Request.
- Phương thức `@ExceptionHandler(value = MethodArgumentNotValidException.class)`:
  - Bắt các lỗi vi phạm ràng buộc dữ liệu đầu vào khi dùng `@Valid` trên Request Body (ví dụ mật khẩu dưới 8 ký tự).
- Phương thức `@ExceptionHandler(value = Exception.class)`:
  - Tấm lưới an toàn cuối cùng bắt mọi lỗi không lường trước được (lỗi hệ thống, null pointer), trả về mã `9999` với thông điệp "Uncategorized error", bảo đảm không bao giờ để lộ vết lỗi hệ thống (Stacktrace) ra ngoài Client.

### 6.2. Tiện ích tạo đường dẫn thân thiện SEO `SlugUtils.java`
- **Mục đích**: Chuyển đổi tiêu đề bài viết tiếng Việt có dấu thành chuỗi URL không dấu ngăn cách bằng gạch nối:
  - Chuỗi gốc: `"Học Spring Boot 3 & JPA: Xây dựng Blog từ A-Z!"`
  - Chuỗi sau xử lý: `"hoc-spring-boot-3-jpa-xay-dung-blog-tu-a-z"`
- **Các bước kỹ thuật trong hàm `generateSlug()`**:
  1. Chuyển chữ thường `.toLowerCase()` và cắt khoảng trắng 2 đầu `.trim()`.
  2. Tách dấu tiếng Việt bằng chuẩn hóa Unicode NFD: `Normalizer.normalize(slug, Normalizer.Form.NFD)`.
  3. Xóa các ký tự dấu tổ hợp bằng biểu thức chính quy Regex: `\\p{InCombiningDiacriticalMarks}+`.
  4. Thay thế ký tự đặc biệt tiếng Việt: Chuyển `"đ"` thành `"d"`.
  5. Thay thế toàn bộ ký tự không phải chữ và số thành dấu gạch ngang: `[^a-z0-9]+` $\rightarrow$ `"-"`.
  6. Gộp nhiều dấu gạch ngang liên tiếp thành 1 dấu: `"-+"` $\rightarrow$ `"-"`.

---

## Mục 7: Tầng Giao Diện & Frontend JavaScript Giao Tiếp API

### 7.1. File `register.html` — Đăng ký & Tự động đăng nhập
- Bắt sự kiện `submit` form, gọi `event.preventDefault()` chặn reload trang.
- Kiểm tra tính hợp lệ ở client (độ dài username $\ge 3$, password $\ge 6$, mật khẩu xác nhận trùng khớp).
- Gửi `fetch('/users', { method: 'POST', body: JSON })`.
- Nếu thành công, tự động kích hoạt hàm `autoLogin()` gửi tiếp request tới `/auth/login` để lấy Token JWT và lưu vào `localStorage.setItem('token', token)` rồi chuyển hướng về trang chủ `/`.

### 7.2. File `nav.js` — Phân quyền hiển thị Menu Admin
- Trích xuất `token` từ `localStorage`.
- Giải mã phần Payload Base64 của JWT bằng `window.atob(token.split('.')[1])`.
- Đọc trường `scope`: Nếu chuỗi quyền có chứa chữ `"ADMIN"`, dùng jQuery `$('#btn-desk-admin').show()` để hiển thị nút vào trang quản trị Admin Controller. Nếu là User thường thì ẩn nút này đi.

---

# PHẦN IV: BỘ 25 CÂU HỎI VẤN ĐÁP "XOÁY TẬN TỪNG DÒNG CODE" & KỊCH BẢN ĐẠT ĐIỂM 10

### Q1: "Trong class `BlogService`, tại sao em không dùng `@Autowired` để tiêm các Repository mà lại dùng `@RequiredArgsConstructor`?"
- **Trả lời chuẩn**:  
  *"Dạ thưa Thầy, đây là kỹ thuật **Implicit Dependency Injection (Tiêm ngầm định)** theo chuẩn mực mới nhất của Spring. Khi dùng `@RequiredArgsConstructor` của Lombok, Lombok sẽ tự động tạo một Constructor chứa tất cả các biến khai báo `final` (`private final BlogRepository blogRepository;`). Kể từ phiên bản Spring 4.3 trở đi, khi một Class chỉ có duy nhất một Constructor, Spring IoC Container sẽ tự động inject các Bean vào mà **không cần phải viết `@Autowired`**. Cách này giúp các biến có tính bất biến (`final`), an toàn đa luồng và giúp nhóm viết Unit Test cực kỳ dễ dàng mà không bị phụ thuộc vào Spring Container ạ."*

### Q2: "Trong class `Comment.java`, tại sao lại có quan hệ `@ManyToOne Comment parent` và `@OneToMany List<Comment> replies` trỏ ngược lại chính nó?"
- **Trả lời chuẩn**:  
  *"Dạ thưa Thầy, đây là mô hình quan hệ **Tự tham chiếu (Self-Referencing Relationship)**. Trong thực tế, hệ thống blog cần hỗ trợ tính năng bình luận phân cấp: một người có thể trả lời (reply) bình luận của người khác. Khi đó, bình luận con sẽ có trường `parent_id` trỏ về khóa chính `id` của bình luận cha trong cùng bảng `comments`. Bình luận gốc cấp cao nhất sẽ có `parent_id = NULL` ạ."*

### Q3: "Tại sao trong `BlogRepository.java` em phải viết `COUNT(DISTINCT v.id)` mà không viết `COUNT(v.id)` thông thường?"
- **Trả lời chuẩn**:  
  *"Dạ thưa Thầy, trong câu truy vấn lấy danh sách bài viết, nhóm em thực hiện `LEFT JOIN` đồng thời 3 bảng quan hệ Một - Nhiều là `blog_views`, `blog_likes` và `comments`. Thao tác JOIN nhiều bảng 1-N cùng lúc sẽ tạo ra **Tích Đề-các (Cartesian Product)** làm nhân chéo số dòng dữ liệu. Nếu không có từ khóa `DISTINCT`, hàm `COUNT` sẽ đếm tất cả các dòng bị nhân chéo dẫn đến số view, like và comment bị sai lệch gấp nhiều lần thực tế. Dùng `COUNT(DISTINCT v.id)` bảo đảm chỉ đếm các định danh duy nhất, cho kết quả chính xác 100% ạ."*

### Q4: "Khi người dùng ấn 'Lưu nháp' một bài viết đã từng xuất bản trước đó, hệ thống xử lý như thế nào để độc giả bên ngoài không đọc phải nội dung dở dang?"
- **Trả lời chuẩn**:  
  *"Dạ thưa Thầy, trong hàm `updateBlog()` của `BlogService`, nhóm em thiết kế 2 cột tách biệt là `content` (nội dung public) và `draftContent` (nội dung đang sửa dở). Khi tác giả bấm 'Save Draft', hệ thống kiểm tra nếu bài viết này đã từng xuất bản (`draft == false`), code sẽ giữ nguyên cột `content` để độc giả xem bài viết bình thường, và chỉ ghi nội dung đang chỉnh sửa vào cột `draftContent`. Khi nào tác giả bấm 'Publish', hệ thống mới đổ dữ liệu từ `draftContent` sang `content` và xóa rỗng cột nháp ạ."*

### Q5: "Tại sao trong `SecurityConfig` nhóm em lại cấu hình `.csrf(AbstractHttpConfigurer::disable)`? Tắt CSRF như vậy có bị nguy hiểm không?"
- **Trả lời chuẩn**:  
  *"Dạ thưa Thầy, tắt CSRF hoàn toàn an toàn và là chuẩn mực bắt buộc cho kiến trúc **Stateless RESTful API dùng JWT**. Tấn công CSRF chỉ xảy ra khi trình duyệt tự động gửi kèm Cookie phiên đăng nhập (`JSESSIONID`) trong các request ẩn danh. Trong hệ thống của nhóm em, ứng dụng lưu Token JWT trong `localStorage` và gửi qua Header `Authorization: Bearer <token>`. Vì trình duyệt không bao giờ tự động đính kèm Header này, website độc hại của hacker không thể kích hoạt request giả mạo, do đó hệ thống miễn nhiễm với CSRF và việc tắt CSRF là hoàn toàn đúng kỹ thuật ạ."*

### Q6: "Làm sao hệ thống của nhóm ngăn chặn được việc một User tự bấm Like bài viết nhiều lần để gian lận số lượt Like?"
- **Trả lời chuẩn**:  
  *"Dạ thưa Thầy, nhóm em bảo vệ ở 2 tầng:*
  1. *Ở tầng CSDL: Bảng `blog_likes` được gắn ràng buộc duy nhất phức hợp `@Table(uniqueConstraints = {@UniqueConstraint(columnNames = {"user_id", "blog_id"})})`. Nếu có câu lệnh INSERT trùng lặp, MySQL sẽ lập tức chặn lại và báo lỗi Duplicate Entry.*
  2. *Ở tầng Logic Service: Hàm `toggleLike()` trước khi lưu sẽ truy vấn `findByBlogIdAndUserUsername()`. Nếu thấy đã tồn tại thì tiến hành xóa (Unlike), nếu chưa có mới tạo mới (Like) ạ."*

### Q7: "Trong `SecurityConfig.java`, tại sao danh sách `PUBLIC_GET_ENDPOINTS` lại chứa cả `/admin/**`? Ai cũng vào được trang Admin hay sao?"
- **Trả lời chuẩn**:  
  *"Dạ thưa Thầy, đây là đặc thù của mô hình Client-Side SPA kết hợp Spring Security. Đường dẫn `/admin/**` trong `PUBLIC_GET_ENDPOINTS` chỉ là đường dẫn tải file HTML tĩnh từ `ViewController` (vì khi người dùng bấm vào link trên thanh địa chỉ trình duyệt, request GET ban đầu không thể đính kèm Header Authorization JWT). Tuy nhiên, trang HTML này chỉ là một khung vỏ rỗng. Khi mở trang lên, mã JavaScript trên trang Admin sẽ lấy Token JWT trong `localStorage` và gửi request lấy số liệu thống kê lên API Backend `/api/admin/stats`. API này nằm trong mảng `ADMIN_ENDPOINTS` và được bảo vệ nghiêm ngặt bằng `.hasRole('ADMIN')`. Nếu người dùng không có quyền Admin, API sẽ trả về mã `HTTP 403 Forbidden` và JavaScript sẽ đẩy người dùng về trang chủ ngay lập tức ạ."*

### Q8: "Annotation `@Transactional` trong `InteractionService.java` hoạt động theo cơ chế nào nếu câu lệnh thêm bình luận thành công nhưng câu lệnh gửi thông báo bị lỗi?"
- **Trả lời chuẩn**:  
  *"Dạ thưa Thầy, nhờ có `@Transactional`, Spring AOP sẽ bọc phương thức `addComment()` bằng một Proxy giao dịch. Mọi câu lệnh SQL thêm bình luận và tạo thông báo đều nằm trong cùng một Database Transaction với cờ `AutoCommit = false`. Nếu câu lệnh gửi thông báo ném ra một ngoại lệ `RuntimeException`, Proxy sẽ bắt được và tự động gọi `Connection.rollback()`. Toàn bộ bình luận vừa thêm trước đó sẽ bị hủy bỏ, khôi phục trạng thái CSDL về nguyên vẹn trước khi gọi hàm, bảo đảm tính chất **Atomicity (Nguyên tử)** của ACID ạ."*

### Q9: "Kiểu dữ liệu UUID có ưu và nhược điểm gì so với kiểu số nguyên tự tăng `BIGINT AUTO_INCREMENT`?"
- **Trả lời chuẩn**:  
  *"Dạ thưa Thầy:
  - **Ưu điểm lớn nhất**: Tính bảo mật. Số tự tăng rất dễ bị lộ quy mô hệ thống và bị tấn công cào dữ liệu qua URL (`/blogs/1`, `/blogs/2`). UUID là chuỗi ngẫu nhiên 128-bit không thể đoán trước được. Ngoài ra, UUID cho phép Client tự sinh ID trong các hệ thống phân tán mà không lo bị xung đột khóa.
  - **Nhược điểm**: Tốn dung lượng lưu trữ hơn (36 ký tự `VARCHAR` hoặc 16 bytes `BINARY`) và tốc độ đánh chỉ mục Index B-Tree trong MySQL chậm hơn số nguyên một chút do tính ngẫu nhiên không có thứ tự tăng dần liên tục ạ."*

### Q10: "Làm sao Backend lấy được danh tính của tác giả khi tạo bài viết mới trong khi Request Body gửi lên không hề có trường `authorId`?"
- **Trả lời chuẩn**:  
  *"Dạ thưa Thầy, nhóm em tuyệt đối không nhận `authorId` từ Client gửi lên để chống hành vi giả mạo danh tính tác giả. Thay vào đó, trong hàm `createBlog()`, nhóm em lấy trực tiếp username từ ngữ cảnh bảo mật của Spring Security:  
  `String currentUsername = SecurityContextHolder.getContext().getAuthentication().getName();`  
  Thông tin này được bộ lọc `JwtAuthenticationFilter` giải mã và xác thực trực tiếp từ chuỗi Token JWT có chữ ký điện tử hợp lệ, bảo đảm an toàn 100% ạ."*

---

### 🎯 CHECKLIST 5 PHÚT TRƯỚC GIỜ VẤN ĐÁP (NGÀY 01/11/2026):
1. **Khởi động dịch vụ sẵn**: Bật MySQL Server (`localhost:3306`), chạy ứng dụng Spring Boot Backend trên cổng `8080`, test thử truy cập `localhost:8080` trên trình duyệt.
2. **Chuẩn bị 2 phiên duyệt web**:
   - Cửa sổ 1: Đăng nhập tài khoản `admin` (mật khẩu `123456`) $\rightarrow$ Sẵn sàng mở Dashboard Thống kê và Quản lý người dùng.
   - Cửa sổ 2 (Ẩn danh): Đăng nhập tài khoản thành viên `duonghd` / `dungnt` / `longlt` $\rightarrow$ Sẵn sàng demo viết bài, upload ảnh banner, like và bình luận bài viết.
3. **Quyển báo cáo in giấy**: Đủ 15-20 trang, đóng bìa chỉn chu, kiểm tra không có trang nào in code.
4. **Tâm thế trả lời**: Tự tin, nói to, dứt khoát, đi thẳng vào keyword kỹ thuật. Thầy hỏi đến đâu chỉ đúng file code và dòng code đến đó.

---
*Bản tài liệu này là tài sản học thuật đầy đủ và toàn diện nhất, chuẩn bị cho nhóm đạt điểm 10 tuyệt đối trong đợt Báo cáo BTL ngày 01/11/2026 và kỳ thi Tự luận cuối kỳ ngày 22/11/2026!*
