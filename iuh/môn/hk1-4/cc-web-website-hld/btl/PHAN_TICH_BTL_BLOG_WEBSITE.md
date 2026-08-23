# 📋 BÁO CÁO PHÂN TÍCH ĐỀ TÀI BÀI TẬP LỚN
## ĐỀ TÀI: XÂY DỰNG BLOG WEBSITE - DIỄN ĐÀN TRỰC TUYẾN
**Môn học:** Công nghệ web và website hướng dữ liệu  
**Đơn vị:** Trường Đại học Công Nghiệp TP. Hồ Chí Minh (IUH) - Khoa Công nghệ Thông tin  

### 👥 THÀNH VIÊN NHÓM THỰC HIỆN:
1. **24743991 - Hoàng Đại Dương**
2. **24000905 - Nguyễn Trung Dũng**
3. **23630851 - Lê Thành Long**

---

## 1. TỔNG QUAN HỆ THỐNG VÀ MỤC TIÊU ĐỀ TÀI
Hệ thống **Blog Website - Diễn đàn trực tuyến** là một nền tảng mạng xã hội thu nhỏ cho phép người dùng chia sẻ kiến thức, viết bài blog, tương tác cộng đồng (bình luận, thả tim, đánh dấu bài viết yêu thích) và cho phép ban quản trị (Admin) kiểm duyệt nội dung, phân quyền tài khoản.

---

## 2. KIẾN TRÚC VÀ CÔNG NGHỆ SỬ DỤNG
Dự án được xây dựng theo kiến trúc phân tầng chuẩn doanh nghiệp (Layered Architecture):

- **Backend Framework**: **Java 21**, **Spring Boot 3.5.x** (Mô hình MVC & RESTful API).
- **Cơ sở dữ liệu (Database)**: **MySQL 8.0** kết hợp **Spring Data JPA (Hibernate)** quản lý ORM.
- **Bảo mật & Phân quyền**: **Spring Security 6**, xác thực Token **JWT (Nimbus-JOSE-JWT)**, **OAuth2 Resource Server**.
- **Lưu trữ đa phương tiện**: Tích hợp **Cloudinary API** phục vụ upload và quản lý hình ảnh đám mây.
- **Thư viện tối ưu mã nguồn**: **Lombok** (giảm thiểu getter/setter), **MapStruct** (tự động mapping DTO ↔ Entity).
- **Giao diện (Frontend)**: **Thymeleaf Template Engine**, HTML5, CSS3, JavaScript tương tác AJAX bất đồng bộ.

---

## 3. CÁC TÍNH NĂNG CHÍNH CỦA HỆ THỐNG

### 👤 Phía Người Dùng (Member / User):
1. **Xác thực tài khoản**: Đăng ký, Đăng nhập bảo mật JWT, Đổi mật khẩu, Cập nhật thông tin cá nhân (Avatar, Tiểu sử).
2. **Quản lý bài viết**: Soạn thảo bài viết mới (hỗ trợ định dạng, chọn danh mục, gắn thẻ Tag, tải ảnh đại diện bài viết), lưu bản nháp, xuất bản bài viết công khai.
3. **Tương tác cộng đồng**: Thả tim (Like/Unlike), Bình luận đa cấp, Lưu bài viết vào danh sách yêu thích cá nhân.
4. **Tìm kiếm & Bộ lọc**: Tìm kiếm bài viết theo từ khóa, lọc theo danh mục (Category) và thẻ (Tag) theo thời gian thực.

### 🛡️ Phía Quản Trị Viên (Admin):
1. **Quản lý người dùng**: Xem danh sách thành viên, khóa tài khoản vi phạm chính sách, phân quyền quản trị.
2. **Kiểm duyệt bài viết**: Duyệt bài viết mới trước khi hiển thị công khai, gỡ bỏ nội dung không phù hợp vào thùng rác.
3. **Quản lý danh mục & Thẻ**: Thêm, sửa, xóa, gộp nhóm danh mục và tag.
4. **Dashboard Thống kê**: Thống kê số lượng bài viết, lượt tương tác, thành viên mới theo thời gian.

---

## 4. CẤU TRÚC PHÂN TẦNG SOURCE CODE (`blog-website-main`)
```text
com.group.blog
├── config/          # Cấu hình Spring Security, JWT, Cloudinary, Web MVC
├── controller/      # Tiếp nhận Request từ Client (AuthController, PostController, AdminController...)
├── dto/             # Đối tượng truyền tải dữ liệu Request / Response
├── entity/          # Các thực thể ánh xạ CSDL (User, Post, Comment, Category, Tag, Like...)
├── enums/           # Định nghĩa các hằng số (Role, PostStatus...)
├── exception/       # Xử lý lỗi tập trung (GlobalExceptionHandler)
├── mapper/          # MapStruct Interface chuyển đổi DTO và Entity
├── repository/      # Tương tác MySQL qua Spring Data JPA
└── service/         # Xử lý nghiệp vụ logic chính
```
