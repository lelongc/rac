# CẨM NANG TOÀN TẬP: GIẢI THÍCH CHI TIẾT MỌI THỨ TRONG CODE JPA (1-N VÀ N-N)
> **Môn học:** Công nghệ Web / Kiến trúc Phần mềm - IUH  
> **Giảng viên:** Thầy Trương Bá Phúc  
> **Dự án thực hành:** [b9_jpa_relationship_project](file:///d:/folder/rac/iuh/môn/hk1-4/cc-web-website-hld/truong/bt/t2/b9_jpa_relationship_project)

---

## 🗺️ TỔNG QUAN HỆ THỐNG: 3 THỰC THỂ & 2 MỐI QUAN HỆ

Dự án hiện tại kết hợp **cả 2 mối quan hệ kinh điển** trong một hệ thống quản lý đào tạo:
1. **Quan hệ 1 - Nhiều (1 - N):** 1 Khoa (`Faculty`) có Nhiều Sinh viên (`Student`).
2. **Quan hệ Nhiều - Nhiều (N - N):** 1 Sinh viên (`Student`) học Nhiều Môn học (`Subject`), và 1 Môn học có Nhiều Sinh viên đăng ký.

```text
 ┌──────────────┐          1 - N           ┌──────────────┐
 │   Faculty    │ ◄─────────────────────── │   Student    │
 └──────────────┘ (faculty_id ở Student)   └──────┬───────┘
                                                  │
                                                  │ N - N
                                                  ▼
                                      ┌───────────────────────┐
                                      │    student_subject    │ (Bảng trung gian)
                                      └───────────┬───────────┘
                                                  │
                                                  ▼
                                           ┌──────────────┐
                                           │   Subject    │
                                           └──────────────┘
```

---

## 🔍 PHẦN 1: GIẢI THÍCH CHI TIẾT TẦNG THỰC THỂ (ENTITY)

### 1.1. `Subject.java` (Thực thể Môn học - Bên Nghịch đảo / Inverse Side)

```java
@Entity
@Table(name = "subjects")
public class Subject {
```
- `@Entity`: Báo cho Spring Boot và Hibernate biết đây là một thực thể CSDL. Hibernate sẽ tự tạo bảng `subjects` trong MySQL.
- `@Table(name = "subjects")`: Đặt tên tường minh cho bảng trong MySQL là số nhiều (`subjects`).

```java
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 100)
    private String name; 

    @Column(length = 20, unique = true)
    private String code; 

    private int credits; 
```
- `@Id` & `@GeneratedValue(strategy = GenerationType.IDENTITY)`: Khai báo khóa chính tự động tăng (Auto Increment: 1, 2, 3...) do MySQL quản lý.
- `nullable = false`: Ràng buộc cột `name` không được phép `NULL`.
- `unique = true`: Mã môn học (ví dụ `CS101`, `SE202`) không được phép trùng lặp trong CSDL.

```java
    @ManyToMany(mappedBy = "subjects", fetch = FetchType.LAZY)
    @JsonIgnoreProperties("subjects")
    private Set<Student> students = new HashSet<>();
```
- **`@ManyToMany`**: Khai báo quan hệ Nhiều - Nhiều với thực thể `Student`.
- **`mappedBy = "subjects"` (CỰC KỲ QUAN TRỌNG)**:
  - Báo cho Hibernate biết rằng: *"Thực thể `Student` (thông qua trường `subjects`) mới là bên chủ sở hữu định nghĩa bảng trung gian"*.
  - **Mục đích:** Nếu không có `mappedBy`, Hibernate sẽ tự động tạo **2 bảng trung gian** riêng biệt (`student_subject` và `subject_student`) gây lỗi logic và lãng phí CSDL!
- **`fetch = FetchType.LAZY`**:
  - Khi bạn truy vấn 1 môn học, Hibernate **chưa vội load toàn bộ danh sách sinh viên** lên bộ nhớ ngay. Chỉ khi nào bạn thực sự gọi `.getStudents()` thì nó mới gửi câu lệnh SQL truy vấn. Điều này giúp tối ưu tốc độ và không gây nghẽn RAM.
- **`@JsonIgnoreProperties("subjects")` (XỬ LÝ BẪY VÒNG LẶP JSON)**:
  - Khi Spring Boot chuyển đối tượng `Subject` thành chuỗi JSON trả về cho trình duyệt, `Subject` chứa danh sách `students`, mỗi `Student` lại chứa danh sách `subjects`, rồi lại chứa `students`... $\rightarrow$ Lặp vô tận $\rightarrow$ Lỗi sập server `StackOverflowError`.
  - `@JsonIgnoreProperties("subjects")` ra lệnh: Khi hiển thị sinh viên trong môn học, **hãy bỏ qua danh sách môn học của sinh viên đó**, cắt đứt vòng lặp!
- **Tại sao dùng `Set<Student>` thay vì `List<Student>`?**
  - Trong quan hệ N-N, `Set` ngăn chặn việc 1 sinh viên bị thêm trùng lặp 2 lần vào cùng 1 môn học.
  - Hibernate tối ưu câu lệnh `DELETE` trên `Set` tốt hơn rất nhiều so với `List`.

```java
    // Helper method đồng bộ 2 chiều trong bộ nhớ Java
    public void addStudent(Student student) {
        this.students.add(student);
        student.getSubjects().add(this);
    }
```
- Khi thêm quan hệ giữa 2 đối tượng trong Java, phải thêm vào cả 2 đầu (`subject.students` và `student.subjects`) để đảm bảo dữ liệu trong RAM luôn nhất quán trước khi lưu xuống MySQL.

---

### 1.2. `Student.java` (Thực thể Sinh viên - Bên Chủ sở hữu / Owning Side)

```java
    // 1. Quan hệ với Khoa (1 - N)
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "faculty_id")
    @JsonBackReference
    private Faculty faculty;
```
- `@ManyToOne`: Nhiều sinh viên thuộc về 1 Khoa.
- `@JoinColumn(name = "faculty_id")`: Tên cột khóa ngoại thực tế trong bảng `students` là `faculty_id`.
- `@JsonBackReference`: Đi kèm với `@JsonManagedReference` ở `Faculty` để chặn lặp JSON chiều con trỏ ngược về cha.

```java
    // 2. Quan hệ với Môn học (N - N)
    @ManyToMany(fetch = FetchType.LAZY)
    @JoinTable(
        name = "student_subject",
        joinColumns = @JoinColumn(name = "student_id"),
        inverseJoinColumns = @JoinColumn(name = "subject_id")
    )
    @JsonIgnoreProperties("students")
    private Set<Subject> subjects = new HashSet<>();
```
- **`@JoinTable` (Bảng trung gian)**:
  - `name = "student_subject"`: Đặt tên cho bảng trung gian sẽ được tạo trong MySQL.
  - `joinColumns = @JoinColumn(name = "student_id")`: Cột khóa ngoại trỏ về ID của chính thực thể hiện tại (`Student`).
  - `inverseJoinColumns = @JoinColumn(name = "subject_id")`: Cột khóa ngoại trỏ về ID của thực thể đối tác (`Subject`).
- Cặp `(student_id, subject_id)` trong MySQL vừa đóng vai trò là **2 khóa ngoại**, vừa kết hợp lại làm **Khóa chính phức hợp (Composite Primary Key)** của bảng `student_subject`.

---

## ⚙️ PHẦN 2: GIẢI THÍCH TẦNG SERVICE & REPOSITORY

### 2.1. `SubjectRepository.java`
```java
@Repository
public interface SubjectRepository extends JpaRepository<Subject, Long> {
    Optional<Subject> findByCode(String code);
}
```
- Kế thừa `JpaRepository<Subject, Long>`: Tự động có sẵn toàn bộ hàm CRUD chuẩn:
  - `findAll()`: Lấy tất cả môn học (`SELECT * FROM subjects`).
  - `findById(id)`: Tìm theo ID.
  - `save(subject)`: Thêm mới hoặc cập nhật.
  - `delete(subject)`: Xóa môn học.
- `findByCode(code)`: Phương thức truy vấn thông minh (Derived Query), Spring Data JPA tự động dịch thành câu SQL: `SELECT * FROM subjects WHERE code = ?`.

---

### 2.2. `SubjectService.java` (Nghiệp vụ cốt lõi)

```java
    @Transactional
    public Subject enrollStudent(Long subjectId, Long studentId) {
        Subject subject = getSubjectById(subjectId);
        Student student = studentRepository.findById(studentId)
                .orElseThrow(() -> new RuntimeException("Student not found with ID: " + studentId));

        student.addSubject(subject);
        studentRepository.save(student);

        return subject;
    }
```
- **Tại sao phải có `@Transactional`?**
  - Nghiệp vụ đăng ký môn học tác động đến 2 thực thể và ghi dữ liệu vào bảng trung gian `student_subject`.
  - `@Transactional` đảm bảo tính toàn vẹn (ACID): Nếu một bước thất bại (ví dụ mất kết nối mạng giữa chừng), toàn bộ thao tác sẽ được rollback (hoàn tác), không để lại dữ liệu rác.
- **Tại sao gọi `studentRepository.save(student)` mà không gọi subjectRepository?**
  - Vì `Student` là bên **chủ sở hữu (Owning Side)** giữ cấu hình `@JoinTable`. Khi lưu `Student`, Hibernate sẽ tự động tạo dòng mới trong bảng `student_subject`.

```java
    public void deleteSubject(Long id) {
        Subject subject = getSubjectById(id);
        // Ngắt liên kết trước khi xóa để tránh lỗi ràng buộc khóa ngoại (Foreign Key Constraint)
        for (Student student : subject.getStudents()) {
            student.getSubjects().remove(subject);
        }
        subjectRepository.delete(subject);
    }
```
- Nếu một môn học đang có sinh viên đăng ký trong bảng `student_subject`, nếu bạn xóa ngang môn học thì MySQL sẽ báo lỗi vi phạm khóa ngoại `Cannot delete or update a parent row: a foreign key constraint fails`.
- Đoạn vòng lặp `remove` này giúp gỡ bỏ các liên kết trong bảng trung gian trước khi thực hiện lệnh xóa môn học an toàn.

---

## 🌐 PHẦN 3: GIẢI THÍCH TẦNG CONTROLLER (REST API)

Tầng Controller chịu trách nhiệm nhận request HTTP từ Client (Postman, Browser, Mobile App), gọi Service xử lý và trả về JSON.

```java
@RestController
@RequestMapping("/api/subjects")
public class SubjectController {
```
- `@RestController`: Đánh dấu class này là Controller theo chuẩn REST, tự động biến kết quả trả về của các hàm thành định dạng JSON.
- `@RequestMapping("/api/subjects")`: Định nghĩa đường dẫn gốc (Base URL) cho tất cả các API môn học.

```java
    // 1. Lấy danh sách tất cả môn học (kèm sinh viên đang học)
    @GetMapping
    public List<Subject> getAll() {
        return subjectService.getAllSubjects();
    }

    // 2. Thêm môn học mới
    @PostMapping
    public ResponseEntity<Subject> create(@RequestBody Subject subject) {
        return new ResponseEntity<>(subjectService.createSubject(subject), HttpStatus.CREATED);
    }

    // 3. ĐĂNG KÝ MÔN HỌC (QUAN HỆ NHIỀU - NHIỀU):
    // POST /api/subjects/1/students/2
    @PostMapping("/{subjectId}/students/{studentId}")
    public ResponseEntity<Subject> enrollStudent(
            @PathVariable Long subjectId,
            @PathVariable Long studentId) {
        return ResponseEntity.ok(subjectService.enrollStudent(subjectId, studentId));
    }
```
- `@PathVariable`: Lấy giá trị trực tiếp từ trên thanh URL (`{subjectId}` và `{studentId}`).
- `HttpStatus.CREATED` (Mã 201): Chuẩn REST thông báo đối tượng đã được tạo mới thành công trong CSDL.

---

## 🗄️ PHẦN 4: HÌNH DẠNG CƠ SỞ DỮ LIỆU MYSQL SAU KHI CHẠY

Khi dự án khởi động, Hibernate sẽ tự tạo **4 bảng** trong CSDL `jpa_relationship_db`:

1. **Bảng `faculties` (Khoa):**
   - `id` (PK)
   - `name`
2. **Bảng `students` (Sinh viên):**
   - `id` (PK)
   - `name`, `email`, `age`
   - `faculty_id` (FK trỏ sang `faculties.id`)
3. **Bảng `subjects` (Môn học):**
   - `id` (PK)
   - `name`, `code`, `credits`
4. **Bảng trung gian `student_subject` (Quan hệ N - N):**
   - `student_id` (FK trỏ sang `students.id`)
   - `subject_id` (FK trỏ sang `subjects.id`)
   - Khóa chính: `PRIMARY KEY (student_id, subject_id)`

---

## 🎯 PHẦN 5: BỘ CÂU HỎI VẤN ĐÁP CỦA THẦY VÀ CÂU TRẢ LỜI LẤY ĐIỂM 10

### ❓ Câu 1: "Tại sao trong CSDL quan hệ, quan hệ N-N bắt buộc phải tách ra bảng trung gian?"
> **Trả lời:**  
> *"Dạ thưa Thầy, vì theo chuẩn hóa dữ liệu 1NF (First Normal Form), một ô dữ liệu trong bảng không được phép chứa một danh sách nhiều giá trị. Nếu bảng Sinh viên lưu danh sách mã môn, hoặc bảng Môn học lưu danh sách mã sinh viên thì sẽ vi phạm tính nguyên tử và gây trùng lặp dữ liệu nghiêm trọng. Do đó, giải pháp chuẩn của CSDL quan hệ là tách thành bảng trung gian chứa các cặp khóa ngoại `(student_id, subject_id)`."*

### ❓ Câu 2: "Tại sao ở `Subject` lại dùng `mappedBy = "subjects"` mà ở `Student` lại dùng `@JoinTable`?"
> **Trả lời:**  
> *"Dạ thưa Thầy, trong JPA cần phân biệt bên Chủ sở hữu (Owning side) và bên Nghịch đảo (Inverse side):*  
> *- Bên nào có `@JoinTable` (ở đây là `Student`) là bên chủ sở hữu trực tiếp quản lý bảng trung gian.*  
> *- Bên đối tác (`Subject`) phải dùng `mappedBy = "subjects"` để báo cho Hibernate biết liên kết này đã được cấu hình bên kia rồi, tránh việc Hibernate tự động sinh thêm bảng trung gian thứ hai thừa thãi."*

### ❓ Câu 3: "Tại sao ở bài 1-N dùng `@JsonManagedReference` / `@JsonBackReference`, nhưng ở bài N-N lại dùng `@JsonIgnoreProperties`?"
> **Trả lời:**  
> *"Dạ thưa Thầy:*  
> *- `@JsonManagedReference` và `@JsonBackReference` chỉ áp dụng cho quan hệ có cấp bậc phân cấp rõ ràng là Cha - Con (1-N, ví dụ Khoa - Sinh viên).*  
> *- Còn quan hệ Nhiều - Nhiều là quan hệ bình đẳng ngang hàng 2 chiều (Sinh viên chứa Môn, Môn cũng chứa Sinh viên). Khi đó, dùng `@JsonIgnoreProperties("students")` và `@JsonIgnoreProperties("subjects")` là giải pháp chuẩn và an toàn nhất để ngắt vòng lặp vô tận (Circular Reference) khi chuyển sang JSON."*

### ❓ Câu 4: "Tại sao em dùng `Set<Subject>` mà không dùng `List<Subject>`?"
> **Trả lời:**  
> *"Dạ thưa Thầy, em dùng `Set` vì 2 lý do:*  
> *1. **Về mặt nghiệp vụ:** `Set` không cho phép phần tử trùng lặp, đảm bảo 1 sinh viên không thể đăng ký 1 môn học 2 lần.*  
> *2. **Về mặt kỹ thuật Hibernate:** Với `List`, khi xóa 1 phần tử trong quan hệ N-N, Hibernate thường phải xóa toàn bộ bảng trung gian của sinh viên đó rồi insert lại từ đầu. Với `Set`, Hibernate chỉ thực hiện đúng duy nhất 1 câu lệnh `DELETE WHERE student_id = ? AND subject_id = ?`, tối ưu hiệu năng vượt trội."*
