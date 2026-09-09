# TỔNG QUAN KIẾN TRÚC FRONTEND, TRẠM TRUNG CHUYỂN API VÀ LƯU TRỮ TOKEN

> **Mục tiêu**: Hiểu rõ kiến trúc giao diện người dùng (Frontend Architecture), cách trình duyệt kết nối với Spring Boot REST API, cơ chế lưu trữ JWT Token trong `localStorage` và hàm trung tâm `callApi()` trong `app.js` tự động đính kèm tiêu đề xác thực `Authorization: Bearer`.

---

## 1. TỔNG QUAN KIẾN TRÚC FRONTEND

Dự án **Blog Website (Bleb Blog)** áp dụng mô hình kiến trúc **Frontend tách biệt nhẹ (Lightweight SPA / Decoupled Client)**:
- **Khung giao diện (Layout)**: Sử dụng **Thymeleaf Template Engine** để cấu trúc các trang HTML chuẩn SEO và nạp các đoạn giao diện dùng chung (Navbar, Sidebar, Footer) thông qua `th:replace="fragments/..."`.
- **Thư viện giao diện CSS**: Sử dụng **Bootstrap 5.3** kết hợp cùng hệ thống biến CSS hiện đại (Dark Theme Sleek Mode, Glassmorphism, Font chữ Google Fonts *Inter* và *Newsreader*).
- **Tầng xử lý dữ liệu (Client Logic)**: Sử dụng **Vanilla JavaScript (ES6)** kết hợp cùng **jQuery** để thao tác DOM, bắt sự kiện người dùng và thực hiện các cuộc gọi API bất đồng bộ (AJAX/Fetch) đến máy chủ Spring Boot.

---

## 2. MÃ NGUỒN TRỌNG TÂM CỦA `app.js`

File nằm tại: `src/main/resources/static/assets/js/app.js`

```javascript
/* ─────────────── STATE TOÀN CỤC (GLOBAL STATE) ─────────────── */
var S = {
    page:    'home',
    cat:     null,           // ID danh mục đang chọn
    tag:     null,           // ID tag đang chọn
    keyword: null,           // Từ khóa tìm kiếm
    sort:    'createdAt,desc',

    // Getter kiểm tra trạng thái đăng nhập
    get isAuth() { return localStorage.getItem('token') !== null; },
    get uname()  { return localStorage.getItem('username') || 'Guest'; }
};

/* ─────────────── TRẠM TRUNG CHUYỂN API (API GATEWAY CLIENT) ─────────────── */
const API_BASE_URL = (window.location.port === '8080' || window.location.host === 'localhost:8080') ? '' : 'http://localhost:8080';

function callApi(endpoint, method, data = null) {
    var token = localStorage.getItem('token');

    var ajaxConfig = {
        url: API_BASE_URL + endpoint,
        type: method,
        contentType: 'application/json',
        beforeSend: function(xhr) {
            // TỰ ĐỘNG GẮN TOKEN NẾU ĐÃ ĐĂNG NHẬP
            if (token) {
                xhr.setRequestHeader('Authorization', 'Bearer ' + token);
            }
        }
    };

    if (data) {
        ajaxConfig.data = JSON.stringify(data);
    }

    return $.ajax(ajaxConfig).fail(function(xhr) {
        console.error("API Error: ", xhr.responseText);
        if (xhr.status === 401 || xhr.status === 403) {
            toast("Phiên đăng nhập hết hạn hoặc không có quyền!");
        }
    });
}

/* ─────────────── HÀM BÓC TÁCH UUID TỪ SLUG ─────────────── */
function extractIdFromSlug(slug) {
    if (!slug) return null;
    // UUID luôn có độ dài cố định 36 ký tự: Lấy 36 ký tự cuối cùng
    return slug.slice(-36);
}

/* ─────────────── HÀM HIỂN THỊ TOAST THÔNG BÁO ─────────────── */
function toast(msg) {
    var $el = $('<div class="toast-item"><span class="toast-dot"></span><span>' + msg + '</span></div>');
    $('#toasts').append($el);
    setTimeout(function(){
        $el.fadeOut(300, function(){ $el.remove(); });
    }, 2800);
}
```

---

## 3. GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE VÀ CƠ CHẾ KỸ THUẬT

### 3.1. Đối tượng State toàn cục `S`
```javascript
var S = {
    page: 'home',
    cat: null,
    tag: null,
    keyword: null,
    get isAuth() { return localStorage.getItem('token') !== null; },
    get uname()  { return localStorage.getItem('username') || 'Guest'; }
};
```
- **Tại sao dùng Getter (`get isAuth`)?**:
  - Khi người dùng vừa bấm "Đăng nhập" hoặc "Đăng xuất", `localStorage` sẽ thay đổi.
  - Nhờ từ khóa `get`, mỗi khi bất kỳ file JS nào gọi `if (S.isAuth)`, JavaScript sẽ lập tức đọc lại giá trị mới nhất trong `localStorage` mà không sợ bị giữ giá trị cũ (Stale State).

---

### 3.2. Trạm trung chuyển API `callApi()`
- **Bài toán đặt ra**: Nếu ở mỗi trang, mỗi nút bấm chúng ta đều tự viết lệnh `fetch()` hoặc `$.ajax()` và tự tay gõ `headers: { Authorization: ... }`, code sẽ bị lặp lại hàng trăm lần. Khi muốn đổi cổng mạng hoặc sửa logic token, ta sẽ phải sửa ở hàng chục file.
- **Giải pháp của hàm `callApi()`**:
  1. **Tự động thích ứng domain (`API_BASE_URL`)**: Nếu đang chạy ở `localhost:8080`, URL gốc là rỗng `''` (tương đối). Nếu chạy ở cổng khác, tự ghép tiền tố `http://localhost:8080`.
  2. **Tự động bơm Bearer Token (`beforeSend`)**: Trước khi gói tin HTTP bay ra khỏi trình duyệt, hàm `beforeSend` kiểm tra xem trong máy có `token` không. Nếu có, nó tự động chèn thêm tiêu đề:
     ```http
     Authorization: Bearer eyJhbGciOiJIUzUxMiJ9...
     ```
  3. **Tự động bắt lỗi quyền hạn (`fail`)**: Nếu Backend trả về mã lỗi `401 Unauthorized` (hết hạn token) hoặc `403 Forbidden` (không đủ quyền Admin), hàm sẽ tự động gọi `toast("Phiên đăng nhập hết hạn hoặc không có quyền!")` để nhắc nhở người dùng.

---

### 3.3. Hàm bóc tách UUID từ Slug: `extractIdFromSlug(slug)`
```javascript
function extractIdFromSlug(slug) {
    if (!slug) return null;
    return slug.slice(-36);
}
```
- **Ý nghĩa tuyệt vời**:
  - Trên thanh địa chỉ URL, người dùng nhìn thấy đường dẫn rất đẹp:
    `post.html?id=kham-pha-kien-truc-spring-boot-3-c0a8012e-8e2b-1a34-818e-2b1a34000000`
  - Vì chuẩn chuỗi **UUID phiên bản 4** luôn luôn có độ dài cố định chính xác là **36 ký tự** (gồm 32 ký tự hex và 4 dấu gạch ngang: `8-4-4-4-12`), nên lệnh `slug.slice(-36)` sẽ cắt đúng 36 ký tự cuối cùng:
    `c0a8012e-8e2b-1a34-818e-2b1a34000000`
  - Chuỗi UUID này được truyền thẳng vào API `GET /blogs/{id}` để Backend tìm kiếm bài viết tức thì theo Khóa chính!

---

## 4. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN VỀ FRONTEND VÀ TRẢ LỜI ĐIỂM 10

### Câu 1: Em hãy giải thích ưu điểm và nhược điểm của việc lưu trữ JWT Token trong `localStorage` so với `HttpOnly Cookie`?
- **Trả lời**:
  > "Thưa thầy/cô:
  > - **Ưu điểm khi lưu ở `localStorage` (cách nhóm đang dùng)**:
  >   1. Rất đơn giản, linh hoạt, JavaScript hoàn toàn kiểm soát được việc đọc token để giải mã lấy thông tin user/roles mà không cần gọi API phụ trợ.
  >   2. Hoàn toàn miễn nhiễm với tấn công CSRF (Cross-Site Request Forgery) vì trình duyệt không tự động gửi `localStorage` kèm theo request.
  >   3. Rất thuận tiện khi phát triển ứng dụng di động (Mobile App) hoặc ứng dụng đa nền tảng sau này.
  > - **Nhược điểm**: Nếu trang web bị dính lỗ hổng XSS (Cross-Site Scripting - mã độc nhúng vào trang), hacker có thể dùng JavaScript để đọc trộm token. Để phòng chống, nhóm em đã xử lý mã hóa dữ liệu HTML và lọc nội dung đầu vào rất cẩn thận bằng hàm `extractText()`."

### Câu 2: Khi người dùng bấm F5 (Refresh) lại trang web, trạng thái đăng nhập có bị mất không? Nhờ đâu mà giữ lại được?
- **Trả lời**:
  > "Thưa thầy/cô, trạng thái đăng nhập **hoàn toàn không bị mất**:
  > Vì khi đăng nhập thành công, chuỗi JWT Token và Username đã được lưu vào bộ nhớ bền vững `localStorage` của trình duyệt. 
  > Khi người dùng bấm F5, sự kiện `$(document).ready()` trong file `init.js` và `auth.js` sẽ chạy đầu tiên. Hàm `updateNavAuth()` sẽ đọc lại token từ `localStorage`, giải mã quyền hạn và tự động vẽ lại giao diện ở trạng thái Đã đăng nhập (hiển thị avatar, tên người dùng, nút Quản trị) một cách mượt mà."
