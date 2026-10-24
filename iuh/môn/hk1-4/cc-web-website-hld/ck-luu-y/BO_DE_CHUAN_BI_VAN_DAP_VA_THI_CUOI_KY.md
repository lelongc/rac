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
  - [Mục 0: Giải Phẫu Toàn Diện Từng Dòng File Quản Lý Dự Án (pom.xml)](#mục-0-giải-phẫu-toàn-diện-từng-dòng-file-quản-lý-dự-án-pomxml)
  - [Mục 1: Lớp Khởi Chạy Ứng Dụng (BlogWebsiteApplication.java)](#mục-1-lớp-khởi-chạy-ứng-dụng-blogwebsiteapplicationjava)
  - [Mục 2: Tầng Cấu Hình (Configuration Package)](#mục-2-tầng-cấu-hình-configuration-package)
  - [📌 CHUYÊN ĐỀ ĐẶC BIỆT: TẦNG THỰC THỂ (ENTITY), TẦNG TRUY XUẤT (REPOSITORY) &amp; DTO](#-chuyên-đề-đặc-biệt-tầng-thực-thể-entity-tầng-truy-xuất-repository--dto)
  - [Mục 3: Tầng Nghiệp Vụ (Service Package - Toàn Bộ 10 Services)](#mục-3-tầng-nghiệp-vụ-service-package---toàn-bộ-10-services)
  - [Mục 4: Tầng Điều Khiển (Controller Package - Toàn Bộ 8 Controllers)](#mục-4-tầng-điều-khiển-controller-package---toàn-bộ-8-controllers)
  - [Mục 5: Tầng Xử Lý Ngoại Lệ, Chuyển Đổi DTO &amp; Tiện Ích (Exception, Mapper &amp; Util)](#mục-5-tầng-xử-lý-ngoại-lệ-chuyển-đổi-dto--tiện-ích-exception-mapper--util)
  - [Mục 6: Tầng Giao Diện &amp; Frontend JavaScript Giao Tiếp API](#mục-6-tầng-giao-diện--frontend-javascript-giao-tiếp-api)
    - [6.1. Kiến Trúc Frontend: Phân Biệt MPA vs SPA &amp; Bản Chất Dự Án](#61-kiến-trúc-frontend-phân-biệt-mpa-vs-spa--bản-chất-dự-án)
    - [6.2. Bóc Tách Chi Tiết Toàn Bộ 21 File Giao Diện HTML (templates/)](#62-bóc-tách-chi-tiết-toàn-bộ-21-file-giao-diện-html-templates)
    - [6.3. Bóc Tách Chi Tiết Toàn Bộ 8 File JavaScript Cốt Lõi (static/assets/js/)](#63-bóc-tách-chi-tiết-toàn-bộ-8-file-javascript-cốt-lõi-staticassetsjs)
    - [6.4. Các Thư Viện Frontend Bổ Trợ &amp; Kỹ Thuật CSS Nâng Cao](#64-các-thư-viện-frontend-bổ-trợ--kỹ-thuật-css-nâng-cao)
    - [6.5. Bộ 5 Câu Hỏi Vấn Đáp Chuyên Sâu Về Frontend &amp; Kịch Bản Ghi Điểm 10](#65-bộ-5-câu-hỏi-vấn-đáp-chuyên-sâu-về-frontend--kịch-bản-ghi-điểm-10)
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

## Mục 0: Giải Phẫu Toàn Diện Từng Dòng File Quản Lý Dự Án (`pom.xml`)

- **Vị trí file**: `d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\btl\blog-website-main\pom.xml`
- **Mục đích**: `pom.xml` (Project Object Model) là tệp cấu hình cốt lõi của công cụ tự động hóa bản dựng **Apache Maven**. Nó quản lý toàn bộ vòng đời ứng dụng: phiên bản máy ảo Java, thư viện phụ thuộc (Dependencies), cấu hình trình biên dịch (Compiler Plugins) và quy trình đóng gói file thực thi (Executable Fat JAR).

---

### 0.1. Khối Cấu Trúc Khai Báo XML & Thông Tin Gốc (Lines 1 - 28)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>3.5.11</version>
		<relativePath/> 
	</parent>
	<groupId>com.group</groupId>
	<artifactId>blog-website</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<name>blog-website</name>
	<description>Group blog website project using Spring Boot</description>
```

- **Phân tích từng dòng & Lý thuyết**:
  - Dòng 1: `<?xml version="1.0" encoding="UTF-8"?>`: Khai báo chuẩn cú pháp XML và bộ mã hóa ký tự UTF-8 (hỗ trợ hiển thị tiếng Việt có dấu).
  - Dòng 2-3: `xmlns` & `xsi:schemaLocation`: Định nghĩa không gian tên (XML Namespace) và sơ đồ Schema POM 4.0.0, giúp IDE (Eclipse/IntelliJ/VS Code) tự động kiểm tra tính hợp lệ và tự động gợi ý thẻ XML.
  - Dòng 4: `<modelVersion>4.0.0</modelVersion>`: Chỉ định phiên bản cấu trúc mô hình đối tượng dự án của Maven (bắt buộc luôn là 4.0.0).
  - Dòng 5-10: Khối `<parent>` (Parent POM / BOM - Bill of Materials):
    - Kế thừa từ `spring-boot-starter-parent` phiên bản `3.5.11`.
    - **Vai trò tối quan trọng**: Parent POM quản lý tập trung phiên bản (Dependency Management) cho hơn 200 thư viện phổ biến trong hệ sinh thái Spring (Spring MVC, Hibernate, Tomcat, Jackson, Thymeleaf...). Nhờ có thẻ `<parent>` này mà hầu hết các thẻ `<dependency>` bên dưới của dự án **không cần phải khai báo thẻ `<version>`**, loại bỏ 100% nguy cơ xung đột phiên bản (Jar Hell / Dependency Hell).
    - Đồng thời cấu hình sẵn: Bộ mã hóa UTF-8 mặc định, cấu hình biên dịch Java, cấu hình plugin đóng gói và quản lý tài nguyên (Resource filtering).
    - `<relativePath/>`: Báo cho Maven không tìm file parent ở thư mục cha cục bộ trên máy tính, mà tải trực tiếp từ kho lưu trữ trung tâm Maven Central Repository (lưu đệm tại `~/.m2/repository`).
  - Dòng 11-15: Tọa độ nhận diện dự án theo chuẩn **GAV (GroupId - ArtifactId - Version)**:
    - `<groupId>com.group</groupId>`: Định danh tên miền ngược của tổ chức/nhóm phát triển.
    - `<artifactId>blog-website</artifactId>`: Tên định danh duy nhất của gói sản phẩm phần mềm (project).
    - `<version>0.0.1-SNAPSHOT</version>`: Phiên bản hiện tại của dự án. Hậu tố **`SNAPSHOT`** biểu thị đây là bản đang trong quá trình phát triển (chưa phải bản phát hành chính thức RELEASE), Maven sẽ tự động kiểm tra và tải các bản cập nhật mới nhất mỗi khi build.
    - `<name>` & `<description>`: Tên hiển thị và mô tả tóm tắt mục tiêu của dự án.

---

### 0.2. Khối Cấu Hình Thuộc Tính Biến Môi Trường `<properties>` (Lines 29 - 36)

```xml
	<properties>
		<java.version>21</java.version>
		<maven.compiler.source>21</maven.compiler.source>
		<maven.compiler.target>21</maven.compiler.target>
		<mapstruct.version>1.5.5.Final</mapstruct.version>
		<m2e.apt.activation>jdt_apt</m2e.apt.activation>
		<maven-jar-plugin.version>3.4.2</maven-jar-plugin.version>
	</properties>
```

- **Phân tích từng dòng & Lý thuyết**:
  - Dòng 30: `<java.version>21</java.version>`: Khai báo phiên bản máy ảo Java mục tiêu của dự án là **Java 21 (Phiên bản hỗ trợ dài hạn LTS mới nhất)**, hỗ trợ các tính năng hiện đại như Record Patterns, Pattern Matching for switch, Virtual Threads.
  - Dòng 31-32: `<maven.compiler.source>21</maven.compiler.source>` & `<maven.compiler.target>21</maven.compiler.target>`: Chỉ định cho trình biên dịch `javac` đọc mã nguồn Java 21 và sinh ra bytecode tương thích với Java Virtual Machine (JVM) 21.
  - Dòng 33: `<mapstruct.version>1.5.5.Final</mapstruct.version>`: Khai báo biến phiên bản thư viện MapStruct dùng chung cho cả phần nạp dependency lẫn plugin biên dịch, tránh việc phải gõ lại số phiên bản ở nhiều nơi.
  - Dòng 34: `<m2e.apt.activation>jdt_apt</m2e.apt.activation>`: Kích hoạt bộ xử lý Annotation Processor tự động (APT - Annotation Processing Tool) cho môi trường Eclipse IDE thông qua plugin M2E (Maven to Eclipse), giúp Eclipse tự động sinh mã Mapper lúc save code mà không cần chạy lệnh maven thủ công.
  - Dòng 35: `<maven-jar-plugin.version>3.4.2</maven-jar-plugin.version>`: Ghim phiên bản plugin đóng gói file JAR.

---

### 0.3. Khối Quản Lý Toàn Bộ 16 Thư Viện Phụ Thuộc `<dependencies>` (Lines 37 - 129)

Mỗi thẻ `<dependency>` đại diện cho một module chức năng được tích hợp vào ứng dụng:

```xml
	<dependencies>
		<!-- 1. Lưu trữ đám mây Cloudinary SDK -->
		<dependency>
			<groupId>com.cloudinary</groupId>
			<artifactId>cloudinary-http44</artifactId>
			<version>1.36.0</version>
		</dependency>

		<!-- 2. Máy chủ tài nguyên xác thực OAuth2 & JWT -->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-oauth2-resource-server</artifactId>
		</dependency>

		<!-- 3. Tương tác CSDL Hibernate ORM & Spring Data JPA -->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-data-jpa</artifactId>
		</dependency>

		<!-- 4. Khung bảo mật phân quyền Spring Security 6 -->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-security</artifactId>
		</dependency>

		<!-- 5. Cỗ máy hiển thị giao diện HTML Thymeleaf -->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-thymeleaf</artifactId>
		</dependency>

		<!-- 6. Xây dựng ứng dụng Web MVC & Nhúng máy chủ Tomcat -->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>

		<!-- 7. Xác thực dữ liệu đầu vào Jakarta Bean Validation -->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-validation</artifactId>
		</dependency>

		<!-- 8. Tích hợp Thymeleaf với Spring Security -->
		<dependency>
			<groupId>org.thymeleaf.extras</groupId>
			<artifactId>thymeleaf-extras-springsecurity6</artifactId>
		</dependency>

		<!-- 9. Mã hóa mật khẩu an toàn BCrypt -->
		<dependency>
			<groupId>org.springframework.security</groupId>
			<artifactId>spring-security-crypto</artifactId>
		</dependency>

		<!-- 10. Xử lý tạo và giải mã chữ ký số JSON Web Token -->
		<dependency>
			<groupId>com.nimbusds</groupId>
			<artifactId>nimbus-jose-jwt</artifactId>
			<version>9.30.1</version>
		</dependency>

		<!-- 11. Công cụ hỗ trợ phát triển Hot-Reload / Tự restart server -->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-devtools</artifactId>
			<scope>runtime</scope>
			<optional>true</optional>
		</dependency>

		<!-- 12. Driver kết nối Cơ sở dữ liệu MySQL -->
		<dependency>
			<groupId>com.mysql</groupId>
			<artifactId>mysql-connector-j</artifactId>
			<scope>runtime</scope>
		</dependency>

		<!-- 13. Tự động sinh mã thừa Lombok (Getter, Setter, Builder) -->
		<dependency>
			<groupId>org.projectlombok</groupId>
			<artifactId>lombok</artifactId>
			<optional>true</optional>
		</dependency>

		<!-- 14. Bộ chuyển đổi DTO sang Entity MapStruct -->
		<dependency>
			<groupId>org.mapstruct</groupId>
			<artifactId>mapstruct</artifactId>
			<version>${mapstruct.version}</version>
		</dependency>

		<dependency>
			<groupId>org.mapstruct</groupId>
			<artifactId>mapstruct-processor</artifactId>
			<version>${mapstruct.version}</version>
			<scope>provided</scope>
		</dependency>

		<!-- 15. Cầu nối đồng bộ thứ tự biên dịch giữa Lombok và MapStruct -->
		<dependency>
			<groupId>org.projectlombok</groupId>
			<artifactId>lombok-mapstruct-binding</artifactId>
			<version>0.2.0</version>
		</dependency>

		<!-- 16. Bộ công cụ kiểm thử tự động JUnit 5 & Mockito -->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>org.springframework.security</groupId>
			<artifactId>spring-security-test</artifactId>
			<scope>test</scope>
		</dependency>
	</dependencies>
```

- **Phân tích chuyên sâu từng thư viện & Câu hỏi vấn đáp liên quan**:
  1. `cloudinary-http44`: Bộ SDK Java chính thức của Cloudinary sử dụng thư viện HTTP client `httpclient 4.4` của Apache, gửi dữ liệu nhị phân file ảnh lên Cloudinary qua HTTPS và nhận về đường dẫn ảnh CDN tốc độ cao.
  2. `spring-boot-starter-oauth2-resource-server`: Đóng vai trò cấu hình hệ thống thành một **OAuth2 Resource Server**. Cung cấp bộ lọc tự động trích xuất token từ Header `Authorization: Bearer <token>`, giải mã chữ ký qua `NimbusJwtDecoder` và gán thông tin người dùng vào `SecurityContext`.
  3. `spring-boot-starter-data-jpa`: Gói thư viện toàn diện gồm:
     - **Hibernate ORM**: Cỗ máy ánh xạ quan hệ đối tượng giữa Java Class và bảng MySQL.
     - **Spring Data JPA**: Cung cấp các interface `JpaRepository` với các phương thức CRUD tự động.
     - **HikariCP**: Bộ quản lý kết nối CSDL (JDBC Connection Pool) nhanh nhất thế giới hiện nay, tự động tối ưu việc tái sử dụng connection mà không phải mở mới liên tục.
  4. `spring-boot-starter-security`: Cung cấp kiến trúc bảo mật lọc yêu cầu (Filter Chain), mã hóa, bảo vệ phiên, và xác thực phân quyền dựa trên quyền hạn (Roles/Authorities).
  5. `spring-boot-starter-thymeleaf`: Tích hợp bộ giải quyết giao diện `ThymeleafViewResolver` giúp render file HTML trên server rồi trả về cho trình duyệt.
  6. `spring-boot-starter-web`: Tích hợp máy chủ **Embedded Apache Tomcat** (chạy ngầm bên trong file JAR, không cần cài đặt Tomcat bên ngoài), cung cấp `DispatcherServlet` và thư viện Jackson (chuyển đổi Java Object $\leftrightarrow$ JSON).
  7. `spring-boot-starter-validation`: Triển khai chuẩn Jakarta Bean Validation (JSR-380) qua Hibernate Validator. Cung cấp các Annotation như `@NotBlank`, `@Size`, `@Min`, `@Max`, `@Email` kết hợp với `@Valid` tại Controller để ngăn chặn dữ liệu rác trước khi đưa vào Service.
  8. `thymeleaf-extras-springsecurity6`: Mở rộng cú pháp Thymeleaf với namespace `sec:authorize="isAuthenticated()"` hoặc `sec:authorize="hasRole('ADMIN')"` để ẩn/hiện menu trên giao diện web theo quyền hạn đăng nhập.
  9. `spring-security-crypto`: Cung cấp class `BCryptPasswordEncoder` sử dụng thuật toán băm mật khẩu một chiều kết hợp muối ngẫu nhiên (salt 10 rounds).
  10. `nimbus-jose-jwt`: Thư viện chuyên dụng tạo, ký điện tử theo thuật toán `HMAC-SHA512` và thẩm định tính hợp lệ của chuỗi JSON Web Token theo chuẩn RFC 7519.
  11. `spring-boot-devtools`: Hỗ trợ lập trình viên: Tự động khởi động lại ứng dụng (LiveReload / Hot Restart) khi phát hiện thay đổi trong mã nguồn. Thẻ `<scope>runtime</scope>` và `<optional>true</optional>` bảo đảm thư viện này **không bao giờ bị đóng gói lên môi trường Production**, tránh gây hao phí tài nguyên máy chủ thật.
  12. `mysql-connector-j`: Thư viện JDBC Driver chính thức của MySQL cho phép Spring Data kết nối và thực thi các lệnh SQL xuống CSDL MySQL (chạy tại cổng 3306). Có `<scope>runtime</scope>` vì mã nguồn Java chỉ cần giao tiếp qua giao diện chuẩn `java.sql.*`, chỉ khi chạy ứng dụng thật mới cần đến file `.jar` cụ thể của MySQL.
  13. `lombok`: Tiền xử lý mã nguồn (Annotation Processor) tự động sinh mã Getter, Setter, Builder, Constructor trong bộ nhớ lúc biên dịch, giúp mã nguồn Java ngắn gọn, sạch sẽ.
  14. `mapstruct` & `mapstruct-processor`: Bộ chuyển đổi DTO $\leftrightarrow$ Entity cực nhanh, sinh mã Java thuần lúc compile time. Cấu hình `<scope>provided</scope>` cho processor vì nó chỉ chạy lúc biên dịch rồi tự hủy, không cần đưa vào file JAR thành phẩm.
  15. `lombok-mapstruct-binding` (0.2.0): **Thư viện cầu nối sinh tử**: Nếu dùng đồng thời cả Lombok và MapStruct mà thiếu thư viện này, MapStruct sẽ chạy trước khi Lombok kịp sinh mã `getter/setter`, dẫn tới lỗi biên dịch *"Cannot find symbol getXxx()"*. `lombok-mapstruct-binding` ép Maven Compiler kích hoạt Lombok sinh getter/setter trước, rồi mới đưa sang cho MapStruct nạp dữ liệu.
  16. `spring-boot-starter-test` & `spring-security-test`: Bộ công cụ kiểm thử tự động gồm: **JUnit 5 (Jupiter)** (viết ca kiểm thử), **Mockito** (giả lập hành vi của Service/Repository), **AssertJ** (khẳng định kết quả kiểm thử), **MockMvc** (giả lập gửi request HTTP đến Controller mà không cần bật máy chủ web). Cấu hình `<scope>test</scope>` để chỉ dùng khi chạy lệnh `mvn test`.

---

### 0.4. Khối Cấu Hình Bản Dựng `<build>` & Các Plugin Biên Dịch (Lines 131 - 171)

```xml
	<build>
		<plugins>
			<!-- Plugin 1: Trình biên dịch mã nguồn Apache Maven Compiler Plugin -->
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-compiler-plugin</artifactId>
				<configuration>
					<source>21</source>
					<target>21</target>
					<annotationProcessorPaths>
						<!-- Bước 1: Lombok chạy trước để sinh Getter, Setter, Builder -->
						<path>
							<groupId>org.projectlombok</groupId>
							<artifactId>lombok</artifactId>
						</path>
						<!-- Bước 2: MapStruct chạy sau để đọc Getter, Setter sinh mã Mapper -->
						<path>
							<groupId>org.mapstruct</groupId>
							<artifactId>mapstruct-processor</artifactId>
							<version>${mapstruct.version}</version>
						</path>
						<!-- Bước 3: Cầu nối điều phối giữa Lombok và MapStruct -->
						<path>
							<groupId>org.projectlombok</groupId>
							<artifactId>lombok-mapstruct-binding</artifactId>
							<version>0.2.0</version>
						</path>
					</annotationProcessorPaths>
				</configuration>
			</plugin>

			<!-- Plugin 2: Plugin đóng gói Fat JAR thực thi của Spring Boot -->
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
				<configuration>
					<excludes>
						<!-- Loại bỏ Lombok ra khỏi file JAR đóng gói để file nhẹ hơn -->
						<exclude>
							<groupId>org.projectlombok</groupId>
							<artifactId>lombok</artifactId>
						</exclude>
					</excludes>
				</configuration>
			</plugin>
		</plugins>
	</build>
```

- **Phân tích từng Plugin & Lý thuyết**:
  1. `maven-compiler-plugin`:
     - Thiết lập `<source>21</source>` và `<target>21</target>` đảm bảo việc biên dịch Java 21 diễn ra chuẩn xác.
     - Khối `<annotationProcessorPaths>` thiết lập thứ tự ưu tiên của các bộ tiền xử lý chú thích: Bắt buộc Lombok phải chạy trước để sinh đầy đủ getter/setter, sau đó MapStruct mới quét được các getter/setter này để sinh mã class Mapper hoàn chỉnh.
  2. `spring-boot-maven-plugin`:
     - Plugin độc quyền của Spring Boot có nhiệm vụ tạo ra gói **Fat JAR (còn gọi là Executable JAR / Uber JAR)**.
     - Khác với file JAR truyền thống chỉ chứa file `.class` của lập trình viên, Fat JAR của Spring Boot chứa toàn bộ mã nguồn dự án, toàn bộ 16 file `.jar` phụ thuộc, và **nhúng trọn vẹn cả máy chủ web Apache Tomcat bên trong**. Nhờ vậy, người dùng chỉ cần một lệnh duy nhất: `java -jar blog-website-0.0.1-SNAPSHOT.jar` là website tự động chạy trên bất kỳ máy chủ nào mà không cần cài Tomcat, cấu hình biến môi trường phức tạp!
     - Thẻ `<excludes>`: Loại bỏ thư viện `lombok` ra khỏi file JAR thành phẩm vì Lombok chỉ cần thiết lúc viết code và biên dịch, không cần thiết lúc chạy thực tế.

---

### 0.5. Bộ Câu Hỏi Vấn Đáp Lý Thuyết Thầy Phúc Hay Hỏi Nhất Về Maven & `pom.xml`

#### Q1: "Maven là gì? Vòng đời của Maven (Maven Build Lifecycle) gồm những giai đoạn (phases) nào?"
- **Trả lời**: *"Dạ thưa Thầy, Maven là công cụ tự động hóa việc quản lý phụ thuộc (Dependency Management) và xây dựng phần mềm (Build Automation) cho Java. Vòng đời mặc định của Maven gồm 8 giai đoạn chính theo thứ tự:
  1. `validate`: Kiểm tra tính hợp lệ của cấu trúc thư mục dự án và file `pom.xml`.
  2. `compile`: Dùng `javac` biên dịch toàn bộ mã nguồn Java trong `src/main/java` thành file bytecode `.class` lưu trong thư mục `target/classes`.
  3. `test-compile`: Biên dịch mã nguồn kiểm thử trong `src/test/java`.
  4. `test`: Thực thi toàn bộ các ca kiểm thử tự động (Unit Test / Integration Test) bằng JUnit/Mockito.
  5. `package`: Đóng gói mã nguồn đã biên dịch thành file nén `.jar` hoặc `.war`.
  6. `verify`: Chạy các kiểm tra chất lượng mã nguồn xem file đóng gói có đạt tiêu chuẩn không.
  7. `install`: Cài đặt file `.jar` vừa đóng gói vào kho lưu trữ cục bộ của máy tính cá nhân (`~/.m2/repository`).
  8. `deploy`: Đẩy file `.jar` lên kho máy chủ trung tâm (Remote Repository / Nexus / Artifactory) để các dự án khác sử dụng ạ!"*

#### Q2: "Thẻ `<scope>` trong Maven có ý nghĩa gì? Kể tên các Scope phổ biến mà dự án của nhóm em đang sử dụng?"
- **Trả lời**: *"Dạ thưa Thầy, thẻ `<scope>` kiểm soát phạm vi và thời điểm một thư viện `.jar` có mặt trong Classpath của ứng dụng. Dự án của nhóm em sử dụng 4 scope phổ biến:
  1. `compile` (Mặc định khi không khai báo): Có mặt trong mọi giai đoạn (biên dịch, kiểm thử, đóng gói và chạy thực tế). Ví dụ: `spring-boot-starter-web`, `spring-boot-starter-security`.
  2. `provided`: Thư viện chỉ cần lúc biên dịch mã nguồn, khi chạy thực tế môi trường (hoặc máy ảo) sẽ cung cấp sẵn, không bị đóng gói vào file JAR. Ví dụ: `mapstruct-processor`.
  3. `runtime`: Không cần thiết lúc biên dịch mã nguồn nhưng bắt buộc phải có lúc chạy ứng dụng thực tế. Ví dụ: `mysql-connector-j` (mã Java chỉ giao tiếp qua interface chuẩn JDBC của Oracle, lúc chạy mới cần file jar kết nối MySQL) và `spring-boot-devtools`.
  4. `test`: Chỉ có mặt trong giai đoạn biên dịch và chạy các ca kiểm thử tự động, tuyệt đối không bị đóng gói vào bản sản phẩm cuối cùng. Ví dụ: `spring-boot-starter-test` và `spring-security-test` ạ!"*

#### Q3: "Tại sao hầu hết các dependency của Spring Boot trong `pom.xml` không cần ghi thẻ `<version>` mà Maven vẫn tải đúng phiên bản?"
- **Trả lời**: *"Dạ thưa Thầy, đó là nhờ cơ chế kế thừa **Parent POM (BOM - Bill of Materials)** từ thẻ `<parent>`: `spring-boot-starter-parent` phiên bản `3.5.11`. Trong Parent POM đã định nghĩa sẵn khối `<dependencyManagement>` chứa danh mục phiên bản đã được đội ngũ kỹ sư Spring kiểm thử kỹ lưỡng về tính tương thích. Khi ta khai báo `spring-boot-starter-data-jpa` hay `spring-boot-starter-web` mà không ghi `<version>`, Maven sẽ tự động kế thừa số phiên bản chuẩn xác từ Parent POM, giúp hệ thống không bao giờ bị xung đột thư viện ạ!"*

#### Q4: "Fat JAR (Executable JAR) là gì? Khác gì với file JAR truyền thống của Java cũ?"
- **Trả lời**: *"Dạ thưa Thầy:
  - File JAR truyền thống (Thin JAR) chỉ chứa các file `.class` do lập trình viên viết ra. Muốn chạy được, lập trình viên phải tự cài đặt máy chủ bên ngoài (như Tomcat riêng), copy các file jar phụ thuộc vào thư mục `lib`, cấu hình rất phức tạp.
  - Còn **Fat JAR** (do plugin `spring-boot-maven-plugin` tạo ra) là một gói nén hoàn chỉnh chứa tất cả mọi thứ: Mã nguồn ứng dụng + Toàn bộ 16 thư viện `.jar` phụ thuộc giải nén trong `BOOT-INF/lib` + **Nhúng sẵn máy chủ Apache Tomcat bên trong**. Chỉ cần chạy lệnh `java -jar app.jar` là web server tự bung ra và chạy ngay lập tức, cực kỳ tiện lợi cho việc triển khai Docker và Microservices ạ!"*

#### Q5: "Nếu dự án gặp xung đột thư viện (Dependency Conflict), ví dụ 2 thư viện phụ thuộc kéo theo 2 phiên bản khác nhau của cùng một file jar thì Maven sẽ xử lý như thế nào?"
- **Trả lời**: *"Dạ thưa Thầy, Maven xử lý xung đột theo nguyên tắc **'Nearest-Wins' (Gần nhất thì thắng)** dựa trên độ sâu của cây phụ thuộc (Dependency Tree):
  - Phiên bản nào có độ sâu trên cây phụ thuộc gần với file `pom.xml` của dự án hơn thì phiên bản đó sẽ được chọn.
  - Nếu hai phiên bản có cùng độ sâu, Maven sẽ áp dụng nguyên tắc **'First-Declared' (Khai báo trước thì thắng)**, tức là dependency nào được khai báo trước trong file `pom.xml` thì thư viện con của nó sẽ được ưu tiên giữ lại ạ!"*

---

## Mục 1: Lớp Khởi Chạy Ứng Dụng (`BlogWebsiteApplication.java`)

- **Vị trí**: `src/main/java/com/group/blog/BlogWebsiteApplication.java`
- **Mã nguồn**:
  ```java
  package com.group.blog;

  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;

  @SpringBootApplication
  public class BlogWebsiteApplication {
      public static void main(String[] args) {
          SpringApplication.run(BlogWebsiteApplication.class, args);
      }
  }
  ```
- **Phân tích từng dòng & Lý thuyết cốt lõi**:
  - Dòng 6: `@SpringBootApplication` — Đây là **Meta-Annotation (Annotation tổ hợp)** cực kỳ quan trọng, tương đương với việc gộp 3 Annotation lớn sau:
    1. `@SpringBootConfiguration`: Đánh dấu class này là nguồn cấu hình chính (Configuration Bean) cho ứng dụng.
    2. `@EnableAutoConfiguration`: Bật cơ chế cấu hình tự động của Spring Boot. Dựa vào các file `.jar` trong `pom.xml`, Spring Boot tự động cấu hình Tomcat, Hibernate, MySQL DataSource, Thymeleaf, Spring Security... mà bạn không cần phải cấu hình file XML phức tạp như thời Spring MVC cũ.
    3. `@ComponentScan`: Tự động quét từ package hiện tại (`com.group.blog`) đi xuống tất cả các sub-package con (`config`, `controller`, `service`, `repository`, `entity`, `mapper`) để tìm các class có gắn `@Component`, `@Service`, `@Repository`, `@RestController`, `@Controller` và tự động khởi tạo thành các **Spring Bean** đưa vào **Spring IoC Container**.
  - Dòng 8: `public static void main(String[] args)`: Hàm `main` chuẩn của Java, là điểm khởi động (Entry Point) của toàn bộ chương trình khi chạy.
  - Dòng 9: `SpringApplication.run(BlogWebsiteApplication.class, args)`: Kích hoạt toàn bộ vòng đời khởi động của Spring Boot:
    - Tạo đối tượng `ApplicationContext` (vũ trụ chứa Bean).
    - Quét môi trường cấu hình (đọc `application.yaml`, `application-secret.yml`).
    - Khởi động máy chủ web nhúng **Embedded Tomcat** mặc định chạy tại cổng `8080`.
    - Kết nối cơ sở dữ liệu MySQL và kích hoạt Hibernate tự sinh/cập nhật bảng.
- **Câu hỏi vấn đáp Thầy hay hỏi**:
  - *Thầy hỏi: "Annotation `@SpringBootApplication` gồm những gì? Nếu thầy để một Controller ở package `com.other.controller` thì Spring có nhận không?"*
  - *Trả lời*: *"Dạ thưa Thầy, `@SpringBootApplication` gồm 3 annotation: `@SpringBootConfiguration`, `@EnableAutoConfiguration` và `@ComponentScan`. Mặc định `@ComponentScan` chỉ quét từ package chứa file Application trở xuống (`com.group.blog.*`). Nếu để ở package `com.other`, Spring Boot sẽ không tìm thấy Bean Controller đó và khi gọi API sẽ bị lỗi HTTP 404 Not Found ạ!"*

---

## Mục 2: Tầng Cấu Hình (Configuration Package)

### 1.1. `SecurityConfig.java` — Trái tim bảo mật hệ thống (Spring Security 6 & JWT)

- **Vị trí**: `src/main/java/com/group/blog/config/SecurityConfig.java`
- **Công dụng**: Cấu hình bảo mật phân quyền theo kiến trúc **Stateless RESTful API** dùng **JWT (JSON Web Token)** kết hợp thư viện Spring Security 6 mới nhất.
- **Phân tích chi tiết từng khối mã nguồn**:
  1. `@Configuration` & `@EnableWebSecurity`:
     - `@Configuration`: Báo cho Spring biết class này định nghĩa các `@Bean` cấu hình.
     - `@EnableWebSecurity`: Kích hoạt bộ lọc bảo mật web của Spring Security, ghi đè toàn bộ cấu hình mặc định.
  2. Mảng đường dẫn `PUBLIC_POST_ENDPOINTS` & `PUBLIC_GET_ENDPOINTS`:
     - `PUBLIC_POST_ENDPOINTS`: Gồm `/users` (đăng ký), `/auth/login` (đăng nhập lấy token), `/auth/introspect` (kiểm tra token). Bất kỳ ai cũng gửi request POST được mà không cần Token.
     - `PUBLIC_GET_ENDPOINTS`: Mở toàn bộ file tĩnh (`/assets/**`, `/fragments/**`), các trang HTML Thymeleaf (`/`, `/home`, `/post`, `/login`...) và các API đọc dữ liệu công khai (`/categories`, `/tags`, `/blogs/**`).
     - `ADMIN_ENDPOINTS = {"/api/admin/**"}`: Chỉ duy nhất tài khoản có quyền `ROLE_ADMIN` mới được phép gọi.
  3. Phương thức `filterChain(HttpSecurity httpSecurity)`:
     - `httpSecurity.cors(...)`: Cho phép trình duyệt gửi request đa nguồn (Cross-Origin).
     - `httpSecurity.authorizeHttpRequests(...)`: Thiết lập quy tắc phân quyền:
       - `.requestMatchers(HttpMethod.POST, PUBLIC_POST_ENDPOINTS).permitAll()`: Cho phép truy cập không cần token.
       - `.requestMatchers(HttpMethod.GET, PUBLIC_GET_ENDPOINTS).permitAll()`: Cho phép truy cập không cần token.
       - `.requestMatchers(ADMIN_ENDPOINTS).hasRole("ADMIN")`: Bắt buộc phải có quyền Admin.
       - `.anyRequest().authenticated()`: Tất cả các API còn lại (viết bài, like, comment, bookmark, upload...) bắt buộc phải có Token JWT hợp lệ.
     - `httpSecurity.oauth2ResourceServer(...)`: Cấu hình máy chủ OAuth2 Resource Server. Khi client gửi request kèm Header `Authorization: Bearer <token>`, Spring Security tự động trích xuất token và chuyển cho `jwtDecoder()` giải mã.
     - `httpSecurity.csrf(AbstractHttpConfigurer::disable)`: **Tắt CSRF**. Vì hệ thống lưu Token ở `localStorage` và gửi qua Header HTTP, trình duyệt không tự động gửi Cookie, loại bỏ 100% nguy cơ tấn công CSRF.
     - `httpSecurity.sessionManagement(...STATELESS)`: Yêu cầu Spring Security **không bao giờ tạo Session trên RAM máy chủ**. Mỗi request gửi lên là một đơn vị độc lập (Stateless).
  4. Phương thức `jwtAuthenticationConverter()`:
     - Trích xuất claim `scope` từ payload của JWT (ví dụ chuỗi `"ADMIN"` hoặc `"USER"`).
     - Dùng `setAuthorityPrefix("ROLE_")` để tự động biến `"ADMIN"` thành `"ROLE_ADMIN"`. Nhờ vậy phương thức `.hasRole("ADMIN")` mới so khớp thành công.
  5. Phương thức `jwtDecoder()`:
     - Tạo đối tượng `SecretKeySpec` với thuật toán mã hóa `HmacSHA512` và chuỗi bí mật `signerKey` lấy từ `application.yaml`.
     - Sử dụng `NimbusJwtDecoder` để giải mã và kiểm tra tính toàn vẹn chữ ký số. Nếu token bị hacker sửa đổi dù chỉ 1 ký tự, chữ ký sẽ không khớp và request bị từ chối ngay lập tức.
  6. Phương thức `passwordEncoder()`:
     - Khởi tạo `@Bean` trả về `new BCryptPasswordEncoder(10)`.
     - Thuật toán băm một chiều BCrypt kết hợp 10 vòng muối ngẫu nhiên (salt), bảo đảm mật khẩu lưu trong MySQL không thể bị dịch ngược ra ban đầu.

### 1.2. `CorsConfig.java` — Cho phép truy cập đa nguồn (Cross-Origin Resource Sharing)

- **Vị trí**: `src/main/java/com/group/blog/config/CorsConfig.java`
- **Mã nguồn**:
  ```java
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
- **Phân tích từng dòng & Lý thuyết**:
  - **CORS là gì?** Cơ chế bảo mật của trình duyệt ngăn chặn mã JavaScript chạy từ một tên miền (Origin) này gửi request đến một tên miền khác.
  - `registry.addMapping("/**")`: Áp dụng chính sách CORS cho toàn bộ các endpoint URL trong hệ thống.
  - `.allowedOriginPatterns("*")`: Cho phép mọi tên miền gọi vào (ví dụ Frontend chạy ở `localhost:3000` hoặc `127.0.0.1:5500` đều kết nối được tới Backend `localhost:8080`).
  - `.allowedMethods("GET", "POST", "PUT", "DELETE", "OPTIONS")`: Cho phép đầy đủ 5 phương thức chuẩn RESTful. Trong đó phương thức `OPTIONS` cực kỳ quan trọng để trình duyệt gửi yêu cầu tiền kiểm tra (**Preflight Request**).
  - `.allowedHeaders("*")`: Chấp nhận mọi Header từ Client gửi lên (đặc biệt là Header `Authorization` và `Content-Type: application/json`).
  - `.allowCredentials(true)`: Cho phép client gửi kèm thông tin xác thực nếu cần.

### 1.3. `ApplicationInitConfig.java` — Tự động gieo dữ liệu khởi tạo (Data Seeding)

- **Vị trí**: `src/main/java/com/group/blog/config/ApplicationInitConfig.java`
- **Công dụng**: Sử dụng functional interface `@Bean ApplicationRunner` của Spring Boot để tự động chạy mã lệnh ngay sau khi ứng dụng khởi động thành công.
- **Phân tích chi tiết luồng xử lý**:
  1. Kiểm tra: `if (userRepository.findByUsername("admin").isEmpty())`. Nếu đã có tài khoản `admin` thì bỏ qua (chống tạo trùng lặp dữ liệu khi restart app).
  2. Tạo tài khoản Admin mặc định:
     - `username: admin`, `password: passwordEncoder.encode("123456")`.
     - `roles: Set.of("ADMIN", "USER")`.
  3. Tạo 3 tài khoản cho 3 thành viên thực hiện đồ án:
     - `duonghd` (Hoàng Đại Dương - 24743991)
     - `dungnt` (Nguyễn Trung Dũng - 24000905)
     - `longlt` (Lê Thành Long - 23630851)
  4. Tạo sẵn 4 Danh mục chủ đề: `Technology`, `Programming`, `Web Design`, `Life & Tips`.
  5. Tạo sẵn 5 Thẻ Tag: `Java`, `SpringBoot`, `Bootstrap`, `Thymeleaf`, `AI`.
  6. Tạo sẵn 3 Bài viết Blog mẫu kèm nội dung HTML, ảnh banner Cloudinary, tác giả và gắn thẻ để khi mở web lên là có sẵn bài viết hiển thị ngay mà không bị trống trang.

### 1.4. `CloudinaryConfig.java` — Cấu hình tích hợp lưu trữ đám mây

- **Vị trí**: `src/main/java/com/group/blog/config/CloudinaryConfig.java`
- **Mã nguồn**:
  ```java
  @Configuration
  public class CloudinaryConfig {
      @Value("${cloudinary.cloud-name}")
      private String cloudName;
      @Value("${cloudinary.api-key}")
      private String apiKey;
      @Value("${cloudinary.api-secret}")
      private String apiSecret;

      @Bean
      public Cloudinary cloudinary() {
          Map<String, String> config = new HashMap<>();
          config.put("cloud_name", cloudName);
          config.put("api_key", apiKey);
          config.put("api_secret", apiSecret);
          return new Cloudinary(config);
      }
  }
  ```
- **Phân tích từng dòng & Lý thuyết**:
  - `@Value("${cloudinary.cloud-name}")`: Đọc giá trị tương ứng từ file cấu hình `application-secret.yml`. Giúp bảo mật thông tin tài khoản Cloudinary, không bị lộ khóa bí mật (API Secret) lên Git.
  - `@Bean public Cloudinary cloudinary()`: Khởi tạo đối tượng `Cloudinary` từ thông số kết nối và đăng ký vào Spring IoC Container. Nhờ vậy class `CloudinaryService` có thể tự động inject Bean này vào để gọi hàm upload ảnh.

---

## 📌 CHUYÊN ĐỀ ĐẶC BIỆT: TẦNG THỰC THỂ (ENTITY), TẦNG REPOSITORY & DTO

> [!IMPORTANT]
> Toàn bộ nội dung bóc tách chi tiết từng dòng code, từng trường, phân tích Annotation JPA/Hibernate (UUID, LongText, UniqueConstraints, Indexes, Self-referencing Comment, Cascade vs OnDelete), các câu truy vấn JPQL phức tạp (Cartesian Product, LEFT JOIN, COUNT DISTINCT) và cấu trúc 20 DTOs (Request + Response) đã được tách riêng thành một chuyên đề độc lập tại:  
> 🔗 **[CHUYEN_DE_DTO_ENTITY_REPOSITORY.md](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/ck-luu-y/CHUYEN_DE_DTO_ENTITY_REPOSITORY.md)**  
> Sinh viên mở file trên để ôn tập chuyên sâu về 10 Entities, 10 Repositories, 20 DTOs cùng 4 câu hỏi vấn đáp CSDL đỉnh cao (N+1 query problem, UUID vs Auto-increment, CascadeType vs @OnDelete, LazyInitializationException).

---

## Mục 3: Tầng Nghiệp Vụ (Service Package - Toàn Bộ 10 Services)

Tầng Service là "trái tim xử lý logic" (Business Logic Layer) của hệ thống. Tất cả các class Service trong dự án đều sử dụng các Annotation chuẩn mực của Spring Boot & Lombok:
- `@Service`: Đánh dấu class là một Spring Bean thuộc tầng nghiệp vụ, được Spring IoC Container quản lý vòng đời.
- `@RequiredArgsConstructor`: Annotation của Lombok tự động sinh Constructor chứa tất cả các thuộc tính khai báo `final`. Đây là chuẩn mực **Constructor Dependency Injection ngầm định (Implicit DI)** của Spring, giúp loại bỏ hoàn toàn việc phải gõ `@Autowired` thủ công.
- `@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)`: Thiết lập mặc định cho tất cả các biến trường trong class thành `private final`, bảo đảm tính đóng gói và tính bất biến (Immutability).
- `@Transactional`: Quản lý giao dịch CSDL tự động theo nguyên tắc ACID. Nếu có ngoại lệ `RuntimeException`, toàn bộ thao tác SQL trong hàm sẽ tự động được Rollback.

---

### 4.1. `AuthenticationService.java` — Xác thực tài khoản & Ký phát sinh Token JWT

- **Vị trí**: `src/main/java/com/group/blog/service/AuthenticationService.java`
- **Các phương thức chi tiết**:
  1. `authenticate(AuthenticationRequest request)`:
     - Dòng 35: `var user = userRepository.findByUsername(request.getUsername()).orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));`: Tìm tài khoản theo username trong bảng `users`. Nếu không có, ném lỗi nghiệp vụ `USER_NOT_EXITED` (mã lỗi 1005).
     - Dòng 38: `boolean authenticated = passwordEncoder.matches(request.getPassword(), user.getPassword());`: Dùng thuật toán BCrypt so khớp mật khẩu người dùng gõ vào form với chuỗi mật khẩu đã được băm mã hóa lưu trong MySQL. Tuyệt đối không so sánh bằng `==` hay `.equals()`.
     - Dòng 39-41: Nếu `!authenticated`, ném lỗi `UNAUTHENTICATED` (mã lỗi 1006).
     - Dòng 43-44: Thiết lập thời gian sống của Token là 1 giờ (`Instant.now().plus(1, ChronoUnit.HOURS)`), gọi hàm `generateToken(user, expiryTime)` và đóng gói vào `AuthenticationResponse`.
  2. `generateToken(User user, Date expiryTime)`:
     - Tạo Header: Khai báo thuật toán mã hóa `JWSAlgorithm.HS512`.
     - Tạo Payload: Chứa các Claim theo chuẩn RFC 7519:
       - `sub` (Subject): Định danh người dùng bằng `user.getUsername()`.
       - `iss` (Issuer): Đơn vị cấp phát `"group.com"`.
       - `iat` (Issued At): Thời điểm cấp phát `new Date()`.
       - `exp` (Expiration Time): Thời điểm hết hạn `expiryTime`.
       - `scope`: Chuỗi lưu quyền hạn người dùng (nối các quyền trong bảng `user_roles` bằng dấu cách, ví dụ `"ADMIN USER"`).
     - Ký số: Sử dụng khóa bí mật `SIGNER_KEY` với đối tượng `new MACSigner(SIGNER_KEY.getBytes())` để tính toán phần Chữ ký điện tử (Signature).
     - Ghép 3 phần tạo thành chuỗi JWT chuẩn: `Header.Payload.Signature`.
  3. `introspect(IntrospectRequest request)`:
     - Nhận vào chuỗi token từ client gửi lên.
     - Dùng `JWSVerifier` kiểm tra tính hợp lệ của chữ ký và thời gian hết hạn (`expirationTime`).
     - Trả về đối tượng `IntrospectResponse.builder().valid(verified && !isExpired).build()`.

---

### 4.2. `UserService.java` — Quản trị thông tin người dùng & Phân quyền

- **Vị trí**: `src/main/java/com/group/blog/service/UserService.java`
- **Các phương thức chi tiết**:
  1. `createUser(UserCreatetionRequest request)`:
     - Kiểm tra trùng username: `if (userRepository.existsByUsername(request.getUsername())) throw new AppException(ErrorCode.USER_EXITED);`.
     - Dùng `userMapper.toUser(request)` chuyển DTO sang Entity User.
     - Mã hóa mật khẩu: `user.setPassword(passwordEncoder.encode(request.getPassword()));`.
     - Gán quyền mặc định: Khởi tạo HashSet và gán quyền `ROLE_USER` cho tài khoản mới.
     - Lưu xuống MySQL và trả về `UserResponse`.
  2. `getMyProfile()`:
     - Lấy username từ ngữ cảnh bảo mật hiện tại: `SecurityContextHolder.getContext().getAuthentication().getName()`.
     - Lấy User từ DB, chuyển sang DTO và gọi `followService.enrichUserResponse()` để bổ sung thông tin số lượng người theo dõi (Followers) và đang theo dõi (Following).
  3. `changePassword(PasswordChangeRequest request)`:
     - Lấy username người đăng nhập.
     - So khớp mật khẩu cũ: `if (!passwordEncoder.matches(request.getOldPassword(), user.getPassword())) throw new AppException(ErrorCode.PASSWORD_INCORRECT);`.
     - Kiểm tra xác nhận mật khẩu mới: `if (!request.getNewPassword().equals(request.getConfirmPassword())) throw new AppException(ErrorCode.PASSWORD_NOT_MATCH);`.
     - Mã hóa mật khẩu mới bằng `passwordEncoder.encode()` và lưu đè vào CSDL.
  4. `updateUser(UUID id, UserUpdateRequest request)`:
     - Phương thức dành riêng cho Admin cập nhật thông tin và phân quyền cho thành viên.
     - Dùng `u.getRoles().clear()` xóa các quyền cũ và `u.getRoles().addAll(request.getRoles())` nạp danh sách quyền mới (ví dụ thăng cấp từ `USER` lên `ADMIN`).

---

### 4.3. `BlogService.java` — Xử lý nghiệp vụ bài viết, bản nháp & tìm kiếm gợi ý

- **Vị trí**: `src/main/java/com/group/blog/service/BlogService.java`
- **Các phương thức chi tiết**:
  1. `createBlog(BlogCreationRequest request)`:
     - Lấy tác giả từ SecurityContext.
     - Tìm kiếm Category nếu có truyền `categoryId`.
     - **Cơ chế lưu Tag thông minh**: Quét từng tên tag trong mảng `request.getTags()`. Nếu tag đã có trong DB thì lấy lại; nếu chưa có thì tự động tạo mới `new Tag(name)` và lưu vào bảng `tags` (`tagRepository.save()`). Cách này giúp người dùng gõ tag tùy thích mà không bị lỗi ràng buộc dữ liệu.
     - Dùng `blogMapper.toBlog(request)` tạo Entity, gán tác giả, danh mục và tập hợp thẻ tags.
     - Đặt trạng thái ban đầu: Nếu `request.getDraft() == false` thì gán `publishedAt = LocalDateTime.now()`.
     - Lưu xuống bảng `blogs`.
  2. `updateBlog(UUID id, BlogUpdateRequest request)`:
     - Kiểm tra quyền: `if (!blog.getAuthor().getUsername().equals(currentUsername)) throw new AppException(ErrorCode.UNAUTHORIZED);` $\rightarrow$ Chỉ chính tác giả mới được sửa bài của mình.
     - **Thuật toán xử lý Lưu Nháp vs Xuất Bản**:
       - *Trường hợp 1 (Bấm Save Draft)*: Nếu bài viết đã từng xuất bản trước đó (`blog.isDraft() == false`), hệ thống **giữ nguyên nội dung cũ ở cột `content`** để độc giả đọc bình thường, và chỉ ghi nội dung đang chỉnh sửa dở vào cột **`draftContent`**.
       - *Trường hợp 2 (Bấm Publish)*: Đổ toàn bộ nội dung mới vào cột `content`, xóa rỗng `draftContent = null`, chuyển cờ `draft = false`, cập nhật `publishedAt = LocalDateTime.now()`.
  3. `getBlogById(UUID id)`:
     - Tìm bài viết theo `id`.
     - **Ghi log lượt xem**: Tạo một bản ghi `BlogView` mới (lưu `blog_id`, `user_id` và `viewedAt = LocalDateTime.now()`) lưu xuống bảng `blog_views`.
     - Kiểm tra trạng thái tương tác: Kiểm tra xem user đang đăng nhập đã Like bài này chưa (`likedByCurrentUser`) và đã Bookmark bài này chưa (`bookmarkedByCurrentUser`).
  4. `deleteBlog(UUID id)`:
     - Phân quyền xóa: Cho phép **Tác giả bài viết** HOẶC **Người dùng có quyền `ROLE_ADMIN`** thực hiện xóa. Nếu không thỏa mãn ném `UNAUTHORIZED`.
  5. `getSearchSuggestions(String keyword)`:
     - Tìm kiếm nhanh 5 bài viết khớp từ khóa trong tiêu đề qua `blogRepository.findTop5ByTitleContainingIgnoreCaseAndDraftFalse()`.
     - Chuyển thành `BlogSuggestionResponse` (chỉ gồm `id`, `title`, `authorName`, `categoryName`) để phục vụ tính năng tìm kiếm gợi ý tức thì khi người dùng đang gõ phím ở thanh Search.

---

### 4.4. `AdminService.java` — Thống kê số liệu bảng điều khiển Dashboard

- **Vị trí**: `src/main/java/com/group/blog/service/AdminService.java`
- **Phương thức `getDashboardStats()`**:
  - `long totalUsers = userRepository.count();`: Đếm tổng số lượng tài khoản trong bảng `users`.
  - `long totalPosts = blogRepository.countByDraftFalse();`: Đếm tổng số bài viết đã xuất bản công khai (bỏ qua các bài nháp).
  - Lấy 5 bài viết mới nhất: Gọi `blogRepository.findTop5ByDraftFalseOrderByCreatedAtDesc()`, dùng Stream API ánh xạ sang `BlogResponse`.
  - Đóng gói toàn bộ vào đối tượng `AdminStatsResponse` gửi về cho giao diện `dashboard.html`.

---

### 4.5. `CategoryService.java` — Quản trị chuyên mục bài viết

- **Vị trí**: `src/main/java/com/group/blog/service/CategoryService.java`
- **Các phương thức chi tiết**:
  1. `create(CategoryRequest request)`: Kiểm tra `existsByName()`, nếu trùng ném `CATEGORY_EXITED`, ngược lại lưu vào CSDL.
  2. `update(UUID id, CategoryRequest request)`: Cập nhật tên chuyên mục, kiểm tra chống trùng lặp tên với các danh mục khác.
  3. `delete(UUID id)`: Xóa chuyên mục theo `id`.
  4. `getAllCategories()`:
     - Gọi câu truy vấn JPQL `findAllCategoriesWithPostCount()` để lấy danh sách danh mục kèm số lượng bài viết của từng danh mục.
     - Dùng `SlugUtils.generateSlug()` tạo chuỗi slug kèm ID (ví dụ: `cong-nghe-UUID`) hỗ trợ chia sẻ link và SEO.

---

### 4.6. `TagService.java` — Quản lý thẻ từ khóa bài viết

- **Vị trí**: `src/main/java/com/group/blog/service/TagService.java`
- **Các phương thức chi tiết**:
  1. `getAllTags()`: Gọi câu truy vấn `findAllTagsWithPostCount()` trong `TagRepository` để lấy danh sách tất cả các thẻ tag kèm theo số lượng bài viết đang gắn thẻ đó.
  2. `create(CategoryRequest request)`: Thêm mới thẻ tag thủ công từ trang quản trị Admin.
  3. `update(UUID id, CategoryRequest request)`: Cập nhật tên thẻ tag.

---

### 4.7. `InteractionService.java` — Quản lý tương tác: Thả tim, Bình luận & Bookmark

- **Vị trí**: `src/main/java/com/group/blog/service/InteractionService.java`
- **Các phương thức chi tiết**:
  1. `@Transactional toggleLike(UUID blogId)`:
     - Tìm kiếm `blogLikeRepository.findByBlogIdAndUserUsername(blogId, username)`.
     - Nếu đã tồn tại $\rightarrow$ Gọi `delete()` (Bỏ thích - Unlike).
     - Nếu chưa tồn tại $\rightarrow$ Gọi `save()` tạo mới bản ghi `BlogLike`, đồng thời gọi `notificationService.createNotification()` để bắn chuông thông báo cho tác giả bài viết (`type = "LIKE"`).
  2. `@Transactional addComment(UUID blogId, CommentRequest request)`:
     - Tạo bản ghi `Comment`. Nếu `request.getParentId() != null`, tìm comment cha trong DB và gán `comment.setParent(parentComment)` để tạo nhánh trả lời (reply).
     - Bắn thông báo thông minh:
       - Nếu là bình luận bài viết: Bắn thông báo cho Tác giả bài viết (`type = "COMMENT"`).
       - Nếu là reply bình luận: Bắn thông báo trực tiếp cho Chủ của bình luận cha (`type = "REPLY"`).
  3. `@Transactional deleteComment(UUID commentId)`:
     - Kiểm tra quyền: Chỉ cho phép **Chính tác giả của bình luận đó** HOẶC **Chủ sở hữu của bài viết chứa bình luận đó** mới có quyền xóa.
  4. `@Transactional toggleBookmark(UUID blogId)`:
     - Bật/tắt lưu bài viết đọc sau. Nếu đã có thì xóa khỏi `bookmarks`, nếu chưa thì thêm mới.
  5. `getMyBookmarks()`:
     - Lấy danh sách các bài viết mà user hiện tại đã lưu, sắp xếp theo thời gian lưu mới nhất (`findByUserUsernameOrderByCreatedAtDesc`).

---

### 4.8. `FollowService.java` — Quản lý quan hệ theo dõi giữa các tác giả

- **Vị trí**: `src/main/java/com/group/blog/service/FollowService.java`
- **Các phương thức chi tiết**:
  1. `@Transactional toggleFollow(String targetUsername)`:
     - Kiểm tra: `if (currentUsername.equals(targetUsername)) throw new RuntimeException("Bạn không thể tự theo dõi chính mình");`.
     - Kiểm tra `userFollowRepository.findByFollowerUsernameAndFollowingUsername()`.
     - Nếu đã follow $\rightarrow$ Xóa bản ghi (Unfollow).
     - Nếu chưa follow $\rightarrow$ Tạo mới bản ghi `UserFollow`, đồng thời gửi thông báo `type = "FOLLOW"` cho tác giả được theo dõi.
  2. `enrichUserResponse(UserResponse response, String targetUsername, String currentUsername)`:
     - Đếm tổng số người đang theo dõi tác giả: `countByFollowingUsername()`.
     - Đếm tổng số người mà tác giả đang theo dõi: `countByFollowerUsername()`.
     - Kiểm tra xem người đang duyệt web đã bấm theo dõi tác giả này chưa: `existsByFollowerUsernameAndFollowingUsername()`.

---

### 4.9. `NotificationService.java` — Quản lý chuông thông báo cá nhân

- **Vị trí**: `src/main/java/com/group/blog/service/NotificationService.java`
- **Các phương thức chi tiết**:
  1. `createNotification(User recipient, String message, String targetUrl, String type)`:
     - Chặn thông báo tự kỷ: `if (recipient.getUsername().equals(currentUsername)) return;` $\rightarrow$ Nếu tự like/comment bài của chính mình thì không gửi thông báo.
     - Tạo Entity `Notification`, gán `isRead = false`, lưu vào bảng `notifications`.
  2. `getMyNotifications()`:
     - Lấy danh sách thông báo của tài khoản đang đăng nhập qua `findByUserUsernameOrderByCreatedAtDesc(username)`.
  3. `@Transactional markAsRead(UUID id)`: Đánh dấu thông báo đã đọc (`n.setRead(true)`).
  4. `deleteNotification(UUID id)`: Xóa thông báo khỏi danh sách.

---

### 4.10. `CloudinaryService.java` — Tải và quản lý tệp hình ảnh đám mây

- **Vị trí**: `src/main/java/com/group/blog/service/CloudinaryService.java`
- **Phương thức `uploadImage(MultipartFile file)`**:
  - Nhận đối tượng file nhị phân `MultipartFile` từ form tải lên.
  - Sử dụng phương thức `cloudinary.uploader().upload(file.getBytes(), ObjectUtils.asMap("resource_type", "auto"))`.
  - Cloudinary tiếp nhận mảng byte, tự động nén ảnh và chuyển đổi định dạng tối ưu.
  - Trích xuất trường `secure_url` (đường link ảnh bảo mật HTTPS) trả về cho Controller.

---

## Mục 4: Tầng Điều Khiển (Controller Package - Toàn Bộ 8 Controllers)

Tầng Controller tiếp nhận HTTP Request từ Client, gọi Service tương ứng xử lý nghiệp vụ, và trả về dữ liệu chuẩn JSON được bọc trong đối tượng `ApiResponse<T>`.

### 4.1. Khái niệm lý thuyết cốt lõi cần nhớ khi vấn đáp:
- `@RestController`: Bằng `@Controller` + `@ResponseBody`. Báo hiệu mọi phương thức trong class này đều tuần tự hóa kết quả trả về trực tiếp thành chuỗi **JSON** (qua bộ chuyển đổi Jackson), không chuyển hướng sang trang HTML.
- `@Controller`: Dành riêng cho `ViewController.java` để Spring MVC hiểu là trả về tên file giao diện HTML (Thymeleaf View).
- `@RequestMapping("/path")`: Khai báo tiền tố đường dẫn dùng chung cho tất cả các endpoint trong Controller.
- `@PathVariable`: Trích xuất giá trị nằm trực tiếp trên đường dẫn URL (ví dụ: `/blogs/{id}`).
- `@RequestParam`: Trích xuất tham số Query Parameter sau dấu `?` (ví dụ: `/blogs/search?keyword=java`).
- `@RequestBody`: Yêu cầu Spring trích xuất nội dung phần thân JSON của HTTP Request và parse tự động sang đối tượng DTO Java.
- `@Valid`: Kích hoạt cơ chế kiểm tra tính hợp lệ của dữ liệu đầu vào (Hibernate Validator) trước khi đưa dữ liệu vào Service.

---

### 4.2. `AuthenticationController.java` — Quản lý đăng nhập & kiểm tra Token
- `@RequestMapping("/auth")`:
  - `@PostMapping("/login")`: Nhận `AuthenticationRequest` (`username`, `password`), gọi `authenticationService.authenticate()`, trả về chuỗi Token JWT.
  - `@PostMapping("/introspect")`: Nhận `IntrospectRequest` (`token`), gọi `authenticationService.introspect()`, trả về kết quả token còn sống hay đã chết.

### 4.3. `UserController.java` — Quản trị người dùng & Hồ sơ cá nhân
- `@RequestMapping("/users")`:
  - `@PostMapping`: Tiếp nhận đăng ký thành viên mới (`UserCreatetionRequest`), có gắn `@Valid` kiểm tra độ dài username/password.
  - `@GetMapping`: Lấy danh sách toàn bộ người dùng (Yêu cầu quyền Admin).
  - `@GetMapping("/my-profile")`: Lấy thông tin cá nhân của chính mình.
  - `@PutMapping("/my-profile")`: Cập nhật Bio, Email, Avatar của tôi.
  - `@PutMapping("/my-profile/change-password")`: Nhận DTO đổi mật khẩu.
  - `@GetMapping("/profile/{username}")`: Lấy hồ sơ công khai của một tác giả bất kỳ để hiển thị trang tác giả.

### 4.4. `BlogController.java` — Điều phối toàn bộ hoạt động bài viết
- `@RequestMapping("/blogs")`:
  - `@PostMapping`: Tạo bài viết mới (`@Valid BlogCreationRequest`).
  - `@GetMapping`: Lấy danh sách bài viết trang chủ kèm thống kê tương tác.
  - `@GetMapping("/{id}")`: Xem chi tiết bài viết theo UUID.
  - `@PutMapping("/{id}")`: Chỉnh sửa bài viết.
  - `@DeleteMapping("/{id}")`: Xóa bài viết.
  - `@GetMapping("/category/{categoryId}")`: Lọc bài viết theo danh mục.
  - `@GetMapping("/tag/{tagId}")`: Lọc bài viết theo thẻ tag.
  - `@GetMapping("/search")`: Tìm kiếm bài viết theo từ khóa `?keyword=...`.
  - `@GetMapping("/search/suggestions")`: Trả về danh sách gợi ý nhanh khi gõ phím.
  - `@GetMapping("/filter")`: Lọc kết hợp đa tiêu chí (vừa có từ khóa vừa có categoryId).
  - `@GetMapping("/my-blogs")`: Lấy tất cả bài viết do tài khoản hiện tại tạo ra (kể cả bản nháp).

### 4.5. `InteractionController.java` — Điều phối Thả tim, Bình luận & Bookmark
- `@RequestMapping("/interactions")`:
  - `@PostMapping("/likes/{blogId}")`: Thả tim / Bỏ like.
  - `@GetMapping("/comments/{blogId}")`: Lấy danh sách cây bình luận của bài viết.
  - `@PostMapping("/comments/{blogId}")`: Thêm bình luận mới hoặc gửi phản hồi reply.
  - `@DeleteMapping("/comments/{commentId}")`: Xóa bình luận.
  - `@PostMapping("/bookmarks/{blogId}")`: Thêm / Xóa bài viết khỏi mục Bookmark.
  - `@GetMapping("/bookmarks/my-bookmarks")`: Lấy danh sách các bài viết đã lưu.

### 4.6. `FollowController.java` — Điều phối theo dõi tác giả
- `@RequestMapping("/follows")`:
  - `@PostMapping("/{targetUsername}")`: Theo dõi / Bỏ theo dõi tác giả.
  - `@GetMapping("/followers/{targetUsername}")`: Lấy danh sách người đang theo dõi tác giả này.
  - `@GetMapping("/following/{targetUsername}")`: Lấy danh sách tác giả mà người này đang theo dõi.

### 4.7. `NotificationController.java` — Điều phối chuông thông báo
- `@RequestMapping({"/api/notifications", "/notifications/api"})`:
  - `@GetMapping`: Lấy toàn bộ thông báo của tôi.
  - `@PutMapping("/{id}/read")`: Đánh dấu thông báo đã đọc.
  - `@DeleteMapping("/{id}")`: Xóa thông báo khỏi danh sách.

### 4.8. `AdminController.java` — Điều phối số liệu thống kê quản trị
- `@RequestMapping("/api/admin")`:
  - `@GetMapping("/stats")`: Gọi `adminService.getDashboardStats()` để lấy tổng số thành viên, tổng số bài viết và danh sách 5 bài viết mới nhất cho Dashboard Admin. Endpoint này được Spring Security bảo vệ bằng luật `.hasRole("ADMIN")`.

### 4.9. `UploadController.java` — Điều phối tải tệp ảnh lên đám mây
- `@RequestMapping("/upload")`:
  - `@PostMapping("/image")`: Nhận tham số `@RequestParam("file") MultipartFile file`, chuyển qua `cloudinaryService.uploadImage(file)` để tải lên đám mây và trả về đường dẫn ảnh công khai HTTPS.

### 4.10. `ViewController.java` — Điều hướng hiển thị các trang giao diện HTML Thymeleaf
- Gắn `@Controller`:
  - Chứa 16 phương thức `@GetMapping` điều hướng các đường dẫn URL (`/`, `/login`, `/register`, `/post`, `/admin/dashboard`...) về các file HTML tương ứng trong thư mục `templates/`.

---

## Mục 5: Tầng Xử Lý Ngoại Lệ, Chuyển Đổi DTO & Tiện Ích (Exception, Mapper & Util)

### 5.1. Tầng Xử Lý Ngoại Lệ Tập Trung (Exception Package)

Hệ thống thiết kế cơ chế xử lý lỗi tập trung theo chuẩn Enterprise, không bao giờ để lộ vết lỗi hệ thống (Stacktrace) hay mã lỗi 500 xấu xí ra màn hình người dùng.

1. **`ErrorCode.java` (Enum định nghĩa danh mục lỗi)**:
   - Là một `enum` chứa danh sách mã lỗi nghiệp vụ chuẩn hóa:
     - `UNCATEGORIZED_EXCEPTION(9999, "Uncategorized error")`: Lỗi hệ thống chưa phân loại.
     - `USER_EXITED(1002, "User Exited")`: Tài khoản đã tồn tại.
     - `USERNAME_INVALID(1003, "Username must be at least 3 charactes")`: Tên đăng nhập không hợp lệ.
     - `INVALID_PASSWORD(1004, "Password must be at least 8 characters")`: Mật khẩu không hợp lệ.
     - `USER_NOT_EXITED(1005, "User Not Exited")`: Không tìm thấy người dùng.
     - `UNAUTHENTICATED(1006, "Unauthenticated")`: Sai thông tin đăng nhập hoặc token hết hạn.
     - `PASSWORD_INCORRECT(1007, "Mật khẩu cũ không chính xác")`.
     - `PASSWORD_NOT_MATCH(1008, "Mật khẩu xác nhận không khớp")`.
     - `CATEGORY_NOT_FOUND(1009, "Danh mục không tồn tại")`.
     - `BLOG_NOT_FOUND(1010, "Bài viết không tồn tại")`.
     - `UNAUTHORIZED(1011, "Bạn không có quyền thực hiện hành động này")`.
     - `CATEGORY_EXITED(1012, "Danh mục đã tồn tại")`.
   - *Lý thuyết vấn đáp*: Dùng `enum` giúp quản lý mã lỗi tập trung, không bị hardcode chuỗi thông báo rải rác trong code và dễ dàng quốc tế hóa ngôn ngữ (i18n).

2. **`AppException.java` (Ngoại lệ nghiệp vụ tùy chỉnh)**:
   - Kế thừa class `RuntimeException` (Ngoại lệ không bắt buộc khai báo - **Unchecked Exception**).
   - Chứa thuộc tính `private ErrorCode errorCode`.
   - Khi Service phát hiện vi phạm nghiệp vụ, chỉ cần ném ra: `throw new AppException(ErrorCode.USER_NOT_EXITED);`.

3. **`GlobalExceptionHandler.java` (Bộ đón bắt ngoại lệ toàn cục)**:
   - Gắn Annotation `@ControllerAdvice`: Lắng nghe và chặn bắt tất cả các Exception văng ra từ bất kỳ Controller nào trong toàn bộ ứng dụng.
   - `@ExceptionHandler(value = AppException.class)`:
     - Bắt các lỗi do lập trình viên chủ động ném ra (`AppException`).
     - Đóng gói mã lỗi và thông điệp vào đối tượng `ApiResponse`:
       ```java
       ErrorCode errorCode = exception.getErrorCode();
       ApiResponse apiResponse = new ApiResponse();
       apiResponse.setCode(errorCode.getCode());
       apiResponse.setMessage(errorCode.getMessage());
       return ResponseEntity.badRequest().body(apiResponse);
       ```
   - `@ExceptionHandler(value = MethodArgumentNotValidException.class)`:
     - Bắt các lỗi khi dữ liệu trong `@RequestBody` vi phạm các Annotation validation (như `@Size`, `@NotNull`).
   - `@ExceptionHandler(value = Exception.class)`:
     - Tấm lưới an toàn cuối cùng bắt mọi lỗi bất ngờ (NullPointerException, lỗi kết nối DB...). Trả về mã lỗi 9999 để bảo mật hệ thống.

---

### 5.2. Tầng Chuyển Đổi DTO & Entity (Mapper Package - Thư viện MapStruct)

Dự án sử dụng thư viện **MapStruct** — công cụ ánh xạ dữ liệu (Bean Mapper) hàng đầu thế giới hiện nay cho Java.

1. **Lý thuyết cốt lõi về MapStruct**:
   - Khác với `ModelMapper` dùng cơ chế Java Reflection lúc chạy (Runtime) rất chậm và dễ gây lỗi `NullPointerException`, **MapStruct là một bộ tiền xử lý mã nguồn (Annotation Processor)**.
   - Tại thời điểm biên dịch (`javac`), MapStruct tự động đọc các interface Mapper và **tự sinh mã nguồn Java thuần 100%** trong thư mục `target/generated-sources/annotations/com/group/blog/mapper/` với các lệnh gán `getter/setter` trực tiếp. Tốc độ thực thi nhanh ngang bằng code tay và hoàn toàn Type-safe.
2. **`UserMapper.java`**:
   - `@Mapper(componentModel = "spring")`: Yêu cầu MapStruct tạo Bean Spring để có thể inject vào Service.
   - `User toUser(UserCreatetionRequest request);`: Tự động map các trường trùng tên (`username`, `email`...) từ DTO sang Entity User.
   - `UserResponse toUserResponse(User user);`: Chuyển Entity User thành DTO trả về cho client.
   - `void updateUser(@MappingTarget User user, UserUpdateRequest request);`: Dùng `@MappingTarget` để cập nhật trực tiếp dữ liệu từ DTO vào đối tượng User đã có sẵn mà không cần khởi tạo lại đối tượng.
3. **`BlogMapper.java`**:
   - `@Mapping(target = "category", ignore = true)`: Báo cho MapStruct bỏ qua việc map tự động trường `category` để Service tự tìm kiếm và gán đối tượng Category chính xác.
   - `@Mapping(target = "tags", ignore = true)`: Bỏ qua trường `tags` để Service tự xử lý logic gán và lưu thẻ tag.
   - `@Mapping(target = "author", ignore = true)`: Bỏ qua trường `author` để Service lấy trực tiếp từ `SecurityContextHolder`.
4. **`CategoryMapper.java`**:
   - `@Mapping(target = "blogs", ignore = true)`: Bỏ qua danh sách bài viết con để tránh lỗi đệ quy lặp vô hạn.

---

### 5.3. Tầng Tiện Ích Chuẩn Hóa Chuỗi SEO (`SlugUtils.java`)

- **Vị trí**: `src/main/java/com/group/blog/util/SlugUtils.java`
- **Mã nguồn**:
  ```java
  package com.group.blog.util;

  import java.text.Normalizer;
  import java.util.regex.Pattern;

  public class SlugUtils {
      public static String generateSlug(String input) {
          if (input == null || input.isEmpty()) return "";
          String normalized = Normalizer.normalize(input.trim().toLowerCase(), Normalizer.Form.NFD);
          Pattern pattern = Pattern.compile("\\p{InCombiningDiacriticalMarks}+");
          String slug = pattern.matcher(normalized).replaceAll("");
          slug = slug.replace("đ", "d");
          slug = slug.replaceAll("[^a-z0-9\\s-]", "");
          slug = slug.replaceAll("[\\s-]+", "-");
          return slug;
      }
  }
  ```
- **Phân tích từng dòng kỹ thuật**:
  - Dòng 9: `input.trim().toLowerCase()`: Cắt khoảng trắng 2 đầu và chuyển toàn bộ sang chữ thường.
  - Dòng 9: `Normalizer.normalize(..., Normalizer.Form.NFD)`: Chuẩn hóa tách dấu tiếng Việt thành ký tự gốc và ký tự dấu tổ hợp (ví dụ chữ `"ệ"` được tách thành chữ `"e"` + dấu mũ + dấu nặng).
  - Dòng 10-11: `Pattern.compile("\\p{InCombiningDiacriticalMarks}+").matcher(normalized).replaceAll("")`: Dùng biểu thức chính quy (Regex) quét và xóa sạch tất cả các ký tự dấu tổ hợp vừa được tách ra, biến `"Lập trình"` thành `"Lap trinh"`.
  - Dòng 12: `slug.replace("đ", "d")`: Ký tự `"đ"` trong tiếng Việt không phải là dấu tổ hợp nên phải thay thế thủ công thành `"d"`.
  - Dòng 13: `slug.replaceAll("[^a-z0-9\\s-]", "")`: Loại bỏ toàn bộ các ký tự đặc biệt, dấu chấm, dấu phẩy, chỉ giữ lại chữ cái `a-z`, số `0-9`, khoảng trắng và dấu gạch nối.
  - Dòng 14: `slug.replaceAll("[\\s-]+", "-")`: Gộp nhiều khoảng trắng hoặc nhiều dấu gạch ngang liên tiếp thành duy nhất 1 dấu gạch ngang `-`.
  - **Kết quả**: `"Học Lập Trình Java & Spring Boot!"` $\rightarrow$ `"hoc-lap-trinh-java-spring-boot"`. Giúp đường dẫn bài viết thân thiện với công cụ tìm kiếm Google (Chuẩn SEO) và không bị lỗi hiển thị ký tự lạ trên thanh địa chỉ trình duyệt.

---

### 5.4. Bộ Câu Hỏi Vấn Đáp Lý Thuyết Thầy Hay Hỏi Về Service, Controller, Exception & Mapper

#### Q1: "Annotation `@Transactional` đặt ở tầng Service hoạt động như thế nào? Nếu phương thức `addComment()` lưu bình luận thành công nhưng lúc gửi `createNotification()` bị lỗi thì CSDL sẽ ra sao?"
- **Trả lời**: *"Dạ thưa Thầy, nhờ có `@Transactional`, Spring AOP sẽ bọc phương thức bằng một Transaction Proxy. Toàn bộ các câu lệnh SQL trong phương thức đều thực thi trên cùng một Connection CSDL với cờ `AutoCommit = false`. Nếu có bất kỳ ngoại lệ `RuntimeException` nào xảy ra khi gửi thông báo, Spring Proxy sẽ bắt được và gọi lệnh `Connection.rollback()`. Toàn bộ bình luận vừa thêm trước đó sẽ bị xóa bỏ, khôi phục CSDL về trạng thái nguyên vẹn, bảo đảm trọn vẹn tính chất **Atomicity (Tính nguyên tử)** của giao dịch ACID ạ!"*

#### Q2: "Tại sao nhóm em dùng `@RestController` ở các API mà lại dùng `@Controller` ở file `ViewController.java`?"
- **Trả lời**: *"Dạ thưa Thầy:
  - `@RestController` là annotation chuyên dụng cho RESTful API, tự động gắn kèm `@ResponseBody`. Mọi giá trị trả về từ phương thức (như `ApiResponse`, `BlogResponse`) đều được chuyển đổi thành chuỗi dữ liệu **JSON** để gửi về cho client.
  - Còn `@Controller` ở `ViewController.java` là Spring MVC Controller truyền thống. Chuỗi trả về là **tên của View Template** (ví dụ `"public/home-page"`). Cỗ máy Thymeleaf ViewResolver sẽ đón chuỗi này để nạp file HTML tương ứng từ thư mục `templates/` nạp lên màn hình trình duyệt ạ!"*

#### Q3: "Tại sao nhóm lại dùng MapStruct mà không dùng thư viện ModelMapper hoặc tự viết các hàm getter/setter thủ công?"
- **Trả lời**: *"Dạ thưa Thầy:
  - Nếu viết getter/setter thủ công cho hàng chục class DTO và Entity thì code sẽ rất dài dòng, dễ nhầm lẫn và tốn thời gian bảo trì.
  - Nếu dùng thư viện `ModelMapper`, ModelMapper sử dụng Java Reflection trong thời gian chạy (Runtime) để quét các thuộc tính, tốc độ xử lý rất chậm và nếu có sai lệch tên trường thì chỉ phát hiện được khi ứng dụng đang chạy thật.
  - Nhóm em chọn **MapStruct** vì MapStruct sinh code Java thuần tại **thời điểm biên dịch (Compile-time)**. Tốc độ chạy nhanh ngang bằng code tay, hoàn toàn Type-safe và nếu có lỗi ánh xạ sai kiểu dữ liệu thì trình biên dịch `javac` sẽ báo lỗi ngay lập tức, không để lọt lỗi ra môi trường Production ạ!"*

#### Q4: "Cơ chế bắt lỗi tập trung `@ControllerAdvice` và `@ExceptionHandler` giải quyết được vấn đề gì so với việc dùng khối `try-catch` ở từng Controller?"
- **Trả lời**: *"Dạ thưa Thầy:
  - Nếu dùng `try-catch` ở từng phương thức Controller, mã nguồn sẽ bị trùng lặp rất nhiều và các Controller bị bẩn code bởi logic xử lý lỗi.
  - Nhờ có `@ControllerAdvice`, toàn bộ ngoại lệ trong hệ thống đều được dồn về một đầu mối duy nhất là `GlobalExceptionHandler`.
  - Giúp chuẩn hóa cấu trúc phản hồi lỗi: Mọi lỗi trả về cho Frontend đều có định dạng JSON đồng nhất (`code`, `message`).
  - Đóng vai trò là bức tường lửa bảo mật: Bắt chặn các lỗi không mong muốn để không bao giờ lộ vết lỗi Stacktrace hay cấu trúc thư mục máy chủ ra ngoài Client ạ!"*

---

---

## Mục 6: Tầng Giao Diện & Frontend JavaScript Giao Tiếp API

### 6.1. Kiến Trúc Frontend: Phân Biệt MPA vs SPA & Bản Chất Dự Án

- **Bản chất kiến trúc cấu trúc (Structural Architecture)**: 
  - Dự án này là **MPA (Multi-Page Application - Ứng dụng Đa Trang)** xây dựng trên nền tảng **HTML5, CSS3 (Bootstrap 5.3.3) và JavaScript ES6+ (kết hợp jQuery 3.7.1)**.
  - Minh chứng: Dự án có hơn 20 file HTML riêng biệt trong thư mục `templates/`, được điều hướng đường dẫn URL độc lập thông qua `ViewController.java` của Spring Boot (ví dụ: `/home` $\rightarrow$ `home-page.html`, `/post` $\rightarrow$ `post.html`, `/login` $\rightarrow$ `login.html`, `/admin/dashboard` $\rightarrow$ `dashboard.html`).
- **Bản chất cơ chế tương tác (Interaction & Rendering)**:
  - Dự án mang **"Trải nghiệm phong cách SPA" (SPA-like Experience)** thông qua **Client-Side Rendering (CSR)** và **Dynamic Component Loading**:
    1. **Không reload (F5) toàn bộ trang**: Mọi thao tác người dùng (Thả tim Like, Bookmark, Gửi bình luận, Tìm kiếm từ khóa, Lọc chuyên mục/thẻ tag, Đăng nhập, Đổi mật khẩu) đều được gửi ngầm qua **AJAX / Fetch API** lên các Endpoint REST API (`/api/...`). JavaScript nhận dữ liệu JSON phản hồi về và trực tiếp cập nhật lên DOM mà không làm chớp hay tải lại trang web.
    2. **Cơ chế Virtual Section Navigation trong `home-page.html`**: Trong trang chủ tích hợp sẵn 3 khối giao diện: `#p-home` (Trang chủ), `#p-categories` (Toàn bộ danh mục) và `#p-tags` (Toàn bộ thẻ tag). Hàm `navigate(page)` trong `nav.js` chỉ ẩn khối này và hiện khối kia (`.hide()` / `.show()`) kết hợp đồng bộ URL bằng `window.history.pushState()`. Người dùng cảm thấy mượt mà y hệt như đang dùng ứng dụng Single Page App của React hay Vue.
    3. **Tách nhỏ thành các Mảnh ghép (Fragments/Components)**: Thay vì lặp lại code của Header, Navbar, Footer ở từng trang, hệ thống dùng kỹ thuật nạp ngầm HTML Component bằng AJAX: `$('#navbar-container').load('/fragments/navbar.html')`.

---

### 6.2. Bóc Tách Chi Tiết Toàn Bộ 21 File Giao Diện HTML (`templates/`)

#### 6.2.1. Nhóm Trang Người Dùng Công Khai (`templates/public/` - 11 Files)

1. **`home-page.html` (Trang chủ chính)**:
   - *Cấu trúc*: Chứa các container rỗng chờ nạp `#navbar-container`, `#hero-container`, `#footer-container`. Phần thân gồm 2 cột: Cột trái (Toolbar sắp xếp Newest/Oldest, danh sách bài viết `#post-list`) và Cột phải (Sidebar chủ đề và Trending).
   - *Tính năng SPA*: Chứa sẵn 2 khối ẩn `#p-categories` và `#p-tags`. Khi người dùng bấm chuyển xem danh mục/thẻ, JS kích hoạt hiển thị mà không rời khỏi trang.
2. **`post.html` (Trang đọc chi tiết bài viết)**:
   - Đọc tham số `?id=...` hoặc `slug` trên URL.
   - Gửi request `GET /blogs/{id}` để lấy chi tiết bài viết.
   - Render nội dung bài viết từ JSON của Editor.js ra HTML hiển thị.
   - Render danh sách bình luận lồng nhau đa cấp (Nested Comments) với nút "Reply", "Like", "Bookmark".
   - Tích hợp form gửi bình luận mới (gọi `POST /interactions/comments`).
3. **`blog-editor.html` (Trang soạn thảo bài viết của Tác giả)**:
   - Tích hợp bộ công cụ soạn thảo hiện đại **Editor.js** (Header, Paragraph, List, Checklist, Code, Quote, Image).
   - Tích hợp ô upload ảnh bìa (Banner/Thumbnail) trực tiếp lên Cloudinary.
   - Hỗ trợ 2 chế độ lưu:
     - Nút **"Save Draft"**: Ghi nháp bài viết (`draft = true`), không hiển thị ra ngoài trang chủ.
     - Nút **"Publish"**: Xuất bản bài viết gửi lên Admin duyệt hoặc hiển thị ngay (`draft = false`).
4. **`login.html` (Trang đăng nhập)**:
   - Form nhập Username và Password.
   - JS chặn submit mặc định, gọi API `POST /auth/token`.
   - Nhận chuỗi JWT token, lưu vào `localStorage.setItem('token', token)` và `localStorage.setItem('username', username)`.
   - Tự động chuyển hướng về trang trước đó hoặc trang chủ `/`.
5. **`register.html` (Trang đăng ký tài khoản)**:
   - Form nhập thông tin: Username, Email, Password, Confirm Password.
   - Validate phía Client: Username $\ge 3$ ký tự, Password $\ge 6$ ký tự, 2 ô mật khẩu phải trùng nhau.
   - Gọi API `POST /users`. Sau khi đăng ký thành công, hàm `autoLogin()` tự động đăng nhập ngầm để lấy Token và đưa người dùng vào hệ thống ngay lập tức mà không bắt đăng nhập lại.
6. **`forgot-password.html` (Trang khôi phục mật khẩu)**:
   - Giao diện nhập Email xác minh để nhận hướng dẫn cấp lại mật khẩu.
7. **`user-profile.html` (Trang hồ sơ công khai của Tác giả)**:
   - Hiển thị Avatar, Tên tác giả, Tiểu sử (Bio), Ngày tham gia.
   - Thống kê: Tổng số người theo dõi (Followers), Tổng số người đang theo dõi (Following), Tổng số bài viết đã xuất bản.
   - Nút **"Follow / Unfollow"**: Gọi API `POST /follows/{targetUserId}` để theo dõi hoặc hủy theo dõi tác giả.
   - Danh sách bài viết do tác giả đó sáng tác.
8. **`edit-profile.html` (Trang chỉnh sửa thông tin cá nhân)**:
   - Cho phép người dùng cập nhật Bio, Email và upload Avatar đại diện mới lên đám mây Cloudinary.
9. **`change-password.html` (Trang đổi mật khẩu)**:
   - Form nhập: Mật khẩu cũ, Mật khẩu mới, Xác nhận mật khẩu mới.
   - Gọi API `PUT /users/change-password` có đính kèm Token xác thực.
10. **`Manage-Blogs.html` (Trang quản lý bài viết cá nhân)**:
    - Bảng danh sách các bài viết do chính tài khoản hiện tại tạo ra.
    - Hiển thị trạng thái bài viết: *Bản nháp (Draft)*, *Đang chờ duyệt (Pending)*, *Đã xuất bản (Published)*, *Bị từ chối (Rejected)*.
    - Nút chức năng: Xem bài, Chỉnh sửa (mở lại Editor), Xóa bài (gọi `DELETE /blogs/{id}`).
11. **`saved-blogs.html` (Trang bài viết đã lưu - Bookmarks)**:
    - Gọi API `GET /interactions/bookmarks/my-bookmarks` để lấy danh sách bài viết người dùng đã lưu lại để đọc sau.
12. **`notifications.html` (Trang thông báo cá nhân)**:
    - Hiển thị danh sách thông báo lịch sử: Có người thả tim bài viết, có người bình luận, có người bắt đầu theo dõi bạn.
    - Nút đánh dấu đã đọc hoặc xóa thông báo.

---

#### 6.2.2. Nhóm Trang Quản Trị Hệ Thống (`templates/admin/` - 4 Files)

1. **`dashboard.html` (Bảng điều khiển tổng quan Admin)**:
   - Khi tải trang, JS gửi `GET /api/admin/stats` (kèm Header `Authorization: Bearer <token>`).
   - Hiển thị các khối Widget thống kê: Tổng số thành viên (`totalUsers`), Tổng số bài viết (`totalBlogs`), Tổng lượt xem (`totalViews`), Tổng lượt tương tác (`totalLikes`, `totalComments`).
2. **`posts.html` (Quản lý kiểm duyệt bài viết)**:
   - Bảng hiển thị toàn bộ bài viết trên toàn hệ thống kèm tên tác giả và ngày gửi.
   - Nút hành động: **Phê duyệt bài viết (Approve)**, **Từ chối xuất bản (Reject)** hoặc **Xóa bài vi phạm (Delete)**.
3. **`users.html` (Quản lý tài khoản người dùng)**:
   - Bảng danh sách toàn bộ người dùng trong hệ thống.
   - Quản lý phân quyền: Thăng cấp thành viên thành `ROLE_ADMIN` hoặc hạ cấp về `ROLE_USER`.
   - Khóa/mở khóa tài khoản người dùng vi phạm tiêu chuẩn cộng đồng.
4. **`categories-tags.html` (Quản trị Danh mục & Thẻ từ khóa)**:
   - Form thêm mới Danh mục (Tên danh mục, mô tả).
   - Form thêm mới Thẻ Tag.
   - Chức năng sửa/xóa các danh mục và thẻ tag cũ.

---

#### 6.2.3. Nhóm Mảnh Ghép Giao Diện Tái Sử Dụng (`templates/fragments/` - 6 Files)

1. **`navbar.html` (Thanh điều hướng đầu trang)**:
   - Logo thương hiệu `Bleb`.
   - Ô tìm kiếm bài viết nhanh bằng từ khóa.
   - Các nút điều hướng: *Home*, *Categories*, *Tags*, *Write (Viết bài)*.
   - Chuông thông báo hiển thị số lượng thông báo mới chưa đọc.
   - Logic chuyển đổi trạng thái (Auth State):
     - Nếu chưa đăng nhập: Hiện nút **Sign In** và **Sign Up**.
     - Nếu đã đăng nhập: Ẩn nút đăng nhập, hiển thị Avatar đại diện và menu Dropdown (Trang cá nhân, Quản lý bài viết, Đổi mật khẩu, Đăng xuất).
     - Nếu tài khoản có quyền `ADMIN`: Tự động hiện thêm nút **"Admin Dashboard"**.
2. **`hero.html` (Banner mở đầu trang chủ)**:
   - Khối chào đón độc giả với khẩu hiệu truyền cảm hứng, giới thiệu nền tảng viết blog.
3. **`footer.html` (Chân trang)**:
   - Thông tin bản quyền, các liên kết điều hướng nhanh và liên kết mạng xã hội.
4. **`sidebar.html` (Cột thông tin bên phải trang chủ)**:
   - Widget **"Stories from all interests"**: Danh sách các chủ đề danh mục dạng viên thuốc (Pill badges).
   - Widget **"Trending Now"**: Top các bài viết có lượt xem và lượt like cao nhất.
5. **`admin_sidebar.html`**: Menu điều hướng bên trái dành riêng cho trang quản trị Admin.
6. **`dashboard-sidebar.html`**: Menu điều hướng thanh bên cho trang quản lý cá nhân của User.

---

### 6.3. Bóc Tách Chi Tiết Toàn Bộ 8 File JavaScript Cốt Lõi (`static/assets/js/`)

#### 6.3.1. `app.js` — Quản Lý State Toàn Cục & Xử Lý Dữ Liệu Editor.js

- **Đối tượng State toàn cục `var S`**:
  ```javascript
  var S = {
      page: 'home',          // Trang/tab hiện tại (home, categories, tags)
      cat: null,             // ID danh mục đang chọn để lọc
      tag: null,             // ID thẻ tag đang chọn để lọc
      keyword: null,         // Từ khóa tìm kiếm đang nhập
      sort: 'createdAt,desc',// Quy tắc sắp xếp bài viết
      get isAuth() { return localStorage.getItem('token') !== null; },
      get uname()  { return localStorage.getItem('username') || 'Guest'; }
  };
  ```
  - Quản lý trạng thái chia sẻ giữa tất cả các file JS. Bất kỳ thao tác chọn danh mục ở Sidebar hay gõ từ khóa ở Navbar đều cập nhật vào biến `S` này.
- **Hàm `excerpt(s, n)`**:
  - Bài viết được lưu trong MySQL dưới dạng chuỗi JSON khối của Editor.js (ví dụ: `{"blocks":[{"type":"paragraph","data":{"text":"Xin chào..."}}]}`).
  - Hàm này dùng `JSON.parse(s)` bóc tách các block paragraph, loại bỏ thẻ HTML bằng Regex `replace(/<[^>]*>/g, '')` và cắt lấy $n$ ký tự đầu tiên để làm mô tả ngắn hiển thị ở trang chủ.
- **Hàm `callApi(url, method, data)`**:
  - Là hàm bọc (wrapper) phương thức `$.ajax()` của jQuery.
  - Tự động kiểm tra nếu có `token` trong `localStorage`, nó sẽ tự động chèn Header bảo mật:
    `headers: { 'Authorization': 'Bearer ' + token }`.
  - Nhờ vậy, tất cả các file JS khác khi gọi API không cần phải viết lại logic đính kèm Token JWT.
- **Hàm `toast(msg)`**: Tạo popup thông báo nhỏ màu tối ở góc màn hình báo thành công hoặc lỗi cho người dùng.

---

#### 6.3.2. `auth.js` — Xác Thực Đăng Nhập, Đăng Ký, Đăng Xuất & LocalStorage

- **Hàm `renderAuth()`**:
  - Kiểm tra `localStorage.getItem('token')`.
  - Nếu có token: Xóa nút "Sign In/Sign Up", chèn Avatar đại diện (dùng hàm `initials()` lấy chữ cái đầu của tên), gắn sự kiện click mở Dropdown menu người dùng.
  - Gắn sự kiện cho nút **"Log Out"**: Gọi hàm `handleLogout()`.
- **Hàm `handleLogout()`**:
  - Xóa token khỏi bộ nhớ trình duyệt: `localStorage.removeItem('token')` và `localStorage.removeItem('username')`.
  - Chuyển hướng người dùng về trang chủ hoặc reload lại giao diện về trạng thái Khách vãng lai (`Guest`).

---

#### 6.3.3. `posts.js` — Gọi API Blogs & Render Card Bài Viết Bằng DOM Manipulation

- **Hàm `renderPosts()`**:
  - Xây dựng URL truy vấn dựa trên State `S`:
    `let url = '/blogs?sort=' + S.sort;`
    Nếu có lọc chuyên mục: thêm `&category=` + `S.cat`.
    Nếu có từ khóa tìm kiếm: thêm `&keyword=` + `S.keyword`.
  - Gửi request `callApi(url, 'GET')`.
  - Làm trống danh sách `#post-list` (`$('#post-list').empty()`).
  - Lặp qua mảng bài viết nhận được (`res.result`), gọi hàm `buildCard(p)` để tạo thành phần HTML tương ứng rồi chèn vào trang (`$container.append(card)`).
- **Hàm `buildCard(p)`**:
  - Tạo cấu trúc HTML thẻ bài viết gồm: Ảnh đại diện tác giả, Tên tác giả, Ngày đăng, Tiêu đề bài viết, Đoạn trích mô tả (`excerpt`), Thời gian đọc ước tính (tính theo công thức số từ $/ 200$), Danh sách thẻ Tag, và Ảnh bìa Banner.
  - Tạo các nút tương tác:
    - **Nút Thả tim (Like)**: Hiển thị icon trái tim và số lượng like.
    - **Nút Lưu (Bookmark)**: Hiển thị icon bookmark.
  - Bắt sự kiện click vào nút Like $\rightarrow$ Gọi hàm `toggleLike(p.id)`.
  - Bắt sự kiện click vào nút Bookmark $\rightarrow$ Gọi hàm `toggleBookmark(p.id)`.
- **Hàm `toggleLike(blogId)`**:
  - Gửi request `POST /interactions/likes/{blogId}`.
  - Không hề tải lại trang: Trực tiếp đổi màu icon trái tim (đỏ/xám) và cộng/trừ số lượng like trên màn hình ngay lập tức (Optimistic UI Update).

---

#### 6.3.4. `filters.js` — Bộ Lọc Đa Tầng, Lọc Kép & Đồng Bộ Query URL

- **Hàm `fetchAndRenderFilters()`**:
  - Gọi đồng thời `GET /categories` và `GET /tags`.
  - Tính tổng số bài viết của toàn hệ thống bằng cách cộng dồn `postCount` của từng danh mục.
  - Gọi hàm `renderCatTabs()` để vẽ thanh menu chọn danh mục nằm ngang dưới dạng các Tab.
- **Hàm `updateUrlWithFilters()`**:
  - Sử dụng đối tượng `URLSearchParams` để tạo chuỗi truy vấn chuẩn SEO: `?cat=UUID&q=tu-khoa`.
  - Dùng `window.history.pushState({}, '', newUrl)` để thay đổi URL hiển thị trên thanh địa chỉ trình duyệt mà **hoàn toàn không làm reload trang web**.
  - Nhờ tính năng này, người dùng có thể copy đường link chia sẻ cho bạn bè, khi bạn bè mở link ra thì trang web vẫn tự lọc đúng bài viết theo danh mục đó!

---

#### 6.3.5. `nav.js` — SPA Navigation, Mổ Payload Token JWT Check Role Admin & Chuông Thông Báo

- **Hàm `navigate(page)` (Linh hồn SPA của trang chủ)**:
  ```javascript
  function navigate(page) {
      S.page = page;
      $('#p-home, #p-categories, #p-tags').hide(); // Ẩn tất cả các view
      $('#p-' + page).show();                      // Chỉ hiện view được chọn
      $('[data-page]').removeClass('is-active');
      $('[data-page="' + page + '"]').addClass('is-active');
      window.scrollTo({ top: 0, behavior: 'smooth' });
  }
  ```
  - Thay vì chuyển trang vật lý, hàm này hoán đổi hiển thị giữa Trang chủ, Danh mục và Thẻ tag trong chớp mắt.
- **Hàm `updateNavAuth()` — Mổ Token JWT để Phân quyền Admin**:
  ```javascript
  const token = localStorage.getItem('token');
  if (token) {
      // Tách lấy phần Payload ở vị trí index 1: header.payload.signature
      const base64Url = token.split('.')[1];
      const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
      const payload = JSON.parse(decodeURIComponent(window.atob(base64)...));
      
      // Kiểm tra chuỗi scope (Spring Security cấp quyền)
      const roles = payload.scope || payload.roles || "";
      if (roles.includes("ADMIN")) {
          $('#btn-desk-admin').show(); // Hiện nút vào Admin Dashboard
      } else {
          $('#btn-desk-admin').hide(); // Người dùng thường thì giấu đi
      }
  }
  ```
  - Giải thích cho Thầy: Phía Frontend chủ động giải mã Payload của JWT để quyết định hiển thị các nút chức năng quản trị, giúp trải nghiệm giao diện thông minh và nhanh chóng. Tuy nhiên, tính bảo mật thực sự vẫn được chốt chặn nghiêm ngặt ở tầng Spring Security của Backend.
- **Xử lý Chuông thông báo (Notifications)**:
  - Gọi `GET /notifications` định kỳ để đếm số thông báo mới.
  - Hiển thị chấm đỏ thông báo và danh sách các thông báo tương tác (Like, Comment, Follow).

---

#### 6.3.6. `pages.js` — Render Danh Mục & Thẻ Tag Với Mảng Màu Xoay Vòng

- **Mảng màu `CAT_COLORS_ARRAY`**:
  - Chứa bảng màu hiện đại gồm các cặp màu sắc thẩm mỹ: Purple, Teal, Gold, Amber, Rose.
- **Hàm `buildCatPage()`**:
  - Lặp qua danh sách Category từ Backend: `var col = CAT_COLORS_ARRAY[index % CAT_COLORS_ARRAY.length];`
  - Gán màu xoay vòng cho từng thẻ Card danh mục (background, viền border, màu chữ) để giao diện luôn đa dạng, sinh động mà không bị đơn điệu.
  - Bấm vào một danh mục $\rightarrow$ Lưu `S.cat = c.id`, tự động gọi `navigate('home')` và kích hoạt `renderPosts()` để lọc ra các bài viết thuộc chủ đề đó.

---

#### 6.3.7. `sidebar.js` — Widget Trending & Category Pill

- **Hàm `renderSbCategories()`**:
  - Vẽ danh sách các chủ đề ở cột bên phải.
  - Bấm vào Category Pill ở Sidebar sẽ toggle lọc bài viết (bấm lần 1: lọc, bấm lần 2: hủy lọc).
- **Hàm `renderSbTrending()`**:
  - Gọi API lấy danh sách các bài viết có lượt xem cao nhất.
  - Hiển thị số thứ tự nổi bật `01`, `02`, `03`... kèm tiêu đề bài viết và tên tác giả.

---

#### 6.3.8. `init.js` — Điểm Khởi Đầu Khởi Chạy Trang Web

- Đóng vai trò là file "nhạc trưởng" (Entry Point) của Frontend:
  - Được bọc trong sự kiện `$(document).ready(function() { ... })`.
  - Bước 1: Quét URL hiện tại xem người dùng có truyền tham số `?cat=...` hoặc `?q=...` từ link chia sẻ hay không. Nếu có, nạp ngay vào `S.cat` và `S.keyword`.
  - Bước 2: Kích hoạt `fetchAndRenderFilters()` để nạp bộ lọc.
  - Bước 3: Kích hoạt `renderPosts()` để tải bài viết.
  - Bước 4: Kích hoạt `renderSbCategories()` và `renderSbTrending()` để tải dữ liệu thanh bên phải.

---

### 6.4. Các Thư Viện Frontend Bổ Trợ & Kỹ Thuật CSS Nâng Cao

1. **Bộ soạn thảo khối Editor.js (Block-style Editor)**:
   - Khác với các bộ soạn thảo lỗi thời sinh mã HTML thô dễ dính lỗi bảo mật XSS (như CKEditor/TinyMCE), Editor.js quản lý nội dung dưới dạng **khối dữ liệu JSON sạch** (Clean Data JSON).
   - Mỗi thành phần (Tiêu đề H1, Đoạn văn, Khối code, Ảnh) là một JSON object độc lập, giúp hệ thống dễ dàng phân tích, trích xuất text tóm tắt và hiển thị an toàn trên cả Web lẫn Mobile App.
2. **Tích hợp Lưu trữ Đám mây Cloudinary API**:
   - Khi người dùng chọn ảnh bìa bài viết hoặc đổi Avatar cá nhân, mã JavaScript gọi trực tiếp API Upload của **Cloudinary**.
   - Cloudinary trả về đường link ảnh an toàn định dạng HTTPS đã tối ưu hóa nén ảnh. Backend chỉ việc lưu đường dẫn chuỗi String này vào CSDL, không tốn dung lượng ổ cứng của server Spring Boot.
3. **Thiết kế Hệ màu CSS Custom Properties (`main.css`)**:
   - Định nghĩa bảng biến màu chuẩn: `--bg: #0b0f17`, `--card: #151a22`, `--purple: #7c6ff7`, `--teal: #3ecfb8`, `--gold: #e9a84c`.
   - Kết hợp Typography từ Google Fonts: **Playfair Display** (dành cho tiêu đề bài viết sang trọng), **Inter** (nội dung dễ đọc) và **JetBrains Mono** (cho các đoạn mã code).

---

### 6.5. Bộ 5 Câu Hỏi Vấn Đáp Chuyên Sâu Về Frontend & Kịch Bản Ghi Điểm 10

#### Q1: "Tại sao nhóm em có dùng Thymeleaf nhưng lại không dùng các cú pháp Server-Side Rendering như `th:text`, `th:each` mà lại dùng JavaScript gọi REST API?"

- **🎯 Trả lời chuẩn**:
  *"Dạ thưa Thầy:
  1. Thymeleaf trong dự án của nhóm em đóng vai trò là **Template Resolver** để trả về các khung vỏ HTML tĩnh và hỗ trợ phân trang routing qua `ViewController`.
  2. Nhóm em chủ động lựa chọn kiến trúc **Client-Side Rendering (CSR)** qua REST API thay vì SSR truyền thống để **tách biệt hoàn toàn tầng Giao diện (Frontend) và tầng Dữ liệu (Backend)**.
  3. Lợi ích lớn nhất: Trải nghiệm người dùng cực kỳ mượt mà. Khi người dùng bấm Thả tim, Đổi bộ lọc, hoặc Viết bình luận, dữ liệu được cập nhật tức thì qua AJAX mà **không phải tải lại toàn bộ trang web (No Page Reload)**, giúp tiết kiệm băng thông máy chủ và sẵn sàng mở rộng sang ứng dụng di động Mobile App sau này ạ!"*

#### Q2: "Dự án có nhiều file HTML như `home-page.html`, `post.html`, `login.html` thì tại sao lại có người gọi là SPA?"

- **🎯 Trả lời chuẩn**:
  *"Dạ thưa Thầy, nếu xét thuần túy về cấu trúc tệp tin thì đây là **MPA (Multi-Page Application)**. Tuy nhiên, hệ thống của nhóm em mang **'Trải nghiệm phong cách SPA' (SPA-like Experience)** bởi 2 lý do kỹ thuật:
  - Thứ nhất, trong chính trang `home-page.html`, nhóm em tích hợp sẵn 3 View ảo (`#p-home`, `#p-categories`, `#p-tags`) và dùng hàm `navigate()` trong `nav.js` để ẩn hiện các Section kết hợp `window.history.pushState()` mà không hề tải lại trang.
  - Thứ hai, toàn bộ tương tác lấy dữ liệu, phân trang và đăng nhập đều dùng REST API và lưu trữ Token trong `localStorage`, người dùng không hề bị chớp màn hình khi thao tác ạ!"*

#### Q3: "Lưu Token JWT ở `localStorage` có nguy cơ bảo mật gì so với `HttpOnly Cookie`?"

- **🎯 Trả lời chuẩn**:
  *"Dạ thưa Thầy:
  - **Nguy cơ**: `localStorage` có thể bị truy cập bởi mã JavaScript chạy trên trình duyệt, do đó nếu trang web bị lỗ hổng **XSS (Cross-Site Scripting)**, hacker có thể chèn mã độc để đánh cắp Token.
  - **Biện pháp phòng ngừa của nhóm**: Nhóm em sử dụng bộ soạn thảo **Editor.js** lưu dữ liệu dạng JSON thuần và mã hóa thực thể HTML khi hiển thị, loại bỏ hoàn toàn nguy cơ chèn script độc hại XSS.
  - **So sánh**: Dùng `localStorage` giúp việc lập trình Client-Side REST API và gửi Header `Authorization: Bearer` cực kỳ linh hoạt, không bị dính lỗi xung đột tên miền chéo CORS và miễn nhiễm hoàn toàn với tấn công **CSRF (Cross-Site Request Forgery)** ạ!"*

#### Q4: "Làm sao trang web biết được ai đang đăng nhập để hiển thị Tên và Avatar lên thanh Menu?"

- **🎯 Trả lời chuẩn**:
  *"Dạ thưa Thầy, quy trình diễn ra như sau:
  1. Khi người dùng đăng nhập thành công ở `login.html`, Backend trả về Token JWT và thông tin tài khoản. JavaScript lưu vào `localStorage.setItem('username', data.username)`.
  2. Khi trang web tải xong, hàm `updateNavAuth()` trong `nav.js` đọc `localStorage`. Nếu thấy tồn tại Token, nó sẽ ẩn vùng khách vãng lai (`.nav-guest`), hiện vùng thành viên (`.nav-user`), lấy username chèn vào thẻ `#nav-username` và dùng hàm `initials()` lấy chữ cái đầu của tên hiển thị lên khung Avatar tròn ạ."*

#### Q5: "Nếu người dùng tự ý vào Console trình duyệt sửa chữ trong Token JWT để giả mạo thành Admin thì có hack được hệ thống không?"

- **🎯 Trả lời chuẩn**:
  *"Dạ thưa Thầy, **tuyệt đối không thể hack được** ạ!
  - Ở Frontend: Người dùng có thể sửa chuỗi Base64 ở client để nút 'Admin Dashboard' hiện ra trên giao diện.
  - Nhưng khi người dùng bấm vào và JavaScript gửi request lên API Backend `/api/admin/stats`, Spring Security ở máy chủ sẽ dùng chữ ký bí mật `SIGNER_KEY` để giải mã và kiểm tra Chữ ký điện tử (Signature) của Token.
  - Do người dùng không biết mã bí mật của Server, chữ ký sẽ không khớp (Invalid Signature). Spring Security sẽ lập tức chặn đứng request và trả về lỗi **HTTP 401 Unauthorized / 403 Forbidden**. Vì vậy hệ thống an toàn 100% ạ!"*

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
