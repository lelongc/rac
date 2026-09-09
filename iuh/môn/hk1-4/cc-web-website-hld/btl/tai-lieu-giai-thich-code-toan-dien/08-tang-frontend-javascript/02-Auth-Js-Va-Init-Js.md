# GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG AUTH.JS VÀ INIT.JS

> **Mục tiêu**: Nắm chắc luồng hiển thị đăng nhập/đăng xuất động (`auth.js`), giải thuật trích xuất chữ cái viết hoa của tên người dùng (`initials`), cơ chế giải phóng phiên làm việc (`handleLogout`), và "ngòi nổ" khởi động trang web (`init.js`).

---

## 1. MÃ NGUỒN VÀ GIẢI THÍCH CHI TIẾT `auth.js`

File nằm tại: `src/main/resources/static/assets/js/auth.js`

```javascript
/**
 * auth.js
 */

function renderAuth() {
    // 1. Xác định vùng chứa trên thanh menu và XÓA SẠCH trước khi vẽ lại
    var $d = $('#auth-area').empty();
    var $m = $('#mob-auth').empty();

    // 2. Kiểm tra trạng thái thực tế từ LocalStorage
    const token = localStorage.getItem('token');
    const uname = localStorage.getItem('username');
    const isAuth = token !== null && token !== "";

    if (isAuth) {
        /* ─────────────── TRẠNG THÁI: ĐÃ ĐĂNG NHẬP ─────────────── */
        const displayName = uname || 'Guest';

        // Nút "New Post" (Viết bài mới)
        $d.append(
            $('<button class="btn-newpost">').html(
                '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>New Post'
            ).on('click', function(){ window.location.href = 'blog-editor.html'; })
        );

        /* Tạo Avatar tròn + Dropdown menu cá nhân */
        var $wrap = $('<div style="position:relative;"></div>');
        var $av   = $('<div class="avatar">').text(initials(displayName)).attr('title', displayName);
        var $dd   = $('<div class="user-dd">');

        $dd.append(
            $('<div class="dd-head">').html(
                '<div class="dn">' + displayName + '</div><div class="dr">Author</div>'
            )
        );

        $dd.append('<div class="dd-sep"></div>');

        // Nút Đăng xuất (Log Out)
        $dd.append(
            $('<button class="dd-btn red">').html(
                '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 21H5a2 2 0 01-2-2V5a2 2 0 012-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/></svg>Log Out'
            ).on('click', handleLogout)
        );

        // Bật/tắt mở Dropdown khi click vào Avatar
        $av.on('click', function(e){
            e.stopPropagation();
            $('.user-dd').not($dd).removeClass('open');
            $dd.toggleClass('open');
        });

        $wrap.append($av, $dd);
        $d.append($wrap);

    } else {
        /* ─────────────── TRẠNG THÁI: CHƯA ĐĂNG NHẬP ─────────────── */
        // Hiện 2 nút: Đăng nhập (Log In) và Đăng ký (Sign Up)
        $d.append(
            $('<button class="btn-login">').text('Log In').on('click', function(){
                window.location.href = 'login.html';
            })
        );
        $d.append(
            $('<button class="btn-register">').text('Sign Up').on('click', function(){
                window.location.href = 'register.html';
            })
        );
    }
}
```

### 1.1. Giải thuật tạo chữ ký viết tắt Avatar: `initials(name)`
```javascript
function initials(name) {
    if (!name || name === 'Guest') return "?";

    name = name.trim();
    var parts = name.split(' ');

    if (parts.length >= 2) {
        // Có từ 2 từ trở lên: Lấy chữ cái đầu của từ đầu + từ cuối
        // Ví dụ: "Hoàng Đại Dương" -> "HD", "Lê Thành Long" -> "LL"
        return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
    } else {
        // Chỉ có 1 từ: Lấy 2 chữ cái đầu (Ví dụ: "admin" -> "AD", "duong" -> "DU")
        return name.slice(0, 2).toUpperCase();
    }
}
```
- **Ý nghĩa thẩm mỹ**: Giúp giao diện luôn có avatar tròn đầy màu sắc và chuyên nghiệp ngay cả khi người dùng chưa kịp upload ảnh đại diện lên Cloudinary.

### 1.2. Hàm Đăng xuất: `handleLogout()`
```javascript
function handleLogout() {
    localStorage.removeItem('token');
    localStorage.removeItem('username');
    localStorage.removeItem('avatarUrl');

    if(typeof toast === 'function') toast('Đã đăng xuất thành công.');

    setTimeout(() => {
        window.location.href = 'home-page.html';
    }, 500);
}
```
- Xóa sạch mọi dấu vết của token và danh tính trong `localStorage`, ngăn chặn người dùng sau sử dụng lại máy tính có thể gọi API với tư cách của tài khoản cũ.

---

## 2. MÃ NGUỒN VÀ GIẢI THÍCH CHI TIẾT `init.js`

File nằm tại: `src/main/resources/static/assets/js/init.js`

```javascript
/**
 * init.js
 * "Công tắc" khởi động toàn bộ trang web
 */

$(document).ready(function() {

    // 0. ĐỌC URL ĐỂ LẤY THAM SỐ (Hỗ trợ người dùng gửi link chia sẻ)
    // Ví dụ link: home-page.html?cat=lap-trinh-java-c0a8012e-...
    const urlParams = new URLSearchParams(window.location.search);
    const catSlug = urlParams.get('cat');

    if (catSlug) {
        // Cắt lấy 36 ký tự UUID cuối cùng để gán vào State toàn cục
        S.cat = extractIdFromSlug(catSlug);
    }

    // 1. Tải bộ lọc Danh mục và Thẻ Tag ở thanh ngang
    if (typeof fetchAndRenderFilters === 'function') {
        fetchAndRenderFilters();
    }

    // 2. Tải danh sách các bài viết ở khu vực chính (Feed)
    if (typeof renderPosts === 'function') {
        renderPosts();
    }

    // 3. Tải danh sách Danh mục ở cột bên phải (Sidebar)
    if (typeof renderSbCategories === 'function') {
        renderSbCategories();
    }

    // 4. Tải danh sách các bài viết Xu hướng đọc nhiều nhất (Trending Now)
    if (typeof renderSbTrending === 'function') {
        renderSbTrending();
    }
});
```

### Điểm sáng về Kiến trúc Module:
- File `init.js` hoạt động như một **Bộ điều phối (Orchestrator)**.
- Các hàm như `fetchAndRenderFilters()`, `renderPosts()`, `renderSbCategories()` nằm ở các file JS khác nhau. `init.js` dùng cấu trúc phòng thủ an toàn: `if (typeof ... === 'function')` trước khi gọi. Nhờ đó, nếu một trang con nào đó không có thanh Sidebar hoặc không có bài viết, code sẽ không bao giờ bị văng lỗi `Uncaught ReferenceError: renderPosts is not defined`!

---

## 3. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN & TRẢ LỜI ĐIỂM 10

### Câu 1: Em hãy giải thích sự kiện `$(document).ready()` trong jQuery là gì? Nếu không dùng nó mà chạy trực tiếp code JavaScript thì có thể gặp lỗi gì?
- **Trả lời**:
  > "Thưa thầy/cô:
  > - `$(document).ready()` đảm bảo đoạn mã JavaScript chỉ bắt đầu thực thi **sau khi toàn bộ cây phân cấp HTML DOM đã được trình duyệt nạp và xây dựng hoàn tất**.
  > - Nếu không dùng `ready()` mà đặt file JS ở đầu trang `<head>`, khi JavaScript thực thi lệnh `$('#auth-area').empty()`, lúc đó thẻ `<div id="auth-area">` bên dưới mã HTML còn chưa kịp sinh ra. Đối tượng jQuery sẽ trả về rỗng và toàn bộ logic vẽ giao diện đăng nhập sẽ bị vô hiệu hóa hoàn toàn."
