# HƯỚNG DẪN HIỂN THỊ VÀ CHẠY CÁC BÀI TẬP TRÊN ECLIPSE PACKAGE EXPLORER

Tài liệu giải thích cách bật hiển thị và chạy các bài tập Spring Boot:
1. **Bài tập 1**: `b5_basic_web` (Cổng 8081 - Quản lý Sản phẩm MVC)
2. **Bài tập 2**: `b6_independent_web` (Cổng 8082 - Quản lý Khoa & Sinh viên MVC gốc)
3. **Bài tập 3**: `b6_2_faculty_crud` (Cổng 8083 - Quản lý Khoa & Sinh viên Full CRUD: Thêm, Sửa, Xóa cả Web & REST API)

---

## 1. CÁCH IMPORT CÁC BÀI TẬP VÀO ECLIPSE PACKAGE EXPLORER

Đã cấu hình sẵn đầy đủ file `.project`, `.classpath`, và `pom.xml` chuẩn Eclipse Maven cho cả 3 thư mục:

1. Trên thanh menu Eclipse: Chọn **File** -> **Import...** (hoặc click chuột phải vào khoảng trống bất kỳ trên **Package Explorer** -> chọn **Import...**).
2. Chọn **General** -> **Existing Projects into Workspace** -> bấm **Next**.
3. Tại dòng **Select root directory**, bấm nút **Browse...** -> chọn thư mục:
   `d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\t2`
4. Eclipse sẽ tự động tìm thấy và đánh dấu tick vào:
   - `[✔] b5_basic_web`
   - `[✔] b6_independent_web`
   - `[✔] b6_2_faculty_crud`
5. Bấm nút **Finish**.
👉 **Kết quả**: Cả 3 project sẽ lập tức xuất hiện ngay trên Package Explorer!

---

## 2. BẢNG TỔNG HỢP CỔNG VÀ URL TRUY CẬP

| Bài tập | Cổng (Port) | File kích hoạt (Main Class) | URL kiểm tra |
|---|---|---|---|
| **`b5_basic_web`** | `8081` | `BasicWebApplication.java` | `http://localhost:8081/products`<br>`http://localhost:8081/dashboard` |
| **`b6_independent_web`** | `8082` | `IndependentWebApplication.java` | `http://localhost:8082/faculties`<br>`http://localhost:8082/faculties/1/students` |
| **`b6_2_faculty_crud`** | `8083` | `FacultyCrudApplication.java` | **Web UI:** `http://localhost:8083/faculties`<br>**REST API:** `http://localhost:8083/api/faculties` |

