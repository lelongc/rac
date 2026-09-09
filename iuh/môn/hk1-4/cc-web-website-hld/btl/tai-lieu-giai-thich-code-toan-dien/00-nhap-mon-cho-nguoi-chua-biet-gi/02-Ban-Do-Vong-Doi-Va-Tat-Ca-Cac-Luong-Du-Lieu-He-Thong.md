# BẢN ĐỒ VÒNG ĐỜI & TOÀN BỘ CÁC LUỒNG DỮ LIỆU HỆ THỐNG (DATA FLOWCHART)

> **Dành cho:** Bất kỳ ai cần giải thích trọn vẹn luồng đi của dữ liệu từ khi bấm chuột trên màn hình, đi qua các tầng mạng, tầng bảo mật, tầng mã nguồn Java, tầng CSDL và quay trở lại màn hình.  
> **Cấu trúc:** 7 sơ đồ tuần tự trực quan (Sequence Diagrams) bằng Mermaid kèm phân tích chi tiết từng bước.

---

## 🌊 1. TỔNG QUAN VÒNG ĐỜI MỘT YÊU CẦU TRONG MÔ HÌNH 3 LỚP

Mọi hành động trên website Bleb Blog đều tuân thủ chặt chẽ theo dòng chảy 6 trạm sau:

```
[Trình duyệt Web (HTML/JS)]
         │  1. Gửi HTTP Request (kèm dữ liệu JSON hoặc Bearer Token)
         ▼
[Spring Security Filter Chain] ──> Kiểm tra Token JWT hợp lệ hay không?
         │  2. Cho phép đi tiếp nếu hợp lệ
         ▼
[Controller Layer]            ──> Đón nhận URL, hứng RequestBody, bắt lỗi @Valid
         │  3. Chuyển dữ liệu DTO
         ▼
[Service Layer]               ──> Xử lý logic nghiệp vụ, tính toán, mã hóa, gọi dịch vụ ngoài
         │  4. Gọi lệnh truy vấn
         ▼
[Repository Layer (JPA)]      ──> Sinh câu lệnh SQL tương tác với CSDL
         │  5. Đọc/Ghi dữ liệu
         ▼
[Database (H2 / MySQL)]
```

---

## 🔐 2. LUỒNG 1: ĐĂNG KÝ TÀI KHOẢN MỚI (USER REGISTRATION FLOW)

### Kịch bản:
Người dùng mở modal Đăng ký (`#modal-auth`), nhập `username`, `password`, `email`, `fullName` và bấm nút **"Create Account"**.

### Sơ đồ tuần tự:
```mermaid
sequenceDiagram
    autonumber
    actor U as Người dùng
    participant FE as auth.js / callApi()
    participant SEC as SecurityFilterChain
    participant C as UserController
    participant S as UserService
    participant R as UserRepository
    participant DB as CSDL (bảng users)

    U->>FE: Điền form & Bấm "Create Account"
    FE->>SEC: POST /users (Body: JSON UserCreatetionRequest)
    Note over SEC: Endpoint /users được permitAll() trong SecurityConfig
    SEC->>C: Chuyển tiếp Request vào controller
    Note over C: @Valid kiểm tra @Size(min=4) username, @Size(min=8) password
    C->>S: Gọi userService.createUser(request)
    S->>R: Kiểm tra trùng: userRepository.existsByUsername(username)
    alt Username đã tồn tại
        R-->>S: Trả về true
        S-->>C: Ném lỗi AppException(ErrorCode.USER_EXISTED)
        C-->>FE: Trả về HTTP 400 kèm mã lỗi USER_EXISTED
        FE-->>U: Hiển thị Toast đỏ: "Tên đăng nhập đã tồn tại!"
    else Username hợp lệ
        R-->>S: Trả về false
        S->>S: Băm mật khẩu: passwordEncoder.encode(rawPassword)
        S->>S: Gán quyền mặc định: roles.add(Role.USER.name())
        S->>R: Lưu entity: userRepository.save(user)
        R->>DB: INSERT INTO users ... & user_roles ...
        DB-->>R: Ghi đĩa thành công
        R-->>S: Trả về User Entity đã có UUID
        S->>S: MapStruct chuyển User sang UserResponse (giấu mật khẩu)
        S-->>C: Trả về UserResponse
        C-->>FE: Trả về HTTP 200 ApiResponse<UserResponse>
        FE-->>U: Tự động điền username sang form đăng nhập & Toast: "Đăng ký thành công!"
    end
```

---

## 🔑 3. LUỒNG 2: ĐĂNG NHẬP & CẤP PHÁT JWT TOKEN (LOGIN FLOW)

### Kịch bản:
Người dùng nhập tên đăng nhập, mật khẩu và bấm nút **"Sign In"**.

### Sơ đồ tuần tự:
```mermaid
sequenceDiagram
    autonumber
    actor U as Người dùng
    participant FE as auth.js
    participant C as AuthenticationController
    participant S as AuthenticationService
    participant R as UserRepository
    participant ENC as PasswordEncoder (BCrypt)
    participant JWT as Nimbus JWT Signer

    U->>FE: Bấm "Sign In"
    FE->>C: POST /auth/token (Body: {username, password})
    C->>S: Gọi authenticationService.authenticate(request)
    S->>R: userRepository.findByUsername(username)
    alt Không tìm thấy tài khoản
        R-->>S: Optional.empty()
        S-->>C: Ném lỗi AppException(ErrorCode.USER_NOT_EXITED)
        C-->>FE: HTTP 400 "Người dùng không tồn tại"
    else Tìm thấy tài khoản
        R-->>S: Trả về User Entity (kèm mật khẩu đã băm trong DB)
        S->>ENC: passwordEncoder.matches(nhập_vào, trong_CSDL)
        alt Sai mật khẩu
            ENC-->>S: false
            S-->>C: Ném lỗi AppException(ErrorCode.UNAUTHENTICATED)
            C-->>FE: HTTP 400 "Tài khoản hoặc mật khẩu không chính xác"
        else Mật khẩu khớp 100%
            ENC-->>S: true
            S->>JWT: Tạo Token (Header HS512, Payload: sub, scope, exp = +1h, SignerKey)
            JWT-->>S: Chuỗi Token xxxxx.yyyyy.zzzzz
            S-->>C: Trả về AuthenticationResponse(token, authenticated=true)
            C-->>FE: HTTP 200 { result: { token: "xxxxx..." } }
            FE->>FE: Lưu token vào localStorage.setItem('token', token)
            FE->>FE: Lưu username vào localStorage.setItem('username', user)
            FE->>FE: Cập nhật giao diện Navbar (Ẩn nút Sign In, Hiện Avatar & Nút Viết bài)
            FE-->>U: Toast: "Chào mừng bạn quay trở lại!"
        end
    end
```

---

## ☁️ 4. LUỒNG 3: TẢI ẢNH BÌA LÊN CLOUDINARY (IMAGE UPLOAD FLOW)

### Kịch bản:
Trong trang `blog-editor.html`, tác giả bấm vào khung ảnh bìa và chọn file ảnh `.png` hoặc `.jpg` từ máy tính.

### Sơ đồ tuần tự:
```mermaid
sequenceDiagram
    autonumber
    actor U as Tác giả
    participant FE as blog-editor.html (AJAX)
    participant SEC as SecurityFilterChain (Kiểm tra Bearer Token)
    participant C as UploadController
    participant S as CloudinaryService
    participant CLOUD as Máy chủ Cloudinary (USA)

    U->>FE: Chọn file ảnh từ máy tính (banner.jpg)
    FE->>FE: Đóng gói vào FormData (file, contentType: false)
    FE->>SEC: POST /api/upload (Header: Authorization Bearer <token>)
    SEC->>C: Token hợp lệ ➔ Chuyển vào uploadController.uploadImage(file)
    C->>S: Gọi cloudinaryService.uploadImage(multipartFile)
    S->>S: Lấy byte[] và tham số: ObjectUtils.asMap("resource_type", "auto")
    S->>CLOUD: Đẩy luồng byte qua kết nối bảo mật HTTPS API
    CLOUD->>CLOUD: Tối ưu hóa dung lượng (WebP), lưu trữ CDN phân tán
    CLOUD-->>S: Trả về Map kết quả (chứa key "secure_url": "https://res.cloudinary.com/...")
    S-->>C: Trả về chuỗi URL HTTPS
    C-->>FE: HTTP 200 { result: { url: "https://res.cloudinary.com/..." } }
    FE->>FE: Gán URL vào thuộc tính src của thẻ <img>
    FE-->>U: Hiển thị ngay ảnh bìa sắc nét lên trình soạn thảo trong 1 giây!
```

---

## ✍️ 5. LUỒNG 4: TẠO & XUẤT BẢN BÀI VIẾT (CREATE BLOG & SLUG FLOW)

### Kịch bản:
Tác giả viết xong bài, gắn danh mục, thẻ tag và bấm nút **"Publish"**.

### Sơ đồ tuần tự:
```mermaid
sequenceDiagram
    autonumber
    actor U as Tác giả
    participant FE as blog-editor.html
    participant C as BlogController
    participant S as BlogService
    participant SEC_CTX as SecurityContextHolder
    participant SLUG as SlugUtils
    participant R as BlogRepository, TagRepo, CatRepo
    participant DB as CSDL

    U->>FE: Bấm nút "Publish"
    FE->>FE: Đóng gói JSON (title, content, banner, categoryId, tagNames, draft: false)
    FE->>C: POST /blogs (Kèm Bearer Token)
    C->>S: blogService.createBlog(request)
    S->>SEC_CTX: Lấy thông tin người đăng: SecurityContextHolder.getContext().getAuthentication().getName()
    SEC_CTX-->>S: Username của tác giả đang đăng nhập
    S->>SLUG: Sinh slug: SlugUtils.toSlug(title) + "-" + UUID.randomUUID()
    SLUG-->>S: Chuỗi slug: "hoc-spring-boot-co-ban-3f7b9c12-88a4-4a55..."
    S->>R: Tìm Category theo ID, Tìm hoặc tạo mới các Tag theo tagNames
    R-->>S: Category Entity & Set<Tag> Entities
    S->>S: Khởi tạo Blog Entity (gắn Author, Category, Tags, Slug, Draft=false)
    S->>R: blogRepository.save(blog)
    R->>DB: INSERT INTO blogs ... & blog_tags ...
    DB-->>R: Ghi CSDL thành công
    R-->>S: Trả về Blog Entity hoàn chỉnh
    S->>S: enrichBlogResponse() (Gán số like=0, số comment=0, isLiked=false)
    S-->>C: Trả về BlogResponse
    C-->>FE: HTTP 200 OK
    FE-->>U: Toast: "Xuất bản bài viết thành công!" ➔ Chuyển hướng về Manage-Blogs.html
```

---

## 📖 6. LUỒNG 5: ĐỌC BÀI VIẾT, TĂNG VIEW & BÌNH LUẬN ĐA CẤP (POST DETAIL & COMMENTS)

### Kịch bản:
Độc giả bấm vào xem bài viết tại đường dẫn `post.html?id=slug-cua-bai-viet`.

### Sơ đồ tuần tự:
```mermaid
sequenceDiagram
    autonumber
    actor U as Độc giả
    participant FE as post.html
    participant BC as BlogController
    participant BS as BlogService
    participant IC as InteractionController
    participant IS as InteractionService
    participant DB as CSDL

    U->>FE: Truy cập bài viết qua URL
    FE->>FE: extractIdFromSlug(slug) ➔ Cắt 36 ký tự cuối lấy blogId
    par Tải chi tiết bài viết & Tăng lượt xem
        FE->>BC: GET /blogs/{blogId}
        BC->>BS: blogService.getBlogById(blogId)
        BS->>DB: INSERT INTO blog_views (IP, UserAgent, BlogId) (Chống spam view)
        BS->>DB: UPDATE blogs SET views = views + 1
        BS-->>BC: Trả về dữ liệu bài viết (title, JSON content, author, views...)
        BC-->>FE: Render các khối Editor.js (h1, p, image, code)
    and Tải cây bình luận
        FE->>IC: GET /blogs/{blogId}/comments
        IC->>IS: interactionService.getCommentsByBlogId(blogId)
        IS->>DB: SELECT * FROM comments WHERE blog_id = :id ORDER BY created_at ASC
        DB-->>IS: Danh sách bình luận
        IS->>IS: Phân loại: parentId == null (Gốc) và parentId != null (Câu trả lời)
        IS-->>IC: Trả về List<CommentResponse>
        IC-->>FE: Hiển thị giao diện Cây bình luận đa tầng có thụt lề
    end
```

---

## ❤️ 7. LUỒNG 6: THẢ TIM (LIKE) & BẮN THÔNG BÁO (NOTIFICATION FLOW)

### Kịch bản:
Người dùng bấm vào nút Trái tim (`#btn-like`) dưới bài viết.

### Sơ đồ tuần tự:
```mermaid
sequenceDiagram
    autonumber
    actor U as Người dùng (Alice)
    participant FE as post.html
    participant C as InteractionController
    participant S as InteractionService
    participant NS as NotificationService
    participant R as BlogLikeRepository
    participant DB as CSDL
    actor A as Tác giả bài viết (Bob)

    U->>FE: Bấm biểu tượng Trái tim
    FE->>C: POST /blogs/{blogId}/like (Kèm Token Alice)
    C->>S: interactionService.toggleLike(blogId)
    S->>S: Lấy username Alice từ SecurityContextHolder
    S->>R: blogLikeRepository.findByUserAndBlog(Alice, Blog)
    alt Alice đã thích bài viết này từ trước
        R-->>S: Trả về bản ghi BlogLike đã có
        S->>R: blogLikeRepository.delete(like) ➔ Xóa khỏi CSDL
        R->>DB: DELETE FROM blog_likes WHERE id = ...
        S-->>C: Trả về false (Đã bỏ thích)
        C-->>FE: HTTP 200 { result: false }
        FE->>FE: Đổi tim đỏ sang tim rỗng, giảm số like -1
        FE-->>U: Toast: "Đã bỏ thích bài viết."
    else Alice chưa từng thích bài này
        R-->>S: Trả về null
        S->>R: blogLikeRepository.save(new BlogLike(Alice, Blog))
        R->>DB: INSERT INTO blog_likes ...
        opt Alice không phải là tác giả bài viết
            S->>NS: Gửi thông báo cho Bob: "@Alice đã thích bài viết của bạn"
            NS->>DB: INSERT INTO notifications (recipient_id = Bob, actor_id = Alice, type = 'LIKE')
            Note over A: Khi Bob mở notifications.html sẽ thấy chuông báo màu tím!
        end
        S-->>C: Trả về true (Đã thích thành công)
        C-->>FE: HTTP 200 { result: true }
        FE->>FE: Đổi tim rỗng sang tim đỏ phát sáng, tăng số like +1
        FE-->>U: Toast: "Đã thích bài viết!"
    end
```

---

## 👑 8. LUỒNG 7: ADMIN PHÂN QUYỀN & KIỂM DUYỆT (ADMIN MANAGEMENT FLOW)

### Kịch bản:
Quản trị viên vào trang `admin/users.html` bấm nút **"Thăng cấp ADMIN"** cho một tài khoản.

### Sơ đồ tuần tự:
```mermaid
sequenceDiagram
    autonumber
    actor AD as Quản trị viên
    participant FE as admin/users.html
    participant SEC as SecurityFilterChain (@PreAuthorize hasRole ADMIN)
    participant C as UserController
    participant S as UserService
    participant DB as CSDL

    AD->>FE: Bấm nút "Thăng cấp ADMIN" cho user "dungnt"
    FE->>SEC: PUT /users/{userId} (Header: Bearer <token_cua_admin>, Body: roles=['ADMIN'])
    Note over SEC: Giải mã JWT: Kiểm tra scope có chứa "ROLE_ADMIN" không?
    alt Token không có ROLE_ADMIN
        SEC-->>FE: HTTP 403 Forbidden
        FE-->>AD: Alert: "Bạn không có quyền quản trị viên!"
    else Token có ROLE_ADMIN hợp lệ
        SEC->>C: Chuyển tiếp vào userController.updateUser()
        C->>S: userService.updateUser(userId, request)
        S->>DB: Cập nhật bảng user_roles thêm dòng (user_id, 'ADMIN')
        DB-->>S: Cập nhật thành công
        S-->>C: Trả về UserResponse có Role mới
        C-->>FE: HTTP 200 OK
        FE->>FE: Đổi nhãn xám USER thành nhãn tím ADMIN
        FE-->>AD: Toast: "Cập nhật quyền thành công!"
    end
```

---

> 🎯 **BÍ QUYẾT KHI ĐI THI VẤN ĐÁP:**  
> Nếu thầy cô hỏi: *"Hãy trình bày cho tôi luồng chạy của chức năng X"*, bạn chỉ cần vẽ nhanh hoặc nói theo 5 bước:  
> 1. **Client (Giao diện):** Người dùng bấm cái gì, JavaScript gọi hàm `callApi()` gửi method gì (GET/POST/PUT/DELETE) lên URL nào.
> 2. **Bảo mật:** `SecurityFilterChain` kiểm tra Bearer Token ra sao.
> 3. **Controller:** Hứng dữ liệu ở hàm nào, kiểm tra `@Valid` cái gì.
> 4. **Service:** Xử lý logic gì (kiểm tra trùng, băm mật khẩu, tạo thông báo).
> 5. **Repository & CSDL:** Lưu vào bảng nào và trả dữ liệu ngược lại ra sao.  
> Trả lời đủ 5 bước này thì không một giảng viên nào có thể trừ điểm của bạn!
