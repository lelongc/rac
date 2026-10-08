# CẨM NANG ÔN THI & TEMPLATE GIỮA KỲ (GK) - PHÁT TRIỂN HỆ THỐNG PHÂN TÁN (IUH)

---

## I. MA TRẬN PHÂN TÍCH ĐỀ THI GIỮA KỲ & THỰC HÀNH (TH TUẦN 1 - 6)

| Tuần / Đề bài | Trọng tâm kiến thức | Khả năng ra thi GK | Dạng câu hỏi thường gặp khi thi |
| :--- | :--- | :---: | :--- |
| **Đề thi mẫu GK (Câu 1)** | UDP Socket xử lý chuỗi | **RẤT CAO** | Chuyển số thành chữ (VD: `"3432"` -> `"3432: ba bốn ba hai"`), đảo chuỗi, đếm nguyên âm/phụ âm. |
| **Đề thi mẫu GK (Câu 2)** | TCP Socket tìm kiếm đối tượng | **RẤT CAO** | Nhận email/mã số, tìm kiếm trong mảng/Map/file rồi trả về thông tin (Tên, SĐT, Địa chỉ). |
| **TH Tuần 5 (Lab 5)** | TCP Socket dãy số | **RẤT CAO** | Nhập dãy số (`"11 22 4 25 28 3"`), trả về chuỗi gốc + chuỗi sắp giảm dần + chuỗi sắp tăng dần. |
| **TH Tuần 6 (RMI)** | Java RMI (Registry + Remote) | **RẤT CAO** | - Bài 1: Tự tạo Registry bằng `LocateRegistry.createRegistry(1099)`<br>- Bài 2: RMI truyền IP/Port động qua args<br>- Bài 3: Dịch vụ tính toán (+ - * /), giải PT, UCLN, kiểm tra số nguyên tố, đối tượng SinhVien. |
| **TH Tuần 4** | Multi-client Chat Socket | **TRUNG BÌNH** | Server đa luồng trung gian broadcast tin nhắn cho các client khác. |
| **TH Tuần 3** | Object Streams & Serialization | **LỒNG GHÉP** | Đối tượng `SinhVien implements Serializable` truyền qua Stream hoặc qua RMI. |
| **TH Tuần 1** | OOP cơ bản | **LỒNG GHÉP** | Xây dựng lớp Sinh viên: mã, họ tên, điểm TB, hàm `rank()` xếp loại. |

---

## II. BỘ 3 TEMPLATE SẴN CÓ TRONG THƯ MỤC `gk`

Trong thư mục `d:\folder\rac\iuh\môn\hk1-4\ptht-phantan\gk\`:

1. **Thư mục `gk/`**: Template **TCP Socket** (Đa luồng `ThreadProcess`, chứa sẵn 35 bài toán nghiệp vụ).
2. **Thư mục `gkudp/`**: Template **UDP Socket** (Client gửi DatagramPacket, Server xử lý 35 bài toán nghiệp vụ).
3. **Thư mục `gkrmi/`**: Template **Java RMI** (Gồm `IRemoteService`, `RemoteServiceImpl`, `RMIServer`, `RMIClient`, `SinhVien` Serializable).

---

## III. HƯỚNG DẪN "ĐI THI MANG VÔ BIẾT XÓA CÁI GÌ, CHỪA LẠI CÁI GÌ"

---

### TRƯỜNG HỢP 1: ĐỀ THI YÊU CẦU **TCP SOCKET**
*Dùng thư mục `gk/`*

1. **File `Server.java`**:
   - **Giữ nguyên 100%**: Đã có sẵn lắng nghe cổng `5000` và đa luồng `new ThreadProcess(s, clientId).start()`.
   - Nếu đề bài yêu cầu đổi cổng (ví dụ: `8888`, `6789`), chỉ cần sửa dòng:
     ```java
     static final int PORT = 5000; // Đổi số port theo đề
     ```

2. **File `Client.java`**:
   - **Giữ nguyên 100%**: Đã có sẵn vòng lặp đọc từ bàn phím `Scanner`, gửi `out.println()`, nhận và in kết quả `in.readLine()`.

3. **File `ThreadProcess.java` (QUAN TRỌNG NHẤT)**:
   - Mở hàm `public static String processData(String data)`:
   - **Cách làm**:
     - Xem đề yêu cầu bài nào (xem danh sách 35 bài đã đánh số rõ ràng).
     - **Uncomment bài đó** (bỏ 2 dấu `//`).
     - **Xóa tất cả các bài còn lại** (hoặc comment lại).
   - **Ví dụ các bài phổ biến nhất**:
     + **Câu 2 Đề thi (Tìm email)**: Tìm đến `BAI 33: ĐỀ THI GIỮA KỲ CÂU 2`, uncomment.
     + **Lab 5 (Sắp xếp dãy số)**: Tìm đến `BAI 34: THỰC HÀNH LAB 5`, uncomment.
     + **Câu 1 Đề thi (Chuyển số thành chữ)**: Tìm đến `BAI 32: ĐỀ THI GIỮA KỲ CÂU 1`, uncomment.
     + **Xếp loại sinh viên**: Tìm đến `BAI 35: THỰC HÀNH LAB 1`, uncomment.

---

### TRƯỜNG HỢP 2: ĐỀ THI YÊU CẦU **UDP SOCKET**
*Dùng thư mục `gkudp/`*

1. **File `Server.java`**:
   - **Giữ nguyên 100%**: Đã có sẵn `DatagramSocket(PORT)`, nhận `DatagramPacket`, gọi `ThreadProcess.processData(msg)` và gửi gói tin phản hồi lại cho Client.

2. **File `Client.java`**:
   - **Giữ nguyên 100%**: Đã có sẵn `DatagramSocket`, nhập dữ liệu từ bàn phím, đóng gói `DatagramPacket` gửi lên Server và nhận kết quả in ra màn hình.

3. **File `ThreadProcess.java`**:
   - Thao tác hoàn toàn giống hệt trường hợp TCP ở trên: Chỉ cần tìm bài tương ứng trong 35 bài có sẵn, uncomment bài cần làm và xóa các bài khác.

---

### TRƯỜNG HỢP 3: ĐỀ THI YÊU CẦU **JAVA RMI**
*Dùng thư mục `gkrmi/`*

1. **File `RMIServer.java`**:
   - **Giữ nguyên 100%**: Đã tự động tạo Registry tại cổng 1099 (`LocateRegistry.createRegistry(PORT)`), đăng ký dịch vụ `Naming.rebind(...)`.

2. **File `IRemoteService.java`**:
   - Nếu đề bài yêu cầu chỉ làm 1 hoặc 2 chức năng cụ thể:
     + **Chừa lại**: Các khai báo phương thức mà đề yêu cầu (ví dụ: `int add(int a, int b)`, `String doiSoThanhChu(String s)`...).
     + **Xóa**: Những hàm không liên quan (để code gọn gàng, giáo viên nhìn vào thấy đúng trọng tâm đề).

3. **File `RemoteServiceImpl.java`**:
   - Giữ lại các hàm đã chừa trong `IRemoteService.java`.
   - Xóa các hàm không dùng tới.
   - Nếu đề bài yêu cầu tìm kiếm người dùng / sinh viên: Chỉ cần sửa lại dữ liệu mẫu trong `userDatabase` hoặc `sinhVienList` theo đúng ví dụ của đề bài.

4. **File `RMIClient.java`**:
   - Đã chuẩn bị sẵn 5 mẫu demo tương ứng:
     + Mẫu 1: Đổi số thành chữ (Câu 1 GK)
     + Mẫu 2: Tìm kiếm theo Email (Câu 2 GK)
     + Mẫu 3: Sắp xếp dãy số (Lab 5)
     + Mẫu 4: Máy tính 4 phép tính (Tuần 6 Bài 3)
     + Mẫu 5: Đối tượng SinhVien (Tuần 1, 3)
   - Đi thi ra dạng nào thì **giữ lại mẫu đó**, xóa 4 mẫu còn lại đi.

5. **File `SinhVien.java`**:
   - Dùng khi đề bài liên quan đến truyền nhận đối tượng (bắt buộc phải có `implements Serializable`).

---

## IV. BẢNG TRA CỨU NHANH 35 BÀI TOÁN SẴN CÓ TRONG `ThreadProcess.java`

- **Bài 1**: Tam giác (Chu vi, diện tích Heron).
- **Bài 2**: Số phức (Cộng, trừ, nhân, chia $a+bi$ và $c+di$).
- **Bài 3**: Fibonacci (Tính số thứ $n$, in dãy).
- **Bài 4**: Quy đổi tiền tệ (USD, EUR, JPY, VND).
- **Bài 5**: Kiểm tra số nguyên tố.
- **Bài 6**: Sắp xếp tăng dần.
- **Bài 7**: Sắp xếp giảm dần.
- **Bài 8**: Thống kê số lần xuất hiện của từ.
- **Bài 9**: Sắp xếp mảng chuỗi theo chữ cái.
- **Bài 10**: Đảo ngược chuỗi.
- **Bài 11**: Tách chuỗi theo ký tự phân cách (`text|delimiter`).
- **Bài 12**: UCLN và BCNN.
- **Bài 13**: Giải phương trình bậc 1 ($ax + b = 0$).
- **Bài 14**: Giải phương trình bậc 2 ($ax^2 + bx + c = 0$).
- **Bài 15**: Tính tổng $1 + 2 + \dots + n$.
- **Bài 16**: Đếm nguyên âm, phụ âm.
- **Bài 17**: Chuẩn hóa chuỗi (Viết hoa chữ cái đầu).
- **Bài 18**: Kiểm tra chuỗi Palindrome (chuỗi đối xứng).
- **Bài 19**: Tính giai thừa ($n!$).
- **Bài 20**: Tính tổng các chữ số của một số nguyên.
- **Bài 21**: Tính tổng danh sách các số.
- **Bài 22**: Tìm Min, Max trong danh sách số.
- **Bài 23**: Kiểm tra chẵn, lẻ.
- **Bài 24**: Chuyển chuỗi sang IN HOA.
- **Bài 25**: Chuyển chuỗi sang in thường.
- **Bài 26**: Đếm tổng số ký tự (có tính và không tính khoảng trắng).
- **Bài 27**: Tính diện tích hình chữ nhật.
- **Bài 28**: Tính diện tích hình tròn.
- **Bài 29**: Tính diện tích hình thang.
- **Bài 30**: Tính chu vi hình vuông.
- **Bài 31**: Tính chu vi hình chữ nhật.
- **Bài 32**: **[ĐỀ THI GK CÂU 1]** Chuyển số thành chữ (VD: `"3432"` -> `"3432: ba bốn ba hai"`).
- **Bài 33**: **[ĐỀ THI GK CÂU 2]** Tìm thông tin người dùng theo Email (VD: `"abcd1234@gmail.com"` -> Tên + SĐT).
- **Bài 34**: **[THỰC HÀNH LAB 5]** Sắp xếp dãy số (In chuỗi gốc, giảm dần, tăng dần).
- **Bài 35**: **[THỰC HÀNH LAB 1]** Xếp loại học sinh/sinh viên theo điểm TB.
