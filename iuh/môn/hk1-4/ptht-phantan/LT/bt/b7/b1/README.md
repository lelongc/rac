# BÀI TẬP 1: API QUẢN LÝ SINH VIÊN ĐƠN GIẢN (SPRING BOOT REST API)

* **Học phần:** Phát triển hệ thống phân tán - Đại học Công nghiệp TP.HCM (IUH)
* **Công nghệ:** Java 21, Spring Boot 3 (Spring Web / REST Controller)

---

## 🚀 1. CÁCH KHỞI CHẠY ỨNG DỤNG

Mở terminal tại thư mục `b1`:

```powershell
.\mvnw.cmd spring-boot:run
```

Server sẽ khởi động tại cổng mặc định `http://localhost:8080`.

---

## 📋 2. DANH SÁCH 3 CHỨC NĂNG REST API THEO ĐỀ BÀI

Hệ thống hỗ trợ cả 2 tiền tố `/students` và `/api/students`:

| STT | Chức năng | Phương thức HTTP | Endpoint | Dữ liệu gửi lên (Body) |
|---|---|---|---|---|
| **1** | Lấy danh sách toàn bộ sinh viên | `GET` | `/students` | Không |
| **2** | Lấy một sinh viên theo ID | `GET` | `/students/{id}` | Không |
| **3** | Thêm sinh viên mới | `POST` | `/students` | JSON `{"name": "...", "age": ...}` |

---

## 💻 3. HƯỚNG DẪN TEST API (CURL HOẶC POWERSHELL)

### Chức năng 1: Lấy danh sách sinh viên
* **Lệnh cURL:**
```bash
curl http://localhost:8080/students
```
* **Kết quả trả về:**
```json
[
  {"id": 1, "name": "Nguyen Van An", "age": 20},
  {"id": 2, "name": "Tran Thi Binh", "age": 21},
  {"id": 3, "name": "Le Van Cuong", "age": 22}
]
```

---

### Chức năng 2: Lấy một sinh viên theo ID (Ví dụ: ID = 1)
* **Lệnh cURL:**
```bash
curl http://localhost:8080/students/1
```
* **Kết quả trả về:**
```json
{
  "id": 1,
  "name": "Nguyen Van An",
  "age": 20
}
```

---

### Chức năng 3: Thêm một sinh viên mới
* **Lệnh PowerShell:**
```powershell
Invoke-RestMethod -Uri http://localhost:8080/students -Method POST -ContentType "application/json" -Body '{"name": "Le Thanh Long", "age": 21}'
```
* **Lệnh cURL:**
```bash
curl -X POST http://localhost:8080/students -H "Content-Type: application/json" -d "{\"name\": \"Le Thanh Long\", \"age\": 21}"
```
* **Kết quả trả về:**
```json
{
  "id": 4,
  "name": "Le Thanh Long",
  "age": 21
}
```

---

## 📁 4. CẤU TRÚC THƯ MỤC DỰ ÁN

```
b1/
├── pom.xml                                                    # Cấu hình Spring Boot Starter Web
├── mvnw / mvnw.cmd / .mvn                                     # Maven Wrapper
├── README.md                                                  # Hướng dẫn chi tiết
└── src/main/
    ├── java/com/example/student/
    │   ├── StudentApplication.java                            # Lớp chạy ứng dụng Spring Boot
    │   ├── model/
    │   │   └── Student.java                                   # Model Sinh viên (id, name, age)
    │   └── controller/
    │       └── StudentController.java                         # REST Controller cài đặt 3 API
    └── resources/
        └── application.properties                             # Cấu hình server.port=8080
```
