# 📖 HƯỚNG DẪN CHẠY & TEST DỰ ÁN BLOG WEBSITE TRÊN ECLIPSE

> **Dự án**: Website Blog & Nền tảng Viết bài trực tuyến (BTL Môn Công nghệ Web & Website Hướng Dữ Liệu - IUH)  
> **Công nghệ**: Spring Boot 3.5, Java 21, Spring Security (JWT), Spring Data JPA, H2 In-Memory Database (MySQL Mode), MapStruct, Lombok, HTML5/CSS3/JavaScript (Bootstrap 5, jQuery).

---

## 📌 PHẦN 1: CẤU HÌNH & IMPORT DỰ ÁN TRÊN ECLIPSE

### 1. Yêu cầu môi trường
* **JDK**: Java 21 hoặc Java 17 trở lên.
* **Eclipse**: Eclipse IDE for Enterprise Java and Web Developers (2023-12 trở lên).
* **Lombok**: Đã cài đặt Agent vào Eclipse (`eclipse.ini`).
  > *Kiểm tra*: Trong file `eclipse.ini` có dòng `-javaagent:...lombok.jar`. Nếu chưa có, tải file `lombok.jar` và chạy lệnh `java -jar lombok.jar` để trỏ vào thư mục cài Eclipse.

### 2. Các bước Import vào Eclipse
1. Mở Eclipse $\rightarrow$ Chọn **File** $\rightarrow$ **Import...**
2. Chọn **Maven** $\rightarrow$ **Existing Maven Projects** $\rightarrow$ Bấm **Next**.
3. Tại ô **Root Directory**, bấm **Browse...** và chọn đến thư mục dự án:
   `D:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\btl\blog-website-main`
4. Tick chọn file `pom.xml` $\rightarrow$ Bấm **Finish**.
5. **Cập nhật Maven (Bắt buộc)**:
   * Click chuột phải vào tên Project (`blog-website`) trong mục *Package Explorer*.
   * Chọn **Maven** $\rightarrow$ **Update Project...** (hoặc phím tắt `Alt + F5`).
   * Tick vào ô **Force Update of Snapshots/Releases** $\rightarrow$ Bấm **OK** để Eclipse tự sinh các class Mapper (`BlogMapperImpl`, `UserMapperImpl`, `CategoryMapperImpl`).

---

## 🚀 PHẦN 2: CÁCH CHẠY DỰ ÁN (RUN APPLICATION)

### Cách 1: Chạy trực tiếp từ Eclipse (Khuyên dùng)
1. Trong cửa sổ *Package Explorer*, mở thư mục:
   `src/main/java` $\rightarrow$ `com.group.blog` $\rightarrow$ Mở file **`BlogWebsiteApplication.java`**.
2. Click **chuột phải** vào file $\rightarrow$ Chọn **Run As** $\rightarrow$ **Java Application** (hoặc **Spring Boot App**).
3. Mở tab **Console** bên dưới để quan sát log khởi động.
4. Khi thấy dòng log sau xuất hiện là ứng dụng đã chạy thành công:
   ```text
   Tomcat started on port 8080 (http) with context path '/'
   Initialized Sample Data Successfully: 4 Users, 4 Categories, 5 Tags, 3 Blogs!
   ```

### Cách 2: Chạy qua Terminal / Command Prompt
Nếu Eclipse bị kẹt tiến trình hoặc port, bạn có thể chạy bằng dòng lệnh trong thư mục dự án:
```powershell
.\mvnw.cmd spring-boot:run
```

> ⚠️ **Xử lý lỗi Port 8080 bị chiếm dụng (Port 8080 was already in use)**:
> Nếu gặp thông báo lỗi cổng 8080, mở PowerShell chạy lệnh sau để giải phóng:
> ```powershell
> Get-NetTCPConnection -LocalPort 8080 -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }
> ```

---

## 🗄️ PHẦN 3: DỮ LIỆU MẪU CÓ SẴN (SEED DATA)

Hệ thống được lập trình tự động nạp sẵn cơ sở dữ liệu mẫu khi khởi động (`ApplicationInitConfig.java`):

### 1. Danh sách Tài khoản thử nghiệm (Mật khẩu chung: `123456`)
| Username | Họ và tên | Vai trò (Role) | Chức năng |
| :--- | :--- | :--- | :--- |
| **`admin`** | Quản Trị Viên Hệ Thống | `ROLE_ADMIN`, `ROLE_USER` | Toàn quyền quản trị bài viết, danh mục, người dùng |
| **`duonghd`** | Hoàng Đại Dương | `ROLE_USER` | Tác giả viết bài, bình luận, like |
| **`dungnt`** | Nguyễn Trung Dũng | `ROLE_USER` | Tác giả viết bài, bình luận, like |
| **`longlt`** | Lê Thành Long | `ROLE_USER` | Tác giả viết bài, bình luận, like |

### 2. Danh mục & Tag mẫu
* **Danh mục (Categories)**: `Technology`, `Programming`, `Web Design`, `Life & Tips`.
* **Thẻ Tag (Tags)**: `Java`, `SpringBoot`, `Bootstrap`, `Thymeleaf`, `AI`.
* **Bài viết (Blogs)**: Có sẵn 3 bài viết lớn kèm ảnh bìa công nghệ độ phân giải cao Unsplash.

---

## 🧪 PHẦN 4: HƯỚNG DẪN TEST ĐẦY ĐỦ CÁC TÍNH NĂNG

### 1. Test Cơ Sở Dữ Liệu Trực Quan (H2 Console)
Hệ thống sử dụng H2 Database (chế độ tương thích MySQL), bạn có thể truy vấn bảng dữ liệu trực tiếp:
* **Đường dẫn**: [http://localhost:8080/h2-console](http://localhost:8080/h2-console)
* **Thông tin đăng nhập**:
  * **Driver Class**: `org.h2.Driver`
  * **JDBC URL**: `jdbc:h2:mem:blogdb` *(Lưu ý nhập chính xác URL này)*
  * **User Name**: `sa`
  * **Password**: *(Để trống - không nhập gì)*
* Bấm nút **Connect** $\rightarrow$ Bạn sẽ thấy cây thư mục gồm các bảng: `USERS`, `BLOGS`, `CATEGORIES`, `TAGS`, `COMMENTS`, `BLOG_LIKES`, `BLOG_TAGS`...

---

### 2. Test Giao Diện Người Dùng (Frontend Website)

#### A. Trang chủ (Home Page)
* **Đường dẫn**: [http://localhost:8080/](http://localhost:8080/)
* **Các mục cần kiểm tra**:
  1. **Thanh Navbar trên cùng**: Logo Inkwell, ô tìm kiếm, các nút *Sign In*, *Sign Up*, *Write*.
  2. **Banner Hero**: Khối giới thiệu nền tảng blog.
  3. **Danh sách bài viết (Cột trái)**: Hiển thị 3 bài viết mẫu có đầy đủ ảnh bìa, avatar tác giả, ngày đăng, danh mục, tags và số lượt like.
  4. **Bộ lọc & Sắp xếp (Sort)**:
     * Chọn dropdown *Sort* $\rightarrow$ Thử sắp xếp theo: *Newest First*, *Oldest First*, *Title A-Z*.
     * Nhập từ khóa vào ô tìm kiếm trên Navbar (Ví dụ: `Spring` hoặc `Thymeleaf`) $\rightarrow$ Bấm Enter để lọc bài viết.
  5. **Thanh bên (Sidebar - Cột phải)**:
     * *Stories from all interests*: Bấm vào từng danh mục (`Technology`, `Programming`...) để lọc bài tương ứng.
     * *Trending ↗*: Hiển thị danh sách các bài viết có lượt đọc nhiều nhất.

#### B. Đăng nhập & Xác thực (Authentication)
* **Đường dẫn**: [http://localhost:8080/login](http://localhost:8080/login) (hoặc bấm nút **Sign In** trên Navbar).
* **Thao tác**:
  1. Nhập `username`: `admin` và `password`: `123456`.
  2. Bấm **Đăng nhập** $\rightarrow$ Hệ thống lưu JWT Token vào `localStorage` và tự động chuyển về trang chủ.
  3. **Kết quả**: Thanh Navbar chuyển sang chế độ đã đăng nhập:
     * Hiện avatar và tên `admin`.
     * Xuất hiện nút **Dashboard / Quản trị** (dành riêng cho tài khoản Admin).
     * Bấm vào avatar để xem menu: *Profile*, *My Stories*, *Settings*, *Sign Out*.

#### C. Viết và Đăng bài mới (Blog Editor)
* **Đường dẫn**: [http://localhost:8080/blog-editor](http://localhost:8080/blog-editor) (hoặc bấm nút **Write** trên Navbar).
* **Thao tác**:
  1. Nhập tiêu đề bài viết.
  2. Chọn danh mục (Category).
  3. Nhập các thẻ Tag (cách nhau bởi dấu phẩy, ví dụ: `Java, Web, IUH`).
  4. Nhập nội dung bài viết.
  5. Bấm nút **Publish / Đăng bài** $\rightarrow$ Bài viết mới sẽ xuất hiện ngay lập tức trên trang chủ.

#### D. Đọc chi tiết bài viết, Like & Bình luận (Post Detail)
* **Thao tác**:
  1. Tại trang chủ, click vào bất kỳ bài viết nào.
  2. Trang chuyển đến `post.html?id=...`.
  3. Đọc toàn bộ nội dung bài viết, xem thông tin tác giả.
  4. Bấm nút **Tim / Like** $\rightarrow$ Số like tăng lên và lưu vào CSDL.
  5. Cuộn xuống dưới, nhập nội dung bình luận $\rightarrow$ Bấm **Gửi bình luận**.

---

### 3. Test REST API bằng Postman (Backend API)

Nếu cần kiểm tra API độc lập qua Postman:

| STT | Chức năng | Phương thức (Method) | Endpoint URL | Request Body (JSON) / Headers |
| :---: | :--- | :---: | :--- | :--- |
| 1 | **Đăng nhập lấy Token** | `POST` | `http://localhost:8080/auth/login` | `{"username": "admin", "password": "123456"}` |
| 2 | **Lấy danh sách bài viết** | `GET` | `http://localhost:8080/blogs/filter` | Không cần Token |
| 3 | **Tìm kiếm & Lọc bài viết** | `GET` | `http://localhost:8080/blogs/filter?keyword=Spring&categoryId=...` | Không cần Token |
| 4 | **Lấy danh sách Danh mục** | `GET` | `http://localhost:8080/categories` | Không cần Token |
| 5 | **Lấy danh sách Thẻ Tag** | `GET` | `http://localhost:8080/tags` | Không cần Token |
| 6 | **Tạo bài viết mới** | `POST` | `http://localhost:8080/blogs` | Header: `Authorization: Bearer <token>`<br>Body: `{"title": "...", "content": "...", "categoryId": "..."}` |
| 7 | **Like bài viết** | `POST` | `http://localhost:8080/blogs/{id}/like` | Header: `Authorization: Bearer <token>` |

---

## 🛠️ CẤU TRÚC DỰ ÁN TỔNG QUAN

```text
blog-website-main/
├── src/main/java/com/group/blog/
│   ├── config/             # Cấu hình Spring Security, CORS, JWT, Seed Data Init
│   ├── controller/         # REST Controllers & ViewController (điều hướng trang HTML)
│   ├── dto/                # Data Transfer Objects (Request / Response)
│   ├── entity/             # JPA Entities (User, Blog, Category, Tag, Comment...)
│   ├── mapper/             # MapStruct Mappers (Chuyển đổi Entity <-> DTO)
│   ├── repository/         # Spring Data JPA Repositories
│   └── service/            # Business Logic Services
├── src/main/resources/
│   ├── static/             # File tĩnh Frontend (assets/css, assets/js, fragments)
│   ├── templates/          # Thymeleaf / HTML Templates
│   └── application.properties # Cấu hình H2 Database, JWT Secret, Server Port
├── pom.xml                 # Khai báo Maven Dependencies & Compiler Plugins
└── HUONG_DAN_CHAY_VA_TEST.md # Tài liệu hướng dẫn này
```
