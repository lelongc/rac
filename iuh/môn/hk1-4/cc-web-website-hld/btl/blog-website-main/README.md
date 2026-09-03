# 🌐 Blog Platform — Website Blog & Nền Tảng Viết Bài Trực Tuyến

> Dự án Bài Tập Lớn môn **Công nghệ Web và Website hướng dữ liệu** — Trường Đại học Công nghiệp TP.HCM (IUH).

---

## 👥 THÀNH VIÊN NHÓM THỰC HIỆN
1. **24743991** — Hoàng Đại Dương
2. **24000905** — Nguyễn Trung Dũng
3. **23630851** — Lê Thành Long

---

## 🏆 KẾT QUẢ KIỂM THỬ HỆ THỐNG
* **Trạng thái kiểm thử**: **`48 / 48 PASS (100%)`**
* **16/16 Trang Giao diện**: `200 OK`
* **Lưu trữ CSDL**: **H2 Persistent File Database** (`./data/blogdb.mv.db`) — **Lưu vĩnh viễn trên ổ cứng, không bao giờ mất dữ liệu khi khởi động lại!**

---

## ⚡ HƯỚNG DẪN NHANH (QUICK START)

1. **Khởi chạy ứng dụng**:
   * Trong Eclipse: Chạy class `com.group.blog.BlogWebsiteApplication` (`Run As -> Java Application`).
   * Hoặc qua Terminal: `.\mvnw.cmd spring-boot:run`
2. **Truy cập Giao diện Web**:
   * Trang chủ: [http://localhost:8080/](http://localhost:8080/)
   * Đăng nhập: [http://localhost:8080/login](http://localhost:8080/login)
   * Quản trị Admin: [http://localhost:8080/admin/dashboard](http://localhost:8080/admin/dashboard)
   * Viết bài mới: [http://localhost:8080/blog-editor](http://localhost:8080/blog-editor)
3. **Cơ sở dữ liệu H2 Console**:
   * Đường dẫn: [http://localhost:8080/h2-console](http://localhost:8080/h2-console)
   * **JDBC URL**: `jdbc:h2:file:./data/blogdb` | **User**: `sa` | **Password**: *(để trống)*
4. **Tài khoản đăng nhập có sẵn** *(Mật khẩu chung: `123456`)*:
   * **Admin**: `admin` / `123456`
   * **Tác giả**: `duonghd` / `123456`, `dungnt` / `123456`, `longlt` / `123456`

---

📚 **TÀI LIỆU HỖ TRỢ BẢO VỆ BÀI TẬP LỚN (BTL)**:  
* 📄 **[HUONG_DAN_CHAY_VA_TEST.md](HUONG_DAN_CHAY_VA_TEST.md)**: Hướng dẫn chạy Eclipse, 48 kịch bản kiểm thử chi tiết từng chức năng.
* 🎓 **[GIAI_THICH_CHI_TIET_CODE_VAN_DAP.md](GIAI_THICH_CHI_TIET_CODE_VAN_DAP.md)**: Giải thích chi tiết từng dòng code cốt lõi, kiến trúc 3 lớp, JWT Security, JPA Entities và **Bộ câu hỏi vấn đáp chuẩn điểm 10** từ Giảng viên.
