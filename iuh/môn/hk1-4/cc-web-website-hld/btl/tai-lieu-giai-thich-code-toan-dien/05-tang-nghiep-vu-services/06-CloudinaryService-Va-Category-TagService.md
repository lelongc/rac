# GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG CLOUDINARYSERVICE, CATEGORYSERVICE VÀ TAGSERVICE

> **Mục tiêu**: Hiểu rõ quy trình nhận file từ người dùng và đẩy lên đám mây Cloudinary bằng Java SDK (`CloudinaryService`), cùng nghiệp vụ quản lý Danh mục (`CategoryService`) và Thẻ bài viết (`TagService`), cách tính số lượng bài viết đi kèm (`postCount`) và sinh đường dẫn Slug động chuẩn 3NF.

---

## 1. MÃ NGUỒN VÀ GIẢI THÍCH CHI TIẾT `CloudinaryService.java`

File nằm tại: `src/main/java/com/group/blog/service/CloudinaryService.java`

```java
package com.group.blog.service;

import com.cloudinary.Cloudinary;
import com.cloudinary.utils.ObjectUtils;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.Map;

@Service
@RequiredArgsConstructor
public class CloudinaryService {
    private final Cloudinary cloudinary;

    public String uploadImage(MultipartFile file) throws IOException {
        // 1. Gửi mảng byte của file lên Cloudinary qua API
        Map uploadResult = cloudinary.uploader().upload(file.getBytes(), ObjectUtils.emptyMap());
        
        // 2. Trích xuất đường link URL ảnh an toàn (HTTPS) trả về cho Client
        return uploadResult.get("url").toString();
    }
}
```

### Giải thích chi tiết:
- **`MultipartFile file`**: Đối tượng đại diện cho file ảnh (PNG, JPG, WebP) được người dùng chọn từ máy tính và gửi lên qua form `multipart/form-data`.
- **`file.getBytes()`**: Đọc toàn bộ nội dung file ảnh thành một mảng byte nhị phân.
- **`cloudinary.uploader().upload(...)`**: Gọi hàm SDK chính thức của Cloudinary. Phương thức này thiết lập kết nối HTTPS đến máy chủ Cloudinary, đẩy dữ liệu ảnh lên và nhận về một đối tượng `Map` chứa thông tin chi tiết về file vừa upload (kích thước, định dạng, độ phân giải, URL).
- **`uploadResult.get("url").toString()`**: Lấy chuỗi URL công khai (Ví dụ: `http://res.cloudinary.com/fu18kpep/image/upload/v172.../sample.jpg`). URL này sau đó sẽ được lưu vào trường `avatarUrl` của User hoặc `banner` của Blog.

---

## 2. MÃ NGUỒN VÀ GIẢI THÍCH CHI TIẾT `CategoryService.java`

File nằm tại: `src/main/java/com/group/blog/service/CategoryService.java`

```java
package com.group.blog.service;

import com.group.blog.dto.request.CategoryRequest;
import com.group.blog.dto.response.CategoryResponse;
import com.group.blog.entity.Category;
import com.group.blog.exception.AppException;
import com.group.blog.exception.ErrorCode;
import com.group.blog.mapper.CategoryMapper;
import com.group.blog.repository.CategoryRepository;
import com.group.blog.util.SlugUtils;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class CategoryService {
    CategoryRepository categoryRepository;
    CategoryMapper categoryMapper;

    @Transactional
    public Category create(CategoryRequest request){
        if(categoryRepository.existsByName(request.getName())) {
            throw new AppException(ErrorCode.CATEGORY_EXITED);
        }
        Category category = categoryMapper.toCategory(request);
        return categoryRepository.save(category);
    }

    @Transactional
    public CategoryResponse update(java.util.UUID id, CategoryRequest request) {
        Category category = categoryRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Category does not exist"));

        // Kiểm tra xem tên mới có bị trùng với một category khác đã có sẵn không
        if (!category.getName().equals(request.getName()) && categoryRepository.existsByName(request.getName())) {
            throw new RuntimeException("This Category already exists");
        }

        category.setName(request.getName());
        category = categoryRepository.save(category);

        return CategoryResponse.builder()
                .id(category.getId())
                .name(category.getName())
                .slug(SlugUtils.generateSlug(category.getName()) + "-" + category.getId().toString())
                .postCount(0L)
                .build();
    }

    @Transactional
    public void delete(java.util.UUID id) {
        if (!categoryRepository.existsById(id)) throw new RuntimeException("Category not found");
        categoryRepository.deleteById(id);
    }

    public List<CategoryResponse> getAllCategories() {
        // 1. Gọi truy vấn gom nhóm tối ưu 1 lần duy nhất từ DB
        List<Object[]> results = categoryRepository.findAllCategoriesWithPostCount();

        // 2. Map dữ liệu Object[] -> CategoryResponse DTO
        return results.stream()
                .map(row -> {
                    Category category = (Category) row[0];
                    long count = (long) row[1];

                    return CategoryResponse.builder()
                            .id(category.getId())
                            .name(category.getName())
                            // Tạo Slug "on-the-fly" chuẩn 3NF (không lưu trường dư thừa trong DB)
                            .slug(SlugUtils.generateSlug(category.getName()) + "-" + category.getId().toString())
                            .postCount(count)
                            .build();
                })
                .toList();
    }
}
```

---

## 3. MÃ NGUỒN VÀ GIẢI THÍCH CHI TIẾT `TagService.java`

File nằm tại: `src/main/java/com/group/blog/service/TagService.java`

```java
package com.group.blog.service;

import com.group.blog.dto.response.TagResponse;
import com.group.blog.entity.Tag;
import com.group.blog.repository.TagRepository;
import com.group.blog.util.SlugUtils;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class TagService {

    TagRepository tagRepository;

    public List<TagResponse> getAllTags() {
        List<Object[]> results = tagRepository.findAllTagsWithPostCount();

        return results.stream().map(row -> {
            Tag tag = (Tag) row[0];
            long postCount = (long) row[1];

            return TagResponse.builder()
                    .id(tag.getId())
                    .name(tag.getName())
                    .slug(SlugUtils.generateSlug(tag.getName()) + "-" + tag.getId())
                    .postCount(postCount)
                    .build();
        }).toList();
    }

    @Transactional
    public TagResponse create(com.group.blog.dto.request.CategoryRequest request) {
        if(tagRepository.existsByName(request.getName())) {
            throw new RuntimeException("Tag is existed!");
        }
        Tag tag = new Tag();
        tag.setName(request.getName());
        tag = tagRepository.save(tag);

        return TagResponse.builder()
                .id(tag.getId())
                .name(tag.getName())
                .slug(SlugUtils.generateSlug(tag.getName()) + "-" + tag.getId())
                .postCount(0L)
                .build();
    }

    @Transactional
    public TagResponse update(java.util.UUID id, com.group.blog.dto.request.CategoryRequest request) {
        Tag tag = tagRepository.findById(id).orElseThrow(() -> new RuntimeException("Tag not found"));
        tag.setName(request.getName());
        tag = tagRepository.save(tag);
        return TagResponse.builder().id(tag.getId()).name(tag.getName()).build();
    }

    @Transactional
    public void delete(java.util.UUID id) {
        tagRepository.deleteById(id);
    }
}
```

---

## 4. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN & TRẢ LỜI ĐIỂM 10

### Câu 1: Tại sao trong bảng `categories` và `tags` ở CSDL không có cột `slug`, mà khi trả về API lại có trường `slug`?
- **Trả lời**:
  > "Thưa thầy/cô, đây là kỹ thuật thiết kế **Chuẩn hóa cơ sở dữ liệu dạng chuẩn 3 (3NF - Third Normal Form)**:
  > - Giá trị của `slug` (ví dụ: `lap-trinh-java`) có thể được tính toán và suy diễn hoàn toàn từ cột tên `name` ('Lập trình Java') và `id`.
  > - Nếu chúng em tạo thêm một cột `slug` trong bảng CSDL, dữ liệu sẽ bị trùng lặp dư thừa (Data Redundancy). Mỗi khi Admin sửa tên Danh mục, chúng em sẽ phải cập nhật cả cột slug, nếu quên cập nhật sẽ gây ra hiện tượng không nhất quán dữ liệu (Data Inconsistency).
  > - Do đó, nhóm em chọn giải pháp tạo Slug động khi trả về ('On-the-fly') trong tầng Service thông qua hàm `SlugUtils.generateSlug()`. Giải pháp này vừa tiết kiệm dung lượng ổ cứng, vừa đảm bảo tính toàn vẹn 100% của cơ sở dữ liệu."

### Câu 2: Trong `CategoryService.update()`, dòng code `if (!category.getName().equals(request.getName()) && categoryRepository.existsByName(request.getName()))` xử lý trường hợp nào?
- **Trả lời**:
  > "Thưa thầy/cô, dòng code này xử lý bài toán **Kiểm tra trùng tên khi cập nhật**:
  > - Nếu người dùng chỉ bấm nút Lưu mà không đổi tên (tên cũ vẫn giữ nguyên), thì điều kiện `!category.getName().equals(request.getName())` sẽ là `false`, hệ thống cho phép lưu bình thường mà không báo lỗi trùng tên với chính nó.
  > - Nhưng nếu người dùng sửa tên thành một tên khác, và tên mới này lại trùng với một danh mục ĐÃ TỒN TẠI của người khác (`existsByName(...)` là `true`), hệ thống sẽ lập tức chặn lại và thông báo `This Category already exists`."
