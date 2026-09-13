# HƯỚNG DẪN CHẠY BÀI TẬP: b6_2_faculty_crud
## HỆ THỐNG QUẢN LÝ KHOA & SINH VIÊN (FULL CRUD: THÊM, SỬA, XÓA)

Dự án này là bài tập nâng cấp toàn diện từ **Bài 6 (`b6_independent_web`)**, tích hợp trọn vẹn:
1. **Giao diện Web Thymeleaf**: Thao tác Thêm, Sửa, Xóa trực quan bằng giao diện có bảng và form đẹp mắt.
2. **Hệ thống RESTful Web Service**: Cung cấp đầy đủ các API chuẩn quốc tế (`GET`, `POST`, `PUT`, `DELETE`) trả về định dạng JSON.

---

## 1. THÔNG TIN DỰ ÁN & CỔNG CHẠY
- **Loại dự án**: Maven Spring Boot (Java 17).
- **Cổng Server (Port)**: `8083` (được cấu hình trong `src/main/resources/application.properties` để không xung đột với các bài khác).
- **File chạy chính (Main Class)**: `src/main/java/com/example/faculty_crud/FacultyCrudApplication.java`.

---

## 2. HƯỚNG DẪN MỞ & CHẠY TRONG ECLIPSE

### Bước 1: Import vào Eclipse (Nếu chưa thấy trên Package Explorer)
1. Chọn menu: **File** ➔ **Import...** (hoặc click chuột phải vào khoảng trống Package Explorer ➔ chọn **Import...**).
2. Chọn **General** ➔ **Existing Projects into Workspace** ➔ bấm **Next**.
3. Tại mục **Select root directory**, bấm **Browse...** chọn thư mục:
   `d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\t2\b6_2_faculty_crud`
4. Bấm **Finish**.

### Bước 2: Khởi động ứng dụng
1. Trong Package Explorer, mở theo đường dẫn:
   `b6_2_faculty_crud` ➔ `src/main/java` ➔ `com.example.faculty_crud` ➔ **`FacultyCrudApplication.java`**.
2. Nhấp chuột phải vào file `FacultyCrudApplication.java` ➔ chọn **Run As** ➔ **Spring Boot App** (hoặc **Java Application**).
3. Quan sát cửa sổ **Console** phía dưới, khi thấy dòng:
   `Started FacultyCrudApplication in ... seconds` và thông báo chạy tại cổng `8083` là thành công!

---

## 3. CÁC ĐƯỜNG DẪN KIỂM TRA TRÊN TRÌNH DUYỆT (GIAO DIỆN WEB)

Mở trình duyệt (Chrome/Edge), truy cập:
- **Trang chủ / Danh sách tất cả các khoa**:
  `http://localhost:8083/` hoặc `http://localhost:8083/faculties`
- **Thêm khoa mới**:
  `http://localhost:8083/faculties/new`
- **Xem danh sách sinh viên Khoa Computer Science (ID = 1)**:
  `http://localhost:8083/faculties/1/students`
- **Thêm sinh viên mới vào Khoa ID = 1**:
  `http://localhost:8083/faculties/1/students/new`

*(Trên giao diện web, mỗi dòng đều có sẵn nút **Sửa**, **Xóa**, **Danh Sách SV** để bạn nhấn thử trực tiếp!)*

---

## 4. TÀI LIỆU TEST HỆ THỐNG REST API (POSTMAN / cURL)

Bạn có thể mở Postman hoặc PowerShell để test các method REST API:

### A. CRUD Khoa (Faculty)
| Chức năng | Phương thức | Endpoint | Dữ liệu gửi lên (Body JSON) |
|---|---|---|---|
| **Xem tất cả khoa** | `GET` | `http://localhost:8083/api/faculties` | Không |
| **Xem 1 khoa** | `GET` | `http://localhost:8083/api/faculties/1` | Không |
| **Thêm khoa mới** | `POST` | `http://localhost:8083/api/faculties` | `{"name": "Khoa Dien Tu"}` |
| **Sửa tên khoa** | `PUT` | `http://localhost:8083/api/faculties/1` | `{"name": "Khoa CNTT Doi Ten"}` |
| **Xóa khoa** | `DELETE` | `http://localhost:8083/api/faculties/1` | Không |

### B. CRUD Sinh Viên Trong Khoa (Student)
| Chức năng | Phương thức | Endpoint | Dữ liệu gửi lên (Body JSON) |
|---|---|---|---|
| **Xem DSSV của khoa** | `GET` | `http://localhost:8083/api/faculties/1/students` | Không |
| **Xem 1 sinh viên** | `GET` | `http://localhost:8083/api/faculties/1/students/101` | Không |
| **Thêm sinh viên** | `POST` | `http://localhost:8083/api/faculties/1/students` | `{"name": "Nguyen Van B", "email": "b@iuh.edu.vn"}` |
| **Sửa sinh viên** | `PUT` | `http://localhost:8083/api/faculties/1/students/101` | `{"name": "Alice Johnson Edit", "email": "alice_new@cs.edu"}` |
| **Xóa sinh viên** | `DELETE` | `http://localhost:8083/api/faculties/1/students/101` | Không |

### Lệnh cURL mẫu chạy nhanh trong PowerShell:
```powershell
# 1. Lấy danh sách tất cả các khoa (JSON):
curl.exe http://localhost:8083/api/faculties

# 2. Thêm một khoa mới:
curl.exe -X POST http://localhost:8083/api/faculties -H "Content-Type: application/json" -d "{\"name\": \"Khoa Tri Tue Nhan Tao\"}"

# 3. Thêm sinh viên mới vào khoa 1:
curl.exe -X POST http://localhost:8083/api/faculties/1/students -H "Content-Type: application/json" -d "{\"name\": \"Tran Van Tien\", \"email\": \"tien@iuh.edu.vn\"}"
```

---

## 5. CHẠY BẰNG DÒNG LỆNH (TERMINAL / CMD)
Tại thư mục `b6_2_faculty_crud`, mở Terminal/PowerShell và gõ:
```powershell
mvn spring-boot:run
```
Sau đó truy cập `http://localhost:8083/` trên trình duyệt.
