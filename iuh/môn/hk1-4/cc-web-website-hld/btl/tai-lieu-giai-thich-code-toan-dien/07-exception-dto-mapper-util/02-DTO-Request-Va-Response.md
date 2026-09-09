# GIẢI THÍCH CHI TIẾT TOÀN BỘ CÁC DTO REQUEST VÀ RESPONSE CỦA HỆ THỐNG

> **Mục tiêu**: Nắm chắc vai trò của mô hình DTO (Data Transfer Object) trong việc ngăn chặn tấn công dữ liệu, bảo vệ mật khẩu, và thiết kế lớp vỏ phản hồi chuẩn hóa `ApiResponse<T>`.

---

## 1. TỔNG QUAN VỀ DTO TRONG DỰ ÁN

Trong dự án **Blog Website**, toàn bộ dữ liệu trao đổi giữa Client và Server được chia làm 2 nhóm rõ rệt:
- **`dto/request` (10 files)**: Hứng dữ liệu người dùng gửi lên từ các Form biểu mẫu, kèm các ràng buộc xác thực dữ liệu (`@Valid`, `@Size`, `@NotBlank`).
- **`dto/response` (10 files)**: Đóng gói dữ liệu từ Server chuẩn bị gửi về cho trình duyệt, chỉ chọn lọc những trường an toàn, che giấu các trường nhạy cảm (mật khẩu) và đính kèm các chỉ số động tính toán từ DB.

---

## 2. CHI TIẾT CÁC REQUEST DTO (`com.group.blog.dto.request`)

### 2.1. `ApiResponse.java` (Lớp vỏ bao bọc phản hồi toàn cục)
```java
package com.group.blog.dto.request;

import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.*;
import lombok.experimental.FieldDefaults;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE)
@JsonInclude(JsonInclude.Include.NON_NULL)
public class ApiResponse <T>{
    @Builder.Default
    int code = 1000;
    String message;
    T result;
}
```
- **`@JsonInclude(JsonInclude.Include.NON_NULL)`**: Cực kỳ thông minh! Nếu trường nào mang giá trị `null` (ví dụ khi gọi thành công thì `message = null`), Jackson sẽ tự động loại bỏ trường đó khỏi chuỗi JSON, giúp gói tin mạng nhẹ hơn và JSON sạch sẽ hơn.
- **`code = 1000`**: Mã quy ước toàn hệ thống cho biết request thực thi thành công.

### 2.2. `UserCreatetionRequest.java` (Đăng ký tài khoản)
```java
public class UserCreatetionRequest {
    @Size(min = 3, message = "USERNAME_INVALID")
    String username;

    @Size(min = 8, message = "INVALID_PASSWORD")
    String password;

    String email;
}
```
- Sử dụng `@Size` để kiểm tra độ dài username tối thiểu 3 ký tự, password tối thiểu 8 ký tự. Thông điệp lỗi liên kết trực tiếp với Enum `ErrorCode`.

### 2.3. `PasswordChangeRequest.java` (Đổi mật khẩu)
```java
public class PasswordChangeRequest {
    String oldPassword;
    String newPassword;
    String confirmPassword;
}
```

### 2.4. `BlogCreationRequest.java` & `BlogUpdateRequest.java`
```java
public class BlogCreationRequest {
    String title;
    String description;
    String content;
    String banner;
    UUID categoryId;
    List<String> tags;
    Boolean draft;
}
```
- Nhận thông tin bài viết cùng danh sách tên các thẻ tag (`List<String> tags`) và cờ lưu nháp `draft`.

### 2.5. `CommentRequest.java` (Bình luận bài viết)
```java
public class CommentRequest {
    String content;
    UUID parentId; // Nếu là reply thì truyền ID của comment cha, nếu comment gốc thì để null
}
```

---

## 3. CHI TIẾT CÁC RESPONSE DTO (`com.group.blog.dto.response`)

### 3.1. `UserResponse.java` (Thông tin người dùng trả về)
```java
public class UserResponse {
    UUID id;
    String username;
    String email;
    String bio;
    String avatarUrl;
    Set<String> roles;
    
    // Các trường làm giàu dữ liệu từ FollowService
    long totalFollowers;
    long totalFollowing;
    boolean isFollowedByCurrentUser;
    LocalDateTime createdAt;
}
```
- **Tuyệt đối không có trường `password`**: Loại bỏ 100% nguy cơ lộ mã băm mật khẩu ra ngoài Internet.
- Bổ sung thêm các chỉ số: tổng số người theo dõi (`totalFollowers`), tổng số người đang theo dõi (`totalFollowing`) và trạng thái tôi đã follow người này chưa (`isFollowedByCurrentUser`).

### 3.2. `BlogResponse.java` (Dữ liệu bài viết đầy đủ)
```java
public class BlogResponse {
    UUID id;
    String title;
    String slug;
    String banner;
    String description;
    String content;
    boolean draft;
    String draftContent;
    String draftBanner;
    LocalDateTime publishedAt;
    LocalDateTime createdAt;
    UserResponse author;
    CategoryResponse category;
    Set<TagResponse> tags;
    
    // Thống kê tương tác thời gian thực
    int totalReads;
    int totalLikes;
    int totalComments;
    boolean isLikedByCurrentUser;
    boolean isBookmarkedByCurrentUser;
}
```
- Trả về đối tượng lồng nhau chuẩn JSON: `author` là một `UserResponse`, `category` là `CategoryResponse`, danh sách `tags` là `Set<TagResponse>`.
- Kèm theo 3 con số thống kê và 2 cờ trạng thái boolean phục vụ giao diện người dùng.

### 3.3. `AdminStatsResponse.java` (Thống kê bảng điều khiển Admin)
```java
public class AdminStatsResponse {
    long totalUsers;
    long totalPosts;
    List<BlogResponse> recentPosts;
}
```

---

## 4. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN VỀ DTO & TRẢ LỜI ĐIỂM 10

### Câu 1: Em hãy giải thích chú thích `@JsonInclude(JsonInclude.Include.NON_NULL)` trong `ApiResponse.java` có tác dụng gì?
- **Trả lời**:
  > "Thưa thầy/cô, annotation này chỉ thị cho thư viện chuyển đổi Jackson: **Chỉ đưa vào chuỗi JSON những thuộc tính có giá trị khác null**.
  > Ví dụ khi gọi API lấy danh sách bài viết thành công, biến `message` mang giá trị `null`, Jackson sẽ tự động bỏ qua thuộc tính `message` trong chuỗi JSON trả về. Ngược lại khi có lỗi xảy ra, biến `result` mang giá trị `null`, Jackson sẽ loại bỏ `result` và chỉ trả về `code` cùng `message`. Điều này giúp gói tin HTTP nhỏ gọn tối đa, tiết kiệm băng thông mạng và định dạng JSON phía Client nhận được rất sạch sẽ."

### Câu 2: Tại sao trong `UserResponse` nhóm lại thiết kế các trường như `totalFollowers` và `isFollowedByCurrentUser` mà trong Entity `User` lại không có các trường này?
- **Trả lời**:
  > "Thưa thầy/cô, đây là minh chứng rõ nét nhất cho sức mạnh của mô hình DTO:
  > - Trong CSDL (Entity `User`), việc lưu trực tiếp cột `totalFollowers` sẽ vi phạm chuẩn hóa dữ liệu 3NF và dễ gây sai lệch số liệu khi có nhiều người cùng follow đồng thời.
  > - Tuy nhiên ở phía giao diện người dùng, trang cá nhân bắt buộc phải hiển thị con số này.
  > - Do đó, DTO `UserResponse` đóng vai trò là một 'View Model' linh hoạt, cho phép tầng Service tính toán (từ `UserFollowRepository`) và gắn thêm các thông số động này vào trước khi gửi về cho giao diện, đáp ứng hoàn hảo nhu cầu hiển thị mà không làm phá vỡ cấu trúc tinh gọn của cơ sở dữ liệu."
