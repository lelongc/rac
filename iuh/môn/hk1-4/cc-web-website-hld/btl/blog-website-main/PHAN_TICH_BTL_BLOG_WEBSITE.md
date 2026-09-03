# 📋 BÁO CÁO PHÂN TÍCH ĐỀ TÀI BÀI TẬP LỚN
## ĐỀ TÀI: XÂY DỰNG BLOG WEBSITE - NỀN TẢNG VIẾT BÀI VÀ DIỄN ĐÀN TRỰC TUYẾN ĐA NGƯỜI DÙNG
> **Môn học:** Công nghệ web và website hướng dữ liệu  
> **Đơn vị:** Trường Đại học Công Nghiệp TP. Hồ Chí Minh (IUH) — Khoa Công nghệ Thông tin  
> **Giảng viên hướng dẫn:** Bộ môn Công nghệ Phần mềm & Hệ thống Thông tin  

---

### 👥 THÀNH VIÊN NHÓM THỰC HIỆN:
1. **24743991 — Hoàng Đại Dương**
2. **24000905 — Nguyễn Trung Dũng**
3. **23630851 — Lê Thành Long**

---

## 1. TỔNG QUAN HỆ THỐNG VÀ MỤC TIÊU ĐỀ TÀI

Hệ thống **Blog Website - Nền tảng Viết bài & Diễn đàn trực tuyến** là một ứng dụng web hướng dữ liệu hiện đại, cho phép các tác giả tự do sáng tạo nội dung, chia sẻ kiến thức công nghệ, kết nối cộng đồng thông qua các tính năng tương tác mạng xã hội thu nhỏ (thả tim, bình luận phân cấp, lưu bài viết yêu thích, theo dõi tác giả, nhận thông báo thời gian thực) và cung cấp bảng điều khiển quản trị (Admin Dashboard) mạnh mẽ để kiểm duyệt nội dung, quản lý người dùng và phân tích dữ liệu thống kê.

---

## 2. KIẾN TRÚC VÀ CÔNG NGHỆ SỬ DỤNG (CẬP NHẬT CHUẨN XÁC 100% THEO ỨNG DỤNG HIỆN TẠI)

Dự án được xây dựng theo mô hình **Kiến trúc phân tầng chuẩn doanh nghiệp (Layered Architecture)** kết hợp giữa **RESTful API Backend** và **Single-Page Multi-View Frontend**:

* **Ngôn ngữ & Nền tảng**: **Java 21**, **Spring Boot 3.5.11**.
* **Cơ sở dữ liệu (Database)**: 
  - **H2 Persistent File Database** (`jdbc:h2:file:./data/blogdb;AUTO_SERVER=TRUE;MODE=MySQL;...`): Dữ liệu được lưu vĩnh viễn vào file nhị phân `data/blogdb.mv.db` trên ổ cứng, **không bị mất khi tắt/khởi động lại server**, chạy độc lập không cần cài đặt thêm phần mềm.
  - **Hỗ trợ chuyển đổi linh hoạt sang MySQL 8.0** chỉ bằng 1 dòng cấu hình trong `application.yaml`.
  - Quản lý CSDL qua **H2 Web Console** tại đường dẫn `/h2-console`.
* **ORM & Data Access**: **Spring Data JPA (Hibernate ORM 6.6)** quản lý thực thể, quan hệ bảng và tự động sinh câu lệnh SQL tối ưu.
* **Bảo mật & Phân quyền**: 
  - **Spring Security 6**, kiến trúc Stateless không lưu session RAM.
  - Xác thực Token **JWT (JSON Web Token)** chuẩn **Nimbus-JOSE-JWT**, mã hóa chữ ký bằng thuật toán băm cực mạnh **HS512**.
  - Mã hóa mật khẩu người dùng một chiều bằng **BCrypt** (`strength = 10`).
  - Phân quyền chặt chẽ theo vai trò: `ROLE_ADMIN` và `ROLE_USER`.
* **Lưu trữ hình ảnh đám mây**: Tích hợp **Cloudinary API (SDK 1.36.0)** phục vụ upload ảnh đại diện (Avatar) và ảnh bìa bài viết (Banner).
* **Thư viện tối ưu mã nguồn**: 
  - **Project Lombok**: Tự động sinh Getter, Setter, `@Builder`, `@RequiredArgsConstructor`, `@FieldDefaults`.
  - **MapStruct (1.5.5.Final)**: Tự động ánh xạ chuyển đổi hiệu năng cao giữa Entity $\leftrightarrow$ DTO.
* **Giao diện người dùng (Frontend)**:
  - **Thymeleaf Template Engine** kết hợp cấu trúc các thành phần dùng chung (Fragments: `navbar`, `hero`, `sidebar`, `footer`, `admin_sidebar`).
  - **HTML5, CSS3, JavaScript (ES6+), jQuery, Bootstrap 5.3, Tailwind CSS**.
  - Giao tiếp bất đồng bộ qua **Fetch API / AJAX**, lưu trữ Token tại `localStorage`.

---

## 3. CÁC TÍNH NĂNG CHÍNH CỦA HỆ THỐNG

### 👤 3.1. Phía Người Dùng (Member / Author):
1. **Xác thực & Bảo mật tài khoản**:
   - Đăng ký tài khoản mới (tự động đăng nhập ngầm và chuyển hướng trang chủ sau khi đăng ký thành công).
   - Đăng nhập bảo mật JWT, hiển thị Toast thông báo trạng thái.
   - Đổi mật khẩu cá nhân (`/change-password`), khôi phục mật khẩu (`/forgot-password`).
   - Đăng xuất (xóa token khỏi `localStorage` và cập nhật lại giao diện Navbar).
2. **Quản lý Hồ sơ & Tác giả (Profile & Social)**:
   - Xem trang cá nhân công khai của tác giả (`/user-profile?username=...`).
   - Chỉnh sửa tiểu sử (Bio), thay đổi ảnh đại diện Avatar (tải lên Cloudinary) tại `/edit-profile`.
   - Tính năng Theo dõi / Bỏ theo dõi tác giả khác (Follow / Unfollow).
3. **Soạn thảo & Quản lý bài viết (Blog Engine)**:
   - Trình soạn thảo bài viết trực quan (`/blog-editor`), nhập tiêu đề, danh mục, gắn nhiều thẻ tag, dán link banner ảnh, nội dung văn bản.
   - Quản lý bài viết cá nhân (`/manage-blogs`): xem danh sách bài do mình viết, chỉnh sửa, xóa bài viết.
4. **Tương tác cộng đồng**:
   - Thả tim bài viết (Like / Unlike) với hiệu ứng đổi màu icon thời gian thực.
   - Bình luận bài viết (Comment) đa cấp, hiển thị ngay lập tức không cần tải lại trang.
   - Lưu bài viết vào danh sách yêu thích cá nhân (Bookmark) và quản lý tại `/saved-blogs`.
   - Tự động tăng số lượt đọc (**Views**) khi có người mở xem chi tiết bài viết (`/post?id=...`).
5. **Bộ lọc, Tìm kiếm & Thông báo**:
   - Lọc bài viết theo Danh mục (Categories) và Thẻ (Tags) ở Sidebar bên phải.
   - Sắp xếp bài viết linh hoạt: Mới nhất, Cũ nhất, Tiêu đề A-Z.
   - Tìm kiếm bài viết theo từ khóa ở Navbar.
   - Trung tâm thông báo (`/notifications`): nhận thông báo khi có người khác thích hoặc bình luận bài viết của mình, đánh dấu đã đọc / xóa thông báo.

### 🛡️ 3.2. Phía Quản Trị Viên (Admin):
1. **Bảng điều khiển quản trị (Admin Dashboard - `/admin/dashboard`)**:
   - Thống kê tổng số thành viên (`Total Users`), tổng số bài viết (`Total Posts`).
   - Bảng danh sách bài viết xuất bản gần đây kèm số lượt đọc và tương tác.
2. **Quản lý người dùng (`/admin/users`)**:
   - Xem toàn bộ danh sách thành viên trong hệ thống kèm thông tin vai trò (`ROLE_ADMIN`, `ROLE_USER`).
3. **Quản lý & Kiểm duyệt bài viết (`/admin/posts`)**:
   - Xem tất cả bài viết của mọi tác giả, tìm kiếm bài viết, xóa bỏ nội dung vi phạm.
4. **Quản lý Danh mục & Thẻ (`/admin/categories-tags`)**:
   - Thêm mới danh mục chủ đề (Category), tạo thẻ tag mới.
   - Phân quyền nghiêm ngặt: Chỉ tài khoản có `ROLE_ADMIN` mới được phép gọi các API thêm/sửa/xóa danh mục (`POST /categories`, `POST /tags`). User thường gọi sẽ bị Spring Security chặn với mã `403 Forbidden`.

---

## 4. THIẾT KẾ CƠ SỞ DỮ LIỆU & MỐI QUAN HỆ THỰC THỂ (ORM ERD)

Cơ sở dữ liệu bao gồm **9 bảng chính** được ánh xạ thông qua JPA Entities:

```text
       ┌──────────────┐                 ┌──────────────┐
       │  CATEGORIES  │ 1             N │    BLOGS     │ N           M ┌──────────────┐
       │  (id, name)  ├─────────────────┤  (id, title, ├───────────────┤     TAGS     │
       └──────────────┘                 │ content, ...)│ (blog_tags)   │  (id, name)  │
                                        └───┬──────┬───┘               └──────────────┘
                                          N │      │ 1
                                            │      │
                      ┌─────────────────────┼──────┴──────────────────────┐
                      │ 1                   │ 1                           │ 1
               ┌──────┴───────┐      ┌──────┴───────┐              ┌──────┴───────┐
               │   COMMENTS   │      │  BLOG_LIKES  │              │  BOOKMARKS   │
               │ (id, content)│      │  (id, dates) │              │  (id, dates) │
               └──────┬───────┘      └──────┬───────┘              └──────┬───────┘
                    N │                   N │                           N │
                      └─────────────────────┼─────────────────────────────┘
                                            │ 1
                                     ┌──────┴───────┐
                                     │    USERS     │
                                     │ (id, username│
                                     │ password...) │
                                     └──┬────────┬──┘
                                      1 │      1 │
                         ┌──────────────┘        └──────────────┐
                       N │                                    N │
                ┌────────┴──────┐                        ┌──────┴───────┐
                │  USER_ROLES   │                        │USER_FOLLOWS  │
                │  (user_id,    │                        │(follower_id, │
                │   role)       │                        │following_id) │
                └───────────────┘                        └──────────────┘
```

### Chi tiết các thực thể (Entities):
1. **`User` (bảng `users`)**: Lưu thông tin tài khoản, mật khẩu đã băm BCrypt, email, bio, avatarUrl. Khóa chính dạng `UUID`.
2. **`user_roles` (bảng phụ `@ElementCollection`)**: Lưu các vai trò quyền hạn (`ADMIN`, `USER`) của người dùng.
3. **`Blog` (bảng `blogs`)**: Lưu tiêu đề, nội dung HTML dài (`LONGTEXT`), ảnh bìa banner, trạng thái bản nháp (`draft`), ngày xuất bản.
4. **`Category` (bảng `categories`)**: Danh mục bài viết (Công nghệ, Lập trình, Thiết kế web,...).
5. **`Tag` (bảng `tags`)**: Thẻ gắn cho bài viết.
6. **`blog_tags` (bảng trung gian N - N)**: Liên kết giữa `blogs` và `tags`.
7. **`Comment` (bảng `comments`)**: Lưu nội dung bình luận, tác giả bình luận và bài viết được bình luận.
8. **`BlogLike` (bảng `blog_likes`)**: Lưu lượt thích bài viết của người dùng (ràng buộc duy nhất 1 like / user / blog).
9. **`Bookmark` (bảng `bookmarks`)**: Lưu danh sách bài viết được đánh dấu yêu thích.
10. **`UserFollow` (bảng `user_follows`)**: Quan hệ theo dõi giữa hai người dùng (`follower` $\leftrightarrow$ `following`).
11. **`Notification` (bảng `notifications`)**: Lưu thông báo tương tác (loại thông báo, nội dung, đường dẫn liên kết, trạng thái đã đọc).

---

## 5. CẤU TRÚC PHÂN TẦNG SOURCE CODE THỰC TẾ (`blog-website-main`)

```text
com.group.blog
├── config/                          # Các lớp cấu hình hệ thống
│   ├── ApplicationInitConfig.java   # Khởi tạo CSDL mẫu (4 Users, 4 Categories, 5 Tags, 3 Blogs)
│   ├── CloudinaryConfig.java        # Cấu hình kết nối API lưu trữ ảnh Cloudinary
│   └── SecurityConfig.java         # Cấu hình Spring Security, JWT Decoder, CORS, CSRF, Phân quyền
│
├── controller/                      # Tầng Điều khiển tiếp nhận Request
│   ├── AdminController.java         # REST API quản trị (/api/admin/stats)
│   ├── AuthenticationController.java# REST API xác thực (/auth/login, /auth/introspect)
│   ├── BlogController.java          # REST API bài viết (/blogs/**)
│   ├── CategoryController.java      # REST API danh mục (/categories/**)
│   ├── FollowController.java        # REST API theo dõi tác giả (/follows/**)
│   ├── InteractionController.java   # REST API like, comment, bookmark (/interactions/**)
│   ├── NotificationController.java  # REST API thông báo (/api/notifications/**)
│   ├── TagController.java           # REST API thẻ tag (/tags/**)
│   ├── UploadController.java        # REST API upload ảnh lên Cloudinary (/upload/**)
│   ├── UserController.java          # REST API quản lý người dùng (/users/**)
│   └── ViewController.java          # Điều hướng 16 trang giao diện Thymeleaf HTML
│
├── dto/                             # Data Transfer Objects (Truyền tải dữ liệu)
│   ├── request/                     # DTO nhận dữ liệu gửi lên từ Client
│   │   ├── ApiResponse.java         # Cấu trúc chuẩn JSON trả về {code, message, result}
│   │   ├── AuthenticationRequest.java
│   │   ├── BlogCreationRequest.java
│   │   ├── BlogUpdateRequest.java
│   │   ├── PasswordChangeRequest.java
│   │   └── UserCreatetionRequest.java
│   └── response/                    # DTO định dạng dữ liệu trả về cho Client
│       ├── AuthenticationResponse.java
│       ├── BlogResponse.java
│       ├── CategoryResponse.java
│       └── UserResponse.java
│
├── entity/                          # Các thực thể JPA ánh xạ CSDL
│   ├── Blog.java
│   ├── BlogLike.java
│   ├── BlogView.java
│   ├── Bookmark.java
│   ├── Category.java
│   ├── Comment.java
│   ├── Notification.java
│   ├── Tag.java
│   ├── User.java
│   └── UserFollow.java
│
├── enums/                           # Hằng số hệ thống
│   └── Role.java                    # Phân quyền (ADMIN, USER)
│
├── exception/                       # Xử lý ngoại lệ tập trung
│   ├── AppException.java            # Custom Exception của dự án
│   ├── ErrorCode.java               # Bảng mã lỗi chuẩn (1000 - 9999)
│   └── GlobalExceptionHandler.java  # @ControllerAdvice bắt lỗi toàn cục
│
├── mapper/                          # MapStruct Interface (Mapping Entity <-> DTO)
│   ├── BlogMapper.java
│   ├── CategoryMapper.java
│   ├── CommentMapper.java
│   └── UserMapper.java
│
├── repository/                      # Tầng tương tác CSDL Spring Data JPA
│   ├── BlogLikeRepository.java
│   ├── BlogRepository.java
│   ├── CategoryRepository.java
│   ├── CommentRepository.java
│   ├── NotificationRepository.java
│   ├── TagRepository.java
│   └── UserRepository.java
│
└── service/                         # Tầng xử lý logic nghiệp vụ cốt lõi
    ├── AdminService.java
    ├── AuthenticationService.java
    ├── BlogService.java
    ├── CategoryService.java
    ├── CloudinaryService.java
    ├── FollowService.java
    ├── InteractionService.java
    ├── NotificationService.java
    ├── TagService.java
    └── UserService.java
```

---

## 6. DỮ LIỆU KHỞI TẠO MẪU (SEED DATA SẴN CÓ ĐỂ DEMO)

Hệ thống được thiết lập sẵn bộ dữ liệu mẫu khởi chạy tự động qua `ApplicationInitConfig.java` để phục vụ demo ngay mà không cần nhập tay:

| STT | Username | Mật khẩu chung | Quyền hạn (Roles) | Họ tên thành viên / Ghi chú |
| :---: | :--- | :---: | :--- | :--- |
| 1 | **`admin`** | **`123456`** | `ROLE_ADMIN`, `ROLE_USER` | Quản trị viên cao nhất hệ thống |
| 2 | **`duonghd`** | **`123456`** | `ROLE_USER` | Tác giả: **Hoàng Đại Dương (MSSV: 24743991)** |
| 3 | **`dungnt`** | **`123456`** | `ROLE_USER` | Tác giả: **Nguyễn Trung Dũng (MSSV: 24000905)** |
| 4 | **`longlt`** | **`123456`** | `ROLE_USER` | Tác giả: **Lê Thành Long (MSSV: 23630851)** |

* **Danh mục có sẵn**: `Technology` (Công nghệ), `Programming` (Lập trình), `Web Design` (Thiết kế Web), `Life & Tips` (Đời sống & Thủ thuật).
* **Thẻ Tag có sẵn**: `Java`, `SpringBoot`, `Frontend`, `UI/UX`, `Database`.
* **Bài viết mẫu**: 3 bài viết chuyên sâu về kiến trúc Spring Boot, thiết kế cơ sở dữ liệu và bảo mật JWT.

---

## 7. KẾT QUẢ KIỂM THỬ HỆ THỐNG (TEST RESULTS)

* **Trạng thái kiểm thử tự động**: **Đạt 48/48 Testcase (100% PASS)** thông qua kịch bản kiểm thử toàn diện `test_suite.ps1`.
* **16/16 Trang Giao diện người dùng & Quản trị**: Hoạt động ổn định, trả về mã **`200 OK`**.
* **Bảo mật & Phân quyền**: Ngăn chặn chính xác các truy cập trái phép bằng mã **`403 Forbidden`**.
* **Độ bền dữ liệu**: Cơ chế **H2 Persistent File Database** bảo toàn 100% dữ liệu tài khoản, bài viết, lượt tương tác qua mọi lần tắt và khởi động lại ứng dụng.

---

## 8. HỆ THỐNG TÀI LIỆU ĐI KÈM DỰ ÁN

Để phục vụ tốt nhất cho quá trình chấm điểm và bảo vệ đồ án, nhóm đã chuẩn bị đầy đủ bộ 3 tài liệu:
1. 📄 **[README.md](blog-website-main/README.md)**: Tóm tắt thông tin đề tài, hướng dẫn cài đặt nhanh và liên kết tài liệu.
2. 📄 **[HUONG_DAN_CHAY_VA_TEST.md](blog-website-main/HUONG_DAN_CHAY_VA_TEST.md)**: Hướng dẫn import và chạy trên Eclipse, kịch bản 8 module kiểm thử chi tiết từng chức năng.
3. 🎓 **[GIAI_THICH_CHI_TIET_CODE_VAN_DAP.md](blog-website-main/GIAI_THICH_CHI_TIET_CODE_VAN_DAP.md)**: Cẩm nang phân tích chi tiết từng dòng code cốt lõi, cơ chế bảo mật JWT, JPA ORM và bộ câu hỏi vấn đáp chuẩn điểm 10 từ Giảng viên.
