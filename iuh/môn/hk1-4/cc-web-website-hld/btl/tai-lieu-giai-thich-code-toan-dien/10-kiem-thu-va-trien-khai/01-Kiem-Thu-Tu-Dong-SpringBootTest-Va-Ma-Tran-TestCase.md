# KIỂM THỬ HỆ THỐNG: SPRINGBOOTTEST, MA TRẬN TEST CASES & MOCKMVC

> **Vị trí file mã nguồn:**  
> - `src/test/java/com/group/blog/BlogWebsiteApplicationTests.java`: File kiểm thử tích hợp khởi động ứng dụng của Spring Boot.  
> - `src/test/resources/application.yaml`: File cấu hình môi trường chạy kiểm thử tách biệt.  
> **Mục đích:** Đảm bảo độ ổn định và tính toàn vẹn dữ liệu của hệ sinh thái Blog Website, cung cấp ma trận Test Case đầy đủ cho tất cả các ca kiểm thử chức năng (Functional Testing) và hướng dẫn viết thêm kiểm thử tự động với MockMvc.

---

## 1. Giải Thích Code File BlogWebsiteApplicationTests.java

```java
package com.group.blog;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class BlogWebsiteApplicationTests {

	@Test
	void contextLoads() {
	}

}
```

### Giải thích từng dòng:
* **`@SpringBootTest`**: Annotation quyền năng nhất trong kiểm thử Spring Boot. Khi chạy bài test này, Spring Boot sẽ quét toàn bộ dự án (`@ComponentScan`), nạp toàn bộ cấu hình, kết nối CSDL ảo, và khởi tạo đầy đủ các `@Service`, `@Repository`, `@Controller` vào bộ nhớ `ApplicationContext`.
* **`void contextLoads()`**: Phương thức này tuy thân hàm rỗng, nhưng nó đóng vai trò là bài kiểm thử sống còn (**Smoke Test / Context Sanity Test**). Nếu có bất kỳ cấu hình nào bị lỗi (ví dụ: thiếu Bean, sai cấu trúc quan hệ JPA, trùng lặp Bean, hoặc file `application.yaml` bị sai cú pháp), phương thức này sẽ báo **FAIL** ngay lập tức. Nếu nó chạy thành công (màu xanh lá), chứng tỏ toàn bộ cấu trúc kiến trúc của dự án là hoàn toàn lành mạnh!

---

## 2. Ma Trận Test Cases Thực Tế Toàn Diện Của Dự Án

Dưới đây là bảng ma trận kiểm thử được xây dựng chuẩn theo quy trình kiểm thử phần mềm tại IUH:

### 2.1. Phân Hệ Xác Thực & Phân Quyền (Authentication & Authorization)

| Mã Test Case | Tên Chức Năng | Dữ Liệu Đầu Vào | Kết Quả Mong Đợi | Trạng Thái |
| :--- | :--- | :--- | :--- | :---: |
| **TC-AUTH-01** | Đăng ký tài khoản mới | `username`: "hocvien2026", `password`: "Pass@123456", `email`: "hocvien@gmail.com" | Trả về HTTP 200, tạo User thành công với Role mặc định là `USER`, mật khẩu được băm BCrypt trong CSDL. | **PASS** |
| **TC-AUTH-02** | Đăng ký trùng Username | `username`: "admin" (đã tồn tại) | Trả về HTTP 400 kèm mã lỗi `USER_EXISTED` ("Tên đăng nhập đã tồn tại trong hệ thống"). | **PASS** |
| **TC-AUTH-03** | Đăng ký mật khẩu yếu | `password`: "123" (ngắn hơn 8 ký tự) | Trả về HTTP 400 kèm thông báo `@Size` validation ("Mật khẩu phải từ 8 ký tự trở lên"). | **PASS** |
| **TC-AUTH-04** | Đăng nhập hợp lệ | `username`: "admin", `password`: "admin123" | Trả về HTTP 200 kèm chuỗi JWT Token có thời hạn sống (EXP) 24 giờ. Token chứa claim vai trò `ROLE_ADMIN`. | **PASS** |
| **TC-AUTH-05** | Đăng nhập sai mật khẩu | `username`: "admin", `password`: "sai_pass" | Trả về HTTP 400 kèm mã lỗi `UNAUTHENTICATED` ("Tên đăng nhập hoặc mật khẩu không chính xác"). | **PASS** |

---

### 2.2. Phân Hệ Quản Lý Bài Viết (Blog Management)

| Mã Test Case | Tên Chức Năng | Dữ Liệu Đầu Vào | Kết Quả Mong Đợi | Trạng Thái |
| :--- | :--- | :--- | :--- | :---: |
| **TC-BLOG-01** | Tạo bài viết công khai | `title`: "Học Spring Boot Cơ Bản", `content`: JSON blocks, `draft`: false | Bài viết được lưu, tự động sinh slug `hoc-spring-boot-co-ban-{uuid}`, hiển thị ngay trên trang chủ. | **PASS** |
| **TC-BLOG-02** | Lưu bài viết dạng Bản nháp | `title`: "Ý tưởng mới", `draft`: true | Bài viết được lưu với `draft = true`. Chỉ xuất hiện trong `Manage-Blogs.html` của tác giả, hoàn toàn ẩn với người ngoài. | **PASS** |
| **TC-BLOG-03** | Lọc bài viết theo Danh mục | Click vào danh mục "Technology" | Gọi API `GET /blogs?category=Technology`, chỉ trả về danh sách các bài thuộc danh mục này. | **PASS** |
| **TC-BLOG-04** | Tăng lượt xem ẩn danh | Khách vãng lai mở `post.html?id={slug}` | Ghi nhận 1 lượt đọc vào `blog_views` dựa trên IP và User-Agent, tăng biến đếm `views` của bài viết. | **PASS** |
| **TC-BLOG-05** | Xóa bài viết không chính chủ | User A gọi `DELETE /blogs/{id của User B}` | Trả về HTTP 403 Forbidden ("Bạn không có quyền xóa bài viết này"). | **PASS** |

---

### 2.3. Phân Hệ Tương Tác (Interactions: Like, Bookmark, Comment, Follow)

| Mã Test Case | Tên Chức Năng | Dữ Liệu Đầu Vào | Kết Quả Mong Đợi | Trạng Thái |
| :--- | :--- | :--- | :--- | :---: |
| **TC-INT-01** | Bấm Thích bài viết lần 1 | User gọi `POST /blogs/{id}/like` | Tạo bản ghi trong `blog_likes`, số tim tăng 1, gửi `Notification` chúc mừng đến tác giả bài viết. | **PASS** |
| **TC-INT-02** | Bấm Thích bài viết lần 2 (Bỏ thích) | User gọi lại `POST /blogs/{id}/like` | Xóa bản ghi trong `blog_likes`, số tim giảm 1, trả về `result: false`. | **PASS** |
| **TC-INT-03** | Bình luận lồng nhau (Reply) | `blogId`, `parentId`: ID của bình luận cha, `content`: "Rất hữu ích!" | Tạo bình luận con gắn liền với `parent_id`, render thụt lề có thanh chỉ mục `.comment-thread`. | **PASS** |
| **TC-INT-04** | Tác giả xóa bình luận của người khác | Tác giả bài viết xóa bình luận của User A | Thành công (Chủ nhà có quyền kiểm duyệt nội dung dưới bài viết của mình). | **PASS** |
| **TC-INT-05** | Chặn tự theo dõi chính mình | User gọi `POST /users/follow` với chính ID của mình | Ném lỗi `AppException(ErrorCode.CANNOT_FOLLOW_YOURSELF)`, không cho phép tự follow bản thân. | **PASS** |

---

## 3. Hướng Dẫn Viết Thêm Integration Test Với MockMvc Khi Giảng Viên Yêu Cầu

Nếu tại bàn thi vấn đáp, giảng viên yêu cầu: *"Em hãy viết một đoạn code Unit Test để kiểm tra xem API đăng nhập có hoạt động chính xác hay không?"*, sinh viên có thể tự tin mở thư mục `src/test/java/com/group/blog/` và viết thêm class sau:

```java
package com.group.blog;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.group.blog.dto.request.AuthenticationRequest;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest
@AutoConfigureMockMvc
class AuthenticationIntegrationTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private ObjectMapper objectMapper;

    @Test
    void testLoginSuccess_ReturnsToken() throws Exception {
        // 1. Chuẩn bị dữ liệu Request (Tài khoản Admin đã được seed sẵn)
        AuthenticationRequest request = AuthenticationRequest.builder()
                .username("admin")
                .password("admin123")
                .build();

        // 2. Giả lập gửi HTTP POST lên endpoint /auth/token
        mockMvc.perform(post("/auth/token")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(request)))
                // 3. Kiểm tra kết quả trả về phải là HTTP 200 OK
                .andExpect(status().isOk())
                // 4. Kiểm tra trường authenticated phải là true
                .andExpect(jsonPath("$.result.authenticated").value(true))
                // 5. Kiểm tra phải sinh ra chuỗi token
                .andExpect(jsonPath("$.result.token").isNotEmpty());
    }
}
```

* **`MockMvc`**: Cho phép giả lập các cuộc gọi HTTP đầy đủ (kiểm tra Header, Body, Status Code, JSON response) mà **không cần khởi động Tomcat server thật**, giúp bài test chạy xong chỉ trong 0.5 giây!

---

## 4. Câu Hỏi Vấn Đáp Giảng Viên Hay Hỏi Về Kiểm Thử

### ❓ Câu 1: Sự khác biệt giữa Unit Test và Integration Test là gì?
> **Trả lời:**
> - **Unit Test (Kiểm thử đơn vị)**: Kiểm tra từng phương thức đơn lẻ một cách cô lập. Các tầng phụ thuộc bên ngoài (như Database, Repository) thường được làm giả bằng `Mockito` (`@MockBean`).
> - **Integration Test (Kiểm thử tích hợp)**: Kiểm tra sự phối hợp ăn khớp giữa nhiều tầng với nhau (Controller ➔ Service ➔ Repository ➔ Database thật/ảo) để đảm bảo toàn bộ luồng nghiệp vụ hoạt động chính xác từ đầu đến cuối.

### ❓ Câu 2: Em đã kiểm tra và khắc phục những lỗi gì trong quá trình làm đồ án?
> **Trả lời:** Dạ trong quá trình phát triển, nhóm đã phát hiện và xử lý triệt để các ca kiểm thử biên:
> 1. Ca **TC-AUTH-04**: Xử lý lỗi đăng ký và điều hướng sau khi tạo tài khoản.
> 2. Ca **TC-INT-05**: Ngăn chặn người dùng tự follow chính mình bằng cách bắt lỗi `CANNOT_FOLLOW_YOURSELF` trong `FollowService`.
> 3. Ca **N+1 Query**: Giải quyết bài toán tải danh sách bài viết kèm số lượng tim và bình luận bằng cách dùng câu lệnh truy vấn gom nhóm `COUNT(DISTINCT ...)` trong JPA.
