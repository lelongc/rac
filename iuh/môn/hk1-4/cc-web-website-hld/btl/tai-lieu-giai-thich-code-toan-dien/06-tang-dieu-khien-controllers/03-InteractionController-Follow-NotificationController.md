# GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG INTERACTION, FOLLOW VÀ NOTIFICATION CONTROLLER

> **Mục tiêu**: Nắm vững hệ thống API phục vụ toàn bộ các tính năng tương tác người dùng: Thích (Like), Bình luận (Comment), Đánh dấu (Bookmark), Theo dõi (Follow/Unfollow), và Hộp thư thông báo thời gian thực (Notifications).

---

## 1. MÃ NGUỒN VÀ GIẢI THÍCH `InteractionController.java`

File nằm tại: `src/main/java/com/group/blog/controller/InteractionController.java`

```java
package com.group.blog.controller;

import com.group.blog.dto.request.ApiResponse;
import com.group.blog.dto.request.CommentRequest;
import com.group.blog.dto.response.BlogResponse;
import com.group.blog.dto.response.CommentResponse;
import com.group.blog.service.InteractionService;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.UUID;

@RestController
@RequestMapping("/blogs")
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class InteractionController {

    InteractionService interactionService;

    // 1. Thích / Bỏ thích bài viết
    @PostMapping("/{blogId}/like")
    public ApiResponse<String> toggleLike(@PathVariable UUID blogId) {
        interactionService.toggleLike(blogId);
        return ApiResponse.<String>builder()
                .result("Toggled like successfully")
                .build();
    }

    // 2. Lấy danh sách bình luận của bài viết
    @GetMapping("/{blogId}/comments")
    public ApiResponse<List<CommentResponse>> getComments(@PathVariable UUID blogId) {
        return ApiResponse.<List<CommentResponse>>builder()
                .result(interactionService.getCommentsByBlogId(blogId))
                .build();
    }

    // 3. Gửi bình luận mới hoặc gửi phản hồi (Reply)
    @PostMapping("/{blogId}/comments")
    public ApiResponse<CommentResponse> addComment(@PathVariable UUID blogId, @RequestBody CommentRequest request) {
        return ApiResponse.<CommentResponse>builder()
                .result(interactionService.addComment(blogId, request))
                .build();
    }

    // 4. Xóa bình luận
    @DeleteMapping("/comments/{commentId}")
    public ApiResponse<String> deleteComment(@PathVariable UUID commentId) {
        interactionService.deleteComment(commentId);
        return ApiResponse.<String>builder()
                .result("Comment deleted successfully")
                .build();
    }

    // 5. Lưu bài viết / Bỏ lưu vào sổ tay
    @PostMapping("/{blogId}/bookmark")
    public ApiResponse<String> toggleBookmark(@PathVariable UUID blogId) {
        interactionService.toggleBookmark(blogId);
        return ApiResponse.<String>builder().result("Toggled bookmark successfully").build();
    }

    // 6. Lấy danh sách toàn bộ bài viết đã lưu của tôi
    @GetMapping("/bookmarks")
    public ApiResponse<List<BlogResponse>> getMyBookmarks() {
        return ApiResponse.<List<BlogResponse>>builder().result(interactionService.getMyBookmarks()).build();
    }
}
```

---

## 2. MÃ NGUỒN VÀ GIẢI THÍCH `FollowController.java`

File nằm tại: `src/main/java/com/group/blog/controller/FollowController.java`

```java
package com.group.blog.controller;

import com.group.blog.dto.request.ApiResponse;
import com.group.blog.dto.response.UserResponse;
import com.group.blog.service.FollowService;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/users")
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class FollowController {

    FollowService followService;

    // 1. Theo dõi hoặc Hủy theo dõi một tác giả
    @PostMapping("/{username}/follow")
    public ApiResponse<String> toggleFollow(@PathVariable String username) {
        followService.toggleFollow(username);
        return ApiResponse.<String>builder()
                .result("Cập nhật trạng thái theo dõi thành công")
                .build();
    }

    // 2. Lấy danh sách những người đang theo dõi tác giả này (Followers)
    @GetMapping("/{username}/followers")
    public ApiResponse<List<UserResponse>> getFollowers(@PathVariable String username) {
        return ApiResponse.<List<UserResponse>>builder()
                .result(followService.getFollowers(username))
                .build();
    }

    // 3. Lấy danh sách những người mà tác giả này đang theo dõi (Following)
    @GetMapping("/{username}/following")
    public ApiResponse<List<UserResponse>> getFollowing(@PathVariable String username) {
        return ApiResponse.<List<UserResponse>>builder()
                .result(followService.getFollowing(username))
                .build();
    }
}
```

---

## 3. MÃ NGUỒN VÀ GIẢI THÍCH `NotificationController.java`

File nằm tại: `src/main/java/com/group/blog/controller/NotificationController.java`

```java
package com.group.blog.controller;

import com.group.blog.dto.request.ApiResponse;
import com.group.blog.dto.response.NotificationResponse;
import com.group.blog.service.NotificationService;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.UUID;

@RestController
@RequestMapping({"/api/notifications", "/notifications/api"})
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class NotificationController {
    NotificationService notificationService;

    // 1. Lấy danh sách thông báo của tôi
    @GetMapping
    public ApiResponse<List<NotificationResponse>> getMyNotifications() {
        return ApiResponse.<List<NotificationResponse>>builder().result(notificationService.getMyNotifications()).build();
    }

    // 2. Đánh dấu một thông báo là đã đọc
    @PutMapping("/{id}/read")
    public ApiResponse<String> markAsRead(@PathVariable UUID id) {
        notificationService.markAsRead(id);
        return ApiResponse.<String>builder().result("Đã đánh dấu đọc").build();
    }

    // 3. Xóa một thông báo
    @DeleteMapping("/{id}")
    public ApiResponse<String> deleteNotification(@PathVariable UUID id) {
        notificationService.deleteNotification(id);
        return ApiResponse.<String>builder().result("Đã xóa thông báo").build();
    }
}
```

### Điểm đặc biệt: `@RequestMapping({"/api/notifications", "/notifications/api"})`
- Spring Boot cho phép khai báo một mảng các URL ánh xạ đến cùng một Controller.
- Điều này giúp hỗ trợ tương thích với cả 2 cách gọi API khác nhau từ các file JS cũ và mới trong mã nguồn giao diện mà không sợ bị lỗi 404 Not Found.

---

## 4. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN & TRẢ LỜI ĐIỂM 10

### Câu 1: Tại sao các API như `/like`, `/follow`, `/bookmark` lại dùng phương thức HTTP POST mà không dùng GET hay PUT?
- **Trả lời**:
  > "Thưa thầy/cô, theo chuẩn thiết kế RESTful API:
  > - Phương thức **GET** có tính chất Idempotent (chỉ đọc dữ liệu, tuyệt đối không được làm thay đổi trạng thái trong CSDL). Hơn nữa trình duyệt có thể tự động cache các request GET hoặc các bot cào dữ liệu Google Bot truy cập vào link GET sẽ vô tình làm thay đổi dữ liệu like/follow.
  > - Hành vi Like/Follow/Bookmark là thao tác tương tác tạo mới hoặc xóa dữ liệu trong DB, do đó bắt buộc phải sử dụng phương thức **POST** (hoặc DELETE) để đảm bảo tính an toàn và đúng chuẩn HTTP."

### Câu 2: Khi gọi API `POST /blogs/{blogId}/comments`, làm sao hệ thống phân biệt được đó là bình luận gốc hay là một câu trả lời (Reply)?
- **Trả lời**:
  > "Thưa thầy/cô, hệ thống căn cứ vào trường `parentId` trong đối tượng `CommentRequest`:
  > - Nếu `parentId == null`: Đó là bình luận gốc cấp 1 vào bài viết.
  > - Nếu `parentId != null`: Đó là câu trả lời cho một bình luận đã có sẵn. Hệ thống sẽ trỏ `comment.setParent(parent)` để tạo nhánh cây phân cấp con."
