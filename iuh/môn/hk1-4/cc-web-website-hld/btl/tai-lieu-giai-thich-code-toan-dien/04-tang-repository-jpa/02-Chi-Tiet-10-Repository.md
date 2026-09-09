# GIẢI THÍCH CHI TIẾT TỪNG PHƯƠNG THỨC TRONG 10 REPOSITORY CỦA DỰ ÁN

> **Mục tiêu**: Nắm chắc 100% mục đích, câu lệnh SQL sinh ngầm và cách sử dụng của từng hàm trong cả 10 file Repository ở thư mục `src/main/java/com/group/blog/repository/`.

---

## 1. `UserRepository.java`
```java
package com.group.blog.repository;

import com.group.blog.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;
import java.util.UUID;

@Repository
public interface UserRepository extends JpaRepository<User, UUID> {
    boolean existsByUsername(String username);
    Optional<User> findById(UUID id);
    Optional<User> findByUsername(String username);
    boolean existsByEmail(String email);
    Optional<User> findByEmail(String email);
    void deleteById(UUID id);
}
```
- **`existsByUsername(String username)`**: Kiểm tra xem tên tài khoản đã tồn tại chưa khi người dùng nhập form đăng ký. Trả về `true` nếu đã có người dùng, giúp tầng Service chặn lại và báo lỗi `USER_EXISTED`.
- **`findByUsername(String username)`**: Tìm đối tượng `User` theo username để phục vụ việc xác thực đăng nhập trong `AuthenticationService`.
- **`existsByEmail(String email)`**: Kiểm tra email đã có ai đăng ký chưa.
- **`findByEmail(String email)`**: Tìm tài khoản theo email (phục vụ tính năng quên mật khẩu / khôi phục tài khoản).
- **`deleteById(UUID id)`**: Xóa người dùng theo ID (dành cho chức năng quản trị viên Admin quản lý thành viên).

---

## 2. `BlogRepository.java`
```java
package com.group.blog.repository;

import com.group.blog.entity.Blog;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.UUID;

@Repository
public interface BlogRepository extends JpaRepository<Blog, UUID> {
    // 1. Lấy tất cả bài viết công khai kèm lượt xem, thích, comment
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

    // 2. Lọc bài viết theo Danh mục (Category)
    @Query("""
       SELECT b, COUNT(DISTINCT v.id), COUNT(DISTINCT l.id), COUNT(DISTINCT c.id)
       FROM Blog b
       LEFT JOIN BlogLike l ON l.blog = b
       LEFT JOIN BlogView  v ON v.blog = b
       LEFT JOIN Comment  c ON c.blog = b
       WHERE b.category.id = :categoryId AND b.draft = false
       GROUP BY b
       ORDER BY b.publishedAt DESC
    """)
    List<Object[]> findBlogsByCategoryIdWithCounts(@Param("categoryId") UUID categoryId);

    // 3. Lọc bài viết theo Thẻ (Tag)
    @Query("""
       SELECT b, COUNT(DISTINCT v.id), COUNT(DISTINCT l.id), COUNT(DISTINCT c.id)
       FROM Blog b
       JOIN b.tags t
       LEFT JOIN BlogLike l ON l.blog = b
       LEFT JOIN BlogView  v ON v.blog = b
       LEFT JOIN Comment  c ON c.blog = b
       WHERE t.id = :tagId AND b.draft = false
       GROUP BY b
       ORDER BY b.publishedAt DESC
    """)
    List<Object[]> findBlogsByTagIdWithCounts(@Param("tagId") UUID tagId);

    // 4. Tìm kiếm bài viết theo từ khóa trong tiêu đề
    @Query("""
       SELECT b, COUNT(DISTINCT v.id), COUNT(DISTINCT l.id), COUNT(DISTINCT c.id)
       FROM Blog b
       LEFT JOIN BlogLike l ON l.blog = b
       LEFT JOIN BlogView  v ON v.blog = b
       LEFT JOIN Comment  c ON c.blog = b
       WHERE LOWER(b.title) LIKE TRIM(LOWER(CONCAT('%',:keyword,'%'))) AND b.draft = false
       GROUP BY b
       ORDER BY b.publishedAt DESC
    """)
    List<Object[]> searchBlogsByKeywordWithCounts(@Param("keyword") String keyword);

    // 5. Gợi ý tìm kiếm nhanh (Top 5 bài viết khớp tiêu đề khi gõ vào ô search)
    List<Blog> findTop5ByTitleContainingIgnoreCaseAndDraftIsFalse(String title);

    // 6. Tìm kiếm kết hợp cả Từ khóa VÀ Danh mục
    @Query("""
       SELECT b, COUNT(DISTINCT v.id), COUNT(DISTINCT l.id), COUNT(DISTINCT c.id)
       FROM Blog b
       LEFT JOIN BlogLike l ON l.blog = b
       LEFT JOIN BlogView  v ON v.blog = b
       LEFT JOIN Comment  c ON c.blog = b
       WHERE LOWER(b.title) LIKE TRIM(LOWER(CONCAT('%',:keyword,'%'))) AND b.category.id = :categoryId AND b.draft = false
       GROUP BY b
       ORDER BY b.publishedAt DESC
    """)
    List<Object[]> findByKeywordAndCategoryIdWithCounts(@Param("keyword") String keyword, @Param("categoryId") UUID categoryId);

    // 7. Lấy tất cả bài viết của Tác giả (gồm cả bản nháp và đã xuất bản - dùng cho trang Quản lý bài viết)
    @Query("""
       SELECT b, COUNT(DISTINCT v.id), COUNT(DISTINCT l.id), COUNT(DISTINCT c.id)
       FROM Blog b
       LEFT JOIN BlogLike l ON l.blog = b
       LEFT JOIN BlogView  v ON v.blog = b
       LEFT JOIN Comment  c ON c.blog = b
       WHERE b.author.username = :username
       GROUP BY b
       ORDER BY b.publishedAt DESC
    """)
    List<Object[]> findByAuthorUsernameWithCounts(@Param("username") String username);

    // 8. Lấy bài viết ĐÃ XUẤT BẢN của một tác giả (dành cho độc giả xem trang cá nhân của tác giả đó)
    @Query("""
       SELECT b, COUNT(DISTINCT v.id), COUNT(DISTINCT l.id), COUNT(DISTINCT c.id)
       FROM Blog b
       LEFT JOIN BlogLike l ON l.blog = b
       LEFT JOIN BlogView  v ON v.blog = b
       LEFT JOIN Comment  c ON c.blog = b
       WHERE b.author.username = :username AND b.draft = false
       GROUP BY b
       ORDER BY b.publishedAt DESC
    """)
    List<Object[]> findPublishedByAuthorUsernameWithCounts(@Param("username") String username);

    // 9. Lấy 5 bài viết mới nhất phục vụ trang Dashboard Admin
    List<Blog> findTop5ByDraftFalseOrderByCreatedAtDesc();

    // 10. Đếm tổng số bài viết đã xuất bản
    long countByDraftFalse();
}
```

---

## 3. `CategoryRepository.java`
```java
package com.group.blog.repository;

import com.group.blog.entity.Category;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.UUID;

@Repository
public interface CategoryRepository extends JpaRepository<Category, UUID> {
    boolean existsByName(String name);

    // Lấy tất cả Category và đếm mỗi chủ đề có bao nhiêu bài viết
    @Query("""
     SELECT c, COUNT(b.id)
     FROM Category c
     LEFT JOIN c.blogs b
     GROUP BY c
    """)
    List<Object[]> findAllCategoriesWithPostCount();
}
```
- **`existsByName(String name)`**: Ngăn chặn việc Admin tạo trùng tên danh mục.
- **`findAllCategoriesWithPostCount()`**: Lấy toàn bộ danh mục kèm số lượng bài viết của từng danh mục để hiển thị số badge trên menu (Ví dụ: `Công nghệ (12)`, `Thiết kế (5)`).

---

## 4. `TagRepository.java`
```java
package com.group.blog.repository;

import com.group.blog.entity.Tag;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Repository
public interface TagRepository extends JpaRepository<Tag, UUID> {
    Optional<Tag> findByName(String name);
    boolean existsByName(String name);

    // Đếm xem có bao nhiêu Blog đang gắn Tag này
    @Query("""
     SELECT t, COUNT(b.id)
     FROM Tag t
     LEFT JOIN t.blogs b
     GROUP BY t
     """)
    List<Object[]> findAllTagsWithPostCount();
}
```
- **`findByName(String name)`**: Dùng khi tạo bài viết mới, nếu tác giả gõ một thẻ tag đã có trong DB thì hệ thống lấy lại tag cũ chứ không tạo mới.
- **`findAllTagsWithPostCount()`**: Thống kê số lượng bài viết theo tag để hiển thị đám mây thẻ tag (Tag Cloud) ở trang chủ.

---

## 5. `CommentRepository.java`
```java
package com.group.blog.repository;

import com.group.blog.entity.Comment;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.List;
import java.util.UUID;

@Repository
public interface CommentRepository extends JpaRepository<Comment, UUID> {
    long countByBlogId(UUID blogId);
    List<Comment> findByBlogIdAndParentIsNullOrderByCreatedAtDesc(UUID blogId);
}
```
- **`countByBlogId(UUID blogId)`**: Đếm nhanh tổng số bình luận của một bài viết.
- **`findByBlogIdAndParentIsNullOrderByCreatedAtDesc(UUID blogId)`**: Cực kỳ quan trọng. Chỉ lấy các bình luận gốc cấp 1 (những comment không có `parent_id`), sắp xếp thời gian mới nhất lên đầu. Các phản hồi con sẽ được tự động nạp qua danh sách `replies`.

---

## 6. `BlogLikeRepository.java`
```java
package com.group.blog.repository;

import com.group.blog.entity.BlogLike;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.Optional;
import java.util.UUID;

@Repository
public interface BlogLikeRepository extends JpaRepository<BlogLike, UUID> {
    long countByBlogId(UUID blogId);
    boolean existsByBlogIdAndUserUsername(UUID blogId, String username);
    Optional<BlogLike> findByBlogIdAndUserUsername(UUID blogId, String username);
}
```
- **`countByBlogId(UUID blogId)`**: Đếm tổng lượt thích của một bài viết.
- **`existsByBlogIdAndUserUsername(...)`**: Kiểm tra xem tài khoản đang đăng nhập đã bấm thích bài này chưa để tô màu đỏ nút trái tim trên giao diện.
- **`findByBlogIdAndUserUsername(...)`**: Tìm bản ghi thích bài viết khi người dùng bấm lần 2 (để xóa bản ghi này đi, tương đương hành động Bỏ thích - Unlike).

---

## 7. `BookmarkRepository.java`
```java
package com.group.blog.repository;

import com.group.blog.entity.Bookmark;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Repository
public interface BookmarkRepository extends JpaRepository<Bookmark, UUID> {
    boolean existsByBlogIdAndUserUsername(UUID blogId, String username);
    Optional<Bookmark> findByBlogIdAndUserUsername(UUID blogId, String username);
    List<Bookmark> findByUserUsernameOrderByCreatedAtDesc(String username);
}
```
- **`existsByBlogIdAndUserUsername(...)`**: Kiểm tra bài viết đã được lưu vào sổ tay đọc lại của user chưa.
- **`findByUserUsernameOrderByCreatedAtDesc(String username)`**: Lấy toàn bộ danh sách các bài viết đã bookmark của người dùng để hiển thị trên trang "Bài viết đã lưu" (`/saved-blogs`).

---

## 8. `UserFollowRepository.java`
```java
package com.group.blog.repository;

import com.group.blog.entity.User;
import com.group.blog.entity.UserFollow;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Repository
public interface UserFollowRepository extends JpaRepository<UserFollow, UUID> {
    long countByFollowing(User following); // Đếm số người đang follow tác giả này (Followers)
    long countByFollower(User follower);   // Đếm số người tác giả này đang theo dõi (Following)
    Optional<UserFollow> findByFollowerAndFollowing(User follower, User following); // Tìm record để hủy follow (Unfollow)
    boolean existsByFollowerUsernameAndFollowing(String followerUsername, User following); // Kiểm tra xem tôi đã follow tác giả này chưa
    List<UserFollow> findByFollowingOrderByCreatedAtDesc(User following); // Danh sách những người theo dõi
    List<UserFollow> findByFollowerOrderByCreatedAtDesc(User follower);   // Danh sách những người mình đang theo dõi
}
```

---

## 9. `NotificationRepository.java`
```java
package com.group.blog.repository;

import com.group.blog.entity.Notification;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.List;
import java.util.UUID;

@Repository
public interface NotificationRepository extends JpaRepository<Notification, UUID> {
    List<Notification> findByUserUsernameOrderByCreatedAtDesc(String username);
}
```
- **`findByUserUsernameOrderByCreatedAtDesc(String username)`**: Lấy toàn bộ danh sách thông báo của một người dùng, ưu tiên các thông báo mới nhất hiện lên trên đầu hộp thư.

---

## 10. `BlogViewRepository.java`
```java
package com.group.blog.repository;

import com.group.blog.entity.BlogView;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.UUID;

@Repository
public interface BlogViewRepository extends JpaRepository<BlogView, UUID> {
    long countByBlogId(UUID blogId);
}
```
- **`countByBlogId(UUID blogId)`**: Đếm tổng số lượt xem thực tế của một bài viết.

---

## 11. BỘ CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN VỀ CÁC REPOSITORY

### Câu 1: Tại sao trong các phương thức của Repository không có annotation `@Transactional`?
- **Trả lời**:
  > "Thưa thầy/cô, mặc định lớp triển khai sẵn của Spring Data JPA là `SimpleJpaRepository` đã được đánh dấu sẵn `@Transactional(readOnly = true)` ở mức class và `@Transactional` ở các phương thức ghi (`save`, `delete`). Do đó ở interface chúng em không cần khai báo lại.
  > Hơn nữa, việc quản lý giao dịch nên được thực hiện ở tầng **Service Layer** để đảm bảo một nghiệp vụ gồm nhiều bước ghi dữ liệu (ví dụ: vừa thêm comment vừa tạo notification) có thể rollback đồng bộ nếu có lỗi xảy ra."

### Câu 2: Sự khác biệt giữa `JpaRepository` và `CrudRepository` là gì? Tại sao nhóm chọn `JpaRepository`?
- **Trả lời**:
  > "Thưa thầy/cô:
  > - `CrudRepository`: Chỉ cung cấp các thao tác cơ bản CRUD (Thêm, Đọc, Sửa, Xóa).
  > - `JpaRepository`: Là interface con mở rộng từ `PagingAndSortingRepository` và `CrudRepository`. Nó cung cấp thêm các tính năng cao cấp đặc thù của JPA như: Phân trang (Pagination), Sắp xếp (Sorting), Xóa hàng loạt theo đợt (`deleteInBatch()`), và đẩy dữ liệu tức thì xuống DB (`flush()`). 
  > Nhóm em chọn `JpaRepository` để có được bộ công cụ mạnh mẽ và linh hoạt nhất."
