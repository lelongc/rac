### 1. Kiến trúc Mô hình MVC (Model - View - Controller)

  là mô hình kiến trúc phân tách ứng dụng phần mềm thành 3 tầng độc lập:

* **Model (Dữ liệu & Trạng thái):** Gồm **Entity** (ánh xạ bảng CSDL) và **DTO** (đối tượng truyền nhận dữ liệu, ẩn trường nhạy cảm).
* **View (Giao diện hiển thị):** Trình diễn dữ liệu cho người dùng (HTML Thymeleaf render phía Server hoặc JSON gửi về cho Front-End).
* **Controller (Điều hướng & Tiếp nhận):** Tiếp nhận HTTP Request từ Client, gọi Service xử lý nghiệp vụ, trả dữ liệu Model về View hoặc trả trực tiếp JSON.
* **Tầng Service (Nghiệp vụ):** Thuộc hoàn toàn về **Back-End**, đứng giữa Controller và Repository, xử lý logic tính toán, kiểm tra ràng buộc và quản lý giao dịch (`@Transactional`).

---

### 2. JPA, Hibernate & Kỹ thuật ORM

**JPA (Java Persistence API) là chuẩn đặc tả kỹ thuật của Java, cho phép lập trình viên ánh xạ các đối tượng Java (Class, Field) sang các bảng và cột trong Cơ sở dữ liệu quan hệ (MySQL) thông qua các Annotation (dấu `@`), giúp tự động hóa việc lưu trữ dữ liệu và sinh câu lệnh SQL mà không cần viết JDBC thuần thủ công**

* **JPA (Java Persistence API / Jakarta Persistence):** Là **chuẩn đặc tả (Specification/Standard)** của Java quy định cách quản lý và ánh xạ dữ liệu đối tượng Java với CSDL quan hệ.
* **Hibernate:** Là thư viện **hiện thực hóa (Implementation)** cụ thể của chuẩn JPA. JPA đưa ra "luật", Hibernate thực thi luật đó.
* **ORM (Object-Relational Mapping):** Kỹ thuật ánh xạ:
  * **Class** Java (`@Entity`) $\longleftrightarrow$ **Bảng** CSDL (`@Table`).
  * **Thuộc tính** (`field`) $\longleftrightarrow$ **Cột** trong bảng (`@Column`).
  * **Đối tượng** (`Object`) $\longleftrightarrow$ **Dòng dữ liệu** (`Record`).
  * **Mối liên kết** (`@ManyToOne`, `@OneToMany`) $\longleftrightarrow$ **Khóa ngoại** (`Foreign Key`).
* **So sánh JDBC vs JPA:**
  * *JDBC cũ:* Mức thấp, viết SQL tay, tự mở Connection, duyệt ResultSet, dài dòng, dễ dính SQL Injection.
  * *JPA mới:* Mức cao, chỉ cần gắn các **dấu `@` (Annotation)**, Hibernate tự sinh toàn bộ SQL và bảng DB.

---

### 3. RESTful API, JSON & Các thành phần cốt lõi

* **RESTful API là gì?** Chuẩn kiến trúc Web Service phi trạng thái (Stateless), dùng URL định danh tài nguyên (Resource) và các phương thức HTTP chuẩn (`GET`, `POST`, `PUT`, `DELETE`) để thao tác CRUD. Dữ liệu chuẩn trao đổi là JSON.
* **Tại sao dùng JSON?** Nhẹ (lightweight), độc lập ngôn ngữ, chuẩn trao đổi quốc tế Client-Server, JavaScript xử lý cực nhanh bằng `JSON.stringify()` và `res.json()`.
* **6 Thành phần cốt lõi của một REST API (Request & Response):**
  1. **Endpoint / URI:** Đường dẫn định danh tài nguyên trên Server (`/api/students`, `/api/students/1`).
  2. **HTTP Method:** Động từ thao tác (`GET`: đọc, `POST`: tạo mới, `PUT`: sửa toàn bộ, `DELETE`: xóa).
  3. **HTTP Headers:** Siêu dữ liệu metadata (`Content-Type: application/json` báo body là JSON, `Accept: application/json`).
  4. **Request Body / Payload:** Chuỗi dữ liệu JSON gửi kèm lên server khi `POST` hoặc `PUT`.
  5. **HTTP Status Code:** Mã 3 chữ số phản hồi:
     * `2xx` (Thành công): `200 OK`, `201 Created` (tạo mới), `204 No Content` (xóa thành công).
     * `4xx` (Lỗi Client): `400 Bad Request` (sai định dạng), `401 Unauthorized` (chưa login), `404 Not Found` (không tìm thấy).
     * `5xx` (Lỗi Server): `500 Internal Server Error` (sập code xử lý backend).
  6. **Response Body:** Dữ liệu JSON hoặc thông báo lỗi server trả về cho client.

---

### 4. Dependency Injection (DI) & Cơ chế Implicit vs Explicit

* **DI (Tiêm phụ thuộc):** Hiện thực hóa nguyên lý **IoC (Đảo ngược điều khiển)**. Thay vì dùng `new` thủ công, Spring IoC Container tự động khởi tạo Bean và tiêm vào nơi cần.
* **Explicit (Tường minh):** Viết rõ `@Autowired` trên thuộc tính hoặc constructor.
* **Implicit (Ngầm định):** Từ Spring 4.3+, class có **1 constructor**, Spring tự động ngầm inject mà **không cần gõ `@Autowired`** (hoặc dùng `@RequiredArgsConstructor` của Lombok).

---

### 5. Danh sách các Công cụ phần mềm môn học (Thầy yêu cầu kể 10 cái)

1. **Eclipse IDE** (hoặc STS): Môi trường phát triển Java.
2. **MySQL Server**: Hệ quản trị cơ sở dữ liệu quan hệ (RDBMS).
3. **MySQL Workbench**: Thiết kế ERD, quản trị CSDL trực quan (GUI).
4. **Postman**: Công cụ GUI gửi HTTP request kiểm thử REST API.
5. **cURL**: Công cụ dòng lệnh (CLI) gửi HTTP request kiểm thử REST API từ terminal.
6. **Maven** (`pom.xml`, `mvnw`): Quản lý dependencies và build dự án tự động.
7. **Spring Initializr** (*start.spring.io*): Web tool khởi tạo nhanh project Spring Boot.
8. **Git**: Phần mềm quản lý phiên bản mã nguồn (VCS).
9. **GitHub**: Nền tảng web lưu trữ kho mã nguồn Git và cộng tác.
10. **Chrome DevTools**: Bộ công cụ trình duyệt debug DOM, Console, Network API.
11. **Docker**: Phần mềm ảo hóa container chạy CSDL/App.
12. **Clever Cloud**: Nền tảng PaaS đám mây deploy MySQL online.
13. **MockAPI**: Công cụ web tạo Virtual/Mock REST API.

---

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

## 💻 PHẦN 3: CODE BACK-END CRUD ĐA NĂNG 

(Mô hình chuẩn: `Student` thuộc 1 `Faculty` (1-N) và học nhiều `Subject` (N-N).

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
    // Quan hệ 1-N (Student giữ khóa ngoại faculty_id - Owning Side)
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

### 2. Entity Cha mẫu: `Faculty.java` (1-N bên 1 - Inverse Side)

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

### 4. Service mẫu: `StudentService.java` (Đầy đủ 5 hàm CRUD)

```java
@Service
@RequiredArgsConstructor // Tự sinh constructor inject biến final (DI ngầm định)
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
@RequiredArgsConstructor
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

## ⚡ PHẦN 4: CODE FRONT-END (FETCH API CRUD & RENDER GIAO DIỆN BẢNG DOM)

### 1. Giao diện HTML mẫu (`index.html`)

```html
<table border="1" id="studentTable">
    <thead>
        <tr><th>ID</th><th>Tên</th><th>Email</th><th>Hành động</th></tr>
    </thead>
    <tbody id="tableBody"></tbody>
</table>
```

### 2. JavaScript Fetch API CRUD đầy đủ & Render dữ liệu vào Table

```javascript
const BASE_URL = 'http://localhost:8080/api/students';
// 1. GET & RENDER: Lấy danh sách đổ vào Table DOM
async function loadStudents() {
    const res = await fetch(BASE_URL);
    const students = await res.json();
    const tbody = document.getElementById('tableBody');
    tbody.innerHTML = ''; // Xóa dữ liệu cũ
    students.forEach(s => {
        tbody.innerHTML += `
            <tr>
                <td>${s.id}</td>
                <td>${s.name}</td>
                <td>${s.email}</td>
                <td>
                    <button onclick="deleteStudent(${s.id})">Xóa</button>
                    <button onclick="updateStudent(${s.id})">Sửa</button>
                </td>
            </tr>`;
    });
}
// 2. POST: Thêm mới sinh viên
async function createStudent(studentData, facultyId) {
    const res = await fetch(`${BASE_URL}?facultyId=${facultyId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(studentData)
    });
    const result = await res.json();
    loadStudents(); // Tải lại bảng
    return result;
}
// 3. PUT: Cập nhật sinh viên theo ID
async function updateStudent(id, studentData) {
    const res = await fetch(`${BASE_URL}/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(studentData)
    });
    const result = await res.json();
    loadStudents(); // Tải lại bảng
    return result;
}
// 4. DELETE: Xóa sinh viên theo ID
async function deleteStudent(id) {
    const res = await fetch(`${BASE_URL}/${id}`, { method: 'DELETE' });
    if (res.status === 204 || res.ok) {
        loadStudents(); // Tải lại bảng
    }
}
// Tự động gọi khi mở trang web
window.onload = loadStudents;
```

---

1. **Đề Quản lý Bán hàng:** `Faculty` $\rightarrow$ `Category` (Danh mục), `Student` $\rightarrow$ `Product` (Sản phẩm), `Subject` $\rightarrow$ `Tag` (Thẻ phân loại).
2. **Đề Quản lý Thư viện:** `Faculty` $\rightarrow$ `Publisher` (Nhà xuất bản), `Student` $\rightarrow$ `Book` (Sách), `Subject` $\rightarrow$ `Author` (Tác giả).
3. **Đề Quản lý Nhân sự:** `Faculty` $\rightarrow$ `Department` (Phòng ban), `Student` $\rightarrow$ `Employee` (Nhân viên), `Subject` $\rightarrow$ `Project` (Dự án).
