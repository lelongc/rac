# 🏆 BÍ KÍP VÀO PHÒNG THI - TÌM NHANH DIỆT GỌN (TỪ TUẦN 1 TỚI TUẦN 6)

Tuyệt đối KHÔNG gõ lại Code dài dòng từ đầu. Nhìn lướt đề, xác định Tuần/Dạng -> Mở file -> Ấn `Ctrl + /` mở Comment ra -> CHẠY.

---

## 🎯 PHẦN I: BẢNG TRA CỨU NHANH (TÌM FILE -> UNCOMMENT LÀ XONG)

| TUẦN 📚 | ĐỀ BÀI KIỂM TRA MÔ TẢ GÌ? | 👉 MỞ FILE NÀY ĐỂ UN-COMMENT LÀM BÀI |
|---|---|---|
| **Tuần 1** | 👉 **Toán Console, Switch/Case** (In tên, Tháng, Tính tổng, Chẵn lẻ) | Mở `1_File_Folder\BaiTapTuan1_Logic.java`. Có đủ 5 Dạng cơ bản. |
| **Tuần 1** | 👉 **Quản Lý Vườn Thú OOP** (Sư tử, Rắn, Khỉ) | Mở `1_File_Folder\QuanLyVuonThu.java`. Ấn Run là chạy do code sẵn class. |
| **Tuần 1** | 👉 **Tìm Kiếm, Xóa File Đệ Quy Folder** | Mở `1_File_Folder\ThaoTacFile.java`. Code đã hoàn thiện chức năng I/O. |
| **Tuần 2** | 👉 **Tính Thuế, Lương (OOP Phương Tiện, Nhân Viên, Chó/Mèo)** | Mở `2_OOP_IOStream\Main.java`. Gỡ comment `DANG 1`, `DANG 2`, HOẶC `DANG 3`. |
| **Tuần 3** | 👉 **Đọc/Ghi 4 chuẩn Stream (InputStream, Byte Array, Scanner/PW)**| Mở `2_OOP_IOStream\BasicStream.java`. Un-comment `DANG 1` đến `DANG 4`. |
| **Tuần 4** | 👉 **Đa Luồng (Thread, Writer/Reader File)** | Mở `3_BaiTapThread\Main.java`. Có đủ `DANG 1` (3 luồng ghi), `DANG 2` (Đọc), `DANG 3` (Đồng Bộ). |
| **Tuần 4** | 👉 **Người Sản Xuất & Tiêu Dùng (Thread Wait/Notify Kho)** | Mở `3_BaiTapThread\Main.java`. Gỡ thả khối `DANG 4`. |
| **Tuần 5** | 👉 **Socket Mạng (Tính Tổng N, Menu Giờ, Operant/Toán, IP)** | Mở `4_Socket_TCP\WorkerThread.java`. (Kéo Dạng 1 tới DANG 20 siêu tốc). |
| **Tuần 5** | 👉 **Chat Liên Tục TCP Server-Client (Vòng lặp True Threading)** | Mở `4_Socket_TCP\Client.java`. Đóng block mặc định, mở khối ReceiveChat ra. |
| **Tuần 5** | 👉 **Gửi Bắn Tập Tin NHỊ PHÂN Cỡ Lớn (Ảnh, File cài)** | Mở đáy tệp `WorkerThread.java` -> Bật khối `[DataInputStream]` thay cho Buffer. |
| **Tuần 6** | 👉 **Nhập Domain/IP trả về Thông Tin, Kiểm tra Loopback** | Mở `6_InetAddress_CoBan\Main.java`. Gỡ khối `DANG 1` tới `DANG 4`. |

---

## 🛠 PHẦN II: HƯỚNG DẪN DÙNG TERMINAL TRONG ECLIPSE ĐỂ CHẠY ARGS (Tham Số Dòng Lệnh)
Ở Tuần 5 và Tuần 6 có những bài bắt nhập số hoặc nhập IP TỪ LÚC CHẠY CHƯƠNG TRÌNH `String[] args` (Vd: Bài bắt bật Client bắn vô `192.168.1.1 8080`).  

Cách làm Cực Đỉnh qua Terminal:
1. Trong Eclipse, **Nhấp chuột phải vào thư mục gốc của Bạn (Vd: `DeCuongGiuaKi`)** ở cây thư mục bên trái (Package Explorer).
2. Chọn **`Show in` \> `Local Terminal` \> `Terminal`**. Một cửa sổ đen mốc ở phía dưới đáy sẽ hiên lên.
3. Ở ô gõ lệnh, biên dịch (biến Java thành Class) bằng lệnh:  
   ```bash
   javac -encoding UTF-8 "4_Socket_TCP\*.java"
   ```
4. Sau đó Gọi nó chạy có kèm Tham Số:  
   ```bash
   java Socket_TCP_Thread.Client 127.0.0.1 8080
   ```
   *(Nhớ thay `Socket_TCP_Thread` bằng dòng `package` ở đầu tệp bạn nhắm tới. Vd Week 6 thì là `java InetAddress_CoBan.Main google.com`)*

---

## ⚡ PHẦN III: QUY TRÌNH SIÊU TỐC TRONG PHÒNG THI RƠI VÀO BÀI SOCKET (TUẦN 5)
Tuần 5 Socket nhai 80% mọi đề cương. Toàn bộ Logic đề bài đã nhồi sẵn vào `WorkerThread.java` (TCP) hoặc `UDPServer.java` (UDP).

**Cách thao tác:**
1. Đọc đề xem có yêu cầu TCP hay UDP không? -> Chọn 1 trong 2 tệp.
2. Vô tệp đó cuộn xuống hàm `while((inputLine = in.readLine()) != null)`.
3. Có sẵn khối ghi chú: `DANG 1 (Viết hoa)`  ->  `DANG 16 (Toán Mini)` -> `DANG 20 (OP)`.
4. Tìm thấy đề thuộc Dạng Máy, dùng chuột Bôi Đen Block đó.
5. Ấn tổ hợp phím **`Ctrl + /`** để UN-COMMENT toàn bộ cái Dạng Đó ra (Nó hóa thành màu thường, không còn xám).
6. Hãy chắc chắn các dạng còn lại Đang Là Màu Xám Comment (Nếu có dạng bị dính lây chưa tắt, cứ quyét khối nó và ấn **`Ctrl + /`** là nó câm ngay).
7. Run con Server lên.  
8. Chạy con Client. Gõ phép tính và gặt điểm Mười! 🥇

**Lưu ý Về Lỗi Nhầm File TXT Lạc Lõng:**
> Ở Tuần 5, mình đã cắm 1 biến `DIR = "DeCuongGiuaKi/4_Socket_TCP/"` tuỳ theo cây thư mục gốc Workspace của bạn để xuất File cho sạch. Nếu Run mà bạn ko thấy cái File TXT được đẻ ra ở chung với Code, thì nó đã bắn tuốt rà ngoài Desktop hoặc thư mục cha. Chú ý sửa biến `DIR` tùy theo môi trường lúc thi báo cáo của bạn.
