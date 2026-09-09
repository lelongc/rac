# GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG INTERACTIONSERVICE

> **Mục tiêu**: Nắm vững 100% nghiệp vụ tương tác mạng xã hội của Blog: Cơ chế bật/tắt Thích bài viết (`toggleLike`), Lưu bài viết vào sổ tay (`toggleBookmark`), Thuật toán đệ quy xây dựng cây bình luận đa tầng (`addComment`, `mapToCommentResponse`), và Cơ chế phân quyền thông minh khi xóa bình luận.

---

## 1. MÃ NGUỒN VÀ GIẢI THÍCH CHI TIẾT TỪNG TÍNH NĂNG

File nằm tại: `src/main/java/com/group/blog/service/InteractionService.java`

### 1.1. Nghiệp vụ Thích và Bỏ thích bài viết (`toggleLike`)
```java
    @Transactional
    public void toggleLike(UUID blogId) {
        String username = SecurityContextHolder.getContext().getAuthentication().getName();

        Optional<BlogLike> existingLike = blogLikeRepository.findByBlogIdAndUserUsername(blogId, username);

        if (existingLike.isPresent()) {
            // Đã like rồi -> Người dùng click lần nữa là BỎ THÍCH (Unlike)
            blogLikeRepository.delete(existingLike.get());
        } else {
            // Chưa like -> THỰC HIỆN THÍCH (Like)
            Blog blog = blogRepository.findById(blogId)
                    .orElseThrow(() -> new AppException(ErrorCode.BLOG_NOT_FOUND));
            User user = userRepository.findByUsername(username)
                    .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));

            BlogLike newLike = BlogLike.builder().blog(blog).user(user).build();
            blogLikeRepository.save(newLike);

            // Gửi thông báo đến tác giả của bài viết
            String slug = SlugUtils.generateSlug(blog.getTitle()) + "-" + blog.getId();
            notificationService.createNotification(
                    blog.getAuthor(),
                    "@" + username + " liked your article \"" + blog.getTitle() + "\".",
                    "post.html?id=" + slug,
                    "LIKE"
            );
        }
    }
```
- **Nguyên lý Toggle (Bật / Tắt)**:
  - Thay vì phải tạo 2 API riêng biệt (`/like` và `/unlike`), hệ thống gom lại thành một phương thức `toggleLike` duy nhất.
  - Hệ thống tự động kiểm tra CSDL: Nếu đã thích rồi thì xóa bản ghi (giảm like), nếu chưa thích thì thêm bản ghi (tăng like) và tự động kích hoạt thông báo gửi đến tác giả bài viết.

---

### 1.2. Thêm bình luận và Trả lời bình luận (`addComment`)
```java
    @Transactional
    public CommentResponse addComment(UUID blogId, CommentRequest request) {
        String username = SecurityContextHolder.getContext().getAuthentication().getName();
        User user = userRepository.findByUsername(username)
                .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));
        Blog blog = blogRepository.findById(blogId)
                .orElseThrow(() -> new AppException(ErrorCode.BLOG_NOT_FOUND));

        Comment comment = Comment.builder()
                .content(request.getContent())
                .blog(blog)
                .user(user)
                .build();

        if (request.getParentId() != null) {
            Comment parent = commentRepository.findById(request.getParentId())
                    .orElseThrow(() -> new RuntimeException("Parent comment not found"));

            // Thuật toán làm phẳng phân cấp: Không cho reply lồng nhau quá sâu
            if(parent.getParent() != null) {
                // Nếu bình luận cha vốn dĩ đã là một câu trả lời rồi, 
                // ta gán bình luận mới cùng cấp với cha đó luôn
                comment.setParent(parent.getParent());
            } else {
                comment.setParent(parent);
            }
        }

        Comment savedComment = commentRepository.save(comment);
        String slug = SlugUtils.generateSlug(blog.getTitle()) + "-" + blog.getId();
        String targetUrl = "post.html?id=" + slug + "&openComments=true";

        if (request.getParentId() != null) {
            // Reply vào comment của ai -> Gửi thông báo cho chủ của bình luận đó
            Comment parent = commentRepository.findById(request.getParentId()).orElseThrow();
            notificationService.createNotification(
                    parent.getUser(),
                    "@" + username + " replied to your comment on \"" + blog.getTitle() + "\".",
                    targetUrl,
                    "REPLY"
            );
        } else {
            // Comment trực tiếp vào bài -> Gửi thông báo cho tác giả bài viết
            notificationService.createNotification(
                    blog.getAuthor(),
                    "@" + username + " commented on your article \"" + blog.getTitle() + "\".",
                    targetUrl,
                    "COMMENT"
            );
        }
        return mapToCommentResponse(savedComment);
    }
```
- **Thuật toán hạn chế lồng sâu (Max Depth Flattener)**:
  - Nếu cho phép người dùng trả lời lồng nhau vô hạn (A trả lời B, C trả lời A, D trả lời C...), giao diện sẽ bị thụt lề liên tục sang phải cho đến khi tràn màn hình điện thoại.
  - Đoạn code `if(parent.getParent() != null)` giới hạn cấu trúc bình luận tối đa ở **mức 2 cấp** (Bình luận gốc và các câu trả lời con), giống như thiết kế của Facebook và YouTube.

---

### 1.3. Thuật toán đệ quy chuyển đổi Cây bình luận (`mapToCommentResponse`)
```java
    private CommentResponse mapToCommentResponse(Comment comment) {
        UserResponse userResponse = userMapper.toUserResponse(comment.getUser());

        List<CommentResponse> replies = null;
        if (comment.getReplies() != null && !comment.getReplies().isEmpty()) {
            replies = comment.getReplies().stream()
                    .map(this::mapToCommentResponse) // ĐỆ QUY TỰ GỌI LẠI CHÍNH NÓ
                    .collect(Collectors.toList());
        }

        return CommentResponse.builder()
                .id(comment.getId())
                .content(comment.getContent())
                .createdAt(comment.getCreatedAt())
                .user(userResponse)
                .replies(replies)
                .build();
    }
```
- **Giải thuật đệ quy**: Lặp qua danh sách `comment.getReplies()` và tự gọi lại hàm `mapToCommentResponse` để đóng gói toàn bộ cây phản hồi con thành đối tượng JSON nhiều tầng hoàn chỉnh gửi về cho giao diện.

---

### 1.4. Phân quyền xóa bình luận (`deleteComment`)
```java
    @Transactional
    public void deleteComment(UUID commentId) {
        Comment comment = commentRepository.findById(commentId)
                .orElseThrow(() -> new RuntimeException("Comment not found"));

        String currentUsername = SecurityContextHolder.getContext().getAuthentication().getName();
        String commentAuthor = comment.getUser().getUsername();
        String blogAuthor = comment.getBlog().getAuthor().getUsername();

        // ĐIỀU KIỆN KÉP: Chỉ người viết comment HOẶC chủ bài viết mới được quyền xóa
        if (!currentUsername.equals(commentAuthor) && !currentUsername.equals(blogAuthor)) {
            throw new AppException(ErrorCode.UNAUTHORIZED);
        }

        commentRepository.delete(comment);
    }
```
- **Tư duy thiết kế thực tế**:
  - Người viết bình luận dĩ nhiên có quyền xóa bình luận của mình nếu muốn rút lại lời nói.
  - Chủ bài viết (Tác giả blog) cũng có quyền xóa bình luận khiêu khích hoặc spam rác dưới bài viết của họ.
  - Những người dùng khác hoàn toàn không có quyền can thiệp (ném lỗi 401/403 `UNAUTHORIZED`).

---

## 2. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN VỀ INTERACTIONSERVICE

### Câu 1: Em hãy giải thích điều kiện kiểm tra quyền trong hàm `deleteComment()`? Tại sao chủ bài viết lại được xóa bình luận của người khác?
- **Trả lời**:
  > "Thưa thầy/cô:
  > Trong hàm `deleteComment()`, chúng em so sánh `currentUsername` (người đang gọi API) với:
  > 1. `commentAuthor`: Người đã viết ra bình luận đó.
  > 2. `blogAuthor`: Tác giả sở hữu bài viết đang chứa bình luận đó.
  > 
  > Nếu `currentUsername` không trùng với cả 2 người trên thì hệ thống từ chối quyền thực thi. Việc cho phép chủ bài viết xóa bình luận là một tính năng quản trị bắt buộc trên mọi mạng xã hội, giúp tác giả có quyền kiểm duyệt, gỡ bỏ các bình luận xúc phạm hoặc quảng cáo rác trên 'ngôi nhà' bài viết của chính mình."
