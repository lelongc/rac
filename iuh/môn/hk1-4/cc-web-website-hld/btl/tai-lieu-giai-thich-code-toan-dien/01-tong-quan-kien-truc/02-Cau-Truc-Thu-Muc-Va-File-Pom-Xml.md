# GIẢI THÍCH CẤU TRÚC THƯ MỤC VÀ TỪNG DÒNG FILE POM.XML

> **Mục tiêu**: Nắm chắc ý nghĩa từng thư mục trong dự án và hiểu rõ 100% các dòng cấu hình trong file quản lý gói `pom.xml` của Maven để trả lời trôi chảy khi giảng viên chỉ vào bất kỳ dòng nào.

---

## 1. CẤU TRÚC THƯ MỤC DỰ ÁN (PROJECT DIRECTORY STRUCTURE)

Dự án tuân thủ chuẩn cấu trúc thư mục Maven tiêu chuẩn của Spring Boot:

```
blog-website-main/
│
├── pom.xml                                 # File cấu hình Maven (quản lý thư viện, phiên bản Java, plugin build)
│
├── src/
│   ├── main/
│   │   ├── java/com/group/blog/           # Mã nguồn Java chính của ứng dụng
│   │   │   ├── BlogWebsiteApplication.java # Class chứa hàm main() để khởi động toàn bộ ứng dụng Spring Boot
│   │   │   │
│   │   │   ├── config/                     # Chứa các file cấu hình hệ thống
│   │   │   │   ├── ApplicationInitConfig.java # Khởi tạo dữ liệu mẫu khi chạy lần đầu (Seed Data)
│   │   │   │   ├── CloudinaryConfig.java      # Cấu hình kết nối dịch vụ lưu ảnh Cloudinary
│   │   │   │   ├── CorsConfig.java            # Cấu hình chia sẻ tài nguyên nguồn gốc chéo (Cross-Origin)
│   │   │   │   └── SecurityConfig.java        # Cấu hình phân quyền, bộ lọc bảo mật JWT, mã hóa mật khẩu
│   │   │   │
│   │   │   ├── controller/                 # Tầng Controller (REST API tiếp nhận HTTP Request)
│   │   │   │   ├── AdminController.java       # API dành riêng cho quản trị viên (thống kê hệ thống)
│   │   │   │   ├── AuthenticationController.java # API đăng nhập, kiểm tra token, đổi mật khẩu
│   │   │   │   ├── BlogController.java        # API quản lý bài viết (CRUD, tìm kiếm, lọc theo danh mục/tag)
│   │   │   │   ├── CategoryController.java    # API quản lý danh mục bài viết
│   │   │   │   ├── FollowController.java      # API theo dõi/bỏ theo dõi tác giả
│   │   │   │   ├── InteractionController.java # API like bài viết, bookmark bài viết, gửi bình luận
│   │   │   │   ├── NotificationController.java# API quản lý thông báo người dùng
│   │   │   │   ├── TagController.java         # API quản lý thẻ gắn bài viết
│   │   │   │   ├── UploadController.java      # API nhận file ảnh và đẩy lên Cloudinary
│   │   │   │   ├── UserController.java        # API đăng ký tài khoản, cập nhật hồ sơ cá nhân
│   │   │   │   └── ViewController.java        # Điều hướng trang giao diện Thymeleaf (trang chủ, login, v.v.)
│   │   │   │
│   │   │   ├── dto/                        # Data Transfer Objects (Đối tượng truyền tải dữ liệu)
│   │   │   │   ├── request/                   # Hứng dữ liệu từ Client gửi lên Server
│   │   │   │   └── response/                  # Đóng gói dữ liệu từ Server trả về cho Client
│   │   │   │
│   │   │   ├── entity/                     # Các lớp ánh xạ bảng trong Database (ORM Hibernate Entities)
│   │   │   │   ├── Blog.java                  # Bảng lưu bài viết
│   │   │   │   ├── BlogLike.java              # Bảng lưu lượt thích bài viết
│   │   │   │   ├── BlogView.java              # Bảng theo dõi lượt xem bài viết
│   │   │   │   ├── Bookmark.java              # Bảng lưu bài viết đã đánh dấu
│   │   │   │   ├── Category.java              # Bảng danh mục
│   │   │   │   ├── Comment.java               # Bảng bình luận (hỗ trợ phân cấp cha - con)
│   │   │   │   ├── Notification.java          # Bảng thông báo
│   │   │   │   ├── Tag.java                   # Bảng thẻ tag
│   │   │   │   ├── User.java                  # Bảng tài khoản người dùng
│   │   │   │   └── UserFollow.java            # Bảng mối quan hệ người theo dõi (Follower - Following)
│   │   │   │
│   │   │   ├── enums/                      # Các kiểu liệt kê hằng số
│   │   │   │   └── Role.java                  # ADMIN, USER
│   │   │   │
│   │   │   ├── exception/                  # Xử lý lỗi toàn cục
│   │   │   │   ├── AppException.java          # Ngoại lệ tùy biến của ứng dụng
│   │   │   │   ├── ErrorCode.java             # Bộ mã lỗi chuẩn hóa kèm HTTP Status
│   │   │   │   └── GlobalExceptionHandler.java# Bộ bắt lỗi tập trung @RestControllerAdvice
│   │   │   │
│   │   │   ├── mapper/                     # MapStruct - Tự động chuyển đổi giữa Entity và DTO
│   │   │   │   ├── BlogMapper.java
│   │   │   │   ├── CategoryMapper.java
│   │   │   │   └── UserMapper.java
│   │   │   │
│   │   │   ├── repository/                 # Giao tiếp Cơ sở dữ liệu (Spring Data JPA)
│   │   │   │   └── (10 Repository interfaces tương ứng với 10 Entity)
│   │   │   │
│   │   │   ├── service/                    # Tầng nghiệp vụ xử lý logic
│   │   │   │   └── (10 Service classes tương ứng)
│   │   │   │
│   │   │   └── util/                       # Các hàm tiện ích dùng chung
│   │   │       └── SlugUtils.java             # Tạo đường dẫn thân thiện URL từ tiếng Việt có dấu
│   │   │
│   │   └── resources/                      # Tài nguyên cấu hình và giao diện
│   │       ├── application.yaml            # Cấu hình chính (Port, H2 Database, JPA, JWT Key)
│   │       ├── application-secret.yml       # Cấu hình bảo mật Cloudinary (Cloud Name, API Key, Secret)
│   │       ├── static/                     # Tài nguyên tĩnh phía Client
│   │       │   ├── assets/css/main.css        # File định dạng giao diện tổng thể
│   │       │   └── assets/js/                 # Các file JavaScript xử lý logic phía Client
│   │       │       ├── app.js                 # Helper chung, hiển thị thông báo Toast, format ngày giờ
│   │       │       ├── auth.js                # Xử lý Đăng nhập, Đăng ký, Đăng xuất, Đổi mật khẩu
│   │       │       ├── filters.js             # Bộ lọc bài viết theo từ khóa, danh mục, tag
│   │       │       ├── init.js                # Khởi động ứng dụng phía Client, load dữ liệu ban đầu
│   │       │       ├── nav.js                 # Xử lý thanh điều hướng, avatar người dùng, icon thông báo
│   │       │       ├── pages.js               # Logic cho các trang đặc thù (Profile, Admin, Notifications)
│   │       │       ├── posts.js               # Hiển thị danh sách blog, chi tiết bài viết, like, comment
│   │       │       └── sidebar.js             # Đóng/mở sidebar trên giao diện điện thoại (Responsive)
│   │       └── templates/                  # Giao diện HTML của Thymeleaf
│   │           ├── admin/                     # Các trang quản trị (dashboard.html, posts.html, users.html...)
│   │           ├── fragments/                 # Các thành phần giao diện dùng chung (navbar, sidebar, footer)
│   │           └── public/                    # Các trang công khai (home-page, login, register, post...)
│   │
│   └── test/                               # Chứa các bài kiểm thử tự động (Unit Test / Integration Test)
│
└── data/                                   # Thư mục lưu trữ file Cơ sở dữ liệu vật lý H2 (blogdb.mv.db)
```

---

## 2. GIẢI THÍCH CHI TIẾT TỪNG DÒNG TRONG FILE `pom.xml`

File `pom.xml` (Project Object Model) là trái tim quản lý các thư viện và quá trình biên dịch dự án Maven.

### Đoạn 1: Khai báo XML và Parent Framework
```xml
1: <?xml version="1.0" encoding="UTF-8"?>
2: <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
3: 	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
4: 	<modelVersion>4.0.0</modelVersion>
5: 	<parent>
6: 		<groupId>org.springframework.boot</groupId>
7: 		<artifactId>spring-boot-starter-parent</artifactId>
8: 		<version>3.5.11</version>
9: 		<relativePath/> <!-- lookup parent from repository -->
10: 	</parent>
```
- **Dòng 1-4**: Khai báo chuẩn XML và mô hình Maven POM phiên bản 4.0.0.
- **Dòng 5-10**: Khai báo **Parent POM** là `spring-boot-starter-parent` phiên bản `3.5.11`.
  - **Ý nghĩa cực kỳ quan trọng**: Giúp dự án tự động kế thừa toàn bộ cấu hình mặc định của Spring Boot, bao gồm: quản lý phiên bản tương thích giữa hàng trăm thư viện con mà không sợ xung đột, cấu hình sẵn plugin biên dịch cho Java.
  - **Dòng 9 (`<relativePath/>`)**: Báo cho Maven biết tải trực tiếp từ kho lưu trữ trung tâm (Maven Central Repository) chứ không tìm trên máy cục bộ.

### Đoạn 2: Thông tin định danh dự án và Cấu hình môi trường (Properties)
```xml
11: 	<groupId>com.group</groupId>
12: 	<artifactId>blog-website</artifactId>
13: 	<version>0.0.1-SNAPSHOT</version>
14: 	<name>blog-website</name>
15: 	<description>Group blog website project using Spring Boot</description>
...
29: 	<properties>
30: 		<java.version>21</java.version>
31: 		<maven.compiler.source>21</maven.compiler.source>
32: 		<maven.compiler.target>21</maven.compiler.target>
33: 		<mapstruct.version>1.5.5.Final</mapstruct.version>
34: 		<m2e.apt.activation>jdt_apt</m2e.apt.activation>
35: 	</properties>
```
- **Dòng 11 (`<groupId>com.group</groupId>`)**: Tên tổ chức/gói gốc của dự án.
- **Dòng 12 (`<artifactId>blog-website</artifactId>`)**: Tên gói của ứng dụng khi được build ra file `.jar`.
- **Dòng 13 (`<version>0.0.1-SNAPSHOT</version>`)**: Phiên bản đang trong giai đoạn phát triển (SNAPSHOT).
- **Dòng 30-32**: Khai báo sử dụng **Java 21 LTS** (bản Java mới nhất có hỗ trợ dài hạn, hiệu năng cao). Maven Compiler sẽ biên dịch mã nguồn theo chuẩn Java 21.
- **Dòng 33 (`<mapstruct.version>1.5.5.Final</mapstruct.version>`)**: Định nghĩa biến phiên bản cho MapStruct để sử dụng đồng bộ bên dưới.

### Đoạn 3: Chi tiết từng Thư viện Phụ thuộc (Dependencies)
```xml
38: 		<dependency>
39: 			<groupId>com.cloudinary</groupId>
40: 			<artifactId>cloudinary-http44</artifactId>
41: 			<version>1.36.0</version>
42: 		</dependency>
```
- **Cloudinary SDK**: Thư viện chính thức từ Cloudinary giúp ứng dụng tải file ảnh từ máy người dùng lên máy chủ đám mây Cloudinary thông qua giao thức HTTP và nhận lại link ảnh URL HTTPS.

```xml
43: 		<dependency>
44: 			<groupId>org.springframework.boot</groupId>
45: 			<artifactId>spring-boot-starter-oauth2-resource-server</artifactId>
46: 		</dependency>
```
- **OAuth2 Resource Server**: Biến ứng dụng Spring Boot thành một "Resource Server" có khả năng nhận và tự động kiểm tra, giải mã chữ ký của chuỗi **JWT Bearer Token** trong các HTTP Request.

```xml
47: 		<dependency>
48: 			<groupId>org.springframework.boot</groupId>
49: 			<artifactId>spring-boot-starter-data-jpa</artifactId>
50: 		</dependency>
```
- **Spring Data JPA**: Cung cấp công nghệ Hibernate ORM (Object-Relational Mapping), tự động sinh câu lệnh SQL và quản lý giao tiếp với CSDL qua các interface `JpaRepository`.

```xml
51: 		<dependency>
52: 			<groupId>org.springframework.boot</groupId>
53: 			<artifactId>spring-boot-starter-security</artifactId>
54: 		</dependency>
```
- **Spring Security**: "Lá chắn thép" bảo mật của toàn bộ dự án, quản lý phân quyền (Role-based access control), chống truy cập trái phép vào các API của hệ thống.

```xml
55: 		<dependency>
56: 			<groupId>org.springframework.boot</groupId>
57: 			<artifactId>spring-boot-starter-thymeleaf</artifactId>
58: 		</dependency>
```
- **Thymeleaf Starter**: Template Engine giúp render mã HTML động phía máy chủ, ghép dữ liệu từ Model vào trang giao diện web trước khi trả về cho trình duyệt.

```xml
60: 		<dependency>
61: 			<groupId>org.springframework.boot</groupId>
62: 			<artifactId>spring-boot-starter-web</artifactId>
63: 		</dependency>
```
- **Spring Web**: Chứa nhúng sẵn máy chủ web **Apache Tomcat** (chạy ở cổng 8080 mặc định), cung cấp các công cụ xây dựng RESTful API (`@RestController`, `@GetMapping`, `@PostMapping`...).

```xml
65: 		<dependency>
66: 			<groupId>org.springframework.boot</groupId>
67: 			<artifactId>spring-boot-starter-validation</artifactId>
68: 		</dependency>
```
- **Validation Starter (Hibernate Validator)**: Giúp kiểm tra tính hợp lệ của dữ liệu đầu vào ngay tại DTO bằng các chú thích như `@NotBlank`, `@Size(min = 6)`, `@Email`... trước khi chuyển cho tầng Service.

```xml
70: 		<dependency>
71: 			<groupId>org.thymeleaf.extras</groupId>
72: 			<artifactId>thymeleaf-extras-springsecurity6</artifactId>
73: 		</dependency>
```
- **Thymeleaf Extras Spring Security 6**: Cho phép viết các thẻ điều kiện phân quyền ngay trong file HTML (ví dụ: chỉ hiển thị nút Quản trị nếu user có vai trò ADMIN: `sec:authorize="hasRole('ADMIN')"`).

```xml
74: 		<dependency>
75: 			<groupId>org.springframework.security</groupId>
76: 			<artifactId>spring-security-crypto</artifactId>
77: 		</dependency>
```
- **Spring Security Crypto**: Cung cấp thuật toán băm mật khẩu an toàn cao `BCryptPasswordEncoder`. Mật khẩu được băm một chiều kèm chuỗi ngẫu nhiên (salt), không ai có thể giải mã ngược lại được kể cả người quản trị cơ sở dữ liệu.

```xml
78: 		<dependency>
79: 			<groupId>com.nimbusds</groupId>
80: 			<artifactId>nimbus-jose-jwt</artifactId>
81: 			<version>9.30.1</version>
82: 		</dependency>
```
- **Nimbus JOSE + JWT**: Thư viện hàng đầu để tạo (generate), ký số (sign) và xác thực (verify) các token JSON Web Token (JWT) theo chuẩn mã hóa HMAC-SHA512.

```xml
83: 		<dependency>
84: 			<groupId>org.springframework.boot</groupId>
85: 			<artifactId>spring-boot-devtools</artifactId>
86: 			<scope>runtime</scope>
87: 			<optional>true</optional>
88: 		</dependency>
```
- **DevTools**: Công cụ hỗ trợ nhà phát triển, tự động khởi động lại ứng dụng (Live Reload / Auto Restart) khi phát hiện có thay đổi trong mã nguồn mà không cần bấm nút Run thủ công.

```xml
89: 		<dependency>
90: 			<groupId>com.mysql</groupId>
91: 			<artifactId>mysql-connector-j</artifactId>
92: 			<scope>runtime</scope>
93: 		</dependency>
94: 		<dependency>
95: 			<groupId>com.h2database</groupId>
96: 			<artifactId>h2</artifactId>
97: 			<scope>runtime</scope>
98: 		</dependency>
```
- **MySQL Connector/J & H2 Database**: 
  - `mysql-connector-j`: Driver kết nối MySQL khi triển khai hệ thống lớn thực tế.
  - `h2`: Hệ quản trị cơ sở dữ liệu nhúng (Embedded In-memory / File Database). H2 giúp ứng dụng chạy được ngay lập tức trên máy của giảng viên hoặc bất kỳ thành viên nào mà không cần cài MySQL Server hay cấu hình mật khẩu DB phức tạp.

```xml
100: 		<dependency>
101: 			<groupId>org.projectlombok</groupId>
102: 			<artifactId>lombok</artifactId>
103: 			<optional>true</optional>
104: 		</dependency>
```
- **Lombok**: Thư viện loại bỏ code thừa (Boilerplate code). Tự động sinh `getters`, `setters`, `equals`, `hashCode`, `toString`, và mẫu thiết kế `Builder` (`@Builder`, `@Data`, `@NoArgsConstructor`, `@AllArgsConstructor`) trong quá trình biên dịch (Compile-time).

```xml
106: 		<dependency>
107: 			<groupId>org.mapstruct</groupId>
108: 			<artifactId>mapstruct</artifactId>
109: 			<version>${mapstruct.version}</version>
110: 		</dependency>
111: 		<dependency>
112: 			<groupId>org.mapstruct</groupId>
113: 			<artifactId>mapstruct-processor</artifactId>
114: 			<version>${mapstruct.version}</version>
115: 			<scope>provided</scope>
116: 		</dependency>
117: 		<dependency>
118: 			<groupId>org.projectlombok</groupId>
119: 			<artifactId>lombok-mapstruct-binding</artifactId>
120: 			<version>0.2.0</version>
121: 		</dependency>
```
- **MapStruct & lombok-mapstruct-binding**: Thư viện sinh code chuyển đổi đối tượng siêu tốc độ tại thời điểm compile-time. `lombok-mapstruct-binding` đảm bảo Lombok tạo xong getter/setter thì MapStruct mới tiến hành tạo code ánh xạ, tránh xung đột thứ tự biên dịch.

```xml
125: 		<dependency>
126: 			<groupId>org.springframework.boot</groupId>
127: 			<artifactId>spring-boot-starter-test</artifactId>
128: 			<scope>test</scope>
129: 		</dependency>
130: 		<dependency>
131: 			<groupId>org.springframework.security</groupId>
132: 			<artifactId>spring-security-test</artifactId>
133: 			<scope>test</scope>
134: 		</dependency>
```
- **Test Dependencies**: Chứa bộ khung kiểm thử tự động JUnit 5, Mockito, AssertJ và các công cụ test bảo mật để phục vụ việc viết Unit Test cho ứng dụng.

### Đoạn 4: Cấu hình Build Plugin và Bộ tiền xử lý chú thích (Annotation Processors)
```xml
136: 	<build>
137: 		<plugins>
138: 			<plugin>
139: 				<groupId>org.apache.maven.plugins</groupId>
140: 				<artifactId>maven-compiler-plugin</artifactId>
141: 				<configuration>
142: 					<source>21</source>
143: 					<target>21</target>
144: 					<annotationProcessorPaths>
145: 						<path>
146: 							<groupId>org.projectlombok</groupId>
147: 							<artifactId>lombok</artifactId>
148: 						</path>
149: 						<path>
150: 							<groupId>org.mapstruct</groupId>
151: 							<artifactId>mapstruct-processor</artifactId>
152: 							<version>${mapstruct.version}</version>
153: 						</path>
154: 						<path>
155: 							<groupId>org.projectlombok</groupId>
156: 							<artifactId>lombok-mapstruct-binding</artifactId>
157: 							<version>0.2.0</version>
158: 						</path>
159: 					</annotationProcessorPaths>
160: 				</configuration>
161: 			</plugin>
162: 			<plugin>
163: 				<groupId>org.springframework.boot</groupId>
164: 				<artifactId>spring-boot-maven-plugin</artifactId>
165: 				<configuration>
166: 					<excludes>
167: 						<exclude>
168: 							<groupId>org.projectlombok</groupId>
169: 							<artifactId>lombok</artifactId>
170: 						</exclude>
171: 					</excludes>
172: 				</configuration>
173: 			</plugin>
174: 		</plugins>
175: 	</build>
```
- **`maven-compiler-plugin`**: Plugin biên dịch của Maven. Cấu hình source/target mức Java 21. 
  - Khai báo các `annotationProcessorPaths` theo đúng thứ tự: `lombok` -> `mapstruct-processor` -> `lombok-mapstruct-binding`. Nếu không có đoạn này, MapStruct sẽ báo lỗi không tìm thấy getter/setter của Lombok khi build!
- **`spring-boot-maven-plugin`**: Đóng gói toàn bộ ứng dụng cùng máy chủ Tomcat nhúng thành một file duy nhất: **Fat JAR (Executable JAR)**. Khi đó, người dùng chỉ cần gõ lệnh `java -jar blog-website-0.0.1-SNAPSHOT.jar` là web chạy ngay.

---

## 3. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN VỀ FILE POM.XML & CÂU TRẢ LỜI

### Câu 1: Em hãy giải thích `<scope>runtime</scope>` và `<scope>test</scope>` trong file pom.xml có ý nghĩa gì?
- **Trả lời**:
  > "Thưa thầy/cô:
  > - `<scope>runtime</scope>` (như thư viện H2, MySQL Connector): Nghĩa là thư viện này không cần thiết trong quá trình biên dịch mã nguồn Java (compile-time) vì code của chúng em chỉ gọi các interface chuẩn của JDBC/JPA, nhưng bắt buộc phải có khi ứng dụng bắt đầu chạy thực tế (runtime) để nạp driver kết nối database.
  > - `<scope>test</scope>`: Nghĩa là thư viện đó (như JUnit, Mockito) chỉ phục vụ cho việc biên dịch và chạy các file kiểm thử trong thư mục `src/test/`. Khi chúng em build ứng dụng ra file jar chính thức để deploy lên production thì Maven sẽ loại bỏ các thư viện test này để giảm dung lượng file."

### Câu 2: Tại sao trong pom.xml nhóm em phải cấu hình cả Lombok lẫn MapStruct trong thẻ `<annotationProcessorPaths>`?
- **Trả lời**:
  > "Thưa thầy/cô, cả Lombok và MapStruct đều hoạt động tại thời điểm biên dịch (Annotation Processing). MapStruct cần đọc các hàm Getter/Setter để tự động sinh code chuyển đổi DTO sang Entity. Tuy nhiên các hàm Getter/Setter này lại do Lombok sinh ra chứ chúng em không viết tay. 
  > Do đó, chúng em phải khai báo `annotationProcessorPaths` kèm thư viện `lombok-mapstruct-binding` để chỉ định thứ tự rõ ràng: Lombok phải sinh code trước, sau đó MapStruct mới đọc code đó để sinh Mapper. Nếu thiếu cấu hình này, quá trình `mvn clean compile` sẽ bị văng lỗi không tìm thấy phương thức."
