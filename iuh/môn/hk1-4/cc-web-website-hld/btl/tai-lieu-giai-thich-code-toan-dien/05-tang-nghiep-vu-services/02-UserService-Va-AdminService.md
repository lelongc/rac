# GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG USERSERVICE VÀ ADMINSERVICE

> **Mục tiêu**: Hiểu trọn vẹn nghiệp vụ quản lý người dùng (Đăng ký tài khoản mới, kiểm tra trùng lặp, cập nhật thông tin hồ sơ, đổi mật khẩu an toàn) và nghiệp vụ thu thập dữ liệu thống kê bảng điều khiển quản trị viên (Admin Dashboard Analytics).

---

## 1. MÃ NGUỒN ĐẦY ĐỦ CỦA `UserService.java`

File nằm tại: `src/main/java/com/group/blog/service/UserService.java`

```java
package com.group.blog.service;

import com.group.blog.dto.request.PasswordChangeRequest;
import com.group.blog.dto.request.UserCreatetionRequest;
import com.group.blog.dto.request.UserUpdateRequest;
import com.group.blog.dto.response.UserResponse;
import com.group.blog.entity.User;
import com.group.blog.enums.Role;
import com.group.blog.exception.AppException;
import com.group.blog.exception.ErrorCode;
import com.group.blog.mapper.UserMapper;
import com.group.blog.repository.UserRepository;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.UUID;

@Service
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class UserService {

    UserRepository userRepository;
    UserMapper userMapper;
    PasswordEncoder passwordEncoder;
    FollowService followService;

    public UserResponse createUser(UserCreatetionRequest request){
        if(userRepository.existsByUsername(request.getUsername())) 
            throw new AppException(ErrorCode.USER_EXITED);

        User u = userMapper.toUser(request);
        if(u.getRoles() == null) u.setRoles(new HashSet<>());
        u.setPassword(passwordEncoder.encode(request.getPassword()));
        u.getRoles().add(Role.USER.name());
        User savedUser = userRepository.save(u);
        return userMapper.toUserResponse(savedUser);
    }

    public UserResponse updateUser(UUID id, UserUpdateRequest request){
        User u = userRepository.findById(id)
                .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));

        userMapper.updateUser(u, request);

        if (request.getRoles() != null && !request.getRoles().isEmpty()) {
            u.getRoles().clear();
            u.getRoles().addAll(request.getRoles());
        }

        return followService.enrichUserResponse(userRepository.save(u));
    }

    public void deleteUser(UUID id){
        if(!userRepository.existsById(id)) throw new AppException(ErrorCode.USER_NOT_EXITED);
        userRepository.deleteById(id);
    }

    public List<UserResponse> getUsers(){
        return userRepository.findAll().stream().map(followService::enrichUserResponse).toList();
    }

    public UserResponse getUser(UUID id){
        return followService.enrichUserResponse(
            userRepository.findById(id).orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED))
        );
    }

    public void changePassword(PasswordChangeRequest request) {
        var context = SecurityContextHolder.getContext();
        String currentUsername = context.getAuthentication().getName();

        User user = userRepository.findByUsername(currentUsername)
                .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));

        boolean isMatch = passwordEncoder.matches(request.getOldPassword(), user.getPassword());
        if (!isMatch) {
            throw new AppException(ErrorCode.PASSWORD_INCORRECT);
        }

        if (!request.getNewPassword().equals(request.getConfirmPassword())) {
            throw new AppException(ErrorCode.PASSWORD_NOT_MATCH);
        }

        user.setPassword(passwordEncoder.encode(request.getNewPassword()));
        userRepository.save(user);
    }

    public UserResponse getMyProfile() {
        var context = SecurityContextHolder.getContext();
        String currentUsername = context.getAuthentication().getName();

        User user = userRepository.findByUsername(currentUsername)
                .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));

        return followService.enrichUserResponse(user);
    }

    @Transactional
    public UserResponse updateMyProfile(UserUpdateRequest request) {
        var context = SecurityContextHolder.getContext();
        String currentUsername = context.getAuthentication().getName();

        User user = userRepository.findByUsername(currentUsername)
                .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));

        if (request.getEmail() != null) user.setEmail(request.getEmail());
        if (request.getBio() != null) user.setBio(request.getBio());
        if (request.getAvatarUrl() != null) user.setAvatarUrl(request.getAvatarUrl());

        return followService.enrichUserResponse(userRepository.save(user));
    }

    public UserResponse getUserByUsername(String username) {
        User user = userRepository.findByUsername(username)
                .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));

        return followService.enrichUserResponse(user);
    }

    public long countTotalUsers() {
        return userRepository.count();
    }
}
```

---

## 2. GIẢI THÍCH CHI TIẾT TỪNG PHƯƠNG THỨC TRONG `UserService`

### 2.1. Đăng ký người dùng mới: `createUser()`
```java
    public UserResponse createUser(UserCreatetionRequest request){
        if(userRepository.existsByUsername(request.getUsername())) 
            throw new AppException(ErrorCode.USER_EXITED);
```
- Bước 1: Kiểm tra xem username đã tồn tại chưa bằng `existsByUsername()`. Nếu đã tồn tại, ném ngoại lệ `USER_EXITED` (Mã lỗi 1002 - HTTP 400).
```java
        User u = userMapper.toUser(request);
        if(u.getRoles() == null) u.setRoles(new HashSet<>());
        u.setPassword(passwordEncoder.encode(request.getPassword()));
        u.getRoles().add(Role.USER.name());
        User savedUser = userRepository.save(u);
        return userMapper.toUserResponse(savedUser);
    }
```
- Bước 2: Chuyển DTO `UserCreatetionRequest` thành Entity `User` thông qua `userMapper`.
- Bước 3: Mã hóa mật khẩu người dùng nhập vào bằng `passwordEncoder.encode(rawPassword)`.
- Bước 4: Mặc định mọi người dùng tự đăng ký ngoài trang chủ chỉ được cấp quyền `USER` (`Role.USER.name()`), tuyệt đối không được tự gán quyền `ADMIN`.
- Bước 5: Lưu vào CSDL và trả về `UserResponse` (đã lọc bỏ mật khẩu).

---

### 2.2. Đổi mật khẩu an toàn 5 bước: `changePassword()`
```java
    public void changePassword(PasswordChangeRequest request) {
        // 1. Lấy ra username của người ĐANG ĐĂNG NHẬP từ Token
        var context = SecurityContextHolder.getContext();
        String currentUsername = context.getAuthentication().getName();

        // 2. Lấy User từ Database lên
        User user = userRepository.findByUsername(currentUsername)
                .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));

        // 3. So sánh: Mật khẩu cũ nhập vào có khớp với mật khẩu băm trong DB không?
        boolean isMatch = passwordEncoder.matches(request.getOldPassword(), user.getPassword());
        if (!isMatch) {
            throw new AppException(ErrorCode.PASSWORD_INCORRECT);
        }

        // 4. Kiểm tra: Mật khẩu mới và Nhập lại mật khẩu có giống nhau không?
        if (!request.getNewPassword().equals(request.getConfirmPassword())) {
            throw new AppException(ErrorCode.PASSWORD_NOT_MATCH);
        }

        // 5. Mọi thứ hợp lệ -> Băm mật khẩu mới và lưu đè
        user.setPassword(passwordEncoder.encode(request.getNewPassword()));
        userRepository.save(user);
    }
```
- **Nguyên lý bảo mật**: Không bao giờ nhận `username` từ Client truyền lên trong form đổi mật khẩu. Lấy thẳng `currentUsername` từ `SecurityContextHolder`. Kẻ xấu không thể đổi mật khẩu của người khác bằng cách sửa tham số trên URL!

---

### 2.3. Cập nhật hồ sơ cá nhân: `updateMyProfile()`
- Đánh dấu bằng `@Transactional`: Đảm bảo toàn bộ quá trình đọc và cập nhật dữ liệu diễn ra trong một giao dịch duy nhất.
- Chỉ cho phép người dùng tự sửa 3 trường an toàn: `email`, `bio` và `avatarUrl`.

---

## 3. MÃ NGUỒN VÀ GIẢI THÍCH `AdminService.java`

File nằm tại: `src/main/java/com/group/blog/service/AdminService.java`

```java
package com.group.blog.service;

import com.group.blog.dto.response.AdminStatsResponse;
import com.group.blog.dto.response.BlogResponse;
import com.group.blog.repository.BlogRepository;
import com.group.blog.repository.UserRepository;
import com.group.blog.mapper.BlogMapper;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class AdminService {

    UserRepository userRepository;
    BlogRepository blogRepository;
    BlogMapper blogMapper;

    public AdminStatsResponse getDashboardStats() {
        // 1. Đếm tổng số lượng người dùng trong hệ thống
        long totalUsers = userRepository.count();

        // 2. Đếm tổng số bài viết đã xuất bản công khai (bỏ qua bản nháp)
        long totalPosts = blogRepository.countByDraftFalse();

        // 3. Lấy 5 bài viết mới nhất vừa được tạo
        List<BlogResponse> recentPosts = blogRepository.findTop5ByDraftFalseOrderByCreatedAtDesc()
                .stream()
                .map(blogMapper::toBlogResponse)
                .collect(Collectors.toList());

        // 4. Đóng gói vào DTO trả về cho Dashboard
        return AdminStatsResponse.builder()
                .totalUsers(totalUsers)
                .totalPosts(totalPosts)
                .recentPosts(recentPosts)
                .build();
    }
}
```
- **Ý nghĩa**: Cung cấp dữ liệu tức thời cho trang quản trị (`/admin/dashboard.html`). Khi Admin đăng nhập vào, giao diện sẽ hiển thị các ô thống kê trực quan (Tổng số thành viên, Tổng số bài viết, Danh sách 5 bài viết mới nhất) chỉ bằng 1 lần gọi API duy nhất: `GET /api/admin/stats`.

---

## 4. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN VỀ USERSERVICE & ADMINSERVICE

### Câu 1: Tại sao trong hàm `changePassword()`, em không nhận `username` từ Client truyền lên mà lại lấy qua `SecurityContextHolder`?
- **Trả lời**:
  > "Thưa thầy/cô, đây là một nguyên tắc bảo mật tối quan trọng (Chống lỗ hổng IDOR - Insecure Direct Object References):
  > Nếu chúng em nhận `username` từ request body của Client, kẻ xấu sau khi đăng nhập tài khoản của hắn có thể sửa body thành `username: admin` và mật khẩu mới để chiếm đoạt tài khoản Admin.
  > Bằng cách lấy trực tiếp từ `SecurityContextHolder.getContext().getAuthentication().getName()`, hệ thống chỉ lấy danh tính đã được kiểm chứng an toàn qua chữ ký số của Token JWT. Người dùng chỉ có thể đổi mật khẩu của chính bản thân họ."

### Câu 2: Trong hàm `updateUser()`, tại sao em phải gọi lệnh `u.getRoles().clear()` trước khi `addAll()`?
- **Trả lời**:
  > "Thưa thầy/cô, trong Hibernate đối với tập hợp `@ElementCollection`, nếu chúng em không gọi `clear()` mà chỉ gọi `add()`, các quyền cũ sẽ vẫn tồn tại trong CSDL.
  > Để đảm bảo khi Admin phân quyền lại (ví dụ thu hồi quyền ADMIN của một user), việc gọi `clear()` giúp Hibernate xóa sạch các dòng quyền cũ trong bảng `user_roles` rồi mới chèn danh sách quyền mới vào, đảm bảo tính nhất quán tuyệt đối của dữ liệu."
