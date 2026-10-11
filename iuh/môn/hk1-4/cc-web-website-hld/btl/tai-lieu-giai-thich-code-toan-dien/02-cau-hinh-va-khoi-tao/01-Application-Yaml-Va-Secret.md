# GIẢI THÍCH CHI TIẾT TỪNG DÒNG FILE APPLICATION.YAML VÀ APPLICATION-SECRET.YML

> **Mục tiêu**: Hiểu cặn kẽ mọi thông số cấu hình của ứng dụng: từ cổng kết nối, chuỗi kết nối cơ sở dữ liệu MySQL Server Local (tại sao dùng các tham số JDBC đặc thù), cấu hình Hibernate MySQLDialect, bảo mật JWT, dung lượng upload ảnh và tích hợp Cloudinary API.

---

## 1. FILE `src/main/resources/application.yaml`

Toàn bộ nội dung file trong dự án:

```yaml
server:
  port: 8080
  tomcat:
    max-http-form-post-size: 10MB

spring:
  datasource:
    url: jdbc:mysql://localhost:3306/blog_website_db?createDatabaseIfNotExist=true&useSSL=false&serverTimezone=UTC&allowPublicKeyRetrieval=true&characterEncoding=UTF-8
    driverClassName: com.mysql.cj.jdbc.Driver
    username: root
    password: root
  jpa:
    database-platform: org.hibernate.dialect.MySQLDialect
    hibernate:
      ddl-auto: update
    show-sql: true
    properties:
      hibernate:
        format_sql: true
  application:
    name: blog-website
  thymeleaf:
    prefix: classpath:/templates/
    suffix: .html
    cache: false
    web:
      resources:
        static-locations: classpath:/static/
  servlet:
    multipart:
      max-request-size: 10MB
  profiles:
    active: secret
jwt:
  signerKey: "b61be1b79d764b64a74332525cc9d1100c44011194a31cb568a3a297a990b406"
```

---

## 2. GIẢI THÍCH CHI TIẾT TỪNG DÒNG CẤU HÌNH TRONG `application.yaml`

### Nhóm 1: Cấu hình Máy chủ Web (Server & Tomcat)
```yaml
server:
  port: 8080
  tomcat:
    max-http-form-post-size: 10MB
```
- **`server.port: 8080`**: Chỉ định cổng mạng (network port) mà ứng dụng Spring Boot sẽ lắng nghe. Khi mở trình duyệt, người dùng truy cập địa chỉ `http://localhost:8080`. Nếu máy tính đang bị trùng cổng 8080 do ứng dụng khác chiếm giữ, ta chỉ cần đổi số này sang `8081` hoặc `8888`.
- **`server.tomcat.max-http-form-post-size: 10MB`**: Giới hạn kích thước tối đa của dữ liệu dạng form POST gửi lên máy chủ Tomcat là 10 Megabyte. Điều này rất quan trọng khi người dùng viết bài blog dài kèm hình ảnh hoặc mã HTML lớn, tránh việc Tomcat từ chối yêu cầu do quá giới hạn mặc định (thường chỉ 2MB).

---

### Nhóm 2: Cấu hình Kết nối Cơ sở dữ liệu MySQL Server Local
```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/blog_website_db?createDatabaseIfNotExist=true&useSSL=false&serverTimezone=UTC&allowPublicKeyRetrieval=true&characterEncoding=UTF-8
    driverClassName: com.mysql.cj.jdbc.Driver
    username: root
    password: root
```
- **`driverClassName: com.mysql.cj.jdbc.Driver`**: Lớp Java Driver chính thức của MySQL Connector/J chịu trách nhiệm làm cầu nối điều khiển cơ sở dữ liệu MySQL.
- **`username: root`** và **`password: root`**: Tài khoản và mật khẩu quản trị của MySQL Server cục bộ.
- **Chuỗi kết nối `url: jdbc:mysql://localhost:3306/blog_website_db?...`** được tối ưu hóa chuẩn mực cho môi trường phát triển cục bộ:
  1. **`localhost:3306/blog_website_db`**: Chỉ định dịch vụ MySQL đang chạy ở cổng mặc định `3306` trên máy tính (`localhost`), trỏ vào cơ sở dữ liệu `blog_website_db`.
  2. **`createDatabaseIfNotExist=true`**: Rất thông minh! Khi ứng dụng khởi động, nếu trong MySQL Server chưa có database `blog_website_db`, driver sẽ tự động tạo mới database mà không cần người dùng phải gõ lệnh SQL tạo database trước bằng tay.
  3. **`useSSL=false`**: Tắt cơ chế mã hóa kết nối SSL. Vì ứng dụng và MySQL chạy trên cùng một máy local, việc tắt SSL giúp tăng tốc độ thiết lập kết nối và tránh lỗi từ chối chứng chỉ số tự ký (self-signed certificate).
  4. **`serverTimezone=UTC`**: Đồng bộ múi giờ quốc tế chuẩn UTC, giúp các trường thời gian như `publishedAt`, `createdAt`, `updatedAt` lưu trữ nhất quán, không bị lỗi lệch múi giờ giữa máy ảo JVM và máy chủ MySQL.
  5. **`allowPublicKeyRetrieval=true`**: Tham số bắt buộc đối với MySQL 8+ sử dụng plugin xác thực `caching_sha2_password`. Nó cho phép JDBC driver lấy khóa công khai từ máy chủ MySQL để mã hóa mật khẩu truyền qua kết nối không có SSL.
  6. **`characterEncoding=UTF-8`**: Đảm bảo toàn bộ chuỗi ký tự gửi và nhận (tiêu đề bài viết, nội dung tiếng Việt có dấu, bình luận) đều được mã hóa chuẩn UTF-8, không bị lỗi font hay dấu hỏi chấm (`???`).

---

### Nhóm 3: Công Cụ Quản Trị Trực Quan (MySQL Workbench)
- Để xem và thao tác trực tiếp với dữ liệu trong `blog_website_db`, nhóm sử dụng phần mềm đồ họa chuyên nghiệp **MySQL Workbench**:
  - **Hostname**: `127.0.0.1` / `localhost`
  - **Port**: `3306`
  - **Username**: `root`
  - **Password**: `root`
- Tại đây, giảng viên có thể xem trực quan 12 bảng đã được Hibernate tự động sinh (`users`, `user_roles`, `blogs`, `categories`, `tags`, `comments`, `blog_likes`, `blog_views`, `bookmarks`, `notifications`, `user_follows`, `blog_tags`) cùng dữ liệu seed ban đầu.

---

### Nhóm 4: Cấu hình Hibernate & JPA (Java Persistence API)
```yaml
  jpa:
    database-platform: org.hibernate.dialect.MySQLDialect
    hibernate:
      ddl-auto: update
    show-sql: true
    properties:
      hibernate:
        format_sql: true
```
- **`database-platform: org.hibernate.dialect.MySQLDialect`**: Khai báo ngôn ngữ thổ ngữ (Dialect) của Hibernate là MySQL. Hibernate sẽ tự động biên dịch các câu lệnh HQL/JPQL và thao tác thực thể thành các câu lệnh SQL tối ưu theo chuẩn cú pháp MySQL 8.
- **`hibernate.ddl-auto: update`**: Cực kỳ thông minh. Mỗi lần khởi động, Hibernate sẽ tự động quét các class Entity (`User.java`, `Blog.java`...) và tự động tạo mới các bảng nếu chưa có, hoặc cập nhật thêm các cột mới mà KHÔNG làm mất dữ liệu cũ đang có trong bảng.
- **`show-sql: true`**: In các câu lệnh SQL mà Spring Data JPA thực thi ngầm ra màn hình Console/Terminal.
- **`properties.hibernate.format_sql: true`**: Định dạng câu lệnh SQL in ra cho đẹp mắt, xuống dòng rõ ràng (indent), giúp nhóm dễ dàng gỡ lỗi (debug) và giải thích luồng truy vấn cho giảng viên xem trực tiếp.

---

### Nhóm 5: Tên ứng dụng, Thymeleaf & Giới hạn tải file (Multipart)
```yaml
  application:
    name: blog-website
  thymeleaf:
    prefix: classpath:/templates/
    suffix: .html
    cache: false
    web:
      resources:
        static-locations: classpath:/static/
  servlet:
    multipart:
      max-request-size: 10MB
```
- **`application.name: blog-website`**: Tên định danh của ứng dụng trong hệ sinh thái Spring.
- **`thymeleaf.prefix: classpath:/templates/`** & **`suffix: .html`**: Khi trong `ViewController` trả về `return "public/home-page"`, Thymeleaf sẽ tự động tìm file tại thư mục `src/main/resources/templates/public/home-page.html`.
- **`thymeleaf.cache: false`**: Tắt bộ nhớ đệm của template. Khi lập trình viên sửa một dòng chữ trong file HTML giao diện, chỉ cần F5 lại trình duyệt là thấy thay đổi ngay lập tức mà không cần khởi động lại server.
- **`static-locations: classpath:/static/`**: Khai báo thư mục chứa file CSS, JS, hình ảnh tĩnh để client truy cập tự do.
- **`servlet.multipart.max-request-size: 10MB`**: Cho phép người dùng upload các file hình ảnh có dung lượng lên đến 10MB.

---

### Nhóm 6: Cấu hình Profile bí mật & Khóa ký số JWT
```yaml
  profiles:
    active: secret
jwt:
  signerKey: "b61be1b79d764b64a74332525cc9d1100c44011194a31cb568a3a297a990b406"
```
- **`profiles.active: secret`**: Kích hoạt profile mang tên `secret`. Khi profile này được bật, Spring Boot sẽ tự động nạp thêm file cấu hình bổ trợ là `application-secret.yml`. Đây là kỹ thuật chuẩn công nghiệp để tách biệt các thông tin nhạy cảm (mật khẩu, API key) ra khỏi file cấu hình chung.
- **`jwt.signerKey`**: Chuỗi khóa bí mật ngẫu nhiên dài 64 ký tự (256-bit entropy) dùng để tạo chữ ký số HMAC-SHA512 cho JWT Token. Chỉ có server nắm giữ khóa này, bất kỳ kẻ gian nào cố ý chỉnh sửa nội dung token phía client đều sẽ bị server phát hiện ngay lập tức vì sai lệch chữ ký số.

---

## 3. FILE `src/main/resources/application-secret.yml`

Toàn bộ nội dung file:

```yaml
cloudinary:
  cloud-name: fu18kpep
  api-key: "616397886535446"
  api-secret: qyvdA2-sFh0sypZG3sTzhe7e5cA
```

### Giải thích các thông số Cloudinary:
- **`cloud-name: fu18kpep`**: Tên không gian lưu trữ đám mây của tài khoản Cloudinary.
- **`api-key: "616397886535446"`**: Mã định danh định tuyến quyền truy cập API.
- **`api-secret: qyvdA2-sFh0sypZG3sTzhe7e5cA`**: Mật mã bí mật dùng để xác thực quyền ghi/xóa tài nguyên media trên Cloudinary.
- **Cơ chế hoạt động**: Lớp `CloudinaryConfig.java` sẽ đọc 3 thông số này thông qua `@Value("${cloudinary....}")` để khởi tạo đối tượng `Cloudinary` Bean. Khi người dùng bấm upload ảnh đại diện hoặc ảnh bìa bài viết, ảnh sẽ được đẩy trực tiếp lên Cloudinary và trả về một đường link URL HTTPS vĩnh viễn (ví dụ: `https://res.cloudinary.com/fu18kpep/image/upload/...`).

---

## 4. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN VỀ CẤU HÌNH & CÂU TRẢ LỜI ĐIỂM 10

### Câu 1: Tại sao nhóm lại sử dụng MySQL Server Local thay vì cơ sở dữ liệu nhúng (In-Memory / SQLite)?
- **Trả lời**:
  > "Thưa thầy/cô:
  > - Các hệ quản trị cơ sở dữ liệu in-memory thuần túy sẽ mất sạch dữ liệu khi tắt máy chủ hoặc gặp sự cố.
  > - MySQL Server là một hệ quản trị cơ sở dữ liệu quan hệ (RDBMS) chuẩn công nghiệp thực tế. Nó đảm bảo tính toàn vẹn dữ liệu nghiêm ngặt theo chuẩn ACID, hỗ trợ cơ chế khóa ngoại và giao dịch đa luồng mạnh mẽ.
  > - Việc kết nối với MySQL Server cục bộ (cổng 3306) kết hợp với công cụ trực quan hóa MySQL Workbench giúp nhóm dễ dàng kiểm tra, phân tích câu lệnh truy vấn SQL thực tế và chuẩn bị sẵn sàng cho môi trường Production của doanh nghiệp."

### Câu 2: Em hãy giải thích cờ `createDatabaseIfNotExist=true` và `allowPublicKeyRetrieval=true` trong chuỗi JDBC URL của MySQL có tác dụng gì?
- **Trả lời**:
  > "Thưa thầy/cô:
  > - Cờ `createDatabaseIfNotExist=true` giúp Spring Boot tự động phát hiện và khởi tạo cơ sở dữ liệu `blog_website_db` trên MySQL Server nếu trên máy chưa tồn tại database này, giúp quá trình triển khai mã nguồn diễn ra hoàn toàn tự động mà không cần chạy file script SQL bằng tay trước.
  > - Cờ `allowPublicKeyRetrieval=true` là cấu hình cần thiết cho chuẩn bảo mật của MySQL 8+. Do MySQL 8 sử dụng thuật toán mã hóa mật khẩu `caching_sha2_password`, khi ứng dụng kết nối ở chế độ không dùng SSL (`useSSL=false`), driver JDBC cần được phép truy xuất khóa công khai của server để mã hóa mật khẩu an toàn trước khi gửi đi."

