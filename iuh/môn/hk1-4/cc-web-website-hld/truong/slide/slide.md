![1786274697116](image/slide/1786274697116.png)

Eclipse J2EE   (Eclipse SE, ME)
MySQL, Workbench
Spring boot
Postman
.....
url (address bar)
href
--> MVC
JQuery
Fetch
Axiox
Ajax

truongbaphuc@iuh.edu.vn

t1

b1/ tạo 1 trang web dùng để quy đổi tiền tệ

b1.1/ true and true , true and false , true and null , true or null, false or null,

Trả lời:

- `true and true`   => **true**
- `true and false`  => **false**
- `true and null`   => **null**
- `true or null`    => **true**
- `false or null`   => **null**

b2/ Cho chứa 1 mảng danh sách các đối tượng (mỗi đối tượng là 1 sản phẩm), viết hàm JS để load danh sách này vào bảng HTML (table).

---

### 📌 Yêu cầu kiến trúc & Kỹ thuật chi tiết:

- **Phía Server**: Xây dựng **Web Service theo chuẩn RESTful API**, xử lý và trả về dữ liệu định dạng **JSON**.
- **Phía Client (Trình duyệt)**: Gửi yêu cầu (Call) tới Web Service bằng **jQuery (`$.ajax` / `$.getJSON`)** hoặc **Fetch API**.
- **Xử lý hiển thị**: Sử dụng **JavaScript DOM** để nhận chuỗi/mảng JSON và kết xuất (render) dữ liệu hiển thị lên giao diện bảng HTML (`<table>`).

TUẦN 2

b1/ tìm virtual restful api có hỗ trợ hình ảnh

b2/ dựa vào virtual restful api trên , viết app Single Page App spa quảng cáo sản phẩm , có các chức năng thêm xóa sửa, tìm kiếm ,
thử fake rest api

tuần 3

thiết kế lại giao diện dùng bootstrap kết hợp thymeleaf , thymeleaf là view engine , bootstrap là css framework

master-n-detail(tên gọi chức năng của trang) + template

thymeleaf + bootstrap

tìm hiểu cách nhúng dữ liệu vào trang , cách chia theo quy định của thymeleaf

### 📊 CÁC CÁCH TRÌNH BÀY DỮ LIỆU TRÊN GIAO DIỆN WEB (DATA PRESENTATION LAYOUTS)

---

#### 1. Dạng Bảng Dữ Liệu Chuẩn (Datasheet / Tabular Layout)

- **Đặc điểm**: Dữ liệu hiển thị dạng bảng lưới gồm các hàng (rows) và cột (columns), mỗi dòng là 1 bản ghi (record).
- **Ứng dụng**: Danh sách sản phẩm, bảng quản lý tài khoản, danh sách sinh viên.

**🖼️ Hình vẽ minh họa:**

```text
┌──────┬──────────────────────────┬────────────┬───────────┬──────────────┐
│ ID   │ Tên Sản Phẩm             │ Đơn Giá    │ Số Lượng  │ Trạng Thái   │
├──────┼──────────────────────────┼────────────┼───────────┼──────────────┤
│ SP01 │ Laptop Dell XPS 15       │ 28.000.000 │ 12        │ Còn hàng     │
│ SP02 │ Chuột Không Dây Logitech │ 1.850.000  │ 45        │ Còn hàng     │
│ SP03 │ Bàn Phím Cơ Keychron     │ 2.200.000  │ 0         │ Hết hàng     │
└──────┴──────────────────────────┴────────────┴───────────┴──────────────┘
```

- **Mã ví dụ Thymeleaf + Bootstrap**:

```html
<table class="table table-bordered table-hover shadow-sm">
    <thead class="table-dark">
        <tr>
            <th>ID</th>
            <th>Tên Sản Phẩm</th>
            <th>Đơn Giá</th>
            <th>Số Lượng</th>
            <th>Hành Động</th>
        </tr>
    </thead>
    <tbody>
        <tr th:each="p : ${products}">
            <td th:text="${p.id}">SP01</td>
            <td th:text="${p.name}">Laptop Dell</td>
            <td th:text="${#numbers.formatDecimal(p.price, 0, 'COMMA', 0, 'POINT')} + ' VNĐ'">28.000.000 VNĐ</td>
            <td>
                <span th:class="${p.quantity > 0} ? 'badge bg-success' : 'badge bg-danger'"
                      th:text="${p.quantity > 0 ? p.quantity : 'Hết hàng'}"></span>
            </td>
            <td>
                <a th:href="@{/products/edit/{id}(id=${p.id})}" class="btn btn-sm btn-primary">Sửa</a>
            </td>
        </tr>
    </tbody>
</table>
```

---

#### 2. Dạng Phân Nhóm Chính - Phụ (Master - Detail / Main - Sub Layout)

- **Đặc điểm**: Trình bày dữ liệu phân cấp quan hệ **1 - Nhiều (1-N)**. Mỗi nhóm chính (**Master/Main**) đại diện cho thực thể cha, bên dưới chứa danh sách chi tiết các thực thể con (**Detail/Sub**).
- **Ứng dụng**: Liệt kê danh sách nhân viên theo từng phòng ban, hóa đơn kèm danh sách món hàng, danh mục kèm các bài viết thuộc danh mục đó.

**🖼️ Hình vẽ minh họa:**

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🏢 PHÒNG BAN: PHÒNG KỸ THUẬT (Mã: PB01 - Trưởng phòng: Hoàng Đại Dương)    │  <-- MASTER (Main)
├──────┬────────────────────────┬─────────────────────┬───────────────────────┤
│ STT  │ Họ Và Tên Nhân Viên    │ Chức Vụ             │ Email                 │  <-- DETAIL (Sub)
├──────┼────────────────────────┼─────────────────────┼───────────────────────┤
│  1   │ Hoàng Đại Dương        │ Lead Developer      │ duong.24743991@iuh.vn │
│  2   │ Nguyễn Trung Dũng      │ Backend Developer   │ dung.24000905@iuh.vn  │
└──────┴────────────────────────┴─────────────────────┴───────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ 🏢 PHÒNG BAN: PHÒNG THIẾT KẾ & UI/UX (Mã: PB02 - Trưởng phòng: Lê Thành Long)│  <-- MASTER (Main)
├──────┬────────────────────────┬─────────────────────┬───────────────────────┤
│ STT  │ Họ Và Tên Nhân Viên    │ Chức Vụ             │ Email                 │  <-- DETAIL (Sub)
├──────┼────────────────────────┼─────────────────────┼───────────────────────┤
│  1   │ Lê Thành Long          │ UI/UX Designer      │ long.23630851@iuh.vn  │
└──────┴────────────────────────┴─────────────────────┴───────────────────────┘
```

- **Mã ví dụ Thymeleaf lồng nhau (Nested `th:each`)**:

```html
<!-- 1. Vòng lặp cấp 1: Lặp qua từng Phòng Ban (Master) -->
<div th:each="dept : ${departments}" class="card mb-4 shadow-sm border-primary">
    <div class="card-header bg-primary text-white d-flex justify-content-between align-items-center">
        <h5 class="mb-0" th:text="'🏢 Phòng Ban: ' + ${dept.name} + ' (' + ${dept.code} + ')'"></h5>
        <span class="badge bg-light text-primary" th:text="${dept.employees.size()} + ' Nhân viên'"></span>
    </div>
    <div class="card-body p-0">
        <table class="table table-striped table-hover mb-0">
            <thead class="table-light">
                <tr>
                    <th style="width: 80px;">STT</th>
                    <th>Họ và Tên</th>
                    <th>Chức Vụ</th>
                    <th>Email</th>
                </tr>
            </thead>
            <tbody>
                <!-- 2. Vòng lặp cấp 2: Lặp qua danh sách nhân viên trong phòng ban đó (Detail) -->
                <tr th:each="emp, stat : ${dept.employees}">
                    <td th:text="${stat.count}">1</td>
                    <td class="fw-bold" th:text="${emp.fullName}">Hoàng Đại Dương</td>
                    <td th:text="${emp.position}">Developer</td>
                    <td th:text="${emp.email}">duong@iuh.vn</td>
                </tr>
                <tr th:if="${#lists.isEmpty(dept.employees)}">
                    <td colspan="4" class="text-center text-muted py-3">Phòng ban này hiện chưa có nhân viên.</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
```

---

#### 3. Dạng Ma Trận / Bảng Chéo (Crosstab / Pivot Table - Chuyển Dòng ⇄ Cột)

- **Đặc điểm**: Xoay chiều dữ liệu (Transpose / Pivot), biến giá trị các dòng thành các tiêu đề cột (hoặc ngược lại) để phân tích đối chiếu đa chiều.
- **Ứng dụng**: Bảng chấm công theo ngày trong tháng, báo cáo doanh số theo tháng, bảng điểm sinh viên theo môn học.

**🖼️ Hình vẽ minh họa:**

```text
┌──────────────────────┬─────────────┬─────────────┬─────────────┬──────────────┐
│ Nhân Viên \ Tháng    │ Tháng 1     │ Tháng 2     │ Tháng 3     │ Tổng Doanh Số│  <-- Tiêu đề cột động
├──────────────────────┼─────────────┼─────────────┼─────────────┼──────────────┤
│ Hoàng Đại Dương      │ 15.000.000đ │ 18.000.000đ │ 22.000.000đ │  55.000.000đ │
│ Nguyễn Trung Dũng    │ 12.000.000đ │ 14.000.000đ │ 16.000.000đ │  42.000.000đ │
│ Lê Thành Long        │ 20.000.000đ │ 25.000.000đ │ 28.000.000đ │  73.000.000đ │
├──────────────────────┼─────────────┼─────────────┼─────────────┼──────────────┤
│ 📌 TỔNG CỘNG         │ 47.000.000đ │ 57.000.000đ │ 66.000.000đ │ 170.000.000đ │
└──────────────────────┴─────────────┴─────────────┴─────────────┴──────────────┘
```

- **Mã ví dụ Thymeleaf**:

```html
<table class="table table-bordered text-center align-middle shadow-sm">
    <thead class="table-secondary">
        <tr>
            <th class="text-start">Họ Tên Nhân Viên</th>
            <!-- Cột động theo danh sách các tháng -->
            <th th:each="m : ${monthList}" th:text="'Tháng ' + ${m}">Tháng 1</th>
            <th class="table-dark">Tổng Cộng</th>
        </tr>
    </thead>
    <tbody>
        <tr th:each="row : ${salesReport}">
            <td class="text-start fw-bold" th:text="${row.employeeName}">Nguyễn Văn A</td>
            <!-- Lấy doanh thu theo từng tháng từ Map -->
            <td th:each="m : ${monthList}" th:text="${#numbers.formatInteger(row.salesByMonth.get(m), 0, 'POINT')} + ' đ'">15.000.000 đ</td>
            <td class="text-danger fw-bold" th:text="${#numbers.formatInteger(row.totalAmount, 0, 'POINT')} + ' đ'">55.000.000 đ</td>
        </tr>
    </tbody>
</table>
```

---

#### 4. Dạng Lưới Thẻ / X Cột Nhiều Dòng (Card Grid Layout - Responsive Matrix)

- **Đặc điểm**: Dữ liệu trực quan gồm cả hình ảnh, badge, mô tả được xếp theo lưới đa cột (Grid: ví dụ 3 cột trên Desktop, 2 cột trên Tablet, 1 cột trên Mobile), tự động xuống hàng theo số lượng bản ghi.
- **Ứng dụng**: Danh mục sản phẩm e-commerce, danh sách tin tức/blog, danh bạ nhân sự.

**🖼️ Hình vẽ minh họa:**

```text
┌─────────────────────────┐  ┌─────────────────────────┐  ┌─────────────────────────┐
│ 🖼️ [ Hình Ảnh Laptop ]  │  │ 🖼️ [ Hình Ảnh Chuột ]   │  │ 🖼️ [ Hình Ảnh Bàn Phím] │
│ 🏷️ Phân loại: Máy tính  │  │ 🏷️ Phân loại: Phụ kiện  │  │ 🏷️ Phân loại: Gaming     │
│ 📌 Laptop Dell XPS 15   │  │ 📌 Chuột Logitech MX    │  │ 📌 Bàn Phím Keychron K2 │
│ 💰 28.000.000 VNĐ       │  │ 💰 1.850.000 VNĐ        │  │ 💰 2.200.000 VNĐ        │
│ [ 🛒 Thêm vào giỏ hàng] │  │ [ 🛒 Thêm vào giỏ hàng] │  │ [ 🛒 Thêm vào giỏ hàng] │
└─────────────────────────┘  └─────────────────────────┘  └─────────────────────────┘
      (Cột 1 - Dòng 1)             (Cột 2 - Dòng 1)             (Cột 3 - Dòng 1)

┌─────────────────────────┐  ┌─────────────────────────┐  ┌─────────────────────────┐
│ 🖼️ [ Hình Ảnh Màn hình] │  │ 🖼️ [ Hình Ảnh Tai nghe] │  │ 🖼️ [ Hình Ảnh Webcam ]  │
│ 🏷️ Phân loại: Màn hình  │  │ 🏷️ Phân loại: Âm thanh  │  │ 🏷️ Phân loại: Phụ kiện  │
│ 📌 Màn hình Dell Ultra  │  │ 📌 Tai nghe Sony WH     │  │ 📌 Webcam Logitech 4K   │
│ 💰 10.500.000 VNĐ       │  │ 💰 6.900.000 VNĐ        │  │ 💰 3.400.000 VNĐ        │
│ [ 🛒 Thêm vào giỏ hàng] │  │ [ 🛒 Thêm vào giỏ hàng] │  │ [ 🛒 Thêm vào giỏ hàng] │
└─────────────────────────┘  └─────────────────────────┘  └─────────────────────────┘
      (Cột 1 - Dòng 2)             (Cột 2 - Dòng 2)             (Cột 3 - Dòng 2)
```

- **Mã ví dụ Thymeleaf + Bootstrap Grid System**:

```html
<div class="container my-4">
    <!-- row-cols thiết lập: 1 cột (mobile), 2 cột (tablet), 3 cột (desktop) -->
    <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
        <!-- Vòng lặp render tự động chia cột và xuống dòng -->
        <div th:each="p : ${products}" class="col">
            <div class="card h-100 shadow-sm border-0 hover-shadow transition">
                <img th:src="${p.imageUrl}" class="card-img-top" alt="Ảnh sản phẩm" style="height: 200px; object-fit: cover;">
                <div class="card-body d-flex flex-column">
                    <span class="badge bg-info text-dark mb-2 align-self-start" th:text="${p.category.name}">Phụ kiện</span>
                    <h5 class="card-title text-truncate" th:text="${p.name}">Tên sản phẩm</h5>
                    <p class="card-text text-muted flex-grow-1" th:text="${p.shortDescription}">Mô tả ngắn...</p>
                    <div class="d-flex justify-content-between align-items-center mt-3 pt-2 border-top">
                        <span class="text-danger fw-bold fs-5" th:text="${#numbers.formatDecimal(p.price, 0, 'COMMA', 0, 'POINT')} + ' đ'"></span>
                        <a th:href="@{/product/detail/{id}(id=${p.id})}" class="btn btn-outline-primary btn-sm">Xem chi tiết</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```


[github.com/baphuc/basic_web](https://github.com/baphuc/basic_web)

github.com/baphuc/independent_web
