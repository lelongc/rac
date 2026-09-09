# GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG POSTS.JS VÀ BỘ SOẠN THẢO BÀI VIẾT

> **Mục tiêu**: Hiểu rõ quy trình kết nối API để hiển thị dòng thời gian bài viết (Feed), giải thuật tính thời gian đọc bài viết (Reading Time), hàm trích xuất văn bản thuần túy (`extractText`), cách render thẻ bài viết (`buildCard`) và luồng hoạt động của trình soạn thảo bài viết (`blog-editor.html`).

---

## 1. MÃ NGUỒN VÀ GIẢI THÍCH CHI TIẾT `posts.js`

File nằm tại: `src/main/resources/static/assets/js/posts.js`

### 1.1. Giải thuật Trích xuất văn bản sạch: `extractText()`
```javascript
function extractText(content, len) {
    if (!content) return '';
    let plainText = "";

    try {
        // 1. Nếu nội dung lưu dưới dạng JSON khối của Editor.js
        const parsed = JSON.parse(content);
        if (parsed && parsed.blocks) {
            parsed.blocks.forEach(b => {
                if (b.data && b.data.text) plainText += b.data.text + " ";
            });
        } else {
            plainText = content;
        }
    } catch (e) {
        // 2. Nếu là chuỗi HTML hoặc Text thông thường
        plainText = content;
    }

    // 3. Sử dụng DOM ảo để bóc sạch tất cả các thẻ HTML (<p>, <b>, <i>...)
    var div = document.createElement("div");
    div.innerHTML = plainText;
    var text = div.textContent || div.innerText || "";
    text = text.trim();

    // 4. Cắt chuỗi theo độ dài mong muốn và thêm dấu ba chấm
    return text.length > len ? text.substring(0, len) + '...' : text;
}
```
- **Ý nghĩa kỹ thuật**: Khi hiển thị danh sách bài viết trên trang chủ, chúng ta chỉ cần một đoạn tóm tắt ngắn (Excerpt) khoảng 150 - 200 chữ. Nếu để nguyên mã HTML thô, giao diện sẽ bị vỡ khung bởi các thẻ `<div>` hay `<img>` chưa đóng. Hàm này đảm bảo nội dung tóm tắt luôn là chữ thuần túy, an toàn 100%.

---

### 1.2. Thuật toán ước tính thời gian đọc (Estimated Reading Time)
```javascript
    let plainTextContent = extractText(p.content, 99999);
    let readingTime = Math.ceil(((plainTextContent || '').split(/\s+/).length || 1) / 200);
    if (readingTime <= 0) readingTime = 1;
```
- **Chuẩn quốc tế (Medium / Dev.to standard)**: Tốc độ đọc trung bình của một người trưởng thành là **200 từ/phút**.
- Biểu thức chính quy `split(/\s+/)` tách nội dung bài viết thành mảng các từ dựa trên khoảng trắng và dấu xuống dòng.
- Lấy tổng số từ chia cho 200 và làm tròn lên bằng `Math.ceil()`. Người đọc sẽ biết bài viết này cần khoảng `3 phút` hay `5 phút` để đọc hết.

---

### 1.3. Xây dựng thẻ bài viết hoàn chỉnh: `buildCard(p)`
```javascript
function buildCard(p) {
    if (!p) return $('<div>');

    var catName = p.category ? (p.category.name || 'Chưa phân loại') : 'Chưa phân loại';
    var authorName = p.author ? (p.author.username || 'Anonymous') : 'Anonymous';
    var authorAvatar = (p.author && p.author.avatarUrl) ? p.author.avatarUrl 
        : `https://ui-avatars.com/api/?name=${encodeURIComponent(authorName)}&background=151a22&color=ac8aff`;
    
    var dateStr = fmtDate(p.createdAt);
    var postExcerpt = p.description ? p.description : extractText(p.content, 180);
    var bannerUrl = p.banner ? p.banner : 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600';

    // Xử lý các Thẻ Tag (Tối đa 3 thẻ, nếu nhiều hơn thì hiện số dư +N)
    let tagsHtml = '';
    if (p.tags && Array.isArray(p.tags) && p.tags.length > 0) {
        tagsHtml = '<div class="d-flex align-items-center flex-wrap gap-2">';
        let maxTags = 3;
        for (let i = 0; i < Math.min(p.tags.length, maxTags); i++) {
            let cleanTag = (p.tags[i].name || '').replace(/^#+/, '');
            tagsHtml += `<span class="badge border">#${cleanTag}</span>`;
        }
        if (p.tags.length > maxTags) {
            tagsHtml += `<span class="badge border text-muted">+${p.tags.length - maxTags}</span>`;
        }
        tagsHtml += '</div>';
    }

    var targetId = p.slug || p.id || '';
    var $card = $('<article class="post-card">')
        .on('click', function(){
            window.location.href = 'post.html?id=' + encodeURIComponent(targetId);
        });

    $card.html(`
        <div class="card-body">
            <div class="author-meta">
                <img src="${authorAvatar}" class="avatar-mini">
                <span class="author-name">${authorName}</span> • <span>${dateStr}</span>
            </div>
            <h2 class="post-title">${p.title}</h2>
            <p class="post-desc">${postExcerpt}</p>
            <div class="post-footer">
                ${tagsHtml}
                <div class="post-stats">
                    <span>❤️ ${p.totalLikes || 0}</span>
                    <span>👁️ ${p.totalReads || 0}</span>
                    <span>💬 ${p.totalComments || 0}</span>
                </div>
            </div>
        </div>
        <div class="card-banner">
            <img src="${bannerUrl}" alt="banner">
        </div>
    `);

    return $card;
}
```

---

## 2. QUY TRÌNH HOẠT ĐỘNG CỦA TRANG SOẠN THẢO BÀI VIẾT (`blog-editor.html`)

Quy trình người dùng tạo bài viết mới diễn ra như sau:
1. **Kiểm tra đăng nhập**: Ngay khi vào trang `blog-editor.html`, JavaScript kiểm tra `if (!S.isAuth)`, nếu chưa đăng nhập lập tức chuyển hướng về trang `login.html`.
2. **Chọn ảnh bìa (Banner)**: Người dùng chọn file ảnh từ máy tính. Sự kiện `change` trên input file tự động gửi `POST /upload/image` lên server. Server trả về đường link ảnh Cloudinary HTTPS. Giao diện hiển thị xem trước ảnh ngay lập tức.
3. **Soạn thảo nội dung**: Người dùng nhập Tiêu đề, Mô tả ngắn, chọn Danh mục từ Dropdown và gõ các Thẻ Tag (ngăn cách bằng dấu phẩy).
4. **Lựa chọn 2 chế độ Lưu**:
   - **Nút "Save Draft" (Lưu nháp)**: Gửi request `POST /blogs` với body `{ draft: true, ... }`. Bài viết được lưu vào cơ sở dữ liệu nhưng chỉ có tác giả nhìn thấy.
   - **Nút "Publish" (Xuất bản)**: Gửi request với body `{ draft: false, ... }`. Bài viết xuất hiện ngay lập tức trên bảng tin trang chủ cho mọi độc giả cùng đọc.

---

## 3. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN VỀ BÀI VIẾT & TRẢ LỜI ĐIỂM 10

### Câu 1: Tại sao trong hàm `buildCard()`, khi click vào bài viết em lại dùng `window.location.href = 'post.html?id=' + encodeURIComponent(targetId)`?
- **Trả lời**:
  > "Thưa thầy/cô:
  > - `targetId` ở đây ưu tiên lấy chuỗi **Slug chuẩn SEO** (ví dụ: `kham-pha-spring-boot-3-c0a8012e-...`).
  > - Hàm `encodeURIComponent()` có nhiệm vụ mã hóa các ký tự đặc biệt (khoảng trắng, dấu gạch chéo, ký tự Unicode) thành các mã phần trăm an toàn trên URL (URL-safe encoding). Điều này đảm bảo khi người dùng chia sẻ link lên Facebook hay Zalo, đường dẫn không bao giờ bị đứt gãy hoặc lỗi mã hóa."
