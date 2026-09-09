# GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG BLOGCONTROLLER VÀ UPLOADCONTROLLER

> **Mục tiêu**: Nắm vững toàn bộ hệ thống API bài viết (CRUD, tìm kiếm từ khóa, gợi ý autocomplete, lọc theo danh mục/tag, phân luồng bài viết của tôi vs bài viết công khai) và API tải ảnh lên đám mây Cloudinary.

---

## 1. MÃ NGUỒN VÀ GIẢI THÍCH CHI TIẾT `BlogController.java`

File nằm tại: `src/main/java/com/group/blog/controller/BlogController.java`

```java
package com.group.blog.controller;

import com.group.blog.dto.request.ApiResponse;
import com.group.blog.dto.request.BlogCreationRequest;
import com.group.blog.dto.request.BlogUpdateRequest;
import com.group.blog.dto.response.BlogResponse;
import com.group.blog.dto.response.BlogSuggestionResponse;
import com.group.blog.service.BlogService;
import jakarta.validation.Valid;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.UUID;

@RestController
@RequestMapping("/blogs")
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class BlogController {

    BlogService blogService;

    // 1. Tạo bài viết mới
    @PostMapping
    public ApiResponse<BlogResponse> createBlog(@RequestBody @Valid BlogCreationRequest request) {
        return ApiResponse.<BlogResponse>builder()
                .result(blogService.createBlog(request))
                .build();
    }

    // 2. Lấy danh sách toàn bộ bài viết công khai (trang chủ)
    @GetMapping
    public ApiResponse<List<BlogResponse>> getAllBlogs() {
        return ApiResponse.<List<BlogResponse>>builder()
                .result(blogService.getAllBlogs())
                .build();
    }

    // 3. Lấy chi tiết 1 bài viết theo ID
    @GetMapping("/{id}")
    public ApiResponse<BlogResponse> getBlogById(@PathVariable UUID id) {
        return ApiResponse.<BlogResponse>builder()
                .result(blogService.getBlogById(id))
                .build();
    }

    // 4. Cập nhật bài viết
    @PutMapping("/{id}")
    public ApiResponse<BlogResponse> updateBlog(
            @PathVariable UUID id,
            @RequestBody @Valid BlogUpdateRequest request) {
        return ApiResponse.<BlogResponse>builder()
                .result(blogService.updateBlog(id, request))
                .build();
    }

    // 5. Xóa bài viết
    @DeleteMapping("/{id}")
    public ApiResponse<String> deleteBlog(@PathVariable UUID id) {
        blogService.deleteBlog(id);
        return ApiResponse.<String>builder()
                .result("Bài viết đã được xóa thành công")
                .build();
    }

    // 6. Lọc bài viết theo Danh mục
    @GetMapping("/category/{categoryId}")
    public ApiResponse<List<BlogResponse>> getBlogsByCategory(@PathVariable UUID categoryId) {
        return ApiResponse.<List<BlogResponse>>builder()
                .result(blogService.getBlogsByCategory(categoryId))
                .build();
    }

    // 7. Lọc bài viết theo Thẻ Tag
    @GetMapping("/tag/{tagId}")
    public ApiResponse<List<BlogResponse>> getBlogsByTag(@PathVariable UUID tagId) {
        return ApiResponse.<List<BlogResponse>>builder()
                .result(blogService.getBlogsByTag(tagId))
                .build();
    }

    // 8. Tìm kiếm bài viết theo từ khóa
    @GetMapping("/search")
    public ApiResponse<List<BlogResponse>> searchBlogs(@RequestParam("keyword") String keyword) {
        return ApiResponse.<List<BlogResponse>>builder()
                .result(blogService.searchBlogs(keyword))
                .build();
    }

    // 9. Gợi ý tìm kiếm nhanh (Top 5 kết quả thả xuống khi gõ phím)
    @GetMapping("/search/suggestions")
    public ApiResponse<List<BlogSuggestionResponse>> getSuggestions(@RequestParam("keyword") String keyword) {
        return ApiResponse.<List<BlogSuggestionResponse>>builder()
                .result(blogService.getSearchSuggestions(keyword))
                .build();
    }

    // 10. Lọc đa điều kiện (Kết hợp cả Từ khóa + Danh mục)
    @GetMapping("/filter")
    public ApiResponse<List<BlogResponse>> filterBlogs(
            @RequestParam(required = false) String keyword,
            @RequestParam(required = false) UUID categoryId) {
        return ApiResponse.<List<BlogResponse>>builder()
                .result(blogService.filterBlogs(keyword, categoryId))
                .build();
    }

    // 11. Lấy danh sách bài viết của chính người đang đăng nhập (gồm cả nháp)
    @GetMapping("/my-blogs")
    public ApiResponse<List<BlogResponse>> getMyBlogs() {
        return ApiResponse.<List<BlogResponse>>builder()
                .result(blogService.getMyBlogs())
                .build();
    }

    // 12. Lấy bài viết công khai của một tác giả
    @GetMapping("/user/{username}")
    public ApiResponse<List<BlogResponse>> getBlogsByUsername(@PathVariable String username) {
        return ApiResponse.<List<BlogResponse>>builder()
                .result(blogService.getPublishedBlogsByUsername(username))
                .build();
    }
}
```

### Các kỹ thuật phân biệt tham số URL:
- **`@PathVariable UUID id`**: Trích xuất giá trị trực tiếp từ thanh địa chỉ URL (Ví dụ: `/blogs/c0a8012e-...` thì `id = c0a8012e-...`).
- **`@RequestParam("keyword") String keyword`**: Trích xuất tham số dạng truy vấn Query Parameter sau dấu chấm hỏi `?` (Ví dụ: `/blogs/search?keyword=spring` thì `keyword = "spring"`).
- **`@RequestParam(required = false)`**: Tham số không bắt buộc. Trong API `/blogs/filter`, người dùng có thể chỉ lọc theo `keyword` mà không chọn `categoryId`, hoặc ngược lại.

---

## 2. MÃ NGUỒN VÀ GIẢI THÍCH CHI TIẾT `UploadController.java`

File nằm tại: `src/main/java/com/group/blog/controller/UploadController.java`

```java
package com.group.blog.controller;

import com.group.blog.dto.request.ApiResponse;
import com.group.blog.service.CloudinaryService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;

@RestController
@RequestMapping("/upload")
@RequiredArgsConstructor
public class UploadController {
    private final CloudinaryService cloudinaryService;

    @PostMapping("/image")
    public ApiResponse<String> uploadImage(@RequestParam("file") MultipartFile file) throws IOException {
        String imageUrl = cloudinaryService.uploadImage(file);
        return ApiResponse.<String>builder()
                .result(imageUrl)
                .build();
    }
}
```

### Quy trình hoạt động của API Upload:
1. Client (trình duyệt) tạo một đối tượng JavaScript `FormData`, đính kèm file ảnh với tên trường là `"file"`:
   ```javascript
   const formData = new FormData();
   formData.append('file', fileInput.files[0]);
   ```
2. Gửi request POST đến `http://localhost:8080/upload/image`.
3. `@RequestParam("file") MultipartFile file`: Spring bắt lấy luồng nhị phân của file.
4. Controller chuyển giao cho `CloudinaryService.uploadImage(file)` để đưa lên mây.
5. Trả về cho Frontend chuỗi URL ảnh dạng:
   ```json
   {
     "code": 1000,
     "message": null,
     "result": "https://res.cloudinary.com/fu18kpep/image/upload/v172.../banner.png"
   }
   ```
6. Frontend lấy `data.result` này chèn ngay vào thẻ `<img src="...">` để xem trước (Preview) và gửi kèm trong form lưu bài viết.

---

## 3. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN VỀ BLOGCONTROLLER & UPLOADCONTROLLER

### Câu 1: Em hãy phân biệt sự khác nhau giữa `@PathVariable` và `@RequestParam`? Khi nào nên dùng loại nào?
- **Trả lời**:
  > "Thưa thầy/cô:
  > - `@PathVariable`: Dùng để định danh duy nhất một tài nguyên cụ thể trong cấu trúc cây URL phân cấp (ví dụ: xem chi tiết một bài viết cụ thể: `/blogs/{id}`).
  > - `@RequestParam`: Dùng cho các tham số tùy chọn dùng để lọc, tìm kiếm, sắp xếp hoặc phân trang tài nguyên (ví dụ: `/blogs/search?keyword=java` hoặc `/blogs/filter?categoryId=...`)."

### Câu 2: Giả sử một người dùng cố tình upload một file virus `.exe` hoặc file nặng 50MB lên API upload ảnh thì hệ thống xử lý ra sao?
- **Trả lời**:
  > "Thưa thầy/cô:
  > 1. Về dung lượng: Trong file `application.yaml`, chúng em đã giới hạn cứng `spring.servlet.multipart.max-request-size: 10MB`. Nếu file lớn hơn 10MB, máy chủ Tomcat sẽ từ chối nhận ngay từ đầu với lỗi `MaxUploadSizeExceededException`.
  > 2. Về độ an toàn: Toàn bộ file được đẩy thẳng lên đám mây Cloudinary chứ không lưu trên ổ cứng của server Spring Boot. Cloudinary có hệ thống quét mã độc và tự động phát hiện định dạng file thực tế (MIME Type). Nếu không phải định dạng ảnh hợp lệ, Cloudinary sẽ trả về mã lỗi và không phân phát file đó."
