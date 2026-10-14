# GIẢI THÍCH CHI TIẾT: QUAN HỆ NHIỀU - NHIỀU (MANY-TO-MANY) GIỮA SINH VIÊN VÀ MÔN HỌC

> **Môn học:** Công nghệ Web / Kiến trúc Phần mềm - IUH  
> **Giảng viên:** Thầy Trương Bá Phúc  
> **Dự án mới (N-N):** [d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\t2\b10_jpa_student_subject_many_to_many](file:///d:/folder/rac/iuh/môn/hk1-4/cc-web-website-hld/truong/bt/t2/b10_jpa_student_subject_many_to_many)  
> **Dự án cũ (1-N giữ nguyên 100%):** [d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\t2\b9_jpa_relationship_project](file:///d:/folder/rac/iuh/môn/hk1-4/cc-web-website-hld/truong/bt/t2/b9_jpa_relationship_project)

---

## ⚡ TỔNG QUAN: TIẾN TRÌNH NÂNG CẤP QUA 3 BÀI HỌC

| Cấp độ | Tên bài | Số bảng CSDL | Bản chất kỹ thuật & Quan hệ |
| :--- | :--- | :---: | :--- |
| **Cấp 1** | **Bài 8 (Demojpa)** | 1 bảng (`students`) | Thực thể độc lập, không có quan hệ khóa ngoại. |
| **Cấp 2** | **Bài 9 (Relationship 1-N)** | 2 bảng (`faculties` - `students`) | **1 - Nhiều (1 Khoa có Nhiều Sinh viên)**. Khóa ngoại `faculty_id` nằm trực tiếp trong bảng `students`. |
| **Cấp 3** | **Bài 10 (Many-to-Many N-N)** | **3 bảng** (`students`, `subjects`, `student_subject`) | **Nhiều - Nhiều (1 SV học Nhiều Môn, 1 Môn có Nhiều SV)**. Bắt buộc phát sinh **Bảng trung gian (Join Table)** để liên kết 2 bảng. |

---

## 1. TẠI SAO QUAN HỆ NHIỀU - NHIỀU BẮT BUỘC PHẢI CÓ BẢNG TRUNG GIAN?

Trong CSDL quan hệ (MySQL):
- Một dòng trong bảng `students` không thể chứa danh sách nhiều ID môn học (vi phạm chuẩn hóa dữ liệu 1NF).
- Một dòng trong bảng `subjects` cũng không thể chứa danh sách nhiều ID sinh viên.
- 👉 **Giải pháp duy nhất của CSDL RDBMS:** Sinh ra một bảng thứ 3 ở giữa gọi là **Bảng trung gian (Join Table / Junction Table)** tên là **`student_subject`**:
  - `student_id` (Khóa ngoại trỏ sang `students.id`)
  - `subject_id` (Khóa ngoại trỏ sang `subjects.id`)
  - Cặp `(student_id, subject_id)` tạo thành Khóa chính phức hợp (Composite Primary Key), đảm bảo 1 sinh viên không bị trùng môn học 2 lần.

---

## 2. PHÂN TÍCH CHI TIẾT TỪNG ANNOTATION & ĐOẠN CODE THEN CHỐT

### 2.1. Tại `Student.java` (Bên Chủ sở hữu quan hệ - Owning Side):
```java
// 1. @ManyToMany: Khai báo quan hệ nhiều - nhiều giữa Student và Subject
// 2. FetchType.LAZY: Chỉ load danh sách môn học khi thực sự cần (tối ưu hiệu năng)
@ManyToMany(fetch = FetchType.LAZY)
@JoinTable(
    name = "student_subject",                          // Tên bảng trung gian trong MySQL
    joinColumns = @JoinColumn(name = "student_id"),     // Cột khóa ngoại trỏ về bảng students (chính nó)
    inverseJoinColumns = @JoinColumn(name = "subject_id")// Cột khóa ngoại trỏ về bảng subjects (đối tác)
)
@JsonIgnoreProperties("students") // Ngăn lặp vòng vô tận khi xuất JSON
private Set<Subject> subjects = new HashSet<>();
```

> **📌 Tại sao dùng `Set` thay vì `List`?**  
> Trong quan hệ `@ManyToMany`, Hibernate khuyến nghị dùng `Set<Subject>` thay vì `List<Subject>` để đảm bảo tính duy nhất (1 sinh viên không đăng ký 1 môn học 2 lần) và Hibernate sinh ra các câu lệnh SQL `DELETE / INSERT` tối ưu nhất.

---

### 2.2. Tại `Subject.java` (Bên Bị sở hữu - Inverse Side):
```java
// 1. mappedBy = "subjects": Trỏ chính xác tới tên trường "subjects" bên Student
//    Ý nghĩa: Báo cho Hibernate biết bên Student đã cấu hình @JoinTable rồi,
//    Hibernate ĐỪNG tự động tạo thêm một bảng trung gian thứ 2 (subject_student)!
@ManyToMany(mappedBy = "subjects", fetch = FetchType.LAZY)
@JsonIgnoreProperties("subjects") // Cắt đứt vòng lặp JSON
private Set<Student> students = new HashSet<>();

// Helper method đồng bộ 2 chiều trong bộ nhớ Java
public void addStudent(Student student) {
    this.students.add(student);
    student.getSubjects().add(this);
}
```

---

### 2.3. Bí quyết giải quyết Bẫy lặp vô tận (Circular Reference) trong N - N:
- Ở bài 1 - Nhiều (Khoa - Sinh viên), ta dùng `@JsonManagedReference` và `@JsonBackReference` vì quan hệ có cấp bậc Cha - Con rõ ràng.
- Nhưng ở quan hệ **Nhiều - Nhiều**, hai thực thể **bình đẳng ngang hàng** nhau (Sinh viên có danh sách Môn học, Môn học cũng có danh sách Sinh viên). Nếu dùng Reference sẽ bị lỗi cú pháp.
- 👉 **Giải pháp chuẩn:** Dùng **`@JsonIgnoreProperties`**:
  - Tại `Student`: `@JsonIgnoreProperties("students")` $\rightarrow$ Khi xuất sinh viên có kèm môn học, bên trong môn học sẽ KHÔNG lặp lại danh sách sinh viên nữa.
  - Tại `Subject`: `@JsonIgnoreProperties("subjects")` $\rightarrow$ Khi xuất môn học có kèm sinh viên, bên trong sinh viên sẽ KHÔNG lặp lại danh sách môn học nữa.
  - Triệt tiêu hoàn toàn lỗi tràn bộ nhớ `StackOverflowError`!

---

## 3. CÁC API RESTful MỚI PHỤC VỤ KIỂM THỬ

| Method | Endpoint | Chức năng | Body JSON mẫu |
| :---: | :--- | :--- | :--- |
| **POST** | `/api/subjects` | Thêm môn học mới | `{"name":"Lap Trinh Java","code":"CS101","credits":3}` |
| **GET** | `/api/subjects` | Xem tất cả môn học (kèm sinh viên) | Không cần |
| **GET** | `/api/subjects/{id}` | Xem chi tiết 1 môn học | Không cần |
| **POST** | `/api/subjects/{subjectId}/students/{studentId}` | **Đăng ký môn học cho sinh viên** | Không cần (truyền ID trên URL) |
| **DELETE** | `/api/subjects/{subjectId}/students/{studentId}` | Hủy môn học của sinh viên | Không cần (truyền ID trên URL) |
| **GET** | `/api/students/{id}` | Xem sinh viên (kèm danh sách môn đã học) | Không cần |

---

## 4. HƯỚNG DẪN IMPORT VÀ CHẠY TRONG ECLIPSE

1. Mở Eclipse $\rightarrow$ **File** $\rightarrow$ **Import...**
2. Chọn **Maven** $\rightarrow$ **Existing Maven Projects** $\rightarrow$ Bấm **Next**.
3. Tại ô **Root Directory**, bấm **Browse...** và trỏ đến thư mục:  
   `d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\t2\b10_jpa_student_subject_many_to_many`
4. Bấm **Finish**.
5. Mở file `DemojpaApplication.java` $\rightarrow$ Chuột phải $\rightarrow$ **Run As** $\rightarrow$ **Spring Boot App**.
6. Vào MySQL Workbench refresh CSDL `b10_student_subject_db`, bạn sẽ thấy xuất hiện ngay **3 bảng**:
   - `faculties`
   - `students`
   - `subjects`
   - `student_subject` (Bảng trung gian tự sinh)

---

## 5. CÁC LỆNH CURL TEST TRỰC TIẾP QUA TERMINAL / CMD

### Bước 1: Tạo môn học
```bash
curl -X POST "http://localhost:8080/api/subjects" -H "Content-Type: application/json" -d "{\"name\":\"Lap Trinh Java\",\"code\":\"CS101\",\"credits\":3}"
curl -X POST "http://localhost:8080/api/subjects" -H "Content-Type: application/json" -d "{\"name\":\"Kien Truc Phan Mem\",\"code\":\"SE202\",\"credits\":4}"
```

### Bước 2: Tạo sinh viên (thuộc Khoa CNTT - facultyId: 1)
```bash
curl -X POST "http://localhost:8080/api/students" -H "Content-Type: application/json" -d "{\"name\":\"Nguyen Van An\",\"email\":\"an@example.com\",\"age\":20,\"facultyId\":1}"
curl -X POST "http://localhost:8080/api/students" -H "Content-Type: application/json" -d "{\"name\":\"Tran Thi Bich\",\"email\":\"bich@example.com\",\"age\":21,\"facultyId\":1}"
```

### Bước 3: Đăng ký môn học (Nhiều - Nhiều):
```bash
# Cho sinh viên 1 học môn Java (subject 1):
curl -X POST "http://localhost:8080/api/subjects/1/students/1"

# Cho sinh viên 1 học tiếp môn Kiến trúc phần mềm (subject 2):
curl -X POST "http://localhost:8080/api/subjects/2/students/1"

# Cho sinh viên 2 cũng học môn Java (subject 1):
curl -X POST "http://localhost:8080/api/subjects/1/students/2"
```

### Bước 4: Kiểm tra kết quả trong MySQL:
```sql
USE b10_student_subject_db;

-- Xem bảng trung gian tự động lưu cặp ID:
SELECT * FROM student_subject;

-- Xem kết quả nối 3 bảng trực quan:
SELECT s.name AS SinhVien, sub.name AS MonHoc, sub.credits AS SoTinChi
FROM students s
JOIN student_subject ss ON s.id = ss.student_id
JOIN subjects sub ON sub.id = ss.subject_id;
```

---

## 🎯 KỊCH BẢN TRẢ LỜI THẦY PHÚC LẤY ĐIỂM 10 TUYỆT ĐỐI

> *"Thưa Thầy, để mô hình hóa quan hệ Nhiều - Nhiều giữa Sinh viên và Môn học:*  
>  
> *1. **Về CSDL:** CSDL quan hệ không thể nối trực tiếp N-N, nên Hibernate tự động tạo bảng trung gian `student_subject` với 2 khóa ngoại `student_id` và `subject_id` thông qua annotation `@JoinTable` đặt bên Entity `Student`.*  
>  
> *2. **Về mappedBy:** Ở Entity `Subject`, em dùng `@ManyToMany(mappedBy = "subjects")` để xác định `Subject` là bên inverse, giúp Hibernate **không sinh ra bảng trung gian thứ hai** bị trùng lặp.*  
>  
> *3. **Về xử lý lặp vô tận JSON:** Em sử dụng `@JsonIgnoreProperties` ở cả 2 đầu để khi gọi REST API xuất thông tin sinh viên kèm môn học (hoặc môn học kèm sinh viên) không bị đệ quy vòng tròn gây lỗi `StackOverflowError`.*  
>  
> *4. **Về cấu trúc tập hợp:** Em sử dụng `Set<Subject>` thay vì `List<Subject>` để đảm bảo tính duy nhất của dữ liệu đăng ký môn học và tối ưu câu lệnh SQL của Hibernate."*
