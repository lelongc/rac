# CHI TIẾT TRÌNH SOẠN THẢO BÀI VIẾT DẠNG KHỐI (BLOG-EDITOR.HTML)

> **Vị trí file mã nguồn:** `src/main/resources/templates/public/blog-editor.html` (và bản tĩnh tại `src/main/resources/static/pages/blog-editor.html`)  
> **Quy mô file:** 1,319 dòng code tích hợp HTML5, CSS Tailwind, Vanilla JS & jQuery.  
> **Mục đích:** Cung cấp trải nghiệm soạn thảo bài viết dạng khối (Block-based Editor) hiện đại tương tự **Notion** hoặc **Medium**, hỗ trợ menu gõ tắt dấu xuyệt (`/`), kéo thả khối, tải ảnh trực tiếp lên Cloudinary, chuyển đổi chế độ Xem trước (Preview) và Lưu bản nháp (Draft).

---

## 1. Kiến Trúc Hoạt Động Của Trình Soạn Thảo Khối (Notion-like Architecture)

Thay vì dùng một thẻ `<textarea>` truyền thống hay thư viện CKEditor nặng nề, nhóm đã tự xây dựng một trình soạn thảo khối trực tiếp trong DOM:
1. Mỗi đoạn nội dung là một thẻ `div.block-row` riêng biệt có thuộc tính `contenteditable="true"`.
2. Mỗi khối đều có một thuộc tính dữ liệu `data-type`:
   - `p`: Đoạn văn bản bình thường (Paragraph).
   - `h1`, `h2`, `h3`: Các cấp độ tiêu đề lớn/vừa/nhỏ (Font chữ cổ điển sang trọng Newsreader).
   - `quote`: Khối trích dẫn có thanh viền màu tím.
   - `code`: Khối mã nguồn máy tính font `JetBrains Mono`.
   - `bullet`: Danh sách gạch đầu dòng (`•`).
   - `numbered`: Danh sách có thứ tự số (`1.`, `2.`).
   - `todo`: Danh sách công việc có hộp kiểm (Checkbox).
   - `image`: Khối hình ảnh tải lên từ máy hoặc paste URL.
3. Khi lưu bài viết, hàm `serializeContent()` duyệt qua tất cả các khối và đóng gói thành một đối tượng JSON chuẩn tương thích với Editor.js để lưu vào database:
   ```json
   {
     "time": 1715000000000,
     "blocks": [
       { "type": "paragraph", "data": { "text": "Hôm nay tôi chia sẻ..." } },
       { "type": "h1", "data": { "text": "Kiến Trúc Microservices" } }
     ],
     "version": "2.28.0"
   }
   ```

---

## 2. Bóc Tách Chi Tiết Từng Khối Logic Trong blog-editor.html

### 2.1. Cấu Trúc Khối Giao Diện HTML & Gutter Kéo Thả (Drag Handle)

```html
<div class="block-row" data-type="p">
    <div class="block-gutter">
        <button class="gutter-btn drag-handle" title="Drag to move">
            <span class="material-symbols-outlined">drag_indicator</span>
        </button>
        <button class="gutter-btn add-btn" title="Click to add a block below">
            <span class="material-symbols-outlined">add</span>
        </button>
    </div>
    <div class="block-content" contenteditable="true" data-placeholder="Gõ '/' để mở lệnh..."></div>
</div>
```

* **`div.block-gutter`**: Vùng điều khiển nằm ẩn bên lề trái của mỗi dòng (`left: -56px; opacity: 0;`). Khi người dùng di chuột (`hover`) vào dòng đó, thanh gutter sẽ hiện lên mượt mà (`opacity: 1;`).
* **`drag_indicator`**: Biểu tượng 6 dấu chấm (chuẩn Notion), cho phép tác giả click giữ chuột để kéo thả (drag & drop) hoán đổi vị trí giữa các đoạn văn.
* **`add-btn`**: Bấm vào để chèn ngay một khối trống mới ngay bên dưới.
* **`contenteditable="true"`**: Thuộc tính của trình duyệt cho phép người dùng gõ phím, bôi đen, sao chép văn bản tự nhiên như trong Word.

---

### 2.2. Menu Lệnh Xuyệt (Slash Menu `/`)

Khi người dùng nhấn phím `/` ở đầu dòng, hệ thống lắng nghe sự kiện `keyup` và hiển thị popover menu tại đúng tọa độ con trỏ:

```javascript
// Bắt sự kiện người dùng gõ dấu '/'
if (e.key === '/') {
    const selection = window.getSelection();
    if (selection.rangeCount > 0) {
        const range = selection.getRangeAt(0);
        const rect = range.getBoundingClientRect();
        showSlashMenu(rect.left, rect.bottom + window.scrollY);
    }
}
```

#### Xử lý chuyển đổi loại khối khi chọn menu:
```javascript
function applyBlockType(type) {
    const activeBlock = getActiveBlock();
    if (!activeBlock) return;

    activeBlock.setAttribute('data-type', type);
    
    // Nếu là khối To-do thì chèn checkbox
    if (type === 'todo') {
        activeBlock.innerHTML = `
            <div class="block-todo">
                <input type="checkbox" onchange="toggleTodo(this)">
                <span class="todo-text" contenteditable="true"></span>
            </div>`;
    }
    // Nếu là khối ảnh thì hiển thị khung tải ảnh
    else if (type === 'image') {
        renderImagePlaceholder(activeBlock);
    }
    hideSlashMenu();
}
```

* Hệ thống hỗ trợ điều hướng menu bằng cả **chuột** lẫn **phím mũi tên lên/xuống (ArrowUp, ArrowDown) + Enter** hệt như Notion thật!

---

### 2.3. Tải Ảnh Lên Cloudinary Qua API Backend

Trình soạn thảo hỗ trợ 2 khu vực ảnh:
1. **Ảnh bìa bài viết (Cover Banner)**: Thẻ `#banner-file-input`
2. **Ảnh bên trong nội dung bài (Inline Image Block)**: Khối `type="image"`

#### Code xử lý Upload qua FormData:
```javascript
function uploadImageToCloudinary(file, onSuccess, onError) {
    const formData = new FormData();
    formData.append('file', file);

    const token = localStorage.getItem('token');
    
    $.ajax({
        url: '/api/upload',
        type: 'POST',
        data: formData,
        processData: false, // Bắt buộc: Không để jQuery biến đổi FormData thành chuỗi query
        contentType: false, // Bắt buộc: Để trình duyệt tự tạo header multipart/form-data kèm boundary
        headers: token ? { 'Authorization': 'Bearer ' + token } : {},
        success: function(res) {
            if (res.result && res.result.url) {
                onSuccess(res.result.url); // Trả về link ảnh https://res.cloudinary.com/...
            } else {
                onError("Không nhận được link ảnh từ máy chủ");
            }
        },
        error: function(xhr) {
            onError(xhr.responseJSON?.message || "Tải ảnh thất bại!");
        }
    });
}
```

* **`processData: false`** và **`contentType: false`**: Hai tham số cực kỳ quan trọng của jQuery AJAX. Nếu thiếu 2 dòng này, jQuery sẽ cố chuyển nhị phân ảnh thành chuỗi URL text và làm lỗi multipart boundary!
* Ảnh sau khi tải lên thành công sẽ nhận về URL Cloudinary tối ưu hóa CDN và chèn ngay vào bài viết.

---

### 2.4. Cơ Chế Chuyển Đổi Chế Độ Soạn Thảo ⇋ Xem Trước (Preview Toggle)

Để tác giả nhìn thấy bài viết của mình trông như thế nào trước khi xuất bản, trang tích hợp SPA View Switcher:

```javascript
function showPreview() {
    // 1. Đồng bộ tiêu đề và ảnh bìa từ form soạn thảo sang view preview
    const title = $('#title-input').val() || 'Chưa đặt tiêu đề';
    $('#pv-title').text(title);
    $('#pv-form-title').val(title);

    // 2. Chuyển đổi toàn bộ các khối nội dung sang HTML
    const previewContentHtml = generatePreviewHtml();
    $('#pv-content').html(previewContentHtml);

    // 3. Đổi trạng thái hiển thị bằng CSS class
    $('body').addClass('show-preview');
    window.scrollTo(0, 0);
}

function hidePreview() {
    $('body').removeClass('show-preview');
}
```

* Giao diện chỉ cần gán class `body.show-preview`. Trong file CSS có quy tắc:
  ```css
  #view-editor { display: flex; }
  #view-preview { display: none; }
  body.show-preview #view-editor { display: none; }
  body.show-preview #view-preview { display: block; }
  ```
* Chuyển đổi giữa 2 chế độ diễn ra tức thì trong **0.01 giây** mà không tốn bất kỳ lượt tải lại trang (reload) nào!

---

### 2.5. Cơ Chế Xuất Bản & Lưu Bản Nháp (Draft vs Publish)

```javascript
function savePost(isDraft) {
    const title = $('#title-input').val().trim();
    if (!title) {
        toast("Vui lòng nhập tiêu đề bài viết!");
        return;
    }

    const payload = {
        title: title,
        content: serializeContent(), // Chuỗi JSON chứa toàn bộ blocks
        banner: $('#banner-img').attr('src') || '',
        categoryId: $('#category-select').val() || null,
        tagNames: pvTags, // Mảng tên các thẻ tag
        draft: isDraft    // true: Lưu bản nháp; false: Xuất bản công khai
    };

    const isEditMode = Boolean(editingBlogId);
    const endpoint = isEditMode ? `/blogs/${editingBlogId}` : '/blogs';
    const method = isEditMode ? 'PUT' : 'POST';

    callApi(endpoint, method, payload).done(function(res) {
        toast(isDraft ? "Đã lưu bản nháp thành công!" : "Xuất bản bài viết thành công!");
        setTimeout(() => {
            window.location.href = 'Manage-Blogs.html';
        }, 1200);
    });
}
```

* Biến boolean `draft`:
  - Khi bấm **"Save Draft"**: `savePost(true)` ➔ Bài viết được lưu vào CSDL với cờ `draft = true`. Bài này chỉ hiển thị trong trang quản lý cá nhân của tác giả, hoàn toàn ẩn với cộng đồng ngoài trang chủ.
  - Khi bấm **"Publish"**: `savePost(false)` ➔ Bài viết được công khai ngay lập tức, tự động sinh slug tiếng Việt thân thiện SEO và xuất hiện trên Newest Feed của trang chủ.

---

## 3. Câu Hỏi Vấn Đáp Giảng Viên Hay Hỏi Về blog-editor.html

### ❓ Câu 1: Tại sao nhóm lại tự code giao diện trình soạn thảo khối thay vì dùng thư viện có sẵn?
> **Trả lời:** Dạ thưa thầy/cô, việc tự xây dựng trình soạn thảo khối bằng DOM `contenteditable` và cấu trúc mảng blocks giúp nhóm làm chủ 100% dữ liệu đầu ra dạng JSON, dễ dàng tùy biến menu lệnh gõ tắt `/`, tích hợp tải ảnh trực tiếp lên Cloudinary thông qua Spring Boot API, và tối ưu hóa tốc độ tải trang nhanh gấp nhiều lần so với các thư viện WYSIWYG nặng nề.

### ❓ Câu 2: Khi upload một ảnh bìa dung lượng 5MB, luồng dữ liệu đi qua những đâu?
> **Trả lời:**
> 1. Trình duyệt đóng gói file vào đối tượng `FormData` và gửi `POST /api/upload` (dạng `multipart/form-data`).
> 2. `UploadController` trong Spring Boot tiếp nhận `MultipartFile`.
> 3. Spring Boot ủy quyền cho `CloudinaryService` đẩy luồng byte sang Cloudinary Server thông qua kết nối HTTPS bảo mật.
> 4. Cloudinary xử lý tối ưu định dạng (WebP), lưu trữ CDN và trả về link URL an toàn (`https://res.cloudinary.com/...`).
> 5. Spring Boot đóng gói URL này vào `ApiResponse<UploadResponse>` trả về cho Frontend hiển thị ảnh lên bài viết.

### ❓ Câu 3: Làm thế nào để phân biệt giữa việc "Tạo mới bài viết" và "Cập nhật bài viết đang có"?
> **Trả lời:** Khi người dùng bấm Sửa bài viết từ trang quản lý, URL sẽ có dạng `blog-editor.html?edit={id}`. JavaScript kiểm tra tham số `edit`:
> - Nếu có: Bật cờ `isEditMode = true`, gọi `GET /blogs/{id}` để nạp dữ liệu cũ vào các khối và gán method gửi đi là `PUT /blogs/{id}`.
> - Nếu không có: Mở một trang soạn thảo trống với 1 khối mặc định và method gửi đi là `POST /blogs`.
