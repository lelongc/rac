# TOP 50 CÂU HỎI VẤN ĐÁP GIẢNG VIÊN HAY HỎI NHẤT VÀ CÂU TRẢ LỜI ĐẠT ĐIỂM 10

> **Bí kíp phòng thi**: Tài liệu tổng hợp 50 câu hỏi cốt lõi mà các giảng viên bộ môn Công nghệ Phần mềm / Công nghệ Web tại Trường Đại học Công nghiệp TP.HCM (IUH) hay dùng để chất vấn sinh viên. Học thuộc tài liệu này đảm bảo tự tin 100% khi bước vào phòng thi.

---

## PHẦN 1: KIẾN TRÚC TỔNG QUAN, SPRING BOOT & MAVEN (CÂU 1 - 8)

### Câu 1: Framework Spring Boot khác gì so với Spring Framework truyền thống?
- **Trả lời**: Spring Framework truyền thống đòi hỏi cấu hình XML hoặc Java Config rất phức tạp và phải cài đặt máy chủ Tomcat bên ngoài. Spring Boot ra đời với 3 ưu điểm cốt tử:
  1. **Tự động cấu hình (Auto-Configuration)** dựa trên các thư viện có trong classpath.
  2. **Máy chủ nhúng (Embedded Server - Tomcat)** tích hợp sẵn, chỉ cần build ra file JAR là chạy được ngay (`java -jar`).
  3. **Các gói Starter Dependencies** gom nhóm các thư viện tương thích, loại bỏ hoàn toàn xung đột phiên bản.

### Câu 2: Em hãy giải thích khái niệm Inversion of Control (IoC) và Dependency Injection (DI)?
- **Trả lời**: 
  - **IoC (Đảo ngược điều khiển)**: Thay vì lập trình viên phải tự dùng lệnh `new` để tạo và quản lý vòng đời của đối tượng, quyền kiểm soát này được trao lại cho Spring Container (ApplicationContext).
  - **DI (Tiêm phụ thuộc)**: Là cơ chế Spring tự động đưa các đối tượng phụ thuộc (Beans) vào một class khi cần (thông qua Constructor hoặc `@Autowired`).

### Câu 3: Tại sao trong các Service của dự án em lại dùng `@RequiredArgsConstructor` thay vì gắn `@Autowired` ở từng trường?
- **Trả lời**: Việc dùng `@RequiredArgsConstructor` kết hợp với các trường `final` là chuẩn thiết kế **Constructor-based Injection**. Cách này vượt trội hơn Field Injection (`@Autowired`) ở chỗ:
  1. Giúp các thuộc tính là `immutable` (bất biến), không bị gán lại sau khi khởi tạo.
  2. Rất dễ viết Unit Test vì có thể truyền đối tượng giả (Mock) trực tiếp qua Constructor mà không cần dùng Reflection của Spring.
  3. Tránh lỗi phụ thuộc vòng tròn (Circular Dependency) lúc ứng dụng khởi động.

### Câu 4: Maven là gì và vòng đời build (Lifecycle) của Maven gồm những giai đoạn nào?
- **Trả lời**: Maven là công cụ quản lý dự án và tự động tải thư viện. Vòng đời build chính gồm: `validate` -> `compile` (biên dịch mã nguồn Java ra `.class`) -> `test` (chạy các bài kiểm thử tự động) -> `package` (đóng gói ra file JAR/WAR) -> `install` -> `deploy`.

### Câu 5: File `pom.xml` có vai trò gì? Thẻ `<parent>` có tác dụng gì?
- **Trả lời**: `pom.xml` chứa thông tin cấu hình dự án, quản lý thư viện và plugin. Thẻ `<parent>` kế thừa `spring-boot-starter-parent` giúp quản lý sẵn phiên bản của hàng trăm thư viện tương thích mà lập trình viên không cần tự khai báo thẻ `<version>` ở từng dependency con.

### Câu 6: Trong dự án này, cơ sở dữ liệu H2 được cấu hình như thế nào?
- **Trả lời**: H2 được cấu hình lưu trữ bền vững thành file vật lý tại `./data/blogdb.mv.db` với chế độ tương thích `MODE=MySQL` và cờ `AUTO_SERVER=TRUE` cho phép cả ứng dụng web và H2 Console cùng truy cập đồng thời mà không bị khóa file.

### Câu 7: Nếu muốn chuyển dự án này sang sử dụng hệ quản trị CSDL MySQL Server thật thì cần làm gì?
- **Trả lời**: Chỉ cần mở file `application.yaml`, sửa chuỗi `spring.datasource.url` trỏ về `jdbc:mysql://localhost:3306/blogdb`, điền `username`, `password` của MySQL và đổi `database-platform` sang MySQL Dialect. Toàn bộ mã nguồn Java và Entity không cần sửa bất kỳ dòng nào vì cú pháp JPA là độc lập với hệ quản trị CSDL!

### Câu 8: Mục đích của thư viện Lombok trong dự án là gì?
- **Trả lời**: Lombok giúp loại bỏ các dòng code thừa (boilerplate code) bằng cách tự động sinh các hàm Getter, Setter, Constructors, `equals`, `hashCode` và Builder Pattern tại thời điểm biên dịch (Compile-time) thông qua các annotation như `@Getter`, `@Setter`, `@Builder`, `@Data`.

---

## PHẦN 2: SPRING SECURITY, JWT & PHÂN QUYỀN (CÂU 9 - 18)

### Câu 9: Trình bày cơ chế hoạt động của JWT (JSON Web Token)?
- **Trả lời**: JWT là một chuỗi mã hóa gồm 3 phần: `Header.Payload.Signature`.
  1. Người dùng đăng nhập với username/password.
  2. Server kiểm tra đúng mật khẩu thì dùng khóa bí mật (`SIGNER_KEY`) ký số tạo ra chuỗi JWT gửi về cho Client.
  3. Client lưu token vào `localStorage`.
  4. Ở các request sau, Client gửi token lên qua header `Authorization: Bearer <token>`.
  5. Server chỉ cần dùng khóa bí mật giải mã và xác minh chữ ký, không cần truy vấn lại bảng mật khẩu trong CSDL.

### Câu 10: Tại sao hệ thống này cấu hình `SessionCreationPolicy.STATELESS`?
- **Trả lời**: Cấu hình Stateless báo cho Spring Security không tạo bất kỳ `HttpSession` nào trên bộ nhớ RAM của Server. Server không lưu trạng thái đăng nhập của người dùng. Điều này giúp hệ thống tiết kiệm tài nguyên máy chủ và cực kỳ thuận tiện khi triển khai hệ thống mở rộng đa máy chủ (Load Balancing / Microservices).

### Câu 11: Tại sao trong `SecurityConfig` lại tắt CSRF (`httpSecurity.csrf(disable)`)?
- **Trả lời**: Vì hệ thống hoạt động theo cơ chế Stateless và sử dụng JWT Bearer Token lưu ở `localStorage`. Tấn công CSRF chỉ nhắm vào các hệ thống xác thực tự động bằng Cookie của trình duyệt. Với JWT trong tiêu đề Authorization, trình duyệt không tự động gửi token nên nguy cơ CSRF không tồn tại, việc tắt CSRF là chuẩn mực để REST API hoạt động thông suốt.

### Câu 12: Thuật toán mã hóa mật khẩu BCrypt hoạt động ra sao?
- **Trả lời**: BCrypt là thuật toán băm mật khẩu một chiều thích ứng. Khi băm, BCrypt tự động sinh ra một chuỗi muối ngẫu nhiên (Salt) dài 16 byte và ghép vào kết quả băm. Do đó, cùng một mật khẩu `"123456"`, mỗi lần băm sẽ ra một chuỗi hoàn toàn khác nhau, ngăn chặn triệt để kỹ thuật tấn công bằng bảng băm tra cứu sẵn (Rainbow Table).

### Câu 13: Làm sao Spring Security phân biệt được vai trò ADMIN và USER?
- **Trả lời**: Khi tạo Token, các quyền được đóng gói vào trường `scope` trong Payload của JWT. Khi giải mã token, Bean `JwtAuthenticationConverter` sẽ gắn thêm tiền tố `ROLE_` (thành `ROLE_ADMIN`, `ROLE_USER`). Trong `SecurityConfig`, các API được chặn bằng `.hasRole("ADMIN")` sẽ đối chiếu với các quyền này trong `SecurityContextHolder`.

### Câu 14: Đoạn code `.headers(headers -> headers.frameOptions(frame -> frame.disable()))` trong `SecurityConfig` giải quyết vấn đề gì?
- **Trả lời**: Mặc định Spring Security bật cờ `X-Frame-Options: DENY` để chống tấn công Clickjacking. Tuy nhiên giao diện web H2 Console (`/h2-console`) sử dụng thẻ `<iframe>` để chia khung màn hình. Dòng code trên tắt `frameOptions` để trình duyệt cho phép hiển thị H2 Console bình thường.

### Câu 15: Token hết hạn (Expired) thì hệ thống xử lý như thế nào?
- **Trả lời**: Khi token hết hạn (quá 1 giờ), bộ giải mã `jwtDecoder()` sẽ phát hiện trường `expirationTime` nhỏ hơn thời điểm hiện tại và ném lỗi xác thực. Phía Frontend, hàm `callApi()` bắt mã lỗi `401/403` và hiển thị Toast: `"Phiên đăng nhập hết hạn hoặc không có quyền!"`, đồng thời người dùng sẽ được yêu cầu đăng nhập lại.

### Câu 16: Phương thức `introspect()` trong `AuthenticationService` dùng để làm gì?
- **Trả lời**: Dùng để cho Client kiểm tra nhanh xem một chuỗi token có còn hợp lệ hay không (chữ ký số có bị sửa đổi không và đã hết hạn chưa) mà không cần phải thực hiện một hành động nghiệp vụ cụ thể nào.

### Câu 17: Phân biệt sự khác nhau giữa Xác thực (Authentication) và Phân quyền (Authorization)?
- **Trả lời**:
  - **Authentication (Xác thực)**: Trả lời câu hỏi "Bạn là ai?" (Kiểm tra username và mật khẩu để cấp danh tính Token).
  - **Authorization (Phân quyền)**: Trả lời câu hỏi "Bạn có quyền làm gì?" (Kiểm tra xem user đó có quyền ADMIN để xóa danh mục hoặc xem dashboard hay không).

### Câu 18: CORS là gì và tại sao cần cấu hình `CorsConfig`?
- **Trả lời**: CORS (Cross-Origin Resource Sharing) là cơ chế bảo mật của trình duyệt ngăn chặn một trang web ở tên miền này gọi API sang tên miền khác. Việc cấu hình CORS cho phép các Client ở cổng khác (ví dụ cổng 3000 của React hay file HTML mở trực tiếp) có thể gửi request đến server Spring Boot ở cổng 8080 an toàn.

---

## PHẦN 3: HIBERNATE, JPA & CƠ SỞ DỮ LIỆU H2 (CÂU 19 - 28)

### Câu 19: JPA và Hibernate có mối quan hệ gì với nhau?
- **Trả lời**: JPA (Java Persistence API) chỉ là một tập hợp các **giao diện và đặc tả tiêu chuẩn (Specification / Interface)** của Java. Còn **Hibernate là lớp triển khai thực tế (Implementation)** cụ thể của chuẩn JPA đó, chịu trách nhiệm trực tiếp sinh câu lệnh SQL và quản lý kết nối CSDL.

### Câu 20: Kỹ thuật ORM (Object-Relational Mapping) là gì?
- **Trả lời**: Là kỹ thuật ánh xạ các bảng (tables) trong cơ sở dữ liệu quan hệ thành các lớp đối tượng (classes) trong ngôn ngữ hướng đối tượng Java. Mỗi dòng dữ liệu tương ứng với một thực thể đối tượng, giúp lập trình viên thao tác với dữ liệu hoàn toàn bằng tư duy hướng đối tượng mà không cần viết câu lệnh SQL thủ công.

### Câu 21: Phân biệt sự khác nhau giữa các giá trị của `hibernate.ddl-auto` (`update`, `create`, `create-drop`, `none`)?
- **Trả lời**:
  - `create`: Xóa sạch bảng cũ và tạo lại bảng mới mỗi khi chạy ứng dụng (Mất toàn bộ dữ liệu).
  - `create-drop`: Tạo bảng khi chạy và tự động xóa sạch bảng khi tắt server.
  - `update`: Kiểm tra và tự động cập nhật thêm cột/bảng mới nếu chưa có, giữ nguyên dữ liệu cũ đang có trong bảng (Dự án nhóm em đang dùng chế độ này).
  - `none` / `validate`: Không can thiệp vào cấu trúc bảng, chỉ kiểm tra xem bảng trong DB có khớp với Entity Java không.

### Câu 22: Phân biệt `FetchType.LAZY` và `FetchType.EAGER`?
- **Trả lời**:
  - `LAZY`: Nạp lười - dữ liệu của bảng liên kết chỉ được tải từ DB khi nào ta gọi hàm getter trên nó (tiết kiệm bộ nhớ).
  - `EAGER`: Nạp ngay lập tức - Hibernate sẽ tự động JOIN bảng liên quan và lấy lên cùng lúc ngay từ câu truy vấn ban đầu.

### Câu 23: Lỗi kinh điển `LazyInitializationException` xảy ra khi nào và cách khắc phục?
- **Trả lời**: Xảy ra khi ta truy cập vào một thuộc tính liên kết được cấu hình `LAZY` sau khi phiên làm việc của Hibernate (Hibernate Session) đã bị đóng. Cách khắc phục: Sử dụng `@Transactional` ở tầng Service để giữ Session mở trong suốt quá trình xử lý, hoặc dùng câu truy vấn `JOIN FETCH` trong Repository.

### Câu 24: Tại sao trong bảng `Comment` nhóm lại sử dụng quan hệ tự tham chiếu (Self-Referencing Entity)?
- **Trả lời**: Vì để phục vụ tính năng trả lời bình luận (Reply Comment). Một bình luận con cần trỏ ngược lại bình luận cha thông qua cột `parent_id`. Việc dùng thực thể tự tham chiếu giúp lưu trữ cấu trúc cây bình luận nhiều tầng ngay trong cùng một bảng `comments`.

### Câu 25: Phân biệt sự khác nhau giữa `@OneToMany` và `@ManyToMany`?
- **Trả lời**:
  - `@OneToMany`: Một thực thể cha có nhiều thực thể con (Ví dụ: 1 Category có nhiều Blog, 1 User có nhiều Blog).
  - `@ManyToMany`: Nhiều thực thể này liên kết với nhiều thực thể khác (Ví dụ: 1 Blog có nhiều Tag và 1 Tag có thể gắn vào nhiều Blog). Bắt buộc phải có một bảng trung gian (`blog_tags`).

### Câu 26: Annotation `@JoinTable` dùng để làm gì?
- **Trả lời**: Dùng để cấu hình tên bảng trung gian (`name = "blog_tags"`), tên cột khóa ngoại trỏ về bảng hiện tại (`joinColumns`) và cột khóa ngoại trỏ về bảng đích (`inverseJoinColumns`) trong mối quan hệ `@ManyToMany`.

### Câu 27: Phân biệt `CascadeType.REMOVE` và `@OnDelete(action = OnDeleteAction.CASCADE)`?
- **Trả lời**:
  - `CascadeType.REMOVE`: Do Hibernate quản lý ở mức ứng dụng. Nó phải SELECT dữ liệu con lên RAM rồi mới DELETE từng dòng (chậm).
  - `@OnDelete(action = OnDeleteAction.CASCADE)`: Sinh trực tiếp ràng buộc khóa ngoại `ON DELETE CASCADE` ở mức CSDL. Khi xóa cha, CSDL tự động xóa toàn bộ con với tốc độ phần cứng cực nhanh.

### Câu 28: Khóa chính dạng UUID có ưu thế gì trong hệ thống mạng xã hội Blog?
- **Trả lời**: UUID đảm bảo tính độc nhất trên toàn cầu, không thể đoán trước được ID của bài viết hoặc người dùng tiếp theo, chống lại các cuộc tấn công quét ID tuần tự (ID Enumeration Attacks) và tối ưu khi mở rộng dữ liệu phân tán.

---

## PHẦN 4: RESTFUL API, CONTROLLER & XỬ LÝ NGOẠI LỆ (CÂU 29 - 36)

### Câu 29: RESTful API là gì và 4 phương thức HTTP chính là gì?
- **Trả lời**: REST là chuẩn kiến trúc trao đổi dữ liệu qua giao thức HTTP không trạng thái. 4 phương thức tương ứng với CRUD:
  - `GET`: Đọc/Lấy dữ liệu.
  - `POST`: Tạo mới dữ liệu.
  - `PUT`: Cập nhật/Sửa dữ liệu đã có.
  - `DELETE`: Xóa dữ liệu.

### Câu 30: Phân biệt `@PathVariable` và `@RequestParam`?
- **Trả lời**:
  - `@PathVariable`: Trích xuất biến nằm trực tiếp trên đường dẫn URL (Ví dụ: `/blogs/{id}`).
  - `@RequestParam`: Trích xuất tham số truy vấn nằm sau dấu `?` dùng để lọc hoặc tìm kiếm (Ví dụ: `/blogs/search?keyword=java`).

### Câu 31: Annotation `@RequestBody` dùng để làm gì?
- **Trả lời**: Báo cho Spring Boot biết lấy chuỗi JSON trong phần thân của HTTP Request (Body) và tự động chuyển đổi (deserialize) thành đối tượng Java tương ứng thông qua thư viện Jackson.

### Câu 32: Cơ chế `@ControllerAdvice` hoạt động như thế nào trong `GlobalExceptionHandler`?
- **Trả lời**: `@ControllerAdvice` là một bộ lắng nghe toàn cục dựa trên Spring AOP. Mọi ngoại lệ xảy ra tại bất kỳ Controller nào sẽ được chuyển tiếp về đây, các phương thức đánh dấu `@ExceptionHandler` sẽ bắt lỗi tương ứng và chuẩn hóa thành phản hồi JSON thân thiện gửi về cho người dùng.

### Câu 33: Mã trạng thái HTTP (HTTP Status Code) gồm những nhóm nào?
- **Trả lời**:
  - `2xx` (Success): Thành công (200 OK, 201 Created).
  - `3xx` (Redirection): Chuyển hướng.
  - `4xx` (Client Error): Lỗi do người dùng gửi sai (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found).
  - `5xx` (Server Error): Lỗi sập máy chủ nội bộ (500 Internal Server Error).

### Câu 34: Tại sao trong `GlobalExceptionHandler` lại có phương thức bắt `MethodArgumentNotValidException`?
- **Trả lời**: Khi dữ liệu gửi lên vi phạm các ràng buộc validate của DTO (như `@Size`, `@NotBlank`), Spring tự động ném ra ngoại lệ này. Phương thức trên sẽ bắt lấy và trích xuất đúng mã lỗi enum đã định nghĩa để báo cho Client biết chính xác trường nào bị sai.

### Câu 35: Lớp `ApiResponse<T>` mang lại lợi ích gì cho việc phát triển phần mềm?
- **Trả lời**: Tạo ra một cấu trúc JSON đồng nhất cho 100% các API của toàn bộ dự án (`code`, `message`, `result`). Lập trình viên Frontend chỉ cần viết một hàm xử lý kết quả duy nhất dựa trên trường `code === 1000`.

### Câu 36: Tại sao phương thức `@GetMapping("/my-profile")` phải đặt trước `@GetMapping("/{userId}")`?
- **Trả lời**: Vì nếu đặt ngược lại, Spring MVC sẽ nhận chuỗi tĩnh `"my-profile"` làm giá trị của biến `{userId}` và cố gắng ép thành kiểu `UUID`, dẫn đến lỗi văng ngoại lệ `MethodArgumentTypeMismatchException` làm sập API.

---

## PHẦN 5: TƯƠNG TÁC MẠNG XÃ HỘI & CLOUDINARY (CÂU 37 - 44)

### Câu 37: Trình bày quy trình upload ảnh lên Cloudinary trong dự án?
- **Trả lời**:
  1. Client gửi file qua `POST /upload/image` dạng `MultipartFile`.
  2. `CloudinaryService` chuyển file thành mảng byte và gọi `cloudinary.uploader().upload()`.
  3. Cloudinary lưu ảnh và trả về link URL HTTPS công khai.
  4. Server trả link này về cho Client để chèn vào bài viết hoặc avatar.

### Câu 38: Cơ chế Toggle Like / Toggle Bookmark hoạt động như thế nào?
- **Trả lời**: Khi người dùng gọi API, hệ thống truy vấn CSDL: nếu bản ghi like/bookmark đã tồn tại với cặp `(blog_id, user_id)` thì xóa đi (Unlike/Bỏ lưu). Nếu chưa có thì tạo mới bản ghi (Like/Lưu). Cơ chế này gom 2 hành vi vào 1 API duy nhất rất tiện lợi.

### Câu 39: Làm sao hệ thống đảm bảo một người không thể Like một bài viết 2 lần?
- **Trả lời**: Bằng ràng buộc `@UniqueConstraint(columnNames = {"user_id", "blog_id"})` ở tầng CSDL của thực thể `BlogLike`.

### Câu 40: Khi nào thì một Thông báo (Notification) được tạo ra?
- **Trả lời**: Khi có các sự kiện: Một người dùng khác Like bài viết của tôi, Bình luận vào bài viết của tôi, Trả lời bình luận của tôi, hoặc Bấm theo dõi tôi. Hệ thống sẽ tự động bỏ qua nếu người thực hiện hành động chính là tác giả bài viết.

### Câu 41: Hệ thống ghi nhận Lượt xem bài viết (View Counter) như thế nào?
- **Trả lời**: Mỗi khi API `GET /blogs/{id}` được gọi để đọc bài viết, một bản ghi `BlogView` được lưu vào CSDL. Người dùng đã đăng nhập sẽ lưu kèm `user_id`, khách vãng lai sẽ lưu kèm địa chỉ IP của máy khách.

### Câu 42: Tại sao người dùng không thể tự Follow chính mình?
- **Trả lời**: Trong hàm `FollowService.toggleFollow()`, hệ thống kiểm tra điều kiện `if (currentUsername.equals(targetUsername))` và chặn lại ngay từ đầu bằng ngoại lệ để đảm bảo tính logic của mạng xã hội.

### Câu 43: Luồng Lưu nháp (Draft) và Xuất bản (Publish) khác nhau như thế nào trong `BlogService`?
- **Trả lời**:
  - Lưu nháp bài đã xuất bản: Nội dung mới được lưu vào `draftContent`, cột `content` công khai được giữ nguyên để độc giả không bị gián đoạn.
  - Xuất bản: Nội dung được đổ vào `content`, làm rỗng cột `draftContent`, đặt cờ `draft = false` và cập nhật ngày xuất bản `publishedAt`.

### Câu 44: Ai có quyền xóa bài viết trong hệ thống?
- **Trả lời**: Trong hàm `deleteBlog()`, chỉ có **Tác giả của bài viết** (người tạo ra bài đó) HOẶC người dùng có quyền **Quản trị viên (ROLE_ADMIN)** mới được phép xóa bài.

---

## PHẦN 6: FRONTEND VANILLA JS & TỐI ƯU HIỆU NĂNG (CÂU 45 - 50)

### Câu 45: Hàm `callApi()` trong `app.js` giải quyết bài toán gì?
- **Trả lời**: Đóng vai trò là cổng API trung tâm phía Client, tự động đọc JWT token từ `localStorage` và gắn vào header `Authorization: Bearer <token>`, đồng thời tự động bắt các lỗi 401/403 để hiện thông báo Toast nhắc nhở người dùng.

### Câu 46: Giải thuật tính Thời gian đọc bài viết (Reading Time) dựa trên cơ sở nào?
- **Trả lời**: Dựa trên chuẩn tốc độ đọc của con người trung bình là 200 từ/phút:
  `Reading Time = Math.ceil(Tổng số từ / 200)`.

### Câu 47: Kỹ thuật `window.history.pushState()` trong bộ lọc bài viết mang lại lợi ích gì?
- **Trả lời**: Cho phép cập nhật tham số trên thanh URL của trình duyệt (ví dụ: `/?q=spring&cat=...`) khi người dùng tìm kiếm hoặc lọc danh mục mà **không làm tải lại (reload) trang web**, giúp trải nghiệm người dùng siêu mượt mà chuẩn Single-Page Application (SPA).

### Câu 48: Làm sao Frontend hiển thị được Avatar chữ cái đầu khi người dùng chưa có ảnh đại diện?
- **Trả lời**: Nhờ hàm `initials(name)` trong `auth.js`, nó bóc tách chữ cái đầu tiên của từ đầu và từ cuối trong họ tên (ví dụ "Hoàng Đại Dương" -> "HD") và in vào thẻ avatar tròn với nền màu tối sang trọng.

### Câu 49: Làm sao Frontend biết được một tài khoản có quyền ADMIN để hiển thị nút Admin Dashboard?
- **Trả lời**: Hàm `updateNavAuth()` trong `nav.js` mổ xẻ chuỗi JWT Token, lấy phần Payload ở giữa giải mã Base64 sang JSON và đọc thuộc tính `scope`. Nếu chuỗi chứa `"ADMIN"`, nút bấm Admin Dashboard sẽ tự động xuất hiện.

### Câu 50: Vấn đề N+1 Queries trong việc hiển thị danh sách bài viết được nhóm giải quyết như thế nào?
- **Trả lời**: Thay vì lặp qua từng bài viết để đếm số lượt like, view, comment (khiến database phải chạy N+1 câu lệnh), nhóm em sử dụng câu truy vấn tối ưu `@Query` với `LEFT JOIN` và `COUNT(DISTINCT ...)` trong `BlogRepository`. Nhờ đó chỉ cần **DUY NHẤT 1 câu lệnh SQL** là lấy được toàn bộ danh sách bài viết kèm 3 con số thống kê đếm phân biệt!
