# BẢNG KỊCH BẢN KIỂM THỬ TOÀN DIỆN HỆ THỐNG TỔNG ĐÀI VOIP ASTERISK
## (HƯỚNG DẪN TEST & DEMO BẢO VỆ ĐỒ ÁN ĐẠT ĐIỂM 10)

**Môn học:** Quản trị dịch vụ mạng  
**Đơn vị:** Đại học Công nghiệp TP.HCM (IUH)  
**Địa chỉ Server IP hiện tại:** `10.160.130.164` (Wi-Fi Hotspot) / `192.168.1.100` (LAN nội bộ)

---

## 📋 BẢNG DANH SÁCH THIẾT BỊ & TÀI KHOẢN HỆ THỐNG

| Thiết bị | Loại thiết bị | Tài khoản (User/Pass) | Domain / Server IP | Số gọi ngắn | Số di động thật | Vai trò trong hệ thống |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Win 7 - Máy 1** | Máy ảo VMware (MicroSIP) | `101` / `123456` | `192.168.1.100` | **`101`** | - | **Giám Đốc** (Quyền cao nhất) |
| **Win 7 - Máy 2** | Máy ảo VMware (MicroSIP) | `102` / `123456` | `192.168.1.100` | **`102`** | - | **Phòng Kinh Doanh** |
| **Điện thoại 1** | Smartphone thật (Sipnetic/Zoiper) | `103` / `123456` | `10.160.130.164` | **`103`** | **`0987214065`** | **Di động Cá nhân 1** |
| **Điện thoại 2** | Smartphone thật (Sipnetic/Zoiper) | `104` / `123456` | `10.160.130.164` | **`104`** | **`0981647882`** | **Di động Cá nhân 2** |
| **Số Tổng Đài** | Hệ thống tự động | - | - | **`100`** | - | **IVR Lời chào tương tác** |
| **Số Gọi Nhóm** | Tính năng tổng đài | - | - | **`600`** | - | **Ring Group (Rung tất cả máy)** |

---

## 🧪 QUY TRÌNH KIỂM THỬ 7 KỊCH BẢN ĐỀ BÀI (STEP-BY-STEP)

---

### 🟢 TEST 1: GỌI SỐ THẬT 10 CHỮ SỐ (ĐIỂM NHẤN ĂN ĐIỂM CỦA THẦY)

* **Mục tiêu:** Chứng minh tổng đài có khả năng định tuyến trực tiếp bằng **số điện thoại di động thật 10 chữ số** của sinh viên tới thiết bị vật lý thật ngoài đời.
* **Các bước thực hiện:**
  1. **Lượt 1 (Gọi Điện thoại 1):**
     - Từ máy tính Win 7 (MicroSIP) hoặc từ Điện thoại 2: Mở bàn phím gõ đúng số: **`0987214065`**.
     - Bấm nút **Call (Gọi)**.
     - 👉 **Kết quả:** Điện thoại 1 cầm trên tay lập tức reo chuông to rõ. Bấm nghe, đàm thoại 2 chiều thông suốt!
  2. **Lượt 2 (Gọi Điện thoại 2):**
     - Từ máy tính Win 7 (MicroSIP) hoặc từ Điện thoại 1: Gõ đúng số: **`0981647882`**.
     - Bấm nút **Call (Gọi)**.
     - 👉 **Kết quả:** Điện thoại 2 cầm trên tay reo chuông, bắt máy nghe nói 2 chiều to rõ!
* **💡 Câu trả lời khi Thầy hỏi:**  
  *"Thưa Thầy, em cấu hình Dialplan trên Asterisk để ánh xạ (Mapping) số di động thật ngoài đời của em vào máy nhánh PJSIP. Khi ai đó bấm 10 số di động thật, Asterisk sẽ tự động chuyển tiếp cuộc gọi qua giao thức SIP tới đúng chiếc Smartphone thật này ạ!"*

---

### 🟢 TEST 2: GỌI NHÓM ĐỒNG THỜI (RING GROUP - SỐ `600`)

* **Mục tiêu:** Khi có sự cố khẩn cấp hoặc khách hàng cần hỗ trợ, 1 cuộc gọi sẽ kích hoạt tất cả các phòng ban cùng reo chuông.
* **Các bước thực hiện:**
  1. Dùng bất kỳ máy nào (Ví dụ: Điện thoại 1 hoặc Win 7 Máy 2).
  2. Mở bàn phím gõ số: **`600`** ➔ Bấm **Call**.
  3. 👉 **Kết quả thực tế:**
     - Cả máy Win 7 Giám Đốc (`101`), Win 7 Kinh Doanh (`102`), Điện thoại 1 (`103`) và Điện thoại 2 (`104`) **đồng thời đổ chuông reo vang cùng một lúc**!
     - Bất kỳ máy nào nhấc máy trước sẽ bắt đàm thoại, các máy còn lại tự động ngừng reo.

---

### 🟢 TEST 3: GỌI NỘI BỘ SỐ NGẮN DI ĐỘNG (EXT `103` & `104`)

* **Mục tiêu:** Kiểm tra khả năng gọi song song bằng số máy nhánh nội bộ truyền thống.
* **Các bước thực hiện:**
  1. Từ Win 7 (`101` hoặc `102`): Bấm gọi số ngắn **`103`** ➔ Điện thoại 1 đổ chuông.
  2. Từ Điện thoại 1: Bấm gọi số ngắn **`104`** ➔ Điện thoại 2 đổ chuông.
  3. 👉 **Kết quả:** Cuộc gọi kết nối ngay tức thì, độ trễ cực thấp (< 20ms).

---

### 🟢 TEST 4: NHẮN TIN TỨC THỜI SIP (SIP MESSAGING)

* **Mục tiêu:** Trao đổi tin nhắn văn bản trực tiếp giữa máy tính PC và Smartphone qua mạng VoIP.
* **Các bước thực hiện:**
  1. Trên phần mềm MicroSIP của Win 7:
     - Chuyển sang tab **Messages** (biểu tượng lá thư / tin nhắn).
     - Ô người nhận: Điền số **`103`** (hoặc điền số thật **`0987214065`**).
     - Khung soạn thảo: Gõ nội dung *"Xin chào, đây là tin nhắn kiểm tra đồ án VoIP IUH!"*.
     - Bấm nút **Send** (ở góc dưới bên phải).
  2. 👉 **Kết quả:** Trên màn hình Điện thoại 1 xuất hiện ngay **thông báo tin nhắn Pop-up** với đầy đủ nội dung vừa gửi!
  3. Có thể thử nhắn ngược lại từ Điện thoại về máy Win 7 để thấy tin nhắn 2 chiều.

---

### 🟢 TEST 5: PHÂN QUYỀN VÀ CHẶN CUỘC GỌI TỚI GIÁM ĐỐC (BLACKLIST / SECURITY)

* **Mục tiêu:** Bảo vệ sự riêng tư cho Giám đốc, chỉ cho phép Giám đốc gọi xuống nhân viên, cấm nhân viên tự ý gọi quấy rầy Giám đốc.
* **Các bước thực hiện:**
  1. **Lượt 1 (Giám đốc gọi nhân viên - Thành công):**
     - Từ máy Giám đốc (`101`): Bấm gọi số `102`, `103` hoặc `0987214065`.
     - 👉 **Kết quả:** Cuộc gọi thành công, nhân viên đổ chuông bình thường.
  2. **Lượt 2 (Nhân viên gọi Giám đốc - BỊ CHẶN):**
     - Từ máy Nhân viên (`102`, `103`, `104`): Bấm gọi số Giám đốc: **`101`**.
     - 👉 **Kết quả:** Cuộc gọi **BỊ CHẶN NGAY LẬP TỨC!**
     - Đầu dây người gọi nghe thấy âm báo tiếng Anh: *"The number you have dialed is not in service..."* (`ss-noservice`) và tổng đài tự động ngắt kết nối!

---

### 🟢 TEST 6: HỘP THƯ THOẠI & GỬI GMAIL CUỘC GỌI NHỠ (VOICEMAIL TO GMAIL)

* **Mục tiêu:** Khi người nhận bận không bắt máy, tổng đài tự động ghi âm lời nhắn và gửi email kèm file ghi âm `.wav` về hòm thư Gmail của người dùng.
* **Các bước thực hiện:**
  1. Từ máy Nhân viên: Bấm gọi Giám đốc thông qua Tổng đài IVR:
     - Bấm gọi số **`100`** ➔ Nghe lời chào tự động.
     - Bấm phím **`1`** để kết nối tới Giám đốc (`101`).
  2. Trên máy Giám đốc: **Cố tình KHÔNG BẮT MÁY**.
  3. Sau 20 giây reo chuông không ai trả lời, tổng đài tự động phát thông báo:
     *"Please leave your message after the tone..."* và phát 1 tiếng **BÍP**.
  4. Người gọi nói vào micro lời nhắn: *"Em chào Giám đốc, em gọi báo cáo tiến độ đồ án mạng ạ!"*.
  5. Nói xong, bấm nút **Kết thúc cuộc gọi (Cúp máy)**.
  6. 👉 **Kết quả kiểm tra:**
     - Mở hộp thư Gmail `lelong191001@gmail.com`.
     - Trong vòng 10 - 30 giây, một email mới xuất hiện từ **Asterisk PBX** với tiêu đề:
       `[IUH-VoIP] Cuoc goi nho tu ...`
     - Mở email ra: Thấy nội dung chào hỏi trang trọng và **1 tệp đính kèm file âm thanh `.wav`** chứa chính xác giọng nói bạn vừa để lại!

---

### 🟢 TEST 7: TỔNG ĐÀI TƯƠNG TÁC GIỌNG NÓI TỰ ĐỘNG (IVR - SỐ `100`)

* **Mục tiêu:** Cung cấp menu thoại hướng dẫn tự động như các tổng đài 1900 của nhà mạng/ngân hàng.
* **Các bước thực hiện:**
  1. Bấm gọi số **`100`** từ bất kỳ máy nào.
  2. Lắng nghe tổng đài phát đoạn âm thanh chào mừng (IVR Welcome Prompt).
  3. **Thử phím 1:** Bấm phím **`1`** trên bàn phím số ➔ Cuộc gọi tự chuyển hướng reo chuông máy Giám đốc (`101`).
  4. **Thử phím 2:** Gọi lại `100`, bấm phím **`2`** ➔ Cuộc gọi tự chuyển sang Phòng Kinh Doanh (`102`).
  5. **Thử phím sai:** Gọi `100`, bấm phím lạ (ví dụ phím `9`) ➔ Tổng đài phát âm báo phím không hợp lệ (`invalid`) và tự động quay lại phát menu ban đầu.

---

## 🏆 CHECKLIST ĐÁNH GIÁ TRƯỚC KHI BẢO VỆ

| STT | Tên bài kiểm tra | Thao tác bấm gọi | Kết quả mong đợi | Trạng thái |
| :---: | :--- | :--- | :--- | :---: |
| 1 | Gọi số thật 1 | Gõ `0987214065` | Điện thoại 1 reo chuông, đàm thoại 2 chiều | [ ] ĐẠT |
| 2 | Gọi số thật 2 | Gõ `0981647882` | Điện thoại 2 reo chuông, đàm thoại 2 chiều | [ ] ĐẠT |
| 3 | Gọi nhóm | Gõ `600` | 4 máy reo chuông cùng lúc | [ ] ĐẠT |
| 4 | Gọi số ngắn | Gõ `103` / `104` | Điện thoại reo chuông tức thì | [ ] ĐẠT |
| 5 | Nhắn tin SIP | Soạn tin gửi `103` / `104` | Điện thoại nhận tin nhắn Pop-up | [ ] ĐẠT |
| 6 | Chặn cuộc gọi | `102` gọi `101` | Bị chặn, nghe âm báo ss-noservice | [ ] ĐẠT |
| 7 | Hộp thư thoại | Để lại lời nhắn khi bận | Nhận email kèm file `.wav` về Gmail | [ ] ĐẠT |
| 8 | Tổng đài IVR | Gõ `100` -> Bấm 1, 2 | Chuyển máy tự động theo phím bấm | [ ] ĐẠT |
