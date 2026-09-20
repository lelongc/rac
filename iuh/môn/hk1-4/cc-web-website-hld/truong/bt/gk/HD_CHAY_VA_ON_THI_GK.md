# HƯỚNG DẪN CHẠY VÀ ÔN THI GIỮA KỲ: DỰ ÁN `gk`
## CHUẨN ĐỀ THI GIỮA KỲ: SINGLE PAGE APPLICATION + WEB SERVICES (REST API)
**Môn:** Xây dựng website hướng dịch vụ - IUH  
**Dành cho kỳ thi:** Thi Giữa Kỳ

---

## ⚠️ LƯU Ý SỐNG CÒN TỪ VIDEO DẶN DÒ CỦA THẦY:
1. **Bài thi giữa kỳ là SINGLE PAGE APPLICATION (SPA) gọi WEB SERVICE (REST API trả về JSON).**
2. **KHÔNG DÙNG Form Submit truyền thống (SSR)** làm tải lại toàn bộ trang web.
3. **Quy trình chuẩn 3 bước:**
   - **Bước 1:** Tải danh sách Khoa vào **Combobox** (`<select>`) bằng API `GET /api/faculties`.
   - **Bước 2:** Bắt sự kiện `onchange` khi chọn Khoa $\to$ gọi API `GET /api/faculties/{id}/students` $\to$ đổ dữ liệu vào **Table** (`<table>`).
   - **Bước 3:** Đầy đủ bộ **CRUD (Thêm mới, Sửa, Xóa)** qua Web Service:
     + Thêm mới sinh viên: Gọi `POST /api/faculties/{id}/students`.
     + Sửa sinh viên: Gọi `PUT /api/faculties/{id}/students/{studentId}`.
     + Xóa sinh viên: Gọi `DELETE /api/faculties/{id}/students/{studentId}`.
   - **BƯỚC 4 & 5 (Phân trang & Sắp xếp): THẦY NÓI RÕ LÀ KHÔNG THI GIỮA KỲ (Dành cho Cuối kỳ).**
4. **Lúc thi, thầy sẽ cung cấp sẵn Web Service (Backend).** Sinh viên chủ yếu tập trung viết mã Frontend (HTML + JavaScript Fetch API).
5. Để bạn luyện tập thực chiến ở nhà y như trong phòng thi, dự án này đã được tích hợp sẵn cả **Backend Web Service (`FacultyController.java`)** và **Frontend Single Page (`index.html`)**!

---

## 🚀 1. CÁCH KHỞI ĐỘNG DỰ ÁN TRÊN MÁY

### Cách 1: Chạy bằng dòng lệnh Terminal
Mở terminal tại thư mục dự án `d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\gk` và gõ:
```bash
./mvnw spring-boot:run
```

### Cách 2: Chạy trong Eclipse IDE
1. Mở Eclipse $\to$ Import dự án: **File** $\to$ **Import...** $\to$ **Existing Projects into Workspace** $\to$ Chọn thư mục `gk`.
2. Mở file: `src/main/java/com/example/gk/GkApplication.java`.
3. Chuột phải vào `GkApplication.java` $\to$ **Run As** $\to$ **Spring Boot App** (hoặc **Java Application**).

---

## 🌐 2. ĐƯỜNG DẪN TRUY CẬP TRÊN TRÌNH DUYỆT (PORT: 8084)

Mở trình duyệt (Chrome / Edge / Cốc Cốc) và truy cập:

* 🌟 **Giao diện thi Giữa kỳ (Single Page Web Service - CHUẨN 100% THEO Ý THẦY):**  
  👉 **`http://localhost:8084/`** hoặc **`http://localhost:8084/spa`**  
  *(Tại đây bạn sẽ thấy Combobox Khoa, Bảng Table sinh viên và Form CRUD thêm/sửa/xóa chạy hoàn toàn không reload trang!)*

* 🔍 **Kiểm tra Web Service (REST API trả về JSON thô của Server):**  
  - Danh sách Khoa: `http://localhost:8084/api/faculties`  
  - Sinh viên khoa CNTT (ID=1): `http://localhost:8084/api/faculties/1/students`  
  - Sinh viên khoa Cơ Khí (ID=2): `http://localhost:8084/api/faculties/2/students`  

---

## 📂 3. CÁC TÀI LIỆU QUAN TRỌNG ĐÃ CHUẨN BỊ CHO BẠN:

1. 📄 **[`note-gk.md`](note-gk.md):** Bản chép lời nguyên văn từng câu chữ của thầy từ video `gk.mp4`, đối chiếu thuật ngữ kỹ thuật và phân tích chi tiết tiêu chí chấm điểm của thầy.
2. 📄 **[`DE_CUONG_ON_THI_GIUA_KY.md`](DE_CUONG_ON_THI_GIUA_KY.md):** Đề cương ôn thi giữa kỳ toàn diện gồm lý thuyết Web Service, "bảng phao code" JavaScript Fetch API chuẩn 3 bước, các bẫy lỗi thường gặp trong phòng thi và cách xử lý.
3. 💻 **[`src/main/resources/templates/spa.html`](src/main/resources/templates/spa.html):** Toàn bộ mã nguồn giao diện Single Page chuẩn 3 bước với chú thích tiếng Việt chi tiết từng dòng.
