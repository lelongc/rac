# KHÁI NIỆM SPRING DATA JPA VÀ CƠ CHẾ HOẠT ĐỘNG NGẦM

> **Mục tiêu**: Hiểu bản chất công nghệ Spring Data JPA: Tại sao chỉ cần khai báo một `interface` không có code thân hàm mà ứng dụng vẫn thực thi được câu lệnh SQL xuống database? Cơ chế sinh query tự động từ tên hàm (Derived Query Methods) và cách tối ưu câu lệnh JPQL với `@Query`.

---

## 1. SPRING DATA JPA LÀ GÌ?

Trong lập trình Java truyền thống (JDBC thuần), để lấy thông tin một người dùng theo username, lập trình viên phải viết hàng chục dòng code phức tạp:
```java
// Cách cũ (JDBC thuần) - Rất dài dòng và dễ lỗi:
Connection conn = DriverManager.getConnection(url, user, pass);
PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE username = ?");
ps.setString(1, "admin");
ResultSet rs = ps.executeQuery();
if (rs.next()) {
    User user = new User();
    user.setId(UUID.fromString(rs.getString("id")));
    user.setUsername(rs.getString("username"));
    // ... gọi hàng chục hàm set thủ công
}
```

**Với Spring Data JPA trong dự án này**:
Lập trình viên chỉ cần khai báo đúng một dòng:
```java
public interface UserRepository extends JpaRepository<User, UUID> {
    Optional<User> findByUsername(String username);
}
```
Không cần viết một dòng `SELECT`, không cần mở đóng Connection, không cần ánh xạ ResultSet!

---

## 2. CƠ CHẾ SINH QUERY TỰ ĐỘNG TỪ TÊN HÀM (DERIVED QUERY METHODS)

Spring Data JPA sở hữu một bộ phân tích cú pháp (Parser) cực kỳ thông minh. Nó tự động "bóc tách" tên phương thức của bạn thành các mệnh đề SQL tương ứng:

| Tên phương thức Java trong dự án | Cú pháp SQL tương đương do Hibernate sinh ra |
| :--- | :--- |
| `findByUsername(String username)` | `SELECT * FROM users WHERE username = ?` |
| `existsByUsername(String username)` | `SELECT COUNT(1) FROM users WHERE username = ?` |
| `existsByBlogIdAndUserUsername(UUID blogId, String username)` | `SELECT COUNT(1) FROM blog_likes l JOIN users u ON l.user_id = u.id WHERE l.blog_id = ? AND u.username = ?` |
| `findByUserUsernameOrderByCreatedAtDesc(String username)` | `SELECT * FROM bookmarks b JOIN users u ON b.user_id = u.id WHERE u.username = ? ORDER BY b.created_at DESC` |
| `findTop5ByDraftFalseOrderByCreatedAtDesc()` | `SELECT * FROM blogs WHERE draft = false ORDER BY created_at DESC LIMIT 5` |
| `countByBlogId(UUID blogId)` | `SELECT COUNT(*) FROM comments WHERE blog_id = ?` |

### Quy tắc đặt tên từ khóa của Spring Data JPA:
- **`findBy...`**: Truy vấn danh sách hoặc đối tượng thỏa mãn điều kiện.
- **`existsBy...`**: Kiểm tra có tồn tại hay không, trả về `boolean` (rất nhanh vì không cần nạp toàn bộ thực thể vào bộ nhớ).
- **`countBy...`**: Đếm số lượng bản ghi thỏa điều kiện, trả về `long`.
- **`OrderBy...Desc / Asc`**: Sắp xếp theo chiều giảm dần hoặc tăng dần của một trường thời gian/số.
- **`Top5`**: Giới hạn lấy 5 bản ghi đầu tiên (tương đương mệnh đề `LIMIT 5` trong MySQL).
- **`ContainingIgnoreCase`**: Tìm kiếm tương đối không phân biệt hoa thường (tương đương `LOWER(column) LIKE %value%`).

---

## 3. TẠI SAO DÙNG `Optional<T>` LÀM KIỂU TRẢ VỀ?
Trong các hàm tìm kiếm như `findByUsername` hay `findById`, dự án luôn trả về `Optional<User>` thay vì `User` trực tiếp.
- **Ý nghĩa sống còn**: Nếu không tìm thấy người dùng, hàm sẽ trả về `Optional.empty()` thay vì giá trị `null`.
- Ở tầng Service, lập trình viên có thể viết code bắt lỗi cực kỳ thanh lịch và an toàn:
  ```java
  User user = userRepository.findByUsername(username)
          .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXISTED));
  ```
  Cách này triệt tiêu hoàn toàn nỗi ám ảnh lỗi `NullPointerException` làm sập server!

---

## 4. KỸ THUẬT VIẾT JPQL VÀ GIẢI QUYẾT BÀI TOÁN N+1 QUERIES BẰNG `@Query`

Trong file `BlogRepository.java`, chúng ta bắt gặp những câu truy vấn rất đặc biệt:

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

### 4.1. JPQL là gì?
- JPQL (Java Persistence Query Language) là ngôn ngữ truy vấn hướng đối tượng của JPA.
- Điểm khác biệt so với SQL: Trong SQL bạn thao tác với tên bảng (`blogs`) và tên cột (`category_id`), còn trong JPQL bạn thao tác với **tên lớp Entity (`Blog b`)** và **tên thuộc tính (`b.category`)**.

### 4.2. Vấn đề N+1 Queries là gì?
- Giả sử trang chủ hiển thị 10 bài viết. Với mỗi bài viết, chúng ta cần hiển thị: Bài này có bao nhiêu like? Bao nhiêu view? Bao nhiêu comment?
- Nếu làm theo cách ngây thơ: 
  - 1 câu truy vấn lấy 10 bài viết.
  - Sau đó lặp qua từng bài viết để gọi `countLike()`, `countView()`, `countComment()`.
  - Tổng cộng hệ thống phải bắn: `1 + (10 * 3) = 31 câu lệnh SQL` xuống Database! Nếu có 1000 người cùng vào trang chủ, database sẽ bị treo ngay lập tức.

### 4.3. Giải pháp tối ưu đỉnh cao của nhóm:
- Câu lệnh `@Query` trên dùng phép nối ngoài `LEFT JOIN` và nhóm `GROUP BY b`.
- Chỉ trong **DUY NHẤT 1 CÂU LỆNH SQL**, hệ thống đã lấy được cả đối tượng `Blog` cùng lúc với 3 con số thống kê đếm phân biệt (`COUNT(DISTINCT ...)`).
- Kết quả trả về là `List<Object[]>`, trong đó:
  - `object[0]`: Đối tượng `Blog`.
  - `object[1]`: Số lượt xem (`Long`).
  - `object[2]`: Số lượt thích (`Long`).
  - `object[3]`: Số lượng bình luận (`Long`).
- Tốc độ load trang chủ tăng gấp hàng chục lần và giảm tải tối đa cho cơ sở dữ liệu.

---

## 5. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN & TRẢ LỜI ĐIỂM 10

### Câu 1: Em hãy giải thích tại sao interface Repository không có class nào `implements` nó mà Spring Boot vẫn gọi được hàm?
- **Trả lời**:
  > "Thưa thầy/cô, Spring Data JPA sử dụng kỹ thuật **Dynamic Proxy (Proxy động)** của Java kết hợp với Spring AOP (Aspect-Oriented Programming):
  > Khi ứng dụng khởi động, Spring quét qua các interface kế thừa `JpaRepository`. Tại thời điểm Runtime, Spring tự động tạo ra một lớp ẩn trung gian (Proxy class) cài đặt interface này và nạp các câu lệnh thực thi JDBC vào trong các phương thức. Do đó lập trình viên chúng em không cần phải viết class `implements` thủ công."

### Câu 2: Tại sao trong hàm `@Query` ở BlogRepository phải dùng `COUNT(DISTINCT l.id)` mà không thể dùng `COUNT(l.id)` thông thường?
- **Trả lời**:
  > "Thưa thầy/cô, đây là một lỗi bẫy kinh điển trong SQL khi JOIN nhiều bảng 1-nhiều:
  > Nếu một bài viết có 3 lượt like và 2 comment, khi chúng ta `LEFT JOIN` cả bảng `BlogLike` và `Comment`, tích Descartes (Cartesian product) sẽ nhân số dòng lên thành `3 x 2 = 6 dòng`.
  > Nếu chỉ dùng `COUNT(l.id)`, kết quả đếm like sẽ bị nhân sai thành 6 thay vì 3!
  > Từ khóa **`DISTINCT`** bắt buộc CSDL chỉ đếm các ID duy nhất khác nhau, loại bỏ hoàn toàn các dòng bị trùng do phép JOIN, đảm bảo kết quả đếm số like, view, comment luôn chuẩn xác 100%."
