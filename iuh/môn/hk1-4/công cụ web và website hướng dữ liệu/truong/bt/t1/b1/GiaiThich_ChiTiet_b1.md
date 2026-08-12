# HƯỚNG DẪN GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE BÀI 1 (QUY ĐỔI TIỀN TỆ)

Tài liệu này giải thích **siêu kỹ từng dòng code, từng cú pháp, thuộc tính và dấu câu** trong bài 1 để bạn nắm vững bản chất HTML, CSS và JavaScript DOM.

---

## 📘 PHẦN 1: FILE `index.html`

```html
1: <!DOCTYPE html>
2: <html lang="vi">
3: <head>
4:     <meta charset="UTF-8">
5:     <title>Quy đổi tiền tệ</title>
6:     <link rel="stylesheet" href="style.css">
7: </head>
8: <body>
9:     <div class="container">
10:         <h2>Chương trình quy đổi tiền tệ</h2>
11: 
12:         <form>
13:             <div class="form-group">
14:                 <label for="amount">Số tiền:</label>
15:                 <input type="number" id="amount" value="1">
16:             </div>
17: 
18:             <div class="form-group">
19:                 <label for="from">Từ đồng tiền:</label>
20:                 <select id="from">
21:                     <option value="USD">USD - Đô la Mỹ</option>
22:                     <option value="VND" selected>VND - Việt Nam Đồng</option>
23:                     <option value="EUR">EUR - Euro</option>
24:                     <option value="JPY">JPY - Yên Nhật</option>
25:                     <option value="GBP">GBP - Bảng Anh</option>
26:                 </select>
27:             </div>
28: 
29:             <div class="form-group">
30:                 <label for="to">Sang đồng tiền:</label>
31:                 <select id="to">
32:                     <option value="USD" selected>USD - Đô la Mỹ</option>
33:                     <option value="VND">VND - Việt Nam Đồng</option>
34:                     <option value="EUR">EUR - Euro</option>
35:                     <option value="JPY">JPY - Yên Nhật</option>
36:                     <option value="GBP">GBP - Bảng Anh</option>
37:                 </select>
38:             </div>
39: 
40:             <button type="button" onclick="convert()">Quy đổi</button>
41:         </form>
42: 
43:         <div class="result-box" id="result">Kết quả: ---</div>
44:     </div>
45: 
46:     <script src="script.js"></script>
47: </body>
48: </html>
```

### 🔍 Giải thích chi tiết từng dòng HTML:

* **Dòng 1: `<!DOCTYPE html>`**
  - `<!DOCTYPE html>`: Khai báo với trình duyệt biết tài liệu này viết theo chuẩn **HTML5**.

* **Dòng 2: `<html lang="vi">`**
  - `<html>`: Thẻ gốc bao bọc toàn bộ nội dung trang web.
  - `lang="vi"`: Thuộc tính khai báo ngôn ngữ chính của trang là tiếng Việt (`vi`).

* **Dòng 3: `<head>`**
  - Thẻ chứa các thông tin cấu hình (metadata) của trang web (không hiển thị trực tiếp ra màn hình).

* **Dòng 4: `<meta charset="UTF-8">`**
  - `<meta>`: Thẻ chứa thông tin ẩn của trang.
  - `charset="UTF-8"`: Cấu hình mã hóa ký tự là **UTF-8**, giúp trang web hiển thị đúng tiếng Việt có dấu không bị lỗi font.

* **Dòng 5: `<title>Quy đổi tiền tệ</title>`**
  - Tên tiêu đề hiển thị trên thẻ (tab) của trình duyệt.

* **Dòng 6: `<link rel="stylesheet" href="style.css">`**
  - `<link>`: Liên kết tài nguyên bên ngoài vào trang HTML.
  - `rel="stylesheet"`: Khai báo mối quan hệ tài nguyên là file kiểu dáng CSS.
  - `href="style.css"`: Đường dẫn trỏ tới file CSS tên là `style.css`.

* **Dòng 7: `</head>`**: Đóng thẻ `<head>`.

* **Dòng 8: `<body>`**
  - Thẻ chứa toàn bộ nội dung giao diện được hiển thị ra màn hình cho người dùng xem.

* **Dòng 9: `<div class="container">`**
  - `<div>`: Thẻ khối tạo một vùng chứa (container).
  - `class="container"`: Đặt tên lớp là `container` để dùng CSS tạo khung hình chữ nhật căn giữa màn hình.

* **Dòng 10: `<h2>Chương trình quy đổi tiền tệ</h2>`**
  - `<h2>`: Thẻ tiêu đề cấp 2 (Heading 2) hiển thị dòng chữ tiêu đề của bài.

* **Dòng 12: `<form>`**
  - Thẻ tạo biểu mẫu nhập dữ liệu.

* **Dòng 13: `<div class="form-group">`**
  - Gom nhóm các phần tử liên quan (label + input) lại với nhau để dế căn chỉnh CSS.

* **Dòng 14: `<label for="amount">Số tiền:</label>`**
  - `<label>`: Thẻ nhãn mô tả cho ô nhập liệu.
  - `for="amount"`: Đặt liên kết với thẻ input có `id="amount"`. Khi click vào dòng chữ "Số tiền:", con trỏ sẽ tự nhảy vào ô input tương ứng.

* **Dòng 15: `<input type="number" id="amount" value="1">`**
  - `<input>`: Ô cho phép người dùng nhập dữ liệu.
  - `type="number"`: Chỉ cho phép nhập số (có mũi tên tăng giảm số).
  - `id="amount"`: Mã định danh **duy nhất** dùng để JavaScript tìm đúng ô này và lấy giá trị.
  - `value="1"`: Giá trị số mặc định ban đầu là `1`.

* **Dòng 19 - 26 (Tương tự cho Đồng tiền nguồn `from`):**
  - `<select id="from">`: Thẻ tạo danh sách sổ xuống (Dropdown menu). `id="from"` giúp JS nhận biết đây là đồng tiền gốc cần đổi.
  - `<option value="USD">`: Thẻ tùy chọn trong danh sách. Thuộc tính `value="USD"` là giá trị máy tính sử dụng, còn chữ `USD - Đô la Mỹ` là chữ hiển thị cho người dùng xem.
  - `selected`: Thuộc tính đánh dấu tùy chọn đó sẽ được chọn mặc định ngay khi tải trang.

* **Dòng 29 - 38 (Tương tự cho Đồng tiền đích `to`):**
  - `<select id="to">`: Thẻ sổ xuống chọn đồng tiền muốn đổi sang.

* **Dòng 40: `<button type="button" onclick="convert()">Quy đổi</button>`**
  - `<button>`: Tạo nút bấm.
  - `type="button"`: Khai báo đây là nút bấm thường (không tự động tải lại trang khi nằm trong `<form>`).
  - `onclick="convert()"`: **Sự kiện click**. Khi người dùng bấm nút này, trình duyệt sẽ kích hoạt chạy hàm `convert()` trong JavaScript.

* **Dòng 43: `<div class="result-box" id="result">Kết quả: ---</div>`**
  - Khung hiển thị kết quả. `id="result"` giúp JavaScript tìm đến thẻ này để thay đổi chữ "Kết quả: ---" thành kết quả quy đổi thực tế.

* **Dòng 46: `<script src="script.js"></script>`**
  - `<script>`: Liên kết file mã nguồn JavaScript tên là `script.js` vào trang HTML.

---

## 🟨 PHẦN 2: FILE `script.js`

```javascript
1: // Bảng tỷ giá quy đổi cơ bản (gốc là USD)
2: const rates = {
3:     "USD": 1,
4:     "VND": 25450,
5:     "EUR": 0.92,
6:     "JPY": 155.2,
7:     "GBP": 0.79
8: };
9: 
10: function convert() {
11:     // Lấy giá trị từ ô nhập và 2 thẻ select
12:     let amount = parseFloat(document.getElementById("amount").value);
13:     let fromCurrency = document.getElementById("from").value;
14:     let toCurrency = document.getElementById("to").value;
15: 
16:     // Kiểm tra dữ liệu đầu vào
17:     if (isNaN(amount) || amount <= 0) {
18:         document.getElementById("result").innerText = "Kết quả: Vui lòng nhập số tiền hợp lệ!";
19:         return;
20:     }
21: 
22:     // Tính toán quy đổi: (Số tiền / tỷ giá gốc) * tỷ giá đích
23:     let result = (amount / rates[fromCurrency]) * rates[toCurrency];
24: 
25:     // Hiển thị kết quả ra màn hình
26:     document.getElementById("result").innerText = 
27:         `Kết quả: ${amount} ${fromCurrency} = ${result.toLocaleString()} ${toCurrency}`;
28: }
```

### 🔍 Giải thích chi tiết từng câu lệnh JS:

* **Dòng 1: `// ...`**: Dòng chú thích (comment), trình duyệt sẽ bỏ qua không chạy dòng này.

* **Dòng 2 - 8: `const rates = { ... };`**
  - `const`: Từ khóa khai báo **hằng số** (biến không bị gán lại).
  - `rates`: Tên biến chứa một **Đối tượng (Object)** lưu trữ bảng tỷ giá quy đổi so với USD.
  - `{ "USD": 1, "VND": 25450, ... }`: Dữ liệu cặp `Key: Value`. Cú pháp truy cập: `rates["VND"]` sẽ trả về con số `25450`.

* **Dòng 10: `function convert() {`**
  - `function`: Từ khóa khai báo một **hàm (function)** trong JS.
  - `convert()`: Tên hàm (trùng với tên đã gọi ở thuộc tính `onclick="convert()"` bên HTML).
  - `{`: Mở khối lệnh của hàm.

* **Dòng 12: `let amount = parseFloat(document.getElementById("amount").value);`**
  - `let`: Từ khóa khai báo **biến** cục bộ.
  - `document`: Đối tượng toàn cục đại diện cho trang web hiện tại (HTML DOM).
  - `.getElementById("amount")`: Tìm thẻ HTML có thuộc tính `id="amount"` (chính là ô nhập số tiền).
  - `.value`: Lấy ra giá trị chuỗi văn bản (String) người dùng gõ vào ô nhập.
  - `parseFloat(...)`: Hàm chuyển đổi chuỗi chữ thành **số thực (Float)** để có thể thực hiện phép tính số học.

* **Dòng 13: `let fromCurrency = document.getElementById("from").value;`**
  - Lấy mã đồng tiền đang được chọn ở danh sách sổ xuống `from` (ví dụ: `"VND"` hoặc `"USD"`).

* **Dòng 14: `let toCurrency = document.getElementById("to").value;`**
  - Lấy mã đồng tiền đang được chọn ở danh sách sổ xuống `to`.

* **Dòng 17: `if (isNaN(amount) || amount <= 0) {`**
  - `if (...)`: Cấu trúc điều kiện "Nếu... thì...".
  - `isNaN(amount)`: Hàm kiểm tra xem `amount` có phải là **Not a Number** (không phải là số) hay không.
  - `||`: Toán tử LOGIC **OR (Hoặc)**.
  - `amount <= 0`: Kiểm tra nếu số tiền nhỏ hơn hoặc bằng 0.

* **Dòng 18: `document.getElementById("result").innerText = "Kết quả: Vui lòng nhập số tiền hợp lệ!";`**
  - Tìm thẻ có `id="result"` và gán thuộc tính `.innerText` (nội dung chữ hiển thị) thành câu thông báo lỗi.

* **Dòng 19: `return;`**
  - Dừng không cho hàm chạy tiếp các câu lệnh phía dưới khi gặp lỗi.

* **Dòng 23: `let result = (amount / rates[fromCurrency]) * rates[toCurrency];`**
  - `rates[fromCurrency]`: Tìm giá trị tỷ giá của đồng tiền gốc trong đối tượng `rates`.
  - Công thức: Quy đổi từ tiền gốc ra USD (`amount / rates[fromCurrency]`), sau đó nhân với tỷ giá tiền đích (`* rates[toCurrency]`).

* **Dòng 26 - 27: `document.getElementById("result").innerText = \`Kết quả: ${amount} ...\`;`**
  - Sử dụng **Template Literals (Dấu ngoặc huyền \`)**: Cho phép chèn trực tiếp giá trị biến vào chuỗi bằng cú pháp `${tên_biến}`.
  - `.toLocaleString()`: Hàm định dạng số có dấu phân cách hàng nghìn (ví dụ: `25450` thành `25,450` hoặc `25.450`).

---

## 🎨 PHẦN 3: FILE `style.css`

```css
1: body {
2:     font-family: Arial, sans-serif;
3:     background-color: #f4f6f9;
4:     margin: 0;
5:     padding: 40px 20px;
6:     display: flex;
7:     justify-content: center;
8: }
```
- `font-family: Arial, sans-serif;`: Đổi phông chữ sang Arial cho dễ đọc.
- `background-color: #f4f6f9;`: Đặt màu nền trang web là màu xám xanh nhẹ.
- `display: flex; justify-content: center;`: Sử dụng Flexbox để căn khung nội dung vào đúng **chính giữa màn hình**.

```css
.container {
    background-color: #ffffff;
    padding: 25px 30px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    width: 100%;
    max-width: 420px;
}
```
- `.container`: Áp dụng kiểu dáng cho thẻ có `class="container"`.
- `background-color: #ffffff;`: Màu nền của khung là màu trắng tinh.
- `border-radius: 8px;`: Bo tròn 4 góc khung 8px.
- `box-shadow: ...`: Tạo hiệu ứng đổ bóng mờ nhẹ dưới khung.
- `max-width: 420px;`: Giới hạn chiều rộng tối đa của khung là 420px.
