# KIẾN TRÚC GIAO DIỆN CSS, DESIGN TOKENS & RESPONSIVE (MAIN.CSS)

> **Vị trí file mã nguồn:** `src/main/resources/static/assets/css/main.css`  
> **Quy mô file:** 797 dòng CSS thuần (Vanilla CSS) kết hợp linh hoạt cùng Bootstrap 5 Grid.  
> **Mục đích:** Xây dựng hệ thống ngôn ngữ thiết kế (Design System) đồng nhất, mang phong cách **Dark Theme** hiện đại, huyền bí, sang trọng với các hiệu ứng kính mờ (Glassmorphism), chuyển động vi mô (Micro-interactions) và tối ưu hiển thị mượt mà trên mọi kích thước màn hình (Responsive Design).

---

## 1. Hệ Thống Biến Thiết Kế (Design Tokens in `:root`)

Thay vì viết cứng mã màu hex ở khắp các thẻ, toàn bộ màu sắc, bán kính bo góc và độ bóng đều được quản lý tập trung ở đầu file `main.css`:

```css
:root {
    /* Bảng màu nền (Background Palette) */
    --bg:          #07080f; /* Đen vũ trụ sâu thẳm - Màu nền chính của trang */
    --bg-s:        #0c0e18; /* Màu nền thứ cấp cho các phần phân tách */
    --bg-card:     #10131f; /* Màu nền của thẻ bài viết (Card) */
    --bg-card-h:   #161929; /* Màu nền khi rê chuột vào Card (Hover State) */
    --bg-hi:       #1b1f30; /* Màu nền nổi bật cho các ô nhập liệu, thanh tìm kiếm */

    /* Màu chủ đạo thương hiệu (Brand Accent Colors) */
    --purple:      #7c6ff7; /* Tím Electric Lavender - Nhận diện thương hiệu */
    --purple-lt:   #9f7aea; /* Tím sáng dùng cho tiêu đề phụ */
    --purple-glow: rgba(124,111,247,.22); /* Hào quang tím phát sáng */
    --gold:        #e9a84c; /* Vàng kim loại cho các huy hiệu đặc biệt */
    --teal:        #3ecfb0; /* Xanh ngọc bích cho các chỉ số tích cực */
    --teal-bg:     rgba(62,207,176,.09);

    /* Hệ thống chữ và độ tương phản (Typography Contrast) */
    --t1:          #edf0f7; /* Chữ chính: Trắng ngà có độ tương phản cao, êm dịu mắt */
    --t2:          #8b91a7; /* Chữ phụ: Xám tro cho mô tả, tên tác giả, ngày tháng */
    --t3:          #525870; /* Chữ mờ: Dành cho chú thích nhỏ, placeholder */

    /* Đường viền và bo góc (Borders & Radii) */
    --bd:          rgba(255,255,255,.055); /* Viền kính siêu mỏng */
    --bd-p:        rgba(124,111,247,.35);   /* Viền sáng tím khi active */
    --r:           14px;                   /* Bo góc tiêu chuẩn cho Card */
    --r-s:         8px;                    /* Bo góc nhỏ cho nút bấm, badge */
    --red:         #ef4444;                /* Màu đỏ cảnh báo, hủy, xóa */
}
```

* **Lợi ích khi bảo vệ đồ án**: Khi giảng viên yêu cầu: *"Em hãy đổi màu chủ đạo của website từ tím sang xanh lá cây"*, sinh viên chỉ cần đổi đúng 1 dòng: `--purple: #10b981;` là toàn bộ nút bấm, hiệu ứng hover, viền phát sáng trên khắp website sẽ đổi màu đồng bộ ngay lập tức!

---

## 2. Bóc Tách Các Thành Phần Giao Diện Độc Đáo

### 2.1. Thanh Điều Hướng Kính Mờ (Glassmorphism Sticky Navbar)

```css
#navbar {
    background: rgba(7,8,15,.9);       /* Màu nền trong suốt 90% */
    backdrop-filter: blur(22px);       /* Hiệu ứng làm mờ nội dung bên dưới khi cuộn trang */
    border-bottom: 1px solid var(--bd);/* Viền đáy siêu mỏng tạo chiều sâu */
    position: sticky;
    top: 0;
    z-index: 1040;
    padding: 0.5rem 0;
}
```

* **`backdrop-filter: blur(22px)`**: Kỹ thuật tạo hiệu ứng **Frosted Glass (Kính đóng băng)** cao cấp giống như iOS và macOS. Khi người dùng cuộn trang, chữ và hình ảnh trôi phía dưới thanh menu sẽ bị làm mờ huyền ảo.

---

### 2.2. Thanh Tìm Kiếm Co Giãn Thông Minh (Expanding Search Box)

```css
.nav-search-box {
    background-color: var(--bg-hi);
    border-radius: 24px;
    padding: 9px 18px;
    display: flex;
    align-items: center;
    width: 280px; /* Chiều rộng mặc định */
    transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s;
    border: 1px solid transparent;
}

/* Khi người dùng click chuột vào ô tìm kiếm (focus-within) */
.nav-search-box:focus-within {
    width: 380px; /* Tự động giãn dài thêm 100px */
    background-color: var(--bg-card-h);
    border-color: var(--purple-lt);
    box-shadow: 0 0 15px var(--purple-glow);
}
```

* **Hiệu ứng Micro-interaction**: Tạo cảm giác mượt mà và tập trung khi tìm kiếm. Sử dụng hàm gia tốc `cubic-bezier` để chuyển động không bị cứng nhắc.

---

### 2.3. Thẻ Bài Viết Sang Trọng (Post Card & Hover Elevation)

```css
.post-card {
    background: var(--bg-card);
    border: 1px solid var(--bd);
    border-radius: var(--r);
    padding: 1.5rem;
    transition: transform 0.25s ease, background 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    cursor: pointer;
    position: relative;
    overflow: hidden;
}

.post-card:hover {
    background: var(--bg-card-h);
    border-color: var(--bd-p);
    transform: translateY(-4px); /* Nhấc bổng thẻ lên 4px */
    box-shadow: 0 12px 30px rgba(0,0,0,0.4), 0 0 20px var(--purple-glow);
}
```

* **`transform: translateY(-4px)` kết hợp `box-shadow`**: Tạo hiệu ứng chiều sâu 3D (Z-index elevation), báo hiệu cho người dùng biết đây là thành phần có thể click tương tác.

---

### 2.4. Hệ Thống Thông Báo Nhỏ (Toast Notification & Keyframes)

```css
#toasts {
    position: fixed;
    bottom: 24px;
    right: 24px;
    z-index: 9999;
    display: flex;
    flex-direction: column;
    gap: 10px;
    pointer-events: none;
}

.toast-item {
    background: #1c2128;
    color: var(--t1);
    border: 1px solid var(--bd-p);
    border-radius: 99px;
    padding: 10px 20px;
    font-size: 0.85rem;
    font-weight: 500;
    box-shadow: 0 8px 24px rgba(0,0,0,0.5);
    display: flex;
    align-items: center;
    gap: 8px;
    animation: toastIn 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes toastIn {
    from { opacity: 0; transform: translateY(15px) scale(0.95); }
    to   { opacity: 1; transform: translateY(0) scale(1); }
}
```

* **`animation: toastIn`**: Khi có sự kiện (Like, Bookmark, Đăng nhập), thông báo trồi nhẹ từ dưới lên và phóng to êm ái, sau đó tự biến mất sau 2.8 giây.

---

## 3. Thiết Kế Thích Ứng Trên Đa Thiết Bị (Responsive Breakpoints)

Website kết hợp linh hoạt hệ thống lưới 12 cột của Bootstrap 5 và các truy vấn `media query` tùy biến trong `main.css`:

```css
/* 1. Màn hình Tablet và Mobile (Dưới 992px) */
@media (max-width: 991px) {
    #navbar .nav-search-box {
        width: 200px; /* Thu gọn thanh tìm kiếm */
    }
    .post-card {
        padding: 1.2rem;
    }
    /* Ẩn bớt các cột phụ, chuyển layout từ 2 cột sang 1 cột xếp chồng */
}

/* 2. Màn hình điện thoại nhỏ (Dưới 768px) */
@media (max-width: 767px) {
    .article-title {
        font-size: 2rem !important; /* Giảm cỡ chữ tiêu đề bài viết để không bị vỡ dòng */
    }
    .nav-search-box {
        display: none !important;   /* Ẩn search box trên menu, chuyển vào icon tìm kiếm */
    }
    .action-bar {
        padding: 0.5rem 0;
    }
}
```

---

## 4. Câu Hỏi Vấn Đáp Giảng Viên Hay Hỏi Về CSS

### ❓ Câu 1: Tại sao nhóm lại chọn xây dựng giao diện Dark Mode (Nền tối) làm mặc định?
> **Trả lời:** Dạ thưa thầy/cô, Dark Mode giúp giảm độ mỏi mắt cho người đọc bài viết dài vào ban đêm, tiết kiệm pin cho màn hình OLED/AMOLED trên thiết bị di động, đồng thời tạo nên tính thẩm mỹ cao cấp, chuyên nghiệp cho một nền tảng viết blog công nghệ.

### ❓ Câu 2: Biến CSS (CSS Variables) trong `:root` mang lại lợi ích gì cho dự án?
> **Trả lời:** Dạ thưa thầy/cô, biến CSS giúp:
> 1. **Dễ bảo trì**: Thay đổi màu sắc chủ đạo của toàn bộ website chỉ trong 1 dòng code duy nhất.
> 2. **Đồng nhất thiết kế**: Tránh tình trạng mỗi trang dùng một mã màu khác nhau làm vỡ giao diện.
> 3. **Tương thích cao**: Hoạt động trực tiếp trên trình duyệt mà không cần cài đặt các công cụ tiền xử lý như SASS/SCSS.

### ❓ Câu 3: Kỹ thuật nào giúp các Card bài viết trông nổi bật và cuốn hút khi rê chuột vào?
> **Trả lời:** Nhóm kết hợp đồng thời 3 thuộc tính:
> 1. `transform: translateY(-4px)`: Nâng vị trí thẻ lên cao.
> 2. `box-shadow`: Tăng độ sâu của bóng đổ đen và bổ sung vầng hào quang tím `--purple-glow`.
> 3. `border-color: var(--bd-p)`: Làm sáng đường viền kính của thẻ.  
> Cả 3 thuộc tính này được đồng bộ chuyển động bằng `transition: all 0.25s ease`.
