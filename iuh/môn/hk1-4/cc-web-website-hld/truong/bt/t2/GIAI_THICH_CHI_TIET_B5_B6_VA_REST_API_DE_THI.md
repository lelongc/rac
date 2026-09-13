# TÀI LIỆU HƯỚNG DẪN ÔN TẬP VẤN ĐÁP & ĐI THI

## PHÂN TÍCH TOÀN DIỆN: `b5_basic_web`, `b6_independent_web` VÀ BÀI GIẢNG REST API SPRING BOOT

> **Dành cho:** Sinh viên chuẩn bị thi vấn đáp, kiểm tra thực hành môn Lập trình Web / Web Services.
> **Nội dung:** Kết hợp chi tiết mã nguồn 2 bài tập (`b5_basic_web`, `b6_independent_web`) và bản phân tích bài giảng 18 phút của Giảng viên về bước chuyển giao từ **Spring MVC (HTML)** sang **RESTful Web Service (JSON)**.

---

## MỤC LỤC

1. [Bức tranh tổng thể: Tiến trình học từ Thầy](#1-bức-tranh-tổng-thể-tiến-trình-học-từ-thầy)
2. [Mổ xẻ chi tiết Bài 1: `b5_basic_web` (Spring Boot MVC cơ bản)](#2-mổ-xẻ-chi-tiết-bài-1-b5_basic_web-spring-boot-mvc-cơ-bản)
3. [Mổ xẻ chi tiết Bài 2: `b6_independent_web` (Mô hình quan hệ 1-N &amp; `@PathVariable`)](#3-mổ-xẻ-chi-tiết-bài-2-b6_independent_web-mô-hình-quan-hệ-1-n--pathvariable)
4. [Giải mã bài giảng Video: Nâng cấp sang RESTful Web Service](#4-giải-mã-bài-giảng-video-nâng-cấp-sang-restful-web-service)
5. [So sánh chuyên sâu: Spring MVC vs REST API](#5-so-sánh-chuyên-sâu-spring-mvc-vs-rest-api)
6. [10 Câu hỏi vấn đáp thường gặp khi đi thi (Kèm câu trả lời mẫu 10 điểm)](#6-10-câu-hỏi-vấn-đáp-thường-gặp-khi-đi-thi-kèm-câu-trả-lời-mẫu-10-điểm)

---

## 1. BỨC TRANH TỔNG THỂ: TIẾN TRÌNH HỌC TỪ THẦY

Để hiểu sâu bản chất và trả lời trôi chảy trước giảng viên, bạn cần nắm rõ **tại sao chúng ta lại học theo lộ trình này**:

```
[GIAI ĐOẠN 1: b0 -> b4]
Học OOP, làm web tĩnh, dùng MockAPI / Fake REST API bên thứ 3 vì chưa tự viết được backend.
       │
       ▼
[GIAI ĐOẠN 2: b5_basic_web]
Làm quen với Spring Boot + Thymeleaf.
Kiến trúc MVC truyền thống: Server render toàn bộ HTML và trả về trình duyệt.
       │
       ▼
[GIAI ĐOẠN 3: b6_independent_web]
Nâng cao Spring MVC: Xử lý dữ liệu liên kết 1-Nhiều (Khoa & Sinh viên).
Làm quen với URL động thông qua `@PathVariable`.
       │
       ▼
[GIAI ĐOẠN 4: BÀI GIẢNG 18 PHÚT CỦA THẦY - BƯỚC NHẢY VỌT VỀ KIẾN TRÚC]
Chuyển đổi từ MVC sang Web Service:
1. Tách logic nghiệp vụ ra tầng riêng: `FacultyService`.
2. Dùng `@RestController` để trả về dữ liệu thô JSON thay vì trang web HTML.
3. Phân biệt `@PathVariable` và `@RequestParam`.
4. Không cần MockAPI nữa: Chính chúng ta tự viết Backend Web Service chuẩn công nghiệp!
```

---

## 2. MỔ XẺ CHI TIẾT BÀI 1: `b5_basic_web` (SPRING BOOT MVC CƠ BẢN)

### 2.1. Mục tiêu bài tập

- Làm quen với cách khởi tạo một ứng dụng web bằng **Spring Boot Starter Web**.
- Sử dụng Template Engine **Thymeleaf** để hiển thị danh sách sản phẩm từ backend ra giao diện người dùng.
- Cấu hình server chạy trên cổng riêng biệt (`server.port=8081`).

### 2.2. Phân tích chi tiết từng file mã nguồn

#### A. File cấu hình `pom.xml`

```xml
<dependencies>
    <!-- Thư viện cốt lõi để làm web (chứa nhúng Tomcat, Spring MVC, REST) -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>

    <!-- Thư viện Template Engine để render file HTML -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-thymeleaf</artifactId>
    </dependency>
</dependencies>
```

- **Ý nghĩa đi thi:** `spring-boot-starter-web` tự động kéo theo Tomcat server nhúng bên trong, lập trình viên không cần cài đặt Tomcat thủ công như Servlet/JSP ngày xưa.

#### B. File kích hoạt `BasicWebApplication.java`

```java
package com.example.basic_web;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class BasicWebApplication {
    public static void main(String[] args) {
        SpringApplication.run(BasicWebApplication.class, args);
    }
}
```

- **Ý nghĩa Annotation `@SpringBootApplication`:** Đây là tổ hợp của 3 annotation quan trọng:
  1. `@Configuration`: Đánh dấu class này là nguồn khai báo cấu hình (Bean) cho Spring Context.
  2. `@EnableAutoConfiguration`: Bật tính năng tự động cấu hình (Auto-configuration) của Spring Boot dựa vào các thư viện có trong `pom.xml`.
  3. `@ComponentScan`: Tự động quét toàn bộ package hiện tại và các package con để tìm và đăng ký các Bean (`@Component`, `@Controller`, `@Service`, `@Repository`).

#### C. Lớp Model: `Product.java`

- Chứa các trường thông tin cơ bản: `id` (Long), `name` (String), `price` (Double).
- Cung cấp: Constructor không đối số (No-args), Constructor đầy đủ đối số (All-args), các cặp Getter/Setter và phương thức `toString()`.

#### D. Lớp Controller: `ProductController.java`

```java
@Controller
public class ProductController {

    @GetMapping({"/", "/products", "/product", "/product-list", "/product_list", "/home", "/index"})
    public String getProducts(Model model) {
        List<Product> productList = Arrays.asList(
            new Product(1L, "Laptop Dell XPS 15", 999.99),
            new Product(2L, "Smartphone iPhone 15", 699.99),
            new Product(3L, "Wireless Headphones Sony", 149.99),
            new Product(4L, "Mechanical Keyboard RGB", 89.50)
        );

        // Gắn danh sách sản phẩm vào đối tượng Model với key là "products"
        model.addAttribute("products", productList);

        // Trả về TÊN CỦA FILE TEMPLATE HTML (Spring sẽ tìm templates/product_list.html)
        return "product_list";
    }
}
```

- **Điểm cốt lõi:**
  - Dùng `@Controller`: Báo hiệu phương thức này sẽ trả về **Tên View** (tên file HTML), không phải trả về dữ liệu thô.
  - Tham số `Model model`: Là túi đựng dữ liệu chuyển giao từ Controller sang View.
  - Lệnh `return "product_list"`: ViewResolver của Thymeleaf sẽ tự động ghép tiền tố `classpath:/templates/` và hậu tố `.html` để xác định file cần hiển thị.

#### E. Giao diện View: `product_list.html`

```html
<tr th:each="product : ${products}">
    <td th:text="${product.id}">1</td>
    <td th:text="${product.name}">Tên sản phẩm</td>
    <td th:text="'$' + ${#numbers.formatDecimal(product.price, 1, 2)}">$0.00</td>
</tr>
```

- `th:each="product : ${products}"`: Vòng lặp foreach duyệt qua từng phần tử trong danh sách `products` được truyền từ `model.addAttribute`.
- `th:text="${...}"`: Thay thế nội dung tĩnh bằng giá trị thực tế lấy từ đối tượng Java.

---

## 3. MỔ XẺ CHI TIẾT BÀI 2: `b6_independent_web` (MÔ HÌNH QUAN HỆ 1-N & `@PathVariable`)

### 3.1. Mục tiêu bài tập

- Quản lý mối quan hệ thực thể phân cấp: **Một Khoa (`Faculty`) có Nhiều Sinh Viên (`Student`)**.
- Học cách truyền tham số biến động trên đường dẫn thông qua `@PathVariable`.
- Xử lý điều hướng: Xem danh sách khoa -> Nhấn vào một khoa để xem danh sách sinh viên thuộc khoa đó.

### 3.2. Phân tích chi tiết mã nguồn

#### A. Mô hình dữ liệu (Models)

- `Student.java`: Đại diện cho 1 sinh viên gồm `id`, `name`, `email`.
- `Faculty.java`: Đại diện cho 1 khoa, chứa:
  ```java
  private Long id;
  private String name;
  private List<Student> students; // Mối quan hệ 1-Nhiều (1 Faculty -> Nhiều Student)
  ```

#### B. Lớp điều khiển: `FacultyController.java`

```java
@Controller
public class FacultyController {

    private List<Faculty> facultyList = new ArrayList<>();

    public FacultyController() {
        // Khởi tạo dữ liệu mẫu trong bộ nhớ
        List<Student> csStudents = Arrays.asList(
            new Student(1L, "Nguyễn Văn An", "an.nguyen@example.com"),
            new Student(2L, "Trần Thị Bình", "binh.tran@example.com"),
            new Student(3L, "Lê Hoàng Long", "long.le@example.com")
        );

        List<Student> engStudents = Arrays.asList(
            new Student(4L, "Phạm Quốc Dũng", "dung.pham@example.com"),
            new Student(5L, "Đỗ Minh Khang", "khang.do@example.com")
        );

        facultyList.add(new Faculty(1L, "Khoa Công Nghệ Thông Tin", csStudents));
        facultyList.add(new Faculty(2L, "Khoa Kỹ Thuật Cơ Khí", engStudents));
    }

    // 1. Hiển thị danh sách tất cả các khoa
    @GetMapping({"/", "/faculties"})
    public String listFaculties(Model model) {
        model.addAttribute("faculties", facultyList);
        return "faculty_list";
    }

    // 2. Hiển thị sinh viên của một khoa cụ thể dựa vào ID trên URL
    @GetMapping("/faculties/{id}/students")
    public String viewFacultyStudents(@PathVariable("id") Long id, Model model) {
        Faculty selectedFaculty = null;
        for (Faculty faculty : facultyList) {
            if (faculty.getId().equals(id)) {
                selectedFaculty = faculty;
                break;
            }
        }

        if (selectedFaculty != null) {
            model.addAttribute("faculty", selectedFaculty);
            model.addAttribute("students", selectedFaculty.getStudents());
        } else {
            // Nếu không tìm thấy khoa, chuyển hướng về trang danh sách
            return "redirect:/faculties";
        }
        return "faculty_students";
    }
}
```

### 3.3. Điểm cần ghi nhớ khi vấn đáp về bài này:

1. **`@PathVariable("id") Long id`:**
   - Cặp ngoặc nhọn `{id}` trên `@GetMapping("/faculties/{id}/students")` khai báo rằng đây là một vị trí biến động.
   - Khi người dùng gõ: `http://localhost:8082/faculties/1/students`, Spring sẽ tự động trích xuất chuỗi `"1"` và ép kiểu thành `Long id = 1L`.
2. **Hạn chế của `b6_independent_web` (Tiền đề dẫn tới bài giảng của thầy):**
   - Dữ liệu bị fix cứng ngay trong Constructor của Controller.
   - Vừa làm nhiệm vụ điều hướng, vừa lọc dữ liệu -> Vi phạm nguyên lý thiết kế **Single Responsibility** (Trách nhiệm đơn lẻ).
   - Chỉ trả về trang web HTML, các ứng dụng khác (như React, Vue, Mobile App Android/iOS) không thể tái sử dụng dữ liệu này.

---

## 4. GIẢI MÃ BÀI GIẢNG VIDEO: NÂNG CẤP SANG RESTFUL WEB SERVICE

Trong file audio 18 phút, Giảng viên đã giải thích bước chuyển giao công nghệ quan trọng nhất của lập trình Web hiện đại. Dưới đây là phân tích chi tiết từng luận điểm của Thầy:

---

### 4.1. Luận điểm 1: "Service không làm web, MVC mới làm web"

- **Thầy phân tích:**
  - `MVC Controller` (`@Controller`) sinh ra để kết nối dữ liệu với giao diện (HTML/CSS). Nó gắn liền với giao diện người dùng.
  - `Service` (`@Service`) sinh ra để giải quyết **nghiệp vụ thuần túy** (Business Logic): Tính toán, lọc, sắp xếp, kết nối CSDL. Service hoàn toàn độc lập với giao diện.
- **Tách lớp `FacultyService` theo chuẩn của Thầy:**

```java
package com.example.independent_web.service;

import com.example.independent_web.model.Faculty;
import com.example.independent_web.model.Student;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@Service
public class FacultyService {

    private List<Faculty> facultyList = new ArrayList<>();

    public FacultyService() {
        // Khởi tạo 3 Khoa mẫu như lời thầy giảng trong video
        List<Student> itStudents = Arrays.asList(
            new Student(1L, "Nguyễn Văn An", "an@iuh.edu.vn"),
            new Student(2L, "Trần Thị Bình", "binh@iuh.edu.vn")
        );
        List<Student> mechaStudents = Arrays.asList(
            new Student(3L, "Lê Hoàng Long", "long@iuh.edu.vn")
        );
        List<Student> bizStudents = Arrays.asList(
            new Student(4L, "Phạm Quốc Dũng", "dung@iuh.edu.vn")
        );

        facultyList.add(new Faculty(1L, "CNTT", itStudents));
        facultyList.add(new Faculty(2L, "CoKhi", mechaStudents));
        facultyList.add(new Faculty(3L, "KinhTe", bizStudents));
    }

    // Nghiệp vụ 1: Lọc danh sách sinh viên theo facultyId (Dùng Java Stream & equals)
    public List<Student> getStudentsByFacultyId(Long facultyId) {
        return facultyList.stream()
                .filter(f -> f.getId().equals(facultyId))
                .map(Faculty::getStudents)
                .findFirst()
                .orElse(new ArrayList<>());
    }

    // Nghiệp vụ 2: Lọc danh sách sinh viên theo facultyName
    public List<Student> getStudentsByFacultyName(String facultyName) {
        return facultyList.stream()
                .filter(f -> f.getName().equalsIgnoreCase(facultyName))
                .map(Faculty::getStudents)
                .findFirst()
                .orElse(new ArrayList<>());
    }
}
```

*Lưu ý của thầy trong video:* Vì mỗi Khoa có ID và Name là duy nhất (không có 2 khoa trùng tên nhau) nên ta dùng `.findFirst()` để lấy ngay khoa đầu tiên khớp điều kiện.

---

### 4.2. Luận điểm 2: Bản chất của `@RestController` và câu đố JSON của Thầy

- **Câu hỏi của Thầy trong video:**
  > *"Các bạn không nhìn thấy bất kỳ dòng code nào chuyển đổi đối tượng sang JSON hết. Vậy tại sao trình duyệt lại nhận được chuỗi JSON?"*
  >
- **Câu trả lời xuất sắc đi thi:**
  1. `@RestController` là sự kết hợp của `@Controller` + `@ResponseBody`.
  2. Khi một method được đánh dấu `@ResponseBody` (hoặc nằm trong `@RestController`), Spring Boot sẽ **không** tìm kiếm View HTML nữa.
  3. Thay vào đó, Spring Boot kích hoạt thư viện **Jackson (`ObjectMapper`)** thông qua bộ chuyển đổi `MappingJackson2HttpMessageConverter`.
  4. Thư viện này âm thầm lấy các thuộc tính của đối tượng Java (thông qua getter) và tuần tự hóa (serialize) thành chuỗi JSON, đồng thời tự động gắn Header `Content-Type: application/json` trả về cho Client.

---

### 4.3. Luận điểm 3: Viết `FacultyRestController` hoàn chỉnh

```java
package com.example.independent_web.controller;

import com.example.independent_web.model.Student;
import com.example.independent_web.service.FacultyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/faculty") // Root tổng (Class level)
public class FacultyRestController {

    // Tiêm (Inject) Service vào Controller thông qua Dependency Injection
    private final FacultyService facultyService;

    @Autowired
    public FacultyRestController(FacultyService facultyService) {
        this.facultyService = facultyService;
    }

    // Dạng 1: Dùng @PathVariable - Root phụ: /{facultyId}/students
    // URL kiểm tra: http://localhost:8082/api/faculty/1/students
    @GetMapping("/{facultyId}/students")
    public List<Student> getStudentsById(@PathVariable("facultyId") Long facultyId) {
        return facultyService.getStudentsByFacultyId(facultyId);
    }

    // Dạng 2: Dùng @RequestParam - Root phụ: /search
    // URL kiểm tra: http://localhost:8082/api/faculty/search?facultyName=CNTT
    @GetMapping("/search")
    public List<Student> getStudentsByName(@RequestParam("facultyName") String facultyName) {
        return facultyService.getStudentsByFacultyName(facultyName);
    }
}
```

---

### 4.4. Luận điểm 4: Phân biệt `@PathVariable` vs `@RequestParam`

Thầy phân tích rất kỹ sự khác nhau giữa 2 cách truyền tham số này:

| Tiêu chí                         | `@PathVariable` (Biến đường dẫn)                                              | `@RequestParam` (Tham số truy vấn)                                             |
| ---------------------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| **Cú pháp URL**            | `http://localhost:8082/api/faculty/1/students`                                     | `http://localhost:8082/api/faculty/search?facultyName=CNTT`                      |
| **Đặc điểm nhận dạng** | Nằm trực tiếp như một phần của cấu trúc URL                                 | Bắt đầu sau dấu hỏi chấm`?` theo cặp `key=value`, nối nhau bằng `&` |
| **Bản chất RESTful**       | Đại diện cho**Danh tính của tài nguyên** (Resource Identifier cụ thể) | Dùng để**Lọc (Filter), Tìm kiếm (Search), Phân trang (Paging)**       |
| **Code Spring Boot**         | `@GetMapping("/{id}")public ... (@PathVariable("id") Long id)`                     | `@GetMapping("/search")public ... (@RequestParam("name") String name)`           |

---

## 5. SO SÁNH CHUYÊN SÂU: SPRING MVC VS REST API

Bảng so sánh kinh điển mà mọi giảng viên đều hỏi khi chấm bài:

| Đặc điểm                                | Spring MVC truyền thống (`b5_basic_web`)                               | RESTful Web Service (Bài giảng của Thầy)                                 |
| ------------------------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Annotation chính**                 | `@Controller`                                                            | `@RestController` (hoặc `@Controller` + `@ResponseBody`)              |
| **Kiến trúc**                       | Monolithic (Nguyên khối): Giao diện và Backend dính liền             | Decoupled (Tách rời): Backend hoàn toàn tách biệt Frontend             |
| **Giá trị phương thức trả về** | `String` (Tên file template như `"product_list"`, `"dashboard"`)   | Đối tượng Java thô (`List<Student>`, `Product`, `ResponseEntity`) |
| **Kết quả Client nhận được**    | Mã nguồn HTML, CSS, JavaScript đầy đủ                                | Chuỗi dữ liệu thô**JSON** hoặc **XML**                      |
| **Nơi xử lý giao diện**           | Server xử lý (Server-Side Rendering - SSR)                               | Client xử lý (Client-Side Rendering - CSR) bởi React, Angular, Mobile App |
| **Băng thông mạng**                | Tốn băng thông hơn (mỗi lần tải lại phải gửi toàn bộ mã HTML) | Rất tiết kiệm băng thông (chỉ truyền tải đúng dữ liệu thô)      |
| **Khả năng mở rộng**              | Kém hơn khi muốn làm thêm ứng dụng Mobile                           | Cực kỳ linh hoạt: 1 REST API phục vụ cho cả Web, iOS, Android, IoT     |

---

## 6. 10 CÂU HỎI VẤN ĐÁP THƯỜNG GẶP KHI ĐI THI (KÈM CÂU TRẢ LỜI MẪU 10 ĐIỂM)

### ❓ Câu 1: Em hãy giải thích luồng đi của một Request trong Spring MVC từ lúc người dùng gõ URL đến khi nhìn thấy giao diện?

**Trả lời mẫu:**

1. Người dùng gửi HTTP Request từ trình duyệt (ví dụ: `GET /products`).
2. Request đầu tiên đi vào **`DispatcherServlet`** (Front Controller trung tâm của Spring Boot).
3. `DispatcherServlet` hỏi **`HandlerMapping`** để tìm xem Controller và method nào đăng ký xử lý URL `/products`.
4. Request được chuyển tới **`ProductController`**. Controller thực thi hàm, lấy danh sách dữ liệu và nạp vào đối tượng `Model`.
5. Controller trả về tên của View (chuỗi `"product_list"`).
6. `DispatcherServlet` chuyển tên View cho **`ViewResolver`** (ở đây là Thymeleaf ViewResolver). ViewResolver tìm file `templates/product_list.html`, trộn dữ liệu từ `Model` vào các thẻ `th:*`.
7. Kết quả là trang HTML hoàn chỉnh được trả về cho trình duyệt hiển thị cho người dùng.

---

### ❓ Câu 2: Sự khác nhau cơ bản nhất giữa `@Controller` và `@RestController` là gì?

**Trả lời mẫu:**

- `@Controller` dùng cho mô hình MVC truyền thống. Giá trị trả về của các method mặc định được hiểu là **tên của View (trang HTML)** để ViewResolver xử lý render giao diện.
- `@RestController` dùng để xây dựng RESTful Web Service. Nó là sự kết hợp của `@Controller` và `@ResponseBody`. Mọi phương thức bên trong `@RestController` đều trả về **dữ liệu thô (mặc định là JSON)** ghi trực tiếp vào HTTP Response Body chứ không tìm kiếm file HTML nào cả.

---

### ❓ Câu 3: Làm thế nào Spring Boot tự động chuyển một `List<Product>` thành JSON mà ta không cần viết code chuyển đổi?

**Trả lời mẫu:**

- Nhờ vào cơ chế **`HttpMessageConverter`** của Spring Web kết hợp với thư viện **Jackson** (được tích hợp sẵn trong `spring-boot-starter-web`).
- Khi thấy class được đánh dấu `@RestController` hoặc method có `@ResponseBody`, Spring Boot sẽ tự động gọi `MappingJackson2HttpMessageConverter`. Bộ chuyển đổi này dùng cơ chế Reflection đọc các trường thông qua Getter của đối tượng Java để tuần tự hóa (serialize) thành chuỗi JSON tương ứng.

---

### ❓ Câu 4: Phân biệt `@PathVariable` và `@RequestParam`? Khi nào nên dùng loại nào?

**Trả lời mẫu:**

- `@PathVariable`: Trích xuất dữ liệu trực tiếp từ cấu trúc URI (ví dụ: `/faculties/1/students` thì `1` là PathVariable). Dùng khi định danh một **tài nguyên cụ thể**.
- `@RequestParam`: Trích xuất dữ liệu từ Query Parameters nằm sau dấu `?` trên URL (ví dụ: `/search?facultyName=CNTT`). Dùng khi cần **tìm kiếm, lọc, phân trang hoặc sắp xếp**.

---

### ❓ Câu 5: Tại sao trong bài giảng Thầy lại yêu cầu tách tầng `Service` (`FacultyService`) thay vì viết hết trong `Controller`?

**Trả lời mẫu:**

- Để tuân thủ nguyên lý thiết kế **Separation of Concerns (Phân tách mối quan tâm)** và **Single Responsibility Principle (Trách nhiệm đơn lẻ)**:
  - **Controller** chỉ làm nhiệm vụ giao tiếp: Nhận request từ Client, kiểm tra tính hợp lệ cơ bản, gọi tầng Service và trả về kết quả.
  - **Service** là nơi chứa toàn bộ **nghiệp vụ cốt lõi (Business Logic)**: Lọc, xử lý, tính toán dữ liệu.
- Tách như vậy giúp code dễ bảo trì, dễ viết Unit Test độc lập và có thể tái sử dụng Service ở nhiều Controller khác nhau.

---

### ❓ Câu 6: Dependency Injection (DI) và Inversion of Control (IoC) trong Spring Boot là gì và thể hiện ở đâu trong bài?

**Trả lời mẫu:**

- **IoC (Đảo ngược quyền điều khiển):** Thay vì lập trình viên phải tự dùng từ khóa `new` để tạo và quản lý vòng đời của đối tượng, Spring IoC Container sẽ nắm quyền khởi tạo, cấu hình và quản lý các đối tượng đó (gọi là các Spring Beans).
- **DI (Tiêm phụ thuộc):** Là cách thức hiện thực của IoC. Thay vì trong `FacultyRestController` ta viết `facultyService = new FacultyService()`, ta khai báo thông qua Constructor hoặc `@Autowired`, Spring Container sẽ tự động tìm Bean `FacultyService` đã tạo sẵn và "tiêm" vào Controller khi khởi chạy.

---

### ❓ Câu 7: Annotation `@SpringBootApplication` có vai trò gì và bao gồm những annotation con nào?

**Trả lời mẫu:**
`@SpringBootApplication` là annotation trung tâm đặt ở Main class, tương đương với 3 annotation:

1. `@SpringBootConfiguration`: Đánh dấu class cấu hình.
2. `@EnableAutoConfiguration`: Tự động nhận diện thư viện trong classpath để cấu hình tự động (như tự cấu hình Tomcat, Jackson, Thymeleaf).
3. `@ComponentScan`: Tự động quét từ package hiện tại trở đi để tìm kiếm các Bean (`@Component`, `@Controller`, `@Service`, `@Repository`) đưa vào Container.

---

### ❓ Câu 8: Khi chạy project Spring Boot gặp lỗi `Port 8081 was already in use`, nguyên nhân là gì và cách xử lý thế nào?

**Trả lời mẫu:**

- **Nguyên nhân:** Cổng mạng 8081 đã bị chiếm dụng bởi một tiến trình khác đang chạy ngầm (ví dụ: một tiến trình Java/Tomcat chạy trước đó chưa được tắt triệt để).
- **Cách xử lý:**
  1. Tìm và tắt tiến trình đang chiếm cổng: Dùng lệnh Windows PowerShell `Get-NetTCPConnection -LocalPort 8081` để lấy PID, sau đó chạy `Stop-Process -Id <PID> -Force`.
  2. Hoặc đổi ứng dụng sang cổng khác trong file `application.properties` bằng lệnh: `server.port=8083`.

---

### ❓ Câu 9: Trong Thymeleaf, cú pháp `th:each` và `th:text` hoạt động như thế nào?

**Trả lời mẫu:**

- `th:each="item : ${collection}"`: Hoạt động như vòng lặp `for-each` trong Java. Với mỗi phần tử trong danh sách `collection` lấy từ Model, Thymeleaf sẽ nhân bản thẻ HTML tương ứng.
- `th:text="${expression}"`: Đánh giá biểu thức trong dấu `${...}` và gán kết quả dạng văn bản an toàn (tự động escape HTML để chống tấn công XSS) vào nội dung của thẻ.

---

### ❓ Câu 10: Làm thế nào để kiểm tra (test) một REST API nếu không xây dựng giao diện web HTML?

**Trả lời mẫu:**
Có thể kiểm tra theo các cách sau:

1. **Dùng Trình duyệt (với các request GET):** Gõ trực tiếp URL `http://localhost:8082/api/faculty/1/students` để xem chuỗi JSON trả về.
2. **Dùng công cụ chuyên dụng (Postman, Insomnia):** Cho phép test toàn bộ các method HTTP (`GET`, `POST`, `PUT`, `DELETE`), gửi kèm Header, Body (JSON).
3. **Dùng lệnh dòng lệnh cURL / PowerShell:**
   ```powershell
   curl.exe http://localhost:8082/api/faculty/1/students
   ```
4. **Tích hợp Swagger / OpenAPI:** Tự động tạo giao diện tài liệu tương tác trực quan ngay trên trình duyệt.

---

*Tài liệu được biên soạn đồng bộ với mã nguồn thực tế tại thư mục `b5_basic_web`, `b6_independent_web` và bài giảng thực hành tại trường.*
