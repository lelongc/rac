# HƯỚNG DẪN CHẠY VÀ ÔN THI GIỮA KỲ: DỰ ÁN `gk`
## CHUẨN MÔ HÌNH SPRING BOOT MVC + THYMELEAF (FULL CRUD)

> **Dự án này đã được tối ưu tinh gọn 100% cho mục đích ÔN THI GIỮA KỲ:**  
> Đã **loại bỏ hoàn toàn REST API** để tránh gây nhầm lẫn. Bạn chỉ cần tập trung vào **Spring MVC + Thymeleaf** (hiển thị bảng biểu, nút Thêm, Sửa, Xóa trên trình duyệt).

---

## 1. THÔNG TIN DỰ ÁN & CỔNG CHẠY
- **Vị trí thư mục:** `d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\gk`
- **Cổng chạy (Port):** `8084` *(cấu hình trong `application.properties` để không đụng hàng với các bài cũ)*.
- **File kích hoạt chính (Main):** `src/main/java/com/example/gk/GkApplication.java`.

---

## 2. CÁCH IMPORT VÀ CHẠY TRÊN ECLIPSE (3 BƯỚC)

### Bước 1: Import vào Eclipse
1. Trong Eclipse, chọn menu **File** ➔ **Import...** (hoặc chuột phải vào khoảng trống Package Explorer ➔ chọn **Import...**).
2. Chọn **General** ➔ **Existing Projects into Workspace** ➔ bấm **Next**.
3. Tại dòng **Select root directory**, bấm **Browse...** chọn thư mục:
   `d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\gk`
4. Eclipse sẽ thấy tick chọn `[✔] gk` ➔ bấm **Finish**.

### Bước 2: Khởi động ứng dụng
1. Mở theo đường dẫn: `gk` ➔ `src/main/java` ➔ `com.example.gk` ➔ **`GkApplication.java`**.
2. Nhấp **chuột phải** vào `GkApplication.java` ➔ chọn **Run As** ➔ **Spring Boot App** (hoặc **Java Application**).
3. Khi thấy Console hiện thông báo:
   ```
   >> UNG DUNG THI GIUA KY (MVC THYMELEAF) DANG CHAY!
   >> TRUY CAP TAI CONG: http://localhost:8084/faculties
   ```
   là server đã khởi động thành công!

---

## 3. CÁC ĐƯỜNG DẪN KIỂM TRA TRÊN TRÌNH DUYỆT (CHROME / EDGE)

Mở trình duyệt, truy cập:
- **Trang chủ / Danh sách tất cả các Khoa:**
  👉 `http://localhost:8084/` hoặc `http://localhost:8084/faculties`
- **Form thêm Khoa mới:**
  👉 `http://localhost:8084/faculties/new`
- **Xem danh sách sinh viên Khoa Công Nghệ Thông Tin (ID = 1):**
  👉 `http://localhost:8084/faculties/1/students`
- **Form thêm sinh viên mới vào Khoa 1:**
  👉 `http://localhost:8084/faculties/1/students/new`

*(Trên giao diện web, mỗi dòng đều có sẵn nút **Sửa**, **Xóa**, **Xem SV** để bạn nhấn thử trực tiếp!)*

---

## 4. TẤT CẢ FILE TRONG DỰ ÁN NÀY (ĐÃ LƯỢC BỎ REST API)

Dự án chỉ còn đúng 5 file Java và 4 file HTML cực kỳ gọn gàng:

```
gk/
├── src/main/java/com/example/gk/
│   ├── GkApplication.java             <-- File main khởi động Spring Boot
│   │
│   ├── model/                         <-- TẦNG MODEL (DỮ LIỆU)
│   │   ├── Faculty.java               <-- Thực thể Khoa (id, name, students)
│   │   └── Student.java               <-- Thực thể Sinh viên (id, name, email)
│   │
│   ├── service/                       <-- TẦNG SERVICE (BẾP NẤU NGHIỆP VỤ)
│   │   └── FacultyService.java        <-- Chứa 3 khoa mẫu và các hàm Thêm/Sửa/Xóa
│   │
│   └── controller/                    <-- TẦNG CONTROLLER (TIẾP TÂN MVC)
│       └── FacultyController.java     <-- Duy nhất 1 Controller (@Controller) trả về HTML
│
└── src/main/resources/
    ├── application.properties         <-- Cấu hình port 8084
    └── templates/                     <-- TẦNG VIEW (GIAO DIỆN THYMELEAF)
        ├── faculty_list.html          <-- Bảng hiển thị danh sách các Khoa
        ├── faculty_form.html          <-- Form nhập thêm/sửa Khoa
        ├── faculty_students.html      <-- Bảng danh sách sinh viên theo Khoa
        └── student_form.html          <-- Form nhập thêm/sửa Sinh viên
```

---

## 5. TÓM TẮT 3 CÚ PHÁP THYMELEAF QUAN TRỌNG NHẤT CẦN NHỚ:

1. **`th:each="item : ${list}"`** : Vòng lặp foreach duyệt danh sách in ra từng dòng `<tr>`.
2. **`th:text="${item.name}"`** : In giá trị biến ra thẻ HTML (ví dụ tên khoa, tên sinh viên).
3. **`th:href="@{/faculties/edit/{id}(id=${f.id})}"`** : Tạo đường link động truyền mã ID vào URL.
