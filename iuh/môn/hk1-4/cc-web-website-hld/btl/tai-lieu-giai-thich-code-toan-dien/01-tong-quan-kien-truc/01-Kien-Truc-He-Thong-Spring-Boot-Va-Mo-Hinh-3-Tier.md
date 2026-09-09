# KIẾN TRÚC HỆ THỐNG SPRING BOOT VÀ MÔ HÌNH 3-TIER (3 LỚP)

> **Mục tiêu tài liệu**: Giúp bất kỳ sinh viên nào (dù chưa từng học lập trình Web) cũng có thể hiểu tường tận cách ứng dụng Web vận hành, luồng đi của dữ liệu từ trình duyệt đến cơ sở dữ liệu, và tự tin trả lời bất kỳ câu hỏi vấn đáp nào của giảng viên.

---

## 1. TỔNG QUAN VỀ DỰ ÁN BLOG WEBSITE

Dự án **Blog Website (Bleb Blog)** là một ứng dụng Web hiện đại kết hợp giữa:
- **Backend**: Xây dựng trên nền tảng **Java 21** và framework **Spring Boot 3.5.11**. Cung cấp hệ thống RESTful API chuẩn mực, xử lý logic nghiệp vụ, xác thực phân quyền bằng JWT (JSON Web Token), và giao tiếp cơ sở dữ liệu qua Spring Data JPA (Hibernate).
- **Database**: Sử dụng **H2 Database** lưu trữ file (`./data/blogdb.mv.db`), tự động tạo bảng (DDL auto-update), cấu hình chuẩn tương thích MySQL (`MODE=MySQL`), cho phép chạy độc lập ngay lập tức mà không phụ thuộc vào việc cài đặt MySQL Server bên ngoài.
- **Lưu trữ hình ảnh đám mây**: Tích hợp **Cloudinary API** để tải lên và lưu trữ ảnh đại diện (avatar), ảnh bài viết (banner) với URL HTTPS vĩnh viễn.
- **Frontend**: Kết hợp giữa **Thymeleaf Template Engine** (render giao diện phía server) và **JavaScript thuần (Vanilla JS / ES6)** phía client, gọi các REST API bất đồng bộ (AJAX/Fetch API), lưu trữ token JWT trong `localStorage`.

---

## 2. MÔ HÌNH KIẾN TRÚC 3 LỚP (3-TIER ARCHITECTURE)

Trong kỹ nghệ phần mềm và các đồ án môn học tại IUH, mô hình 3 lớp là tiêu chuẩn bắt buộc nhằm đảm bảo nguyên lý **Đơn nhiệm (Single Responsibility Principle)** và **Dễ bảo trì, mở rộng (Maintainability & Scalability)**.

```
+-------------------------------------------------------------------------------+
|                             CLIENT BROWSER                                    |
|   HTML5 + CSS3 + Bootstrap 5 + Vanilla JavaScript (Fetch API / LocalStorage)  |
+-------------------------------------------------------------------------------+
                                      │  ▲
              HTTP Request (REST API) │  │ JSON Response (ApiResponse<T>)
           Kèm Header: Authorization: │  │ Status: 200 OK / 400 Bad Request
                     Bearer <JWT>     ▼  │
+───────────────────────────────────────────────────────────────────────────────+
|                         TẦNG 1: CONTROLLER LAYER                              |
|   - Tiếp nhận HTTP Request (GET, POST, PUT, DELETE).                          |
|   - Kiểm tra dữ liệu đầu vào (@Valid, BindingResult).                         |
|   - Gọi Service tương ứng và đóng gói kết quả vào ApiResponse<T>.             |
|   - Ví dụ: BlogController, AuthenticationController, UserController           |
+───────────────────────────────────────────────────────────────────────────────+
                                      │  ▲
                    DTO / Model Object│  │ DTO / Entity
                                      ▼  │
+───────────────────────────────────────────────────────────────────────────────+
|                          TẦNG 2: SERVICE LAYER                                |
|   - Trái tim của hệ thống: Chứa 100% LOGIC NGHIỆP VỤ (Business Logic).        |
|   - Kiểm tra điều kiện: Tài khoản có bị khóa không? Blog có tồn tại không?    |
|     Mật khẩu cũ có đúng không? Người dùng có quyền sửa bài này không?         |
|   - Quản lý giao dịch (@Transactional): Đảm bảo tính toàn vẹn dữ liệu.        |
|   - Ví dụ: BlogService, AuthenticationService, UserService, InteractionService|
+───────────────────────────────────────────────────────────────────────────────+
                                      │  ▲
                             Java Call│  │ Entity Record
                                      ▼  │
+───────────────────────────────────────────────────────────────────────────────+
|                        TẦNG 3: REPOSITORY LAYER (DAO)                         |
|   - Tầng giao tiếp trực tiếp với Cơ sở dữ liệu thông qua Spring Data JPA.     |
|   - Tự động sinh câu lệnh SQL (SELECT, INSERT, UPDATE, DELETE) từ tên method. |
|   - Sử dụng các interface kế thừa JpaRepository<Entity, ID>.                  |
|   - Ví dụ: UserRepository, BlogRepository, CategoryRepository...              |
+───────────────────────────────────────────────────────────────────────────────+
                                      │  ▲
                        SQL Statement │  │ Result Set
                         (H2 / MySQL) ▼  │
+───────────────────────────────────────────────────────────────────────────────+
|                             DATABASE ENGINE                                   |
|                H2 Database Engine (Lưu trữ file ./data/blogdb)                |
+───────────────────────────────────────────────────────────────────────────────+
```

---

## 3. GIẢI THÍCH CHI TIẾT TỪNG THÀNH PHẦN TRONG KIẾN TRÚC

### 3.1. Client (Trình duyệt người dùng)
- **Nhiệm vụ**: Hiển thị giao diện cho người dùng, bắt các sự kiện (click nút đăng nhập, nhập form viết blog, nhấn nút like/bookmark).
- **Cơ chế hoạt động**:
  - Khi người dùng đăng nhập thành công, trình duyệt nhận về một chuỗi mã hóa gọi là **JWT Token** (JSON Web Token).
  - Trình duyệt lưu chuỗi này vào bộ nhớ tạm `localStorage.setItem('token', token)`.
  - Trong mọi yêu cầu tiếp theo cần quyền đăng nhập (ví dụ: tạo bài viết, sửa profile, bấm like), JavaScript sẽ tự động chèn token này vào Header:
    ```http
    Authorization: Bearer eyJhbGciOiJIUzUxMiJ9...
    ```

### 3.2. Tầng Controller (`com.group.blog.controller`)
- **Nhiệm vụ**: Đóng vai trò là "lễ tân" tiếp nhận mọi yêu cầu gửi đến server.
- **Đặc điểm**:
  - Được đánh dấu bởi annotation `@RestController` (kết hợp của `@Controller` và `@ResponseBody`), nghĩa là toàn bộ dữ liệu trả về từ các hàm trong Controller sẽ được tự động chuyển đổi thành định dạng **JSON** để gửi về cho client.
  - Sử dụng `@RequestMapping("/blogs")` để định tuyến đường dẫn URL.
  - Sử dụng `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping` để tương ứng với 4 hành vi chuẩn của REST: Đọc, Tạo mới, Cập nhật, Xóa (CRUD).
  - **Quy tắc vàng**: Controller **tuyệt đối không** viết code xử lý nghiệp vụ phức tạp (như tính toán điểm số, mã hóa mật khẩu, kiểm tra logic phức tạp). Mọi việc nặng đều chuyển giao cho tầng Service.

### 3.3. Tầng Service (`com.group.blog.service`)
- **Nhiệm vụ**: Là "bộ não" của toàn bộ hệ sinh thái phần mềm.
- **Đặc điểm**:
  - Đánh dấu bằng `@Service`.
  - Nhận DTO (Data Transfer Object) từ Controller chuyển xuống.
  - Kiểm tra xem dữ liệu có hợp lý không (Ví dụ: kiểm tra username đã có ai đăng ký trước đó chưa bằng `userRepository.existsByUsername(request.getUsername())`). Nếu vi phạm, lập tức ném ra ngoại lệ `throw new AppException(ErrorCode.USER_EXISTED);`.
  - Thực hiện mã hóa mật khẩu bằng thuật toán an toàn `BCryptPasswordEncoder`.
  - Tạo chuỗi định danh slug cho bài viết (Ví dụ: tiêu đề "Học Spring Boot Dễ Lắm" -> slug "hoc-spring-boot-de-lam").
  - Đảm bảo tính nhất quán qua annotation `@Transactional`.

### 3.4. Tầng Repository (`com.group.blog.repository`)
- **Nhiệm vụ**: Đóng vai trò là "thủ thư" phụ trách việc lấy và cất dữ liệu vào kho (Database).
- **Đặc điểm**:
  - Sử dụng công nghệ **Spring Data JPA**.
  - Lập trình viên chỉ cần khai báo một `interface` kế thừa `JpaRepository<Entity, ID>`.
  - Lợi ích vượt trội: Không cần phải viết những câu lệnh SQL thủ công dài dòng như `SELECT * FROM tbl_user WHERE username = ?` hay `INSERT INTO tbl_user VALUES (...)`. Spring Data JPA tự động dịch tên hàm (ví dụ: `findByUsername(String username)`) thành câu lệnh SQL chuẩn xác chạy ngầm bên dưới.

### 3.5. Tầng Thực thể Entity (`com.group.blog.entity`)
- **Nhiệm vụ**: Ánh xạ các bảng trong cơ sở dữ liệu thành các lớp đối tượng Java (kỹ thuật ORM - Object Relational Mapping).
- **Ví dụ**:
  - Bảng `users` tương ứng với class `User.java`.
  - Bảng `blogs` tương ứng với class `Blog.java`.
  - Bảng `categories` tương ứng với class `Category.java`.
  - Mỗi cột trong bảng tương ứng với một biến thuộc tính trong Java.

### 3.6. DTO (Data Transfer Object) và Mapper
- **DTO là gì?**: Là đối tượng chỉ dùng để mang dữ liệu qua lại giữa Client và Controller.
  - Ví dụ: Khi người dùng đăng ký tài khoản, họ gửi lên `UserCreatetionRequest` (chỉ gồm `username`, `password`, `email`). Server sẽ không trả nguyên đối tượng `User` về cho Client (vì trong đó có mật khẩu mã hóa), mà chỉ trả về `UserResponse` (chỉ gồm `id`, `username`, `email`, `avatarUrl`, `roles`).
- **Mapper (MapStruct)**: Thư viện tự động sao chép các trường dữ liệu từ DTO sang Entity và ngược lại, giúp code cực kỳ sạch sẽ, không cần phải gọi thủ công hàng loạt lệnh `set...()` / `get...()`.

### 3.7. Global Exception Handler (Xử lý lỗi tập trung)
- Đánh dấu bằng `@ControllerAdvice` hoặc `@RestControllerAdvice`.
- Bất kỳ nơi nào trong hệ thống gặp lỗi (ví dụ: sai mật khẩu, tài nguyên không tìm thấy, trùng lặp email), hệ thống chỉ cần ném ra `throw new AppException(ErrorCode.PASSWORD_INCORRECT)`.
- `GlobalExceptionHandler` sẽ ngay lập tức "bắt" lấy ngoại lệ này và định dạng lại thành chuỗi JSON chuẩn mực:
  ```json
  {
    "code": 1007,
    "message": "Password is incorrect",
    "result": null
  }
  ```
  Nhờ đó, ứng dụng không bao giờ bị sập (crash) hoặc hiện lỗi HTML trắng trang xấu xí cho người dùng.

---

## 4. VÒNG ĐỜI CỦA MỘT HTTP REQUEST (HTTP REQUEST LIFECYCLE)

Hãy cùng đi theo bước chân của một request điển hình: **Người dùng bấm nút Đăng nhập** trên trình duyệt:

1. **Client**: Người dùng nhập username `admin` và password `123456`, bấm "Đăng nhập". File JavaScript `auth.js` gửi một HTTP POST request tới URL: `http://localhost:8080/auth/login` với body JSON:
   ```json
   {"username": "admin", "password": "123456"}
   ```
2. **Spring Security Filter**:
   - Request đi qua chuỗi các bộ lọc bảo mật (`SecurityFilterChain`).
   - Bộ lọc kiểm tra URL `/auth/login`. URL này nằm trong danh sách `PUBLIC_POST_ENDPOINTS` nên được cho phép đi tiếp (`permitAll()`) mà không bắt buộc phải có token trước.
3. **Controller**:
   - `AuthenticationController.authenticate()` nhận payload và chuyển thành đối tượng `AuthenticationRequest`.
   - Controller chuyển tiếp cho `AuthenticationService.authenticate(request)`.
4. **Service**:
   - `AuthenticationService` gọi `userRepository.findByUsername("admin")` để truy vấn người dùng trong Database.
   - Nếu không thấy, ném ngoại lệ `USER_NOT_EXISTED`.
   - Nếu thấy, dùng `passwordEncoder.matches("123456", user.getPassword())` để so khớp mật khẩu người dùng vừa nhập với chuỗi hash BCrypt đã lưu trong DB.
   - Nếu khớp, hàm `generateToken(user)` được gọi để tạo ra chuỗi JWT có chữ ký số HMAC-SHA512.
5. **Controller trả về**:
   - Đóng gói token vào `ApiResponse<AuthenticationResponse>` với mã code `1000` (Thành công).
6. **Client nhận kết quả**:
   - Trình duyệt lưu token vào `localStorage`, hiển thị thông báo "Đăng nhập thành công" và chuyển hướng người dùng về trang chủ `/home`.

---

## 5. BỘ CÂU HỎI VẤN ĐÁP CỐT LÕI VỀ KIẾN TRÚC VÀ CÂU TRẢ LỜI ĐẠT ĐIỂM 10

### Câu 1: Em hãy giải thích mô hình 3 lớp của dự án này? Tại sao không viết hết code vào Controller cho nhanh mà phải chia ra Service và Repository?
- **Trả lời ghi điểm tối đa**:
  > "Thưa thầy/cô, dự án của nhóm em áp dụng chuẩn kiến trúc 3 lớp:
  > 1. **Tầng Controller**: Chỉ đảm nhận nhiệm vụ giao tiếp với Client, đón nhận HTTP Request, validate sơ bộ dữ liệu đầu vào và trả về JSON chuẩn thông qua DTO.
  > 2. **Tầng Service**: Chứa toàn bộ nghiệp vụ logic của bài toán (như kiểm tra điều kiện tạo bài viết, băm mật khẩu, xử lý slug, kiểm tra quyền tác giả).
  > 3. **Tầng Repository**: Đảm nhận việc giao tiếp với cơ sở dữ liệu bằng Spring Data JPA.
  > 
  > Việc phân tách 3 lớp này nhằm tuân thủ nguyên lý Đơn nhiệm (Single Responsibility Principle). Nếu gom tất cả vào Controller, code sẽ trở thành 'Spaghetti code' rất dài, khó đọc, không thể tái sử dụng logic ở nhiều nơi, không thể viết Unit Test độc lập cho từng nghiệp vụ và khi có thay đổi về cơ sở dữ liệu sẽ phải sửa lại toàn bộ Controller."

### Câu 2: DTO là gì và tại sao trong dự án này nhóm lại dùng DTO mà không dùng trực tiếp Entity để hứng dữ liệu từ Client?
- **Trả lời ghi điểm tối đa**:
  > "Thưa thầy/cô, DTO là viết tắt của **Data Transfer Object** (đối tượng truyền tải dữ liệu).
  > Nhóm em tuyệt đối không phơi bày Entity ra tầng giao diện vì 3 lý do sống còn:
  > 1. **Bảo mật (Security)**: Entity `User` chứa trường nhạy cảm là mật khẩu đã mã hóa (`password`). Nếu trả thẳng Entity ra ngoài, hacker có thể đọc được hash mật khẩu. DTO `UserResponse` chỉ chọn lọc các trường công khai như username, email, avatar.
  > 2. **Chống tấn công Over-posting / Mass Assignment**: Nếu dùng Entity để hứng form gửi lên, kẻ tấn công có thể chèn thêm trường `role: ADMIN` trong gói tin JSON để tự nâng cấp quyền của mình. DTO chỉ nhận đúng những trường mà hệ thống cho phép sửa.
  > 3. **Tránh lỗi đệ quy vòng lặp JSON (Infinite Recursion)**: Trong quan hệ hai chiều của JPA (như Blog chứa Comment, Comment lại chứa Blog), nếu chuyển Entity trực tiếp thành JSON sẽ gây ra lỗi `StackOverflowError` làm sập server."

### Câu 3: Cơ chế Stateless trong hệ thống này hoạt động như thế nào?
- **Trả lời ghi điểm tối đa**:
  > "Thưa thầy/cô, hệ thống của nhóm em hoạt động theo cơ chế **Stateless hoàn toàn** (không lưu phiên làm việc trên bộ nhớ của Server). Trong file `SecurityConfig.java`, tụi em cấu hình `SessionCreationPolicy.STATELESS`.
  > Điều này có nghĩa là Server không duy trì `HttpSession` hay bộ nhớ cache nào cho người dùng đăng nhập. Thay vào đó, mỗi khi người dùng gửi một yêu cầu, Client phải đính kèm chuỗi **JWT Token** vào tiêu đề `Authorization: Bearer <token>`. Server chỉ cần dùng chữ ký số bí mật (Signer Key) để giải mã và xác thực token đó. Cơ chế này giúp hệ thống tiết kiệm RAM tối đa và rất dễ dàng mở rộng sang mô hình đa máy chủ (Load Balancing)."
