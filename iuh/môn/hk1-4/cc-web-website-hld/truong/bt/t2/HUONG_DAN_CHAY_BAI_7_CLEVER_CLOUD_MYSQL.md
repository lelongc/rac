# HƯỚNG DẪN CẤU HÌNH VÀ CHẠY BÀI 7: SPRING DATA JPA + MYSQL (FULL CRUD)

> **Mã bài tập**: Bài 7 - Quản lý Phòng Ban & Nhân Viên (`Department` - `Staff`)  
> **Thư mục dự án**: `d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\t2\b7_department_staff_mysql`  
> **Trạng thái Database**: ✅ **ĐÃ KẾT NỐI VÀ TEST THÀNH CÔNG VỚI CLEVER CLOUD MYSQL CỦA BẠN!**  
> **Bảng CSDL đã tạo**: `departments` và `staffs` (kèm khóa ngoại `department_id`)  
> **Dữ liệu mẫu đã có sẵn**: 4 phòng ban và 5 nhân viên mẫu trong MySQL.

---

## MỤC LỤC
1. [Thông tin Clever Cloud MySQL đã cấu hình](#1-thông-tin-clever-cloud-mysql-đã-cấu-hình)
2. [Cách xem Sơ đồ quan hệ RDB trực quan (ERD) ngay bây giờ trên phpMyAdmin](#2-cách-xem-sơ-đồ-quan-hệ-rdb-trực-quan-erd-ngay-bây-giờ-trên-phpmyadmin)
3. [Cách mở và chạy dự án trong Eclipse IDE](#3-cách-mở-và-chạy-dự-án-trong-eclipse-ide)
4. [Trải nghiệm các chức năng Full CRUD trên Web](#4-trải-nghiệm-các-chức-năng-full-crud-trên-web)
5. [Kiến trúc chuẩn của Bài 7 theo yêu cầu Thầy Trương Bá Phúc](#5-kiến-trúc-chuẩn-của-bài-7-theo-yêu-cầu-thầy-trương-bá-phúc)
6. [Danh sách các REST API Endpoint](#6-danh-sách-các-rest-api-endpoint)

---

## 1. THÔNG TIN CLEVER CLOUD MYSQL ĐÃ CẤU HÌNH

File `src/main/resources/application.properties` đã được điền chính xác thông số của bạn:

```properties
server.port=8080

# Kết nối Clever Cloud MySQL
spring.datasource.url=jdbc:mysql://bqil983hlw33dnafyqvs-mysql.services.clever-cloud.com:3306/bqil983hlw33dnafyqvs?createDatabaseIfNotExist=true&useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC
spring.datasource.username=un0ambnc8wmldqfb
spring.datasource.password=4YnHLJB7lYnNHrxUO26z
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver

# Tự động đồng bộ bảng & khóa ngoại trong MySQL
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.MySQLDialect
```

---

## 2. CÁCH XEM SƠ ĐỒ QUAN HỆ RDB TRỰC QUAN (ERD) NGAY BÂY GIỜ TRÊN PHPMYADMIN

Do hệ thống đã kết nối và tự động sinh bảng thành công vào Clever Cloud của bạn, bạn có thể xem ngay sơ đồ RDB trực quan:

1. Đăng nhập vào trang quản trị [Clever Cloud Console](https://console.clever-cloud.com).
2. Nhấp chọn Add-on MySQL của bạn (`bqil983hlw33dnafyqvs`).
3. Bấm vào nút **"phpMyAdmin"** ở đầu trang $\rightarrow$ Trình duyệt tự mở giao diện phpMyAdmin.
4. Ở cột bên trái, bấm chọn database: **`bqil983hlw33dnafyqvs`**.
5. Nhìn lên thanh menu ngang phía trên cùng, bấm vào tab **"Designer"** (Bộ thiết kế):
   * *(Nếu màn hình nhỏ chưa thấy, bấm nút **More (Xem thêm)** $\rightarrow$ chọn **Designer**)*.
6. 👉 **Bạn sẽ thấy ngay SƠ ĐỒ RDB TUYỆT ĐẸP**:
   * Bảng **`departments`** (id, name).
   * Bảng **`staffs`** (id, name, email, department_id).
   * Đường kẻ màu xanh nối trực quan từ `departments.id` sang `staffs.department_id` biểu thị quan hệ $1 - N$ chuẩn chỉ.
   * Bạn có thể dùng chuột kéo thả các bảng để sắp xếp vị trí và chụp ảnh đưa vào báo cáo!

---

## 3. CÁCH MỞ VÀ CHẠY DỰ ÁN TRONG ECLIPSE IDE

Dự án đã có sẵn các file cấu hình `.project`, `.classpath`, `pom.xml`:

### Bước 1: Mở Eclipse và Import
1. Trên thanh menu Eclipse, chọn **File** $\rightarrow$ **Open Projects from File System...**  
   *(Hoặc **File** $\rightarrow$ **Import...** $\rightarrow$ chọn **Maven** $\rightarrow$ **Existing Maven Projects**)*.
2. Tại dòng **Import source**, bấm nút **Directory...** và trỏ đến thư mục:
   ```
   d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\t2\b7_department_staff_mysql
   ```
3. Bấm **Finish**.

### Bước 2: Chạy ứng dụng
1. Trong cửa sổ Package Explorer của Eclipse, mở thư mục:  
   `src/main/java` $\rightarrow$ `com.example.demo` $\rightarrow$ click chuột phải vào file **`DemoApplication.java`**.
2. Chọn **Run As** $\rightarrow$ **Spring Boot App** *(hoặc **Java Application**)*.
3. Quan sát tab **Console**: Ứng dụng khởi động trong khoảng 10 giây và sẵn sàng trên cổng `8080`.

---

## 4. TRẢI NGHIỆM CÁC CHỨC NĂNG FULL CRUD TRÊN WEB

Sau khi chạy ứng dụng trong Eclipse, mở trình duyệt vào địa chỉ:  
👉 **`http://localhost:8080/index.html`** *(hoặc `http://localhost:8080`)*

### Các tính năng đã hoạt động 100%:
1. **Lọc theo Phòng ban (Combobox)**: Chọn phòng ban bất kỳ $\rightarrow$ Bảng tự động tải danh sách nhân viên của phòng ban đó. Bấm nút "Tất cả" để xem lại toàn bộ.
2. **Tìm kiếm theo tên**: Nhập tên nhân viên vào ô tìm kiếm và bấm **🔍 Tìm kiếm** (hoặc nhấn phím `Enter`).
3. **Thêm mới nhân viên (Create)**:
   - Bấm nút **➕ Thêm mới nhân viên** màu xanh lá.
   - Nhập Họ tên, Email, chọn Phòng ban $\rightarrow$ bấm **Lưu nhân viên**.
   - Dữ liệu lập tức được ghi trực tiếp vào Clever Cloud MySQL và hiển thị lên bảng.
4. **Sửa thông tin nhân viên (Update)**:
   - Bấm nút **✏️ Sửa** ở hàng nhân viên tương ứng.
   - Hộp thoại popup hiện thông tin hiện tại, cho phép bạn đổi tên, email, hoặc chuyển nhân viên sang phòng ban khác $\rightarrow$ bấm **Cập nhật thay đổi**.
5. **Xóa nhân viên (Delete)**:
   - Bấm nút **🗑️ Xóa** màu đỏ.
   - Trình duyệt sẽ bật thông báo xác nhận: *"Bạn có chắc chắn muốn xóa nhân viên [Tên] không?"* $\rightarrow$ Chọn OK để xóa vĩnh viễn khỏi MySQL.

---

## 5. KIẾN TRÚC CHUẨN CỦA BÀI 7 THEO YÊU CẦU THẦY TRƯƠNG BÁ PHÚC

Dự án được xây dựng theo đúng chuẩn thiết kế MVC + REST Service 3 tầng:

```
b7_department_staff_mysql/
├── pom.xml                               # Khai báo web, data-jpa, mysql-connector-j
├── .project, .classpath                  # Cấu hình Eclipse IDE
├── src/main/java/com/example/demo/
│   ├── DemoApplication.java             # File chạy chính + CommandLineRunner seeder
│   ├── model/
│   │   ├── Department.java               # Entity @Table(name = "departments") [Bảng 1]
│   │   └── Staff.java                    # Entity @Table(name = "staffs") [Bảng N - FK department_id]
│   ├── repository/                       # <-- TẦNG MỚI THẦY YÊU CẦU BỔ SUNG
│   │   ├── DepartmentRepository.java     # extends JpaRepository<Department, Long>
│   │   └── StaffRepository.java          # extends JpaRepository<Staff, Long> (Hỗ trợ tìm kiếm)
│   ├── service/
│   │   └── OrganizationService.java      # Xử lý nghiệp vụ gọi Repository lưu vào CSDL
│   └── controller/
│       ├── DepartmentController.java     # REST API lấy danh sách phòng ban cho Combobox
│       └── StaffController.java          # REST API đầy đủ CRUD (Thêm, Xem, Sửa, Xóa, Tìm kiếm)
└── src/main/resources/
    ├── application.properties            # Cấu hình Clever Cloud MySQL
    └── static/
        └── index.html                    # Giao diện SPA hiện đại (Full Thêm/Sửa/Xóa/Tìm)
```

### Sơ đồ luồng dữ liệu (Data Flow):
$$\text{Giao diện (index.html)} \underset{\text{Fetch API}}{\overset{\text{JSON}}{\longleftrightarrow}} \text{Controllers} \longleftrightarrow \text{OrganizationService} \longleftrightarrow \text{JPA Repositories} \underset{\text{SQL Queries}}{\overset{\text{JDBC}}{\longleftrightarrow}} \text{MySQL (Clever Cloud)}$$

---

## 6. DANH SÁCH CÁC REST API ENDPOINT

| Phương thức | Đường dẫn API | Chức năng | Dữ liệu gửi lên (Body) | Mã phản hồi |
| :---: | :--- | :--- | :---: | :---: |
| `GET` | `/api/departments` | Lấy tất cả phòng ban cho Combobox | Không | `200 OK` |
| `GET` | `/api/departments/{id}/staffs` | Lấy chi tiết phòng ban & nhân viên | Không | `200 OK` / `404` |
| `GET` | `/api/staffs` | Lấy toàn bộ nhân viên (hoặc lọc) | Query: `?departmentId=1&keyword=an` | `200 OK` |
| `GET` | `/api/staffs/{id}` | Lấy 1 nhân viên theo ID | Không | `200 OK` / `404` |
| `POST` | `/api/staffs` | **Thêm mới nhân viên** | `{"name":"...", "email":"...", "departmentId": 1}` | `201 Created` |
| `PUT` | `/api/staffs/{id}` | **Cập nhật nhân viên** | `{"name":"...", "email":"...", "departmentId": 2}` | `200 OK` / `404` |
| `DELETE`| `/api/staffs/{id}` | **Xóa nhân viên** | Không | `204 No Content` |
