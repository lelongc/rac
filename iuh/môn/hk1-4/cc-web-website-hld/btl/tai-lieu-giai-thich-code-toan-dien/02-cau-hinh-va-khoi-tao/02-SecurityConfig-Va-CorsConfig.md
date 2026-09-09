# GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG SECURITYCONFIG VÀ CORSCONFIG

> **Tầm quan trọng đặc biệt**: Đây là file quan trọng nhất trong kỳ thi vấn đáp môn Web/BTL tại IUH. Giảng viên thường xuyên mở file `SecurityConfig.java` và yêu cầu sinh viên chỉ tay giải thích từng dòng: Tại sao phải tắt CSRF? Tại sao cấu hình Stateless? Làm sao hệ thống biết được ai là ADMIN ai là USER?

---

## 1. MÃ NGUỒN ĐẦY ĐỦ CỦA `SecurityConfig.java`

File nằm tại: `src/main/java/com/group/blog/config/SecurityConfig.java`

```java
package com.group.blog.config;

import com.group.blog.enums.Role;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpMethod;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configurers.AbstractHttpConfigurer;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.oauth2.jose.jws.MacAlgorithm;
import org.springframework.security.oauth2.jwt.JwtDecoder;
import org.springframework.security.oauth2.jwt.NimbusJwtDecoder;
import org.springframework.security.oauth2.server.resource.authentication.JwtAuthenticationConverter;
import org.springframework.security.oauth2.server.resource.authentication.JwtGrantedAuthoritiesConverter;
import org.springframework.security.web.SecurityFilterChain;

import javax.crypto.spec.SecretKeySpec;

@Configuration
@EnableWebSecurity
public class SecurityConfig {

    private final String[] PUBLIC_POST_ENDPOINTS = {
            "/users",
            "/auth/login",
            "/auth/introspect",
            "/h2-console/**"
    };

    private final String[] PUBLIC_GET_ENDPOINTS = {
            "/assets/**", "/css/**", "/js/**",
            "/fragments/**",
            "/h2-console/**",
            "/", "/home", "/home-page.html",
            "/login", "/login.html",
            "/register", "/register.html",
            "/forgot-password", "/forgot-password.html",
            "/change-password", "/change-password.html",
            "/post", "/post.html",
            "/blog-editor", "/blog-editor.html",
            "/user-profile", "/user-profile.html",
            "/edit-profile", "/edit-profile.html",
            "/saved-blogs", "/saved-blogs.html",
            "/notifications", "/notifications.html",
            "/manage-blogs", "/manage-blogs.html", "/Manage-Blogs.html",
            "/admin", "/admin/**",
            "/pages/**",
            "/categories", "/tags",
            "/blogs",
            "/blogs/{id:[0-9a-fA-F\\-]{36}}",
            "/blogs/category/**",
            "/blogs/tag/**",
            "/blogs/search/**",
            "/blogs/filter",
            "/blogs/user/**",
            "/users/profile/**",
            "/blogs/*/comments",
            "/users/*/followers",
            "/users/*/following"
    };

    private final String[] ADMIN_ENDPOINTS = {
            "/api/admin/**"
    };

    @Value("${jwt.signerKey}")
    private String signerKey;

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity httpSecurity) throws Exception {
        httpSecurity
                .cors(org.springframework.security.config.Customizer.withDefaults())
                .headers(headers -> headers.frameOptions(frame -> frame.disable()))
                .authorizeHttpRequests(request -> request
                        .requestMatchers(HttpMethod.POST, PUBLIC_POST_ENDPOINTS).permitAll()
                        .requestMatchers(HttpMethod.GET, PUBLIC_GET_ENDPOINTS).permitAll()
                        .requestMatchers("/h2-console/**").permitAll()
                        .requestMatchers(ADMIN_ENDPOINTS).hasRole(Role.ADMIN.name())
                        .requestMatchers(HttpMethod.GET, "/users").hasRole(Role.ADMIN.name())
                        .requestMatchers(HttpMethod.POST, "/categories", "/tags").hasRole(Role.ADMIN.name())
                        .requestMatchers(HttpMethod.PUT, "/categories/**", "/tags/**").hasRole(Role.ADMIN.name())
                        .requestMatchers(HttpMethod.DELETE, "/categories/**", "/tags/**").hasRole(Role.ADMIN.name())
                        .anyRequest().authenticated()
                );

        httpSecurity.oauth2ResourceServer(oauth2 ->
                oauth2.jwt(jwtConfigurer -> jwtConfigurer.decoder(jwtDecoder())
                        .jwtAuthenticationConverter(jwtAuthenticationConverter()))
        );

        httpSecurity.csrf(AbstractHttpConfigurer::disable);

        httpSecurity.sessionManagement(session -> session
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
        );

        return httpSecurity.build();
    }

    @Bean
    JwtAuthenticationConverter jwtAuthenticationConverter() {
        JwtGrantedAuthoritiesConverter jwtGrantedAuthoritiesConverter = new JwtGrantedAuthoritiesConverter();
        jwtGrantedAuthoritiesConverter.setAuthorityPrefix("ROLE_");
        JwtAuthenticationConverter jwtAuthenticationConverter = new JwtAuthenticationConverter();
        jwtAuthenticationConverter.setJwtGrantedAuthoritiesConverter(jwtGrantedAuthoritiesConverter);
        return jwtAuthenticationConverter;
    }

    @Bean
    JwtDecoder jwtDecoder() {
        SecretKeySpec secretKeySpec = new SecretKeySpec(signerKey.getBytes(), "HmacSHA512");
        return NimbusJwtDecoder
                .withSecretKey(secretKeySpec)
                .macAlgorithm(MacAlgorithm.HS512)
                .build();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder(10);
    }

    @Bean
    public org.springframework.web.cors.CorsConfigurationSource corsConfigurationSource() {
        org.springframework.web.cors.CorsConfiguration configuration = new org.springframework.web.cors.CorsConfiguration();
        configuration.setAllowedOriginPatterns(java.util.List.of("*"));
        configuration.setAllowedMethods(java.util.List.of("GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"));
        configuration.setAllowedHeaders(java.util.List.of("*"));
        configuration.setAllowCredentials(true);
        org.springframework.web.cors.UrlBasedCorsConfigurationSource source = new org.springframework.web.cors.UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/**", configuration);
        return source;
    }
}
```

---

## 2. GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG `SecurityConfig.java`

### 2.1. Các Annotation lớp
```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {
```
- **`@Configuration`**: Báo cho Spring Boot biết đây là một lớp cấu hình. Trong lớp này sẽ có các phương thức đánh dấu `@Bean` để tạo và đưa các đối tượng vào vùng quản lý Spring IoC Container.
- **`@EnableWebSecurity`**: Kích hoạt cơ chế bảo mật của Spring Security cho toàn bộ ứng dụng web, cho phép can thiệp vào chuỗi lọc FilterChain.

---

### 2.2. Danh sách các URL công khai và đường dẫn Admin
```java
    private final String[] PUBLIC_POST_ENDPOINTS = {
            "/users",              // Cho phép khách vãng lai đăng ký tài khoản mới
            "/auth/login",          // Cho phép đăng nhập lấy token
            "/auth/introspect",     // Cho phép kiểm tra token có còn hạn hay không
            "/h2-console/**"       // Cho phép gửi form đăng nhập vào H2 console
    };
```
- Mọi request POST gửi đến 4 đường dẫn này đều được phép đi qua mà không cần có Token trước.

```java
    private final String[] PUBLIC_GET_ENDPOINTS = { ... }
```
- Chứa toàn bộ file tĩnh (CSS, JS, hình ảnh), các trang giao diện HTML (trang chủ, xem bài viết, đăng nhập, hồ sơ) và các API lấy dữ liệu công khai (danh sách blog, tìm kiếm, đọc bình luận). Khách chưa đăng nhập vẫn đọc được báo bình thường như các trang VnExpress hay Medium.

```java
    private final String[] ADMIN_ENDPOINTS = {
            "/api/admin/**"
    };
```
- Định nghĩa vùng URL nhạy cảm dành riêng cho quản trị viên, nơi thống kê số lượng user, bài viết, tương tác.

---

### 2.3. Cấu hình chuỗi lọc bảo mật `filterChain(HttpSecurity httpSecurity)`

```java
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity httpSecurity) throws Exception {
```
- **`SecurityFilterChain`**: Chuỗi các "chốt kiểm soát" (Filters) mà mọi HTTP Request gửi đến server đều phải đi qua trước khi đến được Controller.

```java
        httpSecurity
                .cors(org.springframework.security.config.Customizer.withDefaults())
```
- Kích hoạt cơ chế kiểm soát chia sẻ tài nguyên nguồn gốc chéo (CORS) theo cấu hình Bean `corsConfigurationSource()` bên dưới.

```java
                .headers(headers -> headers.frameOptions(frame -> frame.disable()))
```
- **Tại sao phải có dòng này?**: Mặc định Spring Security bật chế độ `X-Frame-Options: DENY` để chống tấn công Clickjacking (ngăn trang web bị nhúng vào thẻ `<iframe>`). Tuy nhiên, giao diện web H2 Console (`/h2-console`) sử dụng thẻ `<iframe>` để chia giao diện thành 3 khung (cây danh mục bên trái, màn hình nhập SQL bên phải). Nếu không tắt `frameOptions`, H2 Console sẽ bị chặn và hiện màn hình trắng xóa!

```java
                .authorizeHttpRequests(request -> request
                        .requestMatchers(HttpMethod.POST, PUBLIC_POST_ENDPOINTS).permitAll()
                        .requestMatchers(HttpMethod.GET, PUBLIC_GET_ENDPOINTS).permitAll()
                        .requestMatchers("/h2-console/**").permitAll()
                        .requestMatchers(ADMIN_ENDPOINTS).hasRole(Role.ADMIN.name())
                        .requestMatchers(HttpMethod.GET, "/users").hasRole(Role.ADMIN.name())
                        .requestMatchers(HttpMethod.POST, "/categories", "/tags").hasRole(Role.ADMIN.name())
                        .requestMatchers(HttpMethod.PUT, "/categories/**", "/tags/**").hasRole(Role.ADMIN.name())
                        .requestMatchers(HttpMethod.DELETE, "/categories/**", "/tags/**").hasRole(Role.ADMIN.name())
                        .anyRequest().authenticated()
                );
```
- **`.permitAll()`**: Cho phép tất cả mọi người (kể cả chưa đăng nhập) được truy cập.
- **`.hasRole(Role.ADMIN.name())`**: Bắt buộc người dùng phải đăng nhập VÀ có quyền `ADMIN`. Các API này gồm: Xem danh sách toàn bộ người dùng (`GET /users`), Thêm mới/Cập nhật/Xóa Danh mục và Thẻ (`POST/PUT/DELETE /categories`, `/tags`), và các API thống kê (`/api/admin/**`).
- **`.anyRequest().authenticated()`**: Bất kỳ API nào khác không được liệt kê ở trên (ví dụ: viết bài mới `POST /blogs`, like bài viết `POST /blogs/{id}/like`, bookmark, comment) thì **bắt buộc phải đăng nhập** mới được thực hiện.

---

### 2.4. Cấu hình xác thực Resource Server bằng JWT Token
```java
        httpSecurity.oauth2ResourceServer(oauth2 ->
                oauth2.jwt(jwtConfigurer -> jwtConfigurer.decoder(jwtDecoder())
                        .jwtAuthenticationConverter(jwtAuthenticationConverter()))
        );
```
- Tích hợp bộ giải mã JWT Token vào Spring Security.
- Mỗi khi có request gửi lên kèm tiêu đề `Authorization: Bearer <token>`, Spring Security sẽ:
  1. Dùng `jwtDecoder()` để kiểm tra tính toàn vẹn và hạn sử dụng của token.
  2. Dùng `jwtAuthenticationConverter()` để trích xuất quyền hạn (Roles) của user và nạp vào đối tượng `SecurityContextHolder`.

---

### 2.5. Tắt CSRF và cấu hình Stateless
```java
        httpSecurity.csrf(AbstractHttpConfigurer::disable);

        httpSecurity.sessionManagement(session -> session
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
        );
```
- **`csrf(AbstractHttpConfigurer::disable)`**: Tắt tính năng phòng chống CSRF (Cross-Site Request Forgery). Vì sao tắt? CSRF chỉ đe dọa các hệ thống truyền thống dùng Cookie và Session để lưu phiên đăng nhập. Ứng dụng của chúng ta dùng **JWT Token** lưu trong header của Request, trình duyệt không tự động gửi Token nên hoàn toàn miễn nhiễm với tấn công CSRF. Việc tắt CSRF giúp client gọi REST API dễ dàng mà không bị lỗi 403 Forbidden.
- **`SessionCreationPolicy.STATELESS`**: Máy chủ sẽ không bao giờ tạo `HttpSession`. Mọi thông tin người dùng đều được gói gọn trong Token JWT.

---

### 2.6. Xử lý tiền tố Role: `jwtAuthenticationConverter()`
```java
    @Bean
    JwtAuthenticationConverter jwtAuthenticationConverter() {
        JwtGrantedAuthoritiesConverter jwtGrantedAuthoritiesConverter = new JwtGrantedAuthoritiesConverter();
        jwtGrantedAuthoritiesConverter.setAuthorityPrefix("ROLE_");
        JwtAuthenticationConverter jwtAuthenticationConverter = new JwtAuthenticationConverter();
        jwtAuthenticationConverter.setJwtGrantedAuthoritiesConverter(jwtGrantedAuthoritiesConverter);
        return jwtAuthenticationConverter;
    }
```
- **Bản chất vấn đề**: Trong database và trong JWT Token, quyền của người dùng được lưu dưới dạng chuỗi ngắn gọn như `"ADMIN"`, `"USER"`.
- Tuy nhiên, phương thức `.hasRole("ADMIN")` của Spring Security mặc định luôn tìm kiếm quyền có tiền tố `ROLE_` (tức là `"ROLE_ADMIN"`).
- Phương thức này cài đặt `setAuthorityPrefix("ROLE_")` để tự động ghép tiền tố `ROLE_` vào trước quyền trong Token. Nhờ đó, hàm kiểm tra `.hasRole(Role.ADMIN.name())` hoạt động hoàn toàn chính xác!

---

### 2.7. Giải mã và kiểm tra chữ ký số: `jwtDecoder()`
```java
    @Bean
    JwtDecoder jwtDecoder() {
        SecretKeySpec secretKeySpec = new SecretKeySpec(signerKey.getBytes(), "HmacSHA512");
        return NimbusJwtDecoder
                .withSecretKey(secretKeySpec)
                .macAlgorithm(MacAlgorithm.HS512)
                .build();
    }
```
- Khởi tạo đối tượng `NimbusJwtDecoder` với thuật toán băm chữ ký **HMAC-SHA512** (chuẩn mã hóa an toàn cao).
- Sử dụng `signerKey` lấy từ file `application.yaml` để xác minh chữ ký của Token. Nếu token bị hacker sửa đổi bất kỳ ký tự nào, hàm này sẽ ném ra lỗi xác thực và chặn request ngay lập tức.

---

### 2.8. Mã hóa mật khẩu: `passwordEncoder()`
```java
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder(10);
    }
```
- Cung cấp Bean `PasswordEncoder` sử dụng thuật toán **BCrypt** với độ phức tạp (strength/cost factor) là **10** (chuẩn an toàn của ngành công nghiệp hiện nay).
- Mật khẩu lưu trong DB sẽ có dạng: `$2a$10$e7K0eD...`.

---

### 2.9. Cấu hình CORS: `corsConfigurationSource()`
```java
    @Bean
    public org.springframework.web.cors.CorsConfigurationSource corsConfigurationSource() {
        org.springframework.web.cors.CorsConfiguration configuration = new org.springframework.web.cors.CorsConfiguration();
        configuration.setAllowedOriginPatterns(java.util.List.of("*"));
        configuration.setAllowedMethods(java.util.List.of("GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"));
        configuration.setAllowedHeaders(java.util.List.of("*"));
        configuration.setAllowCredentials(true);
        org.springframework.web.cors.UrlBasedCorsConfigurationSource source = new org.springframework.web.cors.UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/**", configuration);
        return source;
    }
```
- Cho phép trình duyệt gọi API từ các domain khác nhau (Cross-Origin), chấp nhận đầy đủ các phương thức HTTP và mọi loại tiêu đề gửi lên.

---

## 3. FILE `src/main/java/com/group/blog/config/CorsConfig.java`

File này hỗ trợ thêm cấu hình CORS ở tầng MVC:

```java
package com.group.blog.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class CorsConfig {

    @Bean
    public WebMvcConfigurer corsConfigurer() {
        return new WebMvcConfigurer() {
            @Override
            public void addCorsMappings(CorsRegistry registry) {
                registry.addMapping("/**")
                        .allowedOriginPatterns("*")
                        .allowedMethods("GET", "POST", "PUT", "DELETE", "OPTIONS")
                        .allowedHeaders("*")
                        .allowCredentials(true);
            }
        };
    }
}
```
- **Ý nghĩa**: Đảm bảo hai tầng (Spring Security Filter và Spring MVC DispatcherServlet) đều thống nhất chính sách CORS thông thoáng, giúp ứng dụng không bao giờ gặp lỗi `CORS policy: No 'Access-Control-Allow-Origin' header is present`.

---

## 4. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN VỀ BẢO MẬT & TRẢ LỜI ĐIỂM 10

### Câu 1: Tại sao trong `SecurityConfig` nhóm em lại tắt CSRF (`httpSecurity.csrf(AbstractHttpConfigurer::disable)`)? Tắt như vậy có gây mất an toàn cho hệ thống không?
- **Trả lời**:
  > "Thưa thầy/cô, việc tắt CSRF trong dự án này là hoàn toàn đúng chuẩn thiết kế bảo mật REST API và KHÔNG hề gây mất an toàn:
  > - Tấn công CSRF (Cross-Site Request Forgery) chỉ xảy ra khi ứng dụng xác thực người dùng bằng Cookie được trình duyệt tự động gửi kèm theo mỗi request.
  > - Hệ thống của tụi em hoạt động theo cơ chế **Stateless và JWT Bearer Token**. Token được lưu ở `localStorage` của Client và chỉ được gửi lên khi JavaScript chủ động gắn vào tiêu đề `Authorization: Bearer <token>`. Một trang web độc hại từ bên ngoài không thể tự động đọc được `localStorage` của trang web khác (do chính sách Same-Origin Policy của trình duyệt) và không thể tự gắn header Authorization này được. Do đó nguy cơ CSRF hoàn toàn bị triệt tiêu, việc tắt CSRF là bắt buộc để các Client gọi API không bị vướng mã token CSRF dư thừa."

### Câu 2: Em hãy phân biệt sự khác nhau giữa `hasAuthority()` và `hasRole()` trong Spring Security?
- **Trả lời**:
  > "Thưa thầy/cô:
  > - `hasAuthority('X')`: Kiểm tra chính xác chuỗi quyền hạn mà không thêm bất kỳ tiền tố nào (ví dụ kiểm tra quyền đọc báo: `READ_POST`).
  > - `hasRole('ADMIN')`: Spring Security mặc định quy ước các vai trò (Role) phải có tiền tố `ROLE_`. Do đó, khi chúng em gọi `hasRole('ADMIN')`, Spring Security sẽ ngầm tìm kiếm quyền có tên là `ROLE_ADMIN`. 
  > - Để kết nối mượt mà giữa chuỗi `ADMIN` trong token và phương thức `hasRole`, nhóm em đã tạo Bean `JwtAuthenticationConverter` và dùng lệnh `jwtGrantedAuthoritiesConverter.setAuthorityPrefix("ROLE_")` để tự động ghép tiền tố `ROLE_`."

### Câu 3: Làm sao hệ thống nhận diện được user nào đang gọi API khi không dùng Session?
- **Trả lời**:
  > "Thưa thầy/cô, khi client gọi một API yêu cầu đăng nhập (ví dụ: tạo bài viết `POST /blogs`), request sẽ đi kèm tiêu đề `Authorization: Bearer <token>`.
  > Trong `SecurityConfig`, bộ lọc `oauth2ResourceServer` sẽ gọi `jwtDecoder()` để giải mã token. Nếu chữ ký hợp lệ và token chưa hết hạn, Spring Security sẽ trích xuất tên username từ trường `sub` (Subject) của JWT và nạp vào `SecurityContextHolder`.
  > Tại tầng Service, chúng em chỉ cần gọi: `SecurityContextHolder.getContext().getAuthentication().getName()` là lập tức biết chính xác username của người dùng đang thực hiện hành động đó mà không cần dựa vào bất kỳ Session nào trên máy chủ."
