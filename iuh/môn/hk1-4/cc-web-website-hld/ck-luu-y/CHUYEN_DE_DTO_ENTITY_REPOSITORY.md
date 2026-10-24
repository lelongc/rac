# 📘 CHUYÊN ĐỀ ĐẶC BIỆT: TẦNG THỰC THỂ (ENTITY), TRUY XUẤT DỮ LIỆU (REPOSITORY) & ĐỐI TƯỢNG TRUYỀN DỮ LIỆU (DTO)

## DỰ ÁN BÁO CÁO CUỐI KỲ: NỀN TẢNG BLOG & VIẾT BÀI ĐA NGƯỜI DÙNG (`blog-website-main`)
**Môn học:** Công nghệ Web và Website hướng dữ liệu — ĐH Công Nghiệp TP.HCM (IUH)  
**Giảng viên:** Thầy Trương Bá Phúc  
**Nhóm sinh viên thực hiện:**
1. Hoàng Đại Dương — 24743991
2. Nguyễn Trung Dũng — 24000905
3. Lê Thành Long — 23630851

---

# 📌 MỤC LỤC CHUYÊN ĐỀ

- [PHẦN I: TẦNG THỰC THỂ (ENTITY PACKAGE - TOÀN BỘ 10 ENTITIES)](#phần-i-tầng-thực-thể-entity-package---toàn-bộ-10-entities)
  - [1. User.java (Bảng `users`)](#1-userjava-bảng-users)
  - [2. Blog.java (Bảng `blogs`)](#2-blogjava-bảng-blogs)
  - [3. Comment.java (Bảng `comments`)](#3-commentjava-bảng-comments)
  - [4. BlogLike.java (Bảng `blog_likes`)](#4-bloglikejava-bảng-blog_likes)
  - [5. BlogView.java (Bảng `blog_views`)](#5-blogviewjava-bảng-blog_views)
  - [6. Bookmark.java (Bảng `bookmarks`)](#6-bookmarkjava-bảng-bookmarks)
  - [7. Category.java (Bảng `categories`)](#7-categoryjava-bảng-categories)
  - [8. Tag.java (Bảng `tags`)](#8-tagjava-bảng-tags)
  - [9. UserFollow.java (Bảng `user_follows`)](#9-userfollowjava-bảng-user_follows)
  - [10. Notification.java (Bảng `notifications`)](#10-notificationjava-bảng-notifications)
- [PHẦN II: TẦNG TRUY XUẤT DỮ LIỆU (REPOSITORY PACKAGE - TOÀN BỘ 10 REPOSITORIES)](#phần-ii-tầng-truy-xuất-dữ-liệu-repository-package---toàn-bộ-10-repositories)
  - [1. BlogRepository.java (Tâm điểm JPQL phức tạp)](#1-blogrepositoryjava-tâm-điểm-jpql-phức-tạp)
  - [2. UserRepository.java](#2-userrepositoryjava)
  - [3. CategoryRepository.java](#3-categoryrepositoryjava)
  - [4. TagRepository.java](#4-tagrepositoryjava)
  - [5. CommentRepository.java](#5-commentrepositoryjava)
  - [6. BlogLikeRepository.java](#6-bloglikerepositoryjava)
  - [7. BlogViewRepository.java](#7-blogviewrepositoryjava)
  - [8. BookmarkRepository.java](#8-bookmarkrepositoryjava)
  - [9. UserFollowRepository.java](#9-userfollowrepositoryjava)
  - [10. NotificationRepository.java](#10-notificationrepositoryjava)
- [PHẦN III: TẦNG ĐỐI TƯỢNG TRUYỀN DỮ LIỆU (DTO PACKAGE - TOÀN BỘ 20 DTOS)](#phần-iii-tầng-đối-tượng-truyền-dữ-liệu-dto-package---toàn-bộ-20-dtos)
  - [1. Tại sao phải dùng DTO mà không dùng trực tiếp Entity?](#1-tại-sao-phải-dùng-dto-mà-không-dùng-trực-tiếp-entity)
  - [2. Danh sách 10 Request DTOs (Tiếp nhận & Xác thực dữ liệu vào)](#2-danh-sách-10-request-dtos-tiếp-nhận--xác-thực-dữ-liệu-vào)
  - [3. Danh sách 10 Response DTOs (Đóng gói dữ liệu trả ra Client)](#3-danh-sách-10-response-dtos-đóng-gói-dữ-liệu-trả-ra-client)
- [PHẦN IV: BỘ CÂU HỎI VẤN ĐÁP LÝ THUYẾT ĐỈNH CAO VỀ DTO, ENTITY & REPOSITORY](#phần-iv-bộ-câu-hỏi-vấn-đáp-lý-thuyết-đỉnh-cao-về-dto-entity--repository)

---

# PHẦN I: TẦNG THỰC THỂ (ENTITY PACKAGE - TOÀN BỘ 10 ENTITIES)

Tầng Entity đại diện cho các bảng dữ liệu trong CSDL MySQL. Mọi class đều nằm trong package `com.group.blog.entity` và tuân thủ các chuẩn mực của JPA (Jakarta Persistence API) & Hibernate ORM.

---

### 1. `User.java` (Bảng `users`)
- **Vị trí**: `src/main/java/com/group/blog/entity/User.java`
- **Mã nguồn chi tiết**:
  ```java
  @Entity
  @Getter @Setter @Builder
  @NoArgsConstructor @AllArgsConstructor
  @FieldDefaults(level = AccessLevel.PRIVATE)
  @Table(name = "users")
  public class User {
      @Id
      @GeneratedValue(strategy = GenerationType.UUID)
      UUID id;

      @Column(nullable = false, unique = true, length = 100)
      String username;

      @Column(nullable = false, length = 255)
      String password;

      @Column(unique = true, length = 255)
      String email;

      String bio;
      String avatarUrl;
      LocalDateTime createdAt;

      @ElementCollection(fetch = FetchType.EAGER)
      @CollectionTable(
              name = "user_roles",
              joinColumns = @JoinColumn(name = "user_id"),
              uniqueConstraints = @UniqueConstraint(columnNames = {"user_id", "role"})
      )
      @Column(name = "role")
      @Builder.Default
      Set<String> roles = new HashSet<>();

      @OneToMany(mappedBy = "author", cascade = CascadeType.ALL)
      @Builder.Default
      List<Blog> blogs = new ArrayList<>();

      @PrePersist
      void prePersist() {
          if (createdAt == null) createdAt = LocalDateTime.now();
      }
  }
  ```
- **Phân tích từng dòng & Lý thuyết cốt lõi**:
  - `@Entity`: Báo cho Hibernate biết class này tương ứng với một bảng trong CSDL quan hệ.
  - `@Table(name = "users")`: Đặt tên bảng là `users` (tránh từ khóa bảo lưu `user` trong SQL).
  - `@Id @GeneratedValue(strategy = GenerationType.UUID) UUID id`: Định dạng khóa chính **UUID phiên bản 4 (128-bit ngẫu nhiên)**. Giúp chống lại tấn công vét cạn (ID Enumeration Attack), không để lộ số lượng người dùng thực tế và an toàn tuyệt đối khi phân tán dữ liệu.
  - `@Column(nullable = false, unique = true, length = 100) String username`: Tên đăng nhập bắt buộc duy nhất, không rỗng, giới hạn 100 ký tự.
  - `@Column(nullable = false, length = 255) String password`: Lưu chuỗi mã hóa băm BCrypt dài 60 ký tự.
  - `@ElementCollection(fetch = FetchType.EAGER)` & `@CollectionTable`:
    - Tạo bảng phụ `user_roles` nối với bảng `users` qua `user_id`.
    - Dùng `FetchType.EAGER`: Khi Hibernate nạp User lên RAM, nó sẽ thực hiện truy vấn nạp luôn danh sách Roles để Spring Security kiểm tra quyền hạn (`ROLE_USER`, `ROLE_ADMIN`) tức thì khi đăng nhập.
    - `@UniqueConstraint(columnNames = {"user_id", "role"})`: Chặn việc một user bị gán trùng một vai trò 2 lần.
  - `@OneToMany(mappedBy = "author", cascade = CascadeType.ALL)`: Quan hệ 1-N với `Blog`. Một user viết được nhiều blog. `mappedBy = "author"` chỉ rõ biến `author` bên Entity `Blog` là bên nắm giữ khóa ngoại (Foreign Key).
  - `@PrePersist`: Callback lifecycle của JPA tự động điền `createdAt = LocalDateTime.now()` trước khi bản ghi được `INSERT` xuống MySQL.

---

### 2. `Blog.java` (Bảng `blogs`)
- **Vị trí**: `src/main/java/com/group/blog/entity/Blog.java`
- **Mã nguồn chi tiết**:
  ```java
  @Entity
  @Getter @Setter @Builder
  @NoArgsConstructor @AllArgsConstructor
  @FieldDefaults(level = AccessLevel.PRIVATE)
  @Table(name = "blogs")
  public class Blog {
      @Id
      @GeneratedValue(strategy = GenerationType.UUID)
      UUID id;

      @Column(nullable = false)
      String title;

      String banner;

      @Column(columnDefinition = "TEXT")
      String description;

      @Column(columnDefinition = "LONGTEXT")
      String content;

      boolean draft;

      @Column(columnDefinition = "LONGTEXT")
      String draftContent;

      @Column(columnDefinition = "LONGTEXT")
      String draftBanner;

      LocalDateTime publishedAt;
      LocalDateTime updatedAt;
      LocalDateTime createdAt;

      @ManyToOne(fetch = FetchType.LAZY)
      @JoinColumn(name = "author_id")
      User author;

      @ManyToOne(fetch = FetchType.LAZY)
      @JoinColumn(name = "category_id")
      Category category;

      @ManyToMany
      @JoinTable(
              name = "blog_tags",
              joinColumns = @JoinColumn(name = "blog_id"),
              inverseJoinColumns = @JoinColumn(name = "tag_id"),
              uniqueConstraints = @UniqueConstraint(columnNames = {"blog_id", "tag_id"})
      )
      @Builder.Default
      Set<Tag> tags = new HashSet<>();

      @PrePersist
      void prePersist() {
          createdAt = LocalDateTime.now();
          if (!draft && publishedAt == null) publishedAt = LocalDateTime.now();
      }

      @PreUpdate
      void preUpdate() {
          updatedAt = LocalDateTime.now();
      }
  }
  ```
- **Phân tích từng dòng & Điểm nhấn kiến trúc**:
  - `columnDefinition = "LONGTEXT"`: Cho các trường `content`, `draftContent`, `draftBanner`. Kiểu `LONGTEXT` trong MySQL lưu trữ chuỗi văn bản tối đa lên tới **4GB**, cho phép chứa nội dung HTML phong phú, hình ảnh base64 hoặc định dạng Markdown siêu dài.
  - **Cơ chế lưu nháp kép (Drafting System)**:
    - Cờ `draft = true/false`: Phân biệt bài nháp chưa xuất bản và bài đã công khai.
    - `draftContent` & `draftBanner`: Khi bài viết đã xuất bản (`draft = false`) nhưng tác giả muốn chỉnh sửa, nội dung mới sẽ được lưu vào `draftContent`. Độc giả bên ngoài vẫn đọc nội dung cũ ở cột `content`. Khi tác giả bấm "Publish", nội dung từ `draftContent` mới đè sang `content`.
  - `@ManyToOne(fetch = FetchType.LAZY)`: Quan hệ nhiều bài viết thuộc về một tác giả (`author_id`) và một danh mục (`category_id`). Tải kiểu `LAZY` (lười biếng) để Hibernate không tự động query bảng `users` hay `categories` nếu không cần dùng đến, tránh lãng phí RAM và băng thông kết nối CSDL.
  - `@ManyToMany` & `@JoinTable`: Tạo bảng trung gian `blog_tags` kết nối `blog_id` và `tag_id`. Có `@UniqueConstraint` chống gắn trùng thẻ tag.
  - `@PreUpdate`: Tự động cập nhật `updatedAt = LocalDateTime.now()` mỗi khi gọi lệnh `UPDATE`.

---

### 3. `Comment.java` (Bảng `comments`)
- **Vị trí**: `src/main/java/com/group/blog/entity/Comment.java`
- **Mã nguồn chi tiết**:
  ```java
  @Entity
  @Getter @Setter @Builder
  @NoArgsConstructor @AllArgsConstructor
  @FieldDefaults(level = AccessLevel.PRIVATE)
  @Table(name = "comments", indexes = {
          @Index(name = "idx_comment_blog", columnList = "blog_id"),
          @Index(name = "idx_comment_parent", columnList = "parent_id")
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

      @ManyToOne(fetch = FetchType.LAZY)
      @JoinColumn(name = "parent_id")
      Comment parent;

      @OneToMany(mappedBy = "parent", cascade = CascadeType.ALL, orphanRemoval = true)
      @OrderBy("createdAt ASC")
      List<Comment> replies;

      @Column(columnDefinition = "TEXT")
      String content;

      LocalDateTime createdAt;

      @PrePersist
      void prePersist() {
          if (createdAt == null) createdAt = LocalDateTime.now();
      }
  }
  ```
- **Phân tích kỹ thuật chuyên sâu**:
  - `indexes = { @Index(name="idx_comment_blog", columnList="blog_id"), @Index(...) }`: Tạo chỉ mục **B-Tree Index** trên 2 cột `blog_id` và `parent_id`. Giúp việc lấy danh sách bình luận của bài viết đạt độ phức tạp tìm kiếm $O(\log N)$, phản hồi tức thì kể cả khi có hàng triệu bình luận.
  - **Quan hệ Tự tham chiếu (Self-Referencing Entity)**:
    - `parent`: Trỏ về chính Entity `Comment` cha nếu đây là bình luận trả lời (reply).
    - `replies`: `@OneToMany(mappedBy = "parent")` chứa danh sách bình luận con.
    - `@OrderBy("createdAt ASC")`: Tự động sắp xếp các phản hồi theo thứ tự thời gian tăng dần (ai trả lời trước hiện lên trước).
    - `orphanRemoval = true`: Nếu xóa bình luận cha khỏi CSDL, tất cả bình luận con mồ côi (orphans) sẽ tự động bị xóa sạch.
  - `@OnDelete(action = OnDeleteAction.CASCADE)`: Thiết lập ràng buộc `ON DELETE CASCADE` ở mức DDL của CSDL MySQL. Khi bài blog bị xóa, toàn bộ bình luận của blog đó bị MySQL xóa theo mà không ném lỗi vi phạm khóa ngoại.

---

### 4. `BlogLike.java` (Bảng `blog_likes`)
- **Vị trí**: `src/main/java/com/group/blog/entity/BlogLike.java`
- **Mã nguồn**:
  ```java
  @Entity
  @Getter @Setter @Builder
  @NoArgsConstructor @AllArgsConstructor
  @FieldDefaults(level = AccessLevel.PRIVATE)
  @Table(name = "blog_likes", uniqueConstraints = {
          @UniqueConstraint(columnNames = {"user_id", "blog_id"})
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
      void prePersist() {
          if (createdAt == null) createdAt = LocalDateTime.now();
      }
  }
  ```
- **Điểm chốt**: `@UniqueConstraint(columnNames = {"user_id", "blog_id"})`: Chống hack lượt thích. Một người dùng không bao giờ có thể bấm like một bài viết 2 lần. CSDL sẽ từ chối ngay lập tức nếu có hành vi cố tình chèn trùng.

---

### 5. `BlogView.java` (Bảng `blog_views`)
- **Vị trí**: `src/main/java/com/group/blog/entity/BlogView.java`
- **Mã nguồn**:
  ```java
  @Entity
  @Getter @Setter @Builder
  @NoArgsConstructor @AllArgsConstructor
  @FieldDefaults(level = AccessLevel.PRIVATE)
  @Table(name = "blog_views")
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

      String ipAddress;
      LocalDateTime viewedAt;

      @PrePersist
      void prePersist() {
          if (viewedAt == null) viewedAt = LocalDateTime.now();
      }
  }
  ```
- **Ý nghĩa**: Ghi nhận mỗi lần người dùng bấm vào đọc bài viết. Cho phép `user_id` rỗng (nullable) để phục vụ việc đếm lượt xem từ khách vãng lai chưa đăng nhập.

---

### 6. `Bookmark.java` (Bảng `bookmarks`)
- **Vị trí**: `src/main/java/com/group/blog/entity/Bookmark.java`
- **Mã nguồn**: Tương tự `BlogLike`, có `@UniqueConstraint(columnNames = {"user_id", "blog_id"})` để đảm bảo mỗi bài viết chỉ được người dùng lưu trữ vào mục "Đọc sau" tối đa 1 lần.

---

### 7. `Category.java` (Bảng `categories`)
- **Vị trí**: `src/main/java/com/group/blog/entity/Category.java`
- **Mã nguồn**:
  ```java
  @Entity
  @Getter @Setter @Builder
  @NoArgsConstructor @AllArgsConstructor
  @FieldDefaults(level = AccessLevel.PRIVATE)
  @Table(name = "categories")
  public class Category {
      @Id
      @GeneratedValue(strategy = GenerationType.UUID)
      UUID id;

      @Column(nullable = false, unique = true, length = 100)
      String name;

      @OneToMany(mappedBy = "category", cascade = CascadeType.ALL)
      @Builder.Default
      List<Blog> blogs = new ArrayList<>();
  }
  ```
- **Ý nghĩa**: Bảng danh mục chuyên mục (`Technology`, `Programming`...). Cột `name` là `unique`. Quan hệ 1-N với `Blog`.

---

### 8. `Tag.java` (Bảng `tags`)
- **Vị trí**: `src/main/java/com/group/blog/entity/Tag.java`
- **Mã nguồn**:
  ```java
  @Entity
  @Getter @Setter @Builder
  @NoArgsConstructor @AllArgsConstructor
  @FieldDefaults(level = AccessLevel.PRIVATE)
  @Table(name = "tags")
  public class Tag {
      @Id
      @GeneratedValue(strategy = GenerationType.UUID)
      UUID id;

      @Column(nullable = false, unique = true, length = 100)
      String name;

      @ManyToMany(mappedBy = "tags")
      @Builder.Default
      Set<Blog> blogs = new HashSet<>();
  }
  ```
- **Ý nghĩa**: Quản lý thẻ từ khóa bài viết (`Java`, `SpringBoot`...). `mappedBy = "tags"` chỉ rõ bảng trung gian `blog_tags` được định nghĩa bên Entity `Blog`.

---

### 9. `UserFollow.java` (Bảng `user_follows`)
- **Vị trí**: `src/main/java/com/group/blog/entity/UserFollow.java`
- **Mã nguồn**:
  ```java
  @Entity
  @Getter @Setter @Builder
  @NoArgsConstructor @AllArgsConstructor
  @FieldDefaults(level = AccessLevel.PRIVATE)
  @Table(name = "user_follows", uniqueConstraints = {
          @UniqueConstraint(columnNames = {"follower_id", "following_id"})
  })
  public class UserFollow {
      @Id
      @GeneratedValue(strategy = GenerationType.UUID)
      UUID id;

      @ManyToOne(fetch = FetchType.LAZY)
      @JoinColumn(name = "follower_id", nullable = false)
      User follower;

      @ManyToOne(fetch = FetchType.LAZY)
      @JoinColumn(name = "following_id", nullable = false)
      User following;

      LocalDateTime createdAt;

      @PrePersist
      void prePersist() {
          if (createdAt == null) createdAt = LocalDateTime.now();
      }
  }
  ```
- **Ý nghĩa**: Thiết lập quan hệ Mạng Xã Hội giữa 2 tài khoản: `follower` (người nhấn theo dõi) và `following` (tác giả được theo dõi). Ràng buộc duy nhất chặn việc theo dõi lặp lại.

---

### 10. `Notification.java` (Bảng `notifications`)
- **Vị trí**: `src/main/java/com/group/blog/entity/Notification.java`
- **Mã nguồn**:
  ```java
  @Entity
  @Getter @Setter @Builder
  @NoArgsConstructor @AllArgsConstructor
  @FieldDefaults(level = AccessLevel.PRIVATE)
  @Table(name = "notifications", indexes = {
          @Index(name = "idx_notif_user", columnList = "user_id")
  })
  public class Notification {
      @Id
      @GeneratedValue(strategy = GenerationType.UUID)
      UUID id;

      @ManyToOne(fetch = FetchType.LAZY)
      @JoinColumn(name = "user_id", nullable = false)
      User user;

      @Column(nullable = false)
      String message;

      String targetUrl;

      @Builder.Default
      boolean isRead = false;

      LocalDateTime createdAt;

      @Column(nullable = false)
      String type;

      @PrePersist
      void prePersist() {
          if (createdAt == null) createdAt = LocalDateTime.now();
      }
  }
  ```
- **Ý nghĩa**: Bảng chuông thông báo cá nhân. Đánh chỉ mục trên `user_id`. `type` gồm `LIKE`, `COMMENT`, `REPLY`, `FOLLOW`. `targetUrl` lưu link chuyển hướng kèm param để tự động cuộn đến bình luận khi bấm.

---

# PHẦN II: TẦNG TRUY XUẤT DỮ LIỆU (REPOSITORY PACKAGE - TOÀN BỘ 10 REPOSITORIES)

Toàn bộ các interface kế thừa `JpaRepository<Entity, UUID>` của Spring Data JPA.  
Tại thời điểm ứng dụng khởi chạy, Spring Data sử dụng cơ chế **JDK Dynamic Proxy** để tự động sinh ra một class thực thi (Implementation) nằm trên RAM, cung cấp sẵn các phương thức `save()`, `findById()`, `findAll()`, `deleteById()`, `count()`.

---

### 1. `BlogRepository.java` (Tâm điểm JPQL phức tạp)
- **Vị trí**: `src/main/java/com/group/blog/repository/BlogRepository.java`
- **Các phương thức & Phân tích truy vấn JPQL**:

#### Truy vấn 1: Lấy danh sách bài viết trang chủ kèm tổng Like, View, Comment
```java
@Query("""
   SELECT b, COUNT(DISTINCT v.id), COUNT(DISTINCT l.id), COUNT(DISTINCT c.id)
   FROM Blog b
   LEFT JOIN BlogLike l ON l.blog = b
   LEFT JOIN BlogView  v ON v.blog = b
   LEFT JOIN Comment  c ON c.blog = b
   WHERE b.draft = false
   GROUP BY b
   ORDER BY b.publishedAt DESC
""")
List<Object[]> findAllBlogsWithCounts();
```
- **Phân tích từng từ khóa**:
  - `FROM Blog b`: Viết hoa chữ `Blog`, truy vấn trực tiếp trên Entity Java chứ không phải tên bảng trong MySQL.
  - `LEFT JOIN`: Bắt buộc dùng `LEFT JOIN` thay vì `INNER JOIN`. Vì nếu một bài viết mới đăng chưa có like, view hay comment nào thì kết quả JOIN bảng like/view/comment sẽ rỗng. Nếu dùng `INNER JOIN`, bài viết đó sẽ bị triệt tiêu và biến mất khỏi trang chủ! Dùng `LEFT JOIN` giúp bài viết luôn được giữ lại với count = 0.
  - `COUNT(DISTINCT v.id)`: **Cực kỳ quan trọng để chống lỗi Tích Đề-các (Cartesian Product)**. Khi JOIN 3 bảng 1-N cùng lúc, SQL sẽ nhân chéo số dòng. Nếu bài viết có 2 view, 3 like, 4 comment $\rightarrow$ số dòng sinh ra là $2 \times 3 \times 4 = 24$ dòng! Nếu dùng `COUNT(v.id)` thông thường thì số view sẽ bị đếm sai thành 24. `COUNT(DISTINCT v.id)` bảo đảm chỉ đếm các ID view duy nhất, cho kết quả chính xác 100%.
  - `GROUP BY b`: Gom nhóm dữ liệu theo từng đối tượng bài viết.
  - `ORDER BY b.publishedAt DESC`: Sắp xếp các bài viết xuất bản mới nhất lên trên đầu.

#### Truy vấn 2 & 3: Lọc bài viết theo Chuyên mục & Thẻ Tag
```java
@Query("""
   SELECT b, COUNT(DISTINCT v.id), COUNT(DISTINCT l.id), COUNT(DISTINCT c.id)
   FROM Blog b
   LEFT JOIN BlogLike l ON l.blog = b
   LEFT JOIN BlogView v ON v.blog = b
   LEFT JOIN Comment c ON c.blog = b
   WHERE b.category.id = :categoryId AND b.draft = false
   GROUP BY b
   ORDER BY b.publishedAt DESC
""")
List<Object[]> findBlogsByCategoryIdWithCounts(@Param("categoryId") UUID categoryId);

@Query("""
   SELECT b, COUNT(DISTINCT v.id), COUNT(DISTINCT l.id), COUNT(DISTINCT c.id)
   FROM Blog b
   JOIN b.tags t
   LEFT JOIN BlogLike l ON l.blog = b
   LEFT JOIN BlogView v ON v.blog = b
   LEFT JOIN Comment c ON c.blog = b
   WHERE t.id = :tagId AND b.draft = false
   GROUP BY b
   ORDER BY b.publishedAt DESC
""")
List<Object[]> findBlogsByTagIdWithCounts(@Param("tagId") UUID tagId);
```

#### Truy vấn 4: Tìm kiếm theo từ khóa không phân biệt hoa thường
```java
@Query("""
   SELECT b, COUNT(DISTINCT v.id), COUNT(DISTINCT l.id), COUNT(DISTINCT c.id)
   FROM Blog b
   LEFT JOIN BlogLike l ON l.blog = b
   LEFT JOIN BlogView v ON v.blog = b
   LEFT JOIN Comment c ON c.blog = b
   WHERE LOWER(b.title) LIKE TRIM(LOWER(CONCAT('%', :keyword, '%'))) AND b.draft = false
   GROUP BY b
   ORDER BY b.publishedAt DESC
""")
List<Object[]> searchBlogsByKeywordWithCounts(@Param("keyword") String keyword);
```
- Dùng `CONCAT('%', :keyword, '%')` kết hợp `LOWER()` và `TRIM()` để tìm kiếm linh hoạt chuỗi con trong tiêu đề bài viết.

#### Các phương thức suy diễn tự động (Derived Query Methods):
- `List<Blog> findTop5ByTitleContainingIgnoreCaseAndDraftIsFalse(String title);`: Tự động dịch thành câu SQL tìm 5 bài viết có tiêu đề chứa từ khóa để làm danh sách gợi ý khi gõ phím.
- `List<Blog> findTop5ByDraftFalseOrderByCreatedAtDesc();`: Lấy 5 bài viết mới nhất phục vụ Dashboard Admin.
- `long countByDraftFalse();`: Đếm tổng số bài viết đã xuất bản công khai.

---

### 2. `UserRepository.java`
- `boolean existsByUsername(String username);`: Kiểm tra trùng lặp tài khoản khi đăng ký.
- `Optional<User> findByUsername(String username);`: Tìm người dùng theo username để xác thực JWT.
- `boolean existsByEmail(String email);` & `Optional<User> findByEmail(String email);`.

---

### 3. `CategoryRepository.java`
- `boolean existsByName(String name);`: Kiểm tra trùng tên danh mục.
- Truy vấn đếm số lượng bài viết theo danh mục:
  ```java
  @Query("""
   SELECT c, COUNT(b.id)
   FROM Category c
   LEFT JOIN c.blogs b
   GROUP BY c
  """)
  List<Object[]> findAllCategoriesWithPostCount();
  ```

---

### 4. `TagRepository.java`
- `Optional<Tag> findByName(String name);`: Tìm thẻ tag khi người dùng gán thẻ cho bài viết.
- Truy vấn đếm số bài viết theo từng tag:
  ```java
  @Query("""
   SELECT t, COUNT(b.id)
   FROM Tag t
   LEFT JOIN t.blogs b
   GROUP BY t
  """)
  List<Object[]> findAllTagsWithPostCount();
  ```

---

### 5. `CommentRepository.java`
- `long countByBlogId(UUID blogId);`: Đếm tổng số bình luận của một bài viết.
- `List<Comment> findByBlogIdAndParentIsNullOrderByCreatedAtDesc(UUID blogId);`: **Lấy toàn bộ bình luận gốc (Root Comments)** của bài viết (bình luận không có cha `parent IS NULL`), sắp xếp thời gian tạo giảm dần. Các reply con sẽ được nạp qua quan hệ `getReplies()`.

---

### 6. `BlogLikeRepository.java`
- `long countByBlogId(UUID blogId);`: Đếm tổng số like của bài viết.
- `boolean existsByBlogIdAndUserUsername(UUID blogId, String username);`: Kiểm tra xem người dùng hiện tại đã like bài viết này chưa.
- `Optional<BlogLike> findByBlogIdAndUserUsername(UUID blogId, String username);`: Tìm bản ghi like để phục vụ chức năng Unlike (bỏ like).

---

### 7. `BlogViewRepository.java`
- `long countByBlogId(UUID blogId);`: Đếm tổng số lượt xem bài viết.

---

### 8. `BookmarkRepository.java`
- `boolean existsByBlogIdAndUserUsername(UUID blogId, String username);`: Kiểm tra bài viết đã được lưu chưa.
- `List<Bookmark> findByUserUsernameOrderByCreatedAtDesc(String username);`: Lấy danh sách toàn bộ bài viết đã đánh dấu đọc sau của user hiện tại.

---

### 9. `UserFollowRepository.java`
- `long countByFollowing(User following);`: Đếm số người đang theo dõi tác giả này (Followers).
- `long countByFollower(User follower);`: Đếm số người mà tác giả này đang theo dõi (Following).
- `Optional<UserFollow> findByFollowerAndFollowing(User follower, User following);`: Lấy bản ghi follow để hủy theo dõi (Unfollow).
- `boolean existsByFollowerUsernameAndFollowing(String followerUsername, User following);`: Kiểm tra trạng thái follow.

---

### 10. `NotificationRepository.java`
- `List<Notification> findByUserUsernameOrderByCreatedAtDesc(String username);`: Lấy toàn bộ thông báo của tài khoản đang đăng nhập, xếp mới nhất lên trước.

---

# PHẦN III: TẦNG ĐỐI TƯỢNG TRUYỀN DỮ LIỆU (DTO PACKAGE - TOÀN BỘ 20 DTOS)

DTO (Data Transfer Object) là mẫu thiết kế (Design Pattern) dùng để mang dữ liệu qua lại giữa Client (Trình duyệt) và Server (Controller & Service).

---

### 1. Tại sao phải dùng DTO mà không dùng trực tiếp Entity?

Khi Thầy Phúc hỏi: *"Tại sao phải tạo Request DTO và Response DTO riêng mà không dùng luôn Entity cho nhanh?"*, bạn hãy trả lời bằng 4 lý do sống còn:
1. **Bảo mật — Ngăn chặn tấn công gán đè (Mass Assignment / Over-posting Vulnerability)**:
   * Nếu dùng trực tiếp Entity `User` làm tham số `@RequestBody`, hacker có thể gửi kèm JSON `{"roles": ["ADMIN"]}` hoặc `{"id": "..."}` để tự thăng cấp tài khoản của mình lên Admin. Dùng `UserCreatetionRequest` chỉ có đúng 2 trường `username` và `password`, hoàn toàn vô hiệu hóa kiểu tấn công này.
2. **Ẩn giấu thông tin nhạy cảm**:
   * Entity `User` chứa trường `password`. Nếu trả thẳng Entity `User` ra ngoài API, dù là chuỗi băm thì hacker vẫn có thể thu thập để tấn công từ điển (Dictionary Attack). Dùng `UserResponse` loại bỏ hoàn toàn trường password.
3. **Tránh lỗi vòng lặp đệ quy vô tận khi tuần tự hóa JSON (Circular Dependency Serialization)**:
   * Entity có quan hệ 2 chiều: `User` chứa danh sách `List<Blog>`, mỗi `Blog` lại chứa thuộc tính `User author`. Nếu dùng Jackson parse thẳng Entity ra JSON, nó sẽ lặp vô tận: User $\rightarrow$ Blog $\rightarrow$ User $\rightarrow$ Blog... làm tràn bộ nhớ và sập máy chủ (`StackOverflowError`). DTO cắt đứt mối quan hệ vòng lặp này.
4. **Tối ưu băng thông mạng**:
   * DTO chỉ mang đúng những trường dữ liệu mà màn hình đó cần hiển thị, kết hợp annotation `@JsonInclude(JsonInclude.Include.NON_NULL)` loại bỏ các trường null, giúp dung lượng gói tin truyền tải cực nhẹ và nhanh.

---

### 2. Danh sách 10 Request DTOs (Tiếp nhận & Xác thực dữ liệu vào)

Nằm trong package `com.group.blog.dto.request`:

1. **`ApiResponse<T>.java` (Chuẩn hóa phản hồi API toàn hệ thống)**:
   - Các trường: `int code = 1000` (mã thành công mặc định), `String message`, `T result` (chứa dữ liệu bất kỳ dạng generic).
   - `@JsonInclude(JsonInclude.Include.NON_NULL)`: Nếu `result` hoặc `message` là null thì Jackson không xuất hiện thuộc tính đó trong chuỗi JSON.
2. **`UserCreatetionRequest.java`**:
   - `@NotBlank(message = "USERNAME_REQUIRED") @Size(min = 3, message = "USERNAME_INVALID") String username;`
   - `@NotBlank(message = "PASSWORD_REQUIRED") @Size(min = 6, message = "INVALID_PASSWORD") String password;`
   - Dùng annotation Jakarta Validation để kiểm tra tính hợp lệ dữ liệu ngay tại Controller trước khi đưa vào Service.
3. **`UserUpdateRequest.java`**:
   - Các trường cập nhật hồ sơ: `String email`, `String bio`, `String avatarUrl`, `Set<String> roles` (dành cho Admin phân quyền).
4. **`PasswordChangeRequest.java`**:
   - `String oldPassword`, `String newPassword`, `String confirmPassword`.
5. **`AuthenticationRequest.java`**:
   - `String username`, `String password` phục vụ đăng nhập.
6. **`IntrospectRequest.java`**:
   - `String token`: Gửi chuỗi JWT lên để máy chủ xác thực còn hiệu lực hay không.
7. **`BlogCreationRequest.java`**:
   - `String title`, `String banner`, `String description`, `String content`, `boolean draft`, `UUID categoryId`, `Set<String> tags`.
8. **`BlogUpdateRequest.java`**:
   - Các trường cập nhật bài viết tương tự `BlogCreationRequest`.
9. **`CategoryRequest.java`**:
   - `String name`: Tên chuyên mục hoặc tên thẻ tag khi tạo mới/chỉnh sửa.
10. **`CommentRequest.java`**:
    - `String content`: Nội dung bình luận.
    - `UUID parentId`: ID của bình luận cha nếu là reply (null nếu là bình luận gốc).

---

### 3. Danh sách 10 Response DTOs (Đóng gói dữ liệu trả ra Client)

Nằm trong package `com.group.blog.dto.response`:

1. **`BlogResponse.java` (DTO quan trọng nhất hệ thống)**:
   - Thông tin cơ bản: `UUID id`, `String title`, `String slug`, `String banner`, `String description`, `String content`.
   - Trạng thái nháp: `boolean draft`, `String draftContent`, `String draftBanner`.
   - Số liệu thống kê tương tác: `long totalLikes`, `long totalComments`, `long totalReads`.
   - Trạng thái của phiên người dùng hiện tại: `boolean isLikedByCurrentUser`, `boolean isBookmarkedByCurrentUser`.
   - Đối tượng lồng nhau: `UserResponse author`, `CategoryResponse category`, `Set<TagResponse> tags`.
   - Thời gian: `LocalDateTime publishedAt`, `updatedAt`, `createdAt`.
2. **`UserResponse.java`**:
   - `UUID id`, `String username`, `String email`, `String bio`, `String avatarUrl`, `Set<String> roles`.
   - Dữ liệu mạng xã hội: `long followerCount`, `long followingCount`, `boolean isFollowedByCurrentUser`.
3. **`AuthenticationResponse.java`**:
   - `String token`: Chuỗi JWT cấp cho client sau khi đăng nhập thành công.
   - `boolean authenticated`.
4. **`IntrospectResponse.java`**:
   - `boolean valid`: Kết quả kiểm tra token (true nếu chữ ký hợp lệ và chưa hết hạn).
5. **`CommentResponse.java`**:
   - `UUID id`, `String content`, `LocalDateTime createdAt`, `UserResponse user`, `List<CommentResponse> replies` (cấu trúc cây phân cấp).
6. **`CategoryResponse.java`**:
   - `UUID id`, `String name`, `String slug`, `long postCount`.
7. **`TagResponse.java`**:
   - `UUID id`, `String name`, `long postCount`.
8. **`NotificationResponse.java`**:
   - `UUID id`, `String message`, `String targetUrl`, `boolean isRead`, `String type`, `LocalDateTime createdAt`.
9. **`BlogSuggestionResponse.java`**:
   - `UUID id`, `String title`, `String slug`, `String authorName`, `String categoryName` (DTO siêu nhẹ trả về cho thanh Search Suggestions).
10. **`AdminStatsResponse.java`**:
    - `long totalUsers`, `long totalPosts`, `List<BlogResponse> recentBlogs` (Dữ liệu tổng quan cho Dashboard Quản trị).

---

# PHẦN IV: BỘ CÂU HỎI VẤN ĐÁP LÝ THUYẾT ĐỈNH CAO VỀ DTO, ENTITY & REPOSITORY

#### Q1: "Khóa chính UUID có ưu và nhược điểm gì so với khóa chính số nguyên tự tăng (Auto-Increment / Sequence)?"
- **Trả lời**:
  - **Ưu điểm**:
    1. *Bảo mật cao*: UUID là chuỗi ngẫu nhiên 128-bit, hacker không thể đoán được ID tiếp theo để dò quét dữ liệu (chống Insecure Direct Object References - IDOR).
    2. *Sinh ID phân tán*: Client hoặc Backend có thể tự sinh UUID trước khi lưu xuống CSDL mà không sợ bị trùng lặp, cực kỳ phù hợp với hệ thống phân tán, Microservices và nạp dữ liệu offline.
  - **Nhược điểm**: Chiếm dung lượng lưu trữ lớn hơn (16 bytes so với 4 bytes của INT) và hiệu năng đánh chỉ mục B-Tree Index hơi chậm hơn số nguyên tự tăng một chút vì dữ liệu chèn vào không theo thứ tự tuần tự tuyệt đối.

#### Q2: "Vấn đề N+1 truy vấn (N+1 Query Problem) trong JPA là gì và dự án của nhóm giải quyết như thế nào?"
- **Trả lời**:
  - *Hiện tượng*: Khi lấy danh sách $N$ bài viết, nếu truy cập thuộc tính `author` hoặc `category` mà đang để quan hệ `LAZY`, Hibernate sẽ phải phát sinh thêm $N$ câu lệnh `SELECT` phụ để lấy thông tin cho từng bài viết, tổng cộng là $1 + N$ câu truy vấn gây nghẽn CSDL.
  - *Giải pháp trong dự án*:
    1. Nhóm em dùng câu lệnh JPQL tùy biến với mệnh đề `LEFT JOIN` và gom nhóm `GROUP BY` trực tiếp trong `BlogRepository.java`.
    2. Ở tầng chuyển đổi DTO, nhóm em sử dụng thư viện **MapStruct** cấu hình ánh xạ rõ ràng để không kích hoạt nạp lười ngoài ý muốn.

#### Q3: "Sự khác biệt giữa `CascadeType` trong JPA và `@OnDelete(action = OnDeleteAction.CASCADE)` trong Hibernate là gì?"
- **Trả lời**:
  - `CascadeType.ALL` (hoặc `REMOVE`) của JPA là cơ chế xử lý ở **Tầng Ứng Dụng (Application Level)**: Hibernate sẽ tải các thực thể con lên bộ nhớ RAM rồi lần lượt gửi các lệnh `DELETE` từng dòng một xuống CSDL.
  - `@OnDelete(action = OnDeleteAction.CASCADE)` là cơ chế của **Tầng Cơ Sở Dữ Liệu (Database DDL Level)**: Hibernate sẽ sinh trực tiếp mệnh đề `ON DELETE CASCADE` vào định nghĩa khóa ngoại trong MySQL. Khi xóa bài blog, chính cỗ máy MySQL sẽ tự động xóa sạch toàn bộ lượt like, view, comment trong nháy mắt mà không cần tải dữ liệu lên RAM của Spring Boot, hiệu năng nhanh hơn gấp nhiều lần!

#### Q4: "Lỗi `LazyInitializationException` xảy ra khi nào và cách khắc phục?"
- **Trả lời**:
  - *Nguyên nhân*: Xảy ra khi lập trình viên cố tình truy cập vào một thuộc tính quan hệ được cấu hình `FetchType.LAZY` (ví dụ `blog.getAuthor().getUsername()`) sau khi Session/Transaction của Hibernate đã bị đóng (ngoài phạm vi của `@Transactional`).
  - *Khắc phục*:
    1. Truy cập và map dữ liệu sang DTO ngay bên trong tầng Service khi Transaction còn đang mở.
    2. Dùng kỹ thuật `JOIN FETCH` trong JPQL để nạp dữ liệu cùng lúc.
    3. Cấu hình Spring Boot `spring.jpa.open-in-view=true` (mặc định của Spring Boot) để giữ Hibernate Session mở cho tới khi view được render xong.
