# 📖 HƯỚNG DẪN CẤU HÌNH, CHẠY & BÁO CÁO KIỂM THỬ TOÀN DIỆN (FULL SYSTEM TEST REPORT)

> **Dự án**: Website Blog & Nền tảng Viết bài trực tuyến (BTL Môn Công nghệ Web & Website Hướng Dữ Liệu - IUH)  
> **Nhóm thực hiện**: 
> 1. **24743991** — Hoàng Đại Dương
> 2. **24000905** — Nguyễn Trung Dũng
> 3. **23630851** — Lê Thành Long  
> **Công nghệ**: Spring Boot 3.5, Java 21, Spring Security (JWT), Spring Data JPA, **H2 File-based Persistent Database (Lưu trữ vĩnh viễn trên ổ cứng)**, MapStruct, Lombok, HTML5/CSS3/JavaScript (Bootstrap 5, Tailwind CSS, jQuery).

---

## 🗄️ 1. CƠ SỞ DỮ LIỆU LƯU TRỮ VĨNH VIỄN (PERSISTENT STORAGE)

* **Cơ chế lưu trữ**: Sử dụng **H2 Database dạng File** lưu trực tiếp tại thư mục dự án `data/blogdb.mv.db`.
* **Ưu điểm**:
  - Không cần cài đặt MySQL Server, XAMPP hay Docker.
  - **Dữ liệu được lưu vĩnh viễn 100%** vào file vật lý trên ổ cứng.
  - Khởi động lại ứng dụng, tắt máy tính hoặc reset IDE thì toàn bộ tài khoản, bài viết, like, bình luận **vẫn còn nguyên vẹn**.
* **Truy cập H2 Web Console**:
  - Đường dẫn: [http://localhost:8080/h2-console](http://localhost:8080/h2-console)
  - **Driver Class**: `org.h2.Driver`
  - **JDBC URL**: `jdbc:h2:file:./data/blogdb`
  - **User Name**: `sa`
  - **Password**: *(Để trống)*

---

## 📊 2. KẾT QUẢ KIỂM THỬ TỰ ĐỘNG TOÀN HỆ THỐNG (TEST RESULTS: 48/48 PASS - 100%)

```text
================ TEST SUMMARY ================
Total Tests: 48 | Passed: 48 (100%) | Failed: 0
==============================================
```

### Chi tiết các nhóm kiểm thử:
1. **Giao diện người dùng & Admin (16/16 Trang `200 OK`)**:
   - `GET /` (Trang chủ) $\rightarrow$ `200 OK`
   - `GET /login` (Đăng nhập) $\rightarrow$ `200 OK`
   - `GET /register` (Đăng ký tài khoản) $\rightarrow$ `200 OK`
   - `GET /forgot-password` (Quên mật khẩu) $\rightarrow$ `200 OK`
   - `GET /change-password` (Đổi mật khẩu) $\rightarrow$ `200 OK`
   - `GET /post` (Chi tiết bài viết) $\rightarrow$ `200 OK`
   - `GET /blog-editor` (Trình soạn thảo bài viết) $\rightarrow$ `200 OK`
   - `GET /user-profile` (Hồ sơ người dùng) $\rightarrow$ `200 OK`
   - `GET /edit-profile` (Chỉnh sửa hồ sơ) $\rightarrow$ `200 OK`
   - `GET /saved-blogs` (Bài viết đã lưu) $\rightarrow$ `200 OK`
   - `GET /notifications` (Trung tâm thông báo) $\rightarrow$ `200 OK`
   - `GET /manage-blogs` (Quản lý bài viết cá nhân) $\rightarrow$ `200 OK`
   - `GET /admin/dashboard` (Admin - Bảng điều khiển thống kê) $\rightarrow$ `200 OK`
   - `GET /admin/posts` (Admin - Quản lý bài viết) $\rightarrow$ `200 OK`
   - `GET /admin/users` (Admin - Quản lý người dùng) $\rightarrow$ `200 OK`
   - `GET /admin/categories-tags` (Admin - Quản lý danh mục & thẻ tag) $\rightarrow$ `200 OK`

2. **Các thành phần HTML Tĩnh & Assets (15/15 `200 OK`)**:
   - Fragments: `navbar.html`, `hero.html`, `footer.html`, `sidebar.html`, `admin_sidebar.html`, `dashboard-sidebar.html`.
   - Assets: `main.css`, `app.js`, `posts.js`, `sidebar.js`, `filters.js`, `nav.js`, `auth.js`, `init.js`, `pages.js`.

3. **Xác thực & Phân quyền (Authentication & Authorization)**:
   - Đăng nhập 4 tài khoản có sẵn: `admin`, `duonghd`, `dungnt`, `longlt` (Mật khẩu: `123456`) $\rightarrow$ Cấp JWT Token thành công.
   - Đăng ký thành viên mới $\rightarrow$ Lưu Database và mã hóa BCrypt thành công.
   - Tự động đăng nhập cho thành viên mới $\rightarrow$ Thành công.
   - Phân quyền Admin: User thường truy cập API Admin `/api/admin/stats` bị chặn với mã `403 Forbidden` (Đúng chuẩn bảo mật).

4. **Nghiệp vụ Blog & Dữ liệu**:
   - `GET /categories` (4 Danh mục) & `GET /tags` (5 Tags) $\rightarrow$ Thành công.
   - `GET /blogs/filter` & `GET /blogs/search` $\rightarrow$ Trả về danh sách bài viết kèm lượt thích, lượt xem, tác giả và tag.
   - `POST /blogs` (Tạo bài viết mới) $\rightarrow$ Sinh UUID và lưu file CSDL thành công.
   - `GET /blogs/{id}` (Đọc bài viết) $\rightarrow$ Tăng biến đếm lượt xem (Views) thành công.
   - `GET /api/notifications` $\rightarrow$ Trả về danh sách thông báo tương tác thành công.

---

## 📌 3. CẤU HÌNH & CHẠY DỰ ÁN TRÊN ECLIPSE

### 1. Yêu cầu môi trường
* **JDK**: Java 21 (hoặc Java 17+).
* **Eclipse**: Eclipse IDE for Enterprise Java and Web Developers.
* **Lombok Plugin**: Đã cài đặt trong `eclipse.ini` (`-javaagent:...lombok.jar`).

### 2. Các bước Import vào Eclipse
1. Mở Eclipse $\rightarrow$ **File** $\rightarrow$ **Import...**
2. Chọn **Maven** $\rightarrow$ **Existing Maven Projects** $\rightarrow$ **Next**.
3. Tại ô **Root Directory**, Browse đến thư mục:
   `D:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\btl\blog-website-main`
4. Bấm **Finish**.
5. **Cập nhật Maven (Bắt buộc)**:
   * Chuột phải vào tên Project (`blog-website`) $\rightarrow$ **Maven** $\rightarrow$ **Update Project...** (`Alt + F5`).
   * Tick vào ô **Force Update of Snapshots/Releases** $\rightarrow$ Bấm **OK**.

### 3. Chạy Ứng Dụng
* **Cách 1 (Từ Eclipse)**: Mở file `src/main/java/com/group/blog/BlogWebsiteApplication.java` $\rightarrow$ Chuột phải chọn **Run As** $\rightarrow$ **Java Application** (hoặc **Spring Boot App**).
* **Cách 2 (Từ Terminal / CMD)**:
  ```powershell
  .\mvnw.cmd spring-boot:run
  ```

---

## 👥 4. TÀI KHOẢN MẪU CÓ SẴN (Tất cả mật khẩu: `123456`)

| Username | Mật khẩu | Quyền hạn (Roles) | Ghi chú |
| :--- | :---: | :--- | :--- |
| **`admin`** | `123456` | `ROLE_ADMIN`, `ROLE_USER` | Quản trị viên cao nhất của hệ thống |
| **`duonghd`** | `123456` | `ROLE_USER` | Tác giả: Hoàng Đại Dương (MSSV: 24743991) |
| **`dungnt`** | `123456` | `ROLE_USER` | Tác giả: Nguyễn Trung Dũng (MSSV: 24000905) |
| **`longlt`** | `123456` | `ROLE_USER` | Tác giả: Lê Thành Long (MSSV: 23630851) |

---

## 🧪 5. HƯỚNG DẪN TEST CÁC TÍNH NĂNG TRÊN TRÌNH DUYỆT

### 1. Test Trang chủ ([http://localhost:8080/](http://localhost:8080/))
- Xem 3 bài viết mẫu có sẵn với hình ảnh, tác giả, ngày đăng, danh mục, tag.
- Chọn bộ lọc bên phải (*Stories from all interests*) để lọc bài theo chủ đề.
- Chọn sắp xếp (*Newest First*, *Oldest First*, *Title A-Z*).
- Nhập từ khóa vào ô tìm kiếm ở Navbar (Ví dụ: `Spring`) $\rightarrow$ Bấm Enter để tìm bài.

### 2. Test Đăng nhập ([http://localhost:8080/login](http://localhost:8080/login))
- Nhập `admin` / `123456` $\rightarrow$ Bấm **Đăng nhập**.
- Quan sát thông báo xanh và trang tự chuyển về Trang chủ.
- Navbar xuất hiện avatar, tên tài khoản `admin` và nút **Admin Controller**.

### 3. Test Trang Quản trị Admin ([http://localhost:8080/admin/dashboard](http://localhost:8080/admin/dashboard))
- Bấm nút **Admin Controller** trên Navbar (hoặc truy cập trực tiếp link trên).
- Xem số liệu thống kê: Tổng số người dùng, tổng số bài viết, danh sách bài viết gần đây.
- Chuyển sang menu **Users** để xem toàn bộ danh sách thành viên.
- Chuyển sang menu **Categories & Tags** để thêm/sửa/xóa danh mục và tag.

### 4. Test Viết bài mới ([http://localhost:8080/blog-editor](http://localhost:8080/blog-editor))
- Bấm nút **Write** trên Navbar.
- Nhập tiêu đề, chọn danh mục, gắn tags và viết nội dung $\rightarrow$ Bấm **Publish**.
- Bài viết mới lập tức xuất hiện trên trang chủ và bảng điều khiển cá nhân.

---

## 📁 6. CHẠY LẠI SUITE KIỂM THỬ TỰ ĐỘNG
```powershell
pwsh -File test_suite.ps1
```
