# HƯỚNG DẪN CẤU HÌNH VÀ CHẠY BÀI 7: SPRING DATA JPA + MYSQL (FULL CRUD)

> **Mã bài tập**: Bài 7 - Quản lý Phòng Ban & Nhân Viên (`Department` - `Staff`)  
> **Thư mục dự án**: `d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\t2\b7_department_staff_mysql`  
> **Trạng thái Database**: ✅ **ĐÃ KẾT NỐI VÀ TEST THÀNH CÔNG VỚI CLEVER CLOUD MYSQL CỦA BẠN!**  
> **Bảng CSDL đã tạo**: `departments` (4 dòng) và `staffs` (5 dòng) kèm khóa ngoại `department_id`.

---

## MỤC LỤC
1. [HƯỚNG DẪN THAO TÁC TRÊN PHPMYADMIN (TỪ MÀN HÌNH BẠN ĐANG THẤY)](#1-hướng-dẫn-thao-tác-trên-phpmyadmin-từ-màn-hình-bạn-đang-thấy)
   - [Cách 1: Mở Sơ đồ quan hệ RDB (Designer) để chụp hình](#cách-1-mở-sơ-đồ-quan-hệ-rdb-designer-để-chụp-hình)
   - [Cách 2: Xem dữ liệu các dòng trong bảng (Browse)](#cách-2-xem-dữ-liệu-các-dòng-trong-bảng-browse)
   - [Cách 3: Xem chi tiết Khóa Ngoại (Relation view)](#cách-3-xem-chi-tiết-khóa-ngoại-relation-view)
2. [Cách mở và chạy dự án trong Eclipse IDE](#2-cách-mở-và-chạy-dự-án-trong-eclipse-ide)
3. [Trải nghiệm các chức năng Full CRUD trên Web](#3-trải-nghiệm-các-chức-năng-full-crud-trên-web)
4. [Kiến trúc chuẩn của Bài 7 theo yêu cầu Thầy Trương Bá Phúc](#4-kiến-trúc-chuẩn-của-bài-7-theo-yêu-cầu-thầy-trương-bá-phúc)
5. [Danh sách các REST API Endpoint](#5-danh-sách-các-rest-api-endpoint)

---

## 1. HƯỚNG DẪN THAO TÁC TRÊN PHPMYADMIN (TỪ MÀN HÌNH BẠN ĐANG THẤY)

Nhìn vào màn hình phpMyAdmin bạn vừa chụp được, 2 bảng `departments` (4 dòng) và `staffs` (5 dòng) đã nằm sẵn trong MySQL của bạn. Bây giờ bạn làm tiếp các bước sau:

### Cách 1: Mở Sơ đồ quan hệ RDB (Designer) để chụp hình
1. Nhìn lên thanh menu ngang phía trên cùng (dòng có chữ `Structure`, `SQL`, `Search`, `Query`, `Export`, `Import`, `Operations`, `Routines`...).
2. Ở góc bên phải của thanh menu đó, bấm vào chữ:  
   👉 **`More ▼`** (hoặc dấu mũi tên trỏ xuống bên cạnh chữ `Routines`).
3. Trong menu thả xuống, bấm chọn dòng:  
   👉 **`Designer`** *(hoặc tiếng Việt là **Bộ thiết kế**)*.
4. **KẾT QUẢ**:
   * Toàn bộ màn hình sẽ chuyển sang trang vẽ sơ đồ quan hệ RDB (ERD).
   * Bạn sẽ thấy 2 khối hộp hình chữ nhật: **`departments`** và **`staffs`**.
   * Có một **sợi dây liên kết màu xanh** nối từ `departments.id` sang `staffs.department_id`.
   * Bạn dùng chuột bấm vào tiêu đề các bảng để kéo thả sắp xếp vị trí cho ngay ngắn, sau đó chụp màn hình lại để nộp cho thầy!

---

### Cách 2: Xem dữ liệu các dòng trong bảng (Browse)
1. Trên màn hình danh sách bảng (như trong ảnh của bạn):
   * Nhìn vào dòng `departments`, bấm vào chữ **`Browse`** có icon kính lúp $\rightarrow$ Bạn sẽ thấy 4 phòng ban: *Engineering, Human Resources, Marketing, Finance*.
   * Nhìn vào dòng `staffs`, bấm vào chữ **`Browse`** $\rightarrow$ Bạn sẽ thấy 5 nhân viên: *Nguyen Van An, Tran Thi Binh, Le Hoang Cuong, Pham Thi Dung, Doan Minh Em*.

---

### Cách 3: Xem chi tiết Khóa Ngoại (Relation view)
1. Ở cột danh sách bảng bên trái, bấm vào bảng **`staffs`**.
2. Nhìn lên thanh menu trên cùng, bấm tab **`Structure`** (Cấu trúc).
3. Bấm vào nút **`Relation view`** (Chế độ xem quan hệ):
   * Bạn sẽ thấy dòng khai báo ràng buộc khóa ngoại:  
     `department_id` trỏ tới bảng `departments(id)` với chế độ `ON DELETE CASCADE`.

---

## 2. CÁCH MỞ VÀ CHẠY DỰ ÁN TRONG ECLIPSE IDE

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

## 3. TRẢI NGHIỆM CÁC CHỨC NĂNG FULL CRUD TRÊN WEB

Sau khi chạy ứng dụng trong Eclipse, mở trình duyệt vào địa chỉ:  
👉 **`http://localhost:8080/index.html`** *(hoặc `http://localhost:8080`)*

### Các tính năng đã hoạt động 100%:
1. **Lọc theo Phòng ban (Combobox)**: Chọn phòng ban bất kỳ $\rightarrow$ Bảng tự động tải danh sách nhân viên của phòng ban đó. Bấm nút "Tất cả" để xem lại toàn bộ.
2. **Tìm kiếm theo tên**: Nhập tên nhân viên vào ô tìm kiếm và bấm **Tìm kiếm** (hoặc nhấn phím `Enter`).
3. **Thêm mới nhân viên (Create)**:
   - Bấm nút **Thêm nhân viên** màu xanh lá.
   - Nhập Họ tên, Email, chọn Phòng ban $\rightarrow$ bấm **Lưu nhân viên**.
   - Dữ liệu lập tức được ghi trực tiếp vào Clever Cloud MySQL và hiển thị lên bảng.
4. **Sửa thông tin nhân viên (Update)**:
   - Bấm nút **Sửa** ở hàng nhân viên tương ứng.
   - Hộp thoại popup hiện thông tin hiện tại, cho phép bạn đổi tên, email, hoặc chuyển nhân viên sang phòng ban khác $\rightarrow$ bấm **Lưu thay đổi**.
5. **Xóa nhân viên (Delete)**:
   - Bấm nút **Xóa** màu đỏ.
   - Trình duyệt sẽ bật thông báo xác nhận: *"Bạn có chắc chắn muốn xóa nhân viên [Tên] không?"* $\rightarrow$ Chọn OK để xóa vĩnh viễn khỏi MySQL.

---

## 4. KIẾN TRÚC CHUẨN CỦA BÀI 7 THEO YÊU CẦU THẦY TRƯƠNG BÁ PHÚC

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
        └── index.html                    # Giao diện SPA gọn gàng (Full Thêm/Sửa/Xóa/Tìm)
```

### Sơ đồ luồng dữ liệu (Data Flow):
$$\text{Giao diện (index.html)} \underset{\text{Fetch API}}{\overset{\text{JSON}}{\longleftrightarrow}} \text{Controllers} \longleftrightarrow \text{OrganizationService} \longleftrightarrow \text{JPA Repositories} \underset{\text{SQL Queries}}{\overset{\text{JDBC}}{\longleftrightarrow}} \text{MySQL (Clever Cloud)}$$

---

## 5. DANH SÁCH CÁC REST API ENDPOINT

| Phương thức | Đường dẫn API | Chức năng | Dữ liệu gửi lên (Body) | Mã phản hồi |
| :---: | :--- | :--- | :---: | :---: |
| `GET` | `/api/departments` | Lấy tất cả phòng ban cho Combobox | Không | `200 OK` |
| `GET` | `/api/departments/{id}/staffs` | Lấy chi tiết phòng ban & nhân viên | Không | `200 OK` / `404` |
| `GET` | `/api/staffs` | Lấy toàn bộ nhân viên (hoặc lọc) | Query: `?departmentId=1&keyword=an` | `200 OK` |
| `GET` | `/api/staffs/{id}` | Lấy 1 nhân viên theo ID | Không | `200 OK` / `404` |
| `POST` | `/api/staffs` | **Thêm mới nhân viên** | `{"name":"...", "email":"...", "departmentId": 1}` | `201 Created` |
| `PUT` | `/api/staffs/{id}` | **Cập nhật nhân viên** | `{"name":"...", "email":"...", "departmentId": 2}` | `200 OK` / `404` |
| `DELETE`| `/api/staffs/{id}` | **Xóa nhân viên** | Không | `204 No Content` |
