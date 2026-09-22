# CẨM NANG ÔN THI GIỮA KỲ & GIẢI THÍCH CHI TIẾT TOÀN BỘ CODE
**Môn học:** Xây dựng website hướng dịch vụ (IUH)  
**Giảng viên phụ trách:** Trương Bá Phúc  
**Mô hình bài thi:** Single Page Application (SPA) kết hợp Web Service (REST API)  

---

## 📑 MỤC LỤC
1. [Bản chất bài thi giữa kỳ & Lời dặn dò của thầy](#1-bản-chất-bài-thi-giữa-kỳ)
2. [Giải thích chi tiết các file Java (Backend Web Service)](#2-giải-thích-chi-tiết-các-file-java-backend)
   - [2.1. Model: `Faculty.java` & `Student.java`](#21-model-facultyjava--studentjava)
   - [2.2. Service: `FacultyService.java`](#22-service-facultyservicejava)
   - [2.3. Controller: `FacultyController.java`](#23-controller-facultycontrollerjava)
   - [2.4. Cấu hình: `pom.xml`, `application.properties`, `GkApplication.java`](#24-cấu-hình-pomxml-applicationproperties-gkapplicationjava)
3. [Giải thích chi tiết từng dòng code trong file `index.html` (Frontend SPA)](#3-giải-thích-chi-tiết-từng-dòng-code-trong-indexhtml)
   - [3.1. Cấu trúc HTML & CSS](#31-cấu-trúc-html--css)
   - [3.2. Cơ chế gọi API và xử lý dữ liệu bằng JavaScript](#32-cơ-chế-gọi-api-và-xử-lý-dữ-liệu-bằng-javascript)
4. [Cẩm nang ứng biến trong phòng thi khi đề bài cho dữ liệu khác](#4-cẩm-nang-ứng-biến-khi-đề-thi-thay-đổi-dữ-liệu)
   - [4.1. Bảng ma trận thay thế 4 đề tài kinh điển](#41-bảng-ma-trận-thay-thế-4-đề-tài-kinh-điển)
   - [4.2. Hướng dẫn sửa `index.html` trong 2 phút theo đề mới](#42-hướng-dẫn-sửa-indexhtml-trong-2-phút-theo-đề-mới)
5. [Các lỗi thường gặp trong phòng thi & cách khắc phục tức thì](#5-các-lỗi-thường-gặp--cách-khắc-phục)

---

# 1. BẢN CHẤT BÀI THI GIỮA KỲ

### 1.1. Sự khác biệt cốt lõi: SPA vs MVC truyền thống
- **Bài cũ (Spring MVC + Thymeleaf):** Mỗi khi bấm Thêm/Sửa/Xóa, trình duyệt gửi dữ liệu lên server, server render lại toàn bộ trang HTML mới và redirect (`return "redirect:/faculties"`). Trang web bị chớp/tải lại (F5).
- **Bài thi Giữa Kỳ (Web Service + SPA):**
  - Web Service **KHÔNG BAO GIỜ TRẢ VỀ HTML**, mà trả về **DỮ LIỆU THÔ DẠNG JSON**.
  - Giao diện người dùng là **1 file HTML duy nhất (Single Page)**.
  - Sử dụng **JavaScript (`fetch()`)** để âm thầm gọi Web Service lấy JSON về, sau đó dùng DOM Javascript để vẽ lại bảng table **mà không tải lại trang**.

### 1.2. Quy chế thi giữa kỳ (Lời thầy dặn trong video):
1. **Phạm vi thi: Đúng 3 bước đầu (BỎ Paging & Sorting)**:
   - **Bước 1:** Đổ danh sách đối tượng Cha (Khoa) vào Combobox (`<select>`).
   - **Bước 2:** Bắt sự kiện chọn item trong Combobox (`onchange`) $\to$ gọi Web Service lấy JSON danh sách Con (Sinh viên) $\to$ đổ vào Table (`<table>`).
   - **Bước 3:** Đầy đủ bộ CRUD Thêm mới, Sửa, Xóa, Tìm kiếm qua Web Service.
   - *(Bước 4 & 5 Phân trang, Sắp xếp dành cho thi Cuối kỳ, Giữa kỳ KHÔNG thi)*.
2. **Lúc thi, thầy sẽ cung cấp Web Service:**
   - Bạn chỉ cần tập trung 100% sức lực vào file giao diện HTML + JavaScript.
   - Dự án Spring Boot này được viết sẵn để bạn có Backend chạy tại chỗ luyện tập ở nhà hoặc dự phòng nếu thầy yêu cầu tự chạy Backend.

---

# 2. GIẢI THÍCH CHI TIẾT CÁC FILE JAVA (BACKEND)

## 2.1. Model: `Faculty.java` & `Student.java`
Đây là 2 class định nghĩa cấu trúc dữ liệu theo quan hệ **1 - N (1 Khoa chứa nhiều Sinh viên)**.

### `Student.java`
```java
public class Student {
    private Long id;       // Mã định danh duy nhất của sinh viên
    private String name;   // Họ và tên
    private String email;  // Địa chỉ email
    // ... Constructor không đối số, Constructor có đối số, Getter & Setter
}
```
- Sử dụng kiểu dữ liệu `Long` cho `id` để phù hợp với chuẩn cơ sở dữ liệu khóa chính tự tăng.

### `Faculty.java`
```java
public class Faculty {
    private Long id;                               // Mã khoa
    private String name;                           // Tên khoa
    private List<Student> students = new ArrayList<>(); // Danh sách sinh viên thuộc khoa
    // ... Constructor, Getter & Setter
}
```
- Khởi tạo sẵn `new ArrayList<>()` để tránh lỗi `NullPointerException` khi thêm sinh viên vào khoa.

---

## 2.2. Service: `FacultyService.java`
Đóng vai trò là "Kho dữ liệu và Nghiệp vụ" (Database giả lập lưu trong bộ nhớ RAM).

```java
@Service
public class FacultyService {
    // Sử dụng CopyOnWriteArrayList để an toàn khi nhiều luồng truy cập đồng thời
    private final List<Faculty> faculties = new CopyOnWriteArrayList<>();
    // Bộ sinh ID tự tăng an toàn luồng
    private final AtomicLong facultyIdGenerator = new AtomicLong(3);
    private final AtomicLong studentIdGenerator = new AtomicLong(301);
```
- **Hàm khởi tạo (`FacultyService()`):** Khởi tạo sẵn 3 Khoa mẫu (*Công Nghệ Thông Tin*, *Kỹ Thuật Cơ Khí*, *Quản Trị Kinh Doanh*) kèm theo danh sách sinh viên ban đầu để khi mở web lên là có dữ liệu hiển thị ngay lập tức.
- **Các hàm nghiệp vụ chính:**
  - `getAllFaculties()`: Trả về danh sách tất cả các khoa.
  - `getStudentsByFacultyId(Long facultyId)`: Lọc ra khoa theo ID và lấy danh sách sinh viên của khoa đó.
  - `searchStudents(Long facultyId, String keyword)`: Tìm kiếm sinh viên theo tên hoặc email (không phân biệt hoa thường) trong phạm vi khoa được chọn.
  - `addStudentToFaculty(Long facultyId, Student student)`: Tự động cấp phát ID mới cho sinh viên bằng `studentIdGenerator.incrementAndGet()` và thêm vào khoa.
  - `updateStudent(...)`: Cập nhật tên và email mới cho sinh viên.
  - `deleteStudentFromFaculty(...)`: Xóa sinh viên khỏi khoa bằng `removeIf()`.

---

## 2.3. Controller: `FacultyController.java`
Đóng vai trò là **Web Service (REST API Endpoint)**, tiếp nhận các HTTP Request từ trình duyệt và trả về JSON.

```java
@RestController
@CrossOrigin(origins = "*") // Tránh lỗi CORS nếu frontend chạy từ cổng khác
public class FacultyController {
```
- `@RestController`: Kết hợp giữa `@Controller` và `@ResponseBody`, báo cho Spring Boot biết rằng mọi phương thức trong controller này đều trả về dữ liệu thô (JSON/Text), không tìm kiếm template HTML.
- `@CrossOrigin(origins = "*")`: Cho phép mọi nguồn (khác port, khác IP) gọi API mà không bị trình duyệt chặn CORS.

### Các Endpoint xử lý:
1. **Tự động chuyển hướng về trang chủ khi mở bằng trình duyệt:**
   ```java
   @GetMapping(value = {"/faculties", "/faculty"}, produces = MediaType.TEXT_HTML_VALUE)
   public void redirectToHome(HttpServletResponse response) throws IOException {
       response.sendRedirect("/");
   }
   ```
   *Tác dụng:* Nếu người dùng gõ nhầm đường dẫn cũ `http://localhost:8084/faculties`, server tự động chuyển về `http://localhost:8084/` để hiển thị giao diện SPA, không bao giờ bị lỗi `404 Whitelabel Error Page`.

2. **Lấy danh sách Khoa (Bước 1):**
   ```java
   @GetMapping(value = {"/api/faculties", "/faculties"}, produces = MediaType.APPLICATION_JSON_VALUE)
   public List<Faculty> getAllFaculties() {
       return facultyService.getAllFaculties();
   }
   ```
   *Phương thức:* `GET`. Trả về mảng JSON chứa các khoa: `[{"id":1,"name":"Công Nghệ Thông Tin"},...]`.

3. **Lấy danh sách Sinh viên & Tìm kiếm (Bước 2):**
   ```java
   @GetMapping(value = {"/api/faculties/{facultyId}/students", "/faculties/{facultyId}/students"}, produces = MediaType.APPLICATION_JSON_VALUE)
   public ResponseEntity<List<Student>> getStudents(
           @PathVariable("facultyId") Long facultyId,
           @RequestParam(name = "keyword", required = false) String keyword) {
   ```
   *Lưu ý sống còn:* Phải ghi rõ `@PathVariable("facultyId")` (có tên trong ngoặc kép). Nếu chỉ ghi `@PathVariable Long facultyId`, Spring Boot 3 trên một số bản Eclipse sẽ không đọc được tên biến và ném lỗi `IllegalArgumentException`.

4. **Thêm sinh viên mới (Bước 3):**
   ```java
   @PostMapping(value = {"/api/faculties/{facultyId}/students", "/faculties/{facultyId}/students"})
   public ResponseEntity<Student> addStudent(
           @PathVariable("facultyId") Long facultyId,
           @RequestBody Student student) {
   ```
   *Phương thức:* `POST`. `@RequestBody` nhận dữ liệu JSON gửi lên từ Javascript và tự động parse thành đối tượng Java `Student`. Trả về mã HTTP `201 CREATED`.

5. **Sửa sinh viên (Bước 3):**
   ```java
   @PutMapping(value = {"/api/faculties/{facultyId}/students/{studentId}", "/faculties/{facultyId}/students/{studentId}"})
   public ResponseEntity<Student> updateStudent(
           @PathVariable("facultyId") Long facultyId,
           @PathVariable("studentId") Long studentId,
           @RequestBody Student student) {
   ```
   *Phương thức:* `PUT`. Cập nhật thông tin sinh viên theo `studentId`.

6. **Xóa sinh viên (Bước 3):**
   ```java
   @DeleteMapping(value = {"/api/faculties/{facultyId}/students/{studentId}", "/faculties/{facultyId}/students/{studentId}"})
   public ResponseEntity<Void> deleteStudent(
           @PathVariable("facultyId") Long facultyId,
           @PathVariable("studentId") Long studentId) {
   ```
   *Phương thức:* `DELETE`. Xóa sinh viên, nếu thành công trả về `204 NO CONTENT`.

---

## 2.4. Cấu hình: `pom.xml`, `application.properties`, `GkApplication.java`
- **`pom.xml`:**
  - Sử dụng Spring Boot 3.2.5 và Java 17.
  - Chỉ dùng duy nhất `spring-boot-starter-web` (đã loại bỏ sạch sẽ `spring-boot-starter-thymeleaf` vì môn này làm SPA, không dùng Thymeleaf).
  - Cấu hình plugin compiler với cờ `<parameters>true</parameters>` để đảm bảo tương thích 100% với mọi phiên bản Eclipse cũ/mới:
    ```xml
    <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <configuration>
            <parameters>true</parameters>
        </configuration>
    </plugin>
    ```
- **`application.properties`:**
  - `server.port=8084`: Cổng chạy ứng dụng.
- **`GkApplication.java`:** File kích hoạt Spring Boot tiêu chuẩn, sạch sẽ, không có bất kỳ dòng log nào thừa thãi.

---

# 3. GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG `index.html`

File [index.html](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/cc-web-website-hld/truong/bt/gk/src/main/resources/static/index.html) nằm tại `src/main/resources/static/index.html`. Đây là file mà bạn cần nắm chắc nhất.

## 3.1. Cấu trúc HTML & CSS
- **CSS (Chỉ khoảng 15 dòng):**
  - `table { border-collapse: collapse; width: 100%; }`: Làm bảng viền liền nhau, co giãn 100% chiều rộng.
  - `th, td { border: 1px solid #ccc; padding: 8px; }`: Kẻ viền xám nhạt và tạo khoảng cách đệm 8px cho dễ đọc.
  - `th { background-color: #f4f4f4; }`: Nền tiêu đề bảng màu xám sáng.
  - `button, input, select { padding: 6px; }`: Kích thước vừa tay, dễ bấm.
- **HTML:**
  - Thẻ `<select id="facultySelect" onchange="onFacultyChange()">`: Trình đơn thả xuống. Khi đổi item thì sự kiện `onchange` tự kích hoạt hàm `onFacultyChange()`.
  - Thẻ `<input type="hidden" id="studentId">`: **Điểm mấu chốt của form!** Ô này ẩn đi. Khi thêm mới, ô này rỗng $\to$ code sẽ gọi `POST`. Khi bấm Sửa ở bảng, ô này được điền ID $\to$ code sẽ gọi `PUT`.
  - Thẻ `<tbody id="studentTableBody">`: Thân bảng rỗng, dữ liệu sinh viên sẽ được Javascript lặp qua và chèn vào đây.

---

## 3.2. Cơ chế gọi API và xử lý dữ liệu bằng JavaScript

### 1. Khai báo URL gốc và sự kiện mở trang:
```javascript
const API_URL = '/api';

window.onload = function() {
    loadFaculties();
};
```
- `API_URL = '/api'`: Tiền tố đường dẫn Web Service.
- `window.onload`: Đảm bảo khi trình duyệt tải xong toàn bộ HTML thì tự động gọi ngay hàm `loadFaculties()` (Bước 1).

---

### 2. Bước 1: Tải danh sách Khoa vào Combobox (`loadFaculties`):
```javascript
function loadFaculties() {
    fetch(`${API_URL}/faculties`)
        .then(response => response.json()) // Chuyển kết quả thô sang định dạng JSON Object
        .then(list => {
            const select = document.getElementById('facultySelect');
            select.innerHTML = '<option value="">-- Vui lòng chọn --</option>'; // Xóa dữ liệu cũ, đặt dòng mặc định
            list.forEach(item => {
                // Thêm từng dòng option: value là ID, hiển thị là Tên
                select.innerHTML += `<option value="${item.id}">${item.name}</option>`;
            });
        })
        .catch(err => console.error('Lỗi tải combobox:', err));
}
```
- Dùng cú pháp ES6 Template Literal (dấu phẩy nghiêng `` ` ``) để nhúng biến `${item.id}` và `${item.name}` vào chuỗi HTML cực kỳ trực quan và ngắn gọn.

---

### 3. Bước 2: Khi chọn Khoa $\to$ Lấy Sinh viên đổ vào Table:
```javascript
function onFacultyChange() {
    const parentId = document.getElementById('facultySelect').value;
    if (!parentId) {
        document.getElementById('studentTableBody').innerHTML = 
            '<tr><td colspan="4" style="text-align: center;">Vui lòng chọn mục ở trên</td></tr>';
        return;
    }
    loadStudents(parentId); // Gọi hàm lấy danh sách con
    resetForm();            // Xóa trắng form nhập liệu
}
```
- Hàm `onFacultyChange()` đọc giá trị khoa đang chọn (`parentId`). Nếu người dùng chọn dòng "-- Vui lòng chọn --" thì xóa bảng và dừng lại.

```javascript
function loadStudents(parentId, keyword = '') {
    let url = `${API_URL}/faculties/${parentId}/students`;
    if (keyword) {
        url += `?keyword=${encodeURIComponent(keyword)}`;
    }

    fetch(url)
        .then(response => response.json())
        .then(childList => {
            renderTable(childList); // Vẽ bảng dữ liệu
        })
        .catch(err => console.error('Lỗi tải danh sách con:', err));
}
```
- `encodeURIComponent(keyword)`: Xử lý an toàn khi từ khóa tìm kiếm có dấu tiếng Việt hoặc khoảng trắng.

---

### 4. Hàm vẽ bảng (`renderTable`):
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
    tbody.innerHTML = html; // Gán toàn bộ mã HTML vào tbody một lần duy nhất để tối ưu hiệu năng
}
```
- Nút Sửa gọi: `editStudent(id, name, email)`: truyền trực tiếp dữ liệu của dòng đó lên form.
- Nút Xóa gọi: `deleteStudent(id)`: truyền mã ID cần xóa.

---

### 5. Bước 3: Thêm mới (POST) và Cập nhật (PUT):
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

    // Đóng gói dữ liệu gửi lên
    const requestData = { name: name, email: email };

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
            loadStudents(parentId); // Tải lại bảng để thấy sinh viên mới
        });
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
            loadStudents(parentId); // Tải lại bảng để thấy dữ liệu vừa sửa
        });
    }
}
```
- `headers: { 'Content-Type': 'application/json' }`: Báo cho server biết nội dung gửi lên là JSON.
- `body: JSON.stringify(requestData)`: Chuyển đổi đối tượng JavaScript thành chuỗi JSON dạng text.

---

### 6. Xóa dữ liệu (DELETE):
```javascript
function deleteStudent(studentId) {
    const parentId = document.getElementById('facultySelect').value;
    if (!confirm('Bạn có chắc chắn muốn xóa ID ' + studentId + ' không?')) {
        return; // Người dùng bấm Cancel thì dừng lại
    }

    fetch(`${API_URL}/faculties/${parentId}/students/${studentId}`, {
        method: 'DELETE'
    })
    .then(() => {
        loadStudents(parentId); // Tải lại bảng để dòng vừa xóa biến mất
    });
}
```

---

# 4. CẨM NANG ỨNG BIẾN KHI ĐỀ THI THAY ĐỔI DỮ LIỆU

Bất kỳ đề thi nào của thầy cũng tuân theo **mô hình duy nhất: 1 Cha - Nhiều Con (1 - N)**. Dưới đây là bảng ma trận ánh xạ cho 4 đề tài phổ biến nhất:

## 4.1. Bảng ma trận thay thế 4 đề tài kinh điển

| Thành phần | Đề 1: Khoa & Sinh viên (Hiện tại) | Đề 2: Danh mục & Sản phẩm | Đề 3: Phòng ban & Nhân viên | Đề 4: Lớp học & Học sinh |
| :--- | :--- | :--- | :--- | :--- |
| **Đối tượng Cha** | `Faculty` (Khoa) | `Category` (Danh mục) | `Department` (Phòng ban) | `ClassRoom` (Lớp học) |
| **Đối tượng Con** | `Student` (Sinh viên) | `Product` (Sản phẩm) | `Employee` (Nhân viên) | `Pupil` (Học sinh) |
| **URL lấy danh sách Cha** | `/api/faculties` | `/api/categories` | `/api/departments` | `/api/classes` |
| **URL lấy danh sách Con** | `/api/faculties/{id}/students` | `/api/categories/{id}/products` | `/api/departments/{id}/employees` | `/api/classes/{id}/pupils` |
| **Thuộc tính Con** | `id`, `name`, `email` | `id`, `name`, `price` | `id`, `name`, `salary` | `id`, `name`, `gender` |

---

## 4.2. Hướng dẫn sửa `index.html` trong 2 phút theo đề mới

Ví dụ: Đề bài yêu cầu làm bài **Danh mục (Category) & Sản phẩm (Product)** với thuộc tính `id`, `name`, `price`:

### Bước 1: Đổi nhãn hiển thị trong HTML
- Đổi tiêu đề: `QUẢN LÝ SẢN PHẨM THEO DANH MỤC`.
- Đổi nhãn combobox: `<label>Danh mục: </label>`.
- Đổi form nhập: Ô Email đổi thành `Đơn giá`: `<input type="number" id="studentEmail" placeholder="Nhập giá...">`.
- Đổi tiêu đề bảng: Cột `Email` đổi thành `Đơn giá`.

### Bước 2: Đổi URL API trong JavaScript
- Hàm `loadFaculties()`:
  ```javascript
  // Đổi /faculties thành /categories
  fetch(`${API_URL}/categories`)
  ```
- Hàm `loadStudents()`:
  ```javascript
  // Đổi /faculties/.../students thành /categories/.../products
  let url = `${API_URL}/categories/${parentId}/products`;
  ```

### Bước 3: Đổi tên thuộc tính trong `renderTable()`
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

### Bước 4: Đổi gói tin gửi đi trong `saveStudent()`
```javascript
// Đổi email thành price
const requestData = { 
    name: name, 
    price: parseFloat(email) // Lấy giá trị từ ô input thứ 2
};

// Đổi URL POST:
fetch(`${API_URL}/categories/${parentId}/products`, { method: 'POST', ... })

// Đổi URL PUT:
fetch(`${API_URL}/categories/${parentId}/products/${id}`, { method: 'PUT', ... })
```

### Bước 5: Đổi URL xóa trong `deleteStudent()`
```javascript
// Đổi URL DELETE:
fetch(`${API_URL}/categories/${parentId}/products/${studentId}`, { method: 'DELETE' })
```

👉 **Chỉ cần sửa đúng 5 chỗ đó, toàn bộ ứng dụng chạy hoàn hảo theo đề tài mới mà không cần đụng đến logic cơ bản!**

---

# 5. CÁC LỖI THƯỜNG GẶP & CÁCH KHẮC PHỤC

### Lỗi 1: Mở web lên mà Combobox trắng tinh, không có Khoa nào
- **Nguyên nhân:** Chưa bật backend Spring Boot hoặc link `API_URL` bị sai cổng.
- **Cách sửa:**
  1. Bấm phím **F12** trên trình duyệt $\to$ chọn tab **Console** hoặc **Network** xem có báo lỗi màu đỏ không.
  2. Nếu thấy lỗi `net::ERR_CONNECTION_REFUSED`: Kiểm tra xem đã bấm Run dự án Java trong Eclipse chưa.
  3. Nếu server của thầy chạy ở port 8080 mà web của bạn chạy ở 8084: Sửa dòng đầu `<script>` thành:
     `const API_URL = 'http://localhost:8080/api';`

### Lỗi 2: Bấm chọn Khoa nhưng bảng bên dưới không hiện Sinh viên
- **Nguyên nhân:** Tên thuộc tính trong dữ liệu JSON của thầy khác với code của bạn (ví dụ thầy đặt là `studentName` chứ không phải `name`).
- **Cách sửa:**
  1. Mở F12 $\to$ tab **Network** $\to$ click vào dòng request `students` $\to$ chọn tab **Response**.
  2. Nhìn xem JSON của thầy trả về các tên trường là gì (ví dụ: `{"id": 1, "fullName": "...", "mail": "..."}`).
  3. Mở file `index.html`, sửa `s.name` thành `s.fullName`, `s.email` thành `s.mail`.

### Lỗi 3: Bấm Thêm/Sửa mà báo lỗi đỏ trong Console
- **Nguyên nhân:** Quên gửi header `Content-Type: application/json` hoặc quên `JSON.stringify(requestData)`.
- **Cách sửa:** Đảm bảo trong hàm `fetch` có đủ 2 dòng:
  ```javascript
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(requestData)
  ```

---
*Tài liệu được biên soạn phục vụ kỳ thi Giữa Kỳ môn Xây dựng website hướng dịch vụ - IUH.*
