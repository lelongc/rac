# TỔNG HỢP LÝ THUYẾT WEB SERVICE & RESTFUL API (CHƯƠNG CUỐI)
**Tài liệu ôn thi Cuối kỳ - Môn: Phát triển hệ thống phân tán (IUH)**  
*Sinh viên: Lê Thành Long - MSSV: 23630851*

---

## I. TỔNG QUAN VỀ WEB SERVICE & KIẾN TRÚC SOA

### 1. Web Service là gì?
- **Web Service** là một thành phần phần mềm cung cấp dịch vụ thông qua mạng máy tính, cho phép các ứng dụng viết bằng các ngôn ngữ khác nhau (Java, C#, Python, PHP) và chạy trên các hệ điều hành khác nhau (Windows, Linux, macOS) có thể giao tiếp và trao đổi dữ liệu với nhau qua các giao thức Web chuẩn (**HTTP**, **JSON**, **XML**).
- Bản chất: Là giải pháp hiện đại thay thế cho các cơ chế RPC (Remote Procedure Call) và Java RMI truyền thống, khắc phục được rào cản tường lửa (Firewall) vì chạy trực tiếp trên cổng Web tiêu chuẩn (Port 80/HTTP, 443/HTTPS, 8080).

### 2. Mô hình kiến trúc hướng dịch vụ (SOA - Service Oriented Architecture)
Kiến trúc SOA gồm 3 thực thể (Roles) và 3 thao tác cơ bản (Operations):
- **3 Thực thể**:
  1. **Service Provider** (Nhà cung cấp dịch vụ): Xây dựng và triển khai Web service trên máy chủ, tạo bản mô tả dịch vụ và công bố lên Registry.
  2. **Service Requester / Consumer** (Bên yêu cầu dịch vụ): Ứng dụng client tìm kiếm dịch vụ và gửi yêu cầu sử dụng dịch vụ.
  3. **Service Registry / Broker** (Trung gian đăng ký): Nơi lưu trữ danh bạ các dịch vụ và chỉ dẫn cách kết nối (ví dụ: UDDI trong SOAP, API Marketplace trong REST).
- **3 Thao tác**:
  1. **Publish** (Công bố): Provider đưa mô tả dịch vụ lên Registry.
  2. **Find** (Tìm kiếm): Requester tra cứu Registry để tìm dịch vụ phù hợp.
  3. **Bind** (Ràng buộc / Gọi): Requester gọi trực tiếp dịch vụ tại Provider dựa theo mô tả kỹ thuật đã nhận được.

---

## II. SO SÁNH CHI TIẾT SOAP VÀ RESTFUL (TRỌNG TÂM ĐỀ THI)

| Tiêu chí | RESTful (Representational State Transfer) | SOAP (Simple Object Access Protocol) |
| :--- | :--- | :--- |
| **Bản chất** | Là một **kiểu kiến trúc phần mềm** (Architectural Style). | Là một **giao thức truyền thông chuẩn hóa** (Standard Protocol). |
| **Định dạng dữ liệu** | Đa dạng, linh hoạt: **JSON** (ưu tiên), XML, HTML, Text, YAML. | Bắt buộc **chỉ dùng XML**. |
| **Giao thức mạng** | Gắn liền trực tiếp với **HTTP / HTTPS**. | Độc lập giao thức: Chạy trên HTTP, SMTP, TCP, JMS. |
| **Mô tả dịch vụ** | Dùng Swagger / OpenAPI, RAML hoặc tài liệu API. | Dùng file **WSDL** (Web Services Description Language) định dạng XML chặt chẽ. |
| **Độ phức tạp** | Rất đơn giản, nhẹ, dễ đọc, dễ học và triển khai nhanh. | Nặng nề, phức tạp, cấu trúc XML dài dòng (Envelope, Header, Body, Fault). |
| **Băng thông & Hiệu năng** | **Rất nhanh, tiêu tốn ít băng thông** do JSON ngắn gọn, không có overhead. | **Chậm hơn, tốn băng thông** vì kích thước file XML lớn và tốn tài nguyên parse XML. |
| **Khả năng Caching** | **Có hỗ trợ mạnh mẽ** thông qua cơ chế HTTP Cache-Control, ETag. | Không thể cache vì phần lớn request đều gửi qua HTTP POST. |
| **Bảo mật** | Dùng chuẩn bảo mật Web thông dụng: **HTTPS/TLS, OAuth2, JWT, API Key**. | Dùng **WS-Security** (bảo mật cấp độ thông điệp cực kỳ nghiêm ngặt). |
| **Tính toàn vẹn giao dịch** | Không tích hợp sẵn chuẩn giao dịch ACID phân tán. | Hỗ trợ chuẩn **WS-AtomicTransaction** cho giao dịch tài chính ACID. |
| **Ứng dụng thực tế** | Web API hiện đại, Mobile Apps, Hệ thống Microservices, IoT. | Ngân hàng, Tài chính, Quân sự, Hệ thống doanh nghiệp lớn (Legacy Enterprise). |

---

## III. 6 NGUYÊN TẮC RÀNG BUỘC KIẾN TRÚC REST (ARCHITECTURAL CONSTRAINTS)

Để một Web Service được gọi là **RESTful**, hệ thống bắt buộc phải tuân theo 6 nguyên tắc (được đề xuất bởi Roy Fielding - 2000):

1. **Client - Server (Kiến trúc Khách - Chủ)**:
   - Tách biệt hoàn toàn giữa giao diện người dùng (Client) và nơi xử lý dữ liệu/lưu trữ (Server).
   - Cho phép giao diện phát triển độc lập (Web, React, Flutter, iOS) mà không ảnh hưởng tới backend.
2. **Stateless (Phi trạng thái - CỰC KỲ QUAN TRỌNG)**:
   - Server **không lưu trữ bất kỳ trạng thái phiên (session state)** nào của Client giữa các request.
   - Mỗi request từ Client gửi lên Server phải chứa **đầy đủ mọi thông tin cần thiết** để Server hiểu và xử lý (bao gồm cả token xác thực).
   - *Ưu điểm*: Khả năng mở rộng (Scalability) cực cao vì bất kỳ máy chủ nào trong cụm đều có thể xử lý request.
3. **Cacheable (Khả năng lưu bộ đệm)**:
   - Các phản hồi (Response) từ Server phải được đánh dấu rõ ràng có được lưu cache hay không (thông qua HTTP Header `Cache-Control`).
   - Giúp giảm tải cho server và tăng tốc độ phản hồi cho người dùng.
4. **Uniform Interface (Giao diện đồng nhất)**:
   - Đây là đặc trưng cốt lõi của REST. Bao gồm 4 khía cạnh:
     * Định danh tài nguyên qua URI chuẩn (`/api/products/1`).
     * Thao tác tài nguyên qua các biểu diễn (JSON/XML).
     * Thông điệp tự mô tả (Self-descriptive messages - có Content-Type rõ ràng).
     * HATEOAS (Hypermedia As The Engine Of Application State - trả kèm link điều hướng tiếp theo).
5. **Layered System (Hệ thống phân tầng)**:
   - Client không thể phân biệt được nó đang kết nối trực tiếp đến Server đích hay qua các tầng trung gian (Proxy, API Gateway, Load Balancer, Cache CDN).
   - Tăng cường tính bảo mật và khả năng cân bằng tải.
6. **Code on Demand (Mã lệnh theo yêu cầu - Tùy chọn)**:
   - Server có thể tạm thời mở rộng tính năng của Client bằng cách truyền tải mã thực thi (như JavaScript).

---

## IV. CÁC THÀNH PHẦN RESTFUL & QUY TẮC MAPPING HTTP METHODS

### 1. Thành phần RESTful cơ bản
- **Resource (Tài nguyên)**: Mọi thực thể trong hệ thống đều là tài nguyên (User, Product, Student, Order). Đặt tên bằng **danh từ số nhiều** (`/products`, `/students`), không dùng động từ.
- **Representation (Biểu diễn)**: Định dạng dữ liệu trao đổi (phổ biến nhất là JSON).
- **URI (Uniform Resource Identifier)**: Địa chỉ duy nhất định danh tài nguyên trên mạng (`http://localhost:8080/api/products/123`).

### 2. Bảng ánh xạ HTTP Methods với thao tác CRUD

| Thao tác CRUD | HTTP Method | Endpoint ví dụ | Ý nghĩa & Hành động | Tính Idempotent* | Tính Safe* |
| :--- | :---: | :--- | :--- | :---: | :---: |
| **Create** (Tạo mới) | **POST** | `/api/products` | Thêm mới 1 sản phẩm vào hệ thống. Dữ liệu gửi trong Request Body. | **Không** | **Không** |
| **Read** (Xem tất cả) | **GET** | `/api/products` | Lấy danh sách toàn bộ sản phẩm. | **Có** | **Có** |
| **Read** (Xem chi tiết) | **GET** | `/api/products/{id}` | Lấy thông tin chi tiết của sản phẩm có mã `id`. | **Có** | **Có** |
| **Update** (Sửa toàn bộ) | **PUT** | `/api/products/{id}` | Cập nhật/thay thế toàn bộ thông tin của sản phẩm `id`. | **Có** | **Không** |
| **Update** (Sửa một phần) | **PATCH** | `/api/products/{id}` | Cập nhật một vài trường thông tin cụ thể (ví dụ chỉ đổi giá). | **Không** | **Không** |
| **Delete** (Xóa) | **DELETE** | `/api/products/{id}` | Xóa sản phẩm có mã `id` ra khỏi hệ thống. | **Có** | **Không** |

> **Giải thích thuật ngữ quan trọng**:
> - **Safe (An toàn)**: Phương thức chỉ đọc dữ liệu, không làm thay đổi trạng thái máy chủ (GET).
> - **Idempotent (Đồng nhất/Bất biến)**: Thực hiện gọi 1 lần hay gọi n lần liên tiếp với cùng dữ liệu đều tạo ra cùng một kết quả trên hệ thống (GET, PUT, DELETE).

### 3. Bảng mã trạng thái HTTP (HTTP Status Codes) hay gặp

| Mã Status Code | Tên chuẩn | Ý nghĩa & Khi nào dùng |
| :---: | :--- | :--- |
| **200** | **OK** | Thành công. Trả về kết quả cho các request GET, PUT, DELETE thành công. |
| **201** | **Created** | Tạo mới thành công. Trả về sau request POST thêm mới tài nguyên. |
| **204** | **No Content** | Xử lý thành công nhưng không có nội dung trả về (thường dùng cho DELETE). |
| **400** | **Bad Request** | Lỗi từ client: Sai cú pháp JSON, thiếu tham số bắt buộc. |
| **401** | **Unauthorized** | Chưa xác thực: Thiếu Token hoặc Token hết hạn. |
| **403** | **Forbidden** | Bị cấm truy cập: Đã đăng nhập nhưng không đủ quyền hạn (Role/Permission). |
| **404** | **Not Found** | Không tìm thấy tài nguyên ứng với URI/ID yêu cầu. |
| **405** | **Method Not Allowed** | Phương thức HTTP không được hỗ trợ trên endpoint (ví dụ: POST vào route chỉ có GET). |
| **500** | **Internal Server Error** | Lỗi nội bộ server: Bị crash, NullPointerException, lỗi database. |

---

## V. KIẾN TRÚC SPRING BOOT & SPRING MVC

### 1. Spring Boot là gì và tại sao được ưa chuộng?
- **Khái niệm**: Spring Boot là một nền tảng dựa trên Spring Framework giúp xây dựng các ứng dụng Java độc lập, cấu hình sẵn (Opinionated), sẵn sàng cho môi trường Production mà không cần cấu hình XML phức tạp.
- **3 Cốt lõi của Spring Boot**:
  1. **Auto Configuration**: Tự động cấu hình các thành phần dựa trên các thư viện jar có trong classpath.
  2. **Starter Dependencies**: Gom cụm các thư viện liên quan thành một dependency duy nhất (ví dụ: `spring-boot-starter-web`).
  3. **Embedded Web Server**: Tích hợp sẵn máy chủ Tomcat bên trong file JAR, chỉ cần chạy lệnh `java -jar app.jar` là xong, không cần cài đặt Tomcat bên ngoài.

### 2. Các khái niệm cốt lõi: Bean, IoC và Dependency Injection
- **Spring Bean**: Là một đối tượng Java được khởi tạo, quản lý và hủy bởi **Spring IoC Container**.
- **IoC (Inversion of Control - Đảo ngược điều khiển)**: Lập trình viên không tự dùng lệnh `new Object()` để khởi tạo đối tượng; thay vào đó, Spring Container sẽ chịu trách nhiệm tạo và quản lý chúng.
- **Dependency Injection (DI - Tiêm phụ thuộc)**: Cơ chế Spring tự động cung cấp (inject) các Bean phụ thuộc vào nơi cần sử dụng thông qua annotation `@Autowired` hoặc qua Constructor.

### 3. Phân biệt `@Controller` và `@RestController`
- `@Controller`: Dùng cho mô hình MVC truyền thống. Trả về tên file **Giao diện/View Template** (HTML qua Thymeleaf, JSP).
- `@RestController`: Dùng cho xây dựng **RESTful Web Service**. Tự động kết hợp giữa `@Controller` và `@ResponseBody`. Trả về **dữ liệu thô (JSON/XML)** trực tiếp trong HTTP Response Body thông qua thư viện chuyển đổi Jackson.

### 4. Cấu trúc chuẩn 3 tầng trong Spring Boot
1. **Controller Layer** (`@RestController`): Tiếp nhận HTTP Request từ Client, gọi Service xử lý và trả về HTTP Response.
2. **Service Layer** (`@Service`): Chứa toàn bộ nghiệp vụ (Business Logic), tính toán, xử lý dữ liệu.
3. **Repository Layer** (`@Repository`): Tương tác trực tiếp với Database (Spring Data JPA, Hibernate, JDBC).
4. **Model / Entity Layer**: Đại diện cho các đối tượng dữ liệu trong hệ thống.

### 5. Ý nghĩa các Annotation phổ biến nhất
- `@SpringBootApplication`: Đánh dấu class khởi động chính của Spring Boot (kết hợp `@Configuration`, `@EnableAutoConfiguration`, `@ComponentScan`).
- `@RequestMapping("/path")`: Khai báo URL tiền tố cho cả Controller.
- `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping`: Ánh xạ tương ứng các method GET, POST, PUT, DELETE.
- `@PathVariable`: Trích xuất biến từ đường dẫn URL (ví dụ: `/products/{id}` -> `@PathVariable Long id`).
- `@RequestBody`: Tự động parse chuỗi JSON từ body request thành đối tượng Java.
- `@RequestParam`: Trích xuất query parameter trên URL (ví dụ: `/search?keyword=dell` -> `@RequestParam String keyword`).

---

## VI. CÂU HỎI KINH ĐIỂN DẠNG BỔ SUNG CODE (THƯỜNG GẶP TRONG ĐỀ THI)

### Đề bài: "Cho đoạn code sau, cần bổ sung những gì để trở thành một Web Service hoàn chỉnh?"
```java
public class Student {
    private int id;
    private String name;
    private String email;
    // constructors, getters, setters
}

public class StudentController {
    private List<Student> students = new ArrayList<>();
    
    public List<Student> getAllStudents() {
        return students;
    }
    public Student getStudentById(int id) {
        return students.stream().filter(s -> s.getId() == id).findFirst().orElse(null);
    }
    public Student addStudent(Student newStudent) {
        students.add(newStudent);
        return newStudent;
    }
    public String deleteStudent(int id) {
        students.removeIf(s -> s.getId() == id);
        return "Deleted student with ID: " + id;
    }
}
```

### Hướng dẫn trả lời trọn vẹn điểm tối đa:
Cần bổ sung các thành phần sau:
1. **Bổ sung các Annotation của Spring Web vào Controller**:
   - Thêm `@RestController` trên đầu class `StudentController`.
   - Thêm `@RequestMapping("/api/students")` để định danh đường dẫn URI.
   - Thêm `@GetMapping` cho hàm `getAllStudents()`.
   - Thêm `@GetMapping("/{id}")` và thêm `@PathVariable int id` trong tham số hàm `getStudentById`.
   - Thêm `@PostMapping` và thêm `@RequestBody Student newStudent` trong hàm `addStudent`.
   - Thêm `@DeleteMapping("/{id}")` và thêm `@PathVariable int id` trong hàm `deleteStudent`.
2. **Cấu hình an toàn luồng (Thread-safety)**:
   - Thay `ArrayList<Student>` thành `CopyOnWriteArrayList<Student>` để đảm bảo an toàn khi nhiều request đồng thời truy cập.
3. **Thêm Main Class khởi động Spring Boot**:
   ```java
   @SpringBootApplication
   public class Application {
       public static void main(String[] args) {
           SpringApplication.run(Application.class, args);
       }
   }
   ```
4. **Cấu hình file `pom.xml`**:
   - Thêm dependency `spring-boot-starter-web`.
5. **Tạo Dockerfile để đóng gói container chạy ở port 8080**.

---

## VII. ĐÓNG GÓI DOCKER & LỆNH THI CẦN NHỚ

### 1. Cấu trúc chuẩn file `Dockerfile`
```dockerfile
FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```
- `FROM`: Chọn base image Java 21 gọn nhẹ dạng Alpine Linux (~150MB).
- `WORKDIR`: Đặt thư mục làm việc mặc định trong container là `/app`.
- `COPY`: Sao chép file JAR đã đóng gói từ máy thật vào container đặt tên là `app.jar`.
- `EXPOSE 8080`: Báo hiệu container mở cổng 8080.
- `ENTRYPOINT`: Lệnh thực thi chính chạy ứng dụng Java khi container khởi động.

### 2. Các lệnh Docker nộp bài thi
```powershell
# 1. Đóng gói mã nguồn thành JAR:
mvn clean package -DskipTests

# 2. Build image theo quy ước Username/c2:MaSV
docker build -t shima594/c2:23630851 .

# 3. Chạy container ở cổng 8080:
docker run -d -p 8080:8080 --name product-service shima594/c2:23630851

# 4. Kiểm tra container đang chạy:
docker ps
```
