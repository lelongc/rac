# GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG APPLICATIONINITCONFIG

> **Mục tiêu**: Nắm vững cơ chế khởi tạo dữ liệu mẫu (Data Seeding) của Spring Boot khi ứng dụng vừa khởi động. Hiểu rõ tài khoản mẫu của các thành viên nhóm (admin, duonghd, dungnt, longlt), mật khẩu được mã hóa BCrypt như thế nào và cách tạo sẵn Category, Tag, Blog ban đầu.

---

## 1. MÃ NGUỒN ĐẦY ĐỦ CỦA `ApplicationInitConfig.java`

File nằm tại: `src/main/java/com/group/blog/config/ApplicationInitConfig.java`

```java
package com.group.blog.config;

import com.group.blog.entity.Blog;
import com.group.blog.entity.Category;
import com.group.blog.entity.Tag;
import com.group.blog.entity.User;
import com.group.blog.enums.Role;
import com.group.blog.repository.BlogRepository;
import com.group.blog.repository.CategoryRepository;
import com.group.blog.repository.TagRepository;
import com.group.blog.repository.UserRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.ApplicationRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.crypto.password.PasswordEncoder;

import java.time.LocalDateTime;
import java.util.HashSet;
import java.util.Set;

@Configuration
public class ApplicationInitConfig {
    private static final Logger log = LoggerFactory.getLogger(ApplicationInitConfig.class);

    @Autowired
    private PasswordEncoder passwordEncoder;

    @Bean
    ApplicationRunner applicationRunner(
            UserRepository userRepository,
            CategoryRepository categoryRepository,
            TagRepository tagRepository,
            BlogRepository blogRepository
    ) {
        return args -> {
            if (userRepository.findByUsername("admin").isEmpty()) {
                // 1. Tạo tài khoản Admin
                Set<String> adminRoles = new HashSet<>();
                adminRoles.add(Role.ADMIN.name());
                adminRoles.add(Role.USER.name());

                User admin = User.builder()
                        .username("admin")
                        .email("admin@blog.com")
                        .password(passwordEncoder.encode("123456"))
                        .bio("Quản trị viên hệ thống Blog Bleb")
                        .avatarUrl("https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=150")
                        .roles(adminRoles)
                        .build();
                userRepository.save(admin);

                // 2. Tạo tài khoản các thành viên nhóm
                Set<String> userRoles = new HashSet<>();
                userRoles.add(Role.USER.name());

                User duong = User.builder()
                        .username("duonghd")
                        .email("duong.24743991@iuh.edu.vn")
                        .password(passwordEncoder.encode("123456"))
                        .bio("Hoàng Đại Dương - MSSV: 24743991")
                        .avatarUrl("https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?w=150")
                        .roles(userRoles)
                        .build();
                userRepository.save(duong);

                User dung = User.builder()
                        .username("dungnt")
                        .email("dung.24000905@iuh.edu.vn")
                        .password(passwordEncoder.encode("123456"))
                        .bio("Nguyễn Trung Dũng - MSSV: 24000905")
                        .avatarUrl("https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150")
                        .roles(userRoles)
                        .build();
                userRepository.save(dung);

                User longMember = User.builder()
                        .username("longlt")
                        .email("long.23630851@iuh.edu.vn")
                        .password(passwordEncoder.encode("123456"))
                        .bio("Lê Thành Long - MSSV: 23630851")
                        .avatarUrl("https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=150")
                        .roles(userRoles)
                        .build();
                userRepository.save(longMember);

                // 3. Tạo Danh mục (Categories)
                Category catTech = categoryRepository.save(Category.builder().name("Technology").build());
                Category catDev = categoryRepository.save(Category.builder().name("Programming").build());
                Category catDesign = categoryRepository.save(Category.builder().name("Web Design").build());
                Category catLife = categoryRepository.save(Category.builder().name("Life & Tips").build());

                // 4. Tạo Thẻ (Tags)
                Tag tagJava = tagRepository.save(Tag.builder().name("Java").build());
                Tag tagSpring = tagRepository.save(Tag.builder().name("SpringBoot").build());
                Tag tagBootstrap = tagRepository.save(Tag.builder().name("Bootstrap").build());
                Tag tagThymeleaf = tagRepository.save(Tag.builder().name("Thymeleaf").build());
                Tag tagAI = tagRepository.save(Tag.builder().name("AI").build());

                // 5. Tạo các bài viết mẫu (Sample Blogs)
                Set<Tag> tags1 = new HashSet<>();
                tags1.add(tagSpring);
                tags1.add(tagJava);

                Blog blog1 = Blog.builder()
                        .title("Khám phá kiến trúc Spring Boot 3 và cơ chế In-Memory H2 Database")
                        .description("Tìm hiểu cách xây dựng ứng dụng Web hoàn chỉnh với Spring Boot 3, Hibernate JPA và giải pháp H2 Database nhúng không cần cài đặt MySQL.")
                        .content("Spring Boot là một trong những framework phổ biến nhất trong hệ sinh thái Java. Kết hợp với H2 In-memory Database giúp việc kiểm thử và triển khai diễn ra cực kỳ nhanh chóng và tiện lợi.")
                        .banner("https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800")
                        .draft(false)
                        .author(duong)
                        .category(catDev)
                        .tags(tags1)
                        .publishedAt(LocalDateTime.now())
                        .build();
                blogRepository.save(blog1);

                Set<Tag> tags2 = new HashSet<>();
                tags2.add(tagBootstrap);
                tags2.add(tagThymeleaf);

                Blog blog2 = Blog.builder()
                        .title("Thiết kế giao diện hiện đại với Bootstrap 5 & Thymeleaf View Engine")
                        .description("Tối ưu hóa trải nghiệm người dùng với hệ thống lưới Bootstrap 5 kết hợp cùng khả năng render mạnh mẽ từ Thymeleaf trên Spring Boot.")
                        .content("Bootstrap 5 mang đến bộ công cụ CSS mạnh mẽ, hỗ trợ responsive hoàn hảo trên mọi thiết bị di động và máy tính bảng.")
                        .banner("https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800")
                        .draft(false)
                        .author(dung)
                        .category(catDesign)
                        .tags(tags2)
                        .publishedAt(LocalDateTime.now().minusHours(2))
                        .build();
                blogRepository.save(blog2);

                Set<Tag> tags3 = new HashSet<>();
                tags3.add(tagAI);
                tags3.add(tagSpring);

                Blog blog3 = Blog.builder()
                        .title("Ứng dụng Trí tuệ Nhân tạo và Công nghệ Web hướng dữ liệu 2026")
                        .description("Tổng quan về xu hướng phát triển ứng dụng Web tương tác dữ liệu lớn và tích hợp trợ lý AI thông minh.")
                        .content("Trí tuệ nhân tạo đang làm thay đổi toàn diện cách thức các lập trình viên xây dựng và tối ưu hệ thống web hiện đại.")
                        .banner("https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800")
                        .draft(false)
                        .author(longMember)
                        .category(catTech)
                        .tags(tags3)
                        .publishedAt(LocalDateTime.now().minusDays(1))
                        .build();
                blogRepository.save(blog3);

                log.info("Initialized Sample Data Successfully: 4 Users, 4 Categories, 5 Tags, 3 Blogs!");
            }
        };
    }
}
```

---

## 2. GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE

### 2.1. Khởi tạo Logger và Tiêm phụ thuộc (Dependency Injection)
```java
@Configuration
public class ApplicationInitConfig {
    private static final Logger log = LoggerFactory.getLogger(ApplicationInitConfig.class);

    @Autowired
    private PasswordEncoder passwordEncoder;
```
- **`Logger log`**: Công cụ ghi nhật ký chuẩn SLF4J, in các dòng thông báo trạng thái màu mè trên Terminal khi ứng dụng nạp xong dữ liệu mẫu.
- **`@Autowired private PasswordEncoder passwordEncoder;`**: Tiêm Bean mã hóa mật khẩu đã được khai báo trong `SecurityConfig.java`. Mọi mật khẩu mẫu trước khi ghi vào Database đều phải được băm qua đối tượng này.

---

### 2.2. Cơ chế `ApplicationRunner`
```java
    @Bean
    ApplicationRunner applicationRunner(
            UserRepository userRepository,
            CategoryRepository categoryRepository,
            TagRepository tagRepository,
            BlogRepository blogRepository
    ) {
        return args -> {
```
- **`ApplicationRunner` là gì?**: Là một interface đặc biệt trong Spring Boot. Bất kỳ Bean nào trả về `ApplicationRunner` sẽ được Spring Boot **tự động gọi thực thi phương thức run() ngay sau khi toàn bộ ứng dụng và Database đã khởi động thành công 100%**.
- Các tham số truyền vào hàm (`userRepository`, `categoryRepository`...) được Spring tự động tiêm vào (Constructor-based Injection).
- Đoạn mã `return args -> { ... };` sử dụng biểu thức Lambda (Java 8+) để triển khai phương thức duy nhất `run(ApplicationArguments args)` của `ApplicationRunner`.

---

### 2.3. Kiểm tra điều kiện Idempotency (Tránh trùng lặp dữ liệu)
```java
            if (userRepository.findByUsername("admin").isEmpty()) {
```
- **Tại sao phải có dòng `if` này?**: Đây là nguyên tắc cốt tử trong thiết kế hệ thống.
  - Khi cơ sở dữ liệu đã được khởi tạo trong file vật lý `./data/blogdb.mv.db`, lần thứ 2 chúng ta chạy lại ứng dụng, tài khoản `admin` đã tồn tại trong database rồi.
  - Lệnh `userRepository.findByUsername("admin").isEmpty()` sẽ kiểm tra: Nếu `admin` CHƯA có thì mới tiến hành thêm dữ liệu mẫu.
  - Nếu đã có rồi thì bỏ qua toàn bộ khối lệnh bên dưới. Nhờ đó, ứng dụng không bao giờ bị lỗi văng ngoại lệ `Unique constraint violation` (vi phạm trùng khóa chính/username).

---

### 2.4. Tạo tài khoản Quản trị viên (Admin)
```java
                Set<String> adminRoles = new HashSet<>();
                adminRoles.add(Role.ADMIN.name());
                adminRoles.add(Role.USER.name());

                User admin = User.builder()
                        .username("admin")
                        .email("admin@blog.com")
                        .password(passwordEncoder.encode("123456"))
                        .bio("Quản trị viên hệ thống Blog Bleb")
                        .avatarUrl("https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=150")
                        .roles(adminRoles)
                        .build();
                userRepository.save(admin);
```
- Tài khoản `admin` được cấp 2 quyền: cả `ADMIN` và `USER`.
- Mật khẩu gốc là chuỗi `"123456"`. Phương thức `passwordEncoder.encode("123456")` sẽ băm mật khẩu thành chuỗi BCrypt an toàn trước khi lưu vào database.
- Sử dụng cú pháp `User.builder()` (do Lombok tạo ra) giúp tạo đối tượng rõ ràng, không bị nhầm lẫn vị trí tham số so với việc dùng Constructor dài dằng dặc.
- `userRepository.save(admin)`: Lưu đối tượng vào bảng `users`.

---

### 2.5. Tạo tài khoản các thành viên nhóm làm bài tập lớn
```java
                Set<String> userRoles = new HashSet<>();
                userRoles.add(Role.USER.name());

                // Thành viên 1: Hoàng Đại Dương
                User duong = User.builder()
                        .username("duonghd")
                        .email("duong.24743991@iuh.edu.vn")
                        .password(passwordEncoder.encode("123456"))
                        .bio("Hoàng Đại Dương - MSSV: 24743991")
                        .avatarUrl("https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?w=150")
                        .roles(userRoles)
                        .build();
                userRepository.save(duong);

                // Thành viên 2: Nguyễn Trung Dũng
                User dung = User.builder()
                        .username("dungnt")
                        .email("dung.24000905@iuh.edu.vn")
                        .password(passwordEncoder.encode("123456"))
                        .bio("Nguyễn Trung Dũng - MSSV: 24000905")
                        .avatarUrl("https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150")
                        .roles(userRoles)
                        .build();
                userRepository.save(dung);

                // Thành viên 3: Lê Thành Long
                User longMember = User.builder()
                        .username("longlt")
                        .email("long.23630851@iuh.edu.vn")
                        .password(passwordEncoder.encode("123456"))
                        .bio("Lê Thành Long - MSSV: 23630851")
                        .avatarUrl("https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=150")
                        .roles(userRoles)
                        .build();
                userRepository.save(longMember);
```
- Khởi tạo đầy đủ thông tin định danh của cả 3 thành viên trong nhóm kèm MSSV tại trường Đại học Công nghiệp TP.HCM (IUH).
- Đóng vai trò là các tác giả (Authors) sẵn có trong hệ thống để demo tính năng xem trang cá nhân, viết bài, theo dõi lẫn nhau.

---

### 2.6. Tạo sẵn Danh mục, Thẻ Tag và Bài viết mẫu
```java
                Category catTech = categoryRepository.save(Category.builder().name("Technology").build());
                ...
                Tag tagJava = tagRepository.save(Tag.builder().name("Java").build());
                ...
                Blog blog1 = Blog.builder()
                        .title("Khám phá kiến trúc Spring Boot 3 và cơ chế In-Memory H2 Database")
                        ...
                        .author(duong)
                        .category(catDev)
                        .tags(tags1)
                        .publishedAt(LocalDateTime.now())
                        .build();
                blogRepository.save(blog1);
```
- Gán mối quan hệ đối tượng: Bài viết 1 có tác giả là `duong`, thuộc danh mục `catDev` (Programming) và có 2 thẻ tag là `SpringBoot` và `Java`.
- Hibernate sẽ tự động điền các khóa ngoại `author_id`, `category_id` và sinh các dòng trong bảng liên kết nhiều - nhiều `blog_tags`.

---

## 3. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN VỀ KHỞI TẠO DỮ LIỆU & TRẢ LỜI ĐIỂM 10

### Câu 1: Sự khác nhau giữa `ApplicationRunner` và `CommandLineRunner` trong Spring Boot là gì?
- **Trả lời**:
  > "Thưa thầy/cô, cả `ApplicationRunner` và `CommandLineRunner` đều là các interface dùng để chạy code ngay sau khi Spring Context khởi động xong:
  > - `CommandLineRunner`: Nhận tham số đầu vào dưới dạng mảng chuỗi thô `String[] args`.
  > - `ApplicationRunner`: Tiên tiến hơn, nhận đối tượng `ApplicationArguments args`. Đối tượng này cung cấp sẵn các phương thức tiện ích để phân tích cú pháp tham số dòng lệnh dạng key-value (như `--port=8080` hoặc `--debug`). 
  > Nhóm em lựa chọn `ApplicationRunner` vì đây là chuẩn hiện đại và mạnh mẽ hơn."

### Câu 2: Nếu em muốn thêm một tài khoản mới vào cơ sở dữ liệu khi hệ thống đang chạy thì có cần sửa file này không?
- **Trả lời**:
  > "Thưa thầy/cô, hoàn toàn không cần! 
  > File `ApplicationInitConfig` này chỉ đóng vai trò 'Seed Data' (tạo dữ liệu mồi ban đầu cho hệ thống trống). Khi hệ thống đang chạy, người dùng bên ngoài có thể tự bấm nút 'Đăng ký' trên trang web (`POST /users`), hoặc quản trị viên có thể thao tác thông qua API/giao diện Admin để tạo tài khoản một cách linh hoạt."
