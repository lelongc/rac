# GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG MAPSTRUCT MAPPERS VÀ SLUGUTILS

> **Mục tiêu**: Hiểu rõ công nghệ ánh xạ thực thể siêu tốc **MapStruct** (tại sao tốt hơn Reflection/BeanUtils), các chú thích `@Mapper`, `@Mapping(ignore=true)`, `@MappingTarget`, và giải thuật 6 bước tạo chuỗi URL chuẩn SEO không dấu tiếng Việt trong `SlugUtils.java`.

---

## 1. TẠI SAO LỰA CHỌN MAPSTRUCT TRONG DỰ ÁN?

Trong lập trình Java, việc sao chép dữ liệu từ DTO sang Entity hoặc ngược lại là thao tác diễn ra liên tục:
```java
// Cách làm thủ công bằng tay (Rất dài dòng và dễ quên):
userResponse.setId(user.getId());
userResponse.setUsername(user.getUsername());
userResponse.setEmail(user.getEmail());
userResponse.setBio(user.getBio());
// ... lặp lại 20 lần
```
Một số thư viện cũ như `ModelMapper` hay `BeanUtils` sử dụng cơ chế **Java Reflection** lúc chương trình đang chạy (Runtime), dẫn đến hiệu năng rất chậm và khó debug nếu có lỗi sai tên trường.

**MapStruct giải quyết triệt để vấn đề này**:
- MapStruct là một **Bộ xử lý chú thích tại thời điểm biên dịch (Compile-time Annotation Processor)**.
- Nó tự động sinh ra mã nguồn Java thuần túy (`UserMapperImpl.java`) trong thư mục `target/generated-sources/`.
- Tốc độ thực thi nhanh ngang bằng với code viết tay của lập trình viên và kiểm tra lỗi kiểu dữ liệu ngay khi bấm Build!

---

## 2. CHI TIẾT CÁC FILE MAPPER TRONG DỰ ÁN

### 2.1. `BlogMapper.java` (`src/main/java/com/group/blog/mapper/BlogMapper.java`)
```java
package com.group.blog.mapper;

import com.group.blog.dto.request.BlogCreationRequest;
import com.group.blog.dto.request.BlogUpdateRequest;
import com.group.blog.dto.response.BlogResponse;
import com.group.blog.entity.Blog;
import org.mapstruct.Mapper;
import org.mapstruct.Mapping;
import org.mapstruct.MappingTarget;

@Mapper(componentModel = "spring")
public interface BlogMapper {

    // 1. Ánh xạ từ Request sang Entity để lưu mới
    @Mapping(target = "category", ignore = true)
    @Mapping(target = "tags", ignore = true)
    @Mapping(target = "author", ignore = true)
    Blog toBlog(BlogCreationRequest request);

    // 2. Ánh xạ từ Entity sang Response để trả về cho Client
    BlogResponse toBlogResponse(Blog blog);

    // 3. Cập nhật đè lên Entity đã có sẵn trong Database
    @Mapping(target = "category", ignore = true)
    @Mapping(target = "tags", ignore = true)
    void updateBlog(@MappingTarget Blog blog, BlogUpdateRequest request);
}
```

### Giải thích các chú thích trọng tâm:
- **`@Mapper(componentModel = "spring")`**: Báo cho MapStruct sinh code và tự động gắn annotation `@Component` lên class triển khai `BlogMapperImpl`. Nhờ đó, lớp Service có thể tiêm mapper vào bằng `@Autowired private BlogMapper blogMapper;`.
- **`@Mapping(target = "author", ignore = true)`**: Bỏ qua trường tác giả. Tại sao bỏ qua? Vì trong DTO gửi lên không có thông tin tác giả, thông tin tác giả phải được tầng Service lấy từ Token JWT đăng nhập để chống giả mạo danh tính!
- **`@Mapping(target = "category", ignore = true)` & `target = "tags"`**: Bỏ qua danh mục và thẻ tag để tầng Service tự truy vấn CSDL và gán đối tượng quan hệ vào.
- **`@MappingTarget Blog blog`**: Cực kỳ giá trị! Thay vì tạo ra một đối tượng `new Blog()` mới tinh, annotation này chỉ thị cho MapStruct lấy dữ liệu từ `BlogUpdateRequest` và **đổ đè trực tiếp** vào đối tượng `blog` đang được Hibernate quản lý trong bộ nhớ (Persistent State), giúp câu lệnh `UPDATE` của JPA diễn ra hoàn hảo.

---

### 2.2. `UserMapper.java` (`src/main/java/com/group/blog/mapper/UserMapper.java`)
```java
package com.group.blog.mapper;

import com.group.blog.dto.request.UserCreatetionRequest;
import com.group.blog.dto.request.UserUpdateRequest;
import com.group.blog.dto.response.UserResponse;
import com.group.blog.entity.User;
import org.mapstruct.Mapper;
import org.mapstruct.MappingTarget;

@Mapper(componentModel = "spring")
public interface UserMapper {
    User toUser(UserCreatetionRequest request);
    UserResponse toUserResponse(User user);
    void updateUser(@MappingTarget User user, UserUpdateRequest request);
}
```

---

## 3. MÃ NGUỒN VÀ GIẢI THUẬT 6 BƯỚC TRONG `SlugUtils.java`

File nằm tại: `src/main/java/com/group/blog/util/SlugUtils.java`

```java
package com.group.blog.util;

import java.text.Normalizer;
import java.util.regex.Pattern;

public class SlugUtils {

    public static String generateSlug(String title) {
        if (title == null || title.trim().isEmpty()) {
            return "";
        }

        // 1. Chuyển tất cả thành chữ thường và cắt khoảng trắng 2 đầu
        String slug = title.trim().toLowerCase();

        // 2. Loại bỏ dấu tiếng Việt (Chuẩn hóa Unicode NFD)
        slug = Normalizer.normalize(slug, Normalizer.Form.NFD);
        Pattern pattern = Pattern.compile("\\p{InCombiningDiacriticalMarks}+");
        slug = pattern.matcher(slug).replaceAll("");

        // 3. Xử lý riêng chữ 'đ' (vì Normalizer không tự động chuyển đ thành d)
        slug = slug.replace("đ", "d");

        // 4. Thay thế tất cả các ký tự không phải là chữ cái hoặc số thành dấu gạch ngang (-)
        slug = slug.replaceAll("[^a-z0-9]+", "-");

        // 5. Loại bỏ các dấu gạch ngang liên tiếp (ví dụ: "---" biến thành "-")
        slug = slug.replaceAll("-+", "-");

        // 6. Xóa dấu gạch ngang bị thừa ở đầu hoặc cuối chuỗi (nếu có)
        slug = slug.replaceAll("^-|-$", "");

        return slug;
    }
}
```

### Giải thích chi tiết giải thuật 6 bước tạo Slug:
1. **Bước 1 (`toLowerCase()`)**: Đưa toàn bộ về chữ thường, ví dụ: `"Học Spring Boot 3 & JPA!"` -> `"học spring boot 3 & jpa!"`.
2. **Bước 2 (Unicode NFD & Diacritical Marks)**: 
   - Tiếng Việt sử dụng các dấu thanh (sắc, huyền, hỏi, ngã, nặng).
   - Hàm `Normalizer.normalize(slug, Normalizer.Form.NFD)` tách ký tự gốc và dấu thanh ra làm 2 phần riêng biệt (ví dụ chữ `ọ` được tách thành `o` + `dấu nặng`).
   - Biểu thức chính quy `\p{InCombiningDiacriticalMarks}+` tìm kiếm tất cả các dấu thanh này và xóa sạch. Chuỗi trở thành: `"hoc spring boot 3 & jpa!"`.
3. **Bước 3 (Chữ `đ`)**: Ký tự `đ` và `Đ` trong bảng mã Unicode không thuộc nhóm dấu thanh kết hợp, nên hàm chuẩn hóa NFD sẽ bỏ sót. Ta dùng lệnh `.replace("đ", "d")` riêng biệt để xử lý dứt điểm.
4. **Bước 4 (Ký tự đặc biệt `[^a-z0-9]+`)**: Thay thế tất cả dấu chấm, phẩy, chấm than, dấu `&`, khoảng trắng thành dấu gạch ngang `-`. Chuỗi thành: `"hoc-spring-boot-3---jpa-"`.
5. **Bước 5 (Gộp dấu gạch ngang `-+`)**: Nếu có nhiều dấu gạch ngang liền nhau (ví dụ khoảng cách ` & ` sinh ra 3 dấu gạch), gộp lại thành 1 dấu duy nhất: `"hoc-spring-boot-3-jpa-"`.
6. **Bước 6 (Cắt 2 đầu `^-|-$`)**: Loại bỏ dấu gạch ngang ở đầu hoặc cuối chuỗi nếu có. Kết quả cuối cùng là một đường link hoàn hảo:
   ```
   hoc-spring-boot-3-jpa
   ```

---

## 4. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN & TRẢ LỜI ĐIỂM 10

### Câu 1: MapStruct sinh mã nguồn vào lúc nào? Tại sao nó lại có hiệu năng cao hơn `BeanUtils.copyProperties`?
- **Trả lời**:
  > "Thưa thầy/cô:
  > - MapStruct sinh mã nguồn vào lúc **Biên dịch (Compile-time)**. Khi chúng em gõ lệnh `mvn compile`, plugin `mapstruct-processor` sẽ tự động tạo ra class Java `BlogMapperImpl.java` chứa các dòng lệnh `getter/setter` trực tiếp.
  > - Ngược lại, `BeanUtils.copyProperties` phải dùng cơ chế **Java Reflection** lúc chương trình đang chạy (Runtime) để soi cấu trúc class và gọi hàm qua gương, tốn rất nhiều tài nguyên CPU và RAM. Do đó MapStruct có tốc độ nhanh gấp hàng chục lần và hoàn toàn an toàn về mặt kiểu dữ liệu (Type-safe)."

### Câu 2: Trong `SlugUtils`, tại sao sau khi dùng `Normalizer` vẫn phải có dòng `slug.replace("đ", "d")`?
- **Trả lời**:
  > "Thưa thầy/cô, trong chuẩn mã hóa Unicode:
  > - Các nguyên âm có dấu như `á, à, ả, ã, ạ` được tạo nên bởi nguyên âm gốc `a` cộng với các ký hiệu dấu thanh (Combining Diacritical Marks). `Normalizer.Form.NFD` có thể bóc tách dấu thanh này ra để xóa đi.
  > - Tuy nhiên, chữ `đ` (D với dấu gạch ngang - D with stroke) là một **chữ cái độc lập riêng biệt** trong bảng chữ cái Latin mở rộng chứ không phải là chữ `d` gắn thêm dấu thanh. Vì vậy bộ lọc `Normalizer` không thể biến chữ `đ` thành chữ `d` được. Đó là lý do chúng em phải bổ sung dòng lệnh xử lý riêng `replace("đ", "d")` để các từ tiếng Việt như 'đại học', 'đăng nhập' được chuyển đổi thành 'dai-hoc', 'dang-nhap' một cách chuẩn xác."
