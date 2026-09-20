# ĐỀ CƯƠNG ÔN TẬP TOÀN DIỆN THI GIỮA KỲ (LÝ THUYẾT & THỰC HÀNH)
**Học phần:** Xây dựng website hướng dịch vụ (Web Services) - IUH  
**Dành cho kỳ thi:** Thi Giữa Kỳ (3 ngày tới)  
**Phạm vi:** Trọng tâm 3 bước chuẩn theo video thầy dặn

---

# 📖 PHẦN 1: LÝ THUYẾT CỐT LÕI (BẮT BUỘC PHẢI THUỘC)

## 1. Web Service (Dịch vụ Web) là gì?
* **Định nghĩa:** Web Service là một thành phần phần mềm cung cấp các dịch vụ/dữ liệu cho các ứng dụng khác thông qua mạng Internet dựa trên các giao thức web tiêu chuẩn (HTTP/HTTPS).
* **Đặc điểm sống còn:** 
  - **Độc lập nền tảng và ngôn ngữ:** Backend viết bằng Java Spring Boot, C# .NET, hay Python thì Frontend (JavaScript, Android, iOS) đều gọi được.
  - **Không trả về giao diện HTML:** Web Service **chỉ trả về dữ liệu thô (raw data)**, phổ biến nhất hiện nay là định dạng **JSON (JavaScript Object Notation)**.

---

## 2. So sánh Web MVC truyền thống và Web Service (SPA)

Đây là câu hỏi lý thuyết kinh điển thầy rất hay hỏi:

| Tiêu chí so sánh | Web MVC truyền thống (Thymeleaf / JSP) | Web Service + Single Page (REST API) |
| :--- | :--- | :--- |
| **Bản chất** | Server-Side Rendering (SSR) | Client-Side Rendering (CSR / SPA) |
| **Dữ liệu Server trả về** | **Toàn bộ trang HTML hoàn chỉnh** (gồm CSS, cấu trúc trang) | **Chỉ trả về Dữ liệu thô dạng JSON** (không có HTML) |
| **Trải nghiệm thao tác** | Mỗi lần bấm Thêm/Sửa/Xóa $\to$ trình duyệt chớp trắng và **tải lại toàn bộ trang** (F5 / reload). | **Không tải lại trang**; JavaScript tự nhận JSON và cập nhật đúng vị trí trên màn hình. |
| **Băng thông mạng** | Tốn băng thông vì phải truyền đi truyền lại toàn bộ khung HTML. | Cực kỳ tiết kiệm băng thông vì chỉ truyền gói tin JSON vài kilobyte. |
| **Tái sử dụng** | Chỉ dùng được cho trình duyệt Web. | **Dùng chung 1 Backend** cho cả Website, Ứng dụng Di động (Mobile App), hệ thống đối tác. |

---

## 3. Các phương thức HTTP (HTTP Methods) trong RESTful API

Khi giao tiếp với Web Service, chúng ta dùng các động từ HTTP tương ứng với từng tác vụ CRUD:

| Tác vụ CRUD | HTTP Method | Endpoint mẫu | Mô tả hoạt động |
| :--- | :---: | :--- | :--- |
| **R**ead (Xem/Lấy) | **GET** | `/api/faculties` | Lấy danh sách khoa hoặc sinh viên. Không có Request Body. |
| **C**reate (Thêm mới) | **POST** | `/api/faculties/{id}/students` | Tạo mới sinh viên. **Bắt buộc gửi dữ liệu JSON trong Request Body**. |
| **U**pdate (Cập nhật) | **PUT** | `/api/faculties/{id}/students/{sId}` | Thay thế/Cập nhật sinh viên. **Bắt buộc gửi JSON trong Request Body**. |
| **D**elete (Xóa) | **DELETE** | `/api/faculties/{id}/students/{sId}` | Xóa sinh viên khỏi hệ thống. Không cần Request Body. |

---

## 4. Các mã trạng thái HTTP (HTTP Status Codes) cần biết

* **`200 OK`**: Gọi API thành công, dữ liệu được trả về (thường gặp ở `GET`, `PUT`).
* **`201 Created`**: Tạo mới tài nguyên thành công (thường gặp ở `POST`).
* **`204 No Content`**: Thao tác thành công nhưng không có dữ liệu trả về (thường gặp ở `DELETE`).
* **`400 Bad Request`**: Dữ liệu gửi lên sai định dạng (ví dụ thiếu trường, JSON lỗi cú pháp).
* **`404 Not Found`**: Sai đường dẫn URL hoặc không tìm thấy ID cần tìm.
* **`500 Internal Server Error`**: Lỗi logic bên trong mã nguồn backend của server.

---

# 💻 PHẦN 2: "BẢNG MẪU CODE PHAO" JAVASCRIPT GỌI WEB SERVICE (FETCH API)

> **Khi đi thi:** Thầy đã cấp sẵn Web Service. Bạn chỉ cần mở file HTML và viết đoạn JavaScript dưới đây là ăn trọn điểm!

### 🔹 MẪU 1: GỌI `GET` LẤY DỮ LIỆU ĐỔ VÀO COMBOBOX (`<select>`) - [BƯỚC 1]
```javascript
// Gọi API lấy danh sách Khoa đổ vào thẻ <select id="facultySelect">
async function loadFaculties() {
    try {
        const res = await fetch('http://localhost:8084/api/faculties');
        const faculties = await res.json(); // Chuyển kết quả sang mảng JavaScript

        const select = document.getElementById('facultySelect');
        select.innerHTML = '<option value="">-- Chọn Khoa --</option>';

        faculties.forEach(f => {
            const opt = document.createElement('option');
            opt.value = f.id;     // Lưu ID khoa vào value
            opt.textContent = f.name; // Hiển thị tên khoa
            select.appendChild(opt);
        });
    } catch (err) {
        console.error('Lỗi tải khoa:', err);
    }
}
```

---

### 🔹 MẪU 2: SỰ KIỆN `onchange` CỦA COMBOBOX GỌI `GET` ĐỔ VÀO TABLE (`<table>`) - [BƯỚC 2]
```javascript
// Khi người dùng chọn 1 khoa trong combobox -> Hàm này được kích hoạt
async function onFacultyChange() {
    const facultyId = document.getElementById('facultySelect').value;
    if (!facultyId) return;

    try {
        const res = await fetch(`http://localhost:8084/api/faculties/${facultyId}/students`);
        const students = await res.json();

        const tbody = document.getElementById('studentTableBody');
        tbody.innerHTML = ''; // Xóa danh sách cũ

        students.forEach(s => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${s.id}</td>
                <td>${s.name}</td>
                <td>${s.email}</td>
                <td>
                    <button onclick="editStudent(${s.id}, '${s.name}', '${s.email}')">Sửa</button>
                    <button onclick="deleteStudent(${s.id})">Xóa</button>
                </td>
            `;
            tbody.appendChild(tr);
        });
    } catch (err) {
        console.error('Lỗi tải sinh viên:', err);
    }
}
```

---

### 🔹 MẪU 3: THÊM MỚI BẰNG `POST` (CRUD) - [BƯỚC 3]
```javascript
async function createStudent() {
    const facultyId = document.getElementById('facultySelect').value;
    const name = document.getElementById('studentName').value;
    const email = document.getElementById('studentEmail').value;

    const data = { name: name, email: email };

    try {
        const res = await fetch(`http://localhost:8084/api/faculties/${facultyId}/students`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // BẮT BUỘC PHẢI CÓ DÒNG NÀY!
            },
            body: JSON.stringify(data) // Chuyển object sang chuỗi JSON
        });

        if (res.ok) {
            alert('Thêm thành công!');
            onFacultyChange(); // Gọi lại hàm load Table để cập nhật danh sách
        }
    } catch (err) {
        console.error('Lỗi thêm:', err);
    }
}
```

---

### 🔹 MẪU 4: CẬP NHẬT BẰNG `PUT` (CRUD) - [BƯỚC 3]
```javascript
async function updateStudent(studentId) {
    const facultyId = document.getElementById('facultySelect').value;
    const name = document.getElementById('studentName').value;
    const email = document.getElementById('studentEmail').value;

    const data = { name: name, email: email };

    try {
        const res = await fetch(`http://localhost:8084/api/faculties/${facultyId}/students/${studentId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        if (res.ok) {
            alert('Cập nhật thành công!');
            onFacultyChange(); // Cập nhật lại Table
        }
    } catch (err) {
        console.error('Lỗi cập nhật:', err);
    }
}
```

---

### 🔹 MẪU 5: XÓA BẰNG `DELETE` (CRUD) - [BƯỚC 3]
```javascript
async function deleteStudent(studentId) {
    if (!confirm('Bạn có chắc muốn xóa sinh viên này?')) return;

    const facultyId = document.getElementById('facultySelect').value;

    try {
        const res = await fetch(`http://localhost:8084/api/faculties/${facultyId}/students/${studentId}`, {
            method: 'DELETE'
        });

        if (res.ok) {
            alert('Đã xóa thành công!');
            onFacultyChange(); // Cập nhật lại Table
        }
    } catch (err) {
        console.error('Lỗi xóa:', err);
    }
}
```

---

# ⚠️ PHẦN 3: 4 BẪY LỖI KINH ĐIỂN TRONG PHÒNG THI & CÁCH XỬ LÝ

1. **Bẫy 1: Quên header `'Content-Type': 'application/json'` khi gửi POST/PUT**
   * *Triệu chứng:* Server trả về mã lỗi `415 Unsupported Media Type` hoặc đối tượng nhận được ở backend bị `null`.
   * *Khắc phục:* Luôn luôn thêm `headers: { 'Content-Type': 'application/json' }` vào tùy chọn của `fetch`.

2. **Bẫy 2: Quên `JSON.stringify(data)`**
   * *Triệu chứng:* Gửi body là object JavaScript nguyên thủy `{name: "An"}` $\to$ Server nhận chuỗi `[object Object]` dẫn đến lỗi `400 Bad Request`.
   * *Khắc phục:* Bắt buộc phải bọc bằng `JSON.stringify(...)`.

3. **Bẫy 3: Quên `await` khi đọc `.json()`**
   * *Triệu chứng:* In kết quả ra thấy `Promise {<pending>}` thay vì mảng danh sách.
   * *Khắc phục:* Viết đúng `const data = await res.json();` bên trong hàm có từ khóa `async`.

4. **Bẫy 4: Thêm/Sửa/Xóa xong không cập nhật lại Table**
   * *Triệu chứng:* Thầy bấm nút Xóa thấy báo thành công nhưng dòng đó vẫn nằm trơ trơ trên màn hình (vì chưa vẽ lại Table).
   * *Khắc phục:* Sau khi `res.ok`, gọi ngay hàm load Table: `onFacultyChange();` hoặc `loadStudentsByFaculty(facultyId);`.

---

# 🎯 PHẦN 4: THỰC HÀNH TEST NGAY TẠI NHÀ TRÊN MÁY TÍNH CỦA BẠN

Dự án `d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\gk` đã được tôi cài đặt sẵn toàn bộ:
* **Backend Web Service:** `FacultyRestController.java` (đúng các API mà thầy sẽ cho lúc thi).
* **Giao diện Single Page:** `src/main/resources/templates/spa.html` và `src/main/resources/static/index.html`.

### Cách chạy kiểm thử:
1. Mở terminal, chạy lệnh khởi động Spring Boot:
   ```bash
   ./mvnw spring-boot:run
   ```
   *(Hoặc trong Eclipse: chuột phải vào `GkApplication.java` $\to$ Run As $\to$ Spring Boot App).*
2. Mở trình duyệt (Chrome/Edge), truy cập:
   👉 **`http://localhost:8084/`** hoặc **`http://localhost:8084/spa`**
3. Bạn sẽ thấy ngay giao diện chuẩn 3 bước:
   - Danh sách Khoa tự động hiện trong Combobox.
   - Chọn Khoa $\to$ Bảng Table hiện danh sách sinh viên.
   - Bấm Thêm mới, Sửa, Xóa thử nghiệm trực tiếp mượt mà 100%!
