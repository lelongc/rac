# CẨM NANG ÔN THI & TEMPLATE GIỮA KỲ (GK) - PHÁT TRIỂN HỆ THỐNG PHÂN TÁN (IUH)

---

## I. GÓI TIỆN ÍCH CODE MẪU DÙNG CHUNG: `src/gkmodule`
Gói [src/gkmodule](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/ptht-phantan/gk/src/gkmodule) chứa các module tiện ích chuyên xử lý các yêu cầu phụ bất ngờ trong đề thi. **Khi thi, bạn chỉ cần mở các file này, copy đúng hàm mình cần rồi dán vào `ThreadProcess.java` hoặc `RemoteServiceImpl.java` (không cần nộp kèm cả package này để tránh thừa file)!**

1. **[RandomHelper.java](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/ptht-phantan/gk/src/gkmodule/RandomHelper.java)**:
   - `randomInt(min, max)`: Sinh số nguyên ngẫu nhiên.
   - `randomNumbersString(count, min, max)`: Sinh chuỗi số ngẫu nhiên (vd: `"12 85 43 9 77"`).
   - `generateRandomNumbersToFile(fileName, count, min, max)`: **Sinh N số ngẫu nhiên rồi GHI THẲNG VÀO FILE TEXT** (Đề thi rất hay ra bài này!).
   - `randomString(length)`: Sinh chuỗi ký tự ngẫu nhiên.

2. **[FileHelper.java](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/ptht-phantan/gk/src/gkmodule/FileHelper.java)**:
   - `readFile(fileName)`: Đọc toàn bộ nội dung file text thành 1 String.
   - `readLines(fileName)`: Đọc file text thành danh sách từng dòng.
   - `writeFile(fileName, content)`: Ghi đè chuỗi vào file text.
   - `appendFile(fileName, content)`: Ghi nối tiếp vào cuối file (Ghi log, lịch sử chat).
   - `readKeyValueFile(fileName)`: Đọc file dạng `key=value` (như file `users.txt`).
   - `copyFile(src, dest)`: Copy file bằng Byte Streams (Bài thực hành Tuần 3).
   - `writeObject(fileName, obj)` / `readObject(fileName)`: Đọc/Ghi đối tượng Serializable ra file nhị phân `.dat` (Bài thực hành Tuần 3).

3. **[StringHelper.java](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/ptht-phantan/gk/src/gkmodule/StringHelper.java)**:
   - `caesarEncrypt(text, key)` / `caesarDecrypt(text, key)`: Mã hóa & Giải mã Caesar.
   - `getNow()`: Lấy ngày giờ hiện tại định dạng `"yyyy-MM-dd HH:mm:ss"`.
   - `isValidEmail(email)` / `isValidPhone(phone)`: Kiểm tra định dạng Email, Số điện thoại.
   - `formatName(name)`: Chuẩn hóa họ tên (viết hoa chữ cái đầu mỗi từ).

4. **[DataHelper.java](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/ptht-phantan/gk/src/gkmodule/DataHelper.java)**:
   - `parseNumbers(input)`: Tách chuỗi thành `List<Double>`.
   - `formatList(list)`: Định dạng danh sách số (số nguyên không in `.0`).
   - `sum(list)`, `avg(list)`, `max(list)`, `min(list)`: Thống kê dãy số.
   - `sortAsc(list)`, `sortDesc(list)`: Sắp xếp tăng/giảm.
   - `filterEven(list)`, `filterOdd(list)`: Lọc số chẵn, số lẻ.

---

## II. DANH SÁCH 37 BÀI TOÁN RMI & QUY TẮC XỬ LÝ FILE `SinhVien.java`

Trong package [gkrmi](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/ptht-phantan/gk/src/gkrmi):
- [RMIServer.java](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/ptht-phantan/gk/src/gkrmi/RMIServer.java): Giữ nguyên 100% cho mọi bài (tự tạo Registry cổng 1099 và rebind).
- Cả 3 file [IRemoteService.java](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/ptht-phantan/gk/src/gkrmi/IRemoteService.java), [RemoteServiceImpl.java](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/ptht-phantan/gk/src/gkrmi/RemoteServiceImpl.java), và [RMIClient.java](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/ptht-phantan/gk/src/gkrmi/RMIClient.java) được chia thành **37 BLOCK ĐỒNG BỘ 1-1** (đầy đủ mọi dạng bài cơ bản & nâng cao như bên TCP Socket):

| STT | Tên bài toán RMI | Cần file `SinhVien.java`? | Thao tác khi thi |
| :---: | :--- | :---: | :--- |
| **BÀI 1** | **Máy tính 4 phép tính (+, -, *, /)** (Tuần 6 Bài 3) | ❌ **KHÔNG** | Mặc định đang bật. Chạy được ngay. |
| **BÀI 2** | **Tính tam giác** (Chu vi, diện tích Heron từ $a, b, c$) | ❌ **KHÔNG** | Uncomment Bài 2, comment Bài 1. |
| **BÀI 3** | **Số phức** (ADD, SUB, MUL, DIV) | ❌ **KHÔNG** | Uncomment Bài 3, comment Bài 1. |
| **BÀI 4** | **Số Fibonacci / In dãy Fibonacci** | ❌ **KHÔNG** | Uncomment Bài 4, comment Bài 1. |
| **BÀI 5** | **Quy đổi tiền tệ** (VND, USD, EUR, JPY) | ❌ **KHÔNG** | Uncomment Bài 5, comment Bài 1. |
| **BÀI 6** | **Kiểm tra số nguyên tố** (Prime check) | ❌ **KHÔNG** | Uncomment Bài 6, comment Bài 1. |
| **BÀI 7** | **Sắp xếp tăng dần danh sách số** | ❌ **KHÔNG** | Uncomment Bài 7, comment Bài 1. |
| **BÀI 8** | **Sắp xếp giảm dần danh sách số** | ❌ **KHÔNG** | Uncomment Bài 8, comment Bài 1. |
| **BÀI 9** | **Thống kê số lần xuất hiện của từng từ** | ❌ **KHÔNG** | Uncomment Bài 9, comment Bài 1. |
| **BÀI 10** | **Sắp xếp chuỗi từ theo bảng chữ cái** | ❌ **KHÔNG** | Uncomment Bài 10, comment Bài 1. |
| **BÀI 11** | **Đảo ngược chuỗi** | ❌ **KHÔNG** | Uncomment Bài 11, comment Bài 1. |
| **BÀI 12** | **Ngắt chuỗi theo ký tự phân cách (delimiter)** | ❌ **KHÔNG** | Uncomment Bài 12, comment Bài 1. |
| **BÀI 13** | **UCLN và BCNN** ($a, b$) | ❌ **KHÔNG** | Uncomment Bài 13, comment Bài 1. |
| **BÀI 14** | **Giải phương trình bậc 1** ($ax + b = 0$) | ❌ **KHÔNG** | Uncomment Bài 14, comment Bài 1. |
| **BÀI 15** | **Giải phương trình bậc 2** ($ax^2 + bx + c = 0$) | ❌ **KHÔNG** | Uncomment Bài 15, comment Bài 1. |
| **BÀI 16** | **Tính tổng 1..n** | ❌ **KHÔNG** | Uncomment Bài 16, comment Bài 1. |
| **BÀI 17** | **Đếm nguyên âm và phụ âm** | ❌ **KHÔNG** | Uncomment Bài 17, comment Bài 1. |
| **BÀI 18** | **Chuẩn hóa chuỗi** (Viết hoa chữ cái đầu mỗi từ) | ❌ **KHÔNG** | Uncomment Bài 18, comment Bài 1. |
| **BÀI 19** | **Kiểm tra Palindrome** (Chuỗi đối xứng) | ❌ **KHÔNG** | Uncomment Bài 19, comment Bài 1. |
| **BÀI 20** | **Tính giai thừa** ($n!$) | ❌ **KHÔNG** | Uncomment Bài 20, comment Bài 1. |
| **BÀI 21** | **Tính tổng các chữ số** (vd: `12345` -> `15`) | ❌ **KHÔNG** | Uncomment Bài 21, comment Bài 1. |
| **BÀI 22** | **Tính tổng danh sách số** | ❌ **KHÔNG** | Uncomment Bài 22, comment Bài 1. |
| **BÀI 23** | **Tìm Min và Max của danh sách số** | ❌ **KHÔNG** | Uncomment Bài 23, comment Bài 1. |
| **BÀI 24** | **Kiểm tra chẵn lẻ** | ❌ **KHÔNG** | Uncomment Bài 24, comment Bài 1. |
| **BÀI 25** | **Chuyển chuỗi sang IN HOA** | ❌ **KHÔNG** | Uncomment Bài 25, comment Bài 1. |
| **BÀI 26** | **Chuyển chuỗi sang in thường** | ❌ **KHÔNG** | Uncomment Bài 26, comment Bài 1. |
| **BÀI 27** | **Đếm tổng số ký tự** (có khoảng trắng & không khoảng trắng) | ❌ **KHÔNG** | Uncomment Bài 27, comment Bài 1. |
| **BÀI 28** | **Tính diện tích Hình chữ nhật** | ❌ **KHÔNG** | Uncomment Bài 28, comment Bài 1. |
| **BÀI 29** | **Tính diện tích Hình tròn** | ❌ **KHÔNG** | Uncomment Bài 29, comment Bài 1. |
| **BÀI 30** | **Tính diện tích Hình thang** | ❌ **KHÔNG** | Uncomment Bài 30, comment Bài 1. |
| **BÀI 31** | **Tính chu vi Hình vuông** | ❌ **KHÔNG** | Uncomment Bài 31, comment Bài 1. |
| **BÀI 32** | **Tính chu vi Hình chữ nhật** | ❌ **KHÔNG** | Uncomment Bài 32, comment Bài 1. |
| **BÀI 33** | **[ĐỀ THI GK CÂU 1] Chuyển số thành chữ** (`"3432"` -> `"ba bốn ba hai"`) | ❌ **KHÔNG** | Uncomment Bài 33, comment Bài 1. |
| **BÀI 34** | **[ĐỀ THI GK CÂU 2] Tìm thông tin theo Email** (từ DB/file `users.txt`) | ❌ **KHÔNG** | Uncomment Bài 34, comment Bài 1. |
| **BÀI 35** | **[THỰC HÀNH LAB 5] Sắp xếp dãy số** (in chuỗi gốc, giảm, tăng) | ❌ **KHÔNG** | Uncomment Bài 35, comment Bài 1. |
| **BÀI 36** | **[THỰC HÀNH TUẦN 3] Đọc nội dung file văn bản từ Server** (`users.txt`) | ❌ **KHÔNG** | Uncomment Bài 36, comment Bài 1. |
| **BÀI 37** | **[THỰC HÀNH TUẦN 1 & 3] Tìm đối tượng Sinh viên theo mã** | ✅ **CẦN DUY NHẤT BÀI NÀY** | Giữ file `SinhVien.java`, uncomment Bài 37. |

---

### ⚠️ QUY TẮC SỐNG CÒN VỀ FILE `SinhVien.java` KHI ĐI THI:
- **Nếu đề thi ra BẤT KỲ BÀI NÀO TỪ BÀI 1 ĐẾN BÀI 36:**
  👉 **HÃY XÓA THẲNG TAY FILE [SinhVien.java](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/ptht-phantan/gk/src/gkrmi/SinhVien.java) ĐI!**
  Dự án hoàn toàn KHÔNG BỊ LỖI, biên dịch và chạy 100% bình thường, giúp bài nộp **sạch sẽ, KHÔNG BỊ THỪA BẤT KỲ FILE NÀO**!
- **Chỉ khi nào đề yêu cầu:** *"Xây dựng lớp đối tượng Sinh viên (hoặc truyền nhận đối tượng qua mạng bằng RMI)"* thì bạn mới giữ lại file `SinhVien.java` và uncomment Bài 37.

---

## III. QUY TẮC CHO CÁC GÓI KHÁC (`gk`, `gkudp`, `gkchat`)
- Trong [src/gk](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/ptht-phantan/gk/src/gk) (TCP Socket) và [src/gkudp](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/ptht-phantan/gk/src/gkudp) (UDP Socket):
  - **HOÀN TOÀN KHÔNG CÓ và KHÔNG CẦN file `SinhVien.java`**!
  - 36 bài toán trong `ThreadProcess.java` đều xử lý chuỗi và số trực tiếp, không thừa file.
- Trong [src/gkchat](file:///d:/folder/rac/iuh/m%C3%B4n/hk1-4/ptht-phantan/gk/src/gkchat) (Chat Broadcast Tuần 4):
  - Chỉ có đúng 2 file: `ChatServer.java` và `ChatClient.java`, không có file thừa.

---

## IV. HƯỚNG DẪN KHI ĐI THI TẠO JAVA PROJECT MỚI
1. Mở Eclipse -> **File -> New -> Java Project** -> Đặt tên (ví dụ: `23630851_LeThanhLong`).
2. Mở thư mục code này ngoài Windows Explorer, copy package cần làm dán vào thư mục `src` của dự án thi:
   - Đề ra TCP -> Copy folder `gk` vào `src`.
   - Đề ra UDP -> Copy folder `gkudp` vào `src`.
   - Đề ra RMI -> Copy folder `gkrmi` vào `src` *(Nhớ xóa `SinhVien.java` nếu không làm bài Sinh viên)*.
   - Đề ra Chat -> Copy folder `gkchat` vào `src`.
   - Nếu cần tiện ích đọc file/sinh số ngẫu nhiên -> Mở file trong `gkmodule` copy đúng hàm cần thiết dán vào code của mình.
3. Nhấn **F5** trong Eclipse.
4. Uncomment đúng 1 bài cần làm -> Run -> Nộp bài!
