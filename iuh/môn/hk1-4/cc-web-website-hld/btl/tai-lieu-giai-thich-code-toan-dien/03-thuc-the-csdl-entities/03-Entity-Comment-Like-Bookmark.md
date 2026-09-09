# GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG ENTITY COMMENT, BLOGLIKE VÀ BOOKMARK

> **Mục tiêu**: Hiểu cặn kẽ cách thiết kế tính năng tương tác mạng xã hội của Blog: Cây bình luận đa cấp (cha - con / Self-Referencing Entity), cơ chế chống Like/Bookmark trùng lặp bằng `@UniqueConstraint`, và cơ chế xóa dây chuyền tự động `@OnDelete(action = OnDeleteAction.CASCADE)`.

---

## 1. MÃ NGUỒN ĐẦY ĐỦ CỦA 3 THỰC THỂ

### 1.1. Thực thể `Comment.java` (`src/main/java/com/group/blog/entity/Comment.java`)
```java
package com.group.blog.entity;

import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.FieldDefaults;
import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;

@Entity
@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE)
@Table(name="comments", indexes = {
        @Index(name="idx_comment_blog", columnList="blog_id"),
        @Index(name="idx_comment_parent", columnList="parent_id")
})
public class Comment {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    UUID id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "blog_id", nullable = false)
    @org.hibernate.annotations.OnDelete(action = org.hibernate.annotations.OnDeleteAction.CASCADE)
    Blog blog;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id", nullable = false)
    User user;

    // Quan hệ đệ quy: Trỏ đến bình luận cha (nếu là phản hồi)
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "parent_id")
    Comment parent;

    // 1 comment cha có thể có nhiều bình luận phản hồi con
    @OneToMany(mappedBy = "parent", cascade = CascadeType.ALL, orphanRemoval = true)
    @OrderBy("createdAt ASC")
    List<Comment> replies;

    @Column(columnDefinition = "TEXT")
    String content;

    LocalDateTime createdAt;

    @PrePersist
    void prePersist(){
        if(createdAt == null){
            createdAt = LocalDateTime.now();
        }
    }
}
```

### 1.2. Thực thể `BlogLike.java` (`src/main/java/com/group/blog/entity/BlogLike.java`)
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
@Table(name="blog_likes", uniqueConstraints = {
        @UniqueConstraint(columnNames = {"user_id","blog_id"})
})
public class BlogLike {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    UUID id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id", nullable = false)
    User user;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "blog_id", nullable = false)
    @org.hibernate.annotations.OnDelete(action = org.hibernate.annotations.OnDeleteAction.CASCADE)
    Blog blog;

    LocalDateTime createdAt;

    @PrePersist
    void prePersist(){
        if(createdAt == null){
            createdAt = LocalDateTime.now();
        }
    }
}
```

### 1.3. Thực thể `Bookmark.java` (`src/main/java/com/group/blog/entity/Bookmark.java`)
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
@Table(name="bookmarks", uniqueConstraints = {
        @UniqueConstraint(columnNames = {"user_id", "blog_id"})
})
public class Bookmark {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    UUID id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id", nullable = false)
    User user;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "blog_id", nullable = false)
    @org.hibernate.annotations.OnDelete(action = org.hibernate.annotations.OnDeleteAction.CASCADE)
    Blog blog;

    LocalDateTime createdAt;

    @PrePersist
    void prePersist(){
        if(createdAt == null){
            createdAt = LocalDateTime.now();
        }
    }
}
```

---

## 2. GIẢI THÍCH CHI TIẾT CÁC ĐIỂM SÁNG TRONG THIẾT KẾ CODE

### 2.1. Thiết kế Mô hình Cây Bình luận (Self-Referencing / Nested Comments)
```java
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "parent_id")
    Comment parent;

    @OneToMany(mappedBy = "parent", cascade = CascadeType.ALL, orphanRemoval = true)
    @OrderBy("createdAt ASC")
    List<Comment> replies;
```
- **Bản chất vấn đề**: Trên mạng xã hội (như Facebook hay Reddit), khi một người bình luận vào bài viết thì đó là bình luận gốc (`parent = null`). Khi một người khác bấm nút **"Trả lời" (Reply)** vào bình luận đó, thì bình luận mới tạo ra sẽ trỏ ngược lại bình luận trước thông qua trường `parent_id`.
- Kỹ thuật này gọi là **Thực thể tự tham chiếu (Self-Referencing Entity)**: Cùng trong một bảng `comments`, một dòng có thể vừa là cha của dòng khác, vừa là con của dòng khác nữa.
- **`orphanRemoval = true`**: Nếu xóa một bình luận cha, toàn bộ các câu trả lời con bên dưới cũng sẽ tự động bị xóa theo, không để lại dữ liệu rác.
- **`@OrderBy("createdAt ASC")`**: Tự động sắp xếp các câu trả lời con theo thứ tự thời gian tăng dần (ai bình luận trước thì hiện lên trước).

---

### 2.2. Đánh chỉ mục (Indexes) để tăng tốc độ truy vấn
```java
@Table(name="comments", indexes = {
        @Index(name="idx_comment_blog", columnList="blog_id"),
        @Index(name="idx_comment_parent", columnList="parent_id")
})
```
- Khi bài viết có hàng ngàn bình luận, nếu tìm kiếm bình luận theo `blog_id` hoặc `parent_id` mà không có chỉ mục, CSDL sẽ phải quét toàn bộ bảng từ trên xuống dưới (Full Table Scan).
- Bằng cách đánh `@Index`, CSDL tạo sẵn cây chỉ mục B-Tree, giúp việc tải bình luận của bài viết diễn ra tức thì trong vài mili-giây.

---

### 2.3. Chống Like và Bookmark trùng lặp bằng `@UniqueConstraint`
```java
@Table(name="blog_likes", uniqueConstraints = {
        @UniqueConstraint(columnNames = {"user_id","blog_id"})
})
```
- **Tại sao phải có ràng buộc này?**:
  - Một người dùng chỉ được bấm Like hoặc Bookmark một bài viết đúng 1 lần.
  - Ràng buộc `uniqueConstraints` ở tầng Database đảm bảo cặp giá trị `(user_id, blog_id)` là duy nhất. Kể cả khi người dùng mở nhiều tab trên trình duyệt hoặc dùng bot gửi hàng chục request cùng lúc, Database cũng sẽ chặn đứng mọi hành vi spam trùng lặp.

---

### 2.4. Xóa dây chuyền từ tầng CSDL: `@OnDelete(action = OnDeleteAction.CASCADE)`
```java
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "blog_id", nullable = false)
    @org.hibernate.annotations.OnDelete(action = org.hibernate.annotations.OnDeleteAction.CASCADE)
    Blog blog;
```
- **Sự khác biệt cực kỳ quan trọng**:
  - `cascade = CascadeType.REMOVE` (của JPA): Hibernate phải tự chạy câu lệnh `SELECT` để lôi hết các comment/like lên bộ nhớ JVM rồi mới phát lệnh `DELETE` từng cái một. Cách này rất chậm khi dữ liệu lớn.
  - `@OnDelete(action = OnDeleteAction.CASCADE)` (của Hibernate): Sinh trực tiếp câu lệnh `ON DELETE CASCADE` ở mức định nghĩa bảng trong Database (Foreign Key Constraint). Khi một bài Blog bị xóa, Database Engine (H2 / MySQL) sẽ tự động dọn sạch tất cả Comment, Like, Bookmark liên quan chỉ bằng một nhát búa ở mức phần cứng, tốc độ nhanh gấp hàng chục lần!

---

## 3. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN VỀ BÌNH LUẬN & TƯƠNG TÁC

### Câu 1: Em hãy giải thích cách hệ thống hiển thị bình luận và các phản hồi con (Replies) ra giao diện?
- **Trả lời**:
  > "Thưa thầy/cô:
  > - Khi tải trang bài viết, hệ thống gọi API `GET /blogs/{id}/comments`.
  > - Ở tầng Repository, hàm `findByBlogIdAndParentIsNullOrderByCreatedAtDesc()` sẽ chỉ lấy ra các **bình luận gốc cấp cao nhất** (tức là những comment có `parent_id IS NULL`).
  > - Mỗi bình luận gốc này lại sở hữu danh sách `@OneToMany List<Comment> replies`. Khi chuyển đổi qua DTO, danh sách các phản hồi con này được đính kèm vào mảng `replies` bên trong JSON.
  > - Phía JavaScript (file `posts.js`) chỉ cần duyệt qua mảng này và render giao diện thụt lề vào trong 1 cấp để hiển thị cây bình luận rất trực quan."

### Câu 2: Ràng buộc `@UniqueConstraint(columnNames = {"user_id","blog_id"})` trong `BlogLike` giải quyết bài toán gì?
- **Trả lời**:
  > "Thưa thầy/cô, ràng buộc này giải quyết bài toán **Chống gian lận lượt Thích (Concurrency / Duplicate Like)**:
  > Giả sử một người dùng cố tình click nút Thích liên tục hoặc dùng mã script gửi 10 request POST đồng thời lên server. Nếu không có ràng buộc này ở tầng Database, có thể hệ thống sẽ bị lỗi 'Race Condition' và chèn 10 bản ghi like cho cùng 1 người.
  > Nhờ có `@UniqueConstraint`, Database đảm bảo chỉ có duy nhất 1 bản ghi được chấp nhận. Bất kỳ request thứ hai nào trùng `(user_id, blog_id)` sẽ bị Database từ chối ngay lập tức."
