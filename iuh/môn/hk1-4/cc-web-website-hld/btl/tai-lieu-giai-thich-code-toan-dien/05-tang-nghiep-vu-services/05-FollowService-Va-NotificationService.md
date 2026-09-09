# GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG FOLLOWSERVICE VÀ NOTIFICATIONSERVICE

> **Mục tiêu**: Hiểu trọn vẹn nghiệp vụ Theo dõi tác giả (Follow / Unfollow System), Ngăn chặn tự theo dõi chính mình, Làm giàu dữ liệu hồ sơ cá nhân (`enrichUserResponse`), và Cơ chế gửi thông báo tự động (Notification Engine) cho các sự kiện Thích, Bình luận, Phản hồi, Theo dõi.

---

## 1. MÃ NGUỒN VÀ GIẢI THÍCH CHI TIẾT `FollowService.java`

File nằm tại: `src/main/java/com/group/blog/service/FollowService.java`

### 1.1. Bật/Tắt theo dõi tác giả: `toggleFollow()`
```java
    @Transactional
    public void toggleFollow(String targetUsername) {
        String currentUsername = SecurityContextHolder.getContext().getAuthentication().getName();

        // 1. Ràng buộc nghiệp vụ: Không cho phép tự follow chính mình
        if (currentUsername.equals(targetUsername)) {
            throw new RuntimeException("Bạn không thể tự theo dõi chính mình!");
        }

        User follower = userRepository.findByUsername(currentUsername)
                .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));
        User following = userRepository.findByUsername(targetUsername)
                .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));

        Optional<UserFollow> existingFollow = userFollowRepository.findByFollowerAndFollowing(follower, following);

        if (existingFollow.isPresent()) {
            userFollowRepository.delete(existingFollow.get()); // Đã follow -> Hủy theo dõi (Unfollow)
        } else {
            UserFollow newFollow = UserFollow.builder().follower(follower).following(following).build();
            userFollowRepository.save(newFollow); // Chưa follow -> Lưu bản ghi Theo dõi

            // 2. Kích hoạt thông báo gửi đến người được theo dõi
            notificationService.createNotification(
                    following,
                    "@" + currentUsername + " started following you.",
                    "user-profile.html?user=" + currentUsername,
                    "FOLLOW"
            );
        }
    }
```
- **Ràng buộc an toàn**: Nếu người dùng cố tình gửi request follow chính username của mình, hệ thống sẽ chặn lại ngay từ đầu.
- **Tự động gửi thông báo**: Khi A bấm theo dõi B, hệ thống ngay lập tức tạo thông báo cho B biết kèm đường link dẫn thẳng tới trang cá nhân của A để B có thể follow lại (Follow back).

---

### 1.2. Làm giàu dữ liệu người dùng: `enrichUserResponse()`
```java
    public UserResponse enrichUserResponse(User user) {
        UserResponse response = userMapper.toUserResponse(user);

        // 1. Đếm số lượng Người theo dõi và Đang theo dõi từ Database
        response.setTotalFollowers(userFollowRepository.countByFollowing(user));
        response.setTotalFollowing(userFollowRepository.countByFollower(user));

        // 2. Kiểm tra xem người đang đăng nhập hiện tại đã follow tác giả này chưa
        var auth = SecurityContextHolder.getContext().getAuthentication();
        if (auth != null && auth.isAuthenticated() && !auth.getName().equals("anonymousUser")) {
            boolean isFollowed = userFollowRepository.existsByFollowerUsernameAndFollowing(auth.getName(), user);
            response.setFollowedByCurrentUser(isFollowed);
        } else {
            response.setFollowedByCurrentUser(false);
        }

        return response;
    }
```
- **Ý nghĩa đối với giao diện**:
  - Khi xem trang cá nhân của tác giả bất kỳ (`user-profile.html?user=duonghd`), giao diện cần biết nút bấm nên hiển thị là chữ **"Theo dõi" (+ Follow)** hay **"Đang theo dõi" (Following)**.
  - Trường `followedByCurrentUser` trả về `true/false` chính xác để JavaScript hiển thị nút bấm tương ứng.

---

## 2. MÃ NGUỒN VÀ GIẢI THÍCH CHI TIẾT `NotificationService.java`

File nằm tại: `src/main/java/com/group/blog/service/NotificationService.java`

```java
package com.group.blog.service;

import com.group.blog.dto.response.NotificationResponse;
import com.group.blog.entity.Notification;
import com.group.blog.entity.User;
import com.group.blog.repository.NotificationRepository;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.UUID;

@Service
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class NotificationService {
    NotificationRepository notificationRepository;

    // 1. Hàm dùng nội bộ để tạo thông báo mới
    public void createNotification(User recipient, String message, String targetUrl, String type) {
        // Tối ưu trải nghiệm: Không tự gửi thông báo cho chính mình (VD: Tự like bài của mình)
        String currentUsername = SecurityContextHolder.getContext().getAuthentication().getName();
        if (recipient.getUsername().equals(currentUsername)) return;

        Notification notif = Notification.builder()
                .user(recipient)
                .message(message)
                .targetUrl(targetUrl)
                .type(type)
                .isRead(false)
                .build();
        notificationRepository.save(notif);
    }

    // 2. Lấy danh sách thông báo của người dùng hiện tại
    public List<NotificationResponse> getMyNotifications() {
        String username = SecurityContextHolder.getContext().getAuthentication().getName();
        return notificationRepository.findByUserUsernameOrderByCreatedAtDesc(username)
                .stream().map(n -> NotificationResponse.builder()
                        .id(n.getId())
                        .message(n.getMessage())
                        .targetUrl(n.getTargetUrl())
                        .type(n.getType())
                        .isRead(n.isRead())
                        .createdAt(n.getCreatedAt())
                        .build()).toList();
    }

    // 3. Đánh dấu thông báo đã đọc
    @Transactional
    public void markAsRead(UUID id) {
        Notification n = notificationRepository.findById(id).orElseThrow();
        n.setRead(true);
        notificationRepository.save(n);
    }

    // 4. Xóa thông báo
    public void deleteNotification(UUID id) {
        notificationRepository.deleteById(id);
    }
}
```

### Điểm sáng logic trong `createNotification()`:
- `if (recipient.getUsername().equals(currentUsername)) return;`: Nếu một tác giả tự bấm Like hoặc tự bình luận vào bài viết của chính mình để thử nghiệm, hệ thống sẽ tự động bỏ qua không tạo thông báo rác cho chính người đó.

---

## 3. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN & TRẢ LỜI ĐIỂM 10

### Câu 1: Em hãy giải thích cơ chế thông báo chưa đọc (Unread Badge) trên biểu tượng quả chuông Navbar hoạt động như thế nào?
- **Trả lời**:
  > "Thưa thầy/cô:
  > - Khi người dùng mở bất kỳ trang web nào, file JavaScript `nav.js` sẽ gửi request `GET /api/notifications` để lấy danh sách thông báo của người đó.
  > - Phía Frontend chỉ cần đếm số phần tử có trường `isRead === false`. Nếu số lượng > 0, một chấm đỏ (Badge) hiển thị số thông báo chưa đọc sẽ xuất hiện trên quả chuông.
  > - Khi người dùng click vào xem một thông báo, Frontend gửi request `PUT /api/notifications/{id}/read`. Phương thức `markAsRead()` ở Backend sẽ cập nhật trường `isRead = true` và lưu vào Database, ngay lập tức chấm đỏ sẽ giảm số hoặc biến mất."
