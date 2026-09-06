# HƯỚNG DẪN CHẠY BÀI TẬP: b5_basic_web

Dự án này là bài tập thực hành Spring Boot Web + Thymeleaf hiển thị danh sách sản phẩm và giao diện Admin Dashboard (được clone từ repository `github.com/baphuc/basic_web`).

---

## 1. THÔNG TIN DỰ ÁN & CỔNG CHẠY
- **Loại dự án**: Maven Spring Boot (Java 17).
- **Cổng Server (Port)**: `8081` (Cấu hình trong `src/main/resources/application.properties`).
- **File chạy chính (Main Class)**: `src/main/java/com/example/basic_web/BasicWebApplication.java`.

---

## 2. HƯỚNG DẪN MỞ & CHẠY TRONG ECLIPSE

### Bước 1: Mở dự án trên Eclipse (Nếu chưa thấy trên Package Explorer)
1. Chọn menu: **File** ➔ **Import...** (hoặc chuột phải vào khoảng trống Package Explorer ➔ chọn **Import...**).
2. Chọn **General** ➔ **Existing Projects into Workspace** ➔ bấm **Next**.
3. Tại mục **Select root directory**, bấm **Browse...** chọn thư mục:
   `d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\t2\b5_basic_web`
4. Bấm **Finish**.

### Bước 2: Khởi động ứng dụng
1. Trong Package Explorer, mở theo đường dẫn:
   `b5_basic_web` ➔ `src/main/java` ➔ `com.example.basic_web` ➔ **`BasicWebApplication.java`**.
2. Nhấp chuột phải vào file `BasicWebApplication.java` ➔ chọn **Run As** ➔ **Spring Boot App** (hoặc **Java Application**).
3. Quan sát cửa sổ **Console** phía dưới, khi thấy dòng:
   `Started BasicWebApplication in ... seconds (process running for ...)`
   là ứng dụng đã khởi động thành công trên cổng **8081**!

---

## 3. CÁC ĐƯỜNG DẪN (URL) TRUY CẬP TRÊN TRÌNH DUYỆT

Mở trình duyệt (Chrome/Edge), truy cập:
- **Trang chủ (Tự chuyển hướng sang danh sách sản phẩm)**:
  `http://localhost:8081/`
- **Xem bảng danh sách sản phẩm (Thymeleaf `th:each`)**:
  `http://localhost:8081/products`
- **Xem giao diện Admin Dashboard**:
  `http://localhost:8081/dashboard`
- **Xem trang demo tương tác chọn dòng dữ liệu**:
  `http://localhost:8081/table-demo`

---

## 4. CHẠY BẰNG DÒNG LỆNH (TERMINAL / CMD) - KHÔNG CẦN ECLIPSE
Mở PowerShell tại thư mục `b5_basic_web` và gõ lệnh:
```powershell
mvn spring-boot:run
```
Sau đó truy cập `http://localhost:8081/` trên trình duyệt.
