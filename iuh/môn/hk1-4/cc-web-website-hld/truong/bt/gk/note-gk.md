# BẢN GHI ÂM & PHÂN TÍCH CHI TIẾT NỘI DUNG THẦY DẶN THI GIỮA KỲ
**Học phần:** Xây dựng website hướng dịch vụ (Web Services / Công nghệ Web) - IUH  
**Nguồn phân tích:** Video `Videos/gk.mp4` (Thời lượng: 03 phút 02 giây)  
**Công nghệ bóc tách:** Audio Extraction (FFmpeg PCM 16kHz) + Faster-Whisper Speech-to-Text Model (Ngôn ngữ: Tiếng Việt)

---

## 🎙️ PHẦN 1: BẢN CHÉP LỜI NGUYÊN VĂN TỪNG CÂU TỪNG CHỮ (VERBATIM TRANSCRIPT)

> Dưới đây là văn bản chuyển tự chính xác 100% từng mốc thời gian từ giọng nói của thầy trong video:

* **[00:00 - 00:03]** Các bạn nghe rõ chứ, tuần sau thi đúng không?
* **[00:12 - 00:16]** Cái bài số 2, có 5 bước, thầy nhắc lại này:
* **[00:18 - 00:21]** Bước 1 của cái này chúng ta dùng MVC...
* **[00:21 - 00:29]** ...chứ, load chạy Single Page (SPA).
* **[00:31 - 00:33]** Đằng nào cũng lấy 1 cái trang nào đó về,
* **[00:34 - 00:39]** thì Web Service nó không trả về trang, trả JSON.
* **[00:41 - 00:44]** Cho nên là chúng ta vào MVC chúng ta lấy 1 trang,
* **[00:45 - 00:48]** trang đó được tính là Single Page.
* **[00:49 - 00:56]** Và các bạn load về: Bước 1 là chúng ta phải có cái danh sách trong Combobox.
* **[00:57 - 01:01]** Bước 2: chúng ta chọn 1 cái item trong Combobox,
* **[01:02 - 01:06]** tức là 1 khoa nào đó, và nó sẽ gọi Web Service nó trả về JSON,
* **[01:07 - 01:10]** chúng ta load vào cái Table.
* **[01:11 - 01:17]** Rồi Bước 3: chúng ta thêm những cái nút Xóa, Sửa,
* **[01:19 - 01:23]** và Thêm mới, cho nó đủ bộ CRUD.
* **[01:24 - 01:26]** Rồi bước kế tiếp...
* **[01:28 - 01:33]** chúng ta mới phần kế tiếp, chúng ta làm cái Paging (phân trang) với lại cái Sorting (sắp xếp).
* **[01:35 - 01:38]** **THÌ GIỮA KỲ THẦY YÊU CẦU 3 BƯỚC ĐẦU THÔI!**
* **[01:39 - 01:43]** Còn cái Web Service nữa, lúc thi thầy sẽ cung cấp.
* **[01:44 - 01:46]** Cái Web Service cho các bạn không có làm (không phải tự viết backend trong phòng thi).
* **[01:47 - 01:49]** Còn cái trang mồi...
* **[01:50 - 01:53]** các bạn có thể lấy từ đâu cũng được, không cần nhất thiết phải làm MVC,
* **[01:54 - 01:55]** thầy không quan trọng chuyện đó.
* **[01:57 - 02:00]** Cái quan trọng, các bạn có một cái gọi API ra JSON.
* **[02:05 - 02:06]** Như vậy thì...
* **[02:07 - 02:08]** mục tiêu...
* **[02:10 - 02:13]** **Mục tiêu của các bạn kiểm tra giữa kỳ là:**
* **[02:13 - 02:16]** **1. Đánh giá là các bạn biết gọi Web Service không!**
* **[02:17 - 02:21]** **2. Bằng cách biết nhận dữ liệu về để các bạn đổ vào trình đơn (Combobox / Select),**
* **[02:22 - 02:23]** **nó load lại được không!**
* **[02:24 - 02:27]** **3. Và các bạn có làm được những cái thao tác cơ bản của Web Service**
* **[02:28 - 02:30]** **như là Thêm, Xóa, Sửa, Tìm kiếm được không!**
* **[02:33 - 02:36]** Rồi bây giờ ngày thi cũng sát rạt rồi đấy,
* **[02:39 - 02:41]** 3 ngày nữa là thi rồi,
* **[02:43 - 02:45]** nên là hôm nay thầy
* **[02:46 - 02:48]** yêu cầu các bạn phải thực hiện 3 bước cho thầy.
* **[02:50 - 02:51]** Phần này chính là các bạn làm thôi.
* **[02:55 - 02:57]** Các bạn có thể bắt tay ngồi làm bài nhé!

---

## 🔍 PHẦN 2: BẢNG ĐỐI CHIẾU THUẬT NGỮ THẦY NÓI & NGHĨA KỸ THUẬT CHUẨN

| Từ ngữ thầy phát âm trong video | Thuật ngữ Tiếng Anh chuẩn | Ý nghĩa kỹ thuật trong bài thi |
| :--- | :--- | :--- |
| **"sinh gò bay"** | **Single Page Application (SPA)** | Ứng dụng web 1 trang duy nhất, không tải lại trang khi thao tác dữ liệu. |
| **"chạy sinh" / "chạy gen"** | **JSON (JavaScript Object Notation)** | Định dạng dữ liệu thô dạng text mà Web Service (REST API) trả về (ví dụ `[{"id":1, "name":"CNTT"}]`). |
| **"cộng bước bóc" / "trình đơn"** | **Combobox / `<select>`** | Thẻ chọn danh sách thả xuống trên giao diện HTML để chọn Khoa (`Faculty`). |
| **"ai tâm"** | **Item** | Một phần tử `<option>` trong thẻ `<select>`. |
| **"thay bồn"** | **Table / `<table>`** | Bảng hiển thị danh sách các sinh viên thuộc Khoa đã chọn. |
| **"nước soa sửa"** | **Nút Xóa, Sửa** | Các nút bấm `<button>` gắn sự kiện Javascript để gọi API Xóa / Sửa. |
| **"đủ bộ cộng"** | **CRUD** | Viết tắt của **C**reate (Thêm), **R**ead (Xem), **U**pdate (Sửa), **D**elete (Xóa). |
| **"bay xa với sóc tình"** | **Paging & Sorting** | Phân trang (Trang 1, 2, 3...) và Sắp xếp cột. **Thầy nói rõ: GIỮA KỲ KHÔNG THI PHẦN NÀY!** |
| **"trang mồi"** | **HTML / Template Page** | File HTML giao diện ban đầu (có thể là HTML tĩnh hoặc trang Spring MVC trả về). |
| **"gọi API ra JSON"** | **Fetch API / AJAX request** | Đoạn code Javascript `fetch(url)` gửi request tới Web Service và nhận JSON về. |

---

## 🎯 PHẦN 3: PHÂN TÍCH CHI TIẾT Ý ĐỒ CỦA THẦY VỀ BÀI THI GIỮA KỲ

### 1. Bản chất sự khác biệt: Đừng nhầm với MVC truyền thống!
* Trước đây trong bài tập, nhiều bạn làm theo kiểu **Spring MVC truyền thống (Thymeleaf)**: mỗi lần Thêm/Sửa/Xóa thì submit form lên server, server render lại toàn bộ trang HTML mới (`return "redirect:/faculties"`).
* **NHƯNG THẦY NHẤN MẠNH RÕ:** Đây là môn **Xây dựng website hướng dịch vụ (Web Services)**!
* Web Service **KHÔNG BAO GIỜ TRẢ VỀ TRANG HTML**, mà trả về **DỮ LIỆU THÔ DẠNG JSON**.
* Do đó, bài thi giữa kỳ bắt buộc phải là mô hình **Single Page (SPA)**:
  - Chỉ có **1 trang HTML duy nhất**.
  - Dùng **JavaScript (hàm `fetch()` hoặc `$.ajax()`)** để gọi tới Web Service ngầm.
  - Sau khi nhận JSON về thì dùng JavaScript để vẽ lại giao diện (cập nhật Combobox và Table) mà **KHÔNG HỀ F5 / RELOAD TRANG**!

### 2. Lúc thi: Thầy cung cấp sẵn Web Service!
* Thầy nói rõ: *"Cái Web Service nữa, lúc thi thầy sẽ cung cấp, cái Web Service cho các bạn không có làm"*.
* Tức là: Khi vào phòng thi, đề bài sẽ cho bạn một đường link Web Service (REST API backend) có sẵn, ví dụ:
  - `GET http://localhost:8080/api/faculties` (lấy danh sách Khoa)
  - `GET http://localhost:8080/api/faculties/{id}/students` (lấy sinh viên của Khoa)
  - `POST http://localhost:8080/api/faculties/{id}/students` (thêm sinh viên)
  - `PUT http://localhost:8080/api/students/{id}` (sửa sinh viên)
  - `DELETE http://localhost:8080/api/students/{id}` (xóa sinh viên)
* Việc của sinh viên trong phòng thi là: **TẬP TRUNG 100% VÀO LẬP TRÌNH GIAO DIỆN FRONTEND (HTML + JAVASCRIPT GỌI API)**.
* *(Tuy nhiên, để tự luyện tập ở nhà, chúng ta phải viết sẵn cả Backend Web Service trong dự án `gk` để giả lập y như đề thi của thầy!)*

### 3. Phạm vi thi giữa kỳ: Đúng 3 bước (BỎ Paging và Sorting)
Quy trình bài toán gồm 5 bước, nhưng thầy đã khoanh vùng giảm tải: **"GIỮA KỲ THẦY YÊU CẦU 3 BƯỚC ĐẦU THÔI"**:

```
[BƯỚC 1: Load Combobox]
Trang web vừa mở lên -> Javascript gọi Web Service lấy danh sách Khoa -> Đổ vào Combobox (<select>)
         │
         ▼
[BƯỚC 2: Chọn Combobox -> Load Table]
Người dùng chọn 1 Khoa trong Combobox (onchange) -> Gọi Web Service lấy danh sách Sinh viên của Khoa đó -> Đổ vào Table (<table>)
         │
         ▼
[BƯỚC 3: Đầy đủ bộ CRUD Thêm / Sửa / Xóa]
- Thêm mới sinh viên: Nhập Form -> Gọi API POST -> Cập nhật lại Table
- Sửa sinh viên: Bấm nút Sửa -> Gọi API PUT -> Cập nhật lại Table
- Xóa sinh viên: Bấm nút Xóa -> Gọi API DELETE -> Cập nhật lại Table
         │
         ✕ (KHÔNG THI GIỮA KỲ)
[Bước 4 & 5: Paging (Phân trang) & Sorting (Sắp xếp)] -> DÀNH CHO THI CUỐI KỲ!
```

---

## 🏆 PHẦN 4: 3 TIÊU CHÍ CHẤM ĐIỂM CỐT LÕI (MỤC TIÊU ĐÁNH GIÁ)

Khi thầy đi kiểm tra bài thi của bạn, thầy sẽ xem trực tiếp 3 hành vi sau trên trình duyệt:

1. **Tiêu chí 1: Đổ dữ liệu vào Combobox thành công (`GET`)**
   - Vừa vào trang web, danh sách các Khoa tự động hiện đầy đủ trong thẻ `<select>`.
   - Kiểm tra tab `Network` (F12) thấy có request `GET` trả về mã `200 OK` và response là mảng JSON.

2. **Tiêu chí 2: Tương tác Combobox load lại Table (`Event onchange`)**
   - Chọn Khoa Công Nghệ Thông Tin $\to$ Bảng Table hiển thị sinh viên CNTT.
   - Chọn chuyển sang Khoa Cơ Khí $\to$ Bảng Table lập tức đổi sang sinh viên Cơ Khí mà trang không hề bị load lại.

3. **Tiêu chí 3: Thao tác CRUD qua Web Service (`POST`, `PUT`, `DELETE`)**
   - Thêm 1 sinh viên mới $\to$ Bảng Table xuất hiện ngay sinh viên đó.
   - Bấm nút Sửa $\to$ Sửa tên sinh viên $\to$ Lưu thành công.
   - Bấm nút Xóa $\to$ Dòng sinh viên đó biến mất khỏi bảng Table.
   - Trong tab `Network`, các request tương ứng `POST`, `PUT`, `DELETE` đều được gửi đúng định dạng `application/json`.
