# HƯỚNG DẪN ĐÓNG GÓI BUILD JAR & TRIỂN KHAI ỨNG DỤNG (DEPLOYMENT)

> **Mục đích:** Hướng dẫn từng bước từ việc biên dịch mã nguồn Java thành gói thực thi độc lập `.jar`, chạy ứng dụng trên môi trường Production, tách biệt cấu hình môi trường (Profiles), chuyển đổi sang CSDL MySQL thực tế và triển khai lên máy chủ đám mây (Cloud).

---

## 1. Cơ Chế Đóng Gói Ứng Dụng Độc Lập Của Spring Boot (Fat JAR / Uber JAR)

Trong kiến trúc Java truyền thống (Java EE), lập trình viên phải đóng gói thành file `.war` và cài đặt một Web Server riêng bên ngoài (như Tomcat, JBoss, WebLogic).  
Với **Spring Boot**, ứng dụng được đóng gói thành một file **Executable JAR (Fat JAR)** duy nhất. File này đã nhúng sẵn:
- Toàn bộ mã nguồn bytecode (`.class`) đã biên dịch.
- Toàn bộ thư viện phụ thuộc (`pom.xml`).
- Toàn bộ giao diện tĩnh (`static/`, `templates/`, HTML, CSS, JS).
- Một máy chủ **Tomcat Server nhúng** bên trong.

---

## 2. Quy Trình Đóng Gói Bằng Maven (Build JAR)

Mở cửa sổ dòng lệnh Terminal tại thư mục gốc của dự án `blog-website-main`:

```bash
# 1. Dọn dẹp các bản build cũ và biên dịch đóng gói sản phẩm mới
./mvnw clean package -DskipTests
```
*(Trên Windows PowerShell, nếu dùng Maven hệ thống thì gõ: `mvn clean package -DskipTests`)*

### Ý nghĩa các tham số lệnh:
* **`clean`**: Xóa sạch thư mục `target/` cũ để đảm bảo không bị dính file rác hoặc cache lỗi thời.
* **`package`**: Kích hoạt plugin `spring-boot-maven-plugin` để nén toàn bộ thành file `.jar`.
* **`-DskipTests`**: Tạm thời bỏ qua bước chạy test tự động trong lúc đóng gói để quá trình build diễn ra nhanh chóng (khoảng 15-30 giây).

Sau khi lệnh kết thúc thành công (`BUILD SUCCESS`), file kết quả sẽ nằm tại:
📁 **`target/blog-website-0.0.1-SNAPSHOT.jar`**

---

## 3. Khởi Chạy Ứng Dụng Trên Môi Trường Production

Bất kỳ máy chủ nào chỉ cần cài đặt **JRE hoặc JDK 21+** là có thể chạy ngay website mà không cần cài đặt phần mềm nào khác:

```bash
java -jar target/blog-website-0.0.1-SNAPSHOT.jar
```

### Chạy ứng dụng ngầm trên máy chủ Linux/VPS (Background Service):
```bash
nohup java -jar target/blog-website-0.0.1-SNAPSHOT.jar > app.log 2>&1 &
```
* **`nohup`**: Giúp ứng dụng tiếp tục chạy kể cả khi quản trị viên tắt cửa sổ SSH.
* **`> app.log 2>&1`**: Ghi toàn bộ nhật ký console vào file `app.log` để tiện theo dõi.

---

## 4. Quản Lý Đa Môi Trường Bằng Spring Profiles (Dev vs Prod)

Để không phải sửa code thủ công khi chuyển từ máy cá nhân lên máy chủ thực tế, dự án hỗ trợ tách cấu hình:

### 4.1. Cấu hình Development (`application-dev.yaml`)
Dùng H2 Database trong bộ nhớ, tự động seed tài khoản mẫu, bật H2 Web Console để sinh viên dễ dàng demo và làm bài tập lớn.

### 4.2. Cấu hình Production (`application-prod.yaml`)
Kết nối CSDL MySQL / PostgreSQL thật trên Cloud:

```yaml
server:
  port: 8080

spring:
  datasource:
    url: jdbc:mysql://${DB_HOST:localhost}:3306/${DB_NAME:blogdb}?useSSL=true&serverTimezone=UTC
    username: ${DB_USER:root}
    password: ${DB_PASS:secret}
    driver-class-name: com.mysql.cj.jdbc.Driver
  jpa:
    hibernate:
      ddl-auto: update
    show-sql: false # Tắt log câu lệnh SQL trên production để tăng hiệu năng tối đa
```

### Kích hoạt Profile khi chạy:
```bash
java -jar target/blog-website-0.0.1-SNAPSHOT.jar --spring.profiles.active=prod
```

---

## 5. Bảo Mật Khóa Bí Mật Bằng Biến Môi Trường (Environment Variables)

Tuyệt đối **không bao giờ để lộ API Key thật lên GitHub công khai**. Thay vào đó, truyền giá trị qua biến môi trường:

```bash
# Thiết lập biến môi trường trước khi chạy ứng dụng
export CLOUDINARY_CLOUD_NAME=fu18kpep
export CLOUDINARY_API_KEY=616397886535446
export CLOUDINARY_API_SECRET=qyvdA2-sFh0sypZG3sTzhe7e5cA
export JWT_SIGNER_KEY=DayLaChuoiBiMatSieuCapBaoMatJwtSignerKeyChoDuAnBlogWebsite2026

java -jar target/blog-website-0.0.1-SNAPSHOT.jar
```

Trong file `application.yaml`, Spring Boot sẽ tự động map biến môi trường vào các thuộc tính cấu hình nhờ cú pháp:  
`${CLOUDINARY_CLOUD_NAME:fu18kpep}`.

---

## 6. Câu Hỏi Vấn Đáp Giảng Viên Hay Hỏi Về Đóng Gói & Triển Khai

### ❓ Câu 1: Em hãy giải thích sự khác biệt giữa việc chạy dự án bằng nút "Run" trên IntelliJ IDEA và chạy bằng file `.jar`?
> **Trả lời:**
> - Khi bấm **Run trên IntelliJ**: IDE biên dịch mã nguồn vào thư mục `target/classes` và dùng classpath mở để chạy. Cách này thuận tiện cho việc debug và viết code hàng ngày.
> - Khi đóng gói ra **File `.jar` (Fat JAR)**: Toàn bộ mã nguồn, thư viện bên thứ 3 và máy chủ nhúng Tomcat được nén lại thành một tập tin thực thi duy nhất. File này hoàn toàn độc lập, có thể mang sang bất kỳ máy tính hay server nào (Windows, Linux, Docker, AWS) để chạy ngay chỉ với 1 câu lệnh `java -jar`.

### ❓ Câu 2: Nếu muốn đưa website này lên mạng Internet công cộng để mọi người cùng truy cập, em sẽ làm những gì?
> **Trả lời:**
> 1. Đóng gói ứng dụng thành file `.jar` hoặc tạo một file `Dockerfile`.
> 2. Đưa mã nguồn lên GitHub.
> 3. Sử dụng dịch vụ PaaS như **Render** hoặc **Railway** để liên kết với kho lưu trữ GitHub và tự động build ứng dụng.
> 4. Thiết lập một CSDL **MySQL Cloud** (như Aiven hoặc Railway MySQL).
> 5. Cài đặt các biến môi trường cấu hình (`DB_URL`, `DB_USER`, `DB_PASSWORD`, `CLOUDINARY_API_KEY`).
> 6. Trỏ tên miền (Domain) về địa chỉ IP hoặc đường dẫn của máy chủ Render.

### ❓ Câu 3: Khi khởi động ứng dụng trên máy chủ thật, tại sao hình ảnh bài viết không bị mất kể cả khi server khởi động lại?
> **Trả lời:** Nhờ giải pháp lưu trữ hình ảnh trên đám mây **Cloudinary Media Cloud**. Hình ảnh không hề được lưu trong ổ cứng tạm của máy chủ (local storage), mà được upload thẳng lên hệ thống lưu trữ phân tán toàn cầu của Cloudinary qua API HTTPS. Khi ứng dụng khởi động lại, các bài viết trong CSDL chỉ lưu giữ đường link URL cố định (`https://res.cloudinary.com/...`), do đó hình ảnh luôn hiển thị nguyên vẹn 100%.
