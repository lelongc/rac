# CẨM NANG GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE BÀI 6-2 (ĐI THI VẤN ĐÁP)

## DỰ ÁN: `b6_2_faculty_crud` (SPRING BOOT MVC + RESTful API FULL CRUD)

> **Mục tiêu tài liệu:** Giúp bạn hiểu bản chất **từng dòng code** trong dự án `b6_2_faculty_crud`. Dù thầy cô có đổi đề bài sang bất kỳ chủ đề nào (ví dụ: *Phòng ban - Nhân viên*, *Danh mục - Sản phẩm*, *Lớp học - Học sinh*), bạn vẫn hiểu tường tận và tự tin viết lại từ đầu để đạt điểm tuyệt đối.

---

## 🧭 PHẦN 1: CÔNG THỨC 4 TẦNG KINH ĐIỂN MỌI BÀI THI SPRING BOOT

Mọi bài tập/đề thi Spring Boot ở trường đều tuân thủ kiến trúc phân tầng:

```
[TẦNG 1: MODEL]        --> Định nghĩa các đối tượng thực thể dữ liệu (Student, Faculty).
[TẦNG 2: SERVICE]      --> Chứa dữ liệu (In-Memory/DB) và thuật toán Thêm, Sửa, Xóa, Lọc.
[TẦNG 3: CONTROLLER]   --> Nhận request từ người dùng:
                           • REST Controller (@RestController) trả về dữ liệu thô JSON.
                           • Web Controller (@Controller) trả về giao diện HTML Thymeleaf.
[TẦNG 4: VIEW/HTML]    --> Các file HTML hiển thị bảng biểu, form nhập liệu (Thymeleaf).
```

---

## 📄 PHẦN 2: GIẢI THÍCH CHI TIẾT FILE CẤU HÌNH

### 1. File `pom.xml`

```xml
<!-- 1. Kế thừa cấu hình chuẩn từ Spring Boot cha (phiên bản 3.2.5) -->
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.2.5</version>
    <relativePath/>
</parent>

<!-- 2. Thông tin định danh của dự án mình -->
<groupId>com.example</groupId>
<artifactId>b6_2_faculty_crud</artifactId>
<version>0.0.1-SNAPSHOT</version>

<!-- 3. Khai báo phiên bản Java sử dụng (Java 17) -->
<properties>
    <java.version>17</java.version>
</properties>

<dependencies>
    <!-- THƯ VIỆN 1: spring-boot-starter-web -->
    <!-- Rất quan trọng: Tự động nhúng máy chủ Tomcat, kéo theo Spring MVC và thư viện Jackson chuyển đổi JSON -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>

    <!-- THƯ VIỆN 2: spring-boot-starter-thymeleaf -->
    <!-- Dùng để đọc và render dữ liệu vào các file HTML trong thư mục templates/ -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-thymeleaf</artifactId>
    </dependency>
</dependencies>
```

### 2. File `src/main/resources/application.properties`

```properties
# Đổi cổng chạy sang 8083 để tránh trùng cổng 8080 (của demo), 8081 (của b5), 8082 (của b6)
server.port=8083

# Đặt tên ứng dụng
spring.application.name=b6_2_faculty_crud

# Tắt bộ nhớ đệm (cache) của Thymeleaf để khi sửa file HTML và lưu lại (Ctrl+S), 
# F5 trình duyệt sẽ thấy ngay giao diện mới mà không cần khởi động lại server
spring.thymeleaf.cache=false
spring.thymeleaf.encoding=UTF-8
spring.thymeleaf.mode=HTML
```

---

## ☕ PHẦN 3: FILE CHẠY CHÍNH `FacultyCrudApplication.java`

```java
package com.example.faculty_crud;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

// ĐÂY LÀ ANNOTATION QUAN TRỌNG NHẤT:
// Nó là tổ hợp của 3 annotation:
// 1. @Configuration: Đánh dấu class chứa cấu hình Spring
// 2. @EnableAutoConfiguration: Tự động cấu hình Tomcat, Jackson, Thymeleaf dựa vào pom.xml
// 3. @ComponentScan: Tự động quét tìm tất cả các file có @Component, @Service, @Controller trong package này trở đi
@SpringBootApplication
public class FacultyCrudApplication {

    public static void main(String[] args) {
        // Lệnh kích hoạt toàn bộ hệ thống Spring Boot:
        // Khởi tạo Spring Context -> Bật Tomcat Server nhúng -> Lắng nghe cổng 8083
        SpringApplication.run(FacultyCrudApplication.class, args);
      
        // In thông báo ra màn hình Console để người dùng biết cổng truy cập
        System.out.println(">> Web UI:   http://localhost:8083/faculties");
        System.out.println(">> REST API: http://localhost:8083/api/faculties");
    }
}
```

---

## 📦 PHẦN 4: TẦNG MODEL (THỰC THỂ DỮ LIỆU)

### 1. `Student.java` (Thực thể Sinh viên)

```java
package com.example.faculty_crud.model;

public class Student {
    // Các thuộc tính riêng tư (private) để đảm bảo tính đóng gói trong OOP
    private Long id;       // Mã định danh sinh viên
    private String name;   // Họ và tên
    private String email;  // Địa chỉ email

    // BẮT BUỘC PHẢI CÓ: Constructor không đối số (No-args Constructor)
    // Lý do đi thi: Spring Boot và Jackson cần constructor này để tự động tạo đối tượng khi nhận form HTML hoặc JSON
    public Student() {
    }

    // Constructor đầy đủ đối số: Dùng khi code khởi tạo nhanh dữ liệu mẫu
    public Student(Long id, String name, String email) {
        this.id = id;
        this.name = name;
        this.email = email;
    }

    // Các hàm Getter/Setter: Bắt buộc phải có để:
    // 1. Thymeleaf đọc dữ liệu: ${student.name} thực chất là gọi student.getName()
    // 2. Jackson chuyển đổi sang JSON: Đọc các getter để sinh ra các key JSON tương ứng
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
}
```

### 2. `Faculty.java` (Thực thể Khoa - Quan hệ 1-Nhiều)

```java
package com.example.faculty_crud.model;

import java.util.ArrayList;
import java.util.List;

public class Faculty {
    private Long id;
    private String name;
  
    // MỐI QUAN HỆ 1 - NHIỀU (1 Khoa có NHIỀU Sinh viên):
    // Khởi tạo sẵn danh sách rỗng (new ArrayList<>()) để tránh lỗi NullPointerException
    private List<Student> students = new ArrayList<>();

    public Faculty() {
    }

    public Faculty(Long id, String name) {
        this.id = id;
        this.name = name;
        this.students = new ArrayList<>();
    }

    public Faculty(Long id, String name, List<Student> students) {
        this.id = id;
        this.name = name;
        // Nếu truyền null thì gán list rỗng, ngược lại copy danh sách vào
        this.students = students != null ? new ArrayList<>(students) : new ArrayList<>();
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public List<Student> getStudents() { return students; }
    public void setStudents(List<Student> students) {
        this.students = students != null ? new ArrayList<>(students) : new ArrayList<>();
    }
}
```

---

## ⚙️ PHẦN 5: TẦNG SERVICE `FacultyService.java` (TRÁI TIM NGHIỆP VỤ)

```java
package com.example.faculty_crud.service;

import com.example.faculty_crud.model.Faculty;
import com.example.faculty_crud.model.Student;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.atomic.AtomicLong;

// @Service: Báo cho Spring Boot biết đây là Service chứa logic nghiệp vụ.
// Spring Container sẽ tự động tạo 1 đối tượng duy nhất (Singleton Bean) đưa vào quản lý.
@Service
public class FacultyService {

    // Dùng CopyOnWriteArrayList thay cho ArrayList thường để an toàn đa luồng (Thread-safe)
    // khi nhiều người dùng cùng Thêm/Sửa/Xóa đồng thời
    private final List<Faculty> faculties = new CopyOnWriteArrayList<>();

    // Dùng AtomicLong để tự động tăng mã ID (như Auto Increment trong CSDL)
    private final AtomicLong facultyIdGenerator = new AtomicLong(3);    // Bắt đầu từ 3 vì đã có 3 khoa mẫu
    private final AtomicLong studentIdGenerator = new AtomicLong(301);  // Bắt đầu từ 301

    public FacultyService() {
        // Khởi tạo 3 khoa mẫu kèm sinh viên giống hệt bài giảng của Thầy trong video
        List<Student> itStudents = new ArrayList<>(List.of(
            new Student(101L, "Alice Johnson", "alice@cs.edu"),
            new Student(102L, "Bob Smith", "bob@cs.edu")
        ));
        List<Student> bizStudents = new ArrayList<>(List.of(
            new Student(201L, "Clara Davis", "clara@business.edu"),
            new Student(202L, "Emma Wilson", "emma@business.edu")
        ));
        List<Student> engStudents = new ArrayList<>(List.of(
            new Student(301L, "Daniel Lee", "daniel@eng.edu")
        ));

        faculties.add(new Faculty(1L, "Computer Science", itStudents));
        faculties.add(new Faculty(2L, "Business Administration", bizStudents));
        faculties.add(new Faculty(3L, "Engineering", engStudents));
    }

    // ===============================================
    // CÁC HÀM CRUD CHO KHOA (FACULTY)
    // ===============================================

    // 1. [READ] Lấy toàn bộ danh sách khoa
    public List<Faculty> getAllFaculties() {
        return faculties;
    }

    // 2. [READ] Lấy 1 khoa theo ID: Dùng Optional để nếu không thấy thì trả về Optional.empty()
    public Optional<Faculty> getFacultyById(Long id) {
        return faculties.stream()
                .filter(f -> f.getId().equals(id)) // Lọc khoa có ID trùng khớp
                .findFirst();                      // Lấy khoa đầu tiên tìm thấy
    }

    // 3. [CREATE] Thêm khoa mới
    public Faculty addFaculty(Faculty faculty) {
        if (faculty.getId() == null) {
            // Tự động sinh ID mới tăng dần
            faculty.setId(facultyIdGenerator.incrementAndGet());
        }
        if (faculty.getStudents() == null) {
            faculty.setStudents(new ArrayList<>());
        }
        faculties.add(faculty); // Thêm vào danh sách
        return faculty;
    }

    // 4. [UPDATE] Sửa thông tin khoa
    public Optional<Faculty> updateFaculty(Long id, Faculty updatedFaculty) {
        return getFacultyById(id).map(existingFaculty -> {
            // Nếu tên mới không rỗng thì cập nhật
            if (updatedFaculty.getName() != null && !updatedFaculty.getName().isBlank()) {
                existingFaculty.setName(updatedFaculty.getName());
            }
            return existingFaculty;
        });
    }

    // 5. [DELETE] Xóa khoa theo ID
    public boolean deleteFaculty(Long id) {
        // removeIf: Tìm và xóa phần tử thỏa mãn điều kiện f.getId().equals(id)
        return faculties.removeIf(f -> f.getId().equals(id));
    }

    // ===============================================
    // CÁC HÀM CRUD CHO SINH VIÊN (STUDENT)
    // ===============================================

    // 6. [READ] Lấy danh sách sinh viên theo mã khoa
    public Optional<List<Student>> getStudentsByFacultyId(Long facultyId) {
        return getFacultyById(facultyId).map(Faculty::getStudents);
    }

    // 7. [READ] Lấy chi tiết 1 sinh viên trong 1 khoa
    public Optional<Student> getStudentById(Long facultyId, Long studentId) {
        return getFacultyById(facultyId).flatMap(faculty ->
                faculty.getStudents().stream()
                        .filter(s -> s.getId().equals(studentId))
                        .findFirst()
        );
    }

    // 8. [CREATE] Thêm sinh viên mới vào khoa
    public Optional<Student> addStudentToFaculty(Long facultyId, Student student) {
        return getFacultyById(facultyId).map(faculty -> {
            if (student.getId() == null) {
                student.setId(studentIdGenerator.incrementAndGet()); // Tự tăng ID sinh viên
            }
            faculty.getStudents().add(student);
            return student;
        });
    }

    // 9. [UPDATE] Sửa thông tin sinh viên trong khoa
    public Optional<Student> updateStudent(Long facultyId, Long studentId, Student updatedStudent) {
        return getStudentById(facultyId, studentId).map(existingStudent -> {
            if (updatedStudent.getName() != null && !updatedStudent.getName().isBlank()) {
                existingStudent.setName(updatedStudent.getName());
            }
            if (updatedStudent.getEmail() != null && !updatedStudent.getEmail().isBlank()) {
                existingStudent.setEmail(updatedStudent.getEmail());
            }
            return existingStudent;
        });
    }

    // 10. [DELETE] Xóa sinh viên khỏi khoa
    public boolean deleteStudentFromFaculty(Long facultyId, Long studentId) {
        Optional<Faculty> facultyOpt = getFacultyById(facultyId);
        if (facultyOpt.isPresent()) {
            return facultyOpt.get().getStudents().removeIf(s -> s.getId().equals(studentId));
        }
        return false;
    }
}
```

---

## 🌐 PHẦN 6: TẦNG REST CONTROLLER `FacultyRestController.java` (XUẤT API JSON)

```java
package com.example.faculty_crud.controller;

import com.example.faculty_crud.model.Faculty;
import com.example.faculty_crud.model.Student;
import com.example.faculty_crud.service.FacultyService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

// @RestController = @Controller + @ResponseBody:
// Báo cho Spring Boot biết class này là REST API, tất cả các method đều trả về dữ liệu thô (JSON),
// TUYỆT ĐỐI KHÔNG tìm kiếm file HTML nào.
@RestController
@RequestMapping("/api/faculties") // Root tổng cho toàn bộ API trong class này
public class FacultyRestController {

    private final FacultyService facultyService;

    // DEPENDENCY INJECTION QUA CONSTRUCTOR:
    // Spring tự động tiêm đối tượng FacultyService vào Controller khi khởi tạo
    public FacultyRestController(FacultyService facultyService) {
        this.facultyService = facultyService;
    }

    // ==========================================
    // 1. API KHOA (FACULTY)
    // ==========================================

    // [GET] /api/faculties -> Lấy danh sách tất cả các khoa
    @GetMapping
    public ResponseEntity<List<Faculty>> getAllFaculties() {
        return ResponseEntity.ok(facultyService.getAllFaculties()); // Mã HTTP 200 OK
    }

    // [GET] /api/faculties/{id} -> Lấy 1 khoa theo ID
    // @PathVariable("id") Long id: Trích xuất số ID từ trên đường dẫn URL
    @GetMapping("/{id}")
    public ResponseEntity<Faculty> getFacultyById(@PathVariable("id") Long id) {
        return facultyService.getFacultyById(id)
                .map(ResponseEntity::ok)                           // Nếu thấy -> Trả 200 OK kèm dữ liệu
                .orElseGet(() -> ResponseEntity.notFound().build()); // Nếu không thấy -> Trả 404 Not Found
    }

    // [POST] /api/faculties -> Thêm khoa mới
    // @RequestBody: Tự động hứng chuỗi JSON do Client gửi lên và ép kiểu thành đối tượng Java Faculty
    @PostMapping
    public ResponseEntity<Faculty> createFaculty(@RequestBody Faculty faculty) {
        Faculty created = facultyService.addFaculty(faculty);
        // Trả về mã HTTP 201 Created (Chuẩn RESTful khi tạo mới thành công)
        return ResponseEntity.status(HttpStatus.CREATED).body(created);
    }

    // [PUT] /api/faculties/{id} -> Sửa thông tin khoa
    @PutMapping("/{id}")
    public ResponseEntity<Faculty> updateFaculty(@PathVariable("id") Long id, @RequestBody Faculty updatedFaculty) {
        return facultyService.updateFaculty(id, updatedFaculty)
                .map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    // [DELETE] /api/faculties/{id} -> Xóa một khoa
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteFaculty(@PathVariable("id") Long id) {
        boolean deleted = facultyService.deleteFaculty(id);
        if (deleted) {
            // Mã HTTP 204 No Content: Báo hiệu xóa thành công và không cần trả về nội dung gì
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.notFound().build();
    }

    // ==========================================
    // 2. API SINH VIÊN (STUDENT)
    // ==========================================

    // [GET] /api/faculties/{facultyId}/students -> Lấy danh sách sinh viên của khoa
    @GetMapping("/{facultyId}/students")
    public ResponseEntity<List<Student>> getStudentsByFacultyId(@PathVariable("facultyId") Long facultyId) {
        return facultyService.getStudentsByFacultyId(facultyId)
                .map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    // [POST] /api/faculties/{facultyId}/students -> Thêm sinh viên vào khoa
    @PostMapping("/{facultyId}/students")
    public ResponseEntity<Student> addStudentToFaculty(@PathVariable("facultyId") Long facultyId,
                                                       @RequestBody Student student) {
        return facultyService.addStudentToFaculty(facultyId, student)
                .map(createdStudent -> ResponseEntity.status(HttpStatus.CREATED).body(createdStudent))
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    // [PUT] /api/faculties/{facultyId}/students/{studentId} -> Sửa sinh viên
    @PutMapping("/{facultyId}/students/{studentId}")
    public ResponseEntity<Student> updateStudent(@PathVariable("facultyId") Long facultyId,
                                                 @PathVariable("studentId") Long studentId,
                                                 @RequestBody Student updatedStudent) {
        return facultyService.updateStudent(facultyId, studentId, updatedStudent)
                .map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    // [DELETE] /api/faculties/{facultyId}/students/{studentId} -> Xóa sinh viên
    @DeleteMapping("/{facultyId}/students/{studentId}")
    public ResponseEntity<Void> deleteStudent(@PathVariable("facultyId") Long facultyId,
                                              @PathVariable("studentId") Long studentId) {
        boolean deleted = facultyService.deleteStudentFromFaculty(facultyId, studentId);
        if (deleted) {
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.notFound().build();
    }
}
```

---

## 🖥️ PHẦN 7: TẦNG WEB CONTROLLER `FacultyWebController.java` (RENDER THYMELEAF)

```java
package com.example.faculty_crud.controller;

import com.example.faculty_crud.model.Faculty;
import com.example.faculty_crud.model.Student;
import com.example.faculty_crud.service.FacultyService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

// CHÚ Ý: Dùng @Controller (không có chữ Rest):
// Để các hàm bên dưới trả về TÊN FILE TEMPLATE HTML (Thymeleaf)
@Controller
public class FacultyWebController {

    private final FacultyService facultyService;

    public FacultyWebController(FacultyService facultyService) {
        this.facultyService = facultyService;
    }

    // 1. Xem danh sách tất cả các khoa trên giao diện web
    @GetMapping({"/", "/faculties"})
    public String listFaculties(Model model) {
        // Gắn danh sách các khoa vào Model để HTML có thể dùng cú pháp ${faculties}
        model.addAttribute("faculties", facultyService.getAllFaculties());
        return "faculty_list"; // Tìm file templates/faculty_list.html
    }

    // 2. Mở form thêm khoa mới
    @GetMapping("/faculties/new")
    public String showNewFacultyForm(Model model) {
        model.addAttribute("faculty", new Faculty()); // Tạo 1 đối tượng rỗng để form HTML liên kết (th:object)
        model.addAttribute("isEdit", false);          // Cờ đánh dấu: Đây là chế độ THÊM MỚI
        return "faculty_form";                         // Tìm file templates/faculty_form.html
    }

    // 3. Mở form sửa khoa
    @GetMapping("/faculties/edit/{id}")
    public String showEditFacultyForm(@PathVariable("id") Long id, Model model) {
        Optional<Faculty> facultyOpt = facultyService.getFacultyById(id);
        if (facultyOpt.isPresent()) {
            model.addAttribute("faculty", facultyOpt.get()); // Nạp thông tin khoa cũ vào form
            model.addAttribute("isEdit", true);              // Cờ đánh dấu: Đây là chế độ CHỈNH SỬA
            return "faculty_form";
        }
        return "redirect:/faculties"; // Nếu không tìm thấy thì quay về trang danh sách
    }

    // 4. Nhận dữ liệu submit từ Form Thêm/Sửa Khoa
    // @ModelAttribute("faculty"): Tự động hứng các trường input từ Form HTML nạp vào đối tượng Faculty
    @PostMapping("/faculties/save")
    public String saveFaculty(@ModelAttribute("faculty") Faculty faculty) {
        if (faculty.getId() == null) {
            facultyService.addFaculty(faculty); // Không có ID -> Thêm mới
        } else {
            facultyService.updateFaculty(faculty.getId(), faculty); // Đã có ID -> Cập nhật
        }
        // Lệnh chuyển hướng trình duyệt (Redirect) về lại trang danh sách
        return "redirect:/faculties";
    }

    // 5. Xóa khoa khi nhấn nút Xóa
    @GetMapping("/faculties/delete/{id}")
    public String deleteFaculty(@PathVariable("id") Long id) {
        facultyService.deleteFaculty(id);
        return "redirect:/faculties";
    }

    // 6. Xem danh sách sinh viên của 1 khoa
    @GetMapping("/faculties/{id}/students")
    public String viewFacultyStudents(@PathVariable("id") Long id, Model model) {
        Optional<Faculty> facultyOpt = facultyService.getFacultyById(id);
        if (facultyOpt.isPresent()) {
            model.addAttribute("faculty", facultyOpt.get());
            model.addAttribute("students", facultyOpt.get().getStudents());
            return "faculty_students"; // Tìm file templates/faculty_students.html
        }
        return "redirect:/faculties";
    }

    // 7. Mở form thêm sinh viên vào khoa
    @GetMapping("/faculties/{facultyId}/students/new")
    public String showNewStudentForm(@PathVariable("facultyId") Long facultyId, Model model) {
        Optional<Faculty> facultyOpt = facultyService.getFacultyById(facultyId);
        if (facultyOpt.isEmpty()) {
            return "redirect:/faculties";
        }
        model.addAttribute("faculty", facultyOpt.get());
        model.addAttribute("student", new Student());
        model.addAttribute("isEdit", false);
        return "student_form";
    }

    // 8. Mở form sửa sinh viên
    @GetMapping("/faculties/{facultyId}/students/edit/{studentId}")
    public String showEditStudentForm(@PathVariable("facultyId") Long facultyId,
                                      @PathVariable("studentId") Long studentId,
                                      Model model) {
        Optional<Faculty> facultyOpt = facultyService.getFacultyById(facultyId);
        Optional<Student> studentOpt = facultyService.getStudentById(facultyId, studentId);
        if (facultyOpt.isPresent() && studentOpt.isPresent()) {
            model.addAttribute("faculty", facultyOpt.get());
            model.addAttribute("student", studentOpt.get());
            model.addAttribute("isEdit", true);
            return "student_form";
        }
        return "redirect:/faculties/" + facultyId + "/students";
    }

    // 9. Lưu sinh viên khi submit Form
    @PostMapping("/faculties/{facultyId}/students/save")
    public String saveStudent(@PathVariable("facultyId") Long facultyId,
                              @ModelAttribute("student") Student student) {
        if (student.getId() == null) {
            facultyService.addStudentToFaculty(facultyId, student);
        } else {
            facultyService.updateStudent(facultyId, student.getId(), student);
        }
        return "redirect:/faculties/" + facultyId + "/students";
    }

    // 10. Xóa sinh viên khỏi khoa
    @GetMapping("/faculties/{facultyId}/students/delete/{studentId}")
    public String deleteStudent(@PathVariable("facultyId") Long facultyId,
                                @PathVariable("studentId") Long studentId) {
        facultyService.deleteStudentFromFaculty(facultyId, studentId);
        return "redirect:/faculties/" + facultyId + "/students";
    }
}
```

---

## 🎨 PHẦN 8: CÁC CÚ PHÁP THYMELEAF CỐT LÕI (GIẢI THÍCH HTML)

1. **Khai báo thư viện ở thẻ đầu:**
   ```html
   <html xmlns:th="http://www.thymeleaf.org">
   ```
2. **Vòng lặp Foreach (`th:each`):**
   ```html
   <tr th:each="faculty : ${faculties}">
   ```

   *Ý nghĩa:* Duyệt qua từng phần tử `faculty` trong mảng `faculties` lấy từ Model.
3. **In văn bản (`th:text`):**
   ```html
   <td th:text="${faculty.name}">Tên mẫu</td>
   ```

   *Ý nghĩa:* Thay thế nội dung chữ "Tên mẫu" bằng giá trị thực tế `faculty.getName()`.
4. **Tạo đường link động (`th:href`):**
   ```html
   <a th:href="@{/faculties/edit/{id}(id=${faculty.id})}">Sửa</a>
   ```

   *Ý nghĩa:* Tạo đường link động thay thế `{id}` bằng giá trị `faculty.id` (ví dụ: `/faculties/edit/1`).
5. **Liên kết dữ liệu Form (`th:object` và `th:field`):**
   ```html
   <form th:action="@{/faculties/save}" th:object="${faculty}" method="post">
       <input type="hidden" th:field="*{id}" />
       <input type="text" th:field="*{name}" />
   </form>
   ```

   *Ý nghĩa:*- `th:object="${faculty}"`: Khai báo form này đại diện cho đối tượng `faculty`.
   - `th:field="*{name}"`: Tự động gán thuộc tính `id="name"`, `name="name"`, và `value` lấy từ `faculty.getName()`.
6. **Kiểm tra điều kiện (`th:if`):**
   ```html
   <span th:text="${isEdit ? 'Chỉnh Sửa' : 'Thêm Mới'}"></span>
   ```

---

## ⚡ PHẦN 9: BÍ KÍP ĐỔI ĐỀ BÀI KHI ĐI THI (ÁP DỤNG TRONG 5 PHÚT)

Khi đi thi, nếu thầy cô đổi đề bài sang một chủ đề khác, bạn **chỉ cần thay đổi tên Class và thuộc tính** theo bảng quy đổi sau:

| Đối tượng cha (Khoa)                                 | Đối tượng con (Sinh viên) | Thuộc tính đối tượng con            |
| -------------------------------------------------------- | ------------------------------ | ----------------------------------------- |
| **Đề hiện tại:** `Faculty`                   | `Student`                    | `id`, `name`, `email`               |
| **Đề đổi thành:** `Category` (Danh mục)    | `Product` (Sản phẩm)       | `id`, `name`, `price`, `quantity` |
| **Đề đổi thành:** `Department` (Phòng ban) | `Employee` (Nhân viên)     | `id`, `fullName`, `salary`          |
| **Đề đổi thành:** `Classroom` (Lớp học)   | `Pupil` (Học sinh)          | `id`, `name`, `age`                 |
| **Đề đổi thành:** `Warehouse` (Kho hàng)   | `Item` (Mặt hàng)          | `id`, `itemName`, `unit`            |

👉 **Quy tắc làm bài:**

- Cấu trúc logic của Service và Controller là **HOÀN TOÀN GIỐNG HỆT 100%**.
- Bạn chỉ cần đổi tên biến và tên phương thức (ví dụ: `getProductsByCategoryId` thay cho `getStudentsByFacultyId`).
