# GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG ENTITY USER VÀ ROLE

> **Mục tiêu**: Nắm chắc 100% cấu trúc thực thể người dùng (`User.java`), bảng phụ lưu quyền (`user_roles`), kỹ thuật sinh khóa chính UUID, các chú thích của Hibernate/JPA và enum phân quyền (`Role.java`).

---

## 1. MÃ NGUỒN ĐẦY ĐỦ CỦA `Role.java` VÀ `User.java`

### 1.1. File `Role.java` (`src/main/java/com/group/blog/enums/Role.java`)
```java
package com.group.blog.enums;

public enum Role {
    ADMIN,
    USER
}
```

### 1.2. File `User.java` (`src/main/java/com/group/blog/entity/User.java`)
```java
package com.group.blog.entity;

import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.FieldDefaults;
import java.time.LocalDateTime;
import java.util.*;

@Entity
@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
@FieldDefaults(level= AccessLevel.PRIVATE)
@Table(name="users")
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
    void prePersist(){
       if(createdAt == null)
        createdAt = LocalDateTime.now();
    }
}
```

---

## 2. GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE

### 2.1. Các chú thích mức lớp (Class-level Annotations)
```java
@Entity
@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
@FieldDefaults(level= AccessLevel.PRIVATE)
@Table(name="users")
public class User {
```
- **`@Entity`**: Chú thích quan trọng nhất của JPA. Báo cho Hibernate biết lớp `User` là một thực thể đại diện cho một bảng dữ liệu trong CSDL.
- **`@Getter` & `@Setter` (Lombok)**: Tự động sinh mã nguồn cho toàn bộ các hàm getter (`getId()`, `getUsername()`, ...) và setter (`setUsername(...)`, ...) trong lúc biên dịch.
- **`@Builder` (Lombok)**: Cung cấp mẫu thiết kế Builder pattern, cho phép khởi tạo đối tượng ngắn gọn và an toàn: `User.builder().username("admin").build()`.
- **`@NoArgsConstructor` & `@AllArgsConstructor`**: Hibernate bắt buộc phải có constructor không tham số (`NoArgsConstructor`) để có thể khởi tạo đối tượng khi đọc dữ liệu từ DB lên. `AllArgsConstructor` phục vụ cho `@Builder`.
- **`@FieldDefaults(level = AccessLevel.PRIVATE)`**: Tự động biến tất cả các thuộc tính bên trong lớp này thành `private` mà không cần phải gõ từ khóa `private` lặp đi lặp lại ở từng dòng.
- **`@Table(name="users")`**: Chỉ định tên bảng trong cơ sở dữ liệu là `users`. Tại sao đặt tên là `users` thay vì `user`? Vì trong nhiều hệ quản trị CSDL như PostgreSQL, H2 hay SQL Server, từ khóa `USER` là một từ khóa hạn chế của hệ thống (Reserved Keyword). Đặt tên `users` sẽ tránh mọi lỗi xung đột cú pháp.

---

### 2.2. Khóa chính UUID
```java
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    UUID id;
```
- **`@Id`**: Đánh dấu trường `id` là Khóa chính (Primary Key) của bảng `users`.
- **`@GeneratedValue(strategy = GenerationType.UUID)`**: Tự động sinh chuỗi định danh toàn cầu ngẫu nhiên (Universally Unique Identifier, ví dụ: `c0a8012e-8e2b-1a34-818e-2b1a34000000`).
- **Ưu điểm vượt trội so với số tự tăng `Long / BigInt` (`AUTO_INCREMENT`)**:
  - Không thể đoán trước được ID của người dùng (chống lại việc kẻ xấu đoán ID `1, 2, 3...` để cào dữ liệu qua API).
  - Cực kỳ an toàn và tối ưu khi sáp nhập hoặc phân tán dữ liệu trên nhiều server.

---

### 2.3. Các cột thông tin người dùng
```java
    @Column(nullable = false, unique = true, length = 100)
    String username;

    @Column(nullable = false, length = 255)
    String password;

    @Column(unique = true, length = 255)
    String email;

    String bio;
    String avatarUrl;
    LocalDateTime createdAt;
```
- **`@Column(nullable = false, unique = true, length = 100)`** trên `username`:
  - `nullable = false`: Bắt buộc không được để trống (NOT NULL).
  - `unique = true`: Không được trùng lặp. Nếu có người thứ hai cố tình đăng ký cùng username, DB sẽ từ chối ngay.
  - `length = 100`: Giới hạn độ dài chuỗi tối đa 100 ký tự (tương đương kiểu `VARCHAR(100)` trong SQL).
- **`password`**: Độ dài `255` ký tự. Chuỗi băm BCrypt luôn có độ dài 60 ký tự, khai báo 255 để đảm bảo lưu trữ thoải mái mà không bị tràn bộ nhớ.
- **`bio`**: Tiểu sử ngắn của tác giả (Ví dụ: "Lê Thành Long - MSSV: 23630851").
- **`avatarUrl`**: Đường link ảnh đại diện lưu trên Cloudinary.
- **`createdAt`**: Thời điểm tạo tài khoản.

---

### 2.4. Bảng liên kết quyền hạn: `@ElementCollection` và `@CollectionTable`
```java
    @ElementCollection(fetch = FetchType.EAGER)
    @CollectionTable(
            name = "user_roles",
            joinColumns = @JoinColumn(name = "user_id"),
            uniqueConstraints = @UniqueConstraint(columnNames = {"user_id", "role"})
    )
    @Column(name = "role")
    @Builder.Default
    Set<String> roles = new HashSet<>();
```
- **Tại sao lại dùng `@ElementCollection` thay vì tạo riêng 1 Entity `Role`?**:
  - Đối với bài toán blog cá nhân, một người dùng chỉ có một vài quyền cơ bản (`ADMIN`, `USER`). Việc tạo hẳn một Entity `Role` kèm quan hệ `@ManyToMany` là quá cồng kềnh và dư thừa.
  - `@ElementCollection` là giải pháp thanh thoát nhất: Hibernate sẽ tự động tạo một bảng phụ có tên là `user_roles` gồm 2 cột: `user_id` và `role`.
  - Cặp `(user_id, role)` được gán `uniqueConstraints` để đảm bảo một người không bị lưu trùng 2 quyền giống nhau.
  - **`fetch = FetchType.EAGER`**: Khi nạp thông tin người dùng lên để xác thực đăng nhập, Hibernate sẽ nạp luôn danh sách các quyền ngay lập tức (Eager loading) thay vì nạp lười (Lazy), tránh lỗi `LazyInitializationException` khi Spring Security kiểm tra quyền hạn.
  - **`@Builder.Default`**: Đảm bảo khi dùng Lombok Builder thì tập hợp `roles` luôn được khởi tạo mặc định là một `new HashSet<>()` rỗng, không bao giờ bị dính lỗi `NullPointerException`.

---

### 2.5. Quan hệ 1 - Nhiều với Bài viết (`Blog`)
```java
    @OneToMany(mappedBy = "author", cascade = CascadeType.ALL)
    @Builder.Default
    List<Blog> blogs = new ArrayList<>();
```
- **`@OneToMany`**: Một tác giả (User) có thể viết nhiều bài báo (Blogs).
- **`mappedBy = "author"`**: Khai báo rằng phía đối diện (lớp `Blog.java`) có thuộc tính mang tên `author` nắm giữ khóa ngoại.
- **`cascade = CascadeType.ALL`**: Cơ chế lan truyền (Cascading). Nếu xóa một User, toàn bộ các bài viết do user đó tạo ra cũng sẽ tự động được xóa theo để tránh dữ liệu mồ côi (Orphan records).

---

### 2.6. Tự động điền ngày giờ: `@PrePersist`
```java
    @PrePersist
    void prePersist(){
       if(createdAt == null)
        createdAt = LocalDateTime.now();
    }
```
- **`@PrePersist`**: Hàm này là một hàm đón đầu (Lifecycle Callback) của JPA. Trước khi câu lệnh `INSERT` được bắn xuống Database, Hibernate sẽ tự động kích hoạt hàm này. Nếu `createdAt` chưa có giá trị, nó sẽ lấy thời điểm hiện tại `LocalDateTime.now()` để lưu vào DB. Lập trình viên không cần viết code gán ngày giờ thủ công.

---

## 3. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN VỀ USER & ROLE

### Câu 1: Em hãy giải thích sự khác nhau giữa `FetchType.LAZY` và `FetchType.EAGER`? Tại sao ở trường `roles` em lại chọn `EAGER`?
- **Trả lời**:
  > "Thưa thầy/cô:
  > - `FetchType.LAZY` (Nạp lười): Dữ liệu liên kết chỉ được truy vấn từ Database khi nào chúng em thực sự gọi hàm getter trên đối tượng đó. Giúp tiết kiệm bộ nhớ và tránh truy vấn dư thừa.
  > - `FetchType.EAGER` (Nạp sốt sắng): Dữ liệu của bảng liên quan sẽ được tự động JOIN và lấy lên cùng lúc với bảng chính ngay từ đầu.
  > - Ở trường `roles`, nhóm em chọn `FetchType.EAGER` vì mỗi khi người dùng đăng nhập hoặc gửi token lên, Spring Security bắt buộc phải kiểm tra quyền hạn ngay lập tức trong bộ lọc bảo mật. Nếu để LAZY, khi session Hibernate đóng lại, Spring Security truy cập vào `roles` sẽ lập tức bắn ra ngoại lệ kinh điển `LazyInitializationException: could not initialize proxy - no Session`."

### Câu 2: Khóa chính dạng UUID có ưu điểm và nhược điểm gì so với kiểu số nguyên tự tăng `Long` (`AUTO_INCREMENT`)?
- **Trả lời**:
  > "Thưa thầy/cô:
  > - **Ưu điểm**: UUID là chuỗi ngẫu nhiên dài 128-bit, đảm bảo tính duy nhất trên phạm vi toàn cầu mà không cần sự phối hợp tập trung của database. Về mặt bảo mật, kẻ tấn công không thể dò quét ID (ID Enumeration Attack) như kiểu số `id=1, id=2`.
  > - **Nhược điểm**: Dung lượng lưu trữ lớn hơn (16 byte so với 8 byte của BigInt) và việc đánh chỉ mục Index B-Tree sẽ tốn tài nguyên hơn một chút so với số nguyên tăng tuần tự. Tuy nhiên với quy mô ứng dụng hiện nay, ưu điểm về bảo mật của UUID vượt trội hơn hẳn."
