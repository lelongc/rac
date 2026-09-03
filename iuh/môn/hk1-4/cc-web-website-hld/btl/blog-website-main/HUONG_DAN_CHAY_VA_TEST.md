# 📖 HƯỚNG DẪN CẤU HÌNH, CHẠY & BỘ TESTCASE KIỂM THỬ TOÀN DIỆN (FULL SYSTEM TEST SUITE)

> **Dự án**: Website Blog & Nền tảng Viết bài trực tuyến (BTL Môn Công nghệ Web & Website Hướng Dữ Liệu - IUH)**Nhóm thực hiện**:
>
> 1. **24743991** — Hoàng Đại Dương
> 2. **24000905** — Nguyễn Trung Dũng
> 3. **23630851** — Lê Thành Long
>    **Công nghệ**: Spring Boot 3.5, Java 21, Spring Security (JWT), Spring Data JPA, **H2 File-based Persistent Database (Lưu trữ vĩnh viễn trên ổ cứng)**, MapStruct, Lombok, Thymeleaf/HTML5, CSS3, JavaScript (Bootstrap 5, Tailwind CSS, jQuery).

---

## 🗄️ 1. CƠ SỞ DỮ LIỆU LƯU TRỮ VĨNH VIỄN (PERSISTENT STORAGE)

* **Cơ chế lưu trữ**: Sử dụng **H2 Database dạng File** lưu trực tiếp tại thư mục dự án `data/blogdb.mv.db`.
* **Ưu điểm**:
  - Không cần cài đặt MySQL Server, XAMPP hay Docker.
  - **Dữ liệu được lưu vĩnh viễn 100%** vào file vật lý trên ổ cứng.
  - Khởi động lại ứng dụng, tắt máy tính hoặc reset IDE thì toàn bộ tài khoản, bài viết, like, bình luận **vẫn còn nguyên vẹn**.
* **Truy cập H2 Web Console**:
  - Đường dẫn: [http://localhost:8080/h2-console](http://localhost:8080/h2-console)
  - **Driver Class**: `org.h2.Driver`
  - **JDBC URL**: `jdbc:h2:file:./data/blogdb`
  - **User Name**: `sa`
  - **Password**: *(Để trống)*

---

## 📌 2. CẤU HÌNH & CHẠY DỰ ÁN TRÊN ECLIPSE

### 1. Yêu cầu môi trường

* **JDK**: Java 21 (hoặc Java 17+).
* **Eclipse**: Eclipse IDE for Enterprise Java and Web Developers.
* **Lombok Plugin**: Đã cài đặt trong `eclipse.ini` (`-javaagent:...lombok.jar`).

### 2. Các bước Import vào Eclipse

1. Mở Eclipse $\rightarrow$ **File** $\rightarrow$ **Import...**
2. Chọn **Maven** $\rightarrow$ **Existing Maven Projects** $\rightarrow$ **Next**.
3. Tại ô **Root Directory**, Browse đến thư mục:
   `D:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\btl\blog-website-main`
4. Bấm **Finish**.
5. **Cập nhật Maven (Bắt buộc)**:
   * Chuột phải vào tên Project (`blog-website`) $\rightarrow$ **Maven** $\rightarrow$ **Update Project...** (`Alt + F5`).
   * Tick vào ô **Force Update of Snapshots/Releases** $\rightarrow$ Bấm **OK**.

### 3. Chạy Ứng Dụng

* **Cách 1 (Từ Eclipse)**: Mở file `src/main/java/com/group/blog/BlogWebsiteApplication.java` $\rightarrow$ Chuột phải chọn **Run As** $\rightarrow$ **Java Application** (hoặc **Spring Boot App**).
* **Cách 2 (Từ Terminal / CMD)**:
  ```powershell
  .\mvnw.cmd spring-boot:run
  ```

---

## 👥 3. TÀI KHOẢN MẪU CÓ SẴN (Tất cả mật khẩu: `123456`)

| Username              | Mật khẩu | Quyền hạn (Roles)           | Ghi chú                                         |
| :-------------------- | :--------: | :---------------------------- | :----------------------------------------------- |
| **`admin`**   | `123456` | `ROLE_ADMIN`, `ROLE_USER` | Quản trị viên cao nhất của hệ thống       |
| **`duonghd`** | `123456` | `ROLE_USER`                 | Tác giả: Hoàng Đại Dương (MSSV: 24743991) |
| **`dungnt`**  | `123456` | `ROLE_USER`                 | Tác giả: Nguyễn Trung Dũng (MSSV: 24000905)  |
| **`longlt`**  | `123456` | `ROLE_USER`                 | Tác giả: Lê Thành Long (MSSV: 23630851)      |

---

## 🧪 4. BỘ TESTCASE KIỂM THỬ TOÀN DIỆN TRÊN TRÌNH DUYỆT (MANUAL UI TESTCASES)

### 📦 MODULE 1: XÁC THỰC & TÀI KHOẢN (AUTHENTICATION)

| Testcase ID          | Tên ca kiểm thử                   | Các bước thực hiện                                                                                                                                                                                           | Kết quả kỳ vọng (Expected Result)                                                                                                                                                                                                     |
| :------------------- | :----------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **TC-AUTH-01** | Đăng nhập sai mật khẩu          | 1. Vào[http://localhost:8080/login](http://localhost:8080/login)2. Nhập username `admin`, password `sai_mat_khau`3. Bấm **Đăng nhập**                                                              | Hiện Toast đỏ:*"Tên đăng nhập hoặc mật khẩu không chính xác!"*, giữ nguyên trang.                                                                                                                                        |
| **TC-AUTH-02** | Đăng nhập thành công với Admin | 1. Tại trang login, nhập`admin` / `123456`2. Bấm **Đăng nhập**                                                                                                                                    | Hiện Toast xanh thành công$\rightarrow$ tự chuyển về Trang chủ $\rightarrow$ Trên Navbar hiển thị avatar, username `admin` và nút **Admin Controller**.                                                           |
| **TC-AUTH-03** | Đăng nhập với User thường      | 1. Đăng xuất tài khoản Admin2. Đăng nhập với `duonghd` / `123456`                                                                                                                                    | Đăng nhập thành công$\rightarrow$ Navbar hiển thị username `duonghd` $\rightarrow$ **Không hiển thị** nút Admin Controller (đúng phân quyền).                                                                  |
| **TC-AUTH-04** | Đăng ký tài khoản mới          | 1. Vào[http://localhost:8080/register](http://localhost:8080/register)2. Nhập Username mới (ví dụ: `thanhvien2026`)3. Nhập Mật khẩu: `123456`, Xác nhận: `123456`4. Bấm **Đăng ký ngay** | 1. Hiện Toast xanh:*"Tạo tài khoản thành công! Đang tự động đăng nhập..."*.2. Hệ thống tự lấy JWT Token và lưu vào `localStorage`.3. Tự động chuyển hướng về Trang chủ, Navbar hiển thị user vừa tạo. |
| **TC-AUTH-05** | Đăng ký trùng tên đăng nhập  | 1. Tại trang register, nhập lại username đã tồn tại (ví dụ:`admin` hoặc `duonghd`)2. Bấm **Đăng ký ngay**                                                                                 | Hiện Toast đỏ:*"Tên đăng nhập '...' đã tồn tại! Vui lòng chọn tên đăng nhập khác."*                                                                                                                                   |
| **TC-AUTH-06** | Đăng ký mật khẩu không khớp   | 1. Tại trang register, nhập username hợp lệ, mật khẩu`123456`, xác nhận `654321`2. Bấm **Đăng ký ngay**                                                                                     | Hiện Toast cảnh báo vàng:*"Mật khẩu xác nhận không khớp. Vui lòng nhập lại!"*                                                                                                                                              |
| **TC-AUTH-07** | Đăng xuất (Logout)                | Bấm vào avatar góc phải Navbar$\rightarrow$ Chọn **Sign Out**                                                                                                                                        | Đăng xuất thành công$\rightarrow$ Xóa token trong `localStorage` $\rightarrow$ Navbar trở về nút **Sign In** và **Sign Up**.                                                                                  |

---

### 📰 MODULE 2: TRANG CHỦ, BỘ LỌC & TÌM KIẾM (HOME & FILTER)

| Testcase ID          | Tên ca kiểm thử               | Các bước thực hiện                                                                                     | Kết quả kỳ vọng (Expected Result)                                                                                                                        |
| :------------------- | :------------------------------- | :---------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **TC-HOME-01** | Hiển thị bài viết Trang chủ | Truy cập[http://localhost:8080/](http://localhost:8080/)                                                    | Danh sách bài viết tải mượt mà kèm Banner, Tiêu đề, Tác giả, Ngày đăng, Category, Tags, số lượt Thích, số Bình luận và Lượt đọc. |
| **TC-HOME-02** | Lọc theo Danh mục (Categories) | Ở thanh Sidebar bên phải, bấm vào 1 chủ đề (ví dụ:`Technology` hoặc `Programming`)           | Danh sách bài viết lọc lại ngay lập tức, chỉ hiển thị những bài thuộc danh mục được chọn.                                                  |
| **TC-HOME-03** | Sắp xếp bài viết             | Ở menu dropdown sắp xếp (Sort by), chọn:*Newest First*, *Oldest First*, hoặc *Title A-Z*         | Danh sách tự động đảo thứ tự tương ứng không cần reload lại toàn trang.                                                                       |
| **TC-HOME-04** | Tìm kiếm theo từ khóa        | Tại ô Search trên Navbar$\rightarrow$ Nhập từ khóa `Spring` $\rightarrow$ Nhấn **Enter** | Trang hiển thị đúng các bài viết có chứa từ khóa`Spring` trong tiêu đề hoặc nội dung.                                                      |

---

### 📖 MODULE 3: CHI TIẾT BÀI VIẾT & TƯƠNG TÁC (POST INTERACTIONS)

| Testcase ID          | Tên ca kiểm thử               | Các bước thực hiện                                                                                                                                | Kết quả kỳ vọng (Expected Result)                                                                                                                                                     |
| :------------------- | :------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **TC-POST-01** | Xem chi tiết bài & Tăng View  | 1. Bấm vào tiêu đề một bài viết bất kỳ từ Trang chủ2. Mở trang `/post?id=...`                                                           | Nội dung bài viết hiển thị đầy đủ chi tiết; biến đếm lượt đọc (**Views**) tự động tăng thêm 1.                                                                |
| **TC-POST-02** | Thả tim (Like / Unlike)         | Đăng nhập tài khoản$\rightarrow$ Tại trang chi tiết bài viết, bấm nút **Icon Trái tim (Like)**                                     | Lượt like tăng lên 1, icon chuyển sang màu đỏ (Active). Bấm thêm lần nữa$\rightarrow$ Hủy like, số tim giảm về ban đầu.                                               |
| **TC-POST-03** | Bình luận bài viết (Comment) | Cuộn xuống phần Bình luận$\rightarrow$ Nhập nội dung: *"Bài viết rất hay và bổ ích!"* $\rightarrow$ Bấm **Gửi bình luận** | Bình luận xuất hiện ngay tức thì kèm tên người gửi, avatar và thời gian vừa đăng.                                                                                         |
| **TC-POST-04** | Lưu bài viết (Bookmark)       | Bấm vào biểu tượng**Bookmark (Lưu bài)** ở đầu hoặc cuối bài viết                                                                  | Icon đổi trạng thái đã lưu. Truy cập trang[http://localhost:8080/saved-blogs](http://localhost:8080/saved-blogs) $\rightarrow$ Thấy bài viết nằm trong danh sách đã lưu. |

---

### ✍️ MODULE 4: SOẠN THẢO & QUẢN LÝ BÀI VIẾT CÁ NHÂN

| Testcase ID          | Tên ca kiểm thử             | Các bước thực hiện                                                                                                                                                                                                                                                   | Kết quả kỳ vọng (Expected Result)                                                                                            |
| :------------------- | :----------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------- |
| **TC-BLOG-01** | Viết & Đăng bài mới       | 1. Đăng nhập với`duonghd`2. Bấm nút **Write** trên Navbar (hoặc vào [http://localhost:8080/blog-editor](http://localhost:8080/blog-editor))3. Nhập Tiêu đề, chọn Danh mục, nhập Tags, dán URL ảnh banner, gõ nội dung4. Bấm **Publish** | Báo xuất bản thành công$\rightarrow$ Quay lại Trang chủ thấy ngay bài viết mới vừa đăng ở vị trí đầu tiên. |
| **TC-BLOG-02** | Quản lý bài viết của tôi | Vào trang[http://localhost:8080/manage-blogs](http://localhost:8080/manage-blogs)                                                                                                                                                                                         | Hiển thị toàn bộ các bài do tài khoản`duonghd` đã viết kèm các nút thao tác: Xem, Chỉnh sửa, Xóa.            |

---

### 👤 MODULE 5: PROFILE, ĐỔI MẬT KHẨU & THEO DÕI (USER PROFILE)

| Testcase ID          | Tên ca kiểm thử           | Các bước thực hiện                                                                                                                                                                             | Kết quả kỳ vọng (Expected Result)                                                                                                                |
| :------------------- | :--------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| **TC-USER-01** | Xem trang hồ sơ cá nhân  | Truy cập[http://localhost:8080/user-profile](http://localhost:8080/user-profile)                                                                                                                    | Hiển thị đúng Avatar, Bio, Email, số lượng người theo dõi (Followers), số đang theo dõi (Following) và các bài viết của user đó. |
| **TC-USER-02** | Chỉnh sửa hồ sơ          | Truy cập[http://localhost:8080/edit-profile](http://localhost:8080/edit-profile) $\rightarrow$ Sửa Bio thành *"Sinh viên IUH đam mê Spring Boot"* $\rightarrow$ Bấm **Save**      | Thông tin được cập nhật và lưu vào cơ sở dữ liệu.                                                                                       |
| **TC-USER-03** | Đổi mật khẩu             | 1. Vào[http://localhost:8080/change-password](http://localhost:8080/change-password)2. Nhập mật khẩu cũ `123456`3. Nhập mật khẩu mới `654321` $\rightarrow$ Bấm **Cập nhật** | Báo đổi mật khẩu thành công. Thử đăng xuất và đăng nhập lại bằng`654321` $\rightarrow$ Đăng nhập thành công.               |
| **TC-USER-04** | Theo dõi tác giả (Follow) | Vào bài viết của một tác giả khác$\rightarrow$ Bấm nút **Follow** cạnh tên tác giả                                                                                            | Trạng thái chuyển thành**Following**, số lượng followers của tác giả đó tăng 1.                                                   |

---

### 🔔 MODULE 6: TRUNG TÂM THÔNG BÁO (NOTIFICATIONS)

| Testcase ID          | Tên ca kiểm thử             | Các bước thực hiện                                                                                                                                                                                             | Kết quả kỳ vọng (Expected Result)                                                                           |
| :------------------- | :----------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------- |
| **TC-NOTI-01** | Nhận thông báo tương tác | 1. Dùng tài khoản`dungnt` vào like hoặc comment bài viết của `duonghd`2. Đăng xuất và đăng nhập vào `duonghd`3. Mở [http://localhost:8080/notifications](http://localhost:8080/notifications) | Xuất hiện thông báo:*"dungnt đã thích/bình luận bài viết của bạn"* kèm thời gian tương ứng. |
| **TC-NOTI-02** | Đánh dấu đã đọc         | Bấm vào thông báo                                                                                                                                                                                               | Thông báo chuyển từ trạng thái chưa đọc sang đã đọc.                                               |

---

### 🛡️ MODULE 7: QUẢN TRỊ VIÊN HỆ THỐNG (ADMIN DASHBOARD)

| Testcase ID         | Tên ca kiểm thử        | Các bước thực hiện                                                                                                                                                        | Kết quả kỳ vọng (Expected Result)                                                                                  |
| :------------------ | :------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| **TC-ADM-01** | Xem Dashboard thống kê  | Đăng nhập tài khoản`admin` $\rightarrow$ Truy cập [http://localhost:8080/admin/dashboard](http://localhost:8080/admin/dashboard)                                      | Thống kê chính xác:**Total Users**, **Total Posts**, bảng danh sách bài viết gần đây.           |
| **TC-ADM-02** | Quản lý thành viên    | Vào trang[http://localhost:8080/admin/users](http://localhost:8080/admin/users)                                                                                                | Hiển thị bảng danh sách toàn bộ người dùng trong hệ thống kèm thông tin vai trò (ROLE_ADMIN, ROLE_USER). |
| **TC-ADM-03** | Quản lý bài viết      | Vào trang[http://localhost:8080/admin/posts](http://localhost:8080/admin/posts)                                                                                                | Cho phép Admin xem tất cả bài của mọi tác giả, tìm kiếm và kiểm duyệt/xóa bài viết.                    |
| **TC-ADM-04** | Quản lý Danh mục & Tag | Vào trang[http://localhost:8080/admin/categories-tags](http://localhost:8080/admin/categories-tags) $\rightarrow$ Thêm 1 danh mục mới (ví dụ: `Trí tuệ nhân tạo`) | Danh mục mới xuất hiện ngay trên bảng và xuất hiện ở Sidebar lọc bài viết ngoài trang chủ.              |

---

### 🔒 MODULE 8: BẢO MẬT & LƯU TRỮ DỮ LIỆU BỀN VỮNG (PERSISTENCE)

| Testcase ID         | Tên ca kiểm thử                           | Các bước thực hiện                                                                                                                                         | Kết quả kỳ vọng (Expected Result)                                                                                                                     |
| :------------------ | :------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **TC-SEC-01** | Chặn User thường vào API Admin           | Đăng nhập tài khoản`duonghd` (không có quyền ADMIN) $\rightarrow$ Gọi `GET /api/admin/stats`                                                     | Spring Security chặn lại và trả về mã lỗi**`403 Forbidden`**.                                                                              |
| **TC-DB-01**  | Kiểm tra CSDL qua H2 Console                | 1. Truy cập[http://localhost:8080/h2-console](http://localhost:8080/h2-console)2. Nhập JDBC URL: `jdbc:h2:file:./data/blogdb`3. Bấm **Connect**       | Đăng nhập thành công$\rightarrow$ Thấy đầy đủ cây bảng: `USERS`, `BLOGS`, `COMMENTS`, `CATEGORIES`, `TAGS`, `NOTIFICATIONS`,... |
| **TC-DB-02**  | Kiểm tra Lưu trữ Vĩnh viễn (Persistent) | 1. Đăng ký một user mới hoặc viết 1 bài mới.2. Tắt hẳn ứng dụng Spring Boot.3. Khởi động lại ứng dụng Spring Boot.4. Mở lại trình duyệt. | **Dữ liệu bài viết/tài khoản vừa tạo vẫn còn nguyên 100%**, không hề bị mất (nhờ cơ chế file `data/blogdb.mv.db`).              |

---

## 💻 5. CHẠY KỊCH BẢN KIỂM THỬ TỰ ĐỘNG (AUTOMATED TEST SUITE)

Để kiểm tra nhanh 48 kịch bản API, phân quyền và giao diện:

```powershell
pwsh -File test_suite.ps1
```

* **Kết quả**:

```text
================ TEST SUMMARY ================
Total Tests: 48 | Passed: 48 (100%) | Failed: 0
==============================================
```
