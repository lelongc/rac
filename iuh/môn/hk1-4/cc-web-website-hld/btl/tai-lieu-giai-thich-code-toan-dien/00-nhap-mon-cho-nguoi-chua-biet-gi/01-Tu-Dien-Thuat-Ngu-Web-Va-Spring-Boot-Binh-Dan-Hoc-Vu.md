# TỪ ĐIỂN THUẬT NGỮ LẬP TRÌNH WEB & SPRING BOOT (BÌNH DÂN HỌC VỤ)
### DÀNH RIÊNG CHO NGƯỜI CHƯA BIẾT GÌ VỀ WEB VẪN CÓ THỂ ĐI VẤN ĐÁP ĐẠT ĐIỂM CAO

> **Mục đích:** Khi đi thi vấn đáp, giảng viên thường dùng các thuật ngữ chuyên ngành tiếng Anh để hỏi. Nếu không hiểu thuật ngữ, bạn sẽ bị "đứng hình" dù chức năng đó bạn đã từng nhìn thấy.  
> File tài liệu này giải thích hơn **40 thuật ngữ cốt lõi nhất** của dự án bằng **các hình ảnh đời thường gần gũi** (nhà hàng, công viên, siêu thị), giúp bạn hiểu sâu bản chất trong 5 phút và tự tin chém gió trôi chảy trước hội đồng!

---

## 🏛️ 1. CÁC KHÁI NIỆM TỔNG QUAN VỀ HỆ THỐNG WEB

### 1. Client (Máy khách / Trình duyệt)
- **Hình ảnh đời thường:** Là **Khách hàng** bước vào một nhà hàng ăn uống.
- **Trong dự án:** Là trình duyệt Chrome, Edge, Cốc Cốc trên máy tính hoặc điện thoại của người dùng, nơi hiển thị giao diện HTML, CSS và chạy các đoạn mã JavaScript.

### 2. Server (Máy chủ Backend)
- **Hình ảnh đời thường:** Là **Khu nhà bếp** của nhà hàng. Khách hàng không được tự tiện đi vào bếp, mà chỉ có thể gửi phiếu gọi món vào đó.
- **Trong dự án:** Là ứng dụng Java Spring Boot đang chạy ở cổng `8080`. Nó nhận yêu cầu từ Client, kiểm tra dữ liệu, tính toán và lấy dữ liệu trả về.

### 3. Database (Cơ sở dữ liệu)
- **Hình ảnh đời thường:** Là **Kho chứa nguyên liệu** và **Sổ kế toán** của nhà hàng (chứa gạo, thịt, danh sách công nợ).
- **Trong dự án:** Là CSDL **H2 Database** (lưu trong file `data/blogdb.mv.db`), nơi cất giữ bảng `users`, `blogs`, `comments`, `likes`.

### 4. HTTP Request (Yêu cầu gửi đi)
- **Hình ảnh đời thường:** Là **Tờ phiếu gọi món** mà khách hàng ghi ra rồi đưa cho bồi bàn mang vào bếp.
- **Trong dự án:** Là gói tin mạng do trình duyệt gửi đến Spring Boot (ví dụ: *"Cho tôi đăng nhập với tài khoản admin"*).

### 5. HTTP Response (Phản hồi trả về)
- **Hình ảnh đời thường:** Là **Đĩa thức ăn** hoặc **Lời xin lỗi hết món** mà nhà bếp bưng ra cho khách.
- **Trong dự án:** Là kết quả mà Spring Boot trả về cho trình duyệt (dạng dữ liệu JSON hoặc thông báo lỗi).

---

## 🚦 2. PHƯƠNG THỨC HTTP (HTTP METHODS - CÁC HÀNH ĐỘNG)

Khi Client gửi Request lên Server, nó phải kèm theo một "Động từ hành động":

| Phương thức | Ý nghĩa đời thường | Dùng trong dự án ở đâu? |
| :--- | :--- | :--- |
| **GET** | **"Cho tôi xem / Cho tôi lấy"** (Không làm thay đổi gì trong kho). | `GET /blogs` (Lấy danh sách bài viết), `GET /users/my-profile` (Xem thông tin cá nhân). |
| **POST** | **"Tạo mới cho tôi"** (Tạo thêm đồ vật mới vào kho). | `POST /auth/token` (Đăng nhập), `POST /blogs` (Đăng bài viết mới), `POST /blogs/{id}/like` (Thả tim). |
| **PUT** | **"Sửa đổi toàn bộ"** (Thay thế thông tin cũ bằng thông tin mới). | `PUT /blogs/{id}` (Sửa bài viết), `PUT /users/{id}` (Cập nhật thông tin tài khoản). |
| **DELETE** | **"Vứt bỏ / Xóa đi"** (Xóa vĩnh viễn khỏi kho). | `DELETE /blogs/{id}` (Xóa bài viết), `DELETE /blogs/comments/{id}` (Xóa bình luận). |

---

## 🔢 3. MÃ TRẠNG THÁI HTTP (HTTP STATUS CODES)

Khi Server trả lời, nó luôn gửi kèm một con số 3 chữ số để thông báo tình trạng:

- **`200 OK` (Thành công tốt đẹp):** Giống như bồi bàn nói: *"Món ăn của quý khách đã xong, mời dùng bữa!"*.
- **`400 Bad Request` (Lỗi do người dùng gửi sai):** Giống như khách đòi gọi món không có trong thực đơn hoặc nhập thiếu thông tin (ví dụ: quên nhập mật khẩu, mật khẩu dưới 8 ký tự).
- **`401 Unauthorized` (Chưa xuất trình vé vào cửa):** Khách chưa đăng nhập hoặc token đã hết hạn mà đòi làm hành động của thành viên.
- **`403 Forbidden` (Bị cấm quyền):** Khách thường đòi đi vào phòng kế toán của giám đốc (ví dụ: User thường cố tình vào trang `admin/dashboard.html`).
- **`404 Not Found` (Không tìm thấy):** Tìm bài viết nhưng bài đó đã bị xóa hoặc đường dẫn gõ sai chính tả.
- **`500 Internal Server Error` (Lỗi sập máy chủ):** Đầu bếp trong bếp làm cháy nổ, code Java bị văng Exception mà lập trình viên quên bắt lỗi `try-catch`.

---

## 📦 4. ĐỊNH DẠNG DỮ LIỆU & GIAO TIẾP

### 6. JSON (JavaScript Object Notation)
- **Hình ảnh đời thường:** Giống như **Biên bản bàn giao chuẩn quốc tế**, viết bằng cặp `"Tên thuộc tính" : "Giá trị"`.
- **Ví dụ trong dự án:**
  ```json
  {
    "username": "admin",
    "email": "admin@gmail.com",
    "roles": ["ADMIN"]
  }
  ```
- **Tại sao dùng JSON?** Vì Java đọc được, JavaScript đọc được, Python cũng đọc được. Nó là ngôn ngữ chung giữa Frontend và Backend.

### 7. RESTful API (Application Programming Interface)
- **Hình ảnh đời thường:** Giống như **Menu gọi món chuẩn hóa** của quán ăn nhanh (Combo 1, Combo 2). Khách ở quầy chỉ cần đọc đúng mã combo là bếp hiểu ngay.
- **Trong dự án:** Là tập hợp các đường dẫn (Endpoint) chuẩn mực như `/blogs`, `/users`, `/auth` mà Backend mở ra để Frontend gọi tới.

### 8. Query Param vs Path Variable vs Request Body
- **Path Variable (`@PathVariable`):** Dữ liệu nằm trực tiếp trong đường dẫn để định danh một đối tượng cụ thể.  
  *Ví dụ:* `/blogs/3f7b9c12` ➔ `3f7b9c12` là ID bài viết cần xem.
- **Query Param (`@RequestParam`):** Dữ liệu nằm sau dấu chấm hỏi `?` dùng để tìm kiếm, lọc, sắp xếp.  
  *Ví dụ:* `/blogs?category=Technology&sort=desc`
- **Request Body (`@RequestBody`):** Dữ liệu lớn, bảo mật, được gói kín bên trong thân bức thư (không hiện trên thanh địa chỉ URL).  
  *Ví dụ:* Chuỗi mật khẩu lúc đăng nhập hoặc nội dung bài viết 1000 chữ.

---

## 🛡️ 5. BẢO MẬT & XÁC THỰC (SECURITY & JWT)

### 9. JWT (JSON Web Token)
- **Hình ảnh đời thường:** Giống như **Chiếc vòng đeo tay điện tử** khi bạn mua vé vào công viên nước Sun World.
  1. Lúc mua vé (Đăng nhập thành công), nhân viên phát cho bạn chiếc vòng.
  2. Trên vòng có ghi mã số của bạn, các trò chơi bạn được phép chơi (Role `USER` hay `ADMIN`), và giờ hết hạn.
  3. Chiếc vòng có con dấu dập nổi chống làm giả của công viên (**Chữ ký số Signature**).
  4. Mỗi khi chơi một trò (gọi API), bạn chỉ cần đưa vòng ra quẹt mà không cần phải mang theo thẻ căn cước hay mua lại vé từ đầu!
- **Cấu trúc 3 phần ngăn cách bởi 2 dấu chấm (`xxxxx.yyyyy.zzzzz`):**
  - **Header (`xxxxx`):** Khai báo thuật toán mã hóa (HS512).
  - **Payload (`yyyyy`):** Chứa thông tin người dùng (`sub: "admin"`, `scope: "ROLE_ADMIN"`, `exp: 1715000000`).
  - **Signature (`zzzzz`):** Chữ ký bảo mật được tạo từ mã khóa bí mật `SIGNER_KEY`. Kẻ xấu sửa dù chỉ 1 chữ trong Payload thì chữ ký này lập tức bị sai và hệ thống từ chối ngay.

### 10. Stateless (Không lưu trạng thái)
- **Hình ảnh đời thường:** Bác bảo vệ soát vé ở cổng trò chơi **không cần nhớ mặt hay ghi chép tên bạn vào sổ tay**. Bác chỉ cần nhìn vào chiếc vòng đeo tay (JWT) còn nguyên vẹn con dấu hay không là cho vào.
- **Lợi ích:** Máy chủ Spring Boot không tốn RAM để nhớ phiên làm việc (Session) của hàng triệu người dùng, giúp hệ thống chạy siêu nhẹ và không bị sập khi đông người truy cập.

### 11. BCrypt Password Encoder
- **Hình ảnh đời thường:** Giống như một **Cỗ máy xay thịt cực mạnh**.
  - Bạn thả miếng thịt bò (mật khẩu `"admin123"`) vào, nó xay nhuyễn thành một đĩa pate lộn xộn (`"$2a$10$EixZaYVK1fsbv1Z6W92PqO..."`).
  - Đố ai trên đời có thể từ đĩa pate đó ghép ngược lại thành miếng thịt bò ban đầu!
  - Khi bạn đăng nhập lại, máy lấy miếng thịt mới bạn vừa gõ, xay ra đĩa pate thứ hai rồi so sánh 2 đĩa pate có giống nhau không (`passwordEncoder.matches()`).
- **Lợi ích:** Kể cả khi hacker đột nhập ăn cắp được file CSDL, chúng cũng chỉ nhìn thấy chuỗi ký tự vô nghĩa, không bao giờ biết được mật khẩu thật của người dùng!

---

## ⚙️ 6. CÁC KHÁI NIỆM CỐT LÕI TRONG SPRING BOOT

### 12. Spring Bean & IoC Container (Inversion of Control)
- **Hình ảnh đời thường:** Giống như **Tủ đồ nghề dùng chung** của một xưởng mộc.
  - Bình thường, thợ muốn có cái búa thì phải tự bỏ tiền túi ra đi mua (`new Hammer()`).
  - Với Spring Boot, ông chủ xưởng (IoC Container) mua sẵn búa, kìm, cờ lê để sẵn trong tủ (gọi là các **Spring Bean**). Ai cần dùng món gì chỉ việc xin mượn chứ không cần tự mua mới.

### 13. Dependency Injection (`@Autowired` / `@RequiredArgsConstructor`)
- **Hình ảnh đời thường:** Là hành động **Trao tận tay đồ nghề**.
  - Bạn là thợ sửa ống nước bước vào phòng, trợ lý đã cầm sẵn cờ lê đưa tận tay bạn. Bạn chỉ việc vặn ốc mà không tốn công đi tìm.
  - Trong code: `BlogService` cần dùng `BlogRepository` để lấy dữ liệu, Spring Boot tự động "bơm" (tiêm - inject) `BlogRepository` vào cho `BlogService` dùng.

### 14. Entity (Thực thể CSDL)
- **Hình ảnh đời thường:** Là **Bản thiết kế mẫu** của một bộ hồ sơ.
- **Trong dự án:** Lớp Java có gắn `@Entity` (như `User.java`, `Blog.java`). Hibernate sẽ nhìn vào class này để tự động tạo ra cái bảng tương ứng trong CSDL.

### 15. Repository (Kho chứa dữ liệu)
- **Hình ảnh đời thường:** Là **Bác thủ kho mẫn cán**.
- **Trong dự án:** Là các interface kế thừa `JpaRepository`. Bạn không cần viết câu lệnh SQL dài dòng, chỉ cần gọi `userRepository.findById(id)` hay `blogRepository.save(blog)` là bác thủ kho tự chạy vào DB lấy hoặc lưu dữ liệu ra cho bạn!

### 16. Service (Tầng xử lý nghiệp vụ)
- **Hình ảnh đời thường:** Là **Bác bếp trưởng tài hoa**.
- **Trong dự án:** Nơi tập trung toàn bộ "chất xám" và thuật toán của website: kiểm tra mật khẩu đúng sai, kiểm tra xem người này có phải chủ bài viết không, tính toán view, tạo thông báo...

### 17. Controller (Tầng điều khiển)
- **Hình ảnh đời thường:** Là **Cô lễ tân xinh đẹp** đứng ở cửa đón khách.
- **Trong dự án:** Nơi tiếp nhận các yêu cầu gửi đến từ trình duyệt (`@GetMapping`, `@PostMapping`), kiểm tra tính hợp lệ cơ bản (`@Valid`) rồi chuyển việc cho tầng Service xử lý.

### 18. DTO (Data Transfer Object - Vật chứa truyền dữ liệu)
- **Hình ảnh đời thường:** Giống như **Hộp quà gói sẵn mang về**.
  - Trong kho có củ khoai tây dính đất cát, nhưng khi bán cho khách thì gọt vỏ sạch sẽ, chiên giòn, rắc phô mai rồi bỏ vào hộp đẹp đẽ.
  - Không bao giờ trả trực tiếp Entity `User` ra ngoài (vì nó chứa mật khẩu `password`), mà phải đóng gói vào `UserResponse` (chỉ gồm `username`, `avatarUrl`, `fullName`).

### 19. MapStruct
- **Hình ảnh đời thường:** Là **Cỗ máy đóng gói quà tự động**.
  - Thay vì bạn phải ngồi gõ tay hàng chục dòng: `userResponse.setUsername(user.getUsername()); userResponse.setEmail(...)`, MapStruct tự động sinh ra đoạn mã copy thuộc tính này trong tích tắc khi biên dịch!

### 20. Exception & `@ControllerAdvice` (Bắt lỗi tập trung)
- **Hình ảnh đời thường:** Giống như **Đội cứu hộ khẩn cấp 115**.
  - Bất cứ phòng ban nào trong công ty xảy ra sự cố (hết tiền, cháy nổ, sai mật khẩu), chỉ cần hét lên (`throw new AppException(ErrorCode.USER_NOT_EXITED)`).
  - Đội cứu hộ tập trung (`GlobalExceptionHandler`) sẽ ngay lập tức có mặt, dập tắt sự cố và gửi thông báo nhẹ nhàng, lịch sự về cho khách hàng dưới dạng `ApiResponse` chuẩn, ngăn không cho chương trình bị sập màn hình trắng!

---

## 🎨 7. CÔNG NGHỆ FRONTEND & GIAO DIỆN

### 21. Single State `S` (Bộ nhớ trạng thái tập trung)
- Trong file `app.js`, biến `S` là trái tim lưu trữ trạng thái hiện tại của màn hình: đang ở trang nào (`S.page`), đang lọc danh mục nào (`S.cat`), từ khóa tìm kiếm là gì (`S.keyword`), và người dùng đã đăng nhập chưa (`S.isAuth`).

### 22. Glassmorphism (Hiệu ứng kính mờ)
- Lớp thanh menu phía trên sử dụng thuộc tính `backdrop-filter: blur(22px);` tạo cảm giác như một tấm kính đóng băng nhìn xuyên thấu xuống nội dung bên dưới, mang lại phong cách sang trọng của Apple macOS.

### 23. Cloudinary CDN
- Dịch vụ lưu trữ hình ảnh trên mây của Mỹ. Khi người dùng tải ảnh bìa lên, ảnh được gửi sang Cloudinary tối ưu hóa nén và trả về một đường link URL toàn cầu, giúp website không bị đầy ổ cứng máy chủ.

---

> 💡 **MẸO DÀNH CHO BẠN:** Hãy đọc qua 23 mục trên 2 lần. Khi đi thi vấn đáp, bất cứ khi nào thầy cô hỏi: *"Cái này là gì? Hoạt động ra sao?"*, bạn chỉ cần nhớ lại hình ảnh ví von (nhà hàng, bồi bàn, công viên nước, hộp quà) rồi trả lời theo giọng điệu tự tin. Giảng viên sẽ cực kỳ ấn tượng vì bạn thực sự hiểu bản chất kỹ thuật chứ không học vẹt!
