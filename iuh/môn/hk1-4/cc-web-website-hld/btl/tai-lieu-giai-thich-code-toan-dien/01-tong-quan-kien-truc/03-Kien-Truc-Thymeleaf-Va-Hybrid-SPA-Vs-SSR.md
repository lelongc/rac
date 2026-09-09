# BẢN CHẤT THYMELEAF TRONG DỰ ÁN: KIẾN TRÚC HYBRID VIEW RESOLVER & CSR RESTFUL API

> **Vị trí file cấu hình liên quan:**  
> - `pom.xml` (Khai báo `spring-boot-starter-thymeleaf` và `thymeleaf-extras-springsecurity6`)  
> - `src/main/java/com/group/blog/controller/ViewController.java`  
> - `src/main/resources/templates/`  
> **Mục đích:** Giải thích tường tận câu hỏi sống còn khi bảo vệ đồ án: **"Thymeleaf làm nhiệm vụ gì trong dự án này? Tại sao có dependency Thymeleaf nhưng trong HTML lại không dùng các cú pháp `th:each`, `th:text` mà lại dùng AJAX gọi REST API?"**

---

## 1. Thymeleaf Có Được Sử Dụng Trong Dự Án Không?

**CÂU TRẢ LỜI CHÍNH XÁC 100%: CÓ!**  
Thymeleaf hiện diện rõ ràng và đảm nhận một vai trò vô cùng thiết yếu trong hệ thống:

```xml
<!-- Trích dẫn từ file pom.xml dòng 55-57 và 70-72 -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>
<dependency>
    <groupId>org.thymeleaf.extras</groupId>
    <artifactId>thymeleaf-extras-springsecurity6</artifactId>
</dependency>
```

Và tầng điều hướng giao diện `ViewController.java`:
```java
@Controller
public class ViewController {
    @GetMapping({"/", "/home", "/home-page.html"})
    public String homePage() {
        return "public/home-page"; // Thymeleaf View Resolver phân giải thành templates/public/home-page.html
    }

    @GetMapping({"/admin", "/admin/dashboard"})
    public String adminDashboardPage() {
        return "admin/dashboard";  // Thymeleaf View Resolver phân giải thành templates/admin/dashboard.html
    }
}
```

---

## 2. Bản Chất Vai Trò Của Thymeleaf Trong Dự Án Này

Trong Spring Boot, thư mục `src/main/resources/templates/` là một **vùng thư mục bảo vệ nội bộ** (Internal Protected Resources). Trình duyệt của người dùng **không thể** truy cập trực tiếp bằng đường dẫn URL như thư mục `static/`.

Để một yêu cầu `GET /` hoặc `GET /admin/dashboard` có thể nạp được file HTML từ thư mục `templates/`, Spring Boot bắt buộc phải cần đến một **View Engine Resolver**.  
Khi khai báo `spring-boot-starter-thymeleaf`, Spring Boot tự động kích hoạt bộ phận `ThymeleafViewResolver` với cơ chế:
- **Tiền tố (Prefix)**: `classpath:/templates/`
- **Hậu tố (Suffix)**: `.html`

Khi `ViewController` trả về chuỗi `"public/home-page"`, chính Thymeleaf là công cụ tiếp nhận chuỗi này, định vị file `classpath:/templates/public/home-page.html`, nén luồng và truyền về cho trình duyệt của người dùng!

---

## 3. Tại Sao Trong HTML Không Dùng Cú Pháp `th:each`, `th:text` Kiểu Cũ?

Đây là câu hỏi phân loại sinh viên giỏi của giảng viên IUH!

### 3.1. Mô hình Thymeleaf SSR Truyền Thống (Server-Side Rendering)
Ở các đồ án cũ hoặc cách dạy truyền thống:
1. Người dùng gửi request lên Controller.
2. Controller gọi Service lấy danh sách bài viết từ CSDL.
3. Controller nhét danh sách vào Model: `model.addAttribute("blogs", blogs)`.
4. Thymeleaf tại Server duyệt vòng lặp:
   ```html
   <!-- Kiểu truyền thống SSR -->
   <div th:each="b : ${blogs}">
       <h3 th:text="${b.title}">Tiêu đề</h3>
   </div>
   ```
5. Server render xong toàn bộ chuỗi HTML khổng lồ rồi mới trả về trình duyệt.

**Hạn chế chết người của cách này:**
- **Không dùng được Token JWT trong `localStorage`**: Vì JWT được lưu ở trình duyệt của máy khách (Client), Server lúc render trang đầu tiên **hoàn toàn không biết** người dùng này đã đăng nhập hay chưa để mà hiển thị nút Like, Bookmark hay nút Admin!
- **Tải lại toàn trang (Full Page Reload)**: Mỗi lần bấm Thích (Like), đổi trang (Pagination), hoặc gõ tìm kiếm, trang web phải load lại từ đầu, giật lag, tiêu tốn băng thông máy chủ.

---

### 3.2. Mô hình Đỉnh Cao: Hybrid Client-Side Rendering (CSR) + RESTful API (Dự án đang dùng)

Nhóm đã lựa chọn kiến trúc theo **chuẩn công nghiệp hiện đại (giống mô hình Next.js / Nuxt.js)**:

```
[1. Người dùng mở trang] ──> GET / ──> [Thymeleaf View Resolver]
                                               │
                                               ▼
                              Trả về khung giao diện HTML Skeleton
                                               │
                                               ▼
[2. Trình duyệt tải xong HTML] ──> Kích hoạt JavaScript (app.js, posts.js)
                                               │
                                               ▼
[3. JavaScript đọc Token] ───────> Lấy JWT từ localStorage (biết ngay User là ai)
                                               │
                                               ▼
[4. Gửi AJAX ngầm] ──────────────> GET /blogs (Kèm Header Authorization: Bearer ...)
                                               │
                                               ▼
[5. Spring Boot REST API] ───────> Trả về JSON sạch sẽ
                                               │
                                               ▼
[6. DOM Manipulation] ───────────> JavaScript vẽ danh sách bài viết mượt mà (0ms reload)
```

---

## 4. Bảng So Sánh Chiến Lược Giữa 2 Cách Tiếp Cận

| Tiêu Chí So Sánh | Thymeleaf SSR Cổ Điển | Kiến Trúc Hybrid Của Nhóm (Thymeleaf + REST API) |
| :--- | :--- | :--- |
| **Xác thực & Bảo mật** | Dùng Session / Cookie cồng kềnh, dễ bị tấn công CSRF. | Dùng **JWT Token Stateless** hiện đại, an toàn tuyệt đối. |
| **Trải nghiệm người dùng** | Giật lag vì mỗi lần lọc hay bấm like đều phải F5 tải lại trang. | **Siêu mượt (SPA-like)**: Thả tim, bookmark, lọc thẻ tức thì không reload trang. |
| **Tính độc lập của hệ thống** | Giao diện dính chặt vào Backend Java, không tách rời được. | **Chuẩn REST API**: Cùng 1 hệ thống API này, sau này có thể viết thêm App Mobile (Flutter / React Native) mà không cần sửa 1 dòng code backend nào. |
| **Vai trò của Thymeleaf** | Đảm nhận cả render giao diện lẫn đổ dữ liệu. | Đảm nhận **View Routing an toàn** từ thư mục bảo vệ `templates/`. |

---

## 5. Cẩm Nang Trả Lời Vấn Đáp Giảng Viên Điểm 10 Về Thymeleaf

### ❓ Câu hỏi của Giảng viên: *"Thầy/cô thấy trong pom.xml có thymeleaf, nhưng trong code HTML thầy/cô không thấy `th:text`, `th:each`. Vậy Thymeleaf trong dự án của em dùng để làm gì?"*

> 🎙️ **Câu trả lời chuẩn mẫu 10/10:**  
> *"Dạ thưa thầy/cô! Nhóm em đã tìm hiểu rất kỹ về kiến trúc phần mềm và quyết định áp dụng mô hình **Hybrid Single-Page Architecture** chuẩn công nghiệp:  
> 1. **Thymeleaf** trong dự án đóng vai trò là **Template View Resolver**. Nhờ có Thymeleaf, class `ViewController` mới có thể định tuyến và phục vụ các file giao diện nằm an toàn trong thư mục được bảo vệ `src/main/resources/templates/`.  
> 2. Về phần đổ dữ liệu, nhóm em chủ động **không dùng cú pháp `th:each`, `th:text` kiểu cũ** vì cơ chế SSR truyền thống phụ thuộc vào HTTP Session và bắt buộc phải tải lại toàn bộ trang (Full reload).  
> 3. Thay vào đó, nhóm em xây dựng hệ thống **RESTful API hoàn chỉnh** trả về dữ liệu chuẩn JSON, kết hợp với cơ chế **Stateless JWT Token lưu tại `localStorage`**. Ở phía Frontend, JavaScript sử dụng AJAX để nạp dữ liệu ngầm và render động.  
> Cách tiếp cận này giúp website hoạt động mượt mà không độ trễ, tối ưu hóa băng thông, chống tấn công CSRF, và hệ thống Backend API hoàn toàn sẵn sàng mở rộng cho ứng dụng Mobile trong tương lai mà không cần viết lại!"*

👉 **Kết quả:** Giảng viên sẽ lập tức đánh giá nhóm có kiến thức sâu rộng về kiến trúc ứng dụng web hiện đại, hiểu rõ bản chất công nghệ chứ không phải chỉ copy-paste code mẫu trên mạng!
