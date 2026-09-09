# GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG AUTHENTICATIONCONTROLLER VÀ USERCONTROLLER

> **Mục tiêu**: Hiểu rõ tầng tiếp nhận HTTP Request của hệ thống xác thực và quản lý người dùng. Nắm chắc cấu trúc bao bọc dữ liệu `ApiResponse<T>`, quy tắc thứ tự định tuyến URL trong Spring MVC (Tránh bẫy lỗi PathVariable đè lên Static Route), và cách bảo mật các Endpoint cá nhân (`/my-profile`).

---

## 1. MÃ NGUỒN VÀ GIẢI THÍCH `AuthenticationController.java`

File nằm tại: `src/main/java/com/group/blog/controller/AuthenticationController.java`

```java
package com.group.blog.controller;

import com.group.blog.dto.request.ApiResponse;
import com.group.blog.dto.request.AuthenticationRequest;
import com.group.blog.dto.request.IntrospectRequest;
import com.group.blog.dto.response.AuthenticationResponse;
import com.group.blog.dto.response.IntrospectResponse;
import com.group.blog.service.AuthenticationService;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/auth")
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class AuthenticationController {
    AuthenticationService authenticationService;

    @PostMapping("/login")
    ApiResponse<AuthenticationResponse> authenticate(@RequestBody AuthenticationRequest authenticationRequest) {
        var result = authenticationService.authenticate(authenticationRequest);
        return ApiResponse.<AuthenticationResponse>builder()
                .result(result)
                .build();
    }

    @PostMapping("/introspect")
    ApiResponse<IntrospectResponse> introspect(@RequestBody IntrospectRequest request){
        var result = authenticationService.introspect(request);
        return ApiResponse.<IntrospectResponse>builder()
                .result(result)
                .build();
    }
}
```

### Giải thích chi tiết:
- **`@RestController`**: Là sự kết hợp của `@Controller` và `@ResponseBody`. Báo cho Spring Boot biết mọi giá trị trả về từ các hàm này sẽ được Jackson Serializer tự động chuyển thành chuỗi định dạng **JSON** để gửi về cho Client, chứ không phải là tên file giao diện HTML.
- **`@RequestMapping("/auth")`**: Tiền tố URL chung cho tất cả các API trong Controller này.
- **`@PostMapping("/login")`**: Tiếp nhận HTTP POST đến `http://localhost:8080/auth/login`.
  - `@RequestBody`: Lấy nội dung chuỗi JSON trong phần thân của HTTP Request (Body) và ép kiểu tự động thành đối tượng Java `AuthenticationRequest`.
  - Kết quả trả về được đóng gói vào lớp chuẩn hóa `ApiResponse<AuthenticationResponse>`.
- **`@PostMapping("/introspect")`**: Tiếp nhận HTTP POST đến `http://localhost:8080/auth/introspect` để kiểm tra tính hợp lệ của Token.

---

## 2. MÃ NGUỒN VÀ GIẢI THÍCH `UserController.java`

File nằm tại: `src/main/java/com/group/blog/controller/UserController.java`

```java
package com.group.blog.controller;

import com.group.blog.dto.request.ApiResponse;
import com.group.blog.dto.request.PasswordChangeRequest;
import com.group.blog.dto.request.UserCreatetionRequest;
import com.group.blog.dto.request.UserUpdateRequest;
import com.group.blog.dto.response.UserResponse;
import com.group.blog.service.UserService;
import jakarta.validation.Valid;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.UUID;

@Slf4j
@RestController
@RequestMapping("/users")
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class UserController {
    UserService userService;

    // 1. Đăng ký tài khoản mới (Public)
    @PostMapping()
    ApiResponse<UserResponse> createUser(@RequestBody @Valid UserCreatetionRequest request){
        ApiResponse<UserResponse> apiResponse = new ApiResponse<>();
        apiResponse.setResult(userService.createUser(request));
        return apiResponse;
    }

    // 2. Lấy danh sách tất cả user (Yêu cầu quyền ADMIN)
    @GetMapping
    ApiResponse<List<UserResponse>> getUsers() {
        return ApiResponse.<List<UserResponse>>builder()
                .result(userService.getUsers())
                .build();
    }

    // 3. Lấy thông tin cá nhân của người đang đăng nhập
    @GetMapping("/my-profile")
    public ApiResponse<UserResponse> getMyProfile() {
        return ApiResponse.<UserResponse>builder()
                .result(userService.getMyProfile())
                .build();
    }

    // 4. Cập nhật thông tin cá nhân của người đang đăng nhập
    @PutMapping("/my-profile")
    public ApiResponse<UserResponse> updateMyProfile(@RequestBody @Valid UserUpdateRequest request) {
        return ApiResponse.<UserResponse>builder()
                .result(userService.updateMyProfile(request))
                .build();
    }

    // 5. Đổi mật khẩu tài khoản đang đăng nhập
    @PutMapping("/my-profile/change-password")
    public ApiResponse<String> changePassword(@RequestBody @Valid PasswordChangeRequest request) {
        userService.changePassword(request);
        return ApiResponse.<String>builder()
                .result("Password has been changed successfully")
                .build();
    }

    // 6. Lấy chi tiết user theo ID (Admin hoặc nội bộ)
    @GetMapping("/{userId}")
    ApiResponse<UserResponse> getUser(@PathVariable("userId") UUID userId) {
        ApiResponse<UserResponse> apiResponse = new ApiResponse<>();
        apiResponse.setResult(userService.getUser(userId));
        return apiResponse;
    }

    // 7. Cập nhật user theo ID (Dành cho Admin phân quyền)
    @PutMapping("/{userId}")
    ApiResponse<UserResponse> updateUser(@PathVariable("userId") UUID userId, @RequestBody @Valid UserUpdateRequest request) {
        ApiResponse<UserResponse> apiResponse = new ApiResponse<>();
        apiResponse.setResult(userService.updateUser(userId, request));
        return apiResponse;
    }

    // 8. Xóa user theo ID (Admin)
    @DeleteMapping("/{userId}")
    ApiResponse<String> deleteUser(@PathVariable("userId") UUID userId) {
        userService.deleteUser(userId);
        ApiResponse<String> apiResponse = new ApiResponse<>();
        apiResponse.setResult("User has been deleted");
        return apiResponse;
    }

    // 9. Xem trang hồ sơ công khai của một tác giả dựa vào username
    @GetMapping("/profile/{username}")
    public ApiResponse<UserResponse> getUserByUsername(@PathVariable String username) {
        return ApiResponse.<UserResponse>builder()
                .result(userService.getUserByUsername(username))
                .build();
    }
}
```

---

## 3. BẪY KỸ THUẬT QUAN TRỌNG: THỨ TỰ ĐẶT ĐƯỜNG DẪN URL TRONG CONTROLLER

Hãy quan sát vị trí của 2 phương thức sau trong file:
- Phương thức 3: `@GetMapping("/my-profile")` (Đường dẫn tĩnh)
- Phương thức 6: `@GetMapping("/{userId}")` (Đường dẫn động chứa biến `@PathVariable`)

### Tại sao bắt buộc phải đặt `@GetMapping("/my-profile")` lên TRƯỚC `@GetMapping("/{userId}")`?
- **Nguyên lý của Spring MVC DispatcherServlet**:
  - Khi có một request gửi đến `GET /users/my-profile`, Spring sẽ duyệt danh sách các route từ trên xuống dưới.
  - Nếu chúng ta đặt `@GetMapping("/{userId}")` lên trên đầu: Spring sẽ hiểu lầm chuỗi `"my-profile"` chính là giá trị của biến `{userId}`.
  - Khi Spring cố gắng ép chuỗi `"my-profile"` thành kiểu dữ liệu `UUID`, một ngoại lệ nghiêm trọng sẽ xảy ra:
    ```
    MethodArgumentTypeMismatchException: Failed to convert value of type 'java.lang.String' to required type 'java.util.UUID'
    ```
  - Kết quả là API `/my-profile` bị sập hoàn toàn (lỗi 400 Bad Request)!
  - **Quy tắc vàng**: Các đường dẫn tĩnh cụ thể (`/my-profile`, `/search`) luôn luôn phải được khai báo **trước** các đường dẫn chứa tham số biến đổi (`/{id}`, `/{userId}`).

---

## 4. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN VỀ CONTROLLER & TRẢ LỜI ĐIỂM 10

### Câu 1: Annotation `@Valid` trong các tham số hàm của Controller có tác dụng gì?
- **Trả lời**:
  > "Thưa thầy/cô, `@Valid` là annotation của thư viện Jakarta Bean Validation:
  > - Khi được đặt trước tham số `@RequestBody`, nó yêu cầu Spring tự động quét và kiểm tra các ràng buộc dữ liệu được khai báo trong DTO (như `@NotBlank`, `@Size(min = 6)`, `@Email`).
  > - Nếu dữ liệu người dùng gửi lên không thỏa mãn (ví dụ: mật khẩu ngắn hơn 6 ký tự hoặc email sai định dạng), Spring sẽ tự động chặn request lại ngay lập tức và ném ra ngoại lệ `MethodArgumentNotValidException`. 
  > - Nhờ đó dữ liệu bẩn bị chặn ngay tại cửa ngõ Controller, không thể lọt xuống tầng Service."

### Câu 2: Em hãy giải thích cấu trúc và tác dụng của lớp vỏ `ApiResponse<T>`?
- **Trả lời**:
  > "Thưa thầy/cô, `ApiResponse<T>` là một mẫu thiết kế chuẩn hóa phản hồi RESTful API:
  > Nó đóng gói 3 trường:
  > 1. `code`: Mã trạng thái nội bộ (Mặc định `1000` là thành công, các mã `1001, 1002...` đại diện cho các lỗi cụ thể).
  > 2. `message`: Lời nhắn giải thích ngắn gọn bằng tiếng Anh/Việt.
  > 3. `result`: Dữ liệu thực tế thuộc kiểu Generic `T` (có thể là User, Blog, hoặc List).
  > 
  > Nhờ có `ApiResponse`, mọi phản hồi trả về từ hệ thống đều có cùng một cấu trúc JSON đồng nhất. Phía lập trình viên Frontend (file `auth.js`, `posts.js`) chỉ cần viết một hàm xử lý duy nhất: kiểm tra `if (data.code === 1000)` để hiển thị kết quả thành công, cực kỳ dễ bảo trì và mở rộng."
