# GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG NAV.JS, SIDEBAR.JS, FILTERS.JS VÀ PAGES.JS

> **Mục tiêu**: Nắm chắc cơ chế điều hướng trang mượt mà (SPA Navigation), kỹ thuật mổ xẻ Token JWT ngay tại Client để kiểm tra quyền Quản trị viên (`updateNavAuth`), Cơ chế Bộ lọc kép (Combined Filters) kết hợp đồng bộ URL không tải lại trang (`window.history.pushState`), và thuật toán xếp hạng bài viết Thịnh hành (Trending Algorithm).

---

## 1. MÃ NGUỒN VÀ GIẢI THÍCH KỸ THUẬT GIẢI MÃ TOKEN TRONG `nav.js`

File nằm tại: `src/main/resources/static/assets/js/nav.js`

```javascript
/* ─────────────── MỔ TOKEN ĐỂ CHECK QUYỀN ADMIN TẠI CLIENT ─────────────── */
function updateNavAuth() {
    const isAuth = S.isAuth;
    const uname = S.uname;
    const token = localStorage.getItem('token');

    if (isAuth && token) {
        $('.nav-guest').attr('style', 'display: none !important');
        $('.nav-user').attr('style', 'display: flex !important');
        $('#nav-username, #mob-nav-username').text(uname);

        let isAdmin = false;
        try {
            // 1. Tách chuỗi JWT bằng dấu chấm để lấy phần Payload (phần thứ 2)
            const base64Url = token.split('.')[1];

            // 2. Chuyển đổi chuẩn Base64Url sang Base64 tiêu chuẩn
            const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');

            // 3. Giải mã Base64 sang chuỗi JSON (kèm hỗ trợ tiếng Việt UTF-8)
            const payload = JSON.parse(decodeURIComponent(window.atob(base64).split('').map(function(c) {
                return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
            }).join('')));

            // 4. Đọc thuộc tính "scope" hoặc "roles" do Spring Boot phát hành
            const roles = payload.scope || payload.roles || "";
            if (roles.includes("ADMIN")) {
                isAdmin = true;
            }
        } catch (e) {
            console.error("Lỗi giải mã token:", e);
        }

        // 5. Hiển thị nút Dashboard Quản trị nếu là ADMIN
        if (isAdmin) {
            $('#btn-desk-admin').show();
            $('#btn-mob-admin').attr('style', 'display: flex !important; color: #ac8aff; font-weight: 600;');
            $('.d-role').text('Admin').css('color', '#ac8aff');
        } else {
            $('#btn-desk-admin').hide();
            $('#btn-mob-admin').attr('style', 'display: none !important;');
            $('.d-role').text('Author').css('color', 'var(--t2)');
        }
    }
}
```

### Điểm sáng kỹ thuật hàng đầu:
- **Giải mã JWT không cần cài thư viện ngoài**: Thông thường lập trình viên phải tải thêm các thư viện nặng nề như `jwt-decode.js`. Nhóm đã áp dụng phương pháp giải mã thuần túy bằng hàm tích hợp sẵn của trình duyệt `window.atob()` kết hợp biến đổi URI component.
- **Bảo mật hai lớp**: Giao diện chỉ ẩn/hiện nút bấm Admin để phục vụ trải nghiệm người dùng (UX). Nếu một user cố tình bấm vào đường link Admin hoặc gọi API Admin, tầng `SecurityConfig` của Backend vẫn sẽ kiểm tra chữ ký số của Token và chặn đứng bằng lỗi `403 Forbidden`.

---

## 2. CƠ CHẾ LỌC KÉP VÀ ĐỒNG BỘ URL TRONG `filters.js`

File nằm tại: `src/main/resources/static/assets/js/filters.js`

```javascript
/* ─────────────── ĐỒNG BỘ URL BẰNG PUSHSTATE ─────────────── */
function updateUrlWithFilters() {
    let newUrl = '/';
    let params = new URLSearchParams();

    if (S.keyword) params.append('q', S.keyword);
    if (S.cat) params.append('cat', S.cat);
    if (S.tag) params.append('tag', S.tag);

    if (params.toString() !== '') {
        newUrl += '?' + params.toString();
    }
    // Cập nhật thanh địa chỉ của trình duyệt mà KHÔNG tải lại (reload) trang
    window.history.pushState({}, '', newUrl);
}
```

### Sức mạnh của `window.history.pushState()`:
- Khi người dùng đang tìm kiếm từ khóa `"Spring Boot"` và click chọn thêm danh mục `"Lập trình"`.
- URL trên thanh trình duyệt tự động biến đổi thành: `/?q=Spring+Boot&cat=c0a8012e-...`.
- Trang web **không hề bị chớp hay F5 lại**. Toàn bộ dữ liệu mới được tải ngầm qua AJAX và render mượt mà.
- Độc giả có thể copy nguyên đường link này gửi cho bạn bè hoặc lưu vào Bookmark trình duyệt, khi người khác mở link ra, hàm `init.js` sẽ tự đọc các tham số này và lọc đúng nội dung bài viết đó!

---

## 3. THUẬT TOÁN XẾP HẠNG THỊNH HÀNH TRONG `sidebar.js`

File nằm tại: `src/main/resources/static/assets/js/sidebar.js`

```javascript
    callApi('/blogs', 'GET').done(function(res) {
        $el.empty();
        var allPosts = res.result || res;

        // THUẬT TOÁN TRENDING: Sắp xếp theo Lượt đọc (totalReads) giảm dần
        var trendingPosts = allPosts.sort(function(a, b) {
            return (b.totalReads || 0) - (a.totalReads || 0);
        }).slice(0, 5); // Chỉ lấy Top 5 bài đọc nhiều nhất

        $.each(trendingPosts, function(i, p){
            $el.append(
                $('<div class="tr-item">').html(
                    '<div class="tr-n">0' + (i+1) + '</div>' +
                    '<div>' +
                        '<div class="tr-ttl">' + p.title + '</div>' +
                        '<div class="tr-meta">' + p.category.name + '</div>' +
                    '</div>'
                )
            );
        });
    });
```
- Sử dụng hàm sắp xếp JavaScript `Array.prototype.sort()` để so sánh thuộc tính `totalReads`.
- Đánh số thứ tự tăng dần đẹp mắt: `01, 02, 03, 04, 05` trên thanh Sidebar.

---

## 4. MÃ NGUỒN VÀ BẢNG MÀU XOAY VÒNG TRONG `pages.js`

File nằm tại: `src/main/resources/static/assets/js/pages.js`

```javascript
var CAT_COLORS_ARRAY = [
    { bg:'rgba(124,111,247,.1)', bd:'rgba(124,111,247,.25)', fg:'var(--purple)' },
    { bg:'rgba(62,207,176,.08)', bd:'rgba(62,207,176,.25)',  fg:'var(--teal)'   },
    { bg:'rgba(233,168,76,.08)', bd:'rgba(233,168,76,.25)', fg:'var(--gold)'   },
    { bg:'rgba(251,191,36,.08)', bd:'rgba(251,191,36,.2)',  fg:'#fbbf24'       },
    { bg:'rgba(248,113,113,.08)',bd:'rgba(248,113,113,.2)', fg:'#f87171'       }
];

function buildCatPage() {
    callApi('/categories', 'GET').done(function(res) {
        $.each(res.result, function(index, c){
            // PHÉP CHIA LẤY DƯ (%) ĐỂ XOAY VÒNG MÀU SẮC
            var col = CAT_COLORS_ARRAY[index % CAT_COLORS_ARRAY.length];
            // Render thẻ danh mục với màu sắc rực rỡ tương ứng
        });
    });
}
```
- Toán tử `index % CAT_COLORS_ARRAY.length` đảm bảo dù Admin có tạo thêm 10 hay 100 danh mục mới trong CSDL, hệ thống vẫn tự động gán các bộ màu sắc hài hòa xoay vòng, tạo nên giao diện thẻ cực kỳ bắt mắt và sống động.

---

## 5. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN & TRẢ LỜI ĐIỂM 10

### Câu 1: Em hãy giải thích tại sao khi giải mã Token ở Frontend để hiện nút Admin, nếu một người dùng sửa chuỗi token đó trong `localStorage` thì có hack vào hệ thống được không?
- **Trả lời**:
  > "Thưa thầy/cô, hoàn toàn KHÔNG THỂ hack được!
  > - Việc giải mã token ở file `nav.js` chỉ có mục đích duy nhất là phục vụ hiển thị giao diện (User Interface). Nếu một kẻ gian cố tình sửa `payload` trong `localStorage` thành `ADMIN`, giao diện của hắn có thể hiện ra nút bấm 'Admin Dashboard'.
  > - Tuy nhiên, khi hắn bấm vào nút đó và gửi request đến các API quản trị `/api/admin/**` hoặc `/categories`, gói tin HTTP bắt buộc phải đi qua máy chủ Spring Boot.
  > - Tại file `SecurityConfig.java`, bộ giải mã `jwtDecoder()` của máy chủ sẽ dùng chữ ký số `SIGNER_KEY` bí mật để kiểm tra lại toàn bộ Token. Vì kẻ gian không có khóa bí mật nên chữ ký bị sai lệch, Spring Security sẽ ngay lập tức chặn đứng với mã lỗi **401 Unauthorized / 403 Forbidden**. 
  > Bảo mật thực sự luôn nằm ở tầng Backend, Frontend chỉ làm nhiệm vụ hiển thị!"
