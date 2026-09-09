# HƯỚNG DẪN SỬA CODE TRỰC TIẾP (LIVE CODING) KHI GIẢNG VIÊN YÊU CẦU

> **Bí kíp thực chiến**: Trong phòng thi vấn đáp, giảng viên thường xuyên đưa ra các yêu cầu sửa code tại chỗ để kiểm tra xem sinh viên có thực sự tự tay làm đồ án hay đi thuê/copy code. Tài liệu này cung cấp hướng dẫn từng bước xử lý 6 tình huống giảng viên hay yêu cầu sửa nhất.

---

## TÌNH HUỐNG 1: "HÃY THÊM MỘT TRƯỜNG MỚI VÀO USER HOẶC BLOG" (VÍ DỤ: SỐ ĐIỆN THOẠI `phoneNumber`)

Nếu thầy/cô yêu cầu: *"Bây giờ em thêm trường số điện thoại cho User và cho phép cập nhật xem nào!"*

### Các bước thực hiện nhanh trong 2 phút:
1. **Bước 1: Mở `User.java` (Entity)**:
   Thêm biến vào lớp `User`:
   ```java
   String phoneNumber;
   ```
   *(Nhờ Hibernate cấu hình `ddl-auto: update`, khi restart server Hibernate sẽ tự động chạy câu lệnh `ALTER TABLE users ADD COLUMN phone_number VARCHAR(255)` vào Database mà không làm mất dữ liệu cũ!)*

2. **Bước 2: Mở `UserUpdateRequest.java` (DTO Request)**:
   Thêm trường để nhận dữ liệu từ form:
   ```java
   String phoneNumber;
   ```

3. **Bước 3: Mở `UserResponse.java` (DTO Response)**:
   Thêm trường để trả về cho Frontend:
   ```java
   String phoneNumber;
   ```

4. **Bước 4: Mở `UserService.java` (Service)**:
   Trong hàm `updateMyProfile()`, thêm dòng gán giá trị:
   ```java
   if (request.getPhoneNumber() != null) user.setPhoneNumber(request.getPhoneNumber());
   ```

5. **Bước 5**: Nhấn Save và Restart server -> Vào Postman hoặc trang web kiểm tra -> Xong trọn vẹn điểm 10!

---

## TÌNH HUỐNG 2: "HÃY ĐỔI LUẬT VALIDATE MẬT KHẨU HOẶC TIÊU ĐỀ"

Nếu thầy/cô yêu cầu: *"Thầy thấy mật khẩu tối thiểu 8 ký tự dài quá, giờ em sửa lại tối thiểu 6 ký tự xem!"*

### Cách sửa:
1. Mở file `UserCreatetionRequest.java`:
   Tìm dòng:
   ```java
   @Size(min = 8, message = "INVALID_PASSWORD")
   String password;
   ```
   Sửa số `8` thành số `6`:
   ```java
   @Size(min = 6, message = "INVALID_PASSWORD")
   String password;
   ```
2. Mở file `ErrorCode.java`:
   Sửa câu thông báo lỗi cho tương ứng:
   ```java
   INVALID_PASSWORD(1004, "Mật khẩu phải chứa ít nhất 6 ký tự"),
   ```
3. Lưu lại và thử nhập mật khẩu 6 ký tự trên form đăng ký -> Chạy thành công ngay lập tức!

---

## TÌNH HUỐNG 3: "CHẶN THÊM MỘT API CHỈ CHO ADMIN MỚI ĐƯỢC PHÉP TRUY CẬP"

Nếu thầy/cô yêu cầu: *"Hiện tại API xem danh sách comment ai cũng vào được, giờ em sửa sao cho chỉ có ADMIN mới được xem?"*

### Cách sửa trong `SecurityConfig.java`:
1. Mở file `src/main/java/com/group/blog/config/SecurityConfig.java`.
2. Tìm mảng `PUBLIC_GET_ENDPOINTS`:
   Xóa bỏ hoặc comment dòng:
   ```java
   // "/blogs/*/comments",
   ```
3. Tìm trong khối `.authorizeHttpRequests(...)`:
   Thêm dòng chặn quyền Admin:
   ```java
   .requestMatchers(HttpMethod.GET, "/blogs/*/comments").hasRole(Role.ADMIN.name())
   ```
4. Lưu file và restart server. Bây giờ nếu không có Token của Admin, người dùng bình thường gửi request GET vào xem comment sẽ lập tức nhận mã lỗi `403 Forbidden`!

---

## TÌNH HUỐNG 4: "ĐỔI CỔNG CHẠY SERVER TỪ 8080 SANG 8081"

Nếu thầy/cô yêu cầu: *"Máy của thầy bị trùng cổng 8080 với Oracle rồi, em đổi cổng web sang 8081 chạy thử xem?"*

### Cách sửa:
1. Mở file `src/main/resources/application.yaml`:
   Sửa dòng số 2:
   ```yaml
   server:
     port: 8081
   ```
2. Lưu file và chạy lại ứng dụng: `mvn spring-boot:run`.
3. Ứng dụng sẽ khởi động ngay lập tức tại địa chỉ: `http://localhost:8081`.

---

## TÌNH HUỐNG 5: "HÃY TẠO THÊM MỘT TÀI KHOẢN MẶC ĐỊNH MỚI KHI KHỞI ĐỘNG"

Nếu thầy/cô yêu cầu: *"Giờ em thêm một tài khoản giáo viên `teacher` với mật khẩu `123456` có quyền ADMIN khi hệ thống vừa bật lên xem?"*

### Cách sửa trong `ApplicationInitConfig.java`:
1. Mở file `src/main/java/com/group/blog/config/ApplicationInitConfig.java`.
2. Trong hàm `applicationRunner`, thêm đoạn code sau:
   ```java
   if (userRepository.findByUsername("teacher").isEmpty()) {
       Set<String> teacherRoles = new HashSet<>();
       teacherRoles.add(Role.ADMIN.name());
       teacherRoles.add(Role.USER.name());

       User teacher = User.builder()
               .username("teacher")
               .email("teacher@iuh.edu.vn")
               .password(passwordEncoder.encode("123456"))
               .bio("Giảng viên hướng dẫn môn Công nghệ Web")
               .roles(teacherRoles)
               .build();
       userRepository.save(teacher);
       log.info("Initialized Teacher Account Successfully!");
   }
   ```
3. Lưu file và restart server -> Console in ra dòng thông báo tạo tài khoản thành công -> Dùng tài khoản `teacher` / `123456` đăng nhập được ngay!

---

## TÌNH HUỐNG 6: "MỞ TRỰC TIẾP CƠ SỞ DỮ LIỆU LÊN CHO THẦY CÔ XEM DỮ LIỆU ĐANG LƯU NHƯ THẾ NÀO"

Nếu thầy/cô yêu cầu: *"Dữ liệu nãy giờ em nhập lưu ở đâu? Mở trực tiếp CSDL lên cho thầy xem các bảng USERS và BLOGS!"*

### Các thao tác chỉ tay mượt mà:
1. Mở trình duyệt, truy cập địa chỉ: `http://localhost:8080/h2-console`.
2. Tại màn hình đăng nhập của H2 Console, kiểm tra chính xác các thông số:
   - **JDBC URL**: Điền đúng chuỗi kết nối trong `application.yaml`:
     ```
     jdbc:h2:file:./data/blogdb;AUTO_SERVER=TRUE;DB_CLOSE_DELAY=-1;MODE=MySQL;DATABASE_TO_LOWER=TRUE;CASE_INSENSITIVE_IDENTIFIERS=TRUE
     ```
   - **User Name**: `sa`
   - **Password**: Để trống hoàn toàn.
3. Bấm nút **"Connect"**.
4. Màn hình quản trị mở ra:
   - Ở cột bên trái, chỉ vào các bảng: `USERS`, `BLOGS`, `COMMENTS`, `BLOG_LIKES`, `BOOKMARKS`.
   - Gõ câu lệnh SQL: `SELECT * FROM USERS;` -> Bấm **Run** -> Thấy rõ danh sách các tài khoản với mật khẩu đã được mã hóa chuỗi `$2a$10$...`.
   - Gõ câu lệnh SQL: `SELECT * FROM BLOGS;` -> Bấm **Run** -> Thấy rõ các bài viết vừa tạo.
   - Thầy cô sẽ cực kỳ ấn tượng vì nhóm hiểu tường tận từ mã nguồn đến tận đáy cơ sở dữ liệu!
