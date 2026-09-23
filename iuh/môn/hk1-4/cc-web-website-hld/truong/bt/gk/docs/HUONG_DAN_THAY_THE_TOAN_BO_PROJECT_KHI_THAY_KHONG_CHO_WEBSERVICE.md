# CẨM NANG ĐỔI TÊN TOÀN BỘ PROJECT (CẢ FRONTEND & BACKEND) KHI THẦY KHÔNG CHO WEBSERVICE

**Dành cho:** Kỳ thi Giữa kỳ môn *Xây dựng website hướng dịch vụ* (IUH).  
**Mục tiêu:** Giúp bạn tự tin ứng biến 100% khi vào phòng thi gặp đề tài khác (Danh mục & Sản phẩm, Phòng ban & Nhân viên...), dù thầy có cấp Web Service hay bắt tự chạy Backend từ A đến Z!

---

## 📑 MỤC LỤC
1. [Bản chất bài thi & Vì sao phải đổi cả tên hàm?](#1-bản-chất-bài-thi--vì-sao-phải-đổi-cả-tên-hàm)
2. [PHẦN 1: Đổi toàn bộ Frontend (`index.html`) bằng 12 bước Match Case](#2-phần-1-đổi-toàn-bộ-frontend-indexhtml-bằng-12-bước-match-case)
3. [PHẦN 2: Đổi toàn bộ Backend Java bằng Eclipse Refactor khi thầy KHÔNG CHO Web Service](#3-phần-2-đổi-toàn-bộ-backend-java-bằng-eclipse-refactor-khi-thầy-không-cho-webservice)
4. [Bảng tra cứu trọn gói cho 3 đề thi kinh điển nhất tại IUH](#4-bảng-tra-cứu-trọn-gói-cho-3-đề-thi-kinh-điển-nhất-tại-iuh)

---

# 1. BẢN CHẤT BÀI THI & VÌ SAO PHẢI ĐỔI CẢ TÊN HÀM?

Khi chấm thi, giáo viên thường bấm `F12` kiểm tra mã nguồn JavaScript hoặc yêu cầu sinh viên mở file code lên và hỏi:
- *"Em chỉ cho thầy hàm Thêm sản phẩm của em viết ở đâu?"*
- *"Hàm lấy danh sách sản phẩm theo danh mục tên gì?"*

Nếu đề bài là **Quản lý Sản phẩm theo Danh mục** mà tên hàm trong code của bạn lại là `saveStudent()`, `loadStudents()`, `editStudent()`... thì giáo viên sẽ lập tức trừ điểm hoặc nghi ngờ bạn copy bài từ bài thực hành Khoa - Sinh viên!

👉 Do đó, việc đổi **toàn bộ tên hàm** (`saveProduct`, `editProduct`, `loadProducts`, `deleteProduct`, `onCategoryChange`...) và **tên ID thẻ** (`categorySelect`, `productId`, `productPrice`...) là **BẮT BUỘC** để đạt điểm tối đa 10/10!

---

# 2. PHẦN 1: ĐỔI TOÀN BỘ FRONTEND (`index.html`) BẰNG 12 BƯỚC MATCH CASE

### ⚠️ BẮT BUỘC: BẬT TÍNH NĂNG PHÂN BIỆT CHỮ HOA / CHỮ THƯỜNG (MATCH CASE)
Trước khi tìm kiếm, bạn phải bật tính năng phân biệt hoa/thường để tránh lỗi (ví dụ không bị biến `faculties` thành `categoryies`):
- **Trong Eclipse:** Bấm `Ctrl + F` $\to$ Đánh dấu tick vào ô `[x] Case sensitive`.
- **Trong VS Code:** Bấm `Ctrl + H` $\to$ Click vào biểu tượng chữ `Aa` (hoặc phím tắt `Alt + C`).
- **Trong Notepad++:** Bấm `Ctrl + H` $\to$ Đánh dấu tick vào ô `[x] Match case`.

---

### 🔥 BẢNG 12 BƯỚC THAY THẾ (VÍ DỤ ĐỀ: DANH MỤC & SẢN PHẨM)
Lần lượt nhập từng cặp từ sau và bấm nút **Replace All** (Thay thế tất cả):

| Bước | Tìm từ này (Find) | Thay bằng từ này (Replace) | Ý nghĩa thay đổi trong mã nguồn |
| :---: | :---------------- | :------------------------- | :------------------------------ |
| **1** | `Faculties` | `Categories` | Đổi tên hàm: `loadFaculties()` $\to$ `loadCategories()` |
| **2** | `faculties` | `categories` | Đổi đường dẫn URL API Cha: `/api/categories` |
| **3** | `Faculty` | `Category` | Đổi tên hàm: `onFacultyChange()` $\to$ `onCategoryChange()` |
| **4** | `faculty` | `category` | Đổi ID thẻ Combobox: `facultySelect` $\to$ `categorySelect` |
| **5** | `Students` | `Products` | Đổi tên hàm: `loadStudents()` $\to$ `loadProducts()`, `searchStudents()` $\to$ `searchProducts()` |
| **6** | `students` | `products` | Đổi đường dẫn URL API Con: `.../products` |
| **7** | `Student` | `Product` | Đổi tên các hàm CRUD: `saveProduct()`, `editProduct()`, `deleteProduct()` |
| **8** | `student` | `product` | Đổi ID các thẻ Form & Bảng: `productId`, `productName`, `productTableBody` |
| **9** | `email` | `price` | Đổi thuộc tính JSON: `s.price`, `price: price` |
| **10**| `Email` | `Đơn giá` | Đổi tiêu đề cột bảng `<th>` và nhãn ô input form |
| **11**| `Khoa` | `Danh mục` | Đổi nhãn tiếng Việt trên giao diện |
| **12**| `Sinh viên` | `Sản phẩm` | Đổi tiêu đề tiếng Việt trên giao diện |

---

### Kết quả thu được sau 12 lần bấm Replace All:
1. **Các hàm JavaScript đồng bộ hoàn hảo:**
   ```javascript
   loadCategories();
   onCategoryChange();
   loadProducts(parentId, keyword);
   searchProducts();
   saveProduct();
   editProduct(id, name, price);
   deleteProduct(productId);
   ```
2. **Các ID trong HTML đồng bộ hoàn hảo:**
   ```html
   <select id="categorySelect" onchange="onCategoryChange()">
   <input type="text" id="keyword" oninput="searchProducts()">
   <input type="hidden" id="productId">
   <input type="text" id="productName">
   <input type="text" id="productPrice">
   <tbody id="productTableBody">
   ```
3. **Các đường dẫn URL API đồng bộ hoàn hảo:**
   ```javascript
   fetch(`${API_URL}/categories`)
   fetch(`${API_URL}/categories/${parentId}/products`)
   fetch(`${API_URL}/categories/${parentId}/products/${id}`)
   ```
Không còn sót lại bất kỳ một chữ "Student" hay "Faculty" nào!

---

# 3. PHẦN 2: ĐỔI TOÀN BỘ BACKEND JAVA BẰNG ECLIPSE REFACTOR KHI THẦY KHÔNG CHO WEBSERVICE

Nếu thầy yêu cầu sinh viên phải tự dựng Backend hoặc nộp cả project Spring Boot, bạn mang nguyên project này vào và dùng tính năng **Refactor Rename** của Eclipse để đổi toàn bộ mã nguồn Java trong vòng **2 phút**:

### 🛠️ Kỹ thuật Refactor Rename trong Eclipse:
> Phím tắt thần thánh: **`Alt + Shift + R`** (hoặc click chuột phải vào tên Class $\to$ **Refactor** $\to$ **Rename**).  
> Khi dùng tính năng này, Eclipse sẽ **tự động đổi tên file `.java` và tự động cập nhật mọi nơi gọi trong toàn bộ project** mà không lo bị lỗi biên dịch!

---

### Bước 1: Đổi Entity Cha (`Faculty.java` $\to$ `Category.java`)
1. Mở file `Faculty.java` (trong package `com.example.gk.model`).
2. Bôi đen chữ `Faculty` ở dòng `public class Faculty`.
3. Bấm **`Alt + Shift + R`** $\to$ gõ `Category` $\to$ nhấn **Enter**.
4. *(Tùy chọn)* Đổi tên danh sách con:
   - Đổi `List<Student> students;` thành `List<Product> products;`.

---

### Bước 2: Đổi Entity Con (`Student.java` $\to$ `Product.java`)
1. Mở file `Student.java` (trong package `com.example.gk.model`).
2. Bôi đen chữ `Student` ở dòng `public class Student`.
3. Bấm **`Alt + Shift + R`** $\to$ gõ `Product` $\to$ nhấn **Enter**.
4. Đổi thuộc tính `email`:
   - Bôi đen chữ `email` ở dòng `private String email;`.
   - Bấm **`Alt + Shift + R`** $\to$ gõ `price` $\to$ nhấn **Enter** (Có thể đổi kiểu dữ liệu sang `Double price` hoặc giữ `String price` đều chạy tốt).

---

### Bước 3: Đổi Service (`FacultyService.java` $\to$ `CategoryService.java`)
1. Mở file `FacultyService.java` (trong package `com.example.gk.service`).
2. Bôi đen chữ `FacultyService` ở dòng `public class FacultyService`.
3. Bấm **`Alt + Shift + R`** $\to$ gõ `CategoryService` $\to$ nhấn **Enter**.

---

### Bước 4: Đổi Controller (`FacultyController.java` $\to$ `CategoryController.java`)
1. Mở file `FacultyController.java` (trong package `com.example.gk.controller`).
2. Bôi đen chữ `FacultyController` $\to$ bấm **`Alt + Shift + R`** $\to$ gõ `CategoryController` $\to$ nhấn **Enter**.
3. Sửa lại các đường dẫn `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping` trên URL:
   - Đổi `/api/faculties` $\to$ `/api/categories`
   - Đổi `/api/faculties/{facultyId}/students` $\to$ `/api/categories/{categoryId}/products`

---

### Bước 5: Chạy ứng dụng và kiểm tra
1. Bấm chuột phải vào file `GkApplication.java` $\to$ chọn **Run As** $\to$ **Spring Boot App**.
2. Mở trình duyệt gõ: `http://localhost:8084`
3. Ứng dụng hiển thị giao diện mới, nạp danh sách Danh mục vào Combobox, chọn Danh mục đổ ra Sản phẩm, đầy đủ Thêm - Sửa - Xóa - Tìm kiếm!

---

# 4. BẢNG TRA CỨU TRỌN GÓI CHO 3 ĐỀ THI KINH ĐIỂN NHẤT TẠI IUH

### 📦 ĐỀ 1: QUẢN LÝ SẢN PHẨM THEO DANH MỤC (Category & Product)
- **Cha (Category):**
  - `Faculties` $\to$ `Categories` | `faculties` $\to$ `categories`
  - `Faculty` $\to$ `Category` | `faculty` $\to$ `category` | `Khoa` $\to$ `Danh mục`
- **Con (Product):**
  - `Students` $\to$ `Products` | `students` $\to$ `products`
  - `Student` $\to$ `Product` | `student` $\to$ `product` | `Sinh viên` $\to$ `Sản phẩm`
- **Thuộc tính:**
  - `email` $\to$ `price` | `Email` $\to$ `Đơn giá`

---

### 🏢 ĐỀ 2: QUẢN LÝ NHÂN VIÊN THEO PHÒNG BAN (Department & Employee)
- **Cha (Department):**
  - `Faculties` $\to$ `Departments` | `faculties` $\to$ `departments`
  - `Faculty` $\to$ `Department` | `faculty` $\to$ `department` | `Khoa` $\to$ `Phòng ban`
- **Con (Employee):**
  - `Students` $\to$ `Employees` | `students` $\to$ `employees`
  - `Student` $\to$ `Employee` | `student` $\to$ `employee` | `Sinh viên` $\to$ `Nhân viên`
- **Thuộc tính:**
  - `email` $\to$ `salary` | `Email` $\to$ `Tiền lương`

---

### 🏫 ĐỀ 3: QUẢN LÝ HỌC VIÊN THEO LỚP HỌC (Classroom & Student)
- **Cha (Classroom):**
  - `Faculties` $\to$ `Classrooms` | `faculties` $\to$ `classrooms`
  - `Faculty` $\to$ `Classroom` | `faculty` $\to$ `classroom` | `Khoa` $\to$ `Lớp học`
- **Con (Student):**
  - Giữ nguyên các chữ `Students`, `students`, `Student`, `student`.
- **Thuộc tính:**
  - `email` $\to$ `phone` | `Email` $\to$ `Số điện thoại`
