# GIẢI THÍCH CHI TIẾT TỪNG DÒNG FILE APPLICATION.YAML VÀ APPLICATION-SECRET.YML

> **Mục tiêu**: Hiểu cặn kẽ mọi thông số cấu hình của ứng dụng: từ cổng kết nối, chuỗi kết nối cơ sở dữ liệu H2 Database (tại sao dùng các cờ đặc biệt), cấu hình Hibernate, bảo mật JWT, dung lượng upload ảnh và tích hợp Cloudinary API.

---

## 1. FILE `src/main/resources/application.yaml`

Toàn bộ nội dung file gốc trong dự án:

```yaml
server:
  port: 8080
  tomcat:
    max-http-form-post-size: 10MB

spring:
  datasource:
    url: jdbc:h2:file:./data/blogdb;AUTO_SERVER=TRUE;DB_CLOSE_DELAY=-1;MODE=MySQL;DATABASE_TO_LOWER=TRUE;CASE_INSENSITIVE_IDENTIFIERS=TRUE
    driverClassName: org.h2.Driver
    username: sa
    password: ""
  h2:
    console:
      enabled: true
      path: /h2-console
  jpa:
    database-platform: org.hibernate.dialect.H2Dialect
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

### Nhóm 2: Cấu hình Kết nối Cơ sở dữ liệu H2 Database
```yaml
spring:
  datasource:
    url: jdbc:h2:file:./data/blogdb;AUTO_SERVER=TRUE;DB_CLOSE_DELAY=-1;MODE=MySQL;DATABASE_TO_LOWER=TRUE;CASE_INSENSITIVE_IDENTIFIERS=TRUE
    driverClassName: org.h2.Driver
    username: sa
    password: ""
```
- **`driverClassName: org.h2.Driver`**: Lớp Java chịu trách nhiệm làm cầu nối điều khiển cơ sở dữ liệu H2.
- **`username: sa`** và **`password: ""`**: Tài khoản quản trị mặc định của H2 là `sa` (System Administrator), mật khẩu để trống.
- **Chuỗi kết nối `url: jdbc:h2:file:./data/blogdb;...`** là phần tinh hoa nhất, giải thích từng cờ (flags):
  1. **`file:./data/blogdb`**: Cấu hình lưu trữ dữ liệu bền vững thành file vật lý tại thư mục `./data/blogdb.mv.db`. Khác hoàn toàn với chế độ in-memory thuần túy (`mem:testdb` sẽ bị mất sạch dữ liệu khi tắt server), chế độ file này đảm bảo khi tắt máy tính hoặc khởi động lại ứng dụng thì toàn bộ tài khoản, bài viết, comment vẫn được bảo toàn nguyên vẹn 100%!
  2. **`AUTO_SERVER=TRUE`**: Cho phép chế độ đa tiến trình (Multi-process). Nhờ cờ này, cả ứng dụng Spring Boot và giao diện web H2 Console (hoặc một tool bên ngoài như DBeaver) có thể cùng lúc truy cập vào file database mà không bị lỗi tranh chấp khóa file (`Database already open`).
  3. **`DB_CLOSE_DELAY=-1`**: Giữ cho cơ sở dữ liệu luôn duy trì trạng thái hoạt động chừng nào máy ảo JVM còn chạy, không bị tự động ngắt kết nối khi hết phiên.
  4. **`MODE=MySQL`**: Ép H2 hoạt động ở chế độ tương thích hoàn toàn với hệ quản trị CSDL MySQL (từ cú pháp SQL, hàm ngày giờ, kiểu dữ liệu chuỗi). Nhờ đó, nếu sau này muốn chuyển sang MySQL Server thật, code không cần sửa một dòng nào!
  5. **`DATABASE_TO_LOWER=TRUE`** & **`CASE_INSENSITIVE_IDENTIFIERS=TRUE`**: Không phân biệt chữ hoa, chữ thường cho tên bảng và tên cột, loại bỏ hoàn toàn các lỗi xung đột tên bảng giữa môi trường Windows và Linux.

---

### Nhóm 3: Cấu hình Giao diện Quản trị CSDL (H2 Web Console)
```yaml
  h2:
    console:
      enabled: true
      path: /h2-console
```
- **`enabled: true`**: Kích hoạt giao diện đồ họa quản trị CSDL tích hợp sẵn của H2.
- **`path: /h2-console`**: Đường dẫn URL để truy cập vào trang quản trị cơ sở dữ liệu ngay trên trình duyệt: `http://localhost:8080/h2-console`. Giảng viên có thể vào đây để kiểm tra trực tiếp các bảng `USERS`, `BLOGS`, `COMMENTS` xem dữ liệu được lưu như thế nào.

---

### Nhóm 4: Cấu hình Hibernate & JPA (Java Persistence API)
```yaml
  jpa:
    database-platform: org.hibernate.dialect.H2Dialect
    hibernate:
      ddl-auto: update
    show-sql: true
    properties:
      hibernate:
        format_sql: true
```
- **`database-platform: org.hibernate.dialect.H2Dialect`**: Khai báo ngôn ngữ thổ ngữ (Dialect) của Hibernate là H2. Hibernate sẽ tự động dịch các phương thức Java thành các câu lệnh SQL tối ưu riêng cho H2 Database.
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

### Câu 1: Tại sao nhóm lại sử dụng H2 Database ở chế độ File (`file:./data/blogdb`) thay vì In-Memory (`mem:`) hay cài đặt MySQL trực tiếp?
- **Trả lời**:
  > "Thưa thầy/cô:
  > - Nếu dùng chế độ in-memory thuần túy (`mem:`), mỗi lần dừng ứng dụng thì toàn bộ tài khoản do người dùng đăng ký và các bài viết mới tạo sẽ biến mất hoàn toàn.
  > - Do đó, nhóm em cấu hình chế độ File (`file:./data/blogdb`). H2 sẽ lưu toàn bộ dữ liệu vào file vật lý `blogdb.mv.db`. Dữ liệu sẽ tồn tại vĩnh viễn qua các lần chạy.
  > - Đồng thời, việc dùng H2 kèm cờ `MODE=MySQL` mang lại 2 ưu điểm vượt trội: Thứ nhất, thầy cô và các bạn sinh viên khác khi tải code về máy chỉ cần bấm Run là chạy ngay mà không cần tốn thời gian cài MySQL Server, tạo Database hay sợ sai lệch mật khẩu `root`. Thứ hai, cú pháp và kiểu dữ liệu hoàn toàn tương thích với MySQL nên hệ thống có thể chuyển đổi sang MySQL thật chỉ bằng việc đổi chuỗi kết nối trong 1 nốt nhạc."

### Câu 2: Em hãy giải thích cờ `AUTO_SERVER=TRUE` trong chuỗi JDBC URL của H2 có tác dụng gì? Nếu bỏ cờ này thì chuyện gì xảy ra?
- **Trả lời**:
  > "Thưa thầy/cô, mặc định một file cơ sở dữ liệu H2 chỉ cho phép duy nhất MỘT tiến trình được mở tại một thời điểm (Exclusive Lock). 
  > Nếu không có cờ `AUTO_SERVER=TRUE`, khi ứng dụng Spring Boot đang chạy và chiếm giữ file `blogdb.mv.db`, nếu chúng em mở thêm trình duyệt vào `http://localhost:8080/h2-console` để xem bảng thì H2 sẽ báo lỗi nghiêm trọng: `Database may be already in use: Locked by another process`.
  > Nhờ có cờ `AUTO_SERVER=TRUE`, H2 sẽ tự động khởi động một máy chủ ngầm nội bộ, cho phép cả Spring Boot và H2 Web Console cùng chia sẻ quyền đọc ghi đồng thời một cách an toàn."
