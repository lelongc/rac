# HƯỚNG DẪN CHẠY BÀI TẬP: b6_independent_web

Dự án này là bài tập thực hành Spring Boot Web + Thymeleaf mô phỏng mối quan hệ 1-Nhiều (Khoa & Sinh Viên) kèm kỹ thuật định tuyến động `@PathVariable` (được clone từ repository `github.com/baphuc/independent_web`).

---

## 1. THÔNG TIN DỰ ÁN & CỔNG CHẠY
- **Loại dự án**: Maven Spring Boot (Java 17).
- **Cổng Server (Port)**: `8082` (Cấu hình trong `src/main/resources/application.properties`).
- **File chạy chính (Main Class)**: `src/main/java/com/example/independent_web/IndependentWebApplication.java`.

---

## 2. HƯỚNG DẪN MỞ & CHẠY TRONG ECLIPSE

### Bước 1: Mở dự án trên Eclipse (Nếu chưa thấy trên Package Explorer)
1. Chọn menu: **File** ➔ **Import...** (hoặc chuột phải vào khoảng trống Package Explorer ➔ chọn **Import...**).
2. Chọn **General** ➔ **Existing Projects into Workspace** ➔ bấm **Next**.
3. Tại mục **Select root directory**, bấm **Browse...** chọn thư mục:
   `d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\t2\b6_independent_web`
4. Bấm **Finish**.

### Bước 2: Khởi động ứng dụng
1. Trong Package Explorer, mở theo đường dẫn:
   `b6_independent_web` ➔ `src/main/java` ➔ `com.example.independent_web` ➔ **`IndependentWebApplication.java`**.
2. Nhấp chuột phải vào file `IndependentWebApplication.java` ➔ chọn **Run As** ➔ **Spring Boot App** (hoặc **Java Application**).
3. Quan sát cửa sổ **Console** phía dưới, khi thấy dòng:
   `Started IndependentWebApplication in ... seconds (process running for ...)`
   là ứng dụng đã khởi động thành công trên cổng **8082**!

---

## 3. CÁC ĐƯỜNG DẪN (URL) TRUY CẬP TRÊN TRÌNH DUYỆT

Mở trình duyệt (Chrome/Edge), truy cập:
- **Trang chủ (Tự chuyển hướng sang danh sách các khoa)**:
  `http://localhost:8082/`
- **Xem danh sách các khoa**:
  `http://localhost:8082/faculties`
- **Xem danh sách sinh viên Khoa Công Nghệ Thông Tin (Khoa ID = 1)**:
  `http://localhost:8082/faculties/1/students`
- **Xem danh sách sinh viên Khoa Kỹ Thuật Cơ Khí (Khoa ID = 2)**:
  `http://localhost:8082/faculties/2/students`

---

## 4. CHẠY BẰNG DÒNG LỆNH (TERMINAL / CMD) - KHÔNG CẦN ECLIPSE
Mở PowerShell tại thư mục `b6_independent_web` và gõ lệnh:
```powershell
mvn spring-boot:run
```
Sau đó truy cập `http://localhost:8082/` trên trình duyệt.
