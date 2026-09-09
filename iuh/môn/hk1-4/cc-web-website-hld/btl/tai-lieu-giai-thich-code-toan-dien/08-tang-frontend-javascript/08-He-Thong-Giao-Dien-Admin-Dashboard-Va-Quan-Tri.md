# HỆ THỐNG GIAO DIỆN QUẢN TRỊ VIÊN (ADMIN DASHBOARD & MANAGEMENT)

> **Các file mã nguồn liên quan:**  
> - `src/main/resources/templates/admin/dashboard.html`: Trang tổng quan số liệu thống kê hệ sinh thái.  
> - `src/main/resources/templates/admin/posts.html`: Quản lý toàn bộ bài viết, phân trang và kiểm duyệt nội dung.  
> - `src/main/resources/templates/admin/users.html`: Quản lý danh sách thành viên, phân quyền và khóa tài khoản.  
> - `src/main/resources/templates/admin/categories-tags.html`: Quản lý danh mục bài viết và các thẻ nhãn (Tags).  
> - `src/main/resources/templates/fragments/admin_sidebar.html`: Thanh Menu điều hướng dành riêng cho Quản trị viên.

---

## 1. Cơ Chế Bảo Vệ Và Phân Quyền Trang Quản Trị (Admin Protection Architecture)

Khu vực Admin được bảo vệ kép ở cả **Frontend** lẫn **Backend**:

```
[Trình duyệt mở /admin/dashboard.html]
       │
       ▼
Kiểm tra Client-side (JavaScript):
Có token trong localStorage không? Token có chứa vai trò "ROLE_ADMIN" không?
       ├── KHÔNG ➔ window.location.href = '../public/login.html'; (Chặn ngay tại cửa)
       └── CÓ    ➔ Gửi AJAX GET /api/admin/stats kèm Header "Authorization: Bearer <token>"
                     │
                     ▼
             Kiểm tra Server-side (Spring Security):
             @PreAuthorize("hasRole('ADMIN')")
                     ├── Không hợp lệ ➔ Trả về HTTP 403 Forbidden
                     └── Hợp lệ       ➔ Trả về JSON dữ liệu thống kê
```

---

## 2. Bóc Tách Chi Tiết Từng Giao Diện Quản Trị

### 2.1. Trang Thống Kê Tổng Quan (admin/dashboard.html)

Trang hiển thị cái nhìn toàn cảnh về tình hình hoạt động của website:
- **Thẻ KPI 1**: Tổng số người dùng đăng ký (`#total-users`).
- **Thẻ KPI 2**: Tổng số bài viết đã xuất bản (`#total-posts`).
- **Bảng bài viết gần đây (Recent Posts)**: 5 bài viết mới nhất vừa được đăng tải trên nền tảng.

```javascript
function loadDashboardData() {
    const token = localStorage.getItem('token');
    if (!token) {
        window.location.href = '../public/login.html';
        return;
    }

    $.ajax({
        url: 'http://localhost:8080/api/admin/stats',
        type: 'GET',
        headers: { 'Authorization': 'Bearer ' + token },
        success: function(response) {
            if (response.result) {
                const data = response.result;
                // Hiển thị số liệu có dấu phẩy ngăn cách hàng nghìn
                $('#total-users').text(data.totalUsers.toLocaleString());
                $('#total-posts').text(data.totalPosts.toLocaleString());

                // Đổ dữ liệu vào bảng danh sách bài viết gần đây
                const tbody = $('table tbody').empty();
                data.recentPosts.forEach(post => {
                    const date = new Date(post.createdAt).toLocaleDateString();
                    const authorName = post.author?.username || 'Ẩn danh';
                    const row = `
                        <tr class="hover:bg-slate-50 transition-colors">
                            <td class="px-6 py-5 font-medium text-slate-800">${post.title}</td>
                            <td class="px-6 py-5 font-mono text-[#ac8aff]">@${authorName}</td>
                            <td class="px-6 py-5 text-right font-mono text-xs text-slate-400">${date}</td>
                            <td class="px-6 py-5 text-right">
                                <div class="flex justify-end gap-3">
                                    <a href="../pages/post.html?id=${post.id}" target="_blank" class="text-slate-400 hover:text-[#ac8aff]">
                                        <span class="material-symbols-outlined text-[18px]">visibility</span>
                                    </a>
                                    <button onclick="deletePost('${post.id}')" class="text-slate-400 hover:text-red-400">
                                        <span class="material-symbols-outlined text-[18px]">delete</span>
                                    </button>
                                </div>
                            </td>
                        </tr>`;
                    tbody.append(row);
                });
            }
        },
        error: function(err) {
            if (err.status === 403) {
                alert("Bạn không có quyền truy cập trang quản trị!");
                window.location.href = '../public/home-page.html';
            }
        }
    });
}
```

* **Nút Xóa bài viết khẩn cấp (`deletePost`)**: Cho phép Admin xóa trực tiếp bất kỳ bài viết nào vi phạm tiêu chuẩn cộng đồng ngay từ Dashboard.

---

### 2.2. Quản Lý Bài Viết & Phân Trang (admin/posts.html)

Khi website có hàng trăm bài viết, việc tải và hiển thị tất cả cùng lúc sẽ gây giật lag giao diện. Trang `admin/posts.html` triển khai thuật toán **Phân trang mượt mà (Pagination)**:

```javascript
let allPosts = [];
let currentPage = 1;
const postsPerPage = 5; // Hiển thị 5 bài trên một trang

function renderPosts() {
    const sort = $('#sort-date').val();
    const search = $('#search-input').val().toLowerCase();

    // 1. Lọc theo từ khóa tìm kiếm trên tiêu đề
    let filtered = allPosts.filter(p => p.title.toLowerCase().includes(search));

    // 2. Sắp xếp theo ngày tạo (Mới nhất / Cũ nhất)
    filtered.sort((a, b) => {
        const dateA = new Date(a.createdAt);
        const dateB = new Date(b.createdAt);
        return sort === 'newest' ? dateB - dateA : dateA - dateB;
    });

    // 3. Cắt lát mảng dữ liệu theo trang hiện tại (Slice)
    const totalItems = filtered.length;
    const totalPages = Math.ceil(totalItems / postsPerPage) || 1;
    const startIndex = (currentPage - 1) * postsPerPage;
    const endIndex = Math.min(startIndex + postsPerPage, totalItems);
    const paginatedPosts = filtered.slice(startIndex, endIndex);

    // 4. Render danh sách và thanh chuyển số trang (1, 2, 3...)
    renderTableRows(paginatedPosts);
    renderPaginationControls(totalPages);
}
```

* **Ưu điểm**: Tốc độ chuyển trang tức thì (0ms), không cần tải lại toàn bộ trang, hỗ trợ tìm kiếm kết hợp sắp xếp real-time.

---

### 2.3. Quản Lý Thành Viên & Phân Quyền (admin/users.html)

Trang này quản lý toàn bộ thành viên trong hệ thống, cho phép xem danh sách, lọc theo tên/email, và phân vai trò `USER` hoặc `ADMIN`.

```javascript
function renderUsers(usersArray) {
    const $tbody = $('#users-tbody').empty();

    usersArray.forEach(user => {
        const isAdmin = user.roles && user.roles.includes('ADMIN');
        const roleBadge = isAdmin
            ? `<span class="px-3 py-1 text-xs font-semibold rounded-full bg-purple-100 text-purple-700 border border-purple-200">ADMIN</span>`
            : `<span class="px-3 py-1 text-xs font-semibold rounded-full bg-slate-100 text-slate-600 border border-slate-200">USER</span>`;

        $tbody.append(`
            <tr class="hover:bg-slate-50 transition-colors">
                <td class="px-6 py-4 flex items-center gap-3">
                    <img class="w-9 h-9 rounded-full object-cover border border-slate-200" src="${user.avatarUrl || 'https://placehold.co/100'}" alt="Avatar"/>
                    <div>
                        <div class="font-bold text-slate-800">${user.fullName || user.username}</div>
                        <div class="text-xs text-slate-400 font-mono">@${user.username}</div>
                    </div>
                </td>
                <td class="px-6 py-4 text-slate-600 text-sm font-mono">${user.email}</td>
                <td class="px-6 py-4">${roleBadge}</td>
                <td class="px-6 py-4 text-right">
                    <button onclick="toggleUserRole('${user.id}', ${isAdmin})" class="text-xs font-medium px-3 py-1.5 rounded-lg border border-slate-200 hover:bg-slate-100 transition-all">
                        ${isAdmin ? 'Hạ xuống USER' : 'Thăng cấp ADMIN'}
                    </button>
                </td>
            </tr>
        `);
    });
}
```

* **Bảo vệ tài khoản gốc (Root Admin)**: Không cho phép Admin tự hạ quyền chính mình, tránh trường hợp hệ thống bị mất toàn bộ tài khoản quản trị viên.

---

### 2.4. Quản Lý Danh Mục & Thẻ Nhãn (admin/categories-tags.html)

Quản lý danh mục (`Category`) và thẻ bài viết (`Tag`):
- Hiển thị từng danh mục dưới dạng ô thẻ (Card) trực quan.
- **Thống kê số lượng bài viết (`postCount`)**: Sử dụng câu truy vấn tối ưu 3NF của Backend để hiển thị chính xác có bao nhiêu bài viết đang thuộc danh mục/thẻ đó.
- Cho phép **Thêm mới**, **Đổi tên (Sửa)** hoặc **Xóa** danh mục và thẻ.

```javascript
function createCategory(e) {
    e.preventDefault();
    const name = $('#input-cat-name').val().trim();
    if (!name) return;

    $.ajax({
        url: `${API_BASE}/categories`,
        type: 'POST',
        contentType: 'application/json',
        headers: { 'Authorization': 'Bearer ' + token },
        data: JSON.stringify({ name: name }),
        success: function() {
            showToast("Tạo danh mục mới thành công!");
            $('#input-cat-name').val('');
            fetchCategories(); // Nạp lại danh sách mới
        },
        error: function(err) {
            alert(err.responseJSON?.message || "Lỗi không thể tạo danh mục!");
        }
    });
}
```

---

## 3. Câu Hỏi Vấn Đáp Giảng Viên Hay Hỏi Về Khu Vực Admin

### ❓ Câu 1: Nếu một User bình thường cố tình gõ đường dẫn `http://localhost:8080/admin/dashboard.html` trên trình duyệt thì chuyện gì xảy ra?
> **Trả lời:** Hệ thống có 2 lớp bảo vệ:
> 1. **Lớp 1 (JavaScript tại trình duyệt)**: Trang dashboard đọc token JWT trong `localStorage`. Nếu không có token hoặc token không chứa Role `ADMIN`, JavaScript lập tức chuyển hướng (`redirect`) người dùng về `home-page.html` hoặc `login.html`.
> 2. **Lớp 2 (Spring Security tại Server)**: Kể cả khi kẻ xấu tắt JavaScript để xem giao diện tĩnh, thì khi trang gửi AJAX gọi `/api/admin/stats`, Spring Security kiểm tra `SecurityFilterChain` có cấu hình `.requestMatchers("/api/admin/**").hasRole("ADMIN")`. Request sẽ bị chặn đứng với mã lỗi **HTTP 403 Forbidden**, không có bất kỳ dữ liệu nào bị rò rỉ.

### ❓ Câu 2: Khi Admin xóa một bài viết, những dữ liệu liên quan như Comment, Like, Bookmark sẽ thế nào?
> **Trả lời:** Trong các Entity `Comment`, `BlogLike`, `BlogBookmark`, nhóm đã thiết lập cấu hình:
> ```java
> @ManyToOne(fetch = FetchType.LAZY)
> @JoinColumn(name = "blog_id")
> @OnDelete(action = OnDeleteAction.CASCADE)
> private Blog blog;
> ```
> Nhờ cơ chế `CASCADE` ở tầng Database, khi bài viết bị xóa thì toàn bộ bình luận, lượt like và bookmark gắn liền với bài viết đó sẽ được CSDL tự động xóa sạch, tránh tình trạng rác dữ liệu mồ côi (orphan records).

### ❓ Câu 3: Trang quản lý bài viết của Admin có gì khác so với trang Manage-Blogs.html của Tác giả?
> **Trả lời:**
> - Trang `Manage-Blogs.html`: Dành cho từng tác giả, chỉ hiển thị và quản lý bài viết của chính tác giả đó (`findByAuthorUsername`).
> - Trang `admin/posts.html`: Dành cho Quản trị viên, có quyền xem toàn bộ bài viết của mọi thành viên trên toàn hệ thống, có quyền xóa bất kỳ bài viết nào nếu có nội dung vi phạm.
