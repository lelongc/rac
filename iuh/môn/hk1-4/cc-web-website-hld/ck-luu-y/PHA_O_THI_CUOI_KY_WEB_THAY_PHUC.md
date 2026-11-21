---

## 📌 PHẦN 1: LÝ THUYẾT TRỌNG TÂM (CỰC GỌN & VỪA ĐỦ)

### 1. Danh sách các Công cụ phần mềm môn học (Thầy yêu cầu kể ít nhất 10, học 15 cái cho chắc ăn)

1. **Eclipse IDE** (hoặc Spring Tool Suite - STS): Môi trường phát triển tích hợp (IDE) lập trình Java / Spring Boot.
2. **MySQL Server**: Hệ quản trị cơ sở dữ liệu quan hệ (RDBMS) lưu trữ dữ liệu bền vững.
3. **MySQL Workbench**: Công cụ giao diện đồ họa (GUI) thiết kế ERD, quản trị CSDL trực quan.
4. **Spring Boot**: Framework backend Java phát triển ứng dụng Web & RESTful API.
5. **Spring Initializr** (start.spring.io): Công cụ web khởi tạo nhanh khung dự án Spring Boot.
6. **Maven** (`pom.xml`, `mvnw`): Công cụ tự động hóa build và quản lý thư viện phụ thuộc (Dependencies).
7. **Postman**: Công cụ GUI gửi HTTP request kiểm thử RESTful API (GET, POST, PUT, DELETE).
8. **cURL**: Công cụ dòng lệnh (CLI) gửi HTTP request kiểm thử REST API trực tiếp từ terminal.
9. **Git**: Công cụ phần mềm quản lý phiên bản mã nguồn phân tán (Distributed VCS).
10. **GitHub**: Nền tảng dịch vụ web lưu trữ kho mã nguồn Git và cộng tác dự án.
11. **Thymeleaf**: Template Engine render giao diện HTML phía Server (Server-Side Rendering - SSR).
12. **Docker**: Công cụ ảo hóa cấp hệ điều hành (Containerization) đóng gói và chạy CSDL/ứng dụng.
13. **Clever Cloud**: Nền tảng đám mây (PaaS) lưu trữ và triển khai CSDL MySQL trực tuyến.
14. **Chrome DevTools** (hoặc Firefox DevTools): Công cụ tích hợp sẵn trên trình duyệt để debug giao diện, kiểm tra Network request, Console log và cấu trúc DOM.
15. **MockAPI** (hoặc JSONPlaceholder): Công cụ trực tuyến tạo Virtual/Mock RESTful API phục vụ phát triển Front-End độc lập.

> ⚠️ **BẪY CỰC LỚN CỦA THẦY:** **Bootstrap, jQuery, Lombok, Axios** là **thư viện / framework mã nguồn (Libraries)**, **KHÔNG PHẢI công cụ phần mềm (Tools/Software)**! Nhớ kỹ kẻo bị trừ sạch điểm!

---

### 2. JPA, Hibernate & Kỹ thuật ORM là gì?

* **JPA (Java Persistence API / Jakarta Persistence):** Là **đặc tả kỹ thuật (Specification / Standard)** của Java quy định cách quản lý và ánh xạ dữ liệu đối tượng Java với CSDL quan hệ.
* **Hibernate:** Là thư viện **hiện thực hóa (Implementation)** cụ thể của chuẩn JPA. JPA đưa ra "luật", Hibernate thực thi luật đó.
* **ORM (Object-Relational Mapping):** Kỹ thuật ánh xạ:
  * **Class** Java (`@Entity`) $\longleftrightarrow$ **Bảng** CSDL (`@Table`).
  * **Thuộc tính** (`field`) $\longleftrightarrow$ **Cột** trong bảng (`@Column`).
  * **Đối tượng** (`Object`) $\longleftrightarrow$ **Dòng dữ liệu** (`Record`).
  * **Mối liên kết** (`@ManyToOne`, `@OneToMany`) $\longleftrightarrow$ **Khóa ngoại** (`Foreign Key`).

---

### 3. So sánh JDBC truyền thống vs JPA / Hibernate

* **JDBC (Cũ):** Mức thấp, phải tự mở kết nối (`Connection`), tự viết câu lệnh SQL bằng tay (`SELECT * FROM...`), tự duyệt con trỏ `ResultSet`, code dài dòng (boilerplate) và dễ dính lỗi SQL Injection.
* **JPA / Hibernate (Mới):** Mức cao, chỉ cần gắn các **dấu `@` (Annotation)**, Hibernate sẽ **tự động sinh toàn bộ câu lệnh SQL và bảng CSDL**, giúp lập trình viên thao tác với DB hoàn toàn bằng Object Java.

---

### 4. RESTful API, JSON & Các thành phần cốt lõi của REST API

* **RESTful API là gì?**Là chuẩn kiến trúc thiết kế dịch vụ web (Web Service) phi trạng thái (Stateless), sử dụng đường dẫn URI để định danh tài nguyên (Resource) và dùng các phương thức HTTP chuẩn (`GET`, `POST`, `PUT`, `DELETE`) để thao tác CRUD. Dữ liệu trao đổi chuẩn là JSON.
* **Tại sao dùng JSON (JavaScript Object Notation)?**
  * Định dạng văn bản cực kỳ nhẹ (lightweight), dễ đọc, dễ viết, độc lập với mọi ngôn ngữ lập trình.
  * Là chuẩn quốc tế trao đổi dữ liệu giữa Front-End (JavaScript) và Back-End (Java REST API) hoặc Mobile.
  * Trình duyệt xử lý cực nhanh bằng hàm `JSON.stringify()` và `res.json()`.
* **6 Thành phần cốt lõi của một REST API (Request & Response):**
  1. **Endpoint / URI:** Địa chỉ định danh tài nguyên trên Server (Ví dụ: `/api/students`, `/api/students/1`).
  2. **HTTP Method (Động từ thao tác):** `GET` (đọc), `POST` (tạo mới), `PUT` (cập nhật toàn bộ), `DELETE` (xóa).
  3. **HTTP Headers (Siêu dữ liệu - Metadata):** Khai báo định dạng dữ liệu và thông tin bổ trợ.*(Ví dụ: `Content-Type: application/json` báo cho server biết dữ liệu gửi lên là JSON, `Accept: application/json`)*.
  4. **Request Body / Payload:** Dữ liệu client gửi kèm lên server dưới dạng chuỗi JSON (thường dùng cho `POST`, `PUT`).
  5. **HTTP Status Code (Mã trạng thái phản hồi):** Mã 3 chữ số thông báo kết quả xử lý từ server:
     * `2xx` (Thành công): `200 OK`, `201 Created` (tạo mới thành công), `204 No Content` (xóa thành công).
     * `4xx` (Lỗi Client): `400 Bad Request` (sai định dạng dữ liệu), `401 Unauthorized` (chưa xác thực/đăng nhập), `404 Not Found` (không tìm thấy tài nguyên).
     * `5xx` (Lỗi Server): `500 Internal Server Error` (server bị lỗi sập code).
  6. **Response Body:** Dữ liệu kết quả server phản hồi về cho client dưới dạng chuỗi JSON hoặc thông báo lỗi.
* **Virtual / Fake REST API là gì?**
  Là API giả lập trên đám mây (như MockAPI.io, JSONPlaceholder) cung cấp sẵn các endpoint REST và dữ liệu mẫu (kèm text, hình ảnh), giúp lập trình viên Front-End kiểm thử giao diện và gọi Fetch API độc lập mà không cần chờ viết Back-End.

---

## 🌐 PHẦN 2: THÀNH PHẦN URL, HTTP METHODS (CRUD) & LỆNH cURL

### 1. Cấu trúc các thành phần trong 1 URL

```text
  http:// localhost :8080 /api/students /1 ?status=active #top
  ──┬──   ────┬────  ─┬──  ──────┬────── ─┬ ───────┬──────  ─┬─
    │         │       │          │        │        │        └─ Fragment (Vị trí neo trên trang)
    │         │       │          │        │        └─ Query Parameter (Tham số lọc, sắp xếp)
    │         │       │          │        └─ Path Variable (Định danh tài nguyên cụ thể)
    │         │       │          └─ Path / Endpoint (Đường dẫn tài nguyên)
    │         │       └─ Port (Cổng dịch vụ web)
    │         └─ Host / Domain (Địa chỉ máy chủ)
    └─ Scheme / Protocol (Giao thức mạng: http, https)
```

### 2. Bảng ánh xạ CRUD sang HTTP Methods & Status Code chuẩn

| Thao tác CRUD                        | HTTP Method           | Endpoint URL mẫu      | Request Body (JSON)? | HTTP Status trả về                 |
| :------------------------------------ | :-------------------- | :--------------------- | :------------------: | :----------------------------------- |
| **C** (Create - Thêm)          | **POST**        | `/api/students`      |    **CÓ**    | `201 Created`                      |
| **R** (Read All - Lấy hết)    | **GET**         | `/api/students`      |   **KHÔNG**   | `200 OK`                           |
| **R** (Read One - Lấy theo ID) | **GET**         | `/api/students/{id}` |   **KHÔNG**   | `200 OK` (hoặc `404 Not Found`) |
| **U** (Update - Sửa)           | **PUT** / PATCH | `/api/students/{id}` |    **CÓ**    | `200 OK`                           |
| **D** (Delete - Xóa)           | **DELETE**      | `/api/students/{id}` |   **KHÔNG**   | `204 No Content` / `200 OK`      |

### 3. Cú pháp cURL chuẩn thi (Chép ăn trọn điểm)

```bash
# 1. GET ALL (Lấy tất cả)
curl -X GET http://localhost:8080/api/students

# 2. GET BY ID (Lấy sinh viên id = 1)
curl -X GET http://localhost:8080/api/students/1

# 3. POST (Thêm mới sinh viên kèm JSON)
curl -X POST http://localhost:8080/api/students \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Nguyen Van A\",\"email\":\"a@gmail.com\",\"age\":20,\"facultyId\":1}"

# 4. PUT (Cập nhật sinh viên id = 1)
curl -X PUT http://localhost:8080/api/students/1 \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Nguyen Van B\",\"email\":\"b@gmail.com\",\"age\":21,\"facultyId\":1}"

# 5. DELETE (Xóa sinh viên id = 1)
curl -X DELETE http://localhost:8080/api/students/1

# 6. POST N-N (Sinh viên 2 đăng ký Môn học 1)
curl -X POST http://localhost:8080/api/subjects/1/students/2
```

---

## 💻 PHẦN 3: BỘ KHUNG CODE CRUD ĐA NĂNG (TEMPLATE CÂN MỌI ĐỀ THI)

*(Dùng Lombok `@Getter @Setter @NoArgsConstructor @AllArgsConstructor @RequiredArgsConstructor` để code siêu ngắn gọn khi viết bài thi giấy).*

### 1. Entity mẫu: `Student.java` (Quan hệ 1-N và N-N)

```java
@Entity
@Table(name = "students")
@Getter @Setter
@NoArgsConstructor @AllArgsConstructor
public class Student {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 100)
    private String name;

    @Column(nullable = false, unique = true)
    private String email;

    // Quan hệ 1-N (Student giữ khóa ngoại faculty_id)
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "faculty_id")
    @JsonBackReference
    private Faculty faculty;

    // Quan hệ N-N (Student sở hữu bảng trung gian student_subject)
    @ManyToMany(fetch = FetchType.LAZY)
    @JoinTable(
        name = "student_subject",
        joinColumns = @JoinColumn(name = "student_id"),
        inverseJoinColumns = @JoinColumn(name = "subject_id")
    )
    @JsonIgnoreProperties("students")
    private Set<Subject> subjects = new HashSet<>();
}
```

### 2. Entity Cha mẫu: `Faculty.java` (1-N bên 1)

```java
@Entity
@Table(name = "faculties")
@Getter @Setter
@NoArgsConstructor @AllArgsConstructor
public class Faculty {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;

    @OneToMany(mappedBy = "faculty", cascade = CascadeType.ALL)
    @JsonManagedReference
    private List<Student> students = new ArrayList<>();
}
```

### 3. Repository mẫu: `StudentRepository.java`

```java
@Repository
public interface StudentRepository extends JpaRepository<Student, Long> {
    Optional<Student> findByEmail(String email); // Tìm kiếm theo email
}
```

### 4. Service mẫu: `StudentService.java` (Đầy đủ CRUD)

```java
@Service
@RequiredArgsConstructor // Tự sinh constructor inject các biến final (Dependency Injection ngầm định)
public class StudentService {
    private final StudentRepository studentRepo;
    private final FacultyRepository facultyRepo;

    public List<Student> getAll() { return studentRepo.findAll(); }

    public Student getById(Long id) {
        return studentRepo.findById(id)
            .orElseThrow(() -> new RuntimeException("Not found: " + id));
    }

    public Student create(Student s, Long facultyId) {
        Faculty f = facultyRepo.findById(facultyId)
            .orElseThrow(() -> new RuntimeException("Faculty not found"));
        s.setFaculty(f);
        return studentRepo.save(s);
    }

    public Student update(Long id, Student req) {
        Student s = getById(id);
        s.setName(req.getName());
        return studentRepo.save(s);
    }

    public void delete(Long id) { studentRepo.deleteById(id); }
}
```

### 5. Controller mẫu: `StudentController.java` (Đầy đủ 5 Endpoint REST)

```java
@RestController
@RequestMapping("/api/students")
@RequiredArgsConstructor // Tự sinh constructor inject studentService
public class StudentController {
    private final StudentService studentService;

    @GetMapping
    public List<Student> getAll() {
        return studentService.getAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Student> getById(@PathVariable Long id) {
        return ResponseEntity.ok(studentService.getById(id));
    }

    @PostMapping
    public ResponseEntity<Student> create(@RequestBody Student s, @RequestParam Long facultyId) {
        return new ResponseEntity<>(studentService.create(s, facultyId), HttpStatus.CREATED);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Student> update(@PathVariable Long id, @RequestBody Student s) {
        return ResponseEntity.ok(studentService.update(id, s));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        studentService.delete(id);
        return ResponseEntity.noContent().build(); // Trả mã 204
    }
}
```

---

## ⚡ PHẦN 4: JAVASCRIPT FETCH API CRUD (GỌN NHẤT PHÍA FRONT-END)

Đoạn code JavaScript thuần dùng `async/await` làm đủ 4 thao tác gọi API Backend:

```javascript
const BASE_URL = 'http://localhost:8080/api/students';

// 1. GET: Lấy danh sách sinh viên
async function getStudents() {
    const res = await fetch(BASE_URL);
    const data = await res.json();
    console.log("Danh sách:", data);
    return data;
}

// 2. POST: Thêm mới sinh viên
async function createStudent(studentData, facultyId) {
    const res = await fetch(`${BASE_URL}?facultyId=${facultyId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(studentData)
    });
    return await res.json();
}

// 3. PUT: Cập nhật sinh viên theo ID
async function updateStudent(id, studentData) {
    const res = await fetch(`${BASE_URL}/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(studentData)
    });
    return await res.json();
}

// 4. DELETE: Xóa sinh viên theo ID
async function deleteStudent(id) {
    const res = await fetch(`${BASE_URL}/${id}`, {
        method: 'DELETE'
    });
    if (res.status === 204) console.log("Xóa thành công!");
}
```

---

## 📝 BÍ KÍP ĐỔI TÊN KHI GẶP CÁC ĐỀ THI KHÁC NHAU:

1. **Đề Quản lý Bán hàng:** `Faculty` $\rightarrow$ `Category` (Danh mục), `Student` $\rightarrow$ `Product` (Sản phẩm), `Subject` $\rightarrow$ `Tag` (Thẻ phân loại).
2. **Đề Quản lý Thư viện:** `Faculty` $\rightarrow$ `Publisher` (Nhà xuất bản), `Student` $\rightarrow$ `Book` (Sách), `Subject` $\rightarrow$ `Author` (Tác giả).
3. **Đề Quản lý Nhân sự:** `Faculty` $\rightarrow$ `Department` (Phòng ban), `Student` $\rightarrow$ `Employee` (Nhân viên), `Subject` $\rightarrow$ `Project` (Dự án).
   *(Chỉ cần giữ nguyên cấu trúc `@ManyToOne`, `@OneToMany`, `@ManyToMany` và thay các tên biến tương ứng là xong!)*
