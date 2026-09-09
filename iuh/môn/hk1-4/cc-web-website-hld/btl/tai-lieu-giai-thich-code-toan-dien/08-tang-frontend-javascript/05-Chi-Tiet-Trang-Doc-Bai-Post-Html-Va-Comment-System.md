# CHI TIẾT TRANG ĐỌC BÀI VIẾT (POST.HTML) & HỆ THỐNG COMMENT ĐA CẤP

> **Vị trí file mã nguồn:** `src/main/resources/templates/public/post.html` (và bản tĩnh tại `src/main/resources/static/pages/post.html`)  
> **Mục đích:** Trang hiển thị chi tiết bài viết, giải mã nội dung khối rich text từ Editor.js, tăng lượt đọc, thả tim, đánh dấu bài viết, theo dõi tác giả và luồng bình luận dạng cây (nested comment thread).

---

## 1. Bản Chất Nghiệp Vụ Của Trang Đọc Bài Viết

Khi một độc giả bấm vào một bài viết từ trang chủ:
1. Trình duyệt mở đường dẫn: `post.html?id=tieu-de-bai-viet-3f7b9c12-88a4-4a55-b001-c89283749210`
2. Frontend bóc tách UUID từ chuỗi slug (`3f7b9c12-88a4-4a55-b001-c89283749210`).
3. Frontend gửi request `GET /blogs/{id}` để lấy toàn bộ dữ liệu bài viết (tiêu đề, banner, tác giả, tags, và chuỗi JSON nội dung `content`).
4. Hệ thống ngầm ghi nhận lượt xem (gửi thông tin trình duyệt & IP).
5. Frontend duyệt mảng khối (`blocks`) trong chuỗi JSON và chuyển đổi thành HTML tương ứng.
6. Độc giả có thể mở sidebar bình luận, bấm Thích, Lưu bài viết hoặc Bấm Theo dõi tác giả.

---

## 2. Giải Thích Chi Tiết Từng Khối Code Trong post.html

### 2.1. Cấu hình biến màu sắc giao diện Dark Theme & Style cây bình luận

```css
:root {
  --surface:               #0b0e14;
  --on-surface:            #e0e5f5;
  --on-surface-variant:    #a5abba;
  --outline-variant:       #424855;
  --primary:               #ac8aff;
}

/* Đường kẻ dọc cho Reply lồng nhau (Cây bình luận) */
.comment-thread { position: relative; }
.comment-thread::before {
  content: ''; position: absolute;
  left: 15px; top: 40px; bottom: -10px; /* Căn lề theo tâm avatar */
  width: 2px; background-color: #2D333B;
  border-radius: 2px;
}
```

* **Dòng 16-22**: Định nghĩa các biến màu sắc CSS (`--surface`: màu nền tối đen ánh xanh, `--primary`: màu tím lavender huyền bí đặc trưng của Bleb).
* **Dòng 29-35 (`.comment-thread::before`)**: Tạo một đường kẻ mảnh màu xám chạy dọc từ avatar của bình luận cha xuống các câu trả lời con. Đây là thiết kế chuẩn UI hiện đại giống hệt Reddit hoặc Facebook, giúp người đọc nhận biết câu trả lời nào thuộc về bình luận nào.

---

### 2.2. Khởi tạo trang, bóc tách ID và gọi API chi tiết

```javascript
let blogId = null;
let globalBlogAuthor = '';
let commentIdToDelete = null; // Biến tạm lưu ID bình luận cần xóa

$(document).ready(function() {
  $('#navbar-container').load('../fragments/navbar.html', function() {
    if (typeof updateNavAuth === 'function') updateNavAuth();
  });
  $('#footer-container').load('../fragments/footer.html');

  const urlParams = new URLSearchParams(window.location.search);
  const slug = urlParams.get('id');

  if (!slug) {
    $('#article-wrapper').html('<div class="alert alert-danger text-center">Không tìm thấy mã bài viết!</div>');
    return;
  }

  blogId = extractIdFromSlug(slug);

  callApi('/blogs/' + blogId, 'GET').done(function(res) {
    const post = res.result || res;
    renderArticle(post);
    if (urlParams.get('openComments') === 'true') {
      setTimeout(() => { openCommentSidebar(); }, 500);
    }
  }).fail(function() {
    $('#article-wrapper').html(`
      <div class="text-center py-5">
          <span class="material-symbols-outlined text-danger" style="font-size: 4rem;">error</span>
          <h3 class="mt-3 text-light">Bài viết không tồn tại</h3>
          <p style="color: var(--on-surface-variant);">Có thể bài viết đã bị xóa hoặc đường dẫn không hợp lệ.</p>
          <a href="home-page.html" class="btn mt-3" style="background: var(--primary); color: #000; border-radius: 99px; padding: 0.5rem 1.5rem; font-weight: 600;">Về trang chủ</a>
      </div>
    `);
  });
});
```

* **`URLSearchParams(window.location.search)`**: Lấy tham số truy vấn trên thanh địa chỉ.
* **`extractIdFromSlug(slug)`**: Hàm tiện ích lấy chính xác 36 ký tự UUID ở đuôi chuỗi slug.
* **`callApi('/blogs/' + blogId, 'GET')`**: Gửi yêu cầu lấy chi tiết bài viết. Nếu người dùng đã đăng nhập, `callApi` tự động kèm Header `Authorization: Bearer <token>`, từ đó Backend nhận biết được người đọc này đã Like bài hay chưa (`isLiked`), đã Bookmark bài hay chưa (`isBookmarked`).
* **`openComments === 'true'`**: Nếu người dùng bấm từ trang chủ vào nút icon bình luận, URL sẽ có cờ `openComments=true`, trang sẽ tự động bung Sidebar bình luận sau 500ms.

---

### 2.3. Bóc tách và hiển thị nội dung khối (Editor.js Parser)

Trong database, trường `content` của `Blog` được lưu dưới dạng chuỗi JSON của Editor.js, ví dụ:
```json
{"blocks":[{"type":"paragraph","data":{"text":"Xin chào..."}},{"type":"h1","data":{"text":"Tiêu đề lớn"}}]}
```
Hàm `renderArticle` chịu trách nhiệm chuyển đổi chuỗi JSON này sang HTML:

```javascript
let contentHtml = '';
try {
  const data = JSON.parse(post.content);
  if (data && data.blocks) {
    data.blocks.forEach(b => {
      switch(b.type) {
        case 'paragraph': contentHtml += `<p>${b.data.text}</p>`; break;
        case 'h1': contentHtml += `<h2>${b.data.text}</h2>`; break;
        case 'h2': case 'h3': contentHtml += `<h3>${b.data.text}</h3>`; break;
        case 'image': 
          contentHtml += `<figure><img src="${b.data.url}" alt="image">${b.data.caption ? `<figcaption class="text-center text-muted mt-2" style="font-size: 0.85rem; font-style: italic;">${b.data.caption}</figcaption>` : ''}</figure>`; 
          break;
        case 'quote': contentHtml += `<blockquote>${b.data.text}</blockquote>`; break;
        case 'code': contentHtml += `<pre><code>${b.data.text}</code></pre>`; break;
        case 'bullet': contentHtml += `<ul><li>${b.data.text}</li></ul>`; break;
        case 'numbered': contentHtml += `<ol><li>${b.data.text}</li></ol>`; break;
        case 'divider': contentHtml += `<hr>`; break;
      }
    });
  }
} catch (e) {
  // Dự phòng nếu bài viết cũ lưu bằng plain text hoặc HTML trực tiếp
  contentHtml = `<p>${post.content}</p>`;
}
```

* **`JSON.parse(post.content)`**: Chuyển chuỗi JSON sang Object.
* **`switch(b.type)`**: Duyệt từng khối block:
  - Khối chữ thường (`paragraph`): Đặt trong thẻ `<p>`.
  - Khối tiêu đề (`h1`, `h2`, `h3`): Đặt trong thẻ `<h2>` hoặc `<h3>`.
  - Khối ảnh (`image`): Đặt trong `<figure><img>` kèm chú thích `<figcaption>` nếu tác giả có nhập caption.
  - Khối code (`code`): Đặt trong thẻ `<pre><code>` với font lập trình `JetBrains Mono`.
  - Khối trích dẫn (`quote`): Đặt trong `<blockquote>` có viền tím bên trái.
  - Khối danh sách (`bullet`, `numbered`): Thẻ `<ul>` hoặc `<ol>`.
  - Khối ngăn cách (`divider`): Thẻ `<hr>`.
* **Khối `catch (e)`**: Đảm bảo website không bao giờ bị sập (white screen) nếu nội dung lưu dạng văn bản thô cũ.

---

### 2.4. Xử lý Thả Tim (Like / Unlike) & Đánh dấu (Bookmark)

```javascript
function toggleLike() {
  if (!S.isAuth) {
    toast("Vui lòng đăng nhập để thích bài viết!");
    return;
  }
  callApi('/blogs/' + blogId + '/like', 'POST').done(function(res) {
    const isLiked = res.result; // Backend trả về true nếu vừa like, false nếu vừa bỏ like
    const $icon = $('#like-icon');
    const $count = $('#like-count');
    let count = parseInt($count.text()) || 0;

    if (isLiked) {
      $icon.removeClass('heart-outline').addClass('heart-filled');
      $count.text(count + 1);
      toast("Đã thích bài viết!");
    } else {
      $icon.removeClass('heart-filled').addClass('heart-outline');
      $count.text(Math.max(0, count - 1));
      toast("Đã bỏ thích bài viết.");
    }
  });
}
```

* **Kiểm tra `S.isAuth`**: Chặn khách vãng lai, hiển thị Toast nhắc đăng nhập.
* **Gọi `POST /blogs/{id}/like`**: Backend kích hoạt `toggleLike()` trong `InteractionService`:
  - Nếu đã có bản ghi trong bảng `blog_likes`: Xóa bản ghi và trả về `false`.
  - Nếu chưa có: Tạo bản ghi mới, gửi `Notification` thông báo cho tác giả, và trả về `true`.
* **Cập nhật UI mượt mà**: Đổi icon từ viền (`heart-outline`) sang đỏ đặc (`heart-filled`), đồng thời tăng/giảm biến đếm số lượng hiển thị ngay lập tức mà không cần reload trang.

---

### 2.5. Hệ Thống Bình Luận Phân Cấp (Tree Comments)

#### Nạp danh sách bình luận:
```javascript
function loadComments() {
  callApi('/blogs/' + blogId + '/comments', 'GET').done(function(res) {
    const comments = res.result || [];
    $('#sidebar-comment-count').text(comments.length);
    renderCommentsList(comments);
  });
}
```

#### Xây dựng giao diện cây đệ quy:
```javascript
function renderCommentsList(comments) {
  const $list = $('#comments-list').empty();
  if (comments.length === 0) {
    $list.html('<div class="text-center py-10 text-[#a5abba] text-sm">Chưa có bình luận nào. Hãy là người đầu tiên!</div>');
    return;
  }

  // 1. Phân loại bình luận cha (parentId == null) và bình luận con (replies)
  const parents = comments.filter(c => !c.parentId);
  const replies = comments.filter(c => c.parentId);

  parents.forEach(p => {
    // Lọc ra các câu trả lời con thuộc về bình luận cha p
    const childReplies = replies.filter(r => r.parentId === p.id);
    $list.append(buildCommentHtml(p, childReplies));
  });
}
```

* **Tách biệt 2 tầng**: Nhóm các bình luận gốc (`parentId == null`) làm gốc cây, các phản hồi (`childReplies`) được lồng vào trong khung con thụt lề vào trong kèm thanh kẻ dọc `.comment-thread`.

#### Quyền xóa bình luận (Authorization):
```javascript
const canDelete = (S.uname === c.user.username) || (S.uname === globalBlogAuthor) || S.isAdmin;
```
Một bình luận có thể được xóa bởi 3 đối tượng:
1. Chính người đã viết ra bình luận đó (`S.uname === c.user.username`).
2. Tác giả của bài viết (`S.uname === globalBlogAuthor`) — tác giả có quyền kiểm duyệt mọi bình luận dưới bài của mình.
3. Quản trị viên hệ thống (`S.isAdmin`).

---

## 3. Câu Hỏi Vấn Đáp Giảng Viên Hay Hỏi Về post.html

### ❓ Câu 1: Làm thế nào Frontend hiển thị được nội dung bài viết nếu nội dung đó lưu dưới dạng JSON của Editor.js?
> **Trả lời:** Em sử dụng hàm `renderArticle()` bọc trong khối `try-catch`. Hàm này parse chuỗi JSON từ `post.content` để lấy mảng `blocks`. Sau đó dùng vòng lặp duyệt qua từng block và dựa vào thuộc tính `b.type` (`paragraph`, `h1`, `image`, `code`, `quote`...) để nối chuỗi HTML tương ứng, gắn vào thẻ `#article-wrapper`.

### ❓ Câu 2: Khi người dùng bấm Thả tim, nếu mạng bị lag thì có bị bấm liên tục (Spam) không?
> **Trả lời:** Khi người dùng click, giao diện có thể disable nút tạm thời trong khi chờ Promise của AJAX hoàn tất. Ở Backend, bảng `blog_likes` được áp dụng ràng buộc duy nhất `@UniqueConstraint(columnNames = {"user_id", "blog_id"})`, do đó kể cả có 2 request gửi đồng thời thì CSDL cũng không bao giờ bị nhân đôi lượt thích.

### ❓ Câu 3: Ai có quyền xóa một bình luận trên website?
> **Trả lời:** Em phân quyền xóa bình luận ở cả Frontend lẫn Backend theo 2 cấp:
> 1. Người viết bình luận đó.
> 2. Tác giả của bài viết (chủ nhà có quyền dọn dẹp bình luận rác).
> 3. Admin hệ thống.
> Ở Backend, phương thức `deleteComment` trong `InteractionService` kiểm tra `SecurityContextHolder` để xác thực quyền này trước khi xóa khỏi CSDL.
