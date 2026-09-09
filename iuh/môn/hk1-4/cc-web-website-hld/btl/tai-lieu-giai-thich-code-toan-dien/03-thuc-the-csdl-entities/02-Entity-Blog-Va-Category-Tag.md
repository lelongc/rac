# GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG ENTITY BLOG, CATEGORY VÀ TAG

> **Mục tiêu**: Hiểu rõ mối quan hệ cơ sở dữ liệu giữa Bài viết, Danh mục và Thẻ gắn (Quan hệ 1 - Nhiều và Nhiều - Nhiều trong JPA), kiểu dữ liệu lưu văn bản dài (`TEXT`, `LONGTEXT`), cơ chế lưu bản nháp (`draftContent`, `draftBanner`), và các hàm tự động cập nhật thời gian `@PrePersist`, `@PreUpdate`.

---

## 1. MÃ NGUỒN ĐẦY ĐỦ CỦA 3 THỰC THỂ

### 1.1. Thực thể `Blog.java` (`src/main/java/com/group/blog/entity/Blog.java`)
```java
package com.group.blog.entity;

import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.FieldDefaults;

import java.time.LocalDateTime;
import java.util.HashSet;
import java.util.Set;
import java.util.UUID;

@Entity
@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE)
@Table(name="blogs")
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

    // Cột chứa nội dung đang sửa dở (nháp)
    @Column(columnDefinition = "LONGTEXT")
    String draftContent;

    // Cột chứa ảnh bìa đang sửa dở
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
            uniqueConstraints = {
                    @UniqueConstraint(columnNames = {"blog_id","tag_id"})
            }
    )
    @Builder.Default
    Set<Tag> tags = new HashSet<>();

    @PrePersist
    void prePersist(){
        createdAt = LocalDateTime.now();

        if(!draft && publishedAt == null){
            publishedAt = LocalDateTime.now();
        }
    }

    @PreUpdate
    void preUpdate(){
        updatedAt = LocalDateTime.now();
    }
}
```

### 1.2. Thực thể `Category.java` (`src/main/java/com/group/blog/entity/Category.java`)
```java
package com.group.blog.entity;

import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.FieldDefaults;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

@Entity
@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
@FieldDefaults(level= AccessLevel.PRIVATE)
@Table(name="categories")
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

### 1.3. Thực thể `Tag.java` (`src/main/java/com/group/blog/entity/Tag.java`)
```java
package com.group.blog.entity;

import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.FieldDefaults;

import java.util.HashSet;
import java.util.Set;
import java.util.UUID;

@Entity
@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE)
@Table(name="tags")
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

---

## 2. GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE VÀ Ý NGHĨA THIẾT KẾ

### 2.1. Các kiểu dữ liệu đặc biệt trong `Blog.java`
```java
    @Column(columnDefinition = "TEXT")
    String description;

    @Column(columnDefinition = "LONGTEXT")
    String content;
```
- **Tại sao phải dùng `columnDefinition = "TEXT"` và `"LONGTEXT"`?**:
  - Mặc định, một biến kiểu `String` trong Java khi sinh ra trong database chỉ là `VARCHAR(255)` (tối đa 255 ký tự).
  - Đối với bài viết blog, nội dung bài viết (`content`) chứa hàng ngàn chữ, các đoạn mã code HTML, hình ảnh nhúng, nếu để mặc định `VARCHAR(255)` thì khi lưu bài dài sẽ lập tức bị lỗi `Data truncation: Data too long for column`.
  - `TEXT`: Chứa tối đa 65.535 ký tự (phù hợp cho mô tả ngắn/tóm tắt `description`).
  - `LONGTEXT`: Chứa tối đa lên đến 4GB dữ liệu (khoảng 4 tỷ ký tự), giúp người dùng viết bài thoải mái không giới hạn độ dài.

---

### 2.2. Tính năng Lưu bản nháp (Draft System)
```java
    boolean draft;

    @Column(columnDefinition = "LONGTEXT")
    String draftContent;

    @Column(columnDefinition = "LONGTEXT")
    String draftBanner;
```
- **Ý nghĩa nghiệp vụ**:
  - Nếu `draft = true`: Bài viết đang ở chế độ bản nháp, chỉ có chính tác giả mới nhìn thấy trong trang quản lý bài viết cá nhân, người ngoài không thể tìm kiếm hoặc đọc được.
  - Các cột `draftContent` và `draftBanner`: Cho phép tác giả đang có một bài viết đã xuất bản công khai (`draft = false`), nhưng muốn chỉnh sửa thêm bớt nội dung mà chưa muốn độc giả nhìn thấy ngay. Tác giả lưu nội dung mới vào `draftContent`. Khi nào bấm "Xuất bản cập nhật", hệ thống mới chép từ `draftContent` sang `content` chính thức. Đây là một tính năng cực kỳ cao cấp của các trang như Medium/Dev.to!

---

### 2.3. Quan hệ Nhiều - Một (`@ManyToOne`) với User và Category
```java
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "author_id")
    User author;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "category_id")
    Category category;
```
- **`@ManyToOne`**: Nhiều bài viết (Many) có thể thuộc về Một tác giả (One User) hoặc Một danh mục (One Category).
- **`@JoinColumn(name = "author_id")`**: Hibernate sẽ tạo một cột khóa ngoại có tên là `author_id` trong bảng `blogs`, tham chiếu đến cột `id` của bảng `users`.
- **`fetch = FetchType.LAZY`**: Chỉ nạp thông tin tác giả và danh mục khi thực sự cần thiết, tối ưu hóa tốc độ khi truy vấn danh sách hàng loạt bài viết trên trang chủ.

---

### 2.4. Quan hệ Nhiều - Nhiều (`@ManyToMany`) giữa Blog và Tag
```java
    @ManyToMany
    @JoinTable(
            name = "blog_tags",
            joinColumns = @JoinColumn(name = "blog_id"),
            inverseJoinColumns = @JoinColumn(name = "tag_id"),
            uniqueConstraints = {
                    @UniqueConstraint(columnNames = {"blog_id","tag_id"})
            }
    )
    @Builder.Default
    Set<Tag> tags = new HashSet<>();
```
- **Bản chất thực tế**: Một bài blog có thể gắn nhiều thẻ tag (ví dụ: `#Java`, `#SpringBoot`), và một thẻ tag (ví dụ `#Java`) có thể xuất hiện trong nhiều bài blog khác nhau. Đây là mối quan hệ **Nhiều - Nhiều (Many-to-Many)**.
- Trong mô hình cơ sở dữ liệu quan hệ (RDBMS), không thể liên kết trực tiếp nhiều - nhiều giữa 2 bảng mà bắt buộc phải thông qua một **Bảng trung gian (Join Table)**.
- **`@JoinTable(name = "blog_tags", ...)`**: Hibernate sẽ tự động tạo bảng trung gian có tên là `blog_tags` gồm 2 cột:
  - `blog_id` (tham chiếu đến bảng `blogs`).
  - `tag_id` (tham chiếu đến bảng `tags`).
- `uniqueConstraints`: Ràng buộc không cho phép một bài blog bị gán lặp lại cùng một thẻ tag hai lần.
- Ở phía `Tag.java`, thuộc tính `@ManyToMany(mappedBy = "tags")` cho biết mối quan hệ này là hai chiều và phía `Blog` là chủ sở hữu (Owner side) quản lý bảng liên kết.

---

### 2.5. Xử lý thời gian tự động: `@PrePersist` và `@PreUpdate`
```java
    @PrePersist
    void prePersist(){
        createdAt = LocalDateTime.now();

        if(!draft && publishedAt == null){
            publishedAt = LocalDateTime.now();
        }
    }

    @PreUpdate
    void preUpdate(){
        updatedAt = LocalDateTime.now();
    }
```
- Trước khi thêm bài mới (`@PrePersist`): Tự động gán thời gian tạo `createdAt`. Nếu bài viết không phải là bản nháp (`!draft`) và chưa có ngày xuất bản thì tự động lấy ngày giờ hiện tại làm `publishedAt`.
- Trước khi cập nhật bài (`@PreUpdate`): Tự động cập nhật trường `updatedAt` thành ngày giờ mới nhất, giúp độc giả biết bài viết được chỉnh sửa lần cuối khi nào.

---

## 3. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN VỀ BLOG, CATEGORY, TAG

### Câu 1: Tại sao ở quan hệ `@ManyToMany` giữa `Blog` và `Tag`, nhóm em lại dùng kiểu dữ liệu `Set<Tag>` mà không dùng `List<Tag>`?
- **Trả lời**:
  > "Thưa thầy/cô:
  > 1. Về mặt nghiệp vụ: Một bài viết không thể có 2 tag trùng tên (ví dụ đã có tag Java thì không thể gắn thêm một tag Java nữa). Kiểu `Set` trong Java tự động loại bỏ các phần tử trùng lặp.
  > 2. Về mặt hiệu năng Hibernate: Khi dùng `List`, mỗi lần thêm hoặc xóa 1 phần tử trong danh sách liên kết nhiều-nhiều, Hibernate thường có cơ chế xóa toàn bộ các dòng trong bảng trung gian `blog_tags` rồi chèn lại từ đầu. Khi dùng `Set`, Hibernate chỉ thực hiện duy nhất một câu lệnh `DELETE` hoặc `INSERT` đúng trên dòng bị thay đổi, giúp hiệu năng tối ưu hơn rất nhiều."

### Câu 2: Giả sử em xóa một Danh mục (`Category`), các bài viết thuộc danh mục đó có bị xóa theo không? Điều đó được quy định bởi dòng code nào?
- **Trả lời**:
  > "Thưa thầy/cô, trong class `Category.java`, tại thuộc tính `blogs`, nhóm em có khai báo:
  > `@OneToMany(mappedBy = "category", cascade = CascadeType.ALL)`.
  > Vì có cấu hình `CascadeType.ALL`, nên mặc định nếu gọi lệnh xóa một đối tượng Category thì Hibernate sẽ tự động xóa luôn toàn bộ các bài viết liên kết thuộc danh mục đó.
  > Trong thực tế nếu muốn giữ lại bài viết và chỉ gán danh mục về `null`, chúng em chỉ cần đổi sang `cascade = {CascadeType.PERSIST, CascadeType.MERGE}` và cập nhật `category_id = null` cho các bài viết trước khi xóa."
