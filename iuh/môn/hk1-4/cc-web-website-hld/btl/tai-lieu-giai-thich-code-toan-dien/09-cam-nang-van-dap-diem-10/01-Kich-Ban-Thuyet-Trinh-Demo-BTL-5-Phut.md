# KỊCH BẢN THUYẾT TRÌNH VÀ DEMO BÀI TẬP LỚN (CHUẨN 5 PHÚT ĂN TRỌN ĐIỂM 10)

> **Mục tiêu**: Giúp các thành viên trong nhóm phối hợp nhịp nhàng, trình diễn các tính năng ấn tượng nhất của dự án một cách tự tin, chuyên nghiệp trước hội đồng chấm thi của Trường Đại học Công nghiệp TP.HCM (IUH).

---

## 1. PHÂN CÔNG VÀ CHUẨN BỊ TRƯỚC KHI LÊN BẢNG

- **Thành viên nhóm**:
  1. Hoàng Đại Dương (MSSV: 24743991)
  2. Nguyễn Trung Dũng (MSSV: 24000905)
  3. Lê Thành Long (MSSV: 23630851)
- **Chuẩn bị kỹ thuật**:
  - Khởi động ứng dụng Spring Boot bằng lệnh `mvn spring-boot:run` (Đảm bảo Console báo `Started BlogWebsiteApplication in X seconds` tại cổng `8080`).
  - Mở sẵn 2 trình duyệt:
    - Trình duyệt 1 (Chrome): Dùng để demo tài khoản thành viên (`duonghd` / `123456`).
    - Trình duyệt 2 (Edge hoặc Tab ẩn danh): Dùng để demo tài khoản Quản trị viên (`admin` / `123456`) hoặc tài khoản tác giả khác (`dungnt`).

---

## 2. KỊCH BẢN 5 BƯỚC DEMO TRỰC TIẾP (5-MINUTE LIVE DEMO)

### BƯỚC 1: GIỚI THIỆU TỔNG QUAN VÀ TRANG CHỦ (0:00 - 1:00)
- **Lời thoại của sinh viên**:
  > *"Kính thưa quý Thầy/Cô trong hội đồng, hôm nay nhóm chúng em xin phép báo cáo Bài tập lớn môn Công nghệ Web: Hệ thống Blog mạng xã hội đa người dùng Bleb Blog. Dự án được chúng em xây dựng trên nền tảng Spring Boot 3.5 và Java 21, sử dụng cơ sở dữ liệu H2 cấu hình bền vững dạng File theo chuẩn tương thích MySQL, và lưu trữ hình ảnh đám mây trên Cloudinary.*
  > *Đây là Trang chủ của hệ thống. Khách vãng lai chưa cần đăng nhập vẫn có thể duyệt các bài viết mới nhất, lọc theo danh mục (Technology, Programming, Web Design) và thẻ tag, hoặc xem bảng xếp hạng các bài viết xu hướng (Trending Now) dựa trên lượt đọc thực tế."*
- **Thao tác trên màn hình**:
  - Click vào tab danh mục `Programming` -> Thấy URL đổi thành `/?cat=...` và danh sách bài viết lọc ngay lập tức mà không bị chớp giật trang.
  - Thử gõ từ khóa `"Spring"` vào ô tìm kiếm -> Thấy ô gợi ý nhanh (Autocomplete) thả xuống 5 bài viết khớp tiêu đề.

---

### BƯỚC 2: ĐĂNG KÝ, ĐĂNG NHẬP VÀ BẢO MẬT JWT STATELESS (1:00 - 2:00)
- **Lời thoại**:
  > *"Bây giờ em xin phép thực hiện Đăng nhập vào hệ thống. Hệ thống của chúng em áp dụng chuẩn bảo mật Stateless Authentication bằng JSON Web Token (JWT) mã hóa chữ ký HMAC-SHA512. Khi em đăng nhập thành công, Server trả về một Bearer Token có thời hạn sống 1 giờ."*
- **Thao tác**:
  - Bấm nút "Log In" -> Nhập `duonghd` / `123456` -> Bấm Đăng nhập.
  - Toast thông báo "Đăng nhập thành công" hiện lên.
  - Nhấn phím `F12` (Inspect) -> Mở tab **Application** -> **Local Storage** -> Chỉ cho thầy cô thấy chuỗi `token` và `username`.
  - Chỉ lên thanh Navbar: Nút Đăng nhập/Đăng ký đã tự động biến mất, thay vào đó là nút "New Post" và Avatar tròn có chữ cái viết tắt "HD".

---

### BƯỚC 3: SOẠN THẢO BÀI VIẾT, UPLOAD ẢNH CLOUDINARY & CHẾ ĐỘ NHÁP (2:00 - 3:15)
- **Lời thoại**:
  > *"Em xin phép demo tính năng viết bài. Điểm đặc biệt của hệ thống chúng em là tích hợp dịch vụ lưu ảnh Cloudinary API và hỗ trợ 2 luồng: Lưu nháp (Draft) và Xuất bản (Publish) chuẩn như Medium."*
- **Thao tác**:
  - Click nút "New Post" -> Chuyển sang trang `blog-editor.html`.
  - Bấm nút "Chọn ảnh bìa" -> Chọn một ảnh từ máy tính -> Mở tab Network thấy gọi `POST /upload/image` và nhận về link ảnh Cloudinary `https://res.cloudinary.com/...` hiển thị xem trước cực đẹp.
  - Nhập tiêu đề: `"Lập trình Spring Boot 3 cực dễ với Bleb Blog"`.
  - Chọn danh mục: `"Programming"`, nhập thẻ tag: `Java, SpringBoot, Bleb`.
  - Nhập nội dung bài viết.
  - **Bấm "Save Draft"**: Thông báo bài viết đã lưu vào bản nháp. Về trang chủ tìm kiếm -> Bài viết KHÔNG xuất hiện (đảm bảo tính bảo mật của bản nháp).
  - Vào trang "Manage Blogs" (`/manage-blogs.html`) -> Thấy bài viết nằm trong tab "Drafts".
  - Bấm nút sửa bài và bấm **"Publish"** -> Ra trang chủ thấy bài viết lập tức hiển thị trên đầu bảng tin với đường link Slug chuẩn SEO.

---

### BƯỚC 4: TƯƠNG TÁC MẠNG XÃ HỘI (LIKE, BOOKMARK, CÂY BÌNH LUẬN & THÔNG BÁO) (3:15 - 4:15)
- **Lời thoại**:
  > *"Bây giờ em xin phép demo tính năng tương tác mạng xã hội giữa hai tài khoản khác nhau."*
- **Thao tác**:
  - Mở tab ẩn danh (Tài khoản `dungnt`): Click vào bài viết mà bạn `duonghd` vừa đăng.
  - Bấm nút **Thích (Like)** -> Nút tim đổi màu đỏ và số like tăng lên 1.
  - Bấm nút **Lưu (Bookmark)** -> Bài viết được lưu vào trang `/saved-blogs.html`.
  - Viết một bình luận: `"Bài viết rất hay bạn ơi!"`.
  - Bấm nút "Trả lời" (Reply) ngay dưới bình luận đó: `"Cảm ơn bạn nhiều!"` -> Thấy câu trả lời thụt lề vào trong 1 cấp (Mô hình cây bình luận 2 cấp).
  - Quay lại trình duyệt của bạn `duonghd`:
    - Biểu tượng quả chuông thông báo trên Navbar xuất hiện **chấm đỏ số 2**.
    - Bấm vào quả chuông: Hiện 2 thông báo thời gian thực: `@dungnt đã thích bài viết của bạn` và `@dungnt đã bình luận vào bài viết của bạn`.

---

### BƯỚC 5: TRANG QUẢN TRỊ ADMIN DASHBOARD (4:15 - 5:00)
- **Lời thoại**:
  > *"Cuối cùng, em xin phép đăng nhập vào tài khoản Quản trị viên (Admin) để trình bày hệ thống kiểm soát toàn diện."*
- **Thao tác**:
  - Đăng nhập tài khoản `admin` / `123456`.
  - Trên thanh Navbar tự động xuất hiện nút **"Admin Dashboard"** màu tím (nhờ frontend giải mã payload JWT phát hiện role ADMIN).
  - Click vào Dashboard:
    - Xem thống kê tổng số thành viên, tổng số bài viết, danh sách 5 bài viết gần nhất.
    - Vào mục "Categories & Tags": Thêm một danh mục mới `"Trí tuệ nhân tạo (AI)"`, cập nhật và xóa danh mục.
    - Vào mục "Users": Xem danh sách người dùng trong CSDL H2.
- **Kết thúc thuyết trình**:
  > *"Dạ trên đây là toàn bộ các chức năng chính của Bài tập lớn. Nhóm chúng em đã kiểm thử tự động toàn diện vượt qua 48/48 ca kiểm thử. Chúng em xin chân thành cảm ơn quý Thầy/Cô và rất mong nhận được câu hỏi vấn đáp ạ!"*
