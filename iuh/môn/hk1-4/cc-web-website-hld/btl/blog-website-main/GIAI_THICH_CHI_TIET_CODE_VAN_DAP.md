# 🎓 CẨM NANG GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE PHỤC VỤ VẤN ĐÁP BẢO VỆ BTL
> **Môn học**: Công nghệ Web và Website hướng dữ liệu — Trường Đại học Công nghiệp TP.HCM (IUH)  
> **Dự án**: Website Blog & Nền tảng Viết bài trực tuyến đa người dùng  
> **Nhóm thực hiện**: 
> - **24743991** — Hoàng Đại Dương
> - **24000905** — Nguyễn Trung Dũng
> - **23630851** — Lê Thành Long  

---

## 🏛️ TỔNG QUAN KIẾN TRÚC HỆ THỐNG (ARCHITECTURE OVERVIEW)

Dự án áp dụng mô hình kiến trúc **Phân tầng chuẩn doanh nghiệp (Layered Architecture)** kết hợp giữa **RESTful API Backend** và **Single-Page Multi-View Frontend**:

```text
[Trình duyệt Client: HTML5 / CSS3 / JavaScript (Bootstrap 5, jQuery)]
       │
       ▼ (Giao thức HTTP / HTTPS với Header: Authorization: Bearer <JWT>)
[Spring Security Filter Chain: Giải mã JWT, Kiểm tra Quyền hạn ROLE_...]
       │
       ▼
[Controller Layer: ViewController (HTML) & RestController (JSON ApiResponse)]
       │
       ▼
[Service Layer: Xử lý nghiệp vụ logic, Xác thực, Mã hóa mật khẩu, Giao dịch @Transactional]
       │
       ▼
[Repository Layer: Spring Data JPA Repositories (Giao tiếp tầng CSDL bằng ORM)]
       │
       ▼
[Database: H2 Persistent File Database (Lưu trữ vĩnh viễn ./data/blogdb.mv.db)]
```

---

## 🔐 PHẦN 1: CẤU HÌNH BẢO MẬT & PHÂN QUYỀN (`SecurityConfig.java`)

File này là "trái tim" bảo mật của toàn bộ dự án, nằm tại:  
📁 `src/main/java/com/group/blog/config/SecurityConfig.java`

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {
```
* `@Configuration`: Đánh dấu class này chứa các cấu hình Bean cho Spring Boot.
* `@EnableWebSecurity`: Kích hoạt module bảo mật Spring Security cho toàn bộ ứng dụng web.

---

### 1.1. Khai báo danh sách các Endpoint (Dòng 28 - 75)
```java
private final String[] PUBLIC_POST_ENDPOINTS = {
        "/users",           // API Đăng ký tài khoản mới (POST)
        "/auth/login",      // API Đăng nhập lấy Token (POST)
        "/auth/introspect", // API Kiểm tra Token còn hạn hay không (POST)
        "/h2-console/**"    // CSDL H2 Web Console (POST)
};
```
* **Mục đích**: Đây là các API cho phép bất kỳ ai (kể cả chưa đăng nhập) đều được gửi dữ liệu lên máy chủ.

```java
private final String[] PUBLIC_GET_ENDPOINTS = {
        "/assets/**", "/css/**", "/js/**",         // Cho phép tải file CSS/JS giao diện
        "/fragments/**",                           // Cho phép tải thanh navbar, sidebar, footer
        "/h2-console/**",                          // Cho phép mở giao diện CSDL H2
        "/", "/home", "/home-page.html",           // Trang chủ
        "/login", "/register",                     // Trang Đăng nhập & Đăng ký
        "/post", "/blog-editor",                   // Trang đọc bài & viết bài
        "/user-profile", "/edit-profile",          // Trang hồ sơ người dùng
        "/saved-blogs", "/notifications",          // Trang bài viết đã lưu & thông báo
        "/manage-blogs",                           // Trang quản lý bài viết của tôi
        "/admin", "/admin/**",                     // Cho phép mở view HTML của Admin
        "/categories", "/tags", "/blogs/**"        // Cho phép đọc danh mục, tag, xem danh sách bài viết
};
```
* **Giải thích vấn đáp**: Tại sao lại cho phép `/admin/**` trong `PUBLIC_GET_ENDPOINTS`?  
  *Vì kiến trúc của chúng ta tải trang HTML trước bằng GET (không có header JWT lúc click link), sau đó JavaScript trên trang mới lấy Token trong `localStorage` gửi lên API `/api/admin/**`. Tầng bảo mật dữ liệu thực sự nằm ở `ADMIN_ENDPOINTS`.*

```java
private final String[] ADMIN_ENDPOINTS = {
        "/api/admin/**" // API dữ liệu thống kê, quản trị chỉ dành cho ADMIN
};
```

---

### 1.2. Chuỗi lọc bảo mật `filterChain(HttpSecurity httpSecurity)` (Dòng 81 - 119)
```java
@Bean
public SecurityFilterChain filterChain(HttpSecurity httpSecurity) throws Exception {
    httpSecurity
            // 1. Cấu hình CORS cho phép các request từ trình duyệt
            .cors(org.springframework.security.config.Customizer.withDefaults())
            
            // 2. Cho phép hiển thị giao diện H2-Console trong thẻ <iframe>
            .headers(headers -> headers.frameOptions(frame -> frame.disable()))
            
            // 3. Thiết lập quyền truy cập cho từng đường dẫn
            .authorizeHttpRequests(request -> request
                    .requestMatchers(HttpMethod.POST, PUBLIC_POST_ENDPOINTS).permitAll()
                    .requestMatchers(HttpMethod.GET, PUBLIC_GET_ENDPOINTS).permitAll()
                    .requestMatchers("/h2-console/**").permitAll()

                    // Chặn quyền Admin: Chỉ tài khoản có ROLE_ADMIN mới gọi được API này
                    .requestMatchers(ADMIN_ENDPOINTS).hasRole(Role.ADMIN.name())
                    .requestMatchers(HttpMethod.GET, "/users").hasRole(Role.ADMIN.name())
                    .requestMatchers(HttpMethod.POST, "/categories", "/tags").hasRole(Role.ADMIN.name())
                    .requestMatchers(HttpMethod.PUT, "/categories/**", "/tags/**").hasRole(Role.ADMIN.name())
                    .requestMatchers(HttpMethod.DELETE, "/categories/**", "/tags/**").hasRole(Role.ADMIN.name())

                    // Tất cả các request còn lại (like, comment, post bài...) bắt buộc phải đăng nhập
                    .anyRequest().authenticated()
            );

    // 4. Cấu hình giải mã và xác thực Token JWT trong header Authorization
    httpSecurity.oauth2ResourceServer(oauth2 ->
            oauth2.jwt(jwtConfigurer -> jwtConfigurer.decoder(jwtDecoder())
                    .jwtAuthenticationConverter(jwtAuthenticationConverter()))
    );

    // 5. Tắt bảo vệ CSRF vì hệ thống sử dụng Stateless Token JWT
    httpSecurity.csrf(AbstractHttpConfigurer::disable);

    // 6. Chế độ STATELESS: Server không lưu Session trên RAM
    httpSecurity.sessionManagement(session -> session
            .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
    );

    return httpSecurity.build();
}
```
* **Câu hỏi vấn đáp**: *"Tại sao lại tắt CSRF (`csrf().disable()`)?"*  
  *Trả lời: Vì ứng dụng sử dụng cơ chế xác thực dựa trên Token JWT gửi qua Header HTTP (`Authorization: Bearer <token>`), không sử dụng Cookie Session của trình duyệt nên không bị tấn công theo kiểu Cross-Site Request Forgery.*

---

### 1.3. Bộ chuyển đổi Quyền hạn `jwtAuthenticationConverter()` (Dòng 122 - 128)
```java
@Bean
JwtAuthenticationConverter jwtAuthenticationConverter() {
    JwtGrantedAuthoritiesConverter jwtGrantedAuthoritiesConverter = new JwtGrantedAuthoritiesConverter();
    jwtGrantedAuthoritiesConverter.setAuthorityPrefix("ROLE_"); // Tự động thêm tiền tố "ROLE_"
    JwtAuthenticationConverter jwtAuthenticationConverter = new JwtAuthenticationConverter();
    jwtAuthenticationConverter.setJwtGrantedAuthoritiesConverter(jwtGrantedAuthoritiesConverter);
    return jwtAuthenticationConverter;
}
```
* **Ý nghĩa**: Trong JWT Token, claim `scope` lưu giá trị là `"ADMIN"` hoặc `"USER"`. Spring Security yêu cầu quyền phải có dạng `ROLE_ADMIN` để hàm `.hasRole("ADMIN")` nhận diện được. Đoạn code này tự động thêm tiền tố `ROLE_` vào.

---

### 1.4. Bộ giải mã Token `jwtDecoder()` và Mã hóa mật khẩu `passwordEncoder()` (Dòng 131 - 142)
```java
@Bean
JwtDecoder jwtDecoder() {
    SecretKeySpec secretKeySpec = new SecretKeySpec(signerKey.getBytes(), "HmacSHA512");
    return NimbusJwtDecoder
            .withSecretKey(secretKeySpec)
            .macAlgorithm(MacAlgorithm.HS512) // Sử dụng thuật toán băm cực mạnh HS512
            .build();
}

@Bean
public PasswordEncoder passwordEncoder() {
    return new BCryptPasswordEncoder(10); // Băm mật khẩu bằng BCrypt độ khó 10
}
```
* **Câu hỏi vấn đáp**: *"BCrypt có giải mã ngược lại được không?"*  
  *Trả lời: Không. BCrypt là hàm băm một chiều (One-way Hash). Khi người dùng đăng nhập, hệ thống sẽ băm mật khẩu người dùng vừa nhập và so khớp hai chuỗi băm thông qua hàm `passwordEncoder.matches()`.*

---

## 🔑 PHẦN 2: XÁC THỰC & SINH TOKEN JWT (`AuthenticationService.java`)

File này nằm tại:  
📁 `src/main/java/com/group/blog/service/AuthenticationService.java`

### 2.1. Phương thức Đăng nhập `authenticate()` (Dòng 42 - 53)
```java
public AuthenticationResponse authenticate(AuthenticationRequest request){
    // 1. Thiết lập thời gian hết hạn của Token là 1 tiếng kể từ lúc đăng nhập
    Date expiryTime = new Date(Instant.now().plus(1, ChronoUnit.HOURS).toEpochMilli());
    
    // 2. Tìm người dùng trong CSDL theo username, nếu không có ném lỗi USER_NOT_EXITED
    var user = userRepository.findByUsername(request.getUsername())
            .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));
    
    // 3. So khớp mật khẩu nhập vào với mật khẩu đã băm BCrypt trong CSDL
    boolean authenticated = passwordEncoder.matches(request.getPassword(), user.getPassword());
    if(!authenticated) 
        throw new AppException(ErrorCode.UNAUTHENTICATED); // Báo lỗi nếu sai mật khẩu
    
    // 4. Sinh ra chuỗi JWT Token từ thông tin người dùng
    var token = generateToken(user, expiryTime);
    
    return AuthenticationResponse.builder()
            .token(token)
            .authenticated(true)
            .expiryTime(expiryTime)
            .build();
}
```

---

### 2.2. Phương thức Sinh Token `generateToken()` (Dòng 55 - 73)
```java
private String generateToken(User user, Date expiryTime){
    // 1. Header: Định nghĩa thuật toán băm HS512
    JWSHeader header = new JWSHeader(JWSAlgorithm.HS512);
    
    // 2. Payload: Chứa các thông tin định danh (Claims)
    JWTClaimsSet jwtClaimsSet = new JWTClaimsSet.Builder()
            .subject(user.getUsername())             // Chủ thể token: username người dùng
            .issuer("group.com")                     // Nguồn phát hành
            .issueTime(new Date())                   // Thời điểm phát hành
            .expirationTime(expiryTime)              // Thời điểm hết hạn
            .claim("scope", buildScope(user))        // Danh sách quyền (ví dụ: "ADMIN USER")
            .build();
            
    Payload payload = new Payload(jwtClaimsSet.toJSONObject());
    JWSObject jwsObject = new JWSObject(header, payload);
    
    // 3. Signature: Ký token bằng bí mật SIGNER_KEY để chống giả mạo
    try {
        jwsObject.sign(new MACSigner(SIGNER_KEY.getBytes()));
        return jwsObject.serialize(); // Trả về chuỗi JWT dạng xxxxx.yyyyy.zzzzz
    } catch (JOSEException e) {
        log.error("Cannot create token", e);
        throw new RuntimeException(e);
    }
}
```

---

## 👤 PHẦN 3: ĐĂNG KÝ & QUẢN LÝ NGƯỜI DÙNG (`UserService.java`)

File này nằm tại:  
📁 `src/main/java/com/group/blog/service/UserService.java`

### 3.1. Phương thức Tạo tài khoản mới `createUser()` (Dòng 38 - 47)
```java
public UserResponse createUser(UserCreatetionRequest request){
    // 1. Kiểm tra username đã tồn tại trong CSDL chưa
    if(userRepository.existsByUsername(request.getUsername())) 
        throw new AppException(ErrorCode.USER_EXITED);
        
    // 2. Chuyển đổi từ DTO Request sang Entity User bằng MapStruct
    User u = userMapper.toUser(request);
    
    // 3. Khởi tạo tập hợp roles nếu null để tránh NullPointerException
    if(u.getRoles() == null) u.setRoles(new HashSet<>());
    
    // 4. Mã hóa mật khẩu người dùng trước khi lưu vào CSDL
    u.setPassword(passwordEncoder.encode(request.getPassword()));
    
    // 5. Gán vai trò mặc định khi đăng ký là ROLE_USER
    u.getRoles().add(Role.USER.name());
    
    // 6. Lưu xuống CSDL H2
    User savedUser = userRepository.save(u);
    return userMapper.toUserResponse(savedUser);
}
```

### 3.2. Phương thức Lấy Profile của tôi `getMyProfile()` (Dòng 115 - 128)
```java
public UserResponse getMyProfile() {
    // Lấy thông tin người dùng hiện tại từ SecurityContext (được trích xuất từ JWT Token)
    var context = SecurityContextHolder.getContext();
    String username = context.getAuthentication().getName();
    
    User user = userRepository.findByUsername(username)
            .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));
            
    UserResponse response = userMapper.toUserResponse(user);
    // Tính toán số lượng người theo dõi và số lượng người đang theo dõi
    response.setTotalFollowers(followService.countFollowers(user.getId()));
    response.setTotalFollowing(followService.countFollowing(user.getId()));
    return response;
}
```

---

## 📝 PHẦN 4: NGHIỆP VỤ BÀI VIẾT BLOG (`BlogService.java`)

File này nằm tại:  
📁 `src/main/java/com/group/blog/service/BlogService.java`

### 4.1. Đăng bài viết mới `createBlog()` (Dòng 44 - 76)
```java
@Transactional
public BlogResponse createBlog(BlogCreationRequest request) {
    // 1. Xác định tác giả chính là người đang đăng nhập qua Token
    var context = SecurityContextHolder.getContext();
    String currentUsername = context.getAuthentication().getName();
    User author = userRepository.findByUsername(currentUsername)
            .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));

    // 2. Kiểm tra và liên kết Danh mục (Category)
    Category category = null;
    if (request.getCategoryId() != null) {
        category = categoryRepository.findById(request.getCategoryId())
                .orElseThrow(() -> new AppException(ErrorCode.CATEGORY_NOT_FOUND));
    }

    Blog blog = blogMapper.toBlog(request);
    blog.setAuthor(author);
    blog.setCategory(category);

    // 3. Xử lý Thẻ tag: Tag nào có sẵn thì lấy, chưa có thì tự động tạo mới vào CSDL
    if (request.getTags() != null && !request.getTags().isEmpty()) {
        Set<Tag> finalTags = new HashSet<>();
        for (String tagName : request.getTags()) {
            Tag tag = tagRepository.findByName(tagName)
                    .orElseGet(() -> {
                        Tag newTag = new Tag();
                        newTag.setName(tagName);
                        return tagRepository.save(newTag);
                    });
            finalTags.add(tag);
        }
        blog.setTags(finalTags);
    }
    
    // 4. Lưu bài viết và làm giàu dữ liệu trả về (enrichBlogResponse)
    return enrichBlogResponse(blogRepository.save(blog));
}
```

---

## 📦 PHẦN 5: THỰC THỂ CƠ SỞ DỮ LIỆU JPA (`User.java` & `Blog.java`)

### 5.1. Entity `User.java` (Ánh xạ bảng `users`)
```java
@Entity
@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Table(name="users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.UUID) // Khóa chính dùng UUID tự sinh chống đoán số ID
    UUID id;

    @Column(nullable = false, unique = true, length = 100)
    String username;

    @Column(nullable = false, length = 255)
    String password; // Lưu chuỗi băm BCrypt dài 60 ký tự

    String email;
    String bio;
    String avatarUrl;
    LocalDateTime createdAt;

    // Bảng phụ lưu các vai trò (Role) của user (Quan hệ 1-Nhiều)
    @ElementCollection(fetch = FetchType.EAGER)
    @CollectionTable(name = "user_roles", joinColumns = @JoinColumn(name = "user_id"))
    @Column(name = "role")
    @Builder.Default
    Set<String> roles = new HashSet<>();

    // Quan hệ 1 tác giả có nhiều bài viết (1 - N)
    @OneToMany(mappedBy = "author", cascade = CascadeType.ALL)
    @Builder.Default
    List<Blog> blogs = new ArrayList<>();
}
```

### 5.2. Entity `Blog.java` (Ánh xạ bảng `blogs`)
```java
@Entity
@Table(name = "blogs")
public class Blog {
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    UUID id;

    @Column(nullable = false)
    String title;

    @Column(columnDefinition = "LONGTEXT") // Cho phép lưu nội dung bài viết không giới hạn độ dài
    String content;

    // Tác giả: Nhiều bài viết thuộc về Một tác giả (N - 1)
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "author_id", nullable = false)
    User author;

    // Danh mục: Nhiều bài viết thuộc về Một danh mục (N - 1)
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "category_id")
    Category category;

    // Thẻ tags: Nhiều bài viết có Nhiều tags (N - N) thông qua bảng trung gian blog_tags
    @ManyToMany
    @JoinTable(
        name = "blog_tags",
        joinColumns = @JoinColumn(name = "blog_id"),
        inverseJoinColumns = @JoinColumn(name = "tag_id")
    )
    Set<Tag> tags = new HashSet<>();
}
```

---

## 🌐 PHẦN 6: ĐIỀU HƯỚNG GIAO DIỆN (`ViewController.java`)

File này nằm tại:  
📁 `src/main/java/com/group/blog/controller/ViewController.java`

* **Mục đích**: Thay vì trả về JSON, Controller này trả về tên các file giao diện HTML Thymeleaf trong thư mục `src/main/resources/templates/`.

```java
@Controller
public class ViewController {
    // 1. Mở trang chủ
    @GetMapping({"/", "/home", "/home-page.html"})
    public String homePage() { return "public/home-page"; }

    // 2. Mở trang Đăng nhập & Đăng ký
    @GetMapping({"/login", "/login.html"})
    public String loginPage() { return "public/login"; }

    @GetMapping({"/register", "/register.html"})
    public String registerPage() { return "public/register"; }

    // 3. Mở các trang Quản trị viên (Admin)
    @GetMapping({"/admin", "/admin/dashboard"})
    public String adminDashboard() { return "admin/dashboard"; }

    @GetMapping("/admin/posts")
    public String adminPosts() { return "admin/posts"; }

    @GetMapping("/admin/users")
    public String adminUsers() { return "admin/users"; }

    @GetMapping("/admin/categories-tags")
    public String adminCategoriesTags() { return "admin/categories-tags"; }
}
```

---

## ⚡ PHẦN 7: TẦNG FRONTEND JAVASCRIPT & GIAO TIẾP VỚI BACKEND

### 7.1. File `register.html` — Logic xử lý Đăng ký & Tự động đăng nhập
```javascript
// 1. Bắt sự kiện submit form đăng ký
document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Chặn tải lại trang web mặc định

    const user = document.getElementById('username').value.trim();
    const pass = document.getElementById('password').value;
    const confirmPass = document.getElementById('confirmPassword').value;

    // Kiểm tra tính hợp lệ ở client
    if (user.length < 3) { showToast('Tên đăng nhập phải có ít nhất 3 ký tự!', 'warning'); return; }
    if (pass.length < 6) { showToast('Mật khẩu phải có ít nhất 6 ký tự!', 'warning'); return; }
    if (pass !== confirmPass) { showToast('Mật khẩu xác nhận không khớp. Vui lòng nhập lại!', 'warning'); return; }

    // 2. Gửi request đăng ký lên API Backend
    fetch('/users', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: user, password: pass })
    })
    .then(async response => ({ status: response.status, body: await response.json() }))
    .then(({ status, body }) => {
        if (status === 200 && body.code === 1000) {
            showToast('Tạo tài khoản thành công! Đang tự động đăng nhập...', 'success');
            autoLogin(user, pass); // Tự động gọi hàm đăng nhập ngầm
        } else {
            // Hiển thị lỗi tiếng Việt nếu tài khoản đã tồn tại
            let msg = (body.message === 'User Exited') ? 'Tên đăng nhập đã tồn tại!' : body.message;
            showToast('Đăng ký thất bại: ' + msg, 'danger');
        }
    });
});

// 3. Tự động đăng nhập lấy Token và lưu vào localStorage
function autoLogin(username, password) {
    fetch('/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(async response => ({ status: response.status, body: await response.json() }))
    .then(({ status, body }) => {
        if (status === 200 && body.code === 1000) {
            localStorage.setItem('token', body.result.token); // Lưu token
            localStorage.setItem('username', username);
            setTimeout(() => { window.location.href = "/"; }, 600); // Chuyển về trang chủ
        }
    });
}
```

### 7.2. File `nav.js` — Phân quyền hiển thị Menu Admin trên Navbar
```javascript
// Trích xuất Token từ localStorage để kiểm tra quyền hạn
const token = localStorage.getItem('token');
if (token) {
    try {
        // Giải mã phần thân (Payload) của JWT Base64
        const base64Url = token.split('.')[1];
        const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
        const payload = JSON.parse(window.atob(base64));

        // Kiểm tra xem trong scope có chứa chữ ADMIN hay không
        const roles = payload.scope || "";
        if (roles.includes("ADMIN")) {
            $('#btn-desk-admin').show(); // Nếu là Admin -> Hiển thị nút "Admin Controller"
        } else {
            $('#btn-desk-admin').hide(); // Nếu là User thường -> Ẩn nút Admin
        }
    } catch (e) {
        console.error("Lỗi giải mã token:", e);
    }
}
```

---

## 🎯 PHẦN 8: BỘ CÂU HỎI "BẢO BỐI" VẤN ĐÁP CỦA GIẢNG VIÊN (KÈM CÂU TRẢ LỜI MẪU)

### ❓ Câu 1: "Tại sao nhóm chọn cơ chế xác thực JWT mà không dùng Session Cookie truyền thống?"
* **Trả lời**:  
  *"Dạ thưa Thầy/Cô, JWT có tính chất **Stateless (phi trạng thái)**. Khi người dùng đăng nhập, Server ký và sinh ra chuỗi Token gửi về cho Client lưu tại `localStorage`. Mỗi request sau đó Client tự đính kèm Token vào Header `Authorization`. Server chỉ cần kiểm tra chữ ký số bằng mã bí mật mà **không cần lưu giữ Session trên RAM máy chủ**. Điều này giúp ứng dụng hoạt động rất nhẹ, dễ dàng mở rộng và phân tán sau này."*

---

### ❓ Câu 2: "Mật khẩu của người dùng được lưu trong CSDL như thế nào? Nếu lộ CSDL thì hacker có đọc được mật khẩu không?"
* **Trả lời**:  
  *"Dạ thưa Thầy/Cô, mật khẩu được băm bằng thuật toán **BCrypt** (thuộc class `BCryptPasswordEncoder`) với độ khó 10 (`salt rounds`). Đây là thuật toán **băm một chiều kèm chuỗi ngẫu nhiên (salt)**. Cho dù hacker có chiếm được toàn bộ CSDL thì cũng không thể giải mã ngược lại ra mật khẩu gốc ban đầu của người dùng."*

---

### ❓ Câu 3: "Dữ liệu được lưu trữ ở đâu? Tại sao khi tắt server khởi động lại thì dữ liệu không bị mất?"
* **Trả lời**:  
  *"Dạ, nhóm cấu hình CSDL **H2 Database dạng File** với chuỗi kết nối:  
  `jdbc:h2:file:./data/blogdb;AUTO_SERVER=TRUE;MODE=MySQL;...`  
  Mọi thao tác thêm/sửa/xóa đều được Hibernate ghi vĩnh viễn vào file nhị phân `data/blogdb.mv.db` trên ổ cứng. Do đó khi tắt ứng dụng hoặc khởi động lại máy, dữ liệu vẫn được bảo toàn nguyên vẹn 100%."*

---

### ❓ Câu 4: "Làm sao Backend biết được bài viết mới tạo là của ai khi không thấy truyền ID tác giả trong Request Body?"
* **Trả lời**:  
  *"Dạ thưa Thầy/Cô, để đảm bảo tính an toàn, nhóm không để Client tự ý truyền `authorId` lên. Thay vào đó, trong hàm `createBlog()` của `BlogService`, nhóm lấy trực tiếp username từ ngữ cảnh bảo mật của Spring Security:  
  `String currentUsername = SecurityContextHolder.getContext().getAuthentication().getName();`  
  Username này được trích xuất hoàn toàn tự động từ chuỗi Token JWT đã được kiểm thực ở tầng lọc `SecurityFilterChain`, ngăn chặn triệt để hành vi giả mạo tác giả."*

---

### ❓ Câu 5: "Giải thích các Annotation của Lombok như `@Builder`, `@RequiredArgsConstructor`, `@FieldDefaults`?"
* **Trả lời**:  
  * `@Builder`: Giúp khởi tạo đối tượng nhanh chóng theo mẫu thiết kế Builder Pattern (ví dụ: `User.builder().username("...").build()`).
  * `@RequiredArgsConstructor`: Tự động tạo Constructor cho tất cả các biến có từ khóa `final` (được dùng để **Dependency Injection** thay cho `@Autowired` theo khuyến nghị mới của Spring).
  * `@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)`: Tự động biến tất cả các thuộc tính trong class thành `private final`, giúp code ngắn gọn, sạch sẽ và an toàn.
