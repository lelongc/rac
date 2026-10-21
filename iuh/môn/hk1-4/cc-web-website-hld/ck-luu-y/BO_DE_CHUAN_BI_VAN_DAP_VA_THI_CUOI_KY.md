# 🎓 ĐẠI CẨM NANG TOÀN THƯ: CHUẨN BỊ VẤN ĐÁP BTL & ÔN THI TỰ LUẬN CUỐI KỲ

## MÔN: CÔNG NGHỆ WEB VÀ WEBSITE HƯỚNG DỮ LIỆU — TRƯỜNG ĐH CÔNG NGHIỆP TP.HCM (IUH)

**Giảng viên:** Thầy Trương Bá Phúc**Dự án BTL:** Website Blog & Nền tảng Viết bài trực tuyến đa người dùng (`blog-website-main`)**Thành viên thực hiện:**

1. **24743991 — Hoàng Đại Dương**
2. **24000905 — Nguyễn Trung Dũng**
3. **23630851 — Lê Thành Long**

---

# 📌 MỤC LỤC TỔNG QUAN

- [PHẦN 0: LỊCH THI, LỊCH VẤN ĐÁP &amp; QUY TẮC BẮT BUỘC TỪ THẦY PHÚC](#phần-0-lịch-thi-lịch-vấn-đáp--quy-tắc-bắt-buộc-từ-thầy-phúc)
- [PHẦN I: NHẬP MÔN CẤP TỐC CHO NGƯỜI CHƯA TỪNG HỌC JAVA &amp; SPRING BOOT (ĐỌC 10 PHÚT HIỂU HẾT DỰ ÁN)](#phần-i-nhập-môn-cấp-tốc-cho-người-chưa-từng-học-java--spring-boot-đọc-10-phút-hiểu-hết-dự-án)
  - [1. Java là gì? Class và Object là gì?](#1-java-là-gì-class-và-object-là-gì)
  - [2. Annotation dấu a còng (@) là gì?](#2-annotation-dấu-a-còng--là-gì)
  - [3. Spring Boot là gì? Framework là gì?](#3-spring-boot-là-gì-framework-là-gì)
  - [4. Mô hình 3 lớp (3-tier Architecture) ví như Nhà Hàng](#4-mô-hình-3-lớp-3-tier-architecture-ví-như-nhà-hàng)
  - [5. JSON, API và HTTP Request hoạt động thế nào?](#5-json-api-và-http-request-hoạt-động-thế-nào)
- [PHẦN II: BẢN ĐỒ VỊ TRÍ TOÀN BỘ FILE TRONG DỰ ÁN (BẢNG TRA CỨU CẤP TỐC)](#phần-ii-bản-đồ-vị-trí-toàn-bộ-file-trong-dự-án-bảng-tra-cứu-cấp-tốc)
- [PHẦN III: GIẢI THÍCH CHI TIẾT TOÀN BỘ MỐI QUAN HỆ TRONG CƠ SỞ DỮ LIỆU (12 BẢNG)](#phần-iii-giải-thích-chi-tiết-toàn-bộ-mối-quan-hệ-trong-cơ-sở-dữ-liệu-12-bảng)
  - [1. Sơ đồ thực thể ERD tổng quát](#1-sơ-đồ-thực-thể-erd-tổng-quát)
  - [2. Khái niệm cốt lõi: Khóa chính (PK), Khóa ngoại (FK) và Bảng trung gian](#2-khái-niệm-cốt-lõi-khóa-chính-pk-khóa-ngoại-fk-và-bảng-trung-gian)
  - [3. Phân tích chi tiết 11 mối quan hệ liên kết giữa các bảng](#3-phân-tích-chi-tiết-11-mối-quan-hệ-liên-kết-giữa-các-bảng)
  - [4. Ràng buộc toàn vẹn, Chống gian lận (Unique Constraints) &amp; Xóa tầng (Cascade)](#4-ràng-buộc-toàn-vẹn-chống-gian-lận-unique-constraints--xóa-tầng-cascade)
- [PHẦN IV: TRỌN BỘ LÝ THUYẾT MÔN HỌC &amp; ĐỀ THI TỰ LUẬN TRÊN GIẤY (22/11/2026)](#phần-iv-trọn-bộ-lý-thuyết-môn-học--đề-thi-tự-luận-trên-giấy-22112026)
  - [Chuyên đề 1: Kiến trúc MVC &amp; Vòng đời HTTP Request (Request Lifecycle)](#chuyên-đề-1-kiến-trúc-mvc--vòng-đời-http-request-request-lifecycle)
  - [Chuyên đề 2: Tầng Model trong thực tế (Entity vs DTO vs Service)](#chuyên-đề-2-tầng-model-trong-thực-tế-entity-vs-dto-vs-service)
  - [Chuyên đề 3: Inversion of Control (IoC) &amp; Dependency Injection (DI) Chuyên Sâu](#chuyên-đề-3-inversion-of-control-ioc--dependency-injection-di-chuyên-sâu)
  - [Chuyên đề 4: Cơ Chế Dynamic Proxy Trong Spring Boot &amp; JPA](#chuyên-đề-4-cơ-chế-dynamic-proxy-trong-spring-boot--jpa)
  - [Chuyên đề 5: Toàn Bộ Annotation JPA &amp; Hibernate Ánh Xạ CSDL](#chuyên-đề-5-toàn-bộ-annotation-jpa--hibernate-ánh-xạ-csdl)
  - [Chuyên đề 6: Toàn Bộ Annotation Spring Boot, Spring MVC &amp; Lombok](#chuyên-đề-6-toàn-bộ-annotation-spring-boot-spring-mvc--lombok)
  - [Chuyên đề 7: Quản Lý Giao Dịch @Transactional &amp; Tính Chất ACID](#chuyên-đề-7-quản-lý-giao-dịch-transactional--tính-chất-acid)
  - [Chuyên đề 8: Bảo Mật Stateless JWT &amp; Spring Security 6 vs Session Cookie](#chuyên-đề-8-bảo-mật-stateless-jwt--spring-security-6-vs-session-cookie)
  - [Chuyên đề 9: So Sánh Server-Side Rendering (SSR) vs Client-Side Rendering (CSR)](#chuyên-đề-9-so-sánh-server-side-rendering-ssr-vs-client-side-rendering-csr)
  - [Chuyên đề 10: 10 Công Cụ Cốt Lõi Trong Môn Học Của Thầy Phúc](#chuyên-đề-10-10-công-cụ-cốt-lõi-trong-môn-học-của-thầy-phúc)
- [PHẦN V: PHÂN TÍCH TỪNG DÒNG CODE &amp; MỌI CHỨC NĂNG TRONG DỰ ÁN BTL](#phần-v-phân-tích-từng-dòng-code--mọi-chức-năng-trong-dự-án-btl)
  - [Mục 1: Tầng Cấu Hình (Configuration Package)](#mục-1-tầng-cấu-hình-configuration-package)
  - [Mục 2: Tầng Thực Thể (Entity Package - 10 Entities)](#mục-2-tầng-thực-thể-entity-package---10-entities)
  - [Mục 3: Tầng Truy Xuất Dữ Liệu (Repository Package &amp; Phân Tích JPQL)](#mục-3-tầng-truy-xuất-dữ-liệu-repository-package--phân-tích-jpql)
  - [Mục 4: Tầng Nghiệp Vụ (Service Package - Phân Tích Từng Phương Thức)](#mục-4-tầng-nghiệp-vụ-service-package---phân-tích-từng-phương-thức)
  - [Mục 5: Tầng Điều Khiển (Controller Package - Phân Tích Từng Endpoint)](#mục-5-tầng-điều-khiển-controller-package---phân-tích-từng-endpoint)
  - [Mục 6: Xử Lý Ngoại Lệ &amp; Tiện Ích (Exception &amp; SlugUtils)](#mục-6-xử-lý-ngoại-lệ--tiện-ích-exception--slugutils)
  - [Mục 7: Tầng Giao Diện &amp; Frontend JavaScript Giao Tiếp API](#mục-7-tầng-giao-diện--frontend-javascript-giao-tiếp-api)
- [PHẦN VI: BỘ 25 CÂU HỎI VẤN ĐÁP &#34;XOÁY TẬN TỪNG DÒNG CODE&#34; &amp; KỊCH BẢN ĐẠT ĐIỂM 10](#phần-vi-bộ-25-câu-hỏi-vấn-đáp-xoáy-tận-từng-dòng-code--kịch-bản-đạt-điểm-10)
- [PHẦN VII: CẨM NĂNG CỨU MẠNG VẤN ĐÁP CẤP TỐC (SPEED-READ FOR DEFENSE TOMORROW)](#phần-vii-cẩm-năng-cứu-mạng-vấn-đáp-cấp-tốc-speed-read-for-defense-tomorrow)

---

# PHẦN 0: LỊCH THI, LỊCH VẤN ĐÁP & QUY TẮC BẮT BUỘC TỪ THẦY PHÚC

### 1. Lịch Vấn Đáp Báo Cáo Bài Tập Lớn (BTL)

- **Nhóm xong sớm**: Có thể đăng ký báo cáo vào tuần sau (25/10/2026).
- **Ngày báo cáo chính thức chung**: **Chủ Nhật, ngày 01/11/2026** (hoặc ngày mai nếu bạn đăng ký báo cáo trước).
- **Địa điểm**: **Phòng Giáo viên** (Khoa CNTT - IUH).
- **Khung giờ**: Từ **9h30 sáng đến 17h30 chiều** (Thầy ngồi chấm cả ngày, nhóm đến trình diện, bật máy chạy demo và Thầy sẽ gọi từng thành viên lên hỏi vấn đáp).
- **Quy cách chấm**: Chạy demo trực tiếp trên máy + Thầy lật mã nguồn hỏi bất kỳ dòng nào + Thầy hỏi cấu trúc CSDL và các khái niệm kỹ thuật phần mềm.

### 2. Quy Cách Quyển Báo Cáo In Nộp (In Giấy A4)

- **Độ dài**: Bắt buộc trong khoảng **15 đến 20 trang** (Không ngắn hơn 15 trang, không dài quá 20 trang).
- **Bố cục bắt buộc**:
  1. *Mô tả bài toán / Nghiệp vụ*: Mục tiêu đề tài, phân vai người dùng (Khách, Thành viên, Quản trị viên).
  2. *Sơ đồ CSDL*: Sơ đồ ERD rõ nét, bảng đặc tả 12 bảng (tên bảng, cột, kiểu dữ liệu, khóa chính, khóa ngoại, ràng buộc).
  3. *Kiến trúc hệ thống*: Mô hình phân tầng (MVC / 3-tier: Controller $\rightarrow$ Service $\rightarrow$ Repository), giải thích luồng dữ liệu.
  4. *Giao diện chức năng*: Chụp màn hình các tính năng chính kèm chú thích ngắn.
- ⚠️ **LỜI DẶN ĐẶC BIỆT CỦA THẦY PHÚC**: **TUYỆT ĐỐI KHÔNG DÁN SOURCE CODE VÀO QUYỂN BÁO CÁO!** Báo cáo là tài liệu phân tích thiết kế, không phải chỗ in code. Nhóm nào dán code vào sẽ bị trừ điểm nặng!

### 3. Lịch & Quy Chế Thi Cuối Kỳ

- **Ngày thi**: **Chủ Nhật, ngày 22/11/2026**.
- **Hình thức thi**: **TỰ LUẬN TRÊN GIẤY** (Không dùng máy tính, không mở tài liệu).
- **Cách chấm thi của Thầy**: Thầy chấm cực kỳ chuẩn xác theo từ khóa (keywords) và bản chất kỹ thuật phần mềm. Trả lời đúng trọng tâm, gãy gọn, có sơ đồ minh họa sẽ đạt điểm 9-10. Trả lời lan man, chép sai bản chất hoặc "chém gió" sẽ bị 0 điểm câu đó.

---

# PHẦN I: NHẬP MÔN CẤP TỐC CHO NGƯỜI CHƯA TỪNG HỌC JAVA & SPRING BOOT (ĐỌC 10 PHÚT HIỂU HẾT DỰ ÁN)

*(Nếu bạn chưa từng code Java hay Spring Boot bao giờ, chỉ cần đọc kỹ 5 mục dưới đây bằng ngôn ngữ đời thường là bạn có thể tự tin nói chuyện với Thầy như một lập trình viên chuyên nghiệp!)*

### 1. Java là gì? Class và Object là gì?

- **Java** là ngôn ngữ lập trình hướng đối tượng (OOP). Trong Java, mọi thứ đều xoay quanh "Đối tượng" (Object).
- **Class (Lớp)**: Hãy tưởng tượng Class giống như một **"Khuôn đúc bánh"** hoặc bản vẽ thiết kế. Ví dụ: `class User` là bản thiết kế quy định: Một người dùng thì có `username`, `password`, `email`.
- **Object (Đối tượng)**: Là **"Chiếc bánh thật"** được tạo ra từ cái khuôn đó. Ví dụ: User "admin", User "duonghd", User "longlt" là 3 đối tượng cụ thể được sinh ra trong bộ nhớ máy tính.
- **Interface (Giao diện)**: Là một **"Bản hợp đồng"** chỉ liệt kê tên việc cần làm chứ không viết ruột. Ví dụ: Interface `BlogRepository` ghi: "Tôi có chức năng lưu bài viết, tìm bài viết theo tên", còn chi tiết làm sao lưu xuống database thì Spring Boot sẽ tự làm ngầm.

### 2. Annotation dấu a còng (@) là gì?

- Trong code bạn thấy rất nhiều chữ có dấu `@` ở đầu như `@Entity`, `@Service`, `@Autowired`, `@GetMapping`.
- **Bản chất**: `@` (Annotation) là những **"Tấm tem nhãn chỉ dẫn"** dán lên đầu class hoặc hàm. Khi chương trình chạy, Spring Boot quét qua các tấm tem này để biết phải làm gì:
  - Dán tem `@Entity`: Báo cho hệ thống biết *"Class này tương ứng với 1 bảng trong Database MySQL đấy!"*.
  - Dán tem `@Service`: Báo cho hệ thống biết *"Class này chứa code xử lý nghiệp vụ, tính toán đấy!"*.
  - Dán tem `@RestController`: Báo cho hệ thống biết *"Class này là nơi đón khách từ trình duyệt gửi yêu cầu lên và trả về dữ liệu dạng chữ JSON đấy!"*.
  - Dán tem `@GetMapping("/blogs")`: Báo cho hệ thống biết *"Khi nào người dùng vào link `/blogs` thì hãy gọi hàm này ra chạy!"*.

### 3. Spring Boot là gì? Framework là gì?

- Nếu viết code từ đầu không dùng công cụ hỗ trợ thì giống như bạn tự đi chặt cây, đúc sắt để đóng một chiếc xe hơi.
- **Spring Boot là một Framework (Bộ khung sườn dựng sẵn)**: Nó đã đóng sẵn khung gầm xe, động cơ, phanh, bánh xe (máy chủ web Tomcat, hệ thống bảo mật, kết nối CSDL). Việc của nhóm bạn chỉ là lắp cái vô lăng và ghế ngồi (viết logic chức năng bài viết, bình luận, like). Do đó dự án phát triển cực kỳ nhanh và chuẩn doanh nghiệp.

### 4. Mô hình 3 lớp (3-tier Architecture) ví như Nhà Hàng

Dự án của nhóm chia làm 3 tầng rõ rệt, y hệt như một nhà hàng cao cấp:

1. **Tầng Controller (Người Bồi Bàn)**: Đứng ở cửa đón khách (nhận Request từ trình duyệt). Khách gọi món "Cho tôi xem bài viết số 1", Controller tiếp nhận order, kiểm tra xem khách có vé (Token) hợp lệ không, rồi chuyển order vào cho Bếp. Controller KHÔNG tự nấu ăn.
2. **Tầng Service (Đầu Bếp Trưởng)**: Nằm ở trong bếp. Nhận yêu cầu từ bồi bàn, thực hiện nấu nướng (xử lý logic nghiệp vụ: kiểm tra bài viết có tồn tại không, tính toán số lượt like, kiểm tra mật khẩu có đúng không, lưu nháp hay xuất bản). Khi cần nguyên liệu thịt/cá, Bếp trưởng sẽ bảo Thủ kho đi lấy.
3. **Tầng Repository (Thủ Kho)**: Giữ chìa khóa nhà kho (Database MySQL). Khi Bếp trưởng (Service) bảo: "Lấy cho tôi bài viết có ID này", Repository sẽ chạy vào Database lấy đúng dữ liệu đó mang ra cho Bếp trưởng.

```text
[Khách hàng / Trình duyệt] 
       │ (1. Gửi yêu cầu)
       ▼
[Controller - Bồi Bàn]
       │ (2. Chuyển phiếu gọi món)
       ▼
[Service - Bếp Trưởng]
       │ (3. Yêu cầu lấy nguyên liệu)
       ▼
[Repository - Thủ Kho]
       │ (4. Chạy vào kho lấy)
       ▼
[Database MySQL - Kho Nguyên Liệu]
```

### 5. JSON, API và HTTP Request hoạt động thế nào?

- **HTTP Request**: Khi bạn bấm một nút trên web, trình duyệt gửi một lệnh đi:
  - `GET`: Lấy dữ liệu về để xem (ví dụ: xem danh sách bài viết).
  - `POST`: Gửi dữ liệu mới lên để lưu (ví dụ: đăng ký tài khoản, đăng bài viết mới, bấm like).
  - `PUT`: Cập nhật dữ liệu cũ (ví dụ: sửa bài viết, đổi mật khẩu).
  - `DELETE`: Xóa dữ liệu (ví dụ: xóa bài viết, xóa bình luận).
- **JSON (JavaScript Object Notation)**: Là định dạng chữ text tiêu chuẩn để máy tính nói chuyện với nhau. Ví dụ thông tin một bài viết dạng JSON:
  ```json
  {
    "title": "Học Spring Boot",
    "content": "Nội dung bài viết...",
    "category": "Lập trình"
  }
  ```
- **API (Giao diện lập trình ứng dụng)**: Là cái "cổng giao dịch". Ví dụ cổng `POST /blogs` là nơi tiếp nhận bài viết mới dạng JSON.

---

# PHẦN II: BẢN ĐỒ VỊ TRÍ TOÀN BỘ FILE TRONG DỰ ÁN (BẢNG TRA CỨU CẤP TỐC)

*(Khi Thầy bảo: "Mở code chỗ này chỗ kia cho Thầy coi", hãy nhìn ngay bảng này để mở đúng file trong 2 giây!)*

| Tên File                                  | Nằm ở thư mục nào trong dự án?        | Tác dụng làm gì?                                                                                   | Khi Thầy hỏi, mở file này và nói câu gì?                                                                        |
| :----------------------------------------- | :------------------------------------------- | :----------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- |
| **`SecurityConfig.java`**          | `src/main/java/com/group/blog/config/`     | Cấu hình bảo mật, chặn quyền Admin/User, giải mã JWT, băm BCrypt.                             | *"Dạ đây là trái tim bảo mật của nhóm, cấu hình Stateless JWT và phân quyền API ạ."*                   |
| **`ApplicationInitConfig.java`**   | `src/main/java/com/group/blog/config/`     | Tự động tạo sẵn tài khoản Admin, 3 tài khoản của nhóm và bài viết mẫu khi vừa mở app. | *"Dạ file này dùng `ApplicationRunner` để khởi tạo sẵn dữ liệu mẫu vào MySQL khi chạy lần đầu ạ."* |
| **`CloudinaryConfig.java`**        | `src/main/java/com/group/blog/config/`     | Kết nối tài khoản lưu trữ ảnh đám mây Cloudinary.                                            | *"Dạ file này nạp API Key từ file YAML để cấu hình Bean Cloudinary tải ảnh ạ."*                            |
| **`User.java`**                    | `src/main/java/com/group/blog/entity/`     | Thực thể ánh xạ bảng `users` trong MySQL.                                                       | *"Dạ đây là Entity User, khóa chính UUID, có bảng phụ `user_roles` lưu quyền hạn ạ."*                  |
| **`Blog.java`**                    | `src/main/java/com/group/blog/entity/`     | Thực thể ánh xạ bảng `blogs` (bài viết).                                                      | *"Dạ đây là Entity Blog, có quan hệ N-1 với User, N-1 với Category và N-N với Tag ạ."*                     |
| **`Comment.java`**                 | `src/main/java/com/group/blog/entity/`     | Thực thể ánh xạ bảng `comments` (bình luận).                                                  | *"Dạ đây là Entity Comment, có quan hệ tự tham chiếu cha-con `parent_id` để làm reply ạ."*              |
| **`BlogLike.java`**                | `src/main/java/com/group/blog/entity/`     | Thực thể ánh xạ bảng `blog_likes` (lượt thả tim).                                            | *"Dạ bảng này lưu lượt like, có Unique Constraint `(user_id, blog_id)` chống like 2 lần ạ."*              |
| **`Bookmark.java`**                | `src/main/java/com/group/blog/entity/`     | Thực thể ánh xạ bảng `bookmarks` (lưu bài viết).                                             | *"Dạ bảng này lưu bài viết đọc sau của người dùng ạ."*                                                   |
| **`BlogView.java`**                | `src/main/java/com/group/blog/entity/`     | Thực thể ánh xạ bảng `blog_views` (lượt đọc bài).                                          | *"Dạ bảng này đếm lượt xem, lưu cả `ipAddress` để khách vãng lai đọc vẫn tính view ạ."*           |
| **`UserFollow.java`**              | `src/main/java/com/group/blog/entity/`     | Thực thể ánh xạ bảng `user_follows` (theo dõi tác giả).                                      | *"Dạ bảng này lưu quan hệ theo dõi giữa `follower_id` và `following_id` ạ."*                             |
| **`Notification.java`**            | `src/main/java/com/group/blog/entity/`     | Thực thể ánh xạ bảng `notifications` (thông báo).                                             | *"Dạ bảng này lưu thông báo LIKE, COMMENT, FOLLOW kèm đường dẫn `targetUrl` ạ."*                        |
| **`Category.java` & `Tag.java`** | `src/main/java/com/group/blog/entity/`     | Thực thể Danh mục và Thẻ Tag.                                                                     | *"Dạ lưu danh mục và thẻ tag bài viết, tên là duy nhất (UNIQUE) ạ."*                                       |
| **`BlogRepository.java`**          | `src/main/java/com/group/blog/repository/` | Chứa các câu truy vấn JPQL phức tạp tìm kiếm bài viết.                                       | *"Dạ interface này dùng cơ chế Dynamic Proxy và câu lệnh JPQL `COUNT(DISTINCT)` tối ưu ạ."*              |
| **`BlogService.java`**             | `src/main/java/com/group/blog/service/`    | Chứa toàn bộ nghiệp vụ đăng bài, sửa bài, lưu nháp, tìm kiếm.                            | *"Dạ đây là tầng Service xử lý nghiệp vụ bài viết và phân nhánh Lưu Nháp vs Xuất Bản ạ."*          |
| **`AuthenticationService.java`**   | `src/main/java/com/group/blog/service/`    | Nghiệp vụ Đăng nhập, kiểm tra mật khẩu BCrypt, sinh chuỗi JWT.                                | *"Dạ đây là nơi xác thực tài khoản và ký số sinh mã Token JWT bằng thuật toán HS512 ạ."*             |
| **`UserService.java`**             | `src/main/java/com/group/blog/service/`    | Nghiệp vụ Đăng ký tài khoản, đổi mật khẩu, xem hồ sơ profile.                             | *"Dạ xử lý đăng ký người dùng mới, băm mật khẩu và lấy thông tin cá nhân ạ."*                      |
| **`InteractionService.java`**      | `src/main/java/com/group/blog/service/`    | Nghiệp vụ Thả tim (Like), Thêm/Xóa bình luận, Bookmark.                                         | *"Dạ xử lý tương tác like, comment phân cấp đệ quy và gửi thông báo tự động ạ."*                    |
| **`FollowService.java`**           | `src/main/java/com/group/blog/service/`    | Nghiệp vụ Theo dõi / Bỏ theo dõi tác giả, chặn tự follow mình.                               | *"Dạ xử lý tính năng theo dõi tác giả và thống kê số lượng follower/following ạ."*                     |
| **`CloudinaryService.java`**       | `src/main/java/com/group/blog/service/`    | Đẩy ảnh lên dịch vụ Cloudinary và lấy link ảnh về.                                           | *"Dạ nhận file ảnh dạng MultipartFile và tải lên đám mây Cloudinary ạ."*                                   |
| **`BlogController.java`**          | `src/main/java/com/group/blog/controller/` | Tiếp nhận tất cả các URL liên quan bài viết (`/blogs/**`).                                   | *"Dạ đây là RestController điều phối các API bài viết trả về dữ liệu JSON ạ."*                         |
| **`UserController.java`**          | `src/main/java/com/group/blog/controller/` | Tiếp nhận các URL liên quan người dùng (`/users/**`).                                         | *"Dạ tiếp nhận đăng ký, lấy profile cá nhân và danh sách người dùng ạ."*                               |
| **`ViewController.java`**          | `src/main/java/com/group/blog/controller/` | Mở các trang HTML Thymeleaf cho trình duyệt.                                                       | *"Dạ đây là `@Controller` trả về giao diện HTML Thymeleaf cho người dùng xem ạ."*                        |
| **`GlobalExceptionHandler.java`**  | `src/main/java/com/group/blog/exception/`  | Bắt toàn bộ lỗi trong hệ thống để trả về JSON đẹp đẽ.                                    | *"Dạ dùng `@ControllerAdvice` để bắt lỗi tập trung, không để lộ crash hệ thống ra ngoài ạ."*         |
| **`SlugUtils.java`**               | `src/main/java/com/group/blog/util/`       | Biến tiêu đề tiếng Việt thành link URL không dấu (SEO).                                       | *"Dạ hàm tiện ích bỏ dấu tiếng Việt bằng Unicode NFD và Regex để tạo link đẹp chuẩn SEO ạ."*         |
| **`application-secret.yml`**       | `src/main/resources/`                      | Chứa khóa bí mật Cloudinary và chữ ký JWT.                                                      | *"Dạ file YAML lưu các thông số bảo mật, mật khẩu và khóa bí mật ạ."*                                   |

---

# PHẦN III: GIẢI THÍCH CHI TIẾT TOÀN BỘ MỐI QUAN HỆ TRONG CƠ SỞ DỮ LIỆU (12 BẢNG)

## 1. Sơ đồ thực thể ERD tổng quát

```text
┌──────────────┐          ┌──────────────┐          ┌──────────────┐
│  categories  │          │    users     │          │    roles     │
│  (id, name)  │          │ (id, pass...)│          │ (role_name)  │
└──────┬───────┘          └──────┬───────┘          └──────┬───────┘
       │ 1                       │ 1                       │ N
       │                         │                         │
       │ N                       │ N                       │ M
┌──────┴───────┐          ┌──────┴───────┐          ┌──────┴───────┐
│    blogs     ├──────────┤  user_roles  │          │  user_roles  │
│(id,title...) │          │(user_id,role)│          │(user_id,role)│
└──────┬───────┘          └──────────────┘          └──────────────┘
       │ 1                │ 1                │ 1            │ 1
       ├──────────────────┼──────────────────┼──────────────┤
       │ N                │ N                │ N            │ N
┌──────┴───────┐   ┌──────┴───────┐   ┌──────┴───────┐┌─────┴──────────┐
│  blog_tags   │   │  blog_likes  │   │  bookmarks   ││  user_follows  │
│(blog_id,tag) │   │(blog_id,user)│   │(blog_id,user)││(follower,follow│
└──────┬───────┘   └──────────────┘   └──────────────┘└────────────────┘
       │ N                │ 1                │ 1
┌──────┴───────┐   ┌──────┴───────┐   ┌──────┴───────┐
│     tags     │   │   comments   │   │notifications │
│  (id, name)  │   │(id, blog...) │   │(id, user_id) │
└──────────────┘   └──────────────┘   └──────────────┘
```

---

## 2. Khái niệm cốt lõi: Khóa chính (PK), Khóa ngoại (FK) và Bảng trung gian

- **Khóa chính (Primary Key - PK)**: Là cột dùng để định danh duy nhất một dòng trong bảng (không bao giờ trùng nhau). Ví dụ: Cột `id` của mỗi User hoặc mỗi Blog. Dự án dùng định dạng **UUID** (chuỗi 36 ký tự ngẫu nhiên) làm PK để kẻ xấu không đoán được ID.
- **Khóa ngoại (Foreign Key - FK)**: Là cột nằm ở bảng này nhưng lại **trỏ về Khóa chính của bảng khác** để tạo sợi dây liên kết. Ví dụ: Cột `author_id` trong bảng `blogs` là Khóa ngoại trỏ về `id` của bảng `users` $\rightarrow$ Nhờ đó máy tính biết bài blog này do ai viết.
- **Bảng trung gian (Junction Table)**: Sinh ra khi có mối quan hệ **Nhiều - Nhiều (N - N)**. Vì không thể nhét một danh sách nhiều ID vào 1 ô dữ liệu trong MySQL, ta phải tạo một bảng đứng ở giữa chứa 2 khóa ngoại để kết nối chúng lại (ví dụ bảng `blog_tags`).

---

## 3. Phân tích chi tiết 11 mối quan hệ liên kết giữa các bảng

### 🔗 Mối quan hệ 1: `users` $\leftrightarrow$ `blogs` (Quan hệ Một - Nhiều: 1 - N)

- **Bản chất nghiệp vụ**: 1 Tác giả (User) có thể viết **Nhiều** bài viết (Blogs). Nhưng 1 bài Blog tại một thời điểm chỉ thuộc về **Một** tác giả duy nhất.
- **Vị trí khóa ngoại**: Cột `author_id` nằm trong bảng `blogs`, trỏ về khóa chính `id` của bảng `users`.
- **Annotation JPA tương ứng**:
  - Bên `Blog.java`: `@ManyToOne(fetch = FetchType.LAZY) @JoinColumn(name = "author_id") User author;`
  - Bên `User.java`: `@OneToMany(mappedBy = "author", cascade = CascadeType.ALL) List<Blog> blogs;`
- **Câu hỏi vấn đáp**: *"Tại sao khóa ngoại không để ở bảng `users` mà phải để ở bảng `blogs`?"*
  $\rightarrow$ **Trả lời**: *"Dạ thưa Thầy, theo nguyên tắc chuẩn hóa CSDL, Khóa ngoại luôn luôn phải đặt ở bên 'Nhiều'. Nếu để ở bên `users`, khi một tác giả viết 100 bài blog, bảng user sẽ phải chứa 1 mảng 100 mã bài viết trong 1 ô, vi phạm Dạng chuẩn 1 (1NF - Tính nguyên tử của dữ liệu) ạ."*

---

### 🔗 Mối quan hệ 2: `categories` $\leftrightarrow$ `blogs` (Quan hệ Một - Nhiều: 1 - N)

- **Bản chất nghiệp vụ**: 1 Danh mục (ví dụ "Lập trình") có thể chứa **Nhiều** bài viết. Nhưng mỗi bài viết chỉ thuộc về **Một** danh mục chính. (Nếu lưu nháp chưa chọn thì danh mục có thể để trống NULL).
- **Vị trí khóa ngoại**: Cột `category_id` nằm trong bảng `blogs`, trỏ về `id` của bảng `categories`.
- **Annotation JPA tương ứng**:
  - Bên `Blog.java`: `@ManyToOne(fetch = FetchType.LAZY) @JoinColumn(name = "category_id") Category category;`
  - Bên `Category.java`: `@OneToMany(mappedBy = "category") List<Blog> blogs;`

---

### 🔗 Mối quan hệ 3: `blogs` $\leftrightarrow$ `tags` qua bảng trung gian `blog_tags` (Quan hệ Nhiều - Nhiều: N - N)

- **Bản chất nghiệp vụ**:
  - Một bài Blog có thể gắn **Nhiều Thẻ Tag** (ví dụ bài viết này vừa gắn tag `#Java`, vừa gắn tag `#SpringBoot`, vừa gắn tag `#Web`).
  - Ngược lại, một Thẻ Tag (`#Java`) cũng có thể xuất hiện trong **Nhiều bài Blog** khác nhau.
- **Giải pháp kỹ thuật**: Bắt buộc phải tạo **Bảng trung gian `blog_tags`**.
- **Cấu trúc bảng `blog_tags`**:
  - Cột 1: `blog_id` (Khóa ngoại trỏ về `blogs.id`).
  - Cột 2: `tag_id` (Khóa ngoại trỏ về `tags.id`).
  - Cả 2 cột này gộp lại tạo thành **Khóa chính phức hợp (Composite Primary Key)**.
- **Annotation JPA tương ứng** trong `Blog.java`:
  ```java
  @ManyToMany
  @JoinTable(
      name = "blog_tags",
      joinColumns = @JoinColumn(name = "blog_id"),
      inverseJoinColumns = @JoinColumn(name = "tag_id"),
      uniqueConstraints = @UniqueConstraint(columnNames = {"blog_id", "tag_id"})
  )
  Set<Tag> tags = new HashSet<>();
  ```

---

### 🔗 Mối quan hệ 4: `users` $\leftrightarrow$ `user_roles` (Quan hệ Một - Nhiều qua `@ElementCollection`)

- **Bản chất nghiệp vụ**: Một người dùng có thể sở hữu **Nhiều vai trò** (vừa là `USER` bình thường, vừa là `ADMIN` quản trị).
- **Giải pháp kỹ thuật**: Thay vì tạo riêng một class Entity Role phức tạp, JPA hỗ trợ tạo bảng phụ `user_roles` lưu trực tiếp chuỗi String.
- **Cấu trúc bảng `user_roles`**: Cột `user_id` (trỏ về `users.id`) và cột `role` (chứa chữ `"USER"` hoặc `"ADMIN"`).
- **Annotation JPA tương ứng** trong `User.java`:
  ```java
  @ElementCollection(fetch = FetchType.EAGER)
  @CollectionTable(name = "user_roles", joinColumns = @JoinColumn(name = "user_id"))
  @Column(name = "role")
  Set<String> roles = new HashSet<>();
  ```

---

### 🔗 Mối quan hệ 5: `blogs` $\leftrightarrow$ `comments` (Quan hệ Một - Nhiều: 1 - N)

- **Bản chất nghiệp vụ**: 1 bài Blog có thể có **Nhiều** bình luận của độc giả. Mỗi bình luận thuộc về đúng **Một** bài blog.
- **Vị trí khóa ngoại**: Cột `blog_id` nằm trong bảng `comments`, trỏ về `blogs.id`.
- **Annotation JPA tương ứng** trong `Comment.java`:
  ```java
  @ManyToOne(fetch = FetchType.LAZY)
  @JoinColumn(name = "blog_id", nullable = false)
  @OnDelete(action = OnDeleteAction.CASCADE)
  Blog blog;
  ```

---

### 🔗 Mối quan hệ 6: `users` $\leftrightarrow$ `comments` (Quan hệ Một - Nhiều: 1 - N)

- **Bản chất nghiệp vụ**: 1 Người dùng (User) có thể viết **Nhiều** bình luận khác nhau trên khắp website. Mỗi bình luận do đúng **Một** User viết ra.
- **Vị trí khóa ngoại**: Cột `user_id` nằm trong bảng `comments`, trỏ về `users.id`.
- **Annotation JPA tương ứng** trong `Comment.java`:
  ```java
  @ManyToOne(fetch = FetchType.LAZY)
  @JoinColumn(name = "user_id", nullable = false)
  User user;
  ```

---

### 🔗 Mối quan hệ 7: Tự tham chiếu trong chính bảng `comments` (Self-Referencing 1 - N để Reply bình luận)

- **Bản chất nghiệp vụ**: Một người dùng viết bình luận A, người khác có thể bấm "Trả lời" (Reply) vào bình luận A đó $\rightarrow$ Bình luận trả lời chính là "Con" của bình luận A ("Cha").
- **Giải pháp kỹ thuật**: Bảng `comments` tự trỏ khóa ngoại về chính nó!
- **Cấu trúc cột `parent_id`**:
  - Nếu là bình luận gốc (Comment cấp 1): Cột `parent_id = NULL`.
  - Nếu là bình luận trả lời (Reply): Cột `parent_id` sẽ chứa mã `id` của bình luận cha!
- **Annotation JPA tương ứng** trong `Comment.java`:
  ```java
  // Trỏ về bình luận cha (Nhiều con trỏ về 1 cha)
  @ManyToOne(fetch = FetchType.LAZY)
  @JoinColumn(name = "parent_id")
  Comment parent;

  // Danh sách các phản hồi con (1 cha có nhiều con)
  @OneToMany(mappedBy = "parent", cascade = CascadeType.ALL, orphanRemoval = true)
  @OrderBy("createdAt ASC")
  List<Comment> replies;
  ```

---

### 🔗 Mối quan hệ 8: `users` $\leftrightarrow$ `blogs` qua bảng tương tác `blog_likes` (Thả tim)

- **Bản chất nghiệp vụ**: 1 User có thể thả tim Nhiều bài Blog; 1 bài Blog nhận được tim từ Nhiều User.
- **Bảng `blog_likes` gồm**: `id` (PK), `user_id` (FK trỏ `users`), `blog_id` (FK trỏ `blogs`), `created_at`.
- **Ràng buộc chống like gian lận**: `@UniqueConstraint(columnNames = {"user_id", "blog_id"})` $\rightarrow$ MySQL sẽ từ chối nếu 1 user cố tình bấm like 2 lần cho cùng 1 bài!

---

### 🔗 Mối quan hệ 9: `users` $\leftrightarrow$ `blogs` qua bảng `bookmarks` (Lưu bài viết yêu thích)

- **Bản chất nghiệp vụ**: Người dùng bấm nút "Lưu bài viết" để cho vào thư viện cá nhân đọc sau.
- **Bảng `bookmarks` gồm**: `id` (PK), `user_id` (FK trỏ `users`), `blog_id` (FK trỏ `blogs`), `created_at`.
- **Ràng buộc duy nhất**: `@UniqueConstraint(columnNames = {"user_id", "blog_id"})` $\rightarrow$ Một bài chỉ được lưu 1 lần trong danh sách bookmark của user đó.

---

### 🔗 Mối quan hệ 10: `blogs` $\leftrightarrow$ `blog_views` (Lịch sử lượt xem bài viết)

- **Bản chất nghiệp vụ**: Mỗi khi ai đó bấm vào đọc bài viết, hệ thống tạo 1 bản ghi vào bảng `blog_views`.
- **Bảng `blog_views` gồm**: `id` (PK), `blog_id` (FK), `user_id` (FK - có thể để trống NULL nếu là khách chưa đăng nhập), `ip_address` (lưu địa chỉ IP của khách), `viewed_at`.
- **Ý nghĩa**: Giúp thống kê bài viết nào hot nhất và cho phép cả khách vãng lai tăng view.

---

### 🔗 Mối quan hệ 11: Tự tham chiếu giữa 2 Users qua bảng `user_follows` (Theo dõi tác giả)

- **Bản chất nghiệp vụ**: Mạng xã hội thu nhỏ cho phép Độc giả theo dõi Tác giả mình yêu thích.
- **Bảng `user_follows` gồm**:
  - `follower_id` (FK trỏ về `users.id` - người bấm nút Follow).
  - `following_id` (FK trỏ về `users.id` - tác giả được Follow).
  - `created_at`: Ngày bắt đầu theo dõi.
- **Ràng buộc**: Khóa phức hợp Unique `(follower_id, following_id)` và trong code có lệnh chặn `if (follower.equals(following)) throw...` không cho tự theo dõi chính mình.

---

### 🔗 Mối quan hệ 12: `users` $\leftrightarrow$ `notifications` (Thông báo hoạt động)

- **Bản chất nghiệp vụ**: Khi có người Thả tim, Bình luận, hoặc Bấm theo dõi $\rightarrow$ Hệ thống tự sinh 1 dòng thông báo gửi đến người nhận.
- **Bảng `notifications` gồm**: `id` (PK), `user_id` (FK - người nhận thông báo), `message` (nội dung), `target_url` (đường link bấm vào), `type` (`LIKE`, `COMMENT`, `FOLLOW`), `is_read` (đã đọc hay chưa).

---

## 4. Ràng buộc toàn vẹn, Chống gian lận (Unique Constraints) & Xóa tầng (Cascade)

1. **Ràng buộc toàn vẹn Unique Constraint là gì?**
   - Là quy tắc bắt buộc trong MySQL: Không được phép có 2 dòng giống hệt nhau ở những cột chỉ định.
   - Nhóm áp dụng ở:
     - Cột `username` bảng `users`: Không cho phép 2 người đăng ký cùng tên đăng nhập.
     - Cặp `(user_id, blog_id)` trong `blog_likes`: Chống like 2 lần.
     - Cặp `(follower_id, following_id)` trong `user_follows`: Chống theo dõi 2 lần.
     - Cột `name` trong `categories` và `tags`: Không cho tạo 2 danh mục hoặc tag trùng tên.
2. **Cơ chế Xóa Tầng (Cascade Delete) hoạt động thế nào?**
   - Trong code có khai báo: `@OnDelete(action = OnDeleteAction.CASCADE)` tại `Comment`, `BlogLike`, `Bookmark`, `BlogView`.
   - **Tác dụng thực tế**: Nếu tác giả xóa một bài Blog, MySQL sẽ **tự động xóa sạch toàn bộ** bình luận, lượt like, lượt view và bookmark của bài viết đó. Không bị lỗi ràng buộc khóa ngoại mồ côi (Foreign Key Constraint Violation) và không để lại dữ liệu rác trong database!

---

# PHẦN IV: TRỌN BỘ LÝ THUYẾT MÔN HỌC & ĐỀ THI TỰ LUẬN TRÊN GIẤY (22/11/2026)

## Chuyên đề 1: Kiến trúc MVC & Vòng đời HTTP Request (Request Lifecycle)

### 1.1. Bản chất kiến trúc MVC trong Spring Boot

Mô hình MVC (Model - View - Controller) tách biệt ứng dụng thành 3 tầng độc lập:

- **Model**: Đại diện cho trạng thái dữ liệu và quy tắc nghiệp vụ. Trong Spring Boot hiện đại, Model được phân rã thành:
  - *Entity*: Ánh xạ cấu trúc bảng CSDL (Hibernate ORM).
  - *DTO (Data Transfer Object)*: Vận chuyển dữ liệu ra/vào API, lọc các trường nhạy cảm.
  - *Service Layer*: Thực thi logic nghiệp vụ, tính toán, kiểm tra quyền hạn, quản lý `@Transactional`.
  - *Repository Layer*: Thực hiện các câu lệnh SQL/JPQL giao tiếp với Database.
- **View**: Tầng giao diện người dùng. Có 2 dạng:
  - *Server-Side View*: File template (Thymeleaf `.html`, JSP) được máy chủ render sẵn thành mã HTML trước khi gửi về Client.
  - *Client-Side View*: Trình duyệt (Browser / SPA như React, Vue, HTML/JS thuần) tự render giao diện sau khi nhận dữ liệu thô dạng JSON từ REST API.
- **Controller**: Đóng vai trò điều phối (Traffic Router). Tiếp nhận HTTP Request từ Client, gọi Service tương ứng xử lý, và đóng gói dữ liệu vào Model để trả về View (HTML) hoặc Response Body (JSON).

### 1.2. Luồng xử lý chi tiết của một HTTP Request trong Spring Boot (Vòng đời hoàn chỉnh)

Khi một Client gửi một Request (ví dụ `POST /blogs` với header `Authorization: Bearer <token>`), luồng thực thi đi qua 8 bước tuần tự:

```text
[Browser / Postman]
       │
       ▼  (1. HTTP Request: Method + URL + Headers + Body)
[Tomcat Embedded Web Server] (Cổng 8080)
       │
       ▼  (2. Chuỗi lọc Security & CORS)
[SecurityFilterChain] ──> [CorsFilter] ──> [JwtAuthenticationFilter] ──> [CsrfFilter]
       │ (Kiểm tra Token hợp lệ -> Nạp Authentication vào SecurityContextHolder)
       ▼
[DispatcherServlet] (Front Controller trung tâm của Spring MVC)
       │
       ├──> (3. Tra cứu) ──> [HandlerMapping]: Xác định BlogController.createBlog() xử lý URL
       ├──> (4. Gọi hàm) ──> [HandlerAdapter]: Chuyển đổi Request Body JSON thành Java Object (qua HttpMessageConverter/Jackson)
       │
       ▼
[BlogController] (@RestController)
       │ (5. Gọi tầng nghiệp vụ)
       ▼
[BlogService] (@Service - @Transactional)
       │ ├── Lấy user từ SecurityContextHolder
       │ ├── Kiểm tra logic, map DTO -> Entity qua MapStruct
       │ └── Gọi tầng truy xuất dữ liệu
       ▼
[BlogRepository] (@Repository - Spring Data JPA Dynamic Proxy)
       │ (6. Sinh SQL thông qua Hibernate Session/EntityManager)
       ▼
[MySQL Database] (Thực thi INSERT INTO blogs... và lưu trữ bền vững)
       │
       ▼  (7. Entity trả về -> Service đóng gói thành BlogResponse DTO)
[BlogController]
       │
       ▼  (8. Đóng gói kết quả trả về)
   ├── Nếu là @RestController: Jackson chuyển BlogResponse -> JSON String trả về HTTP Body kèm Status Code (200/201).
   └── Nếu là @Controller: ViewResolver tìm file template Thymeleaf (.html), merge dữ liệu và render mã HTML gửi về Browser.
```

---

## Chuyên đề 2: Tầng Model trong thực tế (Entity vs DTO vs Service)

### 2.1. Phân biệt rõ rệt giữa Entity, DTO và Service

1. **Entity (Domain Model)**: Ánh xạ 1-1 với bảng CSDL.
2. **DTO (Data Transfer Object)**: Vận chuyển dữ liệu ra vào API, bảo vệ dữ liệu nhạy cảm.
3. **Service (Business Model)**: Chứa các quy tắc xử lý nghiệp vụ thực tế và giao dịch.

### 2.2. Tại sao CẤM TUYỆT ĐỐI việc dùng trực tiếp Entity làm Model ở tầng API/View?

1. **Chống tấn công Over-posting / Mass Assignment Vulnerability**: Ngăn hacker tự chèn thêm trường quyền `roles: ["ADMIN"]` khi đăng ký.
2. **Ngăn chặn lỗi đệ quy vô tận (Infinite Recursion - Circular Dependency)**: Tránh lỗi `StackOverflowError` khi serialize quan hệ 2 chiều giữa User và Blog sang JSON.
3. **Che giấu thông tin nhạy cảm**: Không làm lộ chuỗi băm mật khẩu `password`.
4. **Tối ưu hóa hiệu năng**: DTO chỉ tải đúng các trường cần hiển thị, tránh kích hoạt nạp Lazy Loading nặng nề.

---

## Chuyên đề 3: Inversion of Control (IoC) & Dependency Injection (DI) Chuyên Sâu

### 3.1. Bản chất IoC và DI

- **IoC (Inversion of Control - Đảo ngược điều khiển)**: Lập trình viên không tự dùng lệnh `new` để tạo đối tượng, mà giao quyền đó cho Spring Framework tự quản lý.
- **DI (Dependency Injection - Tiêm phụ thuộc)**: Kỹ thuật Spring tự động đưa các đối tượng cần thiết vào class đang dùng tại thời điểm chạy.
- **Nguyên lý SOLID tương ứng**: **DIP (Dependency Inversion Principle)**: Module cấp cao phụ thuộc vào Interface trừu tượng, không phụ thuộc class chi tiết.

### 3.2. So sánh toàn diện: Implicit Injection (Ngầm định) vs Explicit Injection (Tường minh)

| Tiêu chí                      | Implicit Injection (Tiêm Ngầm Định)                                                                                                                                 | Explicit Injection (Tiêm Tường Minh)                                                                               |
| :------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| **Định nghĩa**         | Spring tự phát hiện và inject Bean mà **không cần ghi `@Autowired`**.                                                                                    | Lập trình viên phải ghi rõ ràng `@Autowired` hoặc `@Bean`.                                                 |
| **Cơ chế hoạt động** | **Từ Spring 4.3 trở đi**: Class có duy nhất 1 Constructor thì Spring tự tiêm các tham số vào. Kết hợp với `@RequiredArgsConstructor` của Lombok. | Dùng `@Autowired` trên thuộc tính (Field Injection), hoặc cấu hình `@Bean` trong class `@Configuration`. |
| **Khuyến nghị**         | **Chuẩn mực tốt nhất hiện nay (Best Practice)**: Biến được đặt `final` (bất biến, an toàn đa luồng), dễ viết Unit Test độc lập.            | Field Injection bị coi là **Anti-Pattern** vì vi phạm tính đóng gói, không thể đặt `final`.       |

---

## Chuyên đề 4: Cơ Chế Dynamic Proxy & Ngôn Ngữ JPQL Trong Spring Boot & JPA

### 4.1. Câu hỏi cốt lõi: "Repository là truy vấn SQL thường hay là JPA?"
- **CÂU TRẢ LỜI CHÍNH XÁC 100%**: **ĐÂY LÀ 100% JPA (CỤ THỂ LÀ JPQL - JAVA PERSISTENCE QUERY LANGUAGE), TUYỆT ĐỐI KHÔNG PHẢI LÀ SQL THƯỜNG (NATIVE SQL)!**
- **Tại sao dễ bị nhầm là SQL thường?**
  - Vì trong các câu lệnh `@Query` của `BlogRepository.java` có các từ khóa giống SQL như `SELECT`, `FROM`, `WHERE`, `LEFT JOIN`, `ORDER BY`.
- **Nhưng hãy nhìn vào bản chất khác biệt hoàn toàn:**

| Tiêu chí so sánh | SQL Thường (Native SQL) | JPQL (Java Persistence Query Language của JPA) |
| :--- | :--- | :--- |
| **Đối tượng thao tác** | Thao tác trực tiếp trên **TÊN BẢNG** và **TÊN CỘT** vật lý trong cơ sở dữ liệu MySQL. | Thao tác trên **TÊN CLASS JAVA (Entity)** và **TÊN THUỘC TÍNH (Field)** trong mã nguồn Java! |
| **Cú pháp trong dự án** | `SELECT * FROM blogs b WHERE b.is_draft = 0` (tên bảng `blogs` viết thường số nhiều, cột `is_draft`). Phải có cờ `nativeQuery = true` mới chạy được. | `SELECT b FROM Blog b WHERE b.draft = false` (`Blog` là tên class Java viết hoa chữ B, `draft` là thuộc tính `boolean draft;` trong class Java!). Không hề có cờ `nativeQuery = true`. |
| **Thao tác JOIN quan hệ** | `LEFT JOIN blog_likes l ON l.blog_id = b.id` (JOIN dựa trên cột khóa ngoại `blog_id` và `id`). | `LEFT JOIN BlogLike l ON l.blog = b` (`BlogLike` là Entity Java, `l.blog` là thuộc tính đối tượng Java bên trong class đó). |
| **Tính độc lập CSDL** | **Phụ thuộc chặt chẽ vào MySQL**: Dùng hàm riêng của MySQL, nếu mai sau chuyển sang Oracle, PostgreSQL hay SQL Server thì toàn bộ câu lệnh sẽ bị lỗi cú pháp! | **Độc lập 100% với hệ quản trị CSDL (Database Independent)**: Bạn viết JPQL một lần, Hibernate sẽ tự động dịch câu JPQL đó thành đúng phương ngữ (Dialect) SQL của MySQL, PostgreSQL hay Oracle mà không cần sửa 1 dòng code! |

### 4.2. Hai hình thức truy vấn của Spring Data JPA trong Repository:
1. **Derived Query Methods (Tự động sinh câu lệnh qua tên hàm - Không cần viết lệnh nào)**:
   - Trong `UserRepository.java`: `Optional<User> findByUsername(String username);`
   - Trong `CategoryRepository.java`: `boolean existsByName(String name);`
   - Trong `BlogRepository.java`: `List<Blog> findTop5ByDraftFalseOrderByCreatedAtDesc();`
   $\rightarrow$ Lập trình viên không hề viết bất kỳ chữ SQL hay JPQL nào! Spring Data JPA tự động phân tích tên hàm (`findBy...`, `existsBy...`, `countBy...`) để tự sinh ra câu lệnh truy vấn ngầm định!
2. **Custom Query bằng JPQL (Khi cần JOIN phức tạp, gom nhóm GROUP BY, tính toán)**:
   - Dùng annotation `@Query("SELECT b, COUNT(DISTINCT v.id)... FROM Blog b...")`. Hibernate sẽ phân tích cây cú pháp trừu tượng (AST) của JPQL rồi chuyển thành SQL tối ưu cho MySQL.

### 4.3. Tại sao `BlogRepository` chỉ là interface mà vẫn chạy được SQL?
- Nhờ vào **JDK Dynamic Proxy**: Khi ứng dụng khởi động, Spring Boot tự động sinh ra một Class ẩn trong bộ nhớ RAM hiện thực hóa interface đó (`SimpleJpaRepository`).
- Class này bắt chặn các lời gọi hàm, dịch tên phương thức (`findByTitle`) thành câu lệnh SQL tương ứng và chuyển xuống `EntityManager` của Hibernate thực thi vào MySQL.

### 4.4. Dynamic Proxy trong `@Transactional`:
- Spring AOP bọc hàm bằng một Proxy: Mở kết nối $\rightarrow$ Tắt autocommit $\rightarrow$ Chạy lệnh $\rightarrow$ Nếu thành công gọi `commit()`, nếu có lỗi RuntimeException gọi `rollback()`.

---

## Chuyên đề 5: Toàn Bộ Annotation JPA & Hibernate Ánh Xạ CSDL

| Annotation                       | Ý nghĩa & Bản chất kỹ thuật                                               | Ứng dụng trong dự án BTL Blog       |
| :------------------------------- | :------------------------------------------------------------------------------ | :-------------------------------------- |
| **`@Entity`**            | Đánh dấu class Java là thực thể CSDL được Hibernate quản lý.         | `@Entity public class User`           |
| **`@Table`**             | Chỉ định tên bảng thật trong MySQL (`name="blogs"`).                    | `@Table(name="blogs")`                |
| **`@Id`**                | Khóa chính của bảng.                                                        | `@Id UUID id;`                        |
| **`@GeneratedValue`**    | Chiến lược sinh khóa chính (`strategy = GenerationType.UUID`).           | Khóa chính UUID tự sinh              |
| **`@Column`**            | Tùy biến cột: `nullable`, `unique`, `columnDefinition = "LONGTEXT"`.   | Cột nội dung bài viết               |
| **`@ManyToOne`**         | Quan hệ Nhiều - Một (N - 1), bên giữ khóa ngoại. Dùng `fetch = LAZY`. | Nhiều bài viết thuộc 1 tác giả    |
| **`@OneToMany`**         | Quan hệ Một - Nhiều (1 - N), dùng `mappedBy` trỏ về biến đối tác.   | 1 tác giả có nhiều bài viết       |
| **`@ManyToMany`**        | Quan hệ Nhiều - Nhiều (N - N), dùng kèm `@JoinTable` tạo bảng phụ.    | Bài viết và Thẻ Tag (`blog_tags`) |
| **`@JoinColumn`**        | Chỉ định tên cột khóa ngoại (`name = "author_id"`).                    | Cột `author_id` trong bảng blogs    |
| **`@JoinTable`**         | Cấu hình bảng trung gian cho quan hệ N-N.                                   | Bảng phụ `blog_tags`                |
| **`@ElementCollection`** | Lưu một danh sách dữ liệu cơ bản (String) thành bảng phụ.             | Bảng phụ `user_roles` lưu quyền   |
| **`@PrePersist`**        | Tự động chạy trước khi thêm mới (INSERT) vào DB.                       | Tự điền `createdAt = now()`        |
| **`@PreUpdate`**         | Tự động chạy trước khi sửa (UPDATE) vào DB.                             | Tự điền `updatedAt = now()`        |

---

## Chuyên đề 6: Toàn Bộ Annotation Spring Boot, Spring MVC & Lombok

- `@RestController`: Đón request và trả về dữ liệu chữ dạng JSON cho web Single Page.
- `@Controller`: Trả về tên file giao diện HTML Thymeleaf.
- `@Service`: Đánh dấu tầng nghiệp vụ logic.
- `@Repository`: Đánh dấu tầng truy xuất CSDL.
- `@RequestMapping`, `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping`: Ánh xạ các đường dẫn URL và phương thức HTTP.
- `@PathVariable`: Lấy biến từ URL (ví dụ: `/blogs/{id}`).
- `@RequestParam`: Lấy tham số sau dấu hỏi chấm (ví dụ: `/search?keyword=java`).
- `@RequestBody`: Nhận dữ liệu JSON từ Client chuyển thành Object Java.
- `@Valid`: Kích hoạt kiểm tra tính hợp lệ dữ liệu (độ dài mật khẩu, email hợp lệ).
- `@RequiredArgsConstructor`: Tạo constructor cho các biến `final` $\rightarrow$ Thực hiện tiêm phụ thuộc Implicit DI.
- `@Builder`: Cho phép tạo đối tượng nhanh chóng: `User.builder().username("...").build()`.

---

## Chuyên đề 7: Quản Lý Giao Dịch @Transactional & Tính Chất ACID

- **4 tính chất ACID**:
  1. *Atomicity (Nguyên tử)*: Thành công tất cả hoặc hủy bỏ tất cả (Rollback).
  2. *Consistency (Nhất quán)*: Dữ liệu luôn đúng quy tắc ràng buộc CSDL.
  3. *Isolation (Cô lập)*: Các giao dịch chạy song song không nhìn thấy dữ liệu dở dang của nhau.
  4. *Durability (Bền vững)*: Đã lưu là an toàn vĩnh viễn trong ổ cứng MySQL kể cả khi tắt điện.
- **Vị trí đặt**: Đặt tại tầng **Service** để phối hợp nhiều thao tác ghi dữ liệu từ nhiều Repository khác nhau trong cùng một luồng nghiệp vụ.

---

## Chuyên đề 8: Bảo Mật Stateless JWT & Spring Security 6 vs Session Cookie

| Tiêu chí                | Stateless JWT (Dự án BTL đang dùng)                                                                 | Stateful Session Cookie (Cũ)                                          |
| :------------------------ | :------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------- |
| **Lưu trữ**       | Server **không lưu Session trên RAM**. Client lưu token ở `localStorage`.                  | Server lưu phiên trên RAM, Client giữ `JSESSIONID` qua Cookie.   |
| **Mở rộng**       | Cực kỳ tốt cho Microservices và nhiều cụm server.                                                 | Khó mở rộng, phải dùng Redis để chia sẻ RAM giữa các server. |
| **Tấn công CSRF** | Miễn nhiễm với CSRF $\rightarrow$ **Nên tắt `csrf.disable()` là hoàn toàn an toàn**. | Dễ bị tấn công CSRF nếu không có mã phòng ngừa.              |

---

## Chuyên đề 9: So Sánh Server-Side Rendering (SSR) vs Client-Side Rendering (CSR)

- **SSR (Thymeleaf)**: Máy chủ tự render mã HTML hoàn chỉnh rồi gửi về. Ưu điểm: Chuẩn SEO.
- **CSR (REST API + Fetch JS)**: Máy chủ trả về JSON, trình duyệt tự vẽ giao diện. Ưu điểm: Mượt mà, không giật màn hình khi tải trang.
- **Mô hình Hybrid của BTL**: Dùng Thymeleaf để phân phối khung trang ban đầu, sau đó toàn bộ chức năng (Đăng nhập, Like, Comment, Đăng bài) đều chạy bằng Fetch API bất đồng bộ.

---

## Chuyên đề 10: 10 Công Cụ Cốt Lõi Trong Môn Học Của Thầy Phúc

1. **Java 21 (LTS)**: Ngôn ngữ nền tảng hướng đối tượng.
2. **Spring Boot 3.5.11**: Bộ khung phát triển web hiện đại.
3. **Apache Maven**: Quản lý thư viện phụ thuộc qua `pom.xml`.
4. **MySQL Server Local & Workbench**: Hệ quản trị CSDL quan hệ bền vững.
5. **Hibernate ORM & Spring Data JPA**: Ánh xạ đối tượng Java với bảng CSDL.
6. **Thymeleaf & RESTful API**: Công nghệ hiển thị giao diện và truyền tải JSON.
7. **Postman**: Công cụ kiểm thử độc lập các đầu API Backend.
8. **Git & GitHub**: Quản lý mã nguồn phân tán và cộng tác nhóm.
9. **Project Lombok**: Loại bỏ code thừa (Getter, Setter, Builder).
10. **VS Code / IntelliJ IDEA**: Môi trường lập trình chuyên nghiệp.

---

# PHẦN V: PHÂN TÍCH TỪNG DÒNG CODE & MỌI CHỨC NĂNG TRONG DỰ ÁN BTL

*(Phần này đi qua từng file mã nguồn, phân tích mục đích, vị trí và công năng từng hàm để bạn trả lời mọi câu hỏi của Thầy)*

## Mục 1: Tầng Cấu Hình (Configuration Package)

### 1.1. `SecurityConfig.java` — Trái tim bảo mật hệ thống

- **Vị trí**: `src/main/java/com/group/blog/config/SecurityConfig.java`
- **Công dụng**: Cấu hình Spring Security 6 theo kiến trúc Stateless JWT.
- **Phân tích từng thành phần**:
  - `PUBLIC_POST_ENDPOINTS`: Các đường dẫn `POST` không cần đăng nhập (`/users` để đăng ký, `/auth/login` để lấy token, `/auth/introspect` kiểm tra token).
  - `PUBLIC_GET_ENDPOINTS`: Toàn bộ các trang HTML giao diện, các file tĩnh CSS/JS, và API xem bài viết công khai (`/categories`, `/tags`, `/blogs/**`).
  - `ADMIN_ENDPOINTS = {"/api/admin/**"}`: Các API dữ liệu thống kê quản trị chỉ cho phép tài khoản có quyền `ROLE_ADMIN` gọi.
  - `filterChain(HttpSecurity httpSecurity)`:
    - `.cors()`: Bật hỗ trợ truy cập đa nguồn từ trình duyệt.
    - `.headers(headers -> headers.frameOptions(frame -> frame.disable()))`: Cho phép nhúng iframe nếu cần.
    - `.authorizeHttpRequests(...)`: Định tuyến phân quyền chi tiết cho từng phương thức HTTP.
    - `.oauth2ResourceServer(...)`: Tự động giải mã Bearer Token trong Header HTTP thông qua `jwtDecoder()`.
    - `.csrf(AbstractHttpConfigurer::disable)`: **Tắt CSRF vì hệ thống dùng Token JWT, không dùng Cookie nên miễn nhiễm với CSRF**.
    - `.sessionManagement(session -> session.sessionCreationPolicy(SessionCreationPolicy.STATELESS))`: **Yêu cầu Spring không lưu Session trên RAM**.
  - `jwtAuthenticationConverter()`: Trích xuất trường `scope` trong Token (ví dụ `"ADMIN"`) và tự động thêm tiền tố `"ROLE_"` thành `"ROLE_ADMIN"` để phương thức `.hasRole("ADMIN")` của Spring nhận diện được.
  - `jwtDecoder()`: Sử dụng thuật toán băm cực mạnh `HmacSHA512` kết hợp `SIGNER_KEY` để giải mã và kiểm tra chữ ký số của token.
  - `passwordEncoder()`: Khởi tạo Bean `BCryptPasswordEncoder(10)` phục vụ băm mật khẩu một chiều với 10 vòng lặp muối (salt rounds).

### 1.2. `ApplicationInitConfig.java` — Tự động khởi tạo dữ liệu mẫu khi khởi động

- **Vị trí**: `src/main/java/com/group/blog/config/ApplicationInitConfig.java`
- **Công dụng**: Sử dụng `ApplicationRunner` để kiểm tra xem tài khoản `admin` đã có trong MySQL chưa. Nếu chưa có (chạy lần đầu):
  - Tự động tạo 1 tài khoản quản trị `admin` (`password: 123456`, quyền `ADMIN` và `USER`).
  - Tự động tạo 3 tài khoản cho 3 thành viên nhóm: `duonghd` (24743991), `dungnt` (24000905), `longlt` (23630851).
  - Tự động tạo 4 Danh mục mẫu (`Technology`, `Programming`, `Web Design`, `Life & Tips`).
  - Tự động tạo 5 Thẻ Tag mẫu (`Java`, `SpringBoot`, `Bootstrap`, `Thymeleaf`, `AI`).
  - Tự động tạo 3 Bài viết Blog mẫu kèm hình ảnh banner, tác giả, danh mục và thẻ tag.

### 1.3. `CloudinaryConfig.java` & `CloudinaryService.java` — Quản lý tải ảnh đám mây

- **Vị trí**: `src/main/java/com/group/blog/config/CloudinaryConfig.java` và `src/main/java/com/group/blog/service/CloudinaryService.java`
- **Công dụng**:
  - Dùng Annotation `@Value("${cloudinary.cloud-name}")` để nạp thông số kết nối từ file `application-secret.yml`.
  - Khởi tạo Bean `Cloudinary` đưa vào Spring Context.
  - Phương thức `uploadImage(MultipartFile file)` nhận mảng byte nhị phân của file ảnh tải lên từ form, gửi lên dịch vụ Cloudinary và trả về đường link URL công khai (`https://res.cloudinary.com/...`).

---

## Mục 2: Tầng Thực Thể (Entity Package - 10 Entities)

### 2.1. `User.java` (Bảng `users`)

- Khóa chính `@Id @GeneratedValue(strategy = GenerationType.UUID) UUID id`: Khóa chính định dạng UUID ngẫu nhiên 128-bit chống dò quét ID.
- `@Column(nullable = false, unique = true, length = 100) String username`: Tên đăng nhập không được trùng, không được rỗng.
- `@Column(nullable = false, length = 255) String password`: Lưu chuỗi băm BCrypt dài 60 ký tự.
- `@ElementCollection(fetch = FetchType.EAGER) @CollectionTable(name = "user_roles", joinColumns = @JoinColumn(name = "user_id")) Set<String> roles`: Tạo bảng phụ `user_roles` lưu danh sách vai trò (`ROLE_USER`, `ROLE_ADMIN`). Tải EAGER để kiểm tra quyền hạn ngay lập tức khi đăng nhập.
- `@OneToMany(mappedBy = "author", cascade = CascadeType.ALL) List<Blog> blogs`: Một user có thể viết nhiều bài.
- `@PrePersist void prePersist()`: Tự động điền ngày tạo `createdAt = LocalDateTime.now()` trước khi lưu xuống DB.

### 2.2. `Blog.java` (Bảng `blogs`)

- `String title`, `String banner`, `String description`: Tiêu đề, ảnh bìa và mô tả ngắn bài viết.
- `@Column(columnDefinition = "LONGTEXT") String content`: Nội dung bài viết chính thức đã xuất bản, lưu trữ bằng kiểu `LONGTEXT` trong MySQL (chứa được đến 4GB dữ liệu văn bản/HTML).
- `boolean draft`: Cờ đánh dấu trạng thái (true: bản nháp, false: bài đã xuất bản công khai).
- `@Column(columnDefinition = "LONGTEXT") String draftContent` & `draftBanner`: **Cơ chế lưu nháp bài viết đang sửa**. Cho phép tác giả sửa bài đã public mà người đọc bên ngoài vẫn đọc bản cũ; khi nào bấm Publish thì nội dung từ `draftContent` mới đổ sang `content`.
- `@ManyToOne(fetch = FetchType.LAZY) @JoinColumn(name = "author_id") User author`: Khóa ngoại trỏ về tác giả bài viết.
- `@ManyToOne(fetch = FetchType.LAZY) @JoinColumn(name = "category_id") Category category`: Khóa ngoại trỏ về danh mục bài viết.
- `@ManyToMany @JoinTable(name = "blog_tags", joinColumns = @JoinColumn(name = "blog_id"), inverseJoinColumns = @JoinColumn(name = "tag_id")) Set<Tag> tags`: Quan hệ N-N tạo bảng trung gian `blog_tags`.
- `@PreUpdate void preUpdate()`: Tự động cập nhật `updatedAt = LocalDateTime.now()` mỗi khi có chỉnh sửa.

### 2.3. `Comment.java` (Bảng `comments`)

- `@Table(name="comments", indexes = {@Index(name="idx_comment_blog", columnList="blog_id"), @Index(name="idx_comment_parent", columnList="parent_id")})`: Đánh chỉ mục Index trên cột `blog_id` và `parent_id` để tăng tốc độ truy vấn bình luận của bài viết.
- `@ManyToOne(fetch = FetchType.LAZY) @JoinColumn(name = "parent_id") Comment parent`: **Quan hệ tự tham chiếu (Self-referencing)**. Trỏ về bình luận cha nếu đây là một phản hồi (reply).
- `@OneToMany(mappedBy = "parent", cascade = CascadeType.ALL, orphanRemoval = true) @OrderBy("createdAt ASC") List<Comment> replies`: Danh sách các reply con của bình luận này, tự động sắp xếp theo thứ tự thời gian tăng dần.

### 2.4. `BlogLike.java` & `Bookmark.java`

- Khóa phức hợp duy nhất `@Table(name="blog_likes", uniqueConstraints = {@UniqueConstraint(columnNames = {"user_id","blog_id"})})`: Ngăn chặn tuyệt đối việc một người dùng bấm like hoặc bookmark một bài viết 2 lần ở tầng CSDL.
- `@OnDelete(action = OnDeleteAction.CASCADE)`: Khi bài viết gốc bị xóa, toàn bộ lượt like và bookmark liên quan sẽ tự động bị xóa theo (xóa tầng CSDL, không gây lỗi khóa ngoại).

### 2.5. `UserFollow.java` (Bảng `user_follows`)

- `@ManyToOne User follower`: Người đi theo dõi.
- `@ManyToOne User following`: Tác giả được theo dõi.
- Ràng buộc `@UniqueConstraint(columnNames = {"follower_id", "following_id"})`: Chặn theo dõi trùng lặp.

### 2.6. `Notification.java` (Bảng `notifications`)

- Lưu các thông báo người dùng (`LIKE`, `COMMENT`, `REPLY`, `FOLLOW`).
- `String targetUrl`: Đường dẫn trang web kèm tham số (ví dụ: `post.html?id=java-slug&openComments=true`) để khi người dùng click vào thông báo sẽ tự động nhảy đến đúng bài viết và tự mở khung bình luận.

---

## Mục 3: Tầng Truy Xuất Dữ Liệu (Repository Package & Phân Tích JPQL)

### 3.1. Phân tích truy vấn JPQL phức tạp trong `BlogRepository.java`

```java
@Query("""
   SELECT b, COUNT(DISTINCT v.id), COUNT(DISTINCT l.id), COUNT(DISTINCT c.id)
   FROM Blog b
   LEFT JOIN BlogLike l ON l.blog = b
   LEFT JOIN BlogView v ON v.blog = b
   LEFT JOIN Comment c ON c.blog = b
   WHERE b.draft = false
   GROUP BY b
   ORDER BY b.publishedAt DESC
""")
List<Object[]> findAllBlogsWithCounts();
```

- **Ý nghĩa câu hỏi vấn đáp**: *"Tại sao phải dùng `LEFT JOIN` và `COUNT(DISTINCT ...)` mà không dùng `COUNT(...)` thông thường?"*
  - **Trả lời**:
    1. Dùng `LEFT JOIN` vì nếu bài viết chưa có lượt like, view hoặc comment nào thì bài viết đó vẫn được lấy ra (nếu dùng `INNER JOIN` thì bài viết mới tạo chưa có like/comment sẽ bị biến mất khỏi trang chủ!).
    2. Phải dùng `COUNT(DISTINCT v.id)` vì khi JOIN 3 bảng quan hệ 1-N cùng lúc, SQL sẽ tạo ra **Tích Đề-các (Cartesian Product)** làm nhân chéo các dòng dữ liệu. Nếu bài viết có 2 views, 3 likes và 4 comments thì số dòng sinh ra sẽ là $2 \times 3 \times 4 = 24$ dòng! Nếu dùng `COUNT(v.id)` thì view sẽ thành 24 (sai thực tế). Dùng `COUNT(DISTINCT v.id)` bảo đảm chỉ đếm các ID view duy nhất, trả về con số chính xác 100%.

---

## Mục 4: Tầng Nghiệp Vụ (Service Package - Phân Tích Từng Phương Thức)

### 4.1. `AuthenticationService.java`

1. `authenticate(AuthenticationRequest request)`:
   - Tìm user theo `username`, nếu không thấy ném ngoại lệ `USER_NOT_EXITED`.
   - Dùng `passwordEncoder.matches(request.getPassword(), user.getPassword())` để so khớp mật khẩu nhập vào với chuỗi băm BCrypt trong CSDL.
   - Nếu khớp, thiết lập hạn sử dụng token là 1 giờ (`Instant.now().plus(1, ChronoUnit.HOURS)`), gọi `generateToken()` sinh chuỗi JWT và trả về `AuthenticationResponse`.
2. `generateToken(User user, Date expiryTime)`:
   - Tạo Header định nghĩa thuật toán `HS512`.
   - Tạo Payload chứa các Claim: `sub` (username), `iss` ("group.com"), `iat` (ngày cấp), `exp` (ngày hết hạn), `scope` (chuỗi quyền, ví dụ `"ADMIN USER"`).
   - Dùng `MACSigner(SIGNER_KEY.getBytes())` ký điện tử và xuất ra chuỗi JWT định dạng `header.payload.signature`.
3. `introspect(IntrospectRequest request)`:
   - Nhận token từ client, kiểm tra tính hợp lệ của chữ ký và thời gian hết hạn (`expirationTime`). Trả về boolean `true`/`false`.

### 4.2. `UserService.java`

1. `createUser(UserCreatetionRequest request)`:
   - Kiểm tra `existsByUsername()`, nếu trùng ném `USER_EXITED`.
   - Dùng `userMapper.toUser(request)` ánh xạ sang Entity.
   - Băm mật khẩu bằng `passwordEncoder.encode()`.
   - Gán quyền mặc định `ROLE_USER` và lưu xuống CSDL MySQL.
2. `getMyProfile()`:
   - Trích xuất username trực tiếp từ `SecurityContextHolder.getContext().getAuthentication().getName()`.
   - Tìm user trong DB và làm giàu dữ liệu qua `followService.enrichUserResponse()` (tính tổng số follower, following).
3. `changePassword(PasswordChangeRequest request)`:
   - Lấy user đang đăng nhập từ SecurityContext.
   - So sánh mật khẩu cũ bằng `passwordEncoder.matches()`.
   - Kiểm tra mật khẩu mới và xác nhận mật khẩu có khớp nhau không.
   - Băm mật khẩu mới và lưu đè vào CSDL.
4. `updateUser(UUID id, UserUpdateRequest request)`:
   - Hàm dành cho Quản trị viên cập nhật thông tin và phân quyền cho người dùng.
   - Dùng `u.getRoles().clear()` xóa toàn bộ quyền cũ và `u.getRoles().addAll(request.getRoles())` nạp danh sách quyền mới (ví dụ thăng cấp User thành Admin).

### 4.3. `BlogService.java`

1. `createBlog(BlogCreationRequest request)`:
   - Lấy tác giả từ SecurityContext.
   - Tìm kiếm Danh mục (Category) nếu người dùng có chọn.
   - Xử lý Tag thông minh: Quét từng tên tag trong danh sách, nếu tag đã có trong DB thì lấy lại, nếu chưa có thì tự động tạo mới vào bảng `tags` (`tagRepository.save(newTag)`).
   - Lưu bài viết và gọi `enrichBlogResponse()` để sinh slug SEO và nạp số lượng view/like/comment.
2. `updateBlog(UUID id, BlogUpdateRequest request)`:
   - Kiểm tra quyền tác giả: Chỉ người tạo bài viết mới được sửa (`blog.getAuthor().getUsername().equals(currentUsername)`), nếu không ném lỗi `UNAUTHORIZED`.
   - **Xử lý luồng Lưu Nháp vs Xuất Bản**:
     - *Nếu user bấm Save Draft (`request.getDraft() == true`)*: Nếu bài đã từng publish trước đó, không được sửa cột `content` công khai mà lưu vào `draftContent` để người đọc bên ngoài không bị ảnh hưởng.
     - *Nếu user bấm Publish (`request.getDraft() == false`)*: Đổ toàn bộ nội dung mới vào cột `content`, xóa rỗng cột `draftContent = null`, set `draft = false`, cập nhật `publishedAt`.
3. `getBlogById(UUID id)`:
   - Lấy bài viết từ DB.
   - Tự động tạo một bản ghi `BlogView` lưu xuống bảng `blog_views` để tăng lượt đọc.
   - Trả về DTO kèm thông tin kiểm tra xem tài khoản đang đăng nhập đã like hoặc bookmark bài này chưa (`likedByCurrentUser`, `bookmarkedByCurrentUser`).
4. `deleteBlog(UUID id)`:
   - Kiểm tra: Người thực hiện phải là **Tác giả bài viết** HOẶC **Quản trị viên (`ROLE_ADMIN`)** mới có quyền xóa. Nếu không ném lỗi `UNAUTHORIZED`.
5. `filterBlogs(String keyword, UUID categoryId)`:
   - Lọc đa điều kiện: Vừa theo từ khóa tìm kiếm (tiêu đề), vừa theo danh mục được chọn.
6. `getSearchSuggestions(String keyword)`:
   - Tìm kiếm nhanh 5 bài viết khớp với từ khóa người dùng đang gõ trên thanh tìm kiếm để hiển thị menu gợi ý tức thì (Live search suggestion) kèm tên tác giả và danh mục.

### 4.4. `InteractionService.java`

1. `toggleLike(UUID blogId)`:
   - Kiểm tra trong bảng `blog_likes`: Nếu đã like rồi thì xóa bản ghi (Unlike); nếu chưa like thì tạo bản ghi mới (Like) và gửi thông báo `LIKE` cho tác giả bài viết qua `notificationService`.
2. `addComment(UUID blogId, CommentRequest request)`:
   - Tạo comment mới. Nếu có `parentId`, tìm comment cha và gán vào quan hệ phân cấp.
   - Gửi thông báo: Nếu là bình luận trực tiếp thì báo cho Tác giả bài viết (`COMMENT`); nếu là reply thì báo cho Chủ comment cha (`REPLY`).
3. `deleteComment(UUID commentId)`:
   - **Bảo mật phân quyền**: Chỉ có **Tác giả của bình luận đó** HOẶC **Chủ sở hữu của bài viết đó** mới có quyền xóa comment.

### 4.5. `FollowService.java`

1. `toggleFollow(String targetUsername)`:
   - Chặn không cho tự follow chính mình: `if (currentUsername.equals(targetUsername)) throw ...`.
   - Nếu đã follow thì xóa bản ghi (Unfollow); nếu chưa thì tạo bản ghi `UserFollow` và gửi thông báo `FOLLOW` đến người được theo dõi.

---

## Mục 5: Tầng Điều Khiển (Controller Package - Phân Tích Từng Endpoint)

| Controller Class                       | Endpoint URL                                           | HTTP Method | Chức năng nghiệp vụ & Quyền hạn                                                                                       |
| :------------------------------------- | :----------------------------------------------------- | :---------- | :-------------------------------------------------------------------------------------------------------------------------- |
| **`AuthenticationController`** | `/auth/login`                                        | `POST`    | Tiếp nhận username/password, xác thực và trả về JWT Token. (Public)                                                  |
|                                        | `/auth/introspect`                                   | `POST`    | Kiểm tra token có hợp lệ không. (Public)                                                                               |
| **`UserController`**           | `/users`                                             | `POST`    | Đăng ký tài khoản người dùng mới. (Public)                                                                         |
|                                        | `/users`                                             | `GET`     | Lấy danh sách toàn bộ người dùng trong hệ thống. (Yêu cầu `ROLE_ADMIN`)                                        |
|                                        | `/users/my-profile`                                  | `GET`     | Lấy thông tin cá nhân của người đang đăng nhập. (Đã đăng nhập)                                              |
|                                        | `/users/my-profile`                                  | `PUT`     | Cập nhật email, bio, avatar của tôi. (Đã đăng nhập)                                                                |
|                                        | `/users/my-profile/change-password`                  | `PUT`     | Đổi mật khẩu cá nhân. (Đã đăng nhập)                                                                             |
|                                        | `/users/profile/{username}`                          | `GET`     | Xem trang hồ sơ công khai của một tác giả bất kỳ. (Public)                                                         |
| **`BlogController`**           | `/blogs`                                             | `POST`    | Tạo bài viết mới. (Đã đăng nhập)                                                                                   |
|                                        | `/blogs`                                             | `GET`     | Lấy danh sách bài viết trang chủ kèm lượt xem/thích/bình luận. (Public)                                          |
|                                        | `/blogs/{id}`                                        | `GET`     | Xem chi tiết bài viết và tự động tăng view. (Public)                                                                |
|                                        | `/blogs/{id}`                                        | `PUT`     | Cập nhật bài viết (Tác giả). (Đã đăng nhập)                                                                      |
|                                        | `/blogs/{id}`                                        | `DELETE`  | Xóa bài viết (Tác giả hoặc Admin). (Đã đăng nhập)                                                                |
|                                        | `/blogs/category/{categoryId}`                       | `GET`     | Lọc danh sách bài viết theo Danh mục. (Public)                                                                         |
|                                        | `/blogs/tag/{tagId}`                                 | `GET`     | Lọc danh sách bài viết theo Thẻ Tag. (Public)                                                                          |
|                                        | `/blogs/search`                                      | `GET`     | Tìm kiếm bài viết theo từ khóa tiêu đề. (Public)                                                                   |
|                                        | `/blogs/search/suggestions`                          | `GET`     | Gợi ý top 5 bài viết nhanh khi đang gõ phím. (Public)                                                                |
|                                        | `/blogs/filter`                                      | `GET`     | Lọc kết hợp từ khóa và danh mục. (Public)                                                                            |
|                                        | `/blogs/my-blogs`                                    | `GET`     | Lấy danh sách bài viết của tôi (kể cả bản nháp). (Đã đăng nhập)                                              |
| **`InteractionController`**    | `/blogs/{blogId}/like`                               | `POST`    | Thả tim / Bỏ thả tim bài viết. (Đã đăng nhập)                                                                     |
|                                        | `/blogs/{blogId}/comments`                           | `GET`     | Lấy danh sách bình luận phân cấp của bài viết. (Public)                                                            |
|                                        | `/blogs/{blogId}/comments`                           | `POST`    | Thêm bình luận hoặc phản hồi (reply). (Đã đăng nhập)                                                             |
|                                        | `/blogs/comments/{commentId}`                        | `DELETE`  | Xóa bình luận (Tác giả comment hoặc Chủ bài viết). (Đã đăng nhập)                                             |
|                                        | `/blogs/{blogId}/bookmark`                           | `POST`    | Lưu / Bỏ lưu bài viết vào danh sách đọc sau. (Đã đăng nhập)                                                   |
|                                        | `/blogs/bookmarks`                                   | `GET`     | Lấy danh sách các bài viết tôi đã lưu. (Đã đăng nhập)                                                         |
| **`FollowController`**         | `/users/{username}/follow`                           | `POST`    | Theo dõi / Bỏ theo dõi tác giả. (Đã đăng nhập)                                                                    |
|                                        | `/users/{username}/followers`                        | `GET`     | Lấy danh sách người theo dõi của tác giả. (Public)                                                                  |
|                                        | `/users/{username}/following`                        | `GET`     | Lấy danh sách tác giả mà người này đang theo dõi. (Public)                                                        |
| **`NotificationController`**   | `/api/notifications`                                 | `GET`     | Lấy danh sách thông báo của tôi. (Đã đăng nhập)                                                                  |
|                                        | `/api/notifications/{id}/read`                       | `PUT`     | Đánh dấu thông báo đã đọc. (Đã đăng nhập)                                                                     |
|                                        | `/api/notifications/{id}`                            | `DELETE`  | Xóa một thông báo. (Đã đăng nhập)                                                                                  |
| **`AdminController`**          | `/api/admin/stats`                                   | `GET`     | Lấy số liệu thống kê (Tổng user, tổng post, 5 bài mới nhất) cho trang Dashboard Admin. (Yêu cầu `ROLE_ADMIN`) |
| **`UploadController`**         | `/upload/image`                                      | `POST`    | Tải file ảnh lên Cloudinary và nhận đường link URL. (Đã đăng nhập)                                             |
| **`ViewController`**           | `/`, `/home`, `/login`, `/post`, `/admin/**` | `GET`     | Điều hướng hiển thị các file template HTML Thymeleaf. (Public)                                                       |

---

## Mục 6: Xử Lý Ngoại Lệ & Tiện Ích (Exception & SlugUtils)

### 6.1. Xử lý ngoại lệ tập trung với `GlobalExceptionHandler.java`

- `@ControllerAdvice`: Bắt chặn mọi Exception xảy ra ở bất kỳ Controller nào trong toàn bộ ứng dụng.
- Phương thức `@ExceptionHandler(value = AppException.class)`:
  - Bắt các lỗi nghiệp vụ do lập trình viên chủ động ném ra (`throw new AppException(ErrorCode.USER_NOT_EXITED)`).
  - Trích xuất mã lỗi `code` và thông điệp `message` từ Enum `ErrorCode` đóng gói vào `ApiResponse` chuẩn trả về cho Client với HTTP Status 400 Bad Request.
- Phương thức `@ExceptionHandler(value = MethodArgumentNotValidException.class)`:
  - Bắt các lỗi vi phạm ràng buộc dữ liệu đầu vào khi dùng `@Valid` trên Request Body (ví dụ mật khẩu dưới 8 ký tự).
- Phương thức `@ExceptionHandler(value = Exception.class)`:
  - Tấm lưới an toàn cuối cùng bắt mọi lỗi không lường trước được (lỗi hệ thống, null pointer), trả về mã `9999` với thông điệp "Uncategorized error", bảo đảm không bao giờ để lộ vết lỗi hệ thống (Stacktrace) ra ngoài Client.

### 6.2. Tiện ích tạo đường dẫn thân thiện SEO `SlugUtils.java`

- **Mục đích**: Chuyển đổi tiêu đề bài viết tiếng Việt có dấu thành chuỗi URL không dấu ngăn cách bằng gạch nối:
  - Chuỗi gốc: `"Học Spring Boot 3 & JPA: Xây dựng Blog từ A-Z!"`
  - Chuỗi sau xử lý: `"hoc-spring-boot-3-jpa-xay-dung-blog-tu-a-z"`
- **Các bước kỹ thuật trong hàm `generateSlug()`**:
  1. Chuyển chữ thường `.toLowerCase()` và cắt khoảng trắng 2 đầu `.trim()`.
  2. Tách dấu tiếng Việt bằng chuẩn hóa Unicode NFD: `Normalizer.normalize(slug, Normalizer.Form.NFD)`.
  3. Xóa các ký tự dấu tổ hợp bằng biểu thức chính quy Regex: `\\p{InCombiningDiacriticalMarks}+`.
  4. Thay thế ký tự đặc biệt tiếng Việt: Chuyển `"đ"` thành `"d"`.
  5. Thay thế toàn bộ ký tự không phải chữ và số thành dấu gạch ngang: `[^a-z0-9]+` $\rightarrow$ `"-"`.
  6. Gộp nhiều dấu gạch ngang liên tiếp thành 1 dấu: `"-+"` $\rightarrow$ `"-"`.

---

## Mục 7: Tầng Giao Diện & Frontend JavaScript Giao Tiếp API

### 7.1. File `register.html` — Đăng ký & Tự động đăng nhập

- Bắt sự kiện `submit` form, gọi `event.preventDefault()` chặn reload trang.
- Kiểm tra tính hợp lệ ở client (độ dài username $\ge 3$, password $\ge 6$, mật khẩu xác nhận trùng khớp).
- Gửi `fetch('/users', { method: 'POST', body: JSON })`.
- Nếu thành công, tự động kích hoạt hàm `autoLogin()` gửi tiếp request tới `/auth/login` để lấy Token JWT và lưu vào `localStorage.setItem('token', token)` rồi chuyển hướng về trang chủ `/`.

### 7.2. File `nav.js` — Phân quyền hiển thị Menu Admin

- Trích xuất `token` từ `localStorage`.
- Giải mã phần Payload Base64 của JWT bằng `window.atob(token.split('.')[1])`.
- Đọc trường `scope`: Nếu chuỗi quyền có chứa chữ `"ADMIN"`, dùng jQuery `$('#btn-desk-admin').show()` để hiển thị nút vào trang quản trị Admin Controller. Nếu là User thường thì ẩn nút này đi.

---

# PHẦN VI: BỘ 25 CÂU HỎI VẤN ĐÁP "XOÁY TẬN TỪNG DÒNG CODE" & KỊCH BẢN ĐẠT ĐIỂM 10

### Q1: "Trong class `BlogService`, tại sao em không dùng `@Autowired` để tiêm các Repository mà lại dùng `@RequiredArgsConstructor`?"

- **Trả lời chuẩn**:
  *"Dạ thưa Thầy, đây là kỹ thuật **Implicit Dependency Injection (Tiêm ngầm định)** theo chuẩn mực mới nhất của Spring. Khi dùng `@RequiredArgsConstructor` của Lombok, Lombok sẽ tự động tạo một Constructor chứa tất cả các biến khai báo `final` (`private final BlogRepository blogRepository;`). Kể từ phiên bản Spring 4.3 trở đi, khi một Class chỉ có duy nhất một Constructor, Spring IoC Container sẽ tự động inject các Bean vào mà **không cần phải viết `@Autowired`**. Cách này giúp các biến có tính bất biến (`final`), an toàn đa luồng và giúp nhóm viết Unit Test cực kỳ dễ dàng mà không bị phụ thuộc vào Spring Container ạ."*

### Q2: "Trong class `Comment.java`, tại sao lại có quan hệ `@ManyToOne Comment parent` và `@OneToMany List<Comment> replies` trỏ ngược lại chính nó?"

- **Trả lời chuẩn**:
  *"Dạ thưa Thầy, đây là mô hình quan hệ **Tự tham chiếu (Self-Referencing Relationship)**. Trong thực tế, hệ thống blog cần hỗ trợ tính năng bình luận phân cấp: một người có thể trả lời (reply) bình luận của người khác. Khi đó, bình luận con sẽ có trường `parent_id` trỏ về khóa chính `id` của bình luận cha trong cùng bảng `comments`. Bình luận gốc cấp cao nhất sẽ có `parent_id = NULL` ạ."*

### Q3: "Tại sao trong `BlogRepository.java` em phải viết `COUNT(DISTINCT v.id)` mà không viết `COUNT(v.id)` thông thường?"

- **Trả lời chuẩn**:
  *"Dạ thưa Thầy, trong câu truy vấn lấy danh sách bài viết, nhóm em thực hiện `LEFT JOIN` đồng thời 3 bảng quan hệ Một - Nhiều là `blog_views`, `blog_likes` và `comments`. Thao tác JOIN nhiều bảng 1-N cùng lúc sẽ tạo ra **Tích Đề-các (Cartesian Product)** làm nhân chéo số dòng dữ liệu. Nếu không có từ khóa `DISTINCT`, hàm `COUNT` sẽ đếm tất cả các dòng bị nhân chéo dẫn đến số view, like và comment bị sai lệch gấp nhiều lần thực tế. Dùng `COUNT(DISTINCT v.id)` bảo đảm chỉ đếm các định danh duy nhất, cho kết quả chính xác 100% ạ."*

### Q4: "Khi người dùng ấn 'Lưu nháp' một bài viết đã từng xuất bản trước đó, hệ thống xử lý như thế nào để độc giả bên ngoài không đọc phải nội dung dở dang?"

- **Trả lời chuẩn**:
  *"Dạ thưa Thầy, trong hàm `updateBlog()` của `BlogService`, nhóm em thiết kế 2 cột tách biệt là `content` (nội dung public) và `draftContent` (nội dung đang sửa dở). Khi tác giả bấm 'Save Draft', hệ thống kiểm tra nếu bài viết này đã từng xuất bản (`draft == false`), code sẽ giữ nguyên cột `content` để độc giả xem bài viết bình thường, và chỉ ghi nội dung đang chỉnh sửa vào cột `draftContent`. Khi nào tác giả bấm 'Publish', hệ thống mới đổ dữ liệu từ `draftContent` sang `content` và xóa rỗng cột nháp ạ."*

### Q5: "Tại sao trong `SecurityConfig` nhóm em lại cấu hình `.csrf(AbstractHttpConfigurer::disable)`? Tắt CSRF như vậy có bị nguy hiểm không?"

- **Trả lời chuẩn**:
  *"Dạ thưa Thầy, tắt CSRF hoàn toàn an toàn và là chuẩn mực bắt buộc cho kiến trúc **Stateless RESTful API dùng JWT**. Tấn công CSRF chỉ xảy ra khi trình duyệt tự động gửi kèm Cookie phiên đăng nhập (`JSESSIONID`) trong các request ẩn danh. Trong hệ thống của nhóm em, ứng dụng lưu Token JWT trong `localStorage` và gửi qua Header `Authorization: Bearer <token>`. Vì trình duyệt không bao giờ tự động đính kèm Header này, website độc hại của hacker không thể kích hoạt request giả mạo, do đó hệ thống miễn nhiễm với CSRF và việc tắt CSRF là hoàn toàn đúng kỹ thuật ạ."*

### Q6: "Làm sao hệ thống của nhóm ngăn chặn được việc một User tự bấm Like bài viết nhiều lần để gian lận số lượt Like?"

- **Trả lời chuẩn**:*"Dạ thưa Thầy, nhóm em bảo vệ ở 2 tầng:*
  1. *Ở tầng CSDL: Bảng `blog_likes` được gắn ràng buộc duy nhất phức hợp `@Table(uniqueConstraints = {@UniqueConstraint(columnNames = {"user_id", "blog_id"})})`. Nếu có câu lệnh INSERT trùng lặp, MySQL sẽ lập tức chặn lại và báo lỗi Duplicate Entry.*
  2. *Ở tầng Logic Service: Hàm `toggleLike()` trước khi lưu sẽ truy vấn `findByBlogIdAndUserUsername()`. Nếu thấy đã tồn tại thì tiến hành xóa (Unlike), nếu chưa có mới tạo mới (Like) ạ."*

### Q7: "Trong `SecurityConfig.java`, tại sao danh sách `PUBLIC_GET_ENDPOINTS` lại chứa cả `/admin/**`? Ai cũng vào được trang Admin hay sao?"

- **Trả lời chuẩn**:
  *"Dạ thưa Thầy, đây là đặc thù của mô hình Client-Side SPA kết hợp Spring Security. Đường dẫn `/admin/**` trong `PUBLIC_GET_ENDPOINTS` chỉ là đường dẫn tải file HTML tĩnh từ `ViewController` (vì khi người dùng bấm vào link trên thanh địa chỉ trình duyệt, request GET ban đầu không thể đính kèm Header Authorization JWT). Tuy nhiên, trang HTML này chỉ là một khung vỏ rỗng. Khi mở trang lên, mã JavaScript trên trang Admin sẽ lấy Token JWT trong `localStorage` và gửi request lấy số liệu thống kê lên API Backend `/api/admin/stats`. API này nằm trong mảng `ADMIN_ENDPOINTS` và được bảo vệ nghiêm ngặt bằng `.hasRole('ADMIN')`. Nếu người dùng không có quyền Admin, API sẽ trả về mã `HTTP 403 Forbidden` và JavaScript sẽ đẩy người dùng về trang chủ ngay lập tức ạ."*

### Q8: "Annotation `@Transactional` trong `InteractionService.java` hoạt động theo cơ chế nào nếu câu lệnh thêm bình luận thành công nhưng câu lệnh gửi thông báo bị lỗi?"

- **Trả lời chuẩn**:
  *"Dạ thưa Thầy, nhờ có `@Transactional`, Spring AOP sẽ bọc phương thức `addComment()` bằng một Proxy giao dịch. Mọi câu lệnh SQL thêm bình luận và tạo thông báo đều nằm trong cùng một Database Transaction với cờ `AutoCommit = false`. Nếu câu lệnh gửi thông báo ném ra một ngoại lệ `RuntimeException`, Proxy sẽ bắt được và tự động gọi `Connection.rollback()`. Toàn bộ bình luận vừa thêm trước đó sẽ bị hủy bỏ, khôi phục trạng thái CSDL về nguyên vẹn trước khi gọi hàm, bảo đảm tính chất **Atomicity (Nguyên tử)** của ACID ạ."*

### Q9: "Kiểu dữ liệu UUID có ưu và nhược điểm gì so với kiểu số nguyên tự tăng `BIGINT AUTO_INCREMENT`?"

- **Trả lời chuẩn**:*"Dạ thưa Thầy:
  - **Ưu điểm lớn nhất**: Tính bảo mật. Số tự tăng rất dễ bị lộ quy mô hệ thống và bị tấn công cào dữ liệu qua URL (`/blogs/1`, `/blogs/2`). UUID là chuỗi ngẫu nhiên 128-bit không thể đoán trước được. Ngoài ra, UUID cho phép Client tự sinh ID trong các hệ thống phân tán mà không lo bị xung đột khóa.
  - **Nhược điểm**: Tốn dung lượng lưu trữ hơn (36 ký tự `VARCHAR` hoặc 16 bytes `BINARY`) và tốc độ đánh chỉ mục Index B-Tree trong MySQL chậm hơn số nguyên một chút do tính ngẫu nhiên không có thứ tự tăng dần liên tục ạ."*

### Q10: "Làm sao Backend lấy được danh tính của tác giả khi tạo bài viết mới trong khi Request Body gửi lên không hề có trường `authorId`?"

- **Trả lời chuẩn**:
  *"Dạ thưa Thầy, nhóm em tuyệt đối không nhận `authorId` từ Client gửi lên để chống hành vi giả mạo danh tính tác giả. Thay vào đó, trong hàm `createBlog()`, nhóm em lấy trực tiếp username từ ngữ cảnh bảo mật của Spring Security:
  `String currentUsername = SecurityContextHolder.getContext().getAuthentication().getName();`
  Thông tin này được bộ lọc `JwtAuthenticationFilter` giải mã và xác thực trực tiếp từ chuỗi Token JWT có chữ ký điện tử hợp lệ, bảo đảm an toàn 100% ạ."*

---

# PHẦN VII: CẨM NĂNG CỨU MẠNG VẤN ĐÁP CẤP TỐC (SPEED-READ FOR DEFENSE TOMORROW)

*(Dành riêng cho bạn đọc lướt trong 5 phút trước khi bước vào phòng gặp Thầy Phúc!)*

### ⚡ 10 Câu Nói "Ăn Điểm Ngay Lập Tức" Trong 30 Giây:

1. **Thầy hỏi: "Kiến trúc nhóm em là gì?"**$\rightarrow$ *"Dạ kiến trúc phân tầng 3-tier chuẩn doanh nghiệp: Controller điều phối tiếp nhận RESTful API $\rightarrow$ Service xử lý logic nghiệp vụ và Transaction $\rightarrow$ Repository dùng Spring Data JPA giao tiếp với CSDL MySQL Local qua Hibernate ORM ạ."*
2. **Thầy hỏi: "Chức năng đăng bài viết chạy qua những đâu?"**$\rightarrow$ *"Dạ bắt đầu từ form giao diện `blog-editor.js`, JS lấy Token JWT gửi `POST /blogs` $\rightarrow$ `BlogController` nhận DTO $\rightarrow$ `BlogService` lấy username từ SecurityContext, map sang Entity, tự động lưu tags mới $\rightarrow$ `BlogRepository` sinh lệnh INSERT xuống MySQL và trả về `BlogResponse` ạ."*
3. **Thầy hỏi: "Chỉ cho thầy chỗ dùng Dependency Injection?"**$\rightarrow$ Mở `BlogService.java`, chỉ vào dòng `@RequiredArgsConstructor` và nói: *"Dạ đây là Constructor Injection ngầm định (Implicit DI). Lombok tạo constructor cho các biến final, Spring 4.3+ tự động inject bean mà không cần `@Autowired` ạ."*
4. **Thầy hỏi: "Tại sao Repository không viết code mà vẫn lưu được dữ liệu?"**$\rightarrow$ *"Dạ nhờ cơ chế Dynamic Proxy của Java và Spring Data JPA. Tại thời điểm chạy, Spring tự sinh ra class proxy ẩn `SimpleJpaRepository` trong RAM để dịch các phương thức thành SQL tương ứng nạp xuống Hibernate EntityManager ạ."*
5. **Thầy hỏi: "CSDL có bao nhiêu bảng? Bảng trung gian ở đâu?"**$\rightarrow$ *"Dạ có 12 bảng chuẩn 3NF. Bảng trung gian là `blog_tags` (giải quyết quan hệ N-N giữa bài viết và tag) và `user_roles` (giải quyết quan hệ N-N giữa user và vai trò phân quyền) ạ."*
6. **Thầy hỏi: "Làm sao hệ thống phân biệt được ai là Admin ai là User?"**$\rightarrow$ *"Dạ trong Token JWT có claim `scope` lưu quyền hạn. Khi giải mã, `SecurityConfig` thêm tiền tố `ROLE_` và dùng `.hasRole('ADMIN')` để chặn các API quản trị `/api/admin/**`. User thường gọi vào sẽ bị trả lỗi 403 Forbidden ạ."*
7. **Thầy hỏi: "Tại sao nhóm dùng UUID làm khóa chính?"**$\rightarrow$ *"Dạ để bảo mật chống tấn công dò quét ID (ID Enumeration) và hỗ trợ tốt cho hệ thống phân tán không lo trùng ID ạ."*
8. **Thầy hỏi: "Tại sao không dùng trực tiếp Entity ở Controller mà phải qua DTO?"**$\rightarrow$ *"Dạ để chống tấn công Over-posting hacker tự gán quyền Admin, chống lỗi đệ quy vô hạn JSON khi serialize quan hệ 2 chiều và che giấu trường mật khẩu nhạy cảm ạ."*
9. **Thầy hỏi: "Annotation `@Transactional` để làm gì?"**$\rightarrow$ *"Dạ để đảm bảo tính chất ACID. Nếu trong một hàm có 3 câu lệnh ghi dữ liệu mà câu thứ 3 bị lỗi, hệ thống sẽ tự động Rollback hủy 2 câu trước, không sinh ra dữ liệu rác trong database ạ."*
10. **Thầy hỏi: "Mật khẩu lưu trong DB thế nào? Hacker lấy được file DB có đọc được không?"**
    $\rightarrow$ *"Dạ mật khẩu được băm một chiều bằng thuật toán `BCrypt` với độ khó 10 vòng muối (salt). Đây là hàm băm một chiều không thể giải mã ngược, hacker có lấy được DB cũng không thể dịch ra mật khẩu gốc ạ."*

---

### 🎯 CHECKLIST 5 PHÚT TRƯỚC GIỜ VẤN ĐÁP:

1. **Khởi động dịch vụ sẵn**: Bật MySQL Server (`localhost:3306`), chạy ứng dụng Spring Boot Backend trên cổng `8080`, test thử truy cập `localhost:8080` trên trình duyệt.
2. **Chuẩn bị 2 phiên duyệt web**:
   - Cửa sổ 1: Đăng nhập tài khoản `admin` (mật khẩu `123456`) $\rightarrow$ Sẵn sàng mở Dashboard Thống kê và Quản lý người dùng.
   - Cửa sổ 2 (Ẩn danh): Đăng nhập tài khoản thành viên `duonghd` / `dungnt` / `longlt` $\rightarrow$ Sẵn sàng demo viết bài, upload ảnh banner, like và bình luận bài viết.
3. **Quyển báo cáo in giấy**: Đủ 15-20 trang, đóng bìa chỉn chu, kiểm tra không có trang nào in code.
4. **Tâm thế trả lời**: Tự tin, nói to, dứt khoát, đi thẳng vào keyword kỹ thuật. Thầy hỏi đến đâu chỉ đúng file code và dòng code đến đó theo Bảng tra cứu ở Phần II.

---

*Bản tài liệu này là tài sản học thuật đầy đủ và toàn diện nhất, chuẩn bị cho nhóm bạn đạt điểm 10 tuyệt đối trong đợt Báo cáo BTL và kỳ thi Tự luận cuối kỳ môn Công nghệ Web!*
