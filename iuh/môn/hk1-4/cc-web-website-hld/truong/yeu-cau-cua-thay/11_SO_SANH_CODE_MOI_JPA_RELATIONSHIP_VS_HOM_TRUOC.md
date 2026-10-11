# SO SÁNH ĐỐI CHIẾU: CODE MỚI (JPA RELATIONSHIP) VS CODE HÔM KIA (DEMOJPA B8)
> **Dành cho câu hỏi của Thầy Trương Bá Phúc**: *"Code ngày hôm nay khác gì với code hôm kia? Mục đích của những điểm khác biệt đó là gì?"*  
> **Thư mục code mới**: [d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\thaygui\2\jpa_relationship-main\demojpa](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/thaygui/2/jpa_relationship-main/demojpa)  
> **Thư mục code hôm kia**: [d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\thaygui\demojpa](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/thaygui/demojpa) (hoặc `b8_demojpa_student`)

---

## ⚡ TÓM TẮT NHANH 1 PHÚT ĐỂ TRẢ LỜI THẦY LẤY 2 ĐIỂM CỘNG

Khi Thầy hỏi: *"Code hôm nay khác gì hôm kia?"*, bạn trả lời gọn đúng **5 điểm then chốt** sau:

1. **Từ 1 bảng đơn lẻ $\rightarrow$ Quan hệ 2 bảng (1-N)**: Hôm kia chỉ có duy nhất bảng `Student` độc lập; hôm nay có thêm `Faculty` (Khoa) với quan hệ 1 Khoa - Nhiều Sinh viên (`@OneToMany` và `@ManyToOne`).
2. **Xuất hiện tầng DTO mới (`StudentRequest`)**: Hôm kia Client gửi trực tiếp Entity `Student`; hôm nay có thêm DTO nhận `facultyId` để Client tạo sinh viên chỉ cần gửi mã khoa, không phải gửi nguyên cả đối tượng `Faculty`.
3. **Cấu hình `mappedBy` và Khóa ngoại `@JoinColumn`**: Phía `Student` giữ khóa ngoại `faculty_id`; phía `Faculty` bắt buộc dùng `mappedBy = "faculty"` để Hibernate **không tự sinh ra bảng trung gian (Join Table)** thừa thãi.
4. **Triệt tiêu bẫy lặp vòng Circular Reference**: Dùng cặp Annotation `@JsonManagedReference` (ở Faculty) và `@JsonBackReference` (ở Student) để khi xuất dữ liệu JSON không bị đệ quy vô tận gây sập server (`StackOverflowError`).
5. **Đồng bộ vòng đời và xử lý Dữ liệu mồ côi (Orphan Data)**: Dùng `cascade = CascadeType.ALL` và `orphanRemoval = true` để khi thao tác trên Khoa thì sinh viên tự động đồng bộ theo, tránh sinh viên bị mồ côi khi Khoa bị tác động.

---

## 📊 BẢNG SO SÁNH TRỰC DIỆN TỪNG TẦNG CODE

| Tiêu chí | Code hôm kia (Bài 8 - 04/10) | Code mới hôm nay (JPA Relationship - 11/10) | Mục đích kỹ thuật |
| :--- | :--- | :--- | :--- |
| **Số lượng Thực thể (Entity)** | Chỉ có **1 Entity**: `Student` đơn lẻ (chỉ có id, name, email, phone). | Có **2 Entity liên kết**: `Faculty` (Bên 1) và `Student` (Bên Nhiều). | Mô hình hóa mối quan hệ thực tế giữa các thực thể trong cơ sở dữ liệu. |
| **Tầng DTO (Data Transfer Object)** | ❌ **Không có DTO**. Controller nhận trực tiếp `@RequestBody Student`. | ✅ **Có thêm package `dto` với `StudentRequest.java`** chứa `Long facultyId`. | Tách biệt Model CSDL với dữ liệu truyền nhận, Client chỉ cần truyền `facultyId` rất tiện lợi và an toàn. |
| **Khóa ngoại & Quan hệ JPA** | ❌ Không có quan hệ nào. | ✅ `@ManyToOne` + `@JoinColumn(name = "faculty_id")` ở `Student`.<br>✅ `@OneToMany(mappedBy = "faculty")` ở `Faculty`. | Xác định rõ bên giữ khóa ngoại (`Student`) và tránh việc Hibernate tự tạo bảng trung gian không cần thiết. |
| **Xử lý lặp vô tận (JSON Recursion)** | ❌ Không có (vì không có quan hệ 2 chiều). | ✅ `@JsonManagedReference` (ở Faculty)<br>✅ `@JsonBackReference` (ở Student). | Ngăn chặn Jackson render JSON lẩn vòng đệ quy gây lỗi `StackOverflowError`. |
| **Cascade & Dữ liệu mồ côi** | ❌ Không có Cascade. | ✅ `cascade = CascadeType.ALL`<br>✅ `orphanRemoval = true`. | Tự động đồng bộ thêm/xóa/sửa cha-con trong 1 Transaction, tránh sinh viên mồ côi dữ liệu khi xóa khoa. |
| **Phương thức tiện ích (Helper Method)** | ❌ Không có. | ✅ Có `addStudent()` và `removeStudent()` trong `Faculty.java`. | Đảm bảo tính nhất quán dữ liệu cả 2 chiều trong bộ nhớ Java trước khi commit vào MySQL. |
| **Tầng Service** | `StudentService` chỉ tiêm 1 `StudentRepository`. | `StudentService` tiêm **cả 2 Repository**: `StudentRepository` + `FacultyRepository`. | Phải kiểm tra Khoa có tồn tại hay không trước khi gán cho Sinh viên. |
| **Derived Query Method** | Tìm kiếm theo tên `findByNameContainingIgnoreCase`. | Bổ sung thêm: `List<Student> findByFacultyId(Long facultyId);` | Lấy danh sách tất cả sinh viên thuộc một khoa bất kỳ mà không cần viết câu lệnh SQL nào. |

---

## 🔍 CHI TIẾT 3 ĐOẠN CODE ĐẶC BIỆT NHẤT TRONG DỰ ÁN MỚI

### 1. Tại `Faculty.java` (Bên 1 - Cha):
```java
// 1. mappedBy: Báo cho Hibernate biết bên "faculty" của Student đang giữ khóa ngoại (tránh tạo bảng trung gian)
// 2. cascade = ALL: Lưu/xóa Khoa thì Sinh viên đi kèm tự động lưu/xóa theo
// 3. orphanRemoval: Gỡ sinh viên ra khỏi list là CSDL tự xóa dòng sinh viên đó (tránh mồ côi)
// 4. @JsonManagedReference: Cho phép Jackson serialize danh sách sinh viên ra JSON
@OneToMany(mappedBy = "faculty", cascade = CascadeType.ALL, orphanRemoval = true)
@JsonManagedReference
private List<Student> students = new ArrayList<>();

// Hàm helper giữ tính nhất quán 2 chiều
public void addStudent(Student student) {
    students.add(student);
    student.setFaculty(this);
}
```

### 2. Tại `Student.java` (Bên Nhiều - Con giữ khóa ngoại):
```java
// 1. FetchType.LAZY: Khi load Student thì chưa cần load cả Khoa lên ngay (tối ưu tốc độ)
// 2. @JoinColumn: Tên cột khóa ngoại thực tế trong bảng students là "faculty_id"
// 3. @JsonBackReference: Chặn không serialize ngược lại Khoa, triệt tiêu lỗi lặp vòng Circular Reference
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "faculty_id")
@JsonBackReference
private Faculty faculty;
```

### 3. Tại `StudentService.java` (Nghiệp vụ liên kết 2 bảng):
```java
public Student createStudent(StudentRequest request) {
    // Bước 1: Tìm Khoa dựa vào facultyId gửi lên từ DTO. Không có thì báo lỗi ngay
    Faculty faculty = facultyRepository.findById(request.getFacultyId())
            .orElseThrow(() -> new RuntimeException("Faculty not found with ID: " + request.getFacultyId()));

    // Bước 2: Tạo sinh viên mới và gán đối tượng Khoa vào
    Student student = new Student(request.getName(), request.getEmail(), request.getAge());
    student.setFaculty(faculty);

    // Bước 3: Lưu xuống CSDL
    return studentRepository.save(student);
}
```

---

## 🎯 KỊCH BẢN NÓI TRƯỚC LỚP / KHI THẦY HỎI VẤN ĐÁP

> *"Dạ thưa Thầy, code hôm nay khác code hôm kia ở 3 điểm mấu chốt:*  
> 
> *1. **Về kiến trúc thực thể**: Hôm kia chỉ có 1 bảng `Student` độc lập. Hôm nay là quan hệ 1-N hoàn chỉnh giữa `Faculty` và `Student`. Phía Student dùng `@ManyToOne` giữ khóa ngoại `faculty_id`, phía Faculty dùng `@OneToMany(mappedBy = "faculty")` để Hibernate **không tạo thêm bảng trung gian**.*  
> 
> *2. **Về giải quyết bẫy Circular Reference**: Code hôm nay dùng cặp Annotation `@JsonManagedReference` và `@JsonBackReference` để khi gọi REST API trả về JSON không bị lặp vô tận gây lỗi `StackOverflowError`.*  
> 
> *3. **Về DTO và nghiệp vụ**: Code có thêm lớp `StudentRequest` trong package `dto` giúp Client chỉ cần truyền `facultyId`. Trong `StudentService`, Thầy tiêm cả 2 repository để kiểm tra sự tồn tại của Khoa trước khi gán và lưu Sinh viên; đồng thời dùng `CascadeType.ALL` và `orphanRemoval` để tự động dọn dẹp dữ liệu mồ côi.*"
