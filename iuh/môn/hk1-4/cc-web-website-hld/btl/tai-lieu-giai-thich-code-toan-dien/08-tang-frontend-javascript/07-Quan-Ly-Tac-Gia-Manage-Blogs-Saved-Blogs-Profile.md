# KHÔNG GIAN TÁC GIẢ: QUẢN LÝ BÀI VIẾT, BOOKMARK, HỒ SƠ & HỘP THƯ THÔNG BÁO

> **Các file mã nguồn liên quan:**  
> - `src/main/resources/templates/public/Manage-Blogs.html`: Bảng điều khiển quản lý bài viết cá nhân của tác giả.  
> - `src/main/resources/templates/public/saved-blogs.html`: Trang danh sách bài viết đã lưu (Bookmarks).  
> - `src/main/resources/templates/public/user-profile.html` & `edit-profile.html`: Trang hồ sơ công khai & chỉnh sửa thông tin cá nhân.  
> - `src/main/resources/templates/public/notifications.html`: Hộp thư thông báo tương tác thời gian thực.  
> - `src/main/resources/templates/fragments/dashboard-sidebar.html`: Thanh điều hướng tác giả dùng chung.

---

## 1. Bản Chất Không Gian Tác Giả (Author Dashboard Architecture)

Khi người dùng đăng nhập thành công vào website, họ có một không gian quản trị cá nhân khép kín:
- **Menu điều hướng chung (`dashboard-sidebar.html`)**: Được nhúng tự động vào bên trái của các trang quản lý thông qua jQuery `.load()`. Giúp người dùng chuyển nhanh giữa: *Quản lý bài viết ➔ Bài đã lưu ➔ Hộp thư thông báo ➔ Hồ sơ cá nhân*.
- **Xác thực phiên làm việc (`S.isAuth`)**: Tất cả các trang này đều kiểm tra `if (!S.isAuth) window.location.href = 'login.html';` ngay từ dòng đầu tiên. Khách vãng lai cố tình nhập URL đều bị đẩy về trang đăng nhập.

---

## 2. Bóc Tách Chi Tiết Từng Giao Diện

### 2.1. Quản Lý Bài Viết Của Tôi (Manage-Blogs.html)

Trang này cho phép tác giả theo dõi toàn bộ các bài viết do chính mình sáng tác, phân chia thành 2 tab: **Published (Đã xuất bản)** và **Drafts (Bản nháp)**.

```javascript
// Chuyển đổi giữa 2 Tab: Đã xuất bản và Bản nháp
function switchTab(tab) {
    $('.tab-btn').removeClass('active text-primary font-bold').addClass('text-on-surface-variant font-medium');
    $('#content-published, #content-drafts').addClass('hidden');

    if(tab === 'published') {
        $('#tab-published').addClass('active text-primary font-bold').removeClass('text-on-surface-variant font-medium');
        $('#content-published').removeClass('hidden');
    } else {
        $('#tab-drafts').addClass('active text-primary font-bold').removeClass('text-on-surface-variant font-medium');
        $('#content-drafts').removeClass('hidden');
    }
    $('#dashboard-search').val('');
    $('#content-published article, #content-drafts article').show();
}
```

#### Tải bài viết từ API `GET /blogs/my-blogs`:
```javascript
callApi('/blogs/my-blogs', 'GET').done(function(res) {
    const blogs = res.result || [];
    let pubCount = 0, draftCount = 0;

    blogs.forEach(p => {
        const bannerUrl = p.banner || 'https://placehold.co/600x400/151a22/a5abba?text=No+Image';
        const dateStr = fmtDate(p.createdAt);

        if (p.draft === false) {
            pubCount++;
            // Render card bài viết đã xuất bản kèm nút Xem, Sửa, Xóa
            $pubList.append(buildMyBlogItem(p, bannerUrl, dateStr, false));
        } else {
            draftCount++;
            // Render card bài viết nháp kèm nút "Tiếp tục viết"
            $draftList.append(buildMyBlogItem(p, bannerUrl, dateStr, true));
        }
    });

    $('#count-published').text(`(${pubCount})`);
    $('#count-drafts').text(`(${draftCount})`);
});
```

* **Lọc tức thì tại Frontend (Client-side Search)**: Khi tác giả gõ từ khóa vào ô `#dashboard-search`, JavaScript lắng nghe sự kiện `input` và ẩn/hiện các thẻ `<article>` ngay trong mili-giây mà không cần gửi thêm request lên server.
* **Xóa bài viết**: Kích hoạt `callApi('/blogs/' + id, 'DELETE')`. Backend kiểm tra tác giả trong token JWT xem có đúng là chủ sở hữu bài viết hay không trước khi xóa.

---

### 2.2. Danh Sách Bài Viết Đã Bookmark (saved-blogs.html)

Trang hiển thị bộ sưu tập các bài viết mà người dùng đã bấm lưu (Bookmark) để đọc lại sau.

```javascript
function loadSavedBlogs() {
    callApi('/blogs/bookmarks', 'GET').done(function(res) {
        const blogs = res.result || [];
        if (blogs.length === 0) {
            $('#saved-list').html(`
                <div class="text-center py-16 bg-[#151a22]/50 rounded-2xl border border-dashed border-[#424855]/30">
                    <span class="material-symbols-outlined text-5xl text-[#424855] mb-3">bookmark_border</span>
                    <p class="text-[#a5abba]">Bạn chưa lưu bài viết nào.</p>
                    <a href="home-page.html" class="text-[#ac8aff] hover:underline mt-2 inline-block font-medium">Khám phá bài viết ngay</a>
                </div>
            `);
            return;
        }
        // Render danh sách các bài viết đã bookmark
        renderSavedArticles(blogs);
    });
}
```

* **Bỏ lưu bài viết (Unbookmark)**: Khi người dùng bấm icon Bookmark trên danh sách, một Modal xác nhận sẽ bật lên. Khi bấm "Xác nhận", hệ thống gọi `POST /blogs/{id}/bookmark` (Backend tự động xóa bản ghi khỏi bảng `blog_bookmarks`) và thẻ bài viết biến mất bằng hiệu ứng mờ dần (`fadeOut(300)`).

---

### 2.3. Hồ Sơ Cá Nhân & Danh Sách Người Theo Dõi (user-profile.html)

Trang hồ sơ hiển thị toàn bộ chân dung tác giả:
- Ảnh đại diện có viền hào quang tím (`.avatar-ring`).
- Họ và tên, `@username`, tiểu sử (Bio).
- Bộ ba chỉ số uy tín: **Followers (Người theo dõi)**, **Following (Đang theo dõi)**, **Reads (Tổng lượt đọc)**.
- Toàn bộ danh sách bài viết công khai của tác giả này.

#### Cửa sổ Modal hiển thị danh sách Followers / Following:
```javascript
function openFollowModal(type) {
    const title = type === 'followers' ? 'Người theo dõi' : 'Đang theo dõi';
    $('#modal-follow-title').text(title);
    $('#follow-modal').modal('show');

    const endpoint = `/users/${profileUserId}/${type}`;
    callApi(endpoint, 'GET').done(function(res) {
        const users = res.result || [];
        renderFollowModalList(users);
    });
}
```

* Trong Modal này có tích hợp ô tìm kiếm real-time và nút **Follow / Unfollow** trực tiếp. Người dùng có thể theo dõi lại ngay trong danh sách mà không cần rời khỏi trang profile!

---

### 2.4. Hộp Thư Thông Báo Thời Gian Thực (notifications.html)

Trung tâm nhận thông báo khi có người khác tương tác với tài khoản của mình.

#### Phân loại thông báo bằng màu sắc và Icon:
```javascript
notifs.forEach((n, index) => {
    let icon = ''; let colorClass = ''; let bgClass = '';

    if (n.type === 'LIKE') {
        icon = 'favorite'; // Trái tim
        colorClass = 'text-[#ac8aff]'; // Tím
        bgClass = 'bg-[#ac8aff]/10 border border-[#ac8aff]/20';
    } else if (n.type === 'COMMENT' || n.type === 'REPLY') {
        icon = 'chat_bubble'; // Bong bóng chat
        colorClass = 'text-[#89ceff]'; // Xanh dương
        bgClass = 'bg-[#89ceff]/10 border border-[#89ceff]/20';
    } else if (n.type === 'FOLLOW') {
        icon = 'person_add'; // Người cộng
        colorClass = 'text-[#c9f791]'; // Xanh lá cây chanh
        bgClass = 'bg-[#c9f791]/10 border border-[#c9f791]/20';
    }
});
```

* **Vạch chỉ thị Chưa đọc (Unread Indicator)**: Với thông báo chưa đọc (`!n.read`), bên mép trái thẻ có một vạch sáng tím phát sáng (`shadow-[0_0_10px_rgba(172,138,255,0.8)]`).
* **Hành động Click thông báo**: Khi người dùng click vào một thông báo:
  1. Frontend gọi `PUT /api/notifications/{id}/read` để đánh dấu đã đọc trong database.
  2. Ngay lập tức chuyển hướng trình duyệt đến bài viết hoặc bình luận tương ứng theo trường `targetUrl` (ví dụ: `post.html?id=bai-viet-slug&openComments=true`).

---

## 3. Câu Hỏi Vấn Đáp Giảng Viên Hay Hỏi Về Không Gian Tác Giả

### ❓ Câu 1: Làm thế nào API `/blogs/my-blogs` biết được cần trả về bài viết của ai mà trên URL không hề có ID người dùng?
> **Trả lời:** Dạ thưa thầy/cô, API này không nhận `userId` trên URL nhằm đảm bảo an toàn tuyệt đối. Thay vào đó, API đọc Header `Authorization: Bearer <token>`. Tại `BlogService`, Spring Boot giải mã JWT từ `SecurityContextHolder.getContext().getAuthentication().getName()` để lấy chính xác username của người đang gọi, rồi truy vấn CSDL: `blogRepository.findByAuthorUsername(username)`. Kẻ xấu không thể giả mạo để xem danh sách bài nháp của người khác.

### ❓ Câu 2: Khi một người vừa bấm Like bài viết của tôi, làm sao hệ thống gửi được thông báo tới trang notifications.html?
> **Trả lời:** Trong `InteractionService.toggleLike()`, sau khi lưu bản ghi vào bảng `blog_likes`, hệ thống sẽ gọi phương thức `notificationService.createNotification()`:
> ```java
> Notification notif = Notification.builder()
>     .recipient(blog.getAuthor()) // Người nhận là tác giả bài viết
>     .actor(currentUser)          // Người vừa thả tim
>     .type(NotificationType.LIKE)
>     .message("@" + currentUser.getUsername() + " đã thích bài viết của bạn.")
>     .targetUrl("post.html?id=" + blog.getSlug())
>     .build();
> ```
> Khi tác giả mở trang thông báo hoặc bấm vào biểu tượng chuông trên thanh Navbar, API `GET /api/notifications` sẽ tải bản ghi này lên hiển thị.

### ❓ Câu 3: Nút Unbookmark trong saved-blogs.html hoạt động như thế nào?
> **Trả lời:** Cơ chế Bookmark của hệ thống được thiết kế theo dạng **Toggle (Bật/Tắt trạng thái)**. Cùng một endpoint `POST /blogs/{id}/bookmark`:
> - Nếu người dùng chưa lưu: Hệ thống tạo bản ghi mới vào `blog_bookmarks` và trả về thông điệp đã lưu.
> - Nếu người dùng đã lưu: Hệ thống xóa bản ghi đó và trả về thông điệp đã bỏ lưu.
> Do đó ở trang `saved-blogs.html`, khi người dùng bấm icon xóa, hàm gửi request lên endpoint này để hủy lưu và dùng hiệu ứng `fadeOut(300)` để xóa thẻ bài viết khỏi màn hình.
