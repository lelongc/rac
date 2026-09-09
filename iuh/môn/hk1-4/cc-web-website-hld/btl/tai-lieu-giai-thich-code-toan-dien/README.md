# TÀI LIỆU GIẢI THÍCH TOÀN BỘ CODE DỰ ÁN BÀI TẬP LỚN BLOG WEBSITE (TỪ DÒNG TỚI DÒNG)
### ĐẠI HỌC CÔNG NGHIỆP TP. HỒ CHÍ MINH (IUH) - KHOA CÔNG NGHỆ THÔNG TIN
#### HỌC PHẦN: CÔNG NGHỆ WEB / PHÁT TRIỂN ỨNG DỤNG WEB

---

## 👥 THÔNG TIN NHÓM THỰC HIỆN
1. **Hoàng Đại Dương** - MSSV: **24743991**
2. **Nguyễn Trung Dũng** - MSSV: **24000905**
3. **Lê Thành Long** - MSSV: **23630851**

- **Đề tài**: Xây dựng Website Blog Mạng Xã Hội Đa Người Dùng (Bleb Blog)
- **Công nghệ nền tảng**: Java 21, Spring Boot 3.5.11, Spring Security (JWT HS512), Spring Data JPA (Hibernate), H2 Database (File Mode tương thích MySQL), Cloudinary Media API, Thymeleaf, Vanilla JavaScript (ES6) & Bootstrap 5.3.

---

## 🎯 MỤC ĐÍCH BỘ TÀI LIỆU NÀY
Bộ tài liệu này được biên soạn độc quyền và chi tiết từ dòng tới dòng (Line-by-line) nhằm giúp:
- Bất kỳ thành viên nào trong nhóm — **kể cả người chưa từng học lập trình Web bao giờ** — cũng có thể đọc hiểu từng chú thích (`@Entity`, `@RestController`, `@Autowired`), từng biến số, từng thuật toán và luồng đi của dữ liệu.
- Tự tin giải thích mọi chức năng, trả lời trôi chảy bất kỳ câu hỏi vấn đáp nào của giảng viên, và thực hiện sửa code trực tiếp (Live Coding) ngay tại bàn thi để đạt **điểm 10 tuyệt đối**.

---

## 📚 MỤC LỤC TỔNG QUAN HỆ THỐNG TÀI LIỆU

### 📂 [THƯ MỤC 01: TỔNG QUAN KIẾN TRÚC HỆ THỐNG](./01-tong-quan-kien-truc/)
- [01-Kien-Truc-He-Thong-Spring-Boot-Va-Mo-Hinh-3-Tier.md](./01-tong-quan-kien-truc/01-Kien-Truc-He-Thong-Spring-Boot-Va-Mo-Hinh-3-Tier.md): Giải thích mô hình 3 lớp (Controller - Service - Repository), vòng đời của một HTTP Request, cơ chế Stateless và DTO Pattern.
- [02-Cau-Truc-Thu-Muc-Va-File-Pom-Xml.md](./01-tong-quan-kien-truc/02-Cau-Truc-Thu-Muc-Va-File-Pom-Xml.md): Ý nghĩa từng thư mục mã nguồn và giải thích chi tiết từng dòng trong file quản lý gói `pom.xml` (Maven dependencies, Java 21, MapStruct, Lombok).
- [03-Kien-Truc-Thymeleaf-Va-Hybrid-SPA-Vs-SSR.md](./01-tong-quan-kien-truc/03-Kien-Truc-Thymeleaf-Va-Hybrid-SPA-Vs-SSR.md): **Câu hỏi điểm 10:** Bản chất Thymeleaf trong dự án (Template View Resolver), tại sao không dùng `th:each`/`th:text` cổ điển mà dùng kiến trúc Hybrid CSR + RESTful API kết hợp JWT Token?

### 📂 [THƯ MỤC 02: CẤU HÌNH VÀ KHỞI TẠO](./02-cau-hinh-va-khoi-tao/)
- [01-Application-Yaml-Va-Secret.md](./02-cau-hinh-va-khoi-tao/01-Application-Yaml-Va-Secret.md): Giải thích từng thông số trong `application.yaml` và `application-secret.yml` (Cổng 8080, CSDL H2 bền vững `file:./data/blogdb`, cờ `AUTO_SERVER=TRUE`, khóa ký JWT, tài khoản Cloudinary).
- [02-SecurityConfig-Va-CorsConfig.md](./02-cau-hinh-va-khoi-tao/02-SecurityConfig-Va-CorsConfig.md): **File quan trọng nhất khi thi vấn đáp!** Giải thích từng dòng trong chuỗi lọc `SecurityFilterChain`, bộ giải mã Nimbus JWT Decoder, tắt CSRF, phân quyền Role ADMIN vs USER, và cấu hình CORS.
- [03-ApplicationInitConfig.md](./02-cau-hinh-va-khoi-tao/03-ApplicationInitConfig.md): Cơ chế nạp dữ liệu mồi (`ApplicationRunner`), tạo tài khoản mặc định cho 3 thành viên và admin, băm mật khẩu BCrypt, tạo sẵn Categories, Tags và Blogs mẫu.
- [04-CloudinaryConfig.md](./02-cau-hinh-va-khoi-tao/04-CloudinaryConfig.md): Khởi tạo Bean kết nối dịch vụ lưu trữ hình ảnh đám mây Cloudinary.

### 📂 [THƯ MỤC 03: THỰC THỂ CƠ SỞ DỮ LIỆU (ENTITIES)](./03-thuc-the-csdl-entities/)
- [01-Entity-User-Va-Role.md](./03-thuc-the-csdl-entities/01-Entity-User-Va-Role.md): Chi tiết lớp `User.java`, bảng liên kết quyền `@ElementCollection`, khóa chính UUID ngẫu nhiên và enum `Role.java`.
- [02-Entity-Blog-Va-Category-Tag.md](./03-thuc-the-csdl-entities/02-Entity-Blog-Va-Category-Tag.md): Quan hệ 1-Nhiều (`@ManyToOne`) và Nhiều-Nhiều (`@ManyToMany`), kiểu dữ liệu văn bản lớn `LONGTEXT`, cơ chế lưu nháp `draftContent`, và tự động cập nhật ngày giờ `@PrePersist`, `@PreUpdate`.
- [03-Entity-Comment-Like-Bookmark.md](./03-thuc-the-csdl-entities/03-Entity-Comment-Like-Bookmark.md): Mô hình Cây bình luận đa tầng (Self-Referencing Entity), chống Like/Bookmark trùng lặp bằng `@UniqueConstraint`, và xóa dây chuyền phần cứng `@OnDelete(action = CASCADE)`.
- [04-Entity-Follow-Notification-View.md](./03-thuc-the-csdl-entities/04-Entity-Follow-Notification-View.md): Mối quan hệ người theo dõi (`UserFollow`), bảng thông báo người dùng (`Notification`) và bộ đếm lượt xem hỗ trợ khách vãng lai (`BlogView`).

### 📂 [THƯ MỤC 04: TẦNG REPOSITORY (SPRING DATA JPA)](./04-tang-repository-jpa/)
- [01-Khai-Niem-Spring-Data-Jpa-Va-Cach-Hoat-Dong.md](./04-tang-repository-jpa/01-Khai-Niem-Spring-Data-Jpa-Va-Cach-Hoat-Dong.md): Cơ chế Dynamic Proxy sinh câu lệnh SQL từ tên hàm (Derived Queries), cách dùng `Optional<T>` chống lỗi sập server, và kỹ thuật `@Query` giải quyết bài toán N+1 Queries.
- [02-Chi-Tiet-10-Repository.md](./04-tang-repository-jpa/02-Chi-Tiet-10-Repository.md): Giải thích chi tiết từng hàm trong cả 10 interface Repository của dự án.

### 📂 [THƯ MỤC 05: TẦNG NGHIỆP VỤ (SERVICES)](./05-tang-nghiep-vu-services/)
- [01-AuthenticationService-Va-Token.md](./05-tang-nghiep-vu-services/01-AuthenticationService-Va-Token.md): Toàn bộ luồng đăng nhập, băm so khớp BCrypt, thuật toán tạo JWT HMAC-SHA512 với cấu trúc 3 phần và hàm xác thực token `introspect`.
- [02-UserService-Va-AdminService.md](./05-tang-nghiep-vu-services/02-UserService-Va-AdminService.md): Đăng ký tài khoản, phân quyền, đổi mật khẩu an toàn 5 bước và thu thập số liệu thống kê cho Dashboard Admin.
- [03-BlogService-Toan-Dien.md](./05-tang-nghiep-vu-services/03-BlogService-Toan-Dien.md): Nghiệp vụ quản lý bài viết phức tạp nhất hệ thống: CRUD, cơ chế bản nháp 2 luồng độc quyền, tự động tăng view khi đọc bài, kiểm tra quyền xóa kép và hàm làm giàu dữ liệu `enrichBlogResponse`.
- [04-InteractionService-Va-Comment.md](./05-tang-nghiep-vu-services/04-InteractionService-Va-Comment.md): Nghiệp vụ bật/tắt Thích (Like), Lưu bài viết (Bookmark), thuật toán đệ quy xây dựng cây bình luận và phân quyền xóa bình luận.
- [05-FollowService-Va-NotificationService.md](./05-tang-nghiep-vu-services/05-FollowService-Va-NotificationService.md): Theo dõi tác giả, chặn tự follow bản thân và bộ máy tự động phát thông báo cho người dùng.
- [06-CloudinaryService-Va-Category-TagService.md](./05-tang-nghiep-vu-services/06-CloudinaryService-Va-Category-TagService.md): Đẩy luồng byte ảnh lên Cloudinary lấy link HTTPS, quản lý danh mục và thẻ tag kèm số lượng bài viết chuẩn 3NF.

### 📂 [THƯ MỤC 06: TẦNG ĐIỀU KHIỂN (CONTROLLERS)](./06-tang-dieu-khien-controllers/)
- [01-AuthenticationController-Va-UserController.md](./06-tang-dieu-khien-controllers/01-AuthenticationController-Va-UserController.md): API xác thực và người dùng. Bẫy lỗi thứ tự định tuyến URL giữa route tĩnh (`/my-profile`) và route động (`/{userId}`).
- [02-BlogController-Va-UploadController.md](./06-tang-dieu-khien-controllers/02-BlogController-Va-UploadController.md): Toàn bộ API bài viết (CRUD, tìm kiếm, lọc theo tag/danh mục) và API nhận file ảnh `POST /upload/image`.
- [03-InteractionController-Follow-NotificationController.md](./06-tang-dieu-khien-controllers/03-InteractionController-Follow-NotificationController.md): Các API tương tác mạng xã hội, follow và thông báo chuông.
- [04-AdminController-Category-Tag-ViewController.md](./06-tang-dieu-khien-controllers/04-AdminController-Category-Tag-ViewController.md): API quản trị và sự khác biệt bản chất giữa `@Controller` điều hướng Thymeleaf HTML và `@RestController` trả về JSON.

### 📂 [THƯ MỤC 07: XỬ LÝ NGOẠI LỆ, DTO, MAPPER & UTIL](./07-exception-dto-mapper-util/)
- [01-GlobalExceptionHandler-Va-ErrorCode.md](./07-exception-dto-mapper-util/01-GlobalExceptionHandler-Va-ErrorCode.md): Bắt lỗi tập trung toàn cục bằng `@ControllerAdvice` và từ điển mã lỗi chuẩn hóa `ErrorCode`.
- [02-DTO-Request-Va-Response.md](./07-exception-dto-mapper-util/02-DTO-Request-Va-Response.md): Danh mục 20 DTO Request & Response, lớp vỏ `ApiResponse<T>` và chú thích lọc null `@JsonInclude(NON_NULL)`.
- [03-MapStruct-Mappers-Va-SlugUtils.md](./07-exception-dto-mapper-util/03-MapStruct-Mappers-Va-SlugUtils.md): Công nghệ ánh xạ tự động MapStruct tại thời điểm biên dịch và giải thuật 6 bước tạo Slug tiếng Việt không dấu chuẩn SEO.

### 📂 [THƯ MỤC 08: TẦNG FRONTEND, JAVASCRIPT & GIAO DIỆN](./08-tang-frontend-javascript/)
- [01-Tong-Quan-Kien-Truc-Frontend-Va-Token-Storage.md](./08-tang-frontend-javascript/01-Tong-Quan-Kien-Truc-Frontend-Va-Token-Storage.md): Kiến trúc giao diện, lưu trữ Token trong `localStorage` và trạm trung chuyển `callApi()` tự động gắn tiêu đề Bearer Token.
- [02-Auth-Js-Va-Init-Js.md](./08-tang-frontend-javascript/02-Auth-Js-Va-Init-Js.md): Kiểm tra trạng thái đăng nhập, giải thuật sinh avatar viết tắt `initials()` và bộ điều phối khởi động trang web `init.js`.
- [03-Posts-Js-Va-Blog-Editor.md](./08-tang-frontend-javascript/03-Posts-Js-Va-Blog-Editor.md): Hiển thị thẻ bài viết, trích xuất văn bản sạch `extractText()`, tính thời gian đọc bài viết và luồng soạn thảo bài viết.
- [04-Nav-Js-Sidebar-Js-Filters-Js-Pages-Js.md](./08-tang-frontend-javascript/04-Nav-Js-Sidebar-Js-Filters-Js-Pages-Js.md): Mổ xẻ giải mã Token JWT ngay tại Client để hiện nút Admin, Cơ chế Lọc kép kết hợp `window.history.pushState()` và bảng xếp hạng Trending.
- [05-Chi-Tiet-Trang-Doc-Bai-Post-Html-Va-Comment-System.md](./08-tang-frontend-javascript/05-Chi-Tiet-Trang-Doc-Bai-Post-Html-Va-Comment-System.md): Giải thích toàn diện file `post.html`, cơ chế render khối Editor.js blocks (paragraph, header, code, image, quote), luồng tăng view ẩn danh, thả tim, đánh dấu, theo dõi tác giả và cây bình luận đệ quy đa cấp.
- [06-Chi-Tiet-Trinh-Soan-Thao-Blog-Editor-Html.md](./08-tang-frontend-javascript/06-Chi-Tiet-Trinh-Soan-Thao-Blog-Editor-Html.md): Bóc tách 1,319 dòng trình soạn thảo khối Notion-like của `blog-editor.html`: Menu lệnh Slash `/`, kéo thả khối, tải ảnh bìa & ảnh nội dung lên Cloudinary, chuyển đổi tức thì chế độ Xem trước (Preview) và Lưu bản nháp (Draft).
- [07-Quan-Ly-Tac-Gia-Manage-Blogs-Saved-Blogs-Profile.md](./08-tang-frontend-javascript/07-Quan-Ly-Tac-Gia-Manage-Blogs-Saved-Blogs-Profile.md): Không gian cá nhân tác giả: Quản lý bài viết 2 tab Published vs Drafts (`Manage-Blogs.html`), danh sách bài đã lưu (`saved-blogs.html`), trang hồ sơ cá nhân và Modal Followers / Following (`user-profile.html`), và Hộp thư thông báo (`notifications.html`).
- [08-He-Thong-Giao-Dien-Admin-Dashboard-Va-Quan-Tri.md](./08-tang-frontend-javascript/08-He-Thong-Giao-Dien-Admin-Dashboard-Va-Quan-Tri.md): Hệ thống quản trị toàn diện: Dashboard số liệu thống kê (`dashboard.html`), Quản lý bài viết có phân trang 5 bài/trang (`posts.html`), Quản lý người dùng và cấp quyền (`users.html`), Quản lý Danh mục và Thẻ nhãn (`categories-tags.html`).
- [09-Kien-Truc-Giao-Dien-CSS-Design-Tokens-Main-Css.md](./08-tang-frontend-javascript/09-Kien-Truc-Giao-Dien-CSS-Design-Tokens-Main-Css.md): Kiến trúc giao diện 797 dòng của `main.css`: Hệ thống biến Design Tokens (`:root`), Navbar hiệu ứng kính mờ (Glassmorphism), ô tìm kiếm co giãn thông minh, Post Card hiệu ứng nhấc bổng, Toast notification, và thiết kế đáp ứng (Responsive Breakpoints).

### 📂 [THƯ MỤC 09: CẨM NANG VẤN ĐÁP ĐIỂM 10](./09-cam-nang-van-dap-diem-10/)
- [01-Kich-Ban-Thuyet-Trinh-Demo-BTL-5-Phut.md](./09-cam-nang-van-dap-diem-10/01-Kich-Ban-Thuyet-Trinh-Demo-BTL-5-Phut.md): Kịch bản phân vai và từng câu thoại chuẩn mực khi demo trực tiếp 5 phút trước hội đồng.
- [02-Top-50-Cau-Hoi-Van-Dap-Giang-Vien-Hay-Hoi-Nhat.md](./09-cam-nang-van-dap-diem-10/02-Top-50-Cau-Hoi-Van-Dap-Giang-Vien-Hay-Hoi-Nhat.md): **Bộ 50 câu hỏi trắc nghiệm miệng & câu hỏi chuyên sâu** bao quát 100% mọi tình huống giảng viên hay hỏi kèm câu trả lời chuẩn xác nhất.
- [03-Huong-Dan-Debug-Va-Sua-Code-Truc-Tiep-Khi-Giang-Vien-Yeu-Cau.md](./09-cam-nang-van-dap-diem-10/03-Huong-Dan-Debug-Va-Sua-Code-Truc-Tiep-Khi-Giang-Vien-Yeu-Cau.md): Hướng dẫn Live Coding trong 2 phút: Thêm trường mới, đổi luật validate, phân quyền API, đổi cổng server và cách mở trực tiếp CSDL H2 Console để giải thích dữ liệu.

### 📂 [THƯ MỤC 10: KIỂM THỬ VÀ TRIỂN KHAI](./10-kiem-thu-va-trien-khai/)
- [01-Kiem-Thu-Tu-Dong-SpringBootTest-Va-Ma-Tran-TestCase.md](./10-kiem-thu-va-trien-khai/01-Kiem-Thu-Tu-Dong-SpringBootTest-Va-Ma-Tran-TestCase.md): Cơ chế chạy `@SpringBootTest`, bài kiểm thử Context Sanity, Ma trận Test Cases hoàn chỉnh (Auth, Blog, Interaction, Admin) và hướng dẫn viết Integration Test với MockMvc.
- [02-Huong-Dan-Dong-Goi-Build-Jar-Va-Trien-Khai.md](./10-kiem-thu-va-trien-khai/02-Huong-Dan-Dong-Goi-Build-Jar-Va-Trien-Khai.md): Quy trình đóng gói Fat JAR bằng Maven (`mvn clean package`), chạy độc lập trên Production (`java -jar`), cấu hình đa môi trường (Profiles), chuyển sang MySQL Cloud và bảo mật biến môi trường.

---

## ⚡ LỘ TRÌNH ÔN THI CẤP TỐC DÀNH CHO THÀNH VIÊN NHÓM
- **Ngày 1**: Đọc lướt Thư mục 01 (Tổng quan kiến trúc) + Thư mục 03 (Entities). Mở H2 Console xem các bảng trong DB.
- **Ngày 2**: Đọc Thư mục 02 (Bảo mật SecurityConfig) + Thư mục 05 (Services). Nắm chắc luồng tạo bài viết và xác thực JWT.
- **Ngày 3**: Đọc Thư mục 06 (Controllers) + Thư mục 07 (Exceptions, DTO, Mappers).
- **Ngày 4**: Đọc Thư mục 08 (Frontend JS, HTML, CSS) + Thư mục 10 (Kiểm thử & Triển khai). Tập dượt kịch bản demo 5 phút trên 2 trình duyệt.
- **Ngày 5**: Học thuộc lòng file `09.02-Top-50-Cau-Hoi-Van-Dap-Giang-Vien-Hay-Hoi-Nhat.md` và thực hành thử 6 tình huống Live Coding trong file `09.03`.

Chúc nhóm bảo vệ thành công rực rỡ và đạt điểm 10 tuyệt đối! 🎓🎉
