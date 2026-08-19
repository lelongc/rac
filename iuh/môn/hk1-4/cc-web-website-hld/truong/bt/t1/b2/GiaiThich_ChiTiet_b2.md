# HƯỚNG DẪN GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE BÀI 2 (DANH SÁCH SẢN PHẨM)

Tài liệu này giải thích **siêu kỹ từng dòng code, cú pháp mảng đối tượng, vòng lặp `forEach` và cách chèn HTML tự động (DOM)** trong Bài 2.

---

## 📘 PHẦN 1: FILE `index.html`

```html
1: <!DOCTYPE html>
2: <html lang="vi">
3: <head>
4:     <meta charset="UTF-8">
5:     <title>Danh sách sản phẩm</title>
6:     <link rel="stylesheet" href="style.css">
7: </head>
8: <body>
9:     <div class="container">
10:         <h2>Danh Sách Sản Phẩm</h2>
11: 
12:         <table>
13:             <thead>
14:                 <tr>
15:                     <th>Mã SP</th>
16:                     <th>Tên sản phẩm</th>
17:                     <th>Giá (VNĐ)</th>
18:                     <th>Số lượng</th>
19:                     <th>Danh mục</th>
20:                 </tr>
21:             </thead>
22:             <tbody id="product-table-body">
23:                 <!-- Dữ liệu sản phẩm sẽ được nạp vào đây bằng JavaScript -->
24:             </tbody>
25:         </table>
26:     </div>
27: 
28:     <script src="script.js"></script>
29: </body>
30: </html>
```

### 🔍 Giải thích chi tiết từng dòng HTML:

* **Dòng 12: `<table>`**
  - Thẻ tạo một **bảng dữ liệu** gồm các hàng và cột.

* **Dòng 13: `<thead>`**
  - Thẻ bao bọc phần **tiêu đề của bảng** (Table Head).

* **Dòng 14: `<tr>`**
  - `<tr>` (Table Row): Khai báo một **hàng** (dòng) trong bảng.

* **Dòng 15 - 19: `<th>...</th>`**
  - `<th>` (Table Header Cell): Thẻ ô tiêu đề của cột (chữ hiển thị sẽ tự động được in đậm và căn giữa).
  - Khai báo 5 cột tiêu đề: `Mã SP`, `Tên sản phẩm`, `Giá (VNĐ)`, `Số lượng`, `Danh mục`.

* **Dòng 22: `<tbody id="product-table-body">`**
  - `<tbody>` (Table Body): Phần thân của bảng chứa dữ liệu các dòng sản phẩm.
  - `id="product-table-body"`: Đặt mã ID duy nhất để JavaScript tìm chính xác vị trí này và tự động chèn các hàng dữ liệu sản phẩm vào bên trong.

* **Dòng 23: `<!-- ... -->`**: Dòng chú thích ẩn trong HTML.

---

## 🟨 PHẦN 2: FILE `script.js`

```javascript
1: // Mảng chứa danh sách các đối tượng sản phẩm
2: const products = [
3:     { id: "SP01", name: "Laptop Dell XPS 15", price: 35000000, quantity: 5, category: "Laptop" },
4:     { id: "SP02", name: "Điện thoại iPhone 15 Pro", price: 28000000, quantity: 10, category: "Điện thoại" },
5:     { id: "SP03", name: "Tai nghe Sony WH-1000XM5", price: 8500000, quantity: 12, category: "Phụ kiện" },
6:     { id: "SP04", name: "Bàn phím cơ Keychron K2", price: 2100000, quantity: 8, category: "Phụ kiện" },
7:     { id: "SP05", name: "Màn hình LG UltraGear 27 inch", price: 7900000, quantity: 4, category: "Màn hình" }
8: ];
9: 
10: // Hàm nạp danh sách sản phẩm vào bảng (table)
11: function loadProducts() {
12:     let tbody = document.getElementById("product-table-body");
13:     
14:     // Xóa dữ liệu cũ nếu có
15:     tbody.innerHTML = "";
16: 
17:     // Duyệt qua mảng sản phẩm và nối từng dòng tr vào table
18:     products.forEach(product => {
19:         let row = `
20:             <tr>
21:                 <td>${product.id}</td>
22:                 <td>${product.name}</td>
23:                 <td>${product.price.toLocaleString("vi-VN")}</td>
24:                 <td>${product.quantity}</td>
25:                 <td>${product.category}</td>
26:             </tr>
27:         `;
28:         tbody.innerHTML += row;
29:     });
30: }
31: 
32: // Tự động nạp dữ liệu khi trang web được tải xong
33: window.onload = loadProducts;
```

### 🔍 Giải thích chi tiết từng câu lệnh JS:

* **Dòng 2 - 8: `const products = [ { ... }, { ... } ];`**
  - `[]`: Ký hiệu khai báo một **Mảng (Array)** chứa danh sách các phần tử.
  - `{ id: "SP01", name: "...", ... }`: Khai báo một **Đối tượng (Object)** sản phẩm chứa 5 thuộc tính:
    - `id`: Mã sản phẩm (chuỗi chữ).
    - `name`: Tên sản phẩm.
    - `price`: Giá bán (số nguyên).
    - `quantity`: Số lượng tồn kho.
    - `category`: Tên danh mục.

* **Dòng 11: `function loadProducts() {`**
  - Định nghĩa hàm `loadProducts()` thực hiện công việc đọc mảng và chèn vào bảng HTML.

* **Dòng 12: `let tbody = document.getElementById("product-table-body");`**
  - `document.getElementById("product-table-body")`: Tìm thẻ `<tbody id="product-table-body">` bên file HTML và lưu vào biến `tbody`.

* **Dòng 15: `tbody.innerHTML = "";`**
  - `innerHTML`: Thuộc tính đại diện cho toàn bộ nội dung HTML bên trong thẻ `<tbody>`.
  - `= ""`: Gán bằng chuỗi rỗng để làm sạch/xóa toàn bộ nội dung cũ trước khi nạp dữ liệu mới.

* **Dòng 18: `products.forEach(product => {`**
  - `products.forEach(...)`: Phương thức lặp qua từng phần tử trong mảng `products`.
  - `product =>`: Cú pháp **Arrow Function (Hàm mũi tên)**. Ở mỗi vòng lặp, biến `product` sẽ đại diện cho 1 đối tượng sản phẩm hiện tại.

* **Dòng 19 - 27: `let row = \`<tr> ... </tr>\`;`**
  - Đóng gói cấu trúc 1 dòng trong bảng HTML (`<tr><td>...</td></tr>`) vào biến `row`.
  - `${product.id}`: Lấy giá trị mã SP của sản phẩm hiện tại.
  - `${product.name}`: Lấy tên sản phẩm.
  - `${product.price.toLocaleString("vi-VN")}`: Định dạng số giá tiền theo chuẩn Việt Nam (ví dụ: `35000000` thành `35.000.000`).
  - `${product.quantity}`: Lấy số lượng.
  - `${product.category}`: Lấy danh mục.

* **Dòng 28: `tbody.innerHTML += row;`**
  - `+=`: Toán tử cộng nối chuỗi.
  - Nối dòng HTML vừa tạo (`row`) vào cuối nội dung của thẻ `<tbody>`.

* **Dòng 33: `window.onload = loadProducts;`**
  - `window.onload`: Sự kiện xảy ra khi trình duyệt đã tải xong toàn bộ HTML, CSS và hình ảnh.
  - `= loadProducts`: Gán hàm `loadProducts` tự động thực thi ngay sau khi trang tải xong mà người dùng không cần bấm bất kỳ nút nào.

---

## 🎨 PHẦN 3: FILE `style.css`

```css
table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
}
```
- `width: 100%;`: Bảng chiếm hết chiều rộng của khung chứa.
- `border-collapse: collapse;`: **Gộp đường viền các ô lại thành 1 đường đơn**, giúp bảng nhìn sắc nét, không bị đường viền đôi trùng lặp.

```css
th, td {
    padding: 10px 14px;
    text-align: left;
    border-bottom: 1px solid #e0e0e0;
}
```
- `padding: 10px 14px;`: Tạo khoảng cách đệm trong các ô (trên/dưới 10px, trái/phải 14px) cho chữ không bị dính vào viền.
- `border-bottom: 1px solid #e0e0e0;`: Tạo đường gạch kẻ ngang màu xám mỏng dưới mỗi dòng.

```css
tr:nth-child(even) {
    background-color: #f9f9f9;
}
```
- `tr:nth-child(even)`: Pseudo-class chọn **các hàng số chẵn** (hàng 2, 4, 6...) và tô nền xám rất nhẹ `#f9f9f9` để tạo hiệu ứng kẻ sọc dễ quan sát.

```css
tr:hover {
    background-color: #f1f5f9;
}
```
- `tr:hover`: Khi con trỏ chuột rê qua hàng nào thì hàng đó sẽ tự đổi sang màu nền xám xanh nhạt.
