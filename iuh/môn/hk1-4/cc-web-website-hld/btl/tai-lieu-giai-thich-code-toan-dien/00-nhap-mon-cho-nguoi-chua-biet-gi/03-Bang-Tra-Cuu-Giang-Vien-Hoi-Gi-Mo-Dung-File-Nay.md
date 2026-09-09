# BẢNG TRA CỨU NHANH TRONG PHÒNG THI VẤN ĐÁP
### GIẢNG VIÊN HỎI GÌ ➔ MỞ ĐÚNG FILE NÀO ➔ DÒNG BAO NHIÊU ➔ NÓI CÂU THOẠI GÌ

> **Cứu cánh số 1 cho người mới:** Khi ngồi trước mặt giảng viên, nếu bị hỏi bất ngờ: *"Em mở cho thầy/cô xem chỗ làm chức năng X"*, bạn chỉ cần mở file này ra tra cứu trong 3 giây.  
> Biết chính xác tên file, số dòng, và có sẵn câu thoại mẫu giải thích tự tin!

---

## ⚡ 1. KỸ NĂNG "MỞ FILE TRONG 1 GIÂY" TRÊN INTELLIJ IDEA

Đừng dùng chuột bấm từng thư mục mò mẫm, giảng viên nhìn vào sẽ biết ngay là không thạo code! Hãy dùng phím tắt chuyên nghiệp:

1. **Nhấn 2 lần phím Shift (Double Shift)** hoặc tổ hợp phím **`Ctrl + Shift + N`**:
   - Hiện lên thanh tìm kiếm toàn dự án.
   - Gõ tên file (ví dụ: `BlogService` hoặc `SecurityConfig`), nhấn **Enter** là file mở ra ngay lập tức!
2. **Nhảy đến đúng số dòng (`Ctrl + G`)**:
   - Gõ số dòng (ví dụ: `55`), nhấn **Enter** là con trỏ chuột nhảy thẳng đến dòng đó!
3. **Tìm chữ trong file (`Ctrl + F`)**:
   - Gõ từ khóa hàm (ví dụ: `generateToken` hoặc `toggleLike`).

---

## 📑 2. BẢNG VÀNG TRA CỨU TỪNG CÂU HỎI VẤN ĐÁP

| STT | Giảng Viên Hỏi | Mở File Nào? | Dòng Số | Câu Thoại Chuẩn Để Nói Với Giảng Viên |
| :---: | :--- | :--- | :---: | :--- |
| **1** | *"Chỗ nào mã hóa / băm mật khẩu người dùng?"* | [`UserService.java`](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/btl/blog-website-main/src/main/java/com/group/blog/service/UserService.java) | **Dòng 42** | *"Dạ đây ạ, em dùng `passwordEncoder.encode(request.getPassword())`. Đây là thuật toán băm một chiều BCrypt với độ muối mặc định 10 vòng, đảm bảo không thể giải mã ngược."* |
| **2** | *"Chỗ nào sinh ra chuỗi Token JWT lúc đăng nhập?"* | [`AuthenticationService.java`](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/btl/blog-website-main/src/main/java/com/group/blog/service/AuthenticationService.java) | **Dòng 55** | *"Dạ tại phương thức `generateToken()`, em dùng thư viện Nimbus JOSE JWT. Header dùng thuật toán `HS512`, Payload chứa username và vai trò, ký bằng khóa bí mật `SIGNER_KEY` lấy từ file yaml."* |
| **3** | *"Chỗ nào kiểm tra xem Token gửi lên có hợp lệ không?"* | [`AuthenticationService.java`](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/btl/blog-website-main/src/main/java/com/group/blog/service/AuthenticationService.java) | **Dòng 83** | *"Dạ phương thức `introspect()`. Em dùng `MACVerifier` kiểm tra con dấu chữ ký và so sánh thời gian hết hạn `expiryTime.after(new Date())`."* |
| **4** | *"Chỗ nào cấu hình phân quyền Admin và bảo vệ các đường link?"* | [`SecurityConfig.java`](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/btl/blog-website-main/src/main/java/com/group/blog/configuration/SecurityConfig.java) | **Dòng 38-45** | *"Dạ tại bean `SecurityFilterChain`. Các route `/auth/**`, `/home` được `permitAll()`, còn route `/admin/**` và `/api/admin/**` bắt buộc phải có quyền `hasRole('ADMIN')`."* |
| **5** | *"Tại sao trong Token là chữ ADMIN mà trong Security lại hiểu là ROLE_ADMIN?"* | [`SecurityConfig.java`](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/btl/blog-website-main/src/main/java/com/group/blog/configuration/SecurityConfig.java) | **Dòng 68-76** | *"Dạ em có viết một bean `jwtAuthenticationConverter()`. Em dùng `setAuthorityPrefix("ROLE_")` để tự động nối thêm tiền tố `ROLE_` trước mỗi quyền của người dùng."* |
| **6** | *"Chỗ nào tải ảnh lên Cloudinary?"* | [`CloudinaryService.java`](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/btl/blog-website-main/src/main/java/com/group/blog/service/CloudinaryService.java) | **Dòng 17** | *"Dạ phương thức `uploadImage(MultipartFile file)`. Em đẩy luồng byte sang Cloudinary API bằng `cloudinary.uploader().upload(file.getBytes(), ...)` và nhận về đường dẫn an toàn `secure_url`."* |
| **7** | *"Chỗ nào tự động sinh dữ liệu mẫu lúc khởi động server?"* | [`ApplicationInitConfig.java`](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/btl/blog-website-main/src/main/java/com/group/blog/configuration/ApplicationInitConfig.java) | **Dòng 34** | *"Dạ đây là bean `ApplicationRunner`. Khi server Spring Boot vừa nổ máy, nó kiểm tra nếu chưa có tài khoản admin thì tự động seed tài khoản admin, tài khoản của 3 thành viên trong nhóm và các danh mục mẫu."* |
| **8** | *"Chỗ nào chuyển đổi tiêu đề tiếng Việt có dấu thành Slug không dấu?"* | [`SlugUtils.java`](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/btl/blog-website-main/src/main/java/com/group/blog/util/SlugUtils.java) | **Dòng 14** | *"Dạ phương thức `toSlug()`. Em dùng `Normalizer.normalize(Form.NFD)` để tách dấu ra khỏi chữ cái, thay thế chữ Đ/đ, xóa ký tự đặc biệt bằng Regex và nối các từ bằng dấu gạch ngang chuẩn SEO."* |
| **9** | *"Chỗ nào bắt lỗi tập trung để không bị văng lỗi 500 ra ngoài?"* | [`GlobalExceptionHandler.java`](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/btl/blog-website-main/src/main/java/com/group/blog/exception/GlobalExceptionHandler.java) | **Dòng 18-35** | *"Dạ class này được gắn chú thích `@ControllerAdvice`. Bất cứ khi nào Service ném ra `AppException`, hàm `handlingAppException` sẽ đón bắt và đóng gói thành đối tượng `ApiResponse` chứa `ErrorCode` chuẩn mực."* |
| **10** | *"Chỗ nào xử lý nút Bật/Tắt Thả Tim (Like)?"* | [`InteractionService.java`](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/btl/blog-website-main/src/main/java/com/group/blog/service/InteractionService.java) | **Dòng 43** | *"Dạ phương thức `toggleLike(UUID blogId)`. Em kiểm tra xem bản ghi đã có trong bảng `blog_likes` chưa: nếu có rồi thì gọi `.delete()` (bỏ like), nếu chưa thì gọi `.save()` (thả tim) và gửi thông báo cho tác giả."* |
| **11** | *"Chỗ nào xử lý logic cây bình luận đa tầng (Reply lồng nhau)?"* | [`InteractionService.java`](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/btl/blog-website-main/src/main/java/com/group/blog/service/InteractionService.java) | **Dòng 79** | *"Dạ phương thức `addComment()`. Nếu người dùng reply bình luận khác thì `request.getParentId()` sẽ có giá trị. Hệ thống tìm bình luận cha và gán `comment.setParent(parentComment)`."* |
| **12** | *"Chỗ nào kiểm tra quyền xóa bình luận (Ai có quyền xóa)?"* | [`InteractionService.java`](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/btl/blog-website-main/src/main/java/com/group/blog/service/InteractionService.java) | **Dòng 131** | *"Dạ tại `deleteComment()`. Em kiểm tra người đang đăng nhập có phải là: 1. Người viết bình luận, 2. Tác giả của bài viết, hoặc 3. Quản trị viên Admin. Nếu không phải cả 3 thì ném lỗi 403 Forbidden."* |
| **13** | *"Chỗ nào ngăn không cho người dùng tự Follow chính mình?"* | [`FollowService.java`](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/btl/blog-website-main/src/main/java/com/group/blog/service/FollowService.java) | **Dòng 40** | *"Dạ dòng này: `if (currentUser.getId().equals(targetUser.getId())) throw new AppException(ErrorCode.CANNOT_FOLLOW_YOURSELF);` để chống gian lận tự tăng follower."* |
| **14** | *"Chỗ nào xử lý đếm lượt xem (Views) khi đọc bài?"* | [`BlogService.java`](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/btl/blog-website-main/src/main/java/com/group/blog/service/BlogService.java) | **Dòng 160** | *"Dạ tại `getBlogById()`. Em lấy IP và User-Agent của khách, ghi nhận vào bảng `blog_views`. Sau đó gọi câu truy vấn tăng số lượng view của bài viết lên 1."* |
| **15** | *"Chỗ nào xử lý Lưu bài nháp (Draft) và Xuất bản (Publish)?"* | [`BlogService.java`](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/btl/blog-website-main/src/main/java/com/group/blog/service/BlogService.java) | **Dòng 45-65** | *"Dạ trường boolean `request.isDraft()`. Nếu là `true`, bài viết được lưu với cờ draft để chỉ mình tác giả nhìn thấy. Nếu là `false`, bài được xuất bản công khai ra trang chủ."* |
| **16** | *"Chỗ nào xử lý đổi mật khẩu an toàn 5 bước?"* | [`UserService.java`](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/btl/blog-website-main/src/main/java/com/group/blog/service/UserService.java) | **Dòng 80** | *"Dạ tại `changePassword()`. Em kiểm tra: 1. Mật khẩu cũ có đúng không, 2. Mật khẩu mới có trùng mật khẩu cũ không, 3. Mật khẩu xác nhận có khớp không, 4. Băm mật khẩu mới bằng BCrypt và lưu lại."* |
| **17** | *"Chỗ nào cấu hình đường dẫn file CSDL H2 bền vững?"* | [`application.yaml`](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/btl/blog-website-main/src/main/resources/application.yaml) | **Dòng 15** | *"Dạ dòng `url: jdbc:h2:file:./data/blogdb;AUTO_SERVER=TRUE;MODE=MySQL`. Nhờ có `file:./data` nên khi tắt server dữ liệu không bao giờ bị mất, và `AUTO_SERVER=TRUE` cho phép mở H2 Console xem trực tiếp."* |
| **18** | *"Chỗ nào gọi API tập trung ở tầng Frontend?"* | [`app.js`](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/btl/blog-website-main/src/main/resources/static/assets/js/app.js) | **Dòng 85** | *"Dạ hàm `callApi(endpoint, method, data)`. Hàm này tự động lấy Token từ `localStorage.getItem('token')`, gắn vào Header `Authorization: Bearer <token>` trước khi gửi đi qua jQuery AJAX."* |
| **19** | *"Chỗ nào bóc tách văn bản từ Editor.js để hiển thị mô tả ngắn?"* | [`app.js`](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/btl/blog-website-main/src/main/resources/static/assets/js/app.js) | **Dòng 27** | *"Dạ hàm `excerpt()`. Nó parse chuỗi JSON của Editor.js, lọc ra các khối `paragraph`, dùng Regex `replace(/<[^>]*>/g, '')` xóa sạch các thẻ HTML và cắt lấy 200 ký tự đầu tiên."* |
| **20** | *"Chỗ nào điều hướng các trang HTML bằng Thymeleaf?"* | [`ViewController.java`](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/btl/blog-website-main/src/main/java/com/group/blog/controller/ViewController.java) | **Dòng 10-104** | *"Dạ class `ViewController` được gắn `@Controller`. Nó trả về các chuỗi view như `"public/home-page"`, `"admin/dashboard"`, được Thymeleaf View Resolver phân giải thành các file HTML trong thư mục `templates/`."* |

---

> 💡 **LỜI KHUYÊN KHI TRẢ LỜI:**  
> - Luôn mở đầu bằng: *"Dạ thưa thầy/cô, phần này nằm ở file..."*.  
> - Bấm phím tắt mở file thật nhanh, đưa ngón tay chỉ vào đúng dòng code.  
> - Đọc 1-2 câu giải thích ngắn gọn như trong bảng trên.  
> Đảm bảo giảng viên sẽ gật đầu hài lòng ngay lập tức vì phong thái đĩnh đạc, nắm chắc mã nguồn!
