# HƯỚNG DẪN IMPORT VÀ CHẠY DỰ ÁN SPRING BOOT (DEMO) VÀO ECLIPSE

Dự án **`demo`** là ứng dụng mẫu **Spring Boot Web** (tải từ trang [https://start.spring.io](https://start.spring.io)).

---

## 🚀 CÁC BƯỚC IMPORT DỰ ÁN "DEMO" VÀO ECLIPSE (2 CÁCH)

### 🌟 CÁCH 1: IMPORT DẠNG "MAVEN PROJECT" (CHUẨN NHẤT CHO SPRING BOOT)
1. Mở Eclipse, vào menu trên cùng: **`File` ➔ `Import...`**
2. Trong cửa sổ hiện ra, mở thư mục **`Maven`** ➔ Chọn **`Existing Maven Projects`** ➔ Bấm **`Next`**.
3. Tại mục **Root Directory**, bấm **`Browse...`** ➔ Chọn thư mục:
   `d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\t2\demo`
4. Eclipse sẽ tự động quét thấy file `pom.xml` và tích dấu chọn `pom.xml ...`.
5. Bấm **`Finish`**.
6. ⏳ *Lưu ý*: Lần đầu tiên import, Eclipse sẽ tải các thư viện Spring Boot ở góc dưới bên phải màn hình (`Building workspace...`). Hãy chờ khoảng 30s - 1 phút cho thanh tiến trình chạy xong.

---

### 📂 CÁCH 2: IMPORT DẠNG PROJECT THƯỜNG (NHANH CHÓNG)
1. Vào menu **`File` ➔ `Import...` ➔ `General` ➔ `Existing Projects into Workspace`** ➔ Bấm **`Next`**.
2. Tại mục *Select root directory*, bấm **`Browse...`** ➔ Chọn thư mục `demo`.
3. Bấm **`Finish`**.

---

## 🏃 CÁCH CHẠY ỨNG DỤNG SPRING BOOT TRONG ECLIPSE:

1. Trong Package Explorer của Eclipse, mở cây thư mục:
   `demo` ➔ `src/main/java` ➔ `com.example.demo` ➔ **`DemoApplication.java`**.
2. **Nhấp chuột phải vào `DemoApplication.java`**:
   - Chọn **`Run As` ➔ `Java Application`** (hoặc `Spring Boot App`).
3. Mở tab **Console** bên dưới màn hình Eclipse, bạn sẽ thấy logo chữ ASCII nghệ thuật **`Spring`** xuất hiện và thông báo:
   `Tomcat started on port 8080 (http) with context path ''`

---

## 🌐 KIỂM TRA TRÊN TRÌNH DUYỆT WEB:

Mở trình duyệt (Chrome/Edge) và truy cập các đường dẫn sau để kiểm tra:
1. **Trang chủ Web**: [http://localhost:8080/](http://localhost:8080/)
2. **Test RESTful API Hello**: [http://localhost:8080/api/hello](http://localhost:8080/api/hello)
3. **Test RESTful API Products**: [http://localhost:8080/api/products](http://localhost:8080/api/products)
