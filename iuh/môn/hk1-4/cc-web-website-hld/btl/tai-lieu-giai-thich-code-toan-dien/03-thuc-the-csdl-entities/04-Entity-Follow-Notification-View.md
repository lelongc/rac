# GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG ENTITY USERFOLLOW, NOTIFICATION VÀ BLOGVIEW

> **Mục tiêu**: Hiểu trọn vẹn cách thiết kế 3 tính năng nâng cao: Theo dõi tác giả (Follow System), Hệ thống thông báo thời gian thực (Notification System) và Cơ chế ghi nhận lượt xem bài viết có hỗ trợ khách vãng lai và địa chỉ IP (View Counter System).

---

## 1. MÃ NGUỒN ĐẦY ĐỦ CỦA 3 THỰC THỂ

### 1.1. Thực thể `UserFollow.java` (`src/main/java/com/group/blog/entity/UserFollow.java`)
```java
package com.group.blog.entity;

import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.FieldDefaults;
import java.time.LocalDateTime;
import java.util.UUID;

@Entity
@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE)
@Table(name="user_follows", uniqueConstraints = {
        @UniqueConstraint(columnNames = {"follower_id", "following_id"})
})
public class UserFollow {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    UUID id;

    // Người đi theo dõi (Follower)
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "follower_id", nullable = false)
    User follower;

    // Người được theo dõi (Following)
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "following_id", nullable = false)
    User following;

    LocalDateTime createdAt;

    @PrePersist
    void prePersist() {
        if(createdAt == null) createdAt = LocalDateTime.now();
    }
}
```

### 1.2. Thực thể `Notification.java` (`src/main/java/com/group/blog/entity/Notification.java`)
```java
package com.group.blog.entity;

import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.FieldDefaults;

import java.time.LocalDateTime;
import java.util.UUID;

@Entity
@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE)
@Table(name="notifications", indexes = {
        @Index(name="idx_notif_user", columnList="user_id")
})
public class Notification {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    UUID id;

    // Người NHẬN thông báo
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id", nullable = false)
    User user;

    @Column(nullable = false)
    String message;

    String targetUrl; // Link bấm vào để xem chi tiết (VD: "/post?id=...")

    @Builder.Default
    boolean isRead = false; // Trạng thái đã đọc hay chưa

    LocalDateTime createdAt;

    @Column(nullable = false)
    String type; // Chứa các giá trị: "LIKE", "COMMENT", "REPLY", "FOLLOW"

    @PrePersist
    void prePersist(){
        if(createdAt == null){
            createdAt = LocalDateTime.now();
        }
    }
}
```

### 1.3. Thực thể `BlogView.java` (`src/main/java/com/group/blog/entity/BlogView.java`)
```java
package com.group.blog.entity;

import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.FieldDefaults;
import java.time.LocalDateTime;
import java.util.UUID;

@Entity
@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE)
@Table(name="blog_views")
// Mỗi khi ai đó vào đọc bài, sẽ insert 1 dòng vào đây
public class BlogView {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    UUID id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "blog_id", nullable = false)
    @org.hibernate.annotations.OnDelete(action = org.hibernate.annotations.OnDeleteAction.CASCADE)
    Blog blog;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id")
    User user;

    // Cho phép Khách (Guest) không có tài khoản vẫn tăng View được
    String ipAddress;

    LocalDateTime viewedAt;

    @PrePersist
    void prePersist(){
        if(viewedAt == null){
            viewedAt = LocalDateTime.now();
        }
    }
}
```

---

## 2. GIẢI THÍCH CHI TIẾT TỪNG THÀNH PHẦN

### 2.1. Thiết kế bảng theo dõi tác giả (`UserFollow`)
- **Hai cột cùng trỏ về 1 bảng `users`**:
  - `follower_id`: Người nhấn nút "Theo dõi" (Ví dụ: Bạn Dũng theo dõi Bạn Dương).
  - `following_id`: Người được theo dõi (Bạn Dương).
  - Cả hai đều có kiểu dữ liệu là `User`, nhưng ánh xạ tới 2 cột khóa ngoại khác nhau.
- **`uniqueConstraints = @UniqueConstraint(columnNames = {"follower_id", "following_id"})`**: Ngăn chặn tuyệt đối việc một người có thể nhấn theo dõi 2 lần cùng một tác giả.

---

### 2.2. Thiết kế bảng thông báo (`Notification`)
- **`user_id`**: Người nhận thông báo. Khi người A bấm Like bài viết của người B, hệ thống sẽ tạo một dòng thông báo với `user_id = B.getId()`.
- **`targetUrl`**: Lưu đường dẫn URL để khi người dùng click vào quả chuông thông báo trên thanh Navbar, giao diện sẽ chuyển thẳng đến bài viết hoặc bình luận tương ứng (Ví dụ: `/post?id=abc-123`).
- **`isRead`**: Mặc định là `false` (chưa đọc). Khi người dùng mở hộp thông báo ra xem, API sẽ cập nhật trường này thành `true` và làm giảm số đỏ trên biểu tượng quả chuông thông báo.
- **`type`**: Lưu loại sự kiện (`LIKE`, `COMMENT`, `REPLY`, `FOLLOW`), giúp phía giao diện hiển thị icon phù hợp (icon trái tim cho Like, icon bong bóng thoại cho Comment, icon người dùng cho Follow).

---

### 2.3. Thiết kế bảng lượt xem bài viết (`BlogView`)
- **Tại sao không dùng một cột `view_count INT` trực tiếp trong bảng `blogs` mà lại tách riêng thành một bảng `BlogView`?**:
  - **Lý do 1 (Chống tăng view ảo / Spam View)**: Nếu chỉ có một cột số, mỗi lần người dùng bấm F5 lại trang, số view sẽ tăng lên vô hạn. Với bảng `BlogView`, hệ thống có thể kiểm tra: Nếu trong vòng 30 phút qua, cùng một địa chỉ `ipAddress` hoặc cùng một `user_id` đã xem bài viết này rồi thì không ghi nhận thêm lượt xem mới.
  - **Lý do 2 (Phục vụ thống kê Analytics chuyên sâu)**: Nhờ lưu vết thời gian `viewedAt`, trang Quản trị Admin có thể vẽ biểu đồ lượt xem theo từng ngày, từng tháng, hoặc xem thống kê bài viết nào được đọc nhiều nhất trong tuần.
- **`user_id` không bắt buộc (`nullable = true`)**: Người đọc vãng lai chưa tạo tài khoản vẫn được tính lượt xem thông qua trường `ipAddress`.

---

## 3. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN & TRẢ LỜI ĐIỂM 10

### Câu 1: Em hãy giải thích luồng tạo thông báo (Notification) khi một người dùng bình luận vào bài viết?
- **Trả lời**:
  > "Thưa thầy/cô, luồng diễn ra như sau:
  > 1. Khi User A gửi bình luận vào bài viết của tác giả B, sau khi lưu bình luận vào bảng `comments`, `InteractionService` sẽ so sánh xem User A có phải chính là tác giả B không. Nếu tự bình luận vào bài của chính mình thì không cần gửi thông báo.
  > 2. Nếu User A khác tác giả B, hệ thống gọi `NotificationService.createNotification(...)`.
  > 3. Hệ thống tạo một bản ghi `Notification` mới với người nhận là tác giả B, nội dung: `'{User A} đã bình luận về bài viết của bạn'`, đính kèm `targetUrl` dẫn thẳng đến bài viết, và `type = 'COMMENT'`.
  > 4. Khi tác giả B đăng nhập vào hệ thống, icon quả chuông trên thanh menu sẽ tự động gọi API lấy các thông báo chưa đọc và hiển thị cho tác giả."

### Câu 2: Tại sao trong bảng `BlogView` trường `user` lại được phép `null` trong khi trường `blog` lại bắt buộc `nullable = false`?
- **Trả lời**:
  > "Thưa thầy/cô:
  > - Lượt xem bài viết thì **bắt buộc phải gắn liền với một bài blog cụ thể**, nếu không có bài blog thì lượt xem đó hoàn toàn vô nghĩa, do đó `blog` phải là `nullable = false`.
  > - Ngược lại, một website blog công khai cho phép bất kỳ ai trên Internet truy cập đọc bài mà không bắt buộc phải đăng nhập. Khách vãng lai (Guest) chưa có tài khoản thì trường `user` sẽ mang giá trị `null`, và hệ thống sẽ lưu địa chỉ IP (`ipAddress`) của máy khách để ghi nhận lượt xem hợp lệ."
