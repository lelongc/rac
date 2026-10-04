# PHÂN TÍCH CHI TIẾT BÀI GIẢNG CA 2 (04/10/2026) & DỰ ÁN DEMOJPA (STUDENT WEB)

> **Môn học**: Kiến trúc & Thiết kế Phần mềm / Công nghệ Web - Web Service (IUH)  
> **Giảng viên**: Thầy Trương Bá Phúc  
> **Video nguồn**: `Videos/2026-10-04 18-40-59.mp4` (Thời lượng: 11 phút 58 giây)  
> **Dự án thực hành gốc của thầy**: [d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\thaygui\demojpa](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/thaygui/demojpa)  
> **Bản hoàn thiện đồng bộ tại Bài tập T2**: [d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\t2\b8_demojpa_student](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/bt/t2/b8_demojpa_student)  

---

## MỤC LỤC
1. [TỔNG KẾT NHANH 4 CHỈ ĐẠO CỐT TỬ CỦA THẦY TRONG VIDEO CA 2](#1-tổng-kết-nhanh-4-chỉ-đạo-cốt-tử-của-thầy-trong-video-ca-2)
2. [BẢNG BÓC BĂNG ĐỐI CHIẾU CHI TIẾT TỪNG MỐC THỜI GIAN](#2-bảng-bóc-băng-đối-chiếu-chi-tiết-từng-mốc-thời-gian)
3. [PHÂN TÍCH CHUYÊN SÂU 5 TRỌNG ĐIỂM KIẾN THỨC THẦY DẠY](#3-phân-tích-chuyên-sâu-5-trọng-điểm-kiến-thức-thầy-dạy)
   - [Trọng điểm 1: Hai package mới "entity" và "repository"](#trọng-điểm-1-hai-package-mới-entity-và-repository)
   - [Trọng điểm 2: Lớp Entity Student và các Annotation ràng buộc CSDL](#trọng-điểm-2-lớp-entity-student-và-các-annotation-ràng-buộc-csdl)
   - [Trọng điểm 3: Khái niệm "CÁI KHO" - JpaRepository](#trọng-điểm-3-khái-niệm-cái-kho---jparepository)
   - [Trọng điểm 4: Tầng Service điều phối nghiệp vụ](#trọng-điểm-4-tầng-service-điều-phối-nghiệp-vụ)
   - [Trọng điểm 5: Yêu cầu viết giao diện Web và tính điểm thực hành](#trọng-điểm-5-yêu-cầu-viết-giao-diện-web-và-tính-điểm-thực-hành)
4. [CHI TIẾT MÃ NGUỒN DỰ ÁN DEMOJPA ĐÃ ĐƯỢC XÂY DỰNG HOÀN THIỆN](#4-chi-tiết-mã-nguồn-dự-án-demojpa-đã-được-xây-dựng-hoàn-thiện)
5. [HƯỚNG DẪN TỪNG BƯỚC IMPORT VÀO ECLIPSE & CHẠY THỰC TẾ](#5-hướng-dẫn-từng-bước-import-vào-eclipse--chạy-thực-tế)

---

## 1. TỔNG KẾT NHANH 4 CHỈ ĐẠO CỐT TỬ CỦA THẦY TRONG VIDEO CA 2

1. **Chuyển từ Model thường sang Entity JPA**: Trước đây ở B1 - B6, class Java chỉ là Model lưu RAM tạm thời. Từ hôm nay, class được gắn `@Entity`, Hibernate sẽ **tự động biến class thành bảng CSDL trong MySQL**, không cần phải gõ lệnh SQL bằng tay.
2. **Khái niệm "CÁI KHO" (Repository)**: Thầy ví von `StudentRepository extends JpaRepository<Student, Long>` chính là một "cái kho". Cần lấy dữ liệu hay cất dữ liệu chỉ cần gọi các hàm có sẵn của kho: `findAll()`, `findById()`, `save()`, `deleteById()`.
3. **Mô hình luồng chuẩn**: `Controller` (nhận request) $\rightarrow$ `Service` (nghiệp vụ) $\rightarrow$ `Repository` ("Cái kho" truy vấn CSDL) $\rightarrow$ Trả dữ liệu JSON về cho Client.
4. **YÊU CẦU CHẤM ĐIỂM**: Thầy yêu cầu: *"Bây giờ các bạn viết giao diện cho nó, để nó load mấy cái này lên... Thầy tính điểm mấy cái phần này nhé các bạn nhé!"*. Phải có trang web hiển thị bảng danh sách sinh viên, có chức năng thêm/sửa/xóa sinh viên trực quan.

---

## 2. BẢNG BÓC BĂNG ĐỐI CHIẾU CHI TIẾT TỪNG MỐC THỜI GIAN

| Mốc thời gian | Lời ghi âm của Thầy Trương Bá Phúc | Diễn giải chuẩn hóa chuyên ngành |
| :--- | :--- | :--- |
| `00:26 - 00:44` | *Các bạn thấy Eclipse của thầy chưa? Các bạn nghe giảng không cần phải quay gì đâu, tập trung nghe thầy hướng dẫn...* | Thầy chia sẻ màn hình Eclipse của thầy lên Zoom, yêu cầu sinh viên tập trung nghe giảng thay vì loay hoay quay màn hình. |
| `01:03 - 01:30` | *Bây giờ chúng ta mở cái package mới là entity. Hôm bữa mình học là model đúng không? Rồi bây giờ mình có cái mới là entity. Rồi có cái mới nữa là repository. Hai cái mới này.* | **Cấu trúc package mới trong Spring Data JPA:**<br>- Package `entity` (hoặc `model`): Chứa các lớp ánh xạ bảng CSDL.<br>- Package `repository`: Chứa các Interface kế thừa `JpaRepository`. |
| `01:31 - 02:17` | *Cái mới này nó giống như cái model hôm trước, có lớp Student, có thuộc tính Student: id, name, email. Mấy cái constructor, getter, setter bình thường đúng không?* | Cấu trúc cơ bản của Class POJO vẫn giữ nguyên thuộc tính `id`, `name`, `email` và getter/setter. |
| `02:17 - 03:26` | *Hôm nay có cái này mới này: Khi mà chúng ta gắn cái chữ @Entity vô là nó sẽ tự động... Từ nay mình không cần viết lệnh SQL nữa, mình lập trình bằng Java luôn, cái này rất là hay.* | **Cơ chế ORM (Object-Relational Mapping):** Khi đánh dấu `@Entity`, Hibernate tự động sinh cấu trúc bảng trong MySQL tương ứng với Class Java. Lập trình viên thao tác hoàn toàn bằng OOP. |
| `04:09 - 05:16` | *Chúng ta muốn cái cột id là khóa chính thì gắn @Id, @GeneratedValue nó làm tự động cho mình. Muốn cột name có chiều dài là 100, nullable là false (bắt buộc nhập dữ liệu vô), thì gắn @Column(length = 100, nullable = false)...* | **Các Annotation ràng buộc dữ liệu JPA:**<br>- `@Id` + `@GeneratedValue(strategy = IDENTITY)`: Khóa chính tự tăng (Auto Increment).<br>- `@Column(length = 100, nullable = false)`: Độ dài tối đa 100 ký tự, cấm giá trị `NULL`. |
| `05:16 - 05:43` | *Tương tự, unique = true nghĩa là cột này dữ liệu nó duy nhất, không cho phép trùng... Mấy cái ràng buộc này có mười mấy cái, các bạn tự đọc thêm tài liệu.* | `@Column(unique = true)` trên trường `email` để đảm bảo không có 2 sinh viên trùng email trong hệ thống. |
| `08:42 - 09:11` | *Các bạn vô Service. Service thì mình học rồi... Nó muốn lấy student thì nó trả cái gì, save student nó trả cái gì...* | Lớp `Service` đóng vai trò tầng trung gian xử lý logic nghiệp vụ và giao tiếp với CSDL qua Repository. |
| `09:11 - 10:12` | *Có cái mới này: Repository là cái gì? Là một cái kho! Cái StudentRepository là cái kho cho Student. Interface này kế thừa JpaRepository. Trong Service mình tạo một đối tượng kho...* | **Định nghĩa Repository theo lời thầy:** Interface `StudentRepository extends JpaRepository<Student, Long>` là **"Cái kho"** lưu trữ đối tượng `Student`. |
| `10:51 - 11:20` | *Hôm nay mình học Service đơn giản, trong Service tạo một cái kho ngậm với CSDL... các bạn có thể dùng Postman để test...* | Kiểm thử các chức năng CRUD cơ bản qua các endpoint REST API bằng Postman. |
| `11:20 - 11:36` | *Bây giờ các bạn viết giao diện cho nó, để nó load mấy cái này lên. Bây giờ thầy stop share... Tính điểm mấy cái phần này nhé các bạn nhé!* | **YÊU CẦU ĐÁNH GIÁ CHẤM ĐIỂM:** Thầy yêu cầu sinh viên tự viết giao diện Web hiển thị bảng danh sách sinh viên, có form thêm/sửa/xóa để nộp bài chấm điểm. |

---

## 3. PHÂN TÍCH CHUYÊN SÂU 5 TRỌNG ĐIỂM KIẾN THỨC THẦY DẠY

### Trọng điểm 1: Hai package mới "entity" và "repository"
Trong kiến trúc Spring Boot JPA chuẩn theo chỉ đạo của thầy:
```
com.example.demojpa/
 ├── entity/          <-- [MỚI] Chứa các Entity class có @Entity (Student.java)
 ├── repository/      <-- [MỚI] Chứa các Interface JpaRepository (StudentRepository.java)
 ├── service/         <-- Chứa lớp dịch vụ nghiệp vụ (StudentService.java)
 ├── controller/      <-- Chứa các REST API endpoint (StudentController.java)
 └── DemojpaApplication.java
```

---

### Trọng điểm 2: Lớp Entity Student và các Annotation ràng buộc CSDL
Trong file `Student.java`:
```java
@Entity
@Table(name = "students")
public class Student {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // Khóa chính tự tăng 1, 2, 3...

    @Column(name = "name", length = 100, nullable = false)
    private String name; // Bắt buộc nhập, tối đa 100 ký tự

    @Column(name = "email", length = 100, unique = true)
    private String email; // Không được trùng email

    @Column(name = "phone", length = 20)
    private String phone;
```

---

### Trọng điểm 3: Khái niệm "CÁI KHO" - JpaRepository
Thầy giải thích: Sinh viên không cần viết lệnh `SELECT`, `INSERT`, `UPDATE`, `DELETE` bằng SQL nữa. Chỉ cần khai báo interface:
```java
@Repository
public interface StudentRepository extends JpaRepository<Student, Long> {
    // Tự động có sẵn:
    // .findAll()       -> Lấy tất cả sinh viên
    // .findById(id)    -> Lấy 1 sinh viên theo ID
    // .save(student)   -> Thêm mới hoặc cập nhật
    // .deleteById(id)  -> Xóa sinh viên
    
    // Tùy biến thêm:
    List<Student> findByNameContainingIgnoreCase(String name);
}
```

---

### Trọng điểm 4: Tầng Service điều phối nghiệp vụ
Tầng Service sử dụng cơ chế **Constructor Injection** để lấy "Cái kho" vào sử dụng:
```java
@Service
public class StudentService {

    private final StudentRepository studentRepository; // "Cái kho"

    public StudentService(StudentRepository studentRepository) {
        this.studentRepository = studentRepository;
    }

    public List<Student> getAllStudents() {
        return studentRepository.findAll();
    }
```

---

### Trọng điểm 5: Yêu cầu viết giao diện Web và tính điểm thực hành
Thầy chốt lại ở cuối video: Sinh viên phải viết trang web để người dùng có thể:
1. Nhìn thấy danh sách toàn bộ sinh viên đang lưu trong CSDL MySQL.
2. Có ô tìm kiếm theo tên sinh viên.
3. Có nút bấm thêm sinh viên mới.
4. Có nút bấm sửa và xóa sinh viên.

---

## 4. CHI TIẾT MÃ NGUỒN DỰ ÁN DEMOJPA ĐÃ ĐƯỢC XÂY DỰNG HOÀN THIỆN

Dự án đã được triển khai hoàn chỉnh 100% tại cả 2 vị trí:
1. Thư mục thầy gửi: [d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\thaygui\demojpa](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/thaygui/demojpa)
2. Thư mục bài tập T2: [d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\t2\b8_demojpa_student](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/bt/t2/b8_demojpa_student)

### Bảng tóm tắt các thành phần code:
- **Entity**: [Student.java](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/thaygui/demojpa/src/main/java/com/example/demojpa/entity/Student.java) — Đầy đủ annotation `@Entity`, `@Id`, `@GeneratedValue`, `@Column`.
- **Repository**: [StudentRepository.java](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/thaygui/demojpa/src/main/java/com/example/demojpa/repository/StudentRepository.java) — Kế thừa `JpaRepository<Student, Long>`.
- **Service**: [StudentService.java](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/thaygui/demojpa/src/main/java/com/example/demojpa/service/StudentService.java) — Cung cấp các thao tác CRUD và tìm kiếm sinh viên.
- **Controller**: [StudentController.java](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/thaygui/demojpa/src/main/java/com/example/demojpa/controller/StudentController.java) — Cung cấp RESTful API `/api/students` với đầy đủ GET, POST, PUT, DELETE.
- **Dữ liệu mẫu**: [DemojpaApplication.java](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/thaygui/demojpa/src/main/java/com/example/demojpa/DemojpaApplication.java) — Tự động nạp sẵn 5 sinh viên mẫu vào MySQL khi chạy lần đầu.
- **Giao diện Web**: [index.html](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/thaygui/demojpa/src/main/resources/static/index.html) — Giao diện SPA thuần, sạch sẽ, chuẩn học thuật theo phong cách `gk-real` (không emoji lòe loẹt), có tìm kiếm tức thì, modal thêm/sửa, dialog xóa.
- **Cấu hình CSDL**: [application.properties](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/thaygui/demojpa/src/main/resources/application.properties) — Kết nối MySQL cục bộ cổng `3306`, user `root`, pass `root`.

---

## 5. HƯỚNG DẪN TỪNG BƯỚC IMPORT VÀO ECLIPSE & CHẠY THỰC TẾ

### Bước 1: Đảm bảo MySQL Server đang bật
Mở file **`Bật - Tắt MySQL.bat`** trên Desktop $\rightarrow$ Bấm phím `1` để bật MySQL Server (hoặc kiểm tra bằng phím `5`).

### Bước 2: Mở Eclipse và Import Project
1. Mở phần mềm **Eclipse IDE**.
2. Trên thanh menu, chọn **File** $\rightarrow$ chọn **Import...**
3. Trong hộp thoại Import:
   - Chọn mục **Maven** $\rightarrow$ chọn **Existing Maven Projects** $\rightarrow$ bấm **Next**.
   - Tại ô **Root Directory**, bấm nút **Browse...** $\rightarrow$ chọn đường dẫn:
     `d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\t2\b8_demojpa_student`  
     *(hoặc chọn thư mục `thaygui\demojpa`)*.
   - Eclipse sẽ tự động tick chọn file `pom.xml`.
   - Bấm nút **Finish**.
4. Đợi Eclipse đồng bộ dependencies Maven xong (thanh tiến trình ở góc dưới bên phải chạy xong 100%).

### Bước 3: Khởi chạy ứng dụng
1. Trong cửa sổ **Package Explorer** bên trái của Eclipse, mở project vừa import.
2. Tìm đến file: `src/main/java` $\rightarrow$ `com.example.demojpa` $\rightarrow$ **`DemojpaApplication.java`**.
3. Chuột phải vào file `DemojpaApplication.java` $\rightarrow$ chọn **Run As** $\rightarrow$ chọn **Spring Boot App** (hoặc **Java Application**).
4. Quan sát Console, khi thấy dòng thông báo:
   ```text
   >>> Nap du lieu sinh vien mau vao MySQL Server...
   >>> Khoi tao thanh cong 5 sinh vien vao MySQL!
   Tomcat started on port 8080 (http)
   ```
   Là ứng dụng đã kết nối MySQL thành công và tạo xong bảng!

### Bước 4: Trình chiếu giao diện cho Thầy chấm điểm
1. Mở trình duyệt web (Chrome, Edge hoặc Firefox).
2. Truy cập vào địa chỉ: **`http://localhost:8080/index.html`**
3. Trên màn hình sẽ hiển thị bảng danh sách 5 sinh viên:
   - Thử bấm nút **"+ Thêm sinh viên mới"** $\rightarrow$ Nhập tên, email, SĐT $\rightarrow$ Bấm Lưu.
   - Thử bấm nút **"Sửa"** $\rightarrow$ Cập nhật thông tin sinh viên $\rightarrow$ Bấm Lưu.
   - Thử gõ vào ô **Tìm kiếm** tên sinh viên để lọc trực tiếp.
   - Thử mở **MySQL Workbench** $\rightarrow$ chạy lệnh: `SELECT * FROM b7_db.students;` để chỉ cho thầy thấy dữ liệu đã được lưu bền vững vào CSDL vật lý!
