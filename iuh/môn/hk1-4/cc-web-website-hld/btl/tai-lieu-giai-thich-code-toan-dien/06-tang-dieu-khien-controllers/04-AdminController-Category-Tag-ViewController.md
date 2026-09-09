# GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG ADMIN, CATEGORY, TAG VÀ VIEWCONTROLLER

> **Mục tiêu**: Nắm chắc các API quản trị hệ thống (`AdminController`, `CategoryController`, `TagController`) và hiểu sâu sắc sự khác biệt bản chất giữa `@Controller` điều hướng giao diện Thymeleaf (`ViewController`) và `@RestController` trả về dữ liệu thô JSON.

---

## 1. MÃ NGUỒN VÀ GIẢI THÍCH `AdminController.java`

File nằm tại: `src/main/java/com/group/blog/controller/AdminController.java`

```java
package com.group.blog.controller;

import com.group.blog.dto.request.ApiResponse;
import com.group.blog.dto.response.AdminStatsResponse;
import com.group.blog.service.AdminService;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/admin")
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class AdminController {

    AdminService adminService;

    @GetMapping("/stats")
    public ApiResponse<AdminStatsResponse> getDashboardStats() {
        return ApiResponse.<AdminStatsResponse>builder()
                .result(adminService.getDashboardStats())
                .build();
    }
}
```
- **Phân quyền trong `SecurityConfig`**: Toàn bộ đường dẫn `/api/admin/**` đã được bảo vệ nghiêm ngặt bằng quy tắc `.requestMatchers("/api/admin/**").hasRole("ADMIN")`. Chỉ khi gửi Token chứa quyền `ADMIN`, API `/api/admin/stats` này mới trả về dữ liệu thống kê tổng số user và bài viết.

---

## 2. MÃ NGUỒN VÀ GIẢI THÍCH `CategoryController.java` VÀ `TagController.java`

### 2.1. `CategoryController.java` (`src/main/java/com/group/blog/controller/CategoryController.java`)
```java
@RestController
@RequestMapping("/categories")
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class CategoryController {
    CategoryService categoryService;

    // Lấy danh sách danh mục (Công khai - Ai cũng xem được)
    @GetMapping
    public ApiResponse<List<CategoryResponse>> getAll() {
        return ApiResponse.<List<CategoryResponse>>builder()
                .result(categoryService.getAllCategories())
                .build();
    }

    // Thêm danh mục (Chỉ Admin mới có quyền)
    @PostMapping
    public ApiResponse<Category> create(@RequestBody CategoryRequest request) {
        return ApiResponse.<Category>builder()
                .result(categoryService.create(request))
                .build();
    }

    // Cập nhật tên danh mục (Chỉ Admin)
    @PutMapping("/{id}")
    public ApiResponse<CategoryResponse> update(@PathVariable java.util.UUID id, @RequestBody CategoryRequest request) {
        return ApiResponse.<CategoryResponse>builder()
                .result(categoryService.update(id, request))
                .build();
    }

    // Xóa danh mục (Chỉ Admin)
    @DeleteMapping("/{id}")
    public ApiResponse<Void> delete(@PathVariable java.util.UUID id) {
        categoryService.delete(id);
        return ApiResponse.<Void>builder().build();
    }
}
```

### 2.2. `TagController.java` (`src/main/java/com/group/blog/controller/TagController.java`)
```java
@RestController
@RequestMapping("/tags")
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class TagController {
    TagService tagService;

    @GetMapping
    public ApiResponse<List<TagResponse>> getAll() {
        return ApiResponse.<List<TagResponse>>builder()
                .result(tagService.getAllTags())
                .build();
    }

    @PostMapping
    public ApiResponse<TagResponse> createTag(@RequestBody com.group.blog.dto.request.CategoryRequest request) {
        return ApiResponse.<TagResponse>builder()
                .result(tagService.create(request))
                .build();
    }

    @PutMapping("/{id}")
    public ApiResponse<TagResponse> update(@PathVariable java.util.UUID id, @RequestBody com.group.blog.dto.request.CategoryRequest request) {
        return ApiResponse.<TagResponse>builder().result(tagService.update(id, request)).build();
    }

    @DeleteMapping("/{id}")
    public ApiResponse<Void> delete(@PathVariable java.util.UUID id) {
        tagService.delete(id);
        return ApiResponse.<Void>builder().build();
    }
}
```

---

## 3. MÃ NGUỒN VÀ GIẢI THÍCH `ViewController.java`

File nằm tại: `src/main/java/com/group/blog/controller/ViewController.java`

```java
package com.group.blog.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class ViewController {

    @GetMapping({"/", "/home", "/home-page.html"})
    public String homePage() {
        return "public/home-page";
    }

    @GetMapping({"/login", "/login.html"})
    public String loginPage() {
        return "public/login";
    }

    @GetMapping({"/register", "/register.html"})
    public String registerPage() {
        return "public/register";
    }

    @GetMapping({"/forgot-password", "/forgot-password.html"})
    public String forgotPasswordPage() {
        return "public/forgot-password";
    }

    @GetMapping({"/post", "/post.html"})
    public String postDetailPage() {
        return "public/post";
    }

    @GetMapping({"/blog-editor", "/blog-editor.html"})
    public String blogEditorPage() {
        return "public/blog-editor";
    }

    @GetMapping({"/user-profile", "/user-profile.html"})
    public String userProfilePage() {
        return "public/user-profile";
    }

    @GetMapping({"/edit-profile", "/edit-profile.html"})
    public String editProfilePage() {
        return "public/edit-profile";
    }

    @GetMapping({"/saved-blogs", "/saved-blogs.html"})
    public String savedBlogsPage() {
        return "public/saved-blogs";
    }

    @GetMapping({"/notifications", "/notifications.html"})
    public String notificationsPage() {
        return "public/notifications";
    }

    @GetMapping({"/manage-blogs", "/manage-blogs.html", "/Manage-Blogs.html"})
    public String manageBlogsPage() {
        return "public/Manage-Blogs";
    }

    @GetMapping({"/change-password", "/change-password.html"})
    public String changePasswordPage() {
        return "public/change-password";
    }

    @GetMapping({"/admin", "/admin/dashboard", "/admin/dashboard.html"})
    public String adminDashboardPage() {
        return "admin/dashboard";
    }

    @GetMapping({"/admin/posts", "/admin/posts.html"})
    public String adminPostsPage() {
        return "admin/posts";
    }

    @GetMapping({"/admin/users", "/admin/users.html"})
    public String adminUsersPage() {
        return "admin/users";
    }

    @GetMapping({"/admin/categories-tags", "/admin/categories-tags.html"})
    public String adminCategoriesTagsPage() {
        return "admin/categories-tags";
    }
}
```

---

## 4. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN & TRẢ LỜI ĐIỂM 10

### Câu 1: Em hãy phân biệt sự khác nhau bản chất giữa annotation `@Controller` và `@RestController` trong Spring Boot?
- **Trả lời**:
  > "Thưa thầy/cô, đây là điểm phân biệt kiến trúc rất quan trọng:
  > - **`@Controller`** (như trong `ViewController.java`): Phương thức trả về một chuỗi `String` (ví dụ: `"public/home-page"`). Spring Boot sẽ hiểu chuỗi này là **Tên của file giao diện (View Name)**. Công cụ Thymeleaf View Resolver sẽ tự động tìm file `src/main/resources/templates/public/home-page.html`, biên dịch thành mã HTML và render trả về cho trình duyệt hiển thị.
  > - **`@RestController`** (như trong `BlogController`, `UserController`): Là sự kết hợp của `@Controller` + `@ResponseBody`. Phương thức trả về đối tượng Java (DTO, List, Object). Spring Boot sẽ dùng bộ chuyển đổi Jackson để ép dữ liệu đó thành chuỗi **JSON thô**, không liên quan gì đến file HTML giao diện."

### Câu 2: Trong `ViewController`, tại sao một phương thức lại được gán nhiều đường dẫn trong `@GetMapping({"/", "/home", "/home-page.html"})`?
- **Trả lời**:
  > "Thưa thầy/cô, đây là kỹ thuật định tuyến linh hoạt (Route Aliasing):
  > Giúp người dùng khi gõ bất kỳ địa chỉ nào:
  > - Truy cập trang gốc: `http://localhost:8080/`
  > - Hoặc gõ: `http://localhost:8080/home`
  > - Hoặc click file tĩnh: `http://localhost:8080/home-page.html`
  > thì hệ thống đều điều hướng về cùng một trang chủ duy nhất, mang lại trải nghiệm người dùng liền mạch và không bao giờ gặp lỗi 404 Not Found."
