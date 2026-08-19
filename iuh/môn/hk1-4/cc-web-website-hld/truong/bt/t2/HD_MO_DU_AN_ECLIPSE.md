# HƯỚNG DẪN TỔ CHỨC DỰ ÁN VÀ MỞ BẰNG ECLIPSE IDE (PROJECT T2)

Tài liệu này hướng dẫn chi tiết về cấu trúc phân chia các Package trong dự án **`t2`** và cách mở, biên dịch, khởi chạy dự án trên phần mềm **Eclipse IDE**.

---

## 🚀 CÁCH 1: Tạo Java Project mới trỏ đến thư mục `t2` (KHUYÊN DÙNG - 100% THÀNH CÔNG)

Nếu Eclipse báo lỗi *"Please create project before import"*, bạn làm theo 4 bước cực kỳ nhanh sau đây:

1. Trong **Eclipse IDE**, chọn menu **File** ➔ **New** ➔ **Java Project** (hoặc nhấn phím `Alt + Shift + N` ➔ **Java Project**).
2. Ô **Project name**: Nhập tên là `t2`.
3. Tích **BỎ CHỌN** ô *"Use default location"*:
   - Tại ô **Location**, nhấn nút **Browse...** và trỏ thẳng đến thư mục dự án:
     `D:\folder\rac\iuh\môn\hk1-4\công cụ web và website hướng dữ liệu\truong\bt\t2`
4. Nhấn nút **Finish** (nếu Eclipse hỏi tạo file `module-info.java`, chọn **Don't Create**).

👉 **XONG!** Eclipse sẽ tự động nạp toàn bộ 4 Package và các file web mà không gặp bất kỳ lỗi nào!

---

## 🚀 CÁCH 2: Import qua Menu File Import

1. Trong **Eclipse IDE**, chọn menu **File** ➔ **Import...**
2. Chọn **General** ➔ **Projects from Folder or Archive** (hoặc *Existing Projects into Workspace*) ➔ Nhấn **Next**.
3. Bấm nút **Directory...** chọn đến thư mục `D:\folder\rac\iuh\môn\hk1-4\công cụ web và website hướng dữ liệu\truong\bt\t2`.
4. Nhấn **Finish**.

---

## 🏗️ CẤU TRÚC PHÂN CHIA PACKAGE TRONG ECLIPSE:

```text
t2/
├── .project                         # File cấu hình dự án Eclipse
├── .classpath                       # File cấu hình classpath biên dịch Eclipse
├── HD_MO_DU_AN_ECLIPSE.md           # Tài liệu hướng dẫn chi tiết
├── src/                             # Mã nguồn các Package Java
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
