# HƯỚNG DẪN TỔ CHỨC DỰ ÁN VÀ MỞ BẰNG ECLIPSE IDE (PROJECT T2)

Tài liệu này hướng dẫn chi tiết về cấu trúc phân chia các Package trong dự án **`t2`** và cách mở, biên dịch, khởi chạy dự án trên phần mềm **Eclipse IDE**.

---

## 🏗️ CẤU TRÚC PHÂN CHIA PACKAGE TRONG ECLIPSE IDE:

Trong **Eclipse IDE**, một dự án Java hoàn toàn có thể chứa nhiều Package khác nhau nằm trong cùng thư mục `src`. Dự án `t2` được sắp xếp gọn gàng thành **4 Package chuyên biệt**:

```text
t2/
├── .project                         # File cấu hình dự án Eclipse
├── .classpath                       # File cấu hình classpath biên dịch Eclipse
├── HD_MO_DU_AN_ECLIPSE.md           # Tài liệu hướng dẫn chi tiết
├── src/                             # Mã nguồn Java chính
│   ├── firstoop/                    # [Package 1] Bài tập OOP cũ (Person, Student, Teacher, PersonManagement, App)
│   ├── bt1_currency/                # [Package 2 - Bài 1] Web Service RESTful API Quy đổi tiền tệ (CurrencyServlet)
│   ├── bt2_products/                # [Package 2 - Bài 2] Web Service RESTful API Danh sách sản phẩm (ProductServlet)
│   └── webserver/                   # [Package 4] Standalone WebServer chạy REST API & WebClient trên Eclipse
└── WebContent/                      # Ứng dụng phía Client (HTML, CSS, JS DOM & jQuery AJAX)
    ├── index.html                   # Trang chủ điều hướng chọn bài
    ├── b1_currency.html             # Bài 1 Client: Giao diện Quy đổi tiền tệ
    ├── b2_products.html             # Bài 2 Client: Giao diện Danh sách sản phẩm
    ├── css/
    │   └── style.css                # CSS đơn giản, trang nhã
    └── js/
        ├── currency.js              # Gọi REST API /api/convert (jQuery $.ajax & DOM)
        └── products.js              # Gọi REST API /api/products (jQuery $.getJSON & DOM)
```

---

## 🚀 HƯỚNG DẪN MỞ DỰ ÁN TRÊN ECLIPSE IDE:

### **Bước 1: Import dự án vào Eclipse**
1. Mở phần mềm **Eclipse IDE**.
2. Chọn menu **File** ➔ **Import...**
3. Trong cửa sổ hiện ra, chọn **General** ➔ **Existing Projects into Workspace** ➔ Nhấn **Next**.
4. Tích chọn **Select root directory**, bấm nút **Browse...** và tìm chọn đến thư mục:
   `D:\folder\rac\iuh\môn\hk1-4\công cụ web và website hướng dữ liệu\truong\bt\t2`
5. Eclipse sẽ tự động nhận diện dự án tên là **`t2`**. Nhấn nút **Finish**.

---

## 🏃 HƯỚNG DẪN CHẠY CÁC BÀI TẬP TRÊN ECLIPSE:

### 1. Chạy bài cũ OOP (Package `firstoop`):
- Mở thư mục: `t2` ➔ `src` ➔ `firstoop` ➔ Nhấp đúp mở file **`App.java`**.
- Nhấp chuột phải chọn **Run As** ➔ **Java Application** (hoặc ấn `Ctrl + F11`).

### 2. Chạy bài Web Service RESTful API (Package `bt1_currency` & `bt2_products`):
- Mở thư mục: `t2` ➔ `src` ➔ `webserver` ➔ Nhấp đúp mở file **`WebServer.java`**.
- Nhấp chuột phải chọn **Run As** ➔ **Java Application** (hoặc ấn `Ctrl + F11`).
- Màn hình Console sẽ thông báo Server đã chạy thành công tại cổng `8080`.
- Mở trình duyệt Web (Chrome/Edge) và truy cập:
  * 🌐 **Trang chủ**: [http://localhost:8080/index.html](http://localhost:8080/index.html)
  * 💱 **Bài 1 (Quy đổi tiền tệ)**: [http://localhost:8080/b1_currency.html](http://localhost:8080/b1_currency.html)
  * 📦 **Bài 2 (Danh sách sản phẩm)**: [http://localhost:8080/b2_products.html](http://localhost:8080/b2_products.html)
  * 🔗 **REST API /api/convert (JSON)**: [http://localhost:8080/api/convert?amount=100&from=USD&to=VND](http://localhost:8080/api/convert?amount=100&from=USD&to=VND)
  * 🔗 **REST API /api/products (JSON)**: [http://localhost:8080/api/products](http://localhost:8080/api/products)
