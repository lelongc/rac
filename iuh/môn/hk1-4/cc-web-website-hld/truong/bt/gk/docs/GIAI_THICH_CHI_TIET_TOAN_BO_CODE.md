# CẨM NANG ÔN THI GIỮA KỲ & GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE

**Môn học:** Xây dựng website hướng dịch vụ (IUH)
**Giảng viên:** Trương Bá Phúc
**Mô hình thi:** Single Page Application (SPA) gọi Web Service (REST API)

---

## 📑 MỤC LỤC

1. [Bản chất bài thi giữa kỳ &amp; Lời dặn dò của thầy](#1-bản-chất-bài-thi-giữa-kỳ)
2. [Giải thích chi tiết TỪNG DÒNG CODE trong file `index.html` (Frontend SPA)](#2-giải-thích-chi-tiết-từng-dòng-code-trong-indexhtml)
   - [2.1. Phần thẻ HTML &amp; CSS](#21-phần-thẻ-html--css)
   - [2.2. Phần JavaScript gọi API (`fetch`)](#22-phần-javascript-gọi-api-fetch)
3. [Giải thích chi tiết TỪNG ANNOTATION &amp; DÒNG CODE Java (Backend Web Service)](#3-giải-thích-chi-tiết-từng-annotation--dòng-code-java)
   - [3.1. Controller: `FacultyController.java`](#31-controller-facultycontrollerjava)
   - [3.2. Service: `FacultyService.java`](#32-service-facultyservicejava)
   - [3.3. Model: `Faculty.java` &amp; `Student.java`](#33-model-facultyjava--studentjava)
   - [3.4. Cấu hình: `pom.xml`, `application.properties`, `GkApplication.java`](#34-cấu-hình-pomxml-applicationproperties-gkapplicationjava)
4. [Bộ 15 câu hỏi vấn đáp thầy hay hỏi khi chấm thi &amp; Cách trả lời ăn điểm tuyệt đối](#4-bộ-15-câu-hỏi-vấn-đáp-thầy-hay-hỏi-khi-chấm-thi)
5. [Cẩm nang ứng biến trong 2 phút khi đề bài cho dữ liệu khác](#5-cẩm-nang-ứng-biến-trong-2-phút-khi-đề-thi-đổi-dữ-liệu)
6. [Xử lý 4 lỗi kinh điển trong phòng thi](#6-xử-lý-4-lỗi-kinh-điển-trong-phòng-thi)

---

# 1. BẢN CHẤT BÀI THI GIỮA KỲ

### 1.1. Khác biệt cốt lõi: SPA vs MVC truyền thống

- **Bài tập cũ (Spring MVC + Thymeleaf):** Mỗi lần bấm Thêm/Sửa/Xóa, trình duyệt submit form lên server, server render lại toàn bộ trang HTML mới và redirect (`return "redirect:/faculties"`). Trang web bị chớp/tải lại (F5).
- **Bài thi Giữa Kỳ (Web Service + SPA):**
  - Web Service **KHÔNG BAO GIỜ TRẢ VỀ HTML**, mà trả về **DỮ LIỆU THÔ DẠNG JSON** (ví dụ: `[{"id":1, "name":"CNTT"}]`).
  - Giao diện người dùng là **1 file HTML duy nhất (Single Page Application)**.
  - Sử dụng **JavaScript (`fetch()`)** để âm thầm gửi và nhận JSON từ server ngầm dưới nền, sau đó dùng DOM JavaScript vẽ lại thẻ `<table>` mà **không hề tải lại trang web**.

### 1.2. Quy chế thi giữa kỳ (Lời thầy dặn trong video):

1. **Phạm vi thi: Đúng 3 bước đầu (BỎ Paging & Sorting)**:
   - **Bước 1:** Đổ danh sách đối tượng Cha (Khoa) vào Combobox (`<select>`).
   - **Bước 2:** Bắt sự kiện chọn item trong Combobox (`onchange`) $\to$ gọi Web Service lấy JSON danh sách Con (Sinh viên) $\to$ đổ vào Table (`<table>`).
   - **Bước 3:** Đầy đủ bộ CRUD Thêm mới, Sửa, Xóa, Tìm kiếm qua Web Service.
   - *(Bước 4 & 5 Phân trang, Sắp xếp dành cho thi Cuối kỳ, Giữa kỳ KHÔNG thi)*.
2. **Lúc thi, thầy sẽ cung cấp sẵn Web Service (Backend):**
   - Bạn chỉ cần tập trung làm file giao diện HTML + JavaScript.
   - Dự án Spring Boot này được viết sẵn để bạn chạy giả lập tại nhà và phòng hờ nếu thầy bắt tự dựng cả Backend.

---

# 2. GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG `index.html`

File [index.html](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/bt/gk/src/main/resources/static/index.html) nằm tại `src/main/resources/static/index.html`.

---

## 2.1. Phần thẻ HTML & CSS

### Dòng 1 - 6: Khai báo trang và Tiêu đề

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Quản lý dữ liệu Web Service (SPA)</title>
```

- `<!DOCTYPE html>`: Khai báo chuẩn tài liệu HTML5 để mọi trình duyệt (Chrome, Edge, Firefox) render giao diện chuẩn nhất.
- `<meta charset="UTF-8">`: **Rất quan trọng!** Định dạng bảng mã Unicode UTF-8 để tiếng Việt có dấu không bị lỗi font hay biến thành ký tự lạ `???`.
- `<title>`: Tiêu đề hiển thị trên tab của trình duyệt.

---

### Dòng 7 - 45: Phần CSS (Đơn giản, đúng chuẩn đi thi)

```css
body { font-family: Arial, sans-serif; margin: 20px auto; max-width: 850px; line-height: 1.5; }
```

- `font-family: Arial, sans-serif`: Dùng font chữ Arial cơ bản, máy nào cũng có, nhìn sạch sẽ.
- `margin: 20px auto; max-width: 850px`: Căn toàn bộ nội dung web ra chính giữa màn hình với bề rộng tối đa 850px, nhìn cân đối không bị dạt sang mép trái.

```css
table { border-collapse: collapse; width: 100%; margin-top: 10px; }
th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
th { background-color: #f4f4f4; }
```

- `border-collapse: collapse`: **Bắt buộc khi kẻ bảng!** Nó gộp đường viền của các ô liền kề thành 1 nét đơn (nếu không có thuộc tính này, bảng sẽ bị viền đôi rất xấu).
- `width: 100%`: Bảng tự động giãn đều 100% bề rộng khung chứa.
- `padding: 8px`: Tạo khoảng cách đệm 8px bên trong mỗi ô để chữ không dính sát vào đường viền.
- `th { background-color: #f4f4f4; }`: Nền tiêu đề bảng màu xám sáng để phân biệt rõ với các dòng dữ liệu bên dưới.

```css
.box { border: 1px solid #ccc; padding: 15px; margin-bottom: 15px; border-radius: 4px; }
input, select { padding: 6px; margin: 4px 6px 4px 0; }
button { padding: 6px 12px; margin-right: 5px; cursor: pointer; }
```

- `.box`: Tạo khung viền bao quanh từng khu vực (Chọn khoa, Tìm kiếm, Form, Bảng).
- `cursor: pointer`: Khi di chuột vào nút bấm `<button>`, con trỏ chuột tự động biến thành hình bàn tay chỉ trỏ.

---

### Dòng 52 - 59: Combobox chọn Khoa (Bước 1)

```html
<div class="box">
    <h3>Chọn Khoa</h3>
    <label for="facultySelect"><strong>Khoa: </strong></label>
    <select id="facultySelect" onchange="onFacultyChange()">
        <option value="">-- Vui lòng chọn Khoa --</option>
    </select>
</div>
```

- `<select id="facultySelect">`: Thẻ tạo trình đơn thả xuống (combobox). Thuộc tính `id="facultySelect"` là định danh duy nhất để JavaScript dùng `document.getElementById('facultySelect')` truy xuất vào thẻ này.
- `onchange="onFacultyChange()"`: **Sự kiện cốt lõi của Bước 2!** Khi người dùng click chọn 1 khoa khác trong danh sách, trình duyệt sẽ tự động kích hoạt gọi hàm JavaScript `onFacultyChange()`.
- `<option value="">`: Dòng mặc định ban đầu có giá trị `value` rỗng.

---

### Dòng 70 - 78: Ô tìm kiếm sinh viên (Hỗ trợ cả gõ phím & bấm nút)

```html
<div class="box">
    <h3>Tìm kiếm</h3>
    <input type="text" id="keyword" placeholder="Nhập từ khóa tìm kiếm..." oninput="searchStudents()">
    <button onclick="searchStudents()">Tìm kiếm</button>
</div>
```

- `<input type="text" id="keyword" oninput="searchStudents()">`:
  - `oninput`: Bắt sự kiện mỗi khi nội dung trong ô thay đổi (gõ chữ hoặc xóa chữ).
  - **Tự động tải lại khi xóa chữ:** Ngay khi người dùng nhấn Backspace xóa hết chữ trong ô tìm kiếm, hệ thống tự động tải lại toàn bộ danh sách của khoa ngay lập tức!
- `<button onclick="searchStudents()">`: Nút bấm tìm kiếm thủ công (phòng trường hợp người dùng hoặc thầy muốn click chuột).
- **Vì sao không cần nút "Xóa tìm kiếm"?** Vì sự kiện `oninput` đã tự động khôi phục danh sách ngay khi người dùng xóa trắng ô nhập. Giao diện vừa gọn đẹp, vừa tiện lợi số 1.

---

### Dòng 69 - 82: Form Thêm mới và Sửa sinh viên (Dùng chung 1 Form)

```html
<div class="box">
    <h3 id="formTitle">Thêm mới</h3>
    <input type="hidden" id="studentId">

    <label>Họ tên: </label>
    <input type="text" id="studentName" placeholder="Nhập họ tên...">

    <label>Email: </label>
    <input type="email" id="studentEmail" placeholder="Nhập email...">

    <button id="btnSave" onclick="saveStudent()">Thêm</button>
    <button id="btnCancel" onclick="resetForm()" style="display: none;">Hủy</button>
</div>
```

- `<input type="hidden" id="studentId">`: **Kỹ thuật kinh điển của dân lập trình Web!**
  - Ô này bị ẩn (`hidden`), người dùng không nhìn thấy.
  - **Ý nghĩa:** Khi ô này **rỗng** $\to$ hệ thống hiểu là đang **THÊM MỚI (POST)**. Khi ô này **có số ID** (do người dùng vừa bấm nút Sửa ở bảng) $\to$ hệ thống hiểu là đang **CẬP NHẬT (PUT)** cho chính sinh viên có ID đó!
- `<button id="btnSave" onclick="saveStudent()">`: Nút lưu dữ liệu. Ban đầu ghi chữ "Thêm", khi bấm nút Sửa thì JavaScript sẽ đổi chữ thành "Cập nhật".
- `<button id="btnCancel" style="display: none;">`: Nút Hủy. Mặc định bị ẩn (`display: none`), chỉ khi nào người dùng bấm nút Sửa thì nó mới hiện lên để cho phép hủy bỏ việc sửa.

---

### Dòng 84 - 101: Bảng dữ liệu (Table - Bước 2)

```html
<table>
    <thead>
        <tr>
            <th style="width: 10%;">ID</th>
            <th style="width: 40%;">Họ tên</th>
            <th style="width: 30%;">Email</th>
            <th style="width: 20%;">Hành động</th>
        </tr>
    </thead>
    <tbody id="studentTableBody">
        <tr>
            <td colspan="4" style="text-align: center;">Vui lòng chọn mục ở trên để xem danh sách</td>
        </tr>
    </tbody>
</table>
```

- `<thead>`: Phần tiêu đề bảng, cố định các cột: ID, Họ tên, Email, Hành động.
- `<tbody id="studentTableBody">`: **Thân bảng rỗng!** Toàn bộ các dòng `<tr><td>...</td></tr>` chứa dữ liệu sinh viên sẽ do JavaScript tạo ra và nhồi vào đây.
- `colspan="4"`: Gộp cả 4 cột lại thành 1 ô rộng để hiện thông báo hướng dẫn khi chưa chọn khoa.

---

## 2.2. Phần JavaScript gọi API (`fetch`)

### Dòng 104 - 114: Biến API gốc & Kích hoạt khi mở trang

```javascript
const API_URL = '/api';

window.onload = function() {
    loadFaculties();
};
```

- `const API_URL = '/api'`: Đường dẫn gốc của Web Service.
  - Khi ứng dụng chạy chung một server Spring Boot, viết `/api` (đường dẫn tương đối) là chuẩn nhất, chạy trên bất kỳ port nào (8080, 8084) cũng tự nhận đúng.
  - Nếu thầy cung cấp Web Service ở một link riêng biệt (ví dụ port 8080), bạn chỉ cần sửa thành `const API_URL = 'http://localhost:8080/api'`.
- `window.onload`: Đảm bảo rằng **toàn bộ giao diện HTML đã được trình duyệt tải xong hoàn toàn** thì mới bắt đầu chạy JavaScript. Nếu không có dòng này, code có thể chạy trước khi thẻ `<select>` xuất hiện dẫn đến lỗi `null`.

---

### Dòng 116 - 138: BƯỚC 1 - Lấy danh sách Khoa đổ vào Combobox

```javascript
function loadFaculties() {
    fetch(`${API_URL}/faculties`)
        .then(response => response.json())
        .then(list => {
            const select = document.getElementById('facultySelect');
            select.innerHTML = '<option value="">-- Vui lòng chọn --</option>';
            list.forEach(item => {
                select.innerHTML += `<option value="${item.id}">${item.name}</option>`;
            });
        })
        .catch(err => console.error('Lỗi tải combobox:', err));
}
```

**Giải thích cặn kẽ từng lệnh:**

1. `fetch(`${API_URL}/faculties`)`: Trình duyệt gửi một HTTP request phương thức `GET` đến endpoint `/api/faculties`. Hàm `fetch()` trả về một `Promise`.
2. `.then(response => response.json())`:
   - **Tại sao phải có dòng này?** Đối tượng `response` nhận về ban đầu là dạng luồng stream dữ liệu mạng thô (chưa đọc xong body).
   - Hàm `response.json()` sẽ đọc toàn bộ stream đó và phân tích cú pháp (parse) chuỗi văn bản JSON thành mảng đối tượng JavaScript.
3. `.then(list => { ... })`: Nhận được mảng dữ liệu `list` (ví dụ: `[{id: 1, name: "CNTT"}, {id: 2, name: "Cơ khí"}]`).
4. `select.innerHTML = '<option value="">-- Vui lòng chọn --</option>'`: Đặt lại dòng chữ hướng dẫn ban đầu và xóa sạch các option cũ (tránh bị trùng lặp dữ liệu nếu hàm bị gọi lại).
5. `list.forEach(item => { ... })`: Vòng lặp duyệt qua từng khoa trong mảng:
   - `item.id`: Mã khoa (gán vào thuộc tính `value` của thẻ option để gửi lên server khi chọn).
   - `item.name`: Tên khoa (hiển thị lên màn hình cho người dùng đọc).
   - Dấu `+=`: Cộng dồn từng thẻ `<option>` vào bên trong thẻ `<select>`.
6. `.catch(err => ...)`: Nếu đường truyền mạng lỗi hoặc server bị tắt, đoạn này sẽ bắt lỗi và in ra tab Console (F12) để bạn biết đường sửa, không làm đứng trang web.

---

### Dòng 140 - 171: BƯỚC 2 - Khi chọn Khoa $\to$ Lấy Sinh viên đổ vào Bảng

```javascript
function onFacultyChange() {
    const parentId = document.getElementById('facultySelect').value;
    if (!parentId) {
        document.getElementById('studentTableBody').innerHTML = 
            '<tr><td colspan="4" style="text-align: center;">Vui lòng chọn mục ở trên</td></tr>';
        return;
    }
    loadStudents(parentId);
    resetForm();
}
```

**Giải thích:**

- `const parentId = document.getElementById('facultySelect').value;`: Đọc giá trị `value` của option mà người dùng vừa click chọn (chính là `item.id` của khoa).
- `if (!parentId)`: Nếu người dùng chọn dòng đầu tiên ("-- Vui lòng chọn --"), giá trị `parentId` là rỗng `""` $\to$ hiển thị thông báo nhắc nhở và thoát hàm (`return`), không gọi API vô ích.
- `loadStudents(parentId)`: Gọi hàm lấy danh sách sinh viên thuộc khoa có ID này.
- `resetForm()`: Xóa trắng form nhập liệu để chuẩn bị cho thao tác mới.

```javascript
function loadStudents(parentId, keyword = '') {
    let url = `${API_URL}/faculties/${parentId}/students`;
    if (keyword) {
        url += `?keyword=${encodeURIComponent(keyword)}`;
    }

    fetch(url)
        .then(response => response.json())
        .then(childList => {
            renderTable(childList);
        })
        .catch(err => console.error('Lỗi tải danh sách con:', err));
}
```

**Giải thích:**

- `url = `${API_URL}/faculties/${parentId}/students``: Ghép ID khoa vào đường dẫn theo chuẩn RESTful API: `/api/faculties/1/students`.
- `encodeURIComponent(keyword)`: **Hàm an toàn mạng!** Nó mã hóa các ký tự đặc biệt như khoảng trắng, dấu tiếng Việt, ký tự `&`, `?` thành mã URL hợp lệ (ví dụ khoảng trắng thành `%20`). Giúp tìm kiếm từ khóa tiếng Việt không bao giờ bị lỗi URL.
- `renderTable(childList)`: Sau khi nhận được mảng JSON sinh viên từ server, chuyển toàn bộ dữ liệu cho hàm `renderTable` vẽ lên bảng.

---

### Dòng 173 - 208: Hàm vẽ bảng dữ liệu (`renderTable`)

```javascript
function renderTable(childList) {
    const tbody = document.getElementById('studentTableBody');
    if (!childList || childList.length === 0) {
        tbody.innerHTML = '<tr><td colspan="4" style="text-align: center;">Chưa có dữ liệu nào</td></tr>';
        return;
    }

    let html = '';
    childList.forEach(s => {
        html += `
            <tr>
                <td>${s.id}</td>
                <td>${s.name}</td>
                <td>${s.email}</td>
                <td>
                    <button onclick="editStudent(${s.id}, '${s.name}', '${s.email}')">Sửa</button>
                    <button onclick="deleteStudent(${s.id})">Xóa</button>
                </td>
            </tr>
        `;
    });
    tbody.innerHTML = html;
}
```

**Giải thích:**

- `if (!childList || childList.length === 0)`: Kiểm tra nếu khoa này chưa có sinh viên nào thì báo "Chưa có dữ liệu nào".
- `let html = ''`: Tạo một chuỗi HTML rỗng để tích lũy mã HTML của tất cả các dòng.
  - *Tại sao không gán trực tiếp `tbody.innerHTML += ...` bên trong vòng lặp?* Vì làm như vậy trình duyệt phải vẽ lại DOM liên tục sau mỗi vòng lặp, gây chậm. Gom hết vào biến `html` rồi gán `tbody.innerHTML = html` đúng 1 lần duy nhất ở cuối là cách viết chuẩn và tối ưu nhất!
- `onclick="editStudent(${s.id}, '${s.name}', '${s.email}')"`: Gắn sự kiện click vào nút Sửa, truyền trực tiếp ID, Tên, Email của dòng đó lên form để người dùng sửa.
- `onclick="deleteStudent(${s.id})"`: Gắn sự kiện click vào nút Xóa, truyền ID cần xóa.

---

### Dòng 235 - 245: Chức năng Tìm kiếm (Hỗ trợ cả gõ phím & bấm nút)

```javascript
function searchStudents() {
    const parentId = document.getElementById('facultySelect').value;
    if (!parentId) return; // Nếu chưa chọn Khoa thì không làm gì
    const keyword = document.getElementById('keyword').value.trim();
    // Gọi hàm loadStudents truyền từ khóa.
    // Khi xóa trắng ô tìm kiếm (keyword rỗng), hệ thống tự động tải lại toàn bộ danh sách gốc!
    loadStudents(parentId, keyword);
}
```

**Giải thích:**

1. `parentId`: Lấy mã Khoa đang chọn. Nếu chưa chọn Khoa thì dừng (`return`), tránh hiện thông báo phiền phức khi đang gõ.
2. `keyword`: Lấy chuỗi người dùng gõ và dùng `.trim()` để loại bỏ khoảng trắng thừa ở 2 đầu.
3. `loadStudents(parentId, keyword)`: Gọi hàm gửi request GET lên Web Service.
4. **Cơ chế tự động tải lại danh sách khi xóa chữ:**
   - Khi người dùng xóa hết chữ trong ô tìm kiếm (chuỗi trở thành rỗng `""`), sự kiện `oninput` lập tức gọi `searchStudents()`.
   - Trong `loadStudents()`, do `keyword` rỗng nên điều kiện `if (keyword)` không chạy $\to$ URL được gọi là `/api/faculties/${parentId}/students` $\to$ Web Service tự động trả về toàn bộ danh sách sinh viên ban đầu của khoa!
   - Không cần nút "Xóa tìm kiếm", không cần bấm thêm bất cứ thao tác nào!

---

### 💡 SO SÁNH: Bấm nút "Tìm kiếm" (Click Button) vs Vừa gõ vừa tìm (`oninput`) - Nên trả lời thầy thế nào?

| Tiêu chí                      | Kiểu 1: Bấm nút "Tìm kiếm" (`onclick`)                                                                | Kiểu 2: Vừa gõ vừa tìm (`oninput` / Live Search) ⭐                                                                                                                                                             |
| :------------------------------ | :----------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Độ tiện lợi (UX)**  | Phải nhập xong rồi bấm chuột vào nút "Tìm kiếm".                                                    | **Tiện lợi nhất:** Gõ chữ nào lọc chữ đó; xóa chữ nào hoàn nguyên chữ đó; xóa hết chữ là hiện lại toàn bộ danh sách khoa ngay lập tức.                                              |
| **Độ ngắn & Dễ nhớ** | Cần cả thẻ`<input>` và thẻ `<button>`.                                                              | **Siêu ngắn:** Chỉ cần đúng 1 thẻ `<input oninput="searchStudents()">`. Không cần cả nút Tìm kiếm lẫn nút Xóa!                                                                                 |
| **Khi thầy hỏi**        | "Em dùng nút bấm để người dùng chủ động, tiết kiệm số lượng request mạng gửi lên server." | "Em dùng sự kiện`oninput` để tạo tính năng Live Search thời gian thực. Khi người dùng xóa trắng ô thì tự động tải lại toàn bộ danh sách của khoa mà không cần bấm thêm nút nào ạ." |

👉 **Trong file `index.html`, chúng ta đã kết hợp cả 2**: Vừa có `oninput` (xóa chữ là danh sách tự phục hồi ngay lập tức), vừa có nút `<button>` (ai thích bấm chuột vẫn bấm được bình thường)! Bạn trả lời theo cách nào thầy cũng sẽ khen ngợi.

---

### Dòng 229 - 280: BƯỚC 3 - Thêm mới (POST) và Cập nhật (PUT)

```javascript
function saveStudent() {
    const parentId = document.getElementById('facultySelect').value;
    if (!parentId) {
        alert('Vui lòng chọn mục ở Bước 1 trước!');
        return;
    }

    const id = document.getElementById('studentId').value;
    const name = document.getElementById('studentName').value.trim();
    const email = document.getElementById('studentEmail').value.trim();

    if (!name || !email) {
        alert('Vui lòng nhập đầy đủ thông tin!');
        return;
    }

    const requestData = { name: name, email: email };
```

**Giải thích:**

1. Kiểm tra validation: Bắt buộc người dùng phải chọn Khoa và nhập đủ Họ tên, Email. Nếu để trống thì hiện hộp thoại cảnh báo `alert()` và dừng hàm.
2. `requestData`: Tạo một đối tượng JavaScript chứa dữ liệu cần gửi.

```javascript
    if (!id) {
        // THÊM MỚI (POST)
        fetch(`${API_URL}/faculties/${parentId}/students`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(requestData)
        })
        .then(response => response.json())
        .then(() => {
            resetForm();
            loadStudents(parentId);
        })
        .catch(err => alert('Lỗi thêm mới: ' + err));
    }
```

**Giải thích lệnh gửi POST:**

- `if (!id)`: Khi ô ẩn `studentId` rỗng $\to$ Đây là thao tác **Thêm mới**.
- `method: 'POST'`: Khai báo phương thức HTTP là POST (chuẩn RESTful để tạo mới dữ liệu).
- `headers: { 'Content-Type': 'application/json' }`: **Cực kỳ quan trọng!** Báo cho server Spring Boot biết rằng dữ liệu gửi lên ở phần body là chuỗi JSON. Nếu thiếu dòng này, server Spring Boot sẽ từ chối nhận và trả về lỗi **`415 Unsupported Media Type`**!
- `body: JSON.stringify(requestData)`: **Bắt buộc!** Chuyển đổi đối tượng JavaScript `{ name: "...", email: "..." }` thành chuỗi văn bản JSON `{"name":"...","email":"..."}` để truyền qua dây mạng.
- Sau khi thêm thành công: Gọi `resetForm()` để xóa trắng ô nhập và gọi `loadStudents(parentId)` để nạp lại dữ liệu bảng, sinh viên vừa thêm sẽ hiện ra ngay lập tức!

```javascript
    } else {
        // CẬP NHẬT (PUT)
        fetch(`${API_URL}/faculties/${parentId}/students/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(requestData)
        })
        .then(response => response.json())
        .then(() => {
            resetForm();
            loadStudents(parentId);
        })
        .catch(err => alert('Lỗi cập nhật: ' + err));
    }
}
```

**Giải thích lệnh gửi PUT:**

- Khi ô `studentId` có giá trị $\to$ Đây là thao tác **Sửa**.
- `method: 'PUT'`: Chuẩn RESTful để cập nhật dữ liệu có sẵn.
- Đường dẫn gửi lên có thêm ID sinh viên ở cuối: `/api/faculties/1/students/101`.

---

### Dòng 282 - 308: Thao tác giao diện Form (Đổ dữ liệu & Reset)

```javascript
function editStudent(id, name, email) {
    document.getElementById('studentId').value = id;
    document.getElementById('studentName').value = name;
    document.getElementById('studentEmail').value = email;
  
    document.getElementById('formTitle').innerText = 'Sửa thông tin (ID: ' + id + ')';
    document.getElementById('btnSave').innerText = 'Cập nhật';
    document.getElementById('btnCancel').style.display = 'inline-block';
}
```

- Đưa các giá trị `id`, `name`, `email` vào các ô input tương ứng.
- Đổi tiêu đề form thành "Sửa thông tin (ID: ...)".
- Đổi chữ trên nút lưu từ "Thêm" thành "Cập nhật".
- `style.display = 'inline-block'`: Làm hiện nút Hủy lên để nếu người dùng đổi ý không muốn sửa nữa thì có thể bấm Hủy.

```javascript
function resetForm() {
    document.getElementById('studentId').value = '';
    document.getElementById('studentName').value = '';
    document.getElementById('studentEmail').value = '';
    document.getElementById('formTitle').innerText = 'Thêm mới';
    document.getElementById('btnSave').innerText = 'Thêm';
    document.getElementById('btnCancel').style.display = 'none';
}
```

- Xóa sạch dữ liệu trong các ô input và ô ẩn `studentId`.
- Đổi lại tiêu đề "Thêm mới", nút "Thêm", và ẩn nút Hủy đi (`display = 'none'`).

---

### Dòng 310 - 325: BƯỚC 3 - Xóa sinh viên (DELETE)

```javascript
function deleteStudent(studentId) {
    const parentId = document.getElementById('facultySelect').value;
    if (!confirm('Bạn có chắc chắn muốn xóa ID ' + studentId + ' không?')) {
        return;
    }

    fetch(`${API_URL}/faculties/${parentId}/students/${studentId}`, {
        method: 'DELETE'
    })
    .then(() => {
        loadStudents(parentId);
    })
    .catch(err => alert('Lỗi xóa: ' + err));
}
```

- `confirm(...)`: Bật hộp thoại xác nhận Yes/No của trình duyệt. Nếu người dùng bấm "Cancel" (Hủy), hàm trả về `false` $\to$ lệnh `return;` dừng lại ngay lập tức, không xóa.
- `method: 'DELETE'`: Chuẩn RESTful để xóa dữ liệu.
- Sau khi server xóa xong, gọi `loadStudents(parentId)` để vẽ lại bảng, dòng vừa xóa sẽ biến mất.

---

# 3. GIẢI THÍCH CHI TIẾT TỪNG ANNOTATION & DÒNG CODE JAVA

File [FacultyController.java](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/bt/gk/src/main/java/com/example/gk/controller/FacultyController.java) là Web Service Backend.

## 3.1. Controller: `FacultyController.java`

```java
@RestController
@CrossOrigin(origins = "*")
public class FacultyController {
```

1. **`@RestController`**:
   - Là sự kết hợp của 2 annotation: `@Controller` + `@ResponseBody`.
   - **Tác dụng:** Mọi phương thức trong class này khi return dữ liệu (ví dụ return một `List<Student>`), Spring Boot sẽ dùng thư viện Jackson tự động chuyển đối tượng Java đó thành chuỗi JSON và bắn thẳng vào HTTP Body gửi về trình duyệt. Nó **không bao giờ tìm kiếm file giao diện HTML**.
2. **`@CrossOrigin(origins = "*")`**:
   - Giải quyết bài toán bảo mật **CORS (Cross-Origin Resource Sharing)**.
   - Khi frontend của bạn chạy ở một domain/port khác (ví dụ frontend chạy port 5500 bằng Live Server của VS Code, còn backend chạy port 8084), trình duyệt sẽ chặn không cho gọi API nếu server không bật CORS. Thêm dòng này cho phép gọi API từ bất kỳ đâu.

---

### Các Endpoint xử lý API:

#### 1. Chuyển hướng trình duyệt về giao diện chính:

```java
@GetMapping(value = {"/faculties", "/faculty"}, produces = MediaType.TEXT_HTML_VALUE)
public void redirectToHome(HttpServletResponse response) throws IOException {
    response.sendRedirect("/");
}
```

- `produces = MediaType.TEXT_HTML_VALUE`: Chỉ kích hoạt khi request đòi xem HTML (nghĩa là mở bằng thanh địa chỉ của trình duyệt Chrome/Edge).
- `response.sendRedirect("/")`: Gửi mã HTTP 302 chuyển hướng trình duyệt về `http://localhost:8084/` để mở file `index.html`. Giúp bạn không bao giờ bị lỗi 404 Whitelabel Error Page.

#### 2. Lấy danh sách Khoa (GET):

```java
@GetMapping(value = {"/api/faculties", "/faculties"}, produces = MediaType.APPLICATION_JSON_VALUE)
public List<Faculty> getAllFaculties() {
    return facultyService.getAllFaculties();
}
```

- `@GetMapping`: Tiếp nhận request phương thức `GET`.
- `produces = MediaType.APPLICATION_JSON_VALUE`: Báo rõ định dạng trả về là `application/json`.
- Trả về danh sách tất cả các khoa.

#### 3. Lấy danh sách Sinh viên & Tìm kiếm (GET):

```java
@GetMapping(value = {"/api/faculties/{facultyId}/students", "/faculties/{facultyId}/students"}, produces = MediaType.APPLICATION_JSON_VALUE)
public ResponseEntity<List<Student>> getStudents(
        @PathVariable("facultyId") Long facultyId,
        @RequestParam(name = "keyword", required = false) String keyword) {
```

- `{facultyId}` trong URL là một biến động (Path Variable).
- **`@PathVariable("facultyId") Long facultyId`**:
  - Trích xuất giá trị `{facultyId}` trên URL và ép kiểu thành biến `Long facultyId` trong Java.
  - **LƯU Ý CỰC KỲ QUAN TRỌNG:** Phải ghi rõ chữ `"facultyId"` trong ngoặc kép! Nếu bỏ ngoặc mà chỉ ghi `@PathVariable Long facultyId`, Spring Boot 3 trên một số bản Eclipse sẽ ném lỗi `java.lang.IllegalArgumentException: Name for argument not specified`.
- **`@RequestParam(name = "keyword", required = false) String keyword`**:
  - Đọc tham số tìm kiếm từ Query String trên URL (dạng `?keyword=abc`).
  - `required = false`: Tham số này không bắt buộc. Nếu người dùng không tìm kiếm (không truyền `?keyword=...`), biến `keyword` sẽ nhận giá trị `null` mà không gây lỗi.

#### 4. Thêm sinh viên mới (POST):

```java
@PostMapping(value = {"/api/faculties/{facultyId}/students", "/faculties/{facultyId}/students"})
public ResponseEntity<Student> addStudent(
        @PathVariable("facultyId") Long facultyId,
        @RequestBody Student student) {
    Optional<Student> created = facultyService.addStudentToFaculty(facultyId, student);
    return created.map(s -> ResponseEntity.status(HttpStatus.CREATED).body(s))
                  .orElse(ResponseEntity.notFound().build());
}
```

- `@PostMapping`: Tiếp nhận request phương thức `POST`.
- **`@RequestBody Student student`**: Lấy chuỗi JSON mà JavaScript gửi lên qua body (`JSON.stringify`), tự động chuyển đổi thành đối tượng Java `Student`.
- `HttpStatus.CREATED`: Trả về mã HTTP status code chuẩn `201 Created` (báo hiệu tạo mới thành công).

#### 5. Sửa sinh viên (PUT):

```java
@PutMapping(value = {"/api/faculties/{facultyId}/students/{studentId}", "/faculties/{facultyId}/students/{studentId}"})
public ResponseEntity<Student> updateStudent(
        @PathVariable("facultyId") Long facultyId,
        @PathVariable("studentId") Long studentId,
        @RequestBody Student student) {
```

- `@PutMapping`: Tiếp nhận request phương thức `PUT` để cập nhật dữ liệu.
- Nhận cả ID khoa (`facultyId`) và ID sinh viên cần sửa (`studentId`).

#### 6. Xóa sinh viên (DELETE):

```java
@DeleteMapping(value = {"/api/faculties/{facultyId}/students/{studentId}", "/faculties/{facultyId}/students/{studentId}"})
public ResponseEntity<Void> deleteStudent(
        @PathVariable("facultyId") Long facultyId,
        @PathVariable("studentId") Long studentId) {
    boolean deleted = facultyService.deleteStudentFromFaculty(facultyId, studentId);
    if (deleted) {
        return ResponseEntity.noContent().build(); // Trả về HTTP 204 No Content
    }
    return ResponseEntity.notFound().build();      // Trả về HTTP 404 Not Found
}
```

- `@DeleteMapping`: Tiếp nhận request phương thức `DELETE`.
- `ResponseEntity.noContent().build()`: Trả về mã HTTP `204 No Content` (chuẩn RESTful báo hiệu đã xóa thành công và không có nội dung body trả về).

---

## 3.2. Cấu hình Compiler trong `pom.xml`

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
        <parameters>true</parameters>
    </configuration>
</plugin>
```

- Cờ `<parameters>true</parameters>` ép trình biên dịch Java lưu lại tên tham số của các hàm vào file `.class`. Giúp Spring Boot đọc được tên tham số qua reflection trên mọi phiên bản Eclipse cũ/mới mà không bao giờ bị lỗi.

---

# 4. BỘ 15 CÂU HỎI VẤN ĐÁP THẦY HAY HỎI KHI CHẤM THI

Dưới đây là 15 câu hỏi thầy rất hay hỏi khi đứng chấm bài trực tiếp tại máy thi, kèm theo câu trả lời mẫu ngắn gọn, chính xác:

---

### ❓ Câu 1: Em hãy giải thích luồng hoạt động của ứng dụng từ lúc mở trang đến khi hiện dữ liệu?

> **Trả lời:**"Dạ thưa thầy, khi mở trang web:
>
> 1. Trình duyệt tải xong file HTML thì sự kiện `window.onload` kích hoạt hàm `loadFaculties()`.
> 2. Hàm này dùng `fetch('/api/faculties')` gửi request GET lên Web Service Backend.
> 3. Backend trả về mảng JSON các Khoa. JavaScript nhận được dữ liệu và duyệt vòng lặp `forEach` để thêm các thẻ `<option>` vào combobox `<select>`.
> 4. Khi người dùng click chọn 1 Khoa, sự kiện `onchange` kích hoạt hàm `loadStudents()`. Hàm này gửi tiếp request GET `/api/faculties/{id}/students` để lấy danh sách sinh viên của khoa đó và gọi hàm `renderTable()` vẽ vào thẻ `<tbody>` mà không hề tải lại trang ạ."

---

### ❓ Câu 2: Tại sao lệnh `fetch()` lại có 2 lần `.then()`?

> **Trả lời:**"Dạ thưa thầy:
>
> - Lần `.then()` thứ nhất nhận về đối tượng `response` ở dạng luồng stream dữ liệu mạng. Phương thức `response.json()` là một tác vụ bất đồng bộ đọc toàn bộ body và parse chuỗi văn bản JSON thành đối tượng JavaScript.
> - Lần `.then()` thứ hai mới thực sự nhận được dữ liệu JavaScript đã giải mã xong để mang đi xử lý đổ lên giao diện ạ."

---

### ❓ Câu 3: `@RestController` khác gì `@Controller` thông thường?

> **Trả lời:**"Dạ thưa thầy:
>
> - `@Controller` thông thường dùng cho mô hình MVC truyền thống, khi return một chuỗi String (ví dụ `return "index"`), Spring Boot sẽ tìm file giao diện template `index.html` để render ra HTML.
> - `@RestController` là sự kết hợp của `@Controller` và `@ResponseBody`. Mọi phương thức trả về dữ liệu thô (chuỗi JSON), bắn thẳng vào HTTP body chứ không tìm kiếm file giao diện HTML ạ."

---

### ❓ Câu 4: `@CrossOrigin(origins = "*")` để làm gì? Nếu không có dòng này thì sao?

> **Trả lời:**
> "Dạ thưa thầy, đây là cấu hình giải quyết chính sách bảo mật CORS (Cross-Origin Resource Sharing). Nếu frontend và backend chạy ở 2 cổng (port) khác nhau hoặc 2 domain khác nhau, trình duyệt sẽ tự động chặn request API lại vì lý do an toàn. Thêm `@CrossOrigin(origins = "*")` để báo cho trình duyệt biết server cho phép mọi nguồn được gọi API này ạ."

---

### ❓ Câu 5: Tại sao trong `@PathVariable("id")` lại phải ghi rõ chữ `"id"` trong ngoặc kép?

> **Trả lời:**
> "Dạ thưa thầy, từ Spring Boot 3 (Spring Framework 6), cơ chế tự đoán tên biến qua reflection đã bị lược bỏ. Nếu không ghi rõ tên `"id"` trong ngoặc mà trình biên dịch javac không bật cờ `-parameters`, Spring sẽ không biết biến này tương ứng với phần nào trên URL và ném ra lỗi `IllegalArgumentException` ạ."

---

### ❓ Câu 6: `@PathVariable` khác gì `@RequestParam`?

> **Trả lời:**"Dạ thưa thầy:
>
> - `@PathVariable`: Dùng để lấy giá trị là một phần trực tiếp của đường dẫn URL (Path Segment), ví dụ `/api/faculties/{facultyId}/students` thì `facultyId` là Path Variable.
> - `@RequestParam`: Dùng để lấy tham số nằm sau dấu chấm hỏi trên URL (Query Parameter), ví dụ `/api/faculties/1/students?keyword=An` thì `keyword` là Request Param ạ."

---

### ❓ Câu 7: Khi gửi dữ liệu Thêm mới bằng `fetch`, tại sao phải dùng `JSON.stringify()`?

> **Trả lời:**
> "Dạ thưa thầy, biến dữ liệu trong JavaScript là một đối tượng nằm trong bộ nhớ RAM của trình duyệt. Giao thức HTTP chỉ truyền được dữ liệu dạng chuỗi văn bản (String) qua đường mạng. Lệnh `JSON.stringify()` có nhiệm vụ chuyển đổi đối tượng JavaScript thành chuỗi văn bản chuẩn JSON để gửi đi ạ."

---

### ❓ Câu 8: Header `headers: { 'Content-Type': 'application/json' }` có ý nghĩa gì? Nếu thiếu thì bị lỗi gì?

> **Trả lời:**
> "Dạ thưa thầy, header này báo cho server Spring Boot biết rằng định dạng dữ liệu ở phần Body là JSON. Nếu thiếu header này, server sẽ không biết dùng thư viện Jackson để đọc dữ liệu và trả về lỗi HTTP **415 Unsupported Media Type** ạ."

---

### ❓ Câu 9: Thẻ `<input type="hidden" id="studentId">` dùng để làm gì?

> **Trả lời:**"Dạ thưa thầy, đây là kỹ thuật dùng chung 1 form cho cả Thêm mới và Sửa:
>
> - Khi người dùng bấm Thêm mới, ô `studentId` rỗng $\to$ code sẽ gửi request `POST`.
> - Khi người dùng bấm nút Sửa ở bảng, hàm `editStudent` sẽ gán ID của sinh viên vào ô ẩn này. Khi bấm nút lưu, code thấy `studentId` có giá trị $\to$ gửi request `PUT` kèm theo ID đó để cập nhật ạ."

---

### ❓ Câu 10: Tại sao em chọn dùng nút bấm Tìm kiếm (`onclick`) thay vì gõ phím đến đâu tìm đến đó (`onkeyup`)?

> **Trả lời:**"Dạ thưa thầy:
>
> 1. **Về mặt hiệu năng mạng:** Nếu dùng `onkeyup`, mỗi khi người dùng gõ một ký tự (ví dụ gõ từ khóa 8 chữ cái), trình duyệt sẽ bắn liên tục 8 request bất đồng bộ lên server. Nếu không cài đặt kỹ thuật Debounce (chờ người dùng dừng gõ) thì server rất dễ bị quá tải (spam request) và có nguy cơ lỗi Race Condition (kết quả request trước về sau request sau).
> 2. **Về mặt kiến trúc Web Service:** Dùng nút bấm giúp người dùng hoàn tất từ khóa rồi mới gửi **duy nhất 1 request GET**, vừa tiết kiệm băng thông mạng, vừa đúng chuẩn nghiệp vụ truy vấn dữ liệu ạ."

---

### ❓ Câu 11: Hàm `encodeURIComponent()` trong hàm tìm kiếm có tác dụng gì?

> **Trả lời:**
> "Dạ thưa thầy, hàm này dùng để mã hóa các ký tự đặc biệt (khoảng trắng, dấu tiếng Việt, dấu `&`, `?`) thành định dạng mã an toàn trên URL (ví dụ khoảng trắng thành `%20`). Nó giúp đường dẫn URL không bị vỡ hoặc lỗi khi người dùng gõ từ khóa tìm kiếm có dấu tiếng Việt ạ."

---

### ❓ Câu 12: Các phương thức HTTP GET, POST, PUT, DELETE trong bài này được dùng làm gì?

> **Trả lời:**"Dạ thưa thầy, đây là 4 phương thức chuẩn của kiến trúc RESTful:
>
> - `GET`: Dùng để truy vấn, đọc dữ liệu (lấy danh sách Khoa, danh sách Sinh viên).
> - `POST`: Dùng để tạo mới một bản ghi (thêm sinh viên mới).
> - `PUT`: Dùng để cập nhật, chỉnh sửa thông tin bản ghi có sẵn (sửa sinh viên).
> - `DELETE`: Dùng để xóa bỏ bản ghi (xóa sinh viên) ạ."

---

### ❓ Câu 13: Các mã trạng thái HTTP (Status Code) 200, 201, 204, 404, 500 nghĩa là gì?

> **Trả lời:**"Dạ thưa thầy:
>
> - `200 OK`: Yêu cầu thành công, có dữ liệu trả về (dùng cho GET, PUT).
> - `201 Created`: Tạo mới dữ liệu thành công trên server (dùng cho POST).
> - `204 No Content`: Thao tác thành công nhưng không có nội dung body trả về (thường dùng cho DELETE).
> - `404 Not Found`: Không tìm thấy tài nguyên hoặc sai đường dẫn URL.
> - `500 Internal Server Error`: Lỗi code xảy ra bên trong server backend ạ."

---

### ❓ Câu 14: SPA (Single Page Application) là gì? Điều gì trong bài chứng minh đây là SPA?

> **Trả lời:**
> "Dạ thưa thầy, SPA là ứng dụng web chỉ có duy nhất 1 trang HTML. Khi người dùng thao tác chọn combobox, tìm kiếm, thêm, sửa, xóa, trang web hoàn toàn không bị tải lại (không F5, không nhấp nháy). Toàn bộ dữ liệu được cập nhật ngầm qua JavaScript `fetch` và DOM manipulation vẽ lại thẻ `<tbody>` tại chỗ ạ."

---

### ❓ Câu 15: Hàm `confirm()` trong JavaScript trả về kiểu dữ liệu gì?

> **Trả lời:**"Dạ thưa thầy, hàm `confirm()` bật popup xác nhận và trả về kiểu dữ liệu `boolean`:
>
> - Nếu người dùng bấm `OK` $\to$ trả về `true`.
> - Nếu người dùng bấm `Cancel` $\to$ trả về `false`.
>   Đoạn code `if (!confirm(...)) return;` có nghĩa là nếu người dùng bấm Cancel thì thoát hàm ngay, không gửi request xóa lên server ạ."

---

# 5. CẨM NANG ỨNG BIẾN TRONG 2 PHÚT KHI ĐỀ THI ĐỔI DỮ LIỆU

Bất kỳ đề thi nào cũng tuân theo **mô hình duy nhất: 1 Cha - Nhiều Con (1 - N)**.

### Ví dụ: Đề đổi thành "Danh mục (Category) & Sản phẩm (Product)" có thuộc tính `id`, `name`, `price`:

Bạn mở file `index.html` lên và sửa đúng **5 vị trí** sau:

1. **Sửa tiêu đề & nhãn:**

   - Đổi chữ "Khoa" $\to$ "Danh mục".
   - Đổi nhãn ô "Email" $\to$ "Đơn giá": `<input type="number" id="studentEmail" placeholder="Nhập giá...">`.
   - Đổi cột tiêu đề bảng "Email" $\to$ "Đơn giá".
2. **Sửa URL trong hàm `loadFaculties()`:**

   ```javascript
   // Đổi /faculties thành /categories
   fetch(`${API_URL}/categories`)
   ```
3. **Sửa URL trong hàm `loadStudents()`:**

   ```javascript
   // Đổi /faculties/.../students thành /categories/.../products
   let url = `${API_URL}/categories/${parentId}/products`;
   ```
4. **Sửa thuộc tính hiển thị trong `renderTable()`:**

   ```javascript
   // Đổi s.email thành s.price
   html += `
       <tr>
           <td>${s.id}</td>
           <td>${s.name}</td>
           <td>${s.price} VNĐ</td>
           <td>
               <button onclick="editStudent(${s.id}, '${s.name}', '${s.price}')">Sửa</button>
               <button onclick="deleteStudent(${s.id})">Xóa</button>
           </td>
       </tr>
   `;
   ```
5. **Sửa đóng gói JSON trong `saveStudent()`:**

   ```javascript
   // Đổi email thành price
   const requestData = { 
       name: name, 
       price: parseFloat(email) // Ép kiểu số thực cho đơn giá
   };

   // URL POST và PUT: đổi sang categories/.../products
   fetch(`${API_URL}/categories/${parentId}/products`, ...)
   ```

---

# 6. XỬ LÝ 4 LỖI KINH ĐIỂN TRONG PHÒNG THI

1. **Mở web lên combobox trắng tinh, không hiện gì:**

   - Mở **F12** $\to$ tab **Console**.
   - Nếu thấy đỏ lòm `net::ERR_CONNECTION_REFUSED`: Do chưa bấm Run backend Spring Boot hoặc link API bị sai cổng.
   - Nếu server của thầy chạy port 8080: Đổi dòng đầu thẻ `<script>` thành:
     `const API_URL = 'http://localhost:8080/api';`
2. **Bấm chọn Khoa nhưng bảng không hiện Sinh viên:**

   - Mở **F12** $\to$ tab **Network** $\to$ click vào dòng request vừa gửi $\to$ chọn tab **Response**.
   - Nhìn xem tên thuộc tính JSON thầy trả về là gì (ví dụ thầy đặt là `fullName` thay vì `name`, `cost` thay vì `price`).
   - Sửa lại đúng tên biến trong hàm `renderTable()` (`s.fullName`, `s.cost`).
3. **Bấm Thêm mới bị báo lỗi HTTP 415:**

   - Do quên header JSON. Thêm vào hàm `fetch`:
     `headers: { 'Content-Type': 'application/json' }`
4. **Bấm Thêm mới bị báo lỗi HTTP 400 Bad Request:**

   - Do quên `JSON.stringify(requestData)`. Đảm bảo body là chuỗi text đã được stringify.

---

*Tài liệu được biên soạn phục vụ kỳ thi Giữa Kỳ môn Xây dựng website hướng dịch vụ - IUH.*
