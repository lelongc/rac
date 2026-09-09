# GIẢI THÍCH TOÀN DIỆN TỪNG DÒNG CODE TRONG BLOGSERVICE

> **Mục tiêu**: Nắm vững 100% nghiệp vụ phức tạp nhất của dự án: Quản lý bài viết (CRUD Blog), Cơ chế bản nháp độc quyền 2 luồng (Draft vs Published), Tự động tăng lượt xem khi đọc bài, Kiểm tra quyền tác giả hoặc Admin khi xóa bài, Sinh đường dẫn thân thiện SEO (Slug), và Cơ chế kiểm tra trạng thái Like/Bookmark của người dùng hiện tại (`enrichBlogResponse`).

---

## 1. MÃ NGUỒN VÀ GIẢI THÍCH CHI TIẾT TỪNG PHƯƠNG THỨC

File nằm tại: `src/main/java/com/group/blog/service/BlogService.java`

### 1.1. Tạo bài viết mới (`createBlog`)
```java
    @Transactional
    public BlogResponse createBlog(BlogCreationRequest request) {
        // 1. Lấy thông tin tác giả từ Token đăng nhập
        var context = SecurityContextHolder.getContext();
        String currentUsername = context.getAuthentication().getName();
        User author = userRepository.findByUsername(currentUsername)
                .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));

        // 2. Kiểm tra Danh mục (nếu có chọn thì tìm trong DB)
        Category category = null;
        if (request.getCategoryId() != null) {
            category = categoryRepository.findById(request.getCategoryId())
                    .orElseThrow(() -> new AppException(ErrorCode.CATEGORY_NOT_FOUND));
        }

        // 3. Chuyển đổi DTO sang Entity và gán tác giả, danh mục
        Blog blog = blogMapper.toBlog(request);
        blog.setAuthor(author);
        blog.setCategory(category);

        // 4. Xử lý Thẻ Tag (Nếu tag đã có thì dùng lại, chưa có thì tạo mới)
        if (request.getTags() != null && !request.getTags().isEmpty()) {
            Set<Tag> finalTags = new HashSet<>();
            for (String tagName : request.getTags()) {
                Tag tag = tagRepository.findByName(tagName)
                        .orElseGet(() -> {
                            Tag newTag = new Tag();
                            newTag.setName(tagName);
                            return tagRepository.save(newTag);
                        });
                finalTags.add(tag);
            }
            blog.setTags(finalTags);
        }
        return enrichBlogResponse(blogRepository.save(blog));
    }
```
- **Điểm sáng kiến trúc về Thẻ Tag (`orElseGet`)**:
  - Khi tác giả nhập danh sách tag: `["Java", "Spring", "BlebBlog"]`.
  - Hàm `tagRepository.findByName(tagName)` sẽ kiểm tra trong DB.
  - Nếu `"Java"` đã có sẵn, nó sẽ tái sử dụng tag cũ.
  - Nếu `"BlebBlog"` là tag mới tinh chưa từng ai tạo, lệnh `orElseGet()` sẽ tạo đối tượng `new Tag()`, lưu vào bảng `tags` và gán vào bài viết. Điều này ngăn chặn việc tạo trùng lặp thẻ tag trong CSDL.

---

### 1.2. Cập nhật bài viết với Cơ chế Bản nháp độc quyền 2 luồng (`updateBlog`)
```java
    @Transactional
    public BlogResponse updateBlog(UUID id, BlogUpdateRequest request) {
        Blog blog = blogRepository.findById(id)
                .orElseThrow(() -> new AppException(ErrorCode.BLOG_NOT_FOUND));

        // Kiểm tra quyền: Chỉ tác giả của bài viết mới được sửa bài
        var context = SecurityContextHolder.getContext();
        String currentUsername = context.getAuthentication().getName();
        if (!blog.getAuthor().getUsername().equals(currentUsername)) {
            throw new AppException(ErrorCode.UNAUTHORIZED);
        }
```
- Chặn đứng mọi hành vi sửa bài của người khác.

```java
        boolean isRequestingSaveDraft = Boolean.TRUE.equals(request.getDraft());

        if (isRequestingSaveDraft) {
            // HÀNH ĐỘNG 1: LƯU NHÁP (User bấm Save Draft)
            if (blog.isDraft()) {
                // Bài viết trước nay vẫn là bản nháp: Lưu thẳng vào content
                if(request.getContent() != null) blog.setContent(request.getContent());
                if(request.getBanner() != null) blog.setBanner(request.getBanner());
            } else {
                // ĐẶC BIỆT: Bài viết ĐÃ XUẤT BẢN CÔNG KHAI, tác giả vào sửa lại
                // Không được sửa cột content (vì độc giả bên ngoài đang đọc bài đó!)
                // Lưu nội dung chỉnh sửa mới vào draftContent
                if(request.getContent() != null) blog.setDraftContent(request.getContent());
                if(request.getBanner() != null) blog.setDraftBanner(request.getBanner());
            }
        } else {
            // HÀNH ĐỘNG 2: XUẤT BẢN (User bấm Publish)
            // Đổ nội dung mới vào cột content chính thức
            if(request.getContent() != null) blog.setContent(request.getContent());
            if(request.getBanner() != null) blog.setBanner(request.getBanner());

            // Xóa rỗng bản nháp vì bản nháp đã được công khai
            blog.setDraftContent(null);
            blog.setDraftBanner(null);
            blog.setDraft(false);

            if (blog.getPublishedAt() == null) {
                blog.setPublishedAt(LocalDateTime.now());
            }
        }
```
- **Ý nghĩa thực tế**: Đây là tính năng giống hệt như trên nền tảng **Medium.com**. Độc giả vẫn xem được phiên bản bài viết cũ ổn định, trong khi tác giả có thể thảnh thơi lưu bản nháp sửa đổi qua nhiều ngày. Khi tác giả bấm "Publish", nội dung mới mới chính thức thay thế bản cũ!

---

### 1.3. Xem chi tiết bài viết và Tự động tăng lượt xem (`getBlogById`)
```java
    @Transactional
    public BlogResponse getBlogById(UUID id) {
        Blog blog = blogRepository.findById(id)
                .orElseThrow(() -> new AppException(ErrorCode.BLOG_NOT_FOUND));

        // Tự động ghi nhận một lượt xem mới vào bảng blog_views
        BlogView view = new BlogView();
        view.setBlog(blog);
        blogViewRepository.save(view);

        return enrichBlogResponse(blog);
    }
```
- Mỗi lần người dùng click vào xem bài viết, một bản ghi `BlogView` được lưu vào CSDL, làm tăng chỉ số `totalReads` của bài viết một cách tự động và chính xác.

---

### 1.4. Xóa bài viết với Quyền kép: Tác giả HOẶC Admin (`deleteBlog`)
```java
    @Transactional
    public void deleteBlog(UUID id) {
        Blog blog = blogRepository.findById(id)
                .orElseThrow(() -> new AppException(ErrorCode.BLOG_NOT_FOUND));

        var context = SecurityContextHolder.getContext();
        String currentUsername = context.getAuthentication().getName();

        boolean isAuthor = blog.getAuthor().getUsername().equals(currentUsername);
        boolean isAdmin = context.getAuthentication().getAuthorities().stream()
                .anyMatch(a -> a.getAuthority().equals("ROLE_ADMIN"));

        // Người xóa BẮT BUỘC phải là Tác giả của bài HOẶC là Quản trị viên Admin
        if (!isAuthor && !isAdmin) {
            throw new AppException(ErrorCode.UNAUTHORIZED);
        }

        blogRepository.deleteById(id);
    }
```
- Thiết kế phân quyền cực kỳ chặt chẽ: Một tác giả bình thường chỉ có thể xóa bài viết của chính mình. Quản trị viên (Admin) có quyền tối cao xóa bất kỳ bài viết nào vi phạm quy định cộng đồng.

---

### 1.5. Hàm bổ trợ làm giàu dữ liệu DTO (`enrichBlogResponse`)
```java
    private BlogResponse enrichBlogResponse(Blog blog) {
        BlogResponse response = blogMapper.toBlogResponse(blog);

        // 1. Tạo Slug chuẩn SEO: "tieu-de-khong-dau-uuid"
        String generatedSlug = SlugUtils.generateSlug(blog.getTitle()) + "-" + blog.getId().toString();
        response.setSlug(generatedSlug);

        // 2. Đếm số liệu tương tác thực tế từ Database
        response.setTotalReads((int) blogViewRepository.countByBlogId(blog.getId()));
        response.setTotalLikes((int) blogLikeRepository.countByBlogId(blog.getId()));
        response.setTotalComments((int) commentRepository.countByBlogId(blog.getId()));

        // 3. Kiểm tra xem người dùng hiện tại đã Like và Bookmark bài này chưa
        var authentication = SecurityContextHolder.getContext().getAuthentication();
        if (authentication != null && authentication.isAuthenticated() && !authentication.getName().equals("anonymousUser")) {
            String currentUsername = authentication.getName();
            boolean isLiked = blogLikeRepository.existsByBlogIdAndUserUsername(blog.getId(), currentUsername);
            boolean isBookmarked = bookmarkRepository.existsByBlogIdAndUserUsername(blog.getId(), currentUsername);
            response.setLikedByCurrentUser(isLiked);
            response.setBookmarkedByCurrentUser(isBookmarked);
        } else {
            response.setLikedByCurrentUser(false);
            response.setBookmarkedByCurrentUser(false);
        }
        return response;
    }
```
- Khi trả bài viết về cho trình duyệt, hàm này sẽ bổ sung các thông tin động:
  - `likedByCurrentUser: true/false`: Giúp nút Like trên giao diện tự động đổi màu đỏ nếu người đang xem đã thích bài viết này.
  - `bookmarkedByCurrentUser: true/false`: Giúp nút Lưu đổi icon nếu bài viết đã có trong sổ tay.
  - Khách vãng lai (`anonymousUser`) chưa đăng nhập sẽ nhận về `false`.

---

## 2. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN VỀ BLOGSERVICE & TRẢ LỜI ĐIỂM 10

### Câu 1: Em hãy giải thích cơ chế sinh Slug của bài viết trong hàm `enrichBlogResponse()`? Tại sao lại ghép thêm UUID vào cuối Slug?
- **Trả lời**:
  > "Thưa thầy/cô:
  > - Slug là chuỗi ký tự không dấu ngăn cách bằng dấu gạch ngang (ví dụ: `kham-pha-kien-truc-spring-boot-3`), giúp đường dẫn bài viết thân thiện với công cụ tìm kiếm (SEO Friendly) và người dùng dễ đọc hơn.
  > - Nhóm em sử dụng định dạng: `[slug-tieu-de]-[UUID]`.
  > - **Lý do bắt buộc phải ghép UUID vào cuối**: Hai tác giả khác nhau hoàn toàn có thể đặt cùng một tiêu đề bài viết (ví dụ cùng viết bài có tên 'Học Java cơ bản'). Nếu chỉ dùng slug theo tiêu đề thì sẽ bị trùng lặp URL. Khi ghép UUID vào cuối, URL vừa đẹp mắt chuẩn SEO, vừa đảm bảo tính duy nhất 100%. Khi người dùng click vào link, Backend chỉ cần bóc tách chuỗi UUID ở đuôi là tìm thấy bài viết ngay lập tức với tốc độ của khóa chính!"

### Câu 2: Trong hàm `deleteBlog()`, nếu bài viết có hàng chục Comment và Like thì khi xóa có bị lỗi vi phạm khóa ngoại (Foreign Key Constraint Violation) không?
- **Trả lời**:
  > "Thưa thầy/cô, hoàn toàn không bị lỗi!
  > Vì trong các Entity `Comment`, `BlogLike`, `Bookmark`, `BlogView`, nhóm em đều đã cấu hình chú thích:
  > `@org.hibernate.annotations.OnDelete(action = OnDeleteAction.CASCADE)`.
  > Chú thích này sinh trực tiếp ràng buộc `ON DELETE CASCADE` ở tầng CSDL. Khi lệnh `blogRepository.deleteById(id)` được thực thi, CSDL H2/MySQL sẽ tự động xóa sạch tất cả Comment, Like, Bookmark và View của bài viết đó chỉ trong một giao dịch duy nhất, đảm bảo tính toàn vẹn dữ liệu hoàn hảo."
