# HƯỚNG DẪN TỪ A-Z: CÁCH TẢI BỘ KHUNG SPRING BOOT VÀ ĐƯA CÁC FILE CODE LẺ VÀO ECLIPSE ĐỂ CHẠY NGAY

> **Dành cho tình huống thực tế:** Khi Thầy/Cô hoặc trên GitHub chỉ gửi cho bạn các file code lẻ (chẳng hạn như chỉ có `Faculty.java`, `Student.java`, `FacultyController.java`, `faculty_list.html` mà KHÔNG CÓ cấu trúc dự án hoàn chỉnh, không có `pom.xml`, không có bộ khung Spring Boot).

---

## 🎯 BỨC TRANH CỐT LÕI: TẠI SAO PHẢI CẦN "BỘ KHUNG"?

Trong lập trình Spring Boot:
- Các file `.java` và `.html` chỉ là **"ruột"** (mã nguồn logic).
- Để Eclipse hiểu và chạy được như một web server (có Tomcat nhúng, tự động chạy cổng 8080/8082, nhận diện Spring annotation), dự án bắt buộc phải có **"bộ khung chuẩn"** gồm:
  1. File `pom.xml` (khai báo thư viện Spring Boot).
  2. File Main có hàm `main` gắn `@SpringBootApplication`.
  3. Cấu trúc thư mục chuẩn Maven: `src/main/java` và `src/main/resources`.

---

## BƯỚC 1: TẢI BỘ KHUNG WEB BASIC CHUẨN Ở ĐÂU? (CHÍNH HÃNG 100%)

Trang web chính thức và chuẩn nhất thế giới của Spring Boot để tải bộ khung là:
👉 **[https://start.spring.io](https://start.spring.io)** *(Spring Initializr)*

### 📝 Các thông số cần chọn trên trang `start.spring.io`:

| Mục | Lựa chọn chuẩn | Giải thích lý do |
|---|---|---|
| **Project** | **Maven** | Mặc định các trường đại học tại VN đều dùng Maven |
| **Language** | **Java** | Ngôn ngữ học trong trường |
| **Spring Boot** | **3.2.x** hoặc **3.3.x** | Chọn bản số thường, **TUYỆT ĐỐI KHÔNG CHỌN** bản có chữ *(SNAPSHOT)* hoặc *(M1, M2)* vì là bản thử nghiệm dễ lỗi |
| **Group** | `com.example` | Tên định danh gói cơ sở |
| **Artifact** | `demo_web` *(hoặc tên bài tùy ý)* | Tên thư mục dự án |
| **Packaging** | **Jar** | Chuẩn đóng gói hiện đại của Spring Boot |
| **Java** | **17** *(hoặc 21)* | Khớp với phiên bản JDK đã cài trên máy bạn |

### ➕ Chọn Dependencies (Thư viện cần thiết - BẮT BUỘC):
Nhấn vào nút **ADD DEPENDENCIES...** (nút màu xanh góc phải) và gõ tìm 2 thư viện sau:
1. **Spring Web**: *(Bắt buộc)* Giúp chạy web, tạo REST API, nhúng sẵn máy chủ Tomcat.
2. **Thymeleaf**: *(Bắt buộc nếu làm bài có giao diện HTML)* Giúp render các trang `.html` động.
3. *(Tùy chọn thêm)* **Spring Boot DevTools**: Tự động reload ứng dụng khi bạn chỉnh sửa code mà không cần tắt đi bật lại.

👉 Bấm nút **GENERATE** (hoặc phím tắt **Ctrl + Enter**) ở dưới cùng.  
Trình duyệt sẽ tự động tải về một file nén có đuôi: **`demo_web.zip`** (dung lượng chỉ khoảng vài chục KB).

---

## BƯỚC 2: GIẢI NÉN VÀ ĐƯA DỰ ÁN VÀO TRONG ECLIPSE

1. Chuột phải vào file `demo_web.zip` vừa tải về ➔ Chọn **Extract Here** (Giải nén). Bạn sẽ được thư mục `demo_web`.
2. Mở **Eclipse**:
   - Chọn menu: **File** ➔ **Import...** (hoặc chuột phải vào khoảng trống Package Explorer ➔ chọn **Import...**).
   - Chọn thư mục: **Maven** ➔ **Existing Maven Projects** ➔ bấm **Next**.
   - Tại dòng **Root Directory**, bấm nút **Browse...** ➔ Chọn đúng thư mục `demo_web` vừa giải nén.
   - Eclipse sẽ nhận diện thấy file `pom.xml` có dấu tick `[✔] pom.xml`.
   - Bấm nút **Finish**.
3. **Chờ Eclipse tải thư viện:** Nhìn xuống góc phải dưới cùng của Eclipse, chờ thanh tiến trình `Building workspace...` chạy xong 100% (khoảng 30 giây đến 1 phút trong lần đầu tiên).

---

## BƯỚC 3: QUY TẮC "BỎ ĐỒ ĐÚNG NGĂN" - ĐƯA CÁC FILE CODE LẺ VÀO DỰ ÁN

Khi mở dự án trên Eclipse, bạn sẽ thấy cấu trúc thư mục chuẩn. Hãy copy các file lẻ trên GitHub/thầy gửi vào **đúng vị trí** như sau:

```
demo_web/
├── src/main/java/com/example/demo_web/
│   ├── DemoWebApplication.java              <-- File chạy chính có sẵn từ đầu
│   ├── model/                               <-- Tạo thư mục model ở đây
│   │   ├── Faculty.java                     <-- Bỏ file Entity / Model vào đây
│   │   └── Student.java
│   ├── service/                             <-- Tạo thư mục service ở đây
│   │   └── FacultyService.java              <-- Bỏ file xử lý nghiệp vụ vào đây
│   └── controller/                          <-- Tạo thư mục controller ở đây
│       ├── FacultyController.java           <-- Bỏ file Controller MVC vào đây
│       └── FacultyRestController.java       <-- Bỏ file REST API vào đây
│
└── src/main/resources/
    ├── application.properties               <-- File chỉnh cổng server.port
    ├── static/                              <-- Chứa ảnh, CSS, JS tĩnh (nếu có)
    └── templates/                           <-- BỎ TẤT CẢ FILE .HTML VÀO ĐÂY
        ├── faculty_list.html
        └── faculty_students.html
```

### 📌 Thao tác nhanh trực tiếp trong Eclipse:
1. **Tạo Package con:** Click chuột phải vào `src/main/java/com/example/demo_web` ➔ Chọn **New** ➔ **Package** ➔ Đặt tên là `com.example.demo_web.model` (tương tự tạo thêm `.controller`, `.service`).
2. **Copy file vào:** Kéo thả trực tiếp file `.java` từ Windows Explorer vào package tương ứng trên Eclipse (hoặc mở file copy toàn bộ code dán vào).
3. **Copy file HTML:** Kéo thả các file `.html` vào thư mục `src/main/resources/templates`.

---

## BƯỚC 4: SỬA 2 LỖI KINH ĐIỂN HAY GẶP NHẤT KHI DÁN CODE LẺ

### ❌ Lỗi 1: Dòng đầu tiên báo lỗi gạch đỏ `The declared package "..." does not match the expected package`
- **Nguyên nhân:** File code lẻ trên mạng đang ghi package của người ta (ví dụ: `package model;` hoặc `package com.baphuc;`), trong khi dự án của bạn đang ở package `com.example.demo_web.model`.
- **Cách sửa siêu nhanh:**
  - Cách 1: Rê chuột vào dòng chữ gạch đỏ, nhấn vào gợi ý màu xanh: **"Change package declaration to 'com.example.demo_web.model'"**.
  - Cách 2: Sửa lại bằng tay dòng đầu tiên cho khớp với tên thư mục package chứa file đó:
    ```java
    package com.example.demo_web.model;
    ```

### ❌ Lỗi 2: Báo lỗi đỏ không nhận diện được Model ở Controller (`Student cannot be resolved to a type`)
- **Nguyên nhân:** Do tách Controller và Model sang 2 package khác nhau nên Controller chưa `import` Model.
- **Cách sửa:** Bấm phím tắt **`Ctrl + Shift + O`** (Eclipse sẽ tự động quét và import tất cả thư viện còn thiếu trong 1 giây).

---

## BƯỚC 5: CHỈNH CỔNG CHẠY VÀ KHỞI ĐỘNG ỨNG DỤNG

1. **Đổi cổng (Port) nếu cần:**
   - Mở file: `src/main/resources/application.properties`.
   - Gõ thêm dòng:
     ```properties
     server.port=8082
     ```
     *(Để tránh đụng cổng 8080 nếu máy đang chạy ứng dụng khác).*

2. **Khởi động ứng dụng:**
   - Mở file: `src/main/java/com/example/demo_web/DemoWebApplication.java`.
   - Nhấp **chuột phải** vào file đó ➔ chọn **Run As** ➔ **Spring Boot App** (hoặc **Java Application**).
   - Nhìn cửa sổ **Console** bên dưới, khi thấy dòng:
     `Started DemoWebApplication in ... seconds (process running for ...)`
     là máy chủ Tomcat đã bật thành công!

3. **Kiểm tra trên trình duyệt:**
   - Nếu là giao diện HTML: `http://localhost:8082/` hoặc `http://localhost:8082/faculties`
   - Nếu là REST API JSON: `http://localhost:8082/api/faculties`

---

## 🏆 TỔNG KẾT BẢNG PHÍM TẮT THẦN THÁNH TRONG ECLIPSE

| Phím tắt | Công dụng | Khi nào dùng? |
|---|---|---|
| **Ctrl + Shift + O** | Tự động Import / Xóa import thừa | Khi dán code mới vào bị lỗi đỏ gạch chân các Class |
| **Ctrl + Shift + F** | Tự động canh lề, làm đẹp code (Format) | Giúp code thẳng hàng, gọn gàng, chuyên nghiệp |
| **Alt + F5** | Update Maven Project | Khi pom.xml tải thư viện bị lag, Eclipse chưa cập nhật |
| **F5** | Refresh thư mục | Khi mới copy file từ bên ngoài Windows vào |
| **Ctrl + F11** | Chạy lại ứng dụng gần nhất | Khởi động lại server nhanh |
