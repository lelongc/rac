# HƯỚNG DẪN HIỂN THỊ VÀ CHẠY 2 BÀI TẬP TRÊN ECLIPSE PACKAGE EXPLORER

Tài liệu giải thích lý do tại sao Eclipse Package Explorer chưa hiển thị ngay và cách bật hiển thị 2 bài tập:
1. **Bài tập 1**: `b5_basic_web` (từ `github.com/baphuc/basic_web`)
2. **Bài tập 2**: `b6_independent_web` (từ `github.com/baphuc/independent_web`)

---

## 1. TẠI SAO PACKAGE EXPLORER CHƯA HIỂN THỊ 2 THƯ MỤC?

Eclipse có 2 đặc tính cơ bản:
1. **Package Explorer chỉ hiển thị các dự án (Projects) đã được Import vào Workspace**, nó không tự ý quét thư mục ổ đĩa bên ngoài trừ khi được Import.
2. **Khi có file/thư mục mới tạo từ bên ngoài hệ thống**, Eclipse không tự động cập nhật ngay mà yêu cầu lệnh **Refresh (F5)**.

---

## 2. CÁCH HIỂN THỊ TRÊN ECLIPSE (CHỌN 1 TRONG 2 HOẶC CẢ 2)

### 📌 TRƯỜNG HỢP A: Bạn muốn thấy 2 thư mục `b5_basic_web` và `b6_independent_web` đứng riêng thành 2 Project trên Package Explorer (như `b0_firstoop` ... `b4_product_ads`):

Đã cấu hình sẵn đầy đủ file `.project`, `.classpath`, và `pom.xml` chuẩn Eclipse Maven cho cả 2 thư mục. Bạn chỉ cần Import vào:

1. Trên thanh menu Eclipse: Chọn **File** -> **Import...** (hoặc click chuột phải vào khoảng trống bất kỳ trên **Package Explorer** -> chọn **Import...**).
2. Chọn **General** -> **Existing Projects into Workspace** -> bấm **Next**.
3. Tại dòng **Select root directory**, bấm nút **Browse...** -> chọn thư mục:
   `d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\t2`
4. Eclipse sẽ tự động tìm thấy và đánh dấu tick vào:
   - `[✔] b5_basic_web`
   - `[✔] b6_independent_web`
5. Bấm nút **Finish**.
👉 **Kết quả**: Cả 2 project `b5_basic_web` và `b6_independent_web` sẽ lập tức xuất hiện ngay trên Package Explorer!

---

### 📌 TRƯỜNG HỢP B: Bạn muốn xem 2 bài tập đã tích hợp sẵn bên trong dự án `demo`:

Mã nguồn của 2 bài tập đã được chia thành 2 package riêng biệt nằm ngay trong `demo`:
- `com.example.demo.basic_web`
- `com.example.demo.independent_web`

Để Eclipse hiển thị 2 package này:
1. Trên Package Explorer, **click chuột phải vào project `demo`**.
2. Chọn **Refresh** (hoặc nhấn phím tắt **F5** trên bàn phím).
3. Mở rộng thư mục `demo` -> `src/main/java` -> `com.example.demo`, bạn sẽ thấy ngay 2 package:
   - `com.example.demo.basic_web.controller` & `model`
   - `com.example.demo.independent_web.controller` & `model`

---

## 3. CÁCH CHẠY VÀ CỔNG TRUY CẬP

| Cách chạy | Cổng (Port) | URL kiểm tra |
|---|---|---|
| **Chạy qua project `demo`** | `8080` | `http://localhost:8080/products`<br>`http://localhost:8080/dashboard`<br>`http://localhost:8080/faculties` |
| **Chạy riêng `b5_basic_web`** | `8081` | `http://localhost:8081/products`<br>`http://localhost:8081/dashboard` |
| **Chạy riêng `b6_independent_web`** | `8082` | `http://localhost:8082/faculties`<br>`http://localhost:8082/faculties/1/students` |
