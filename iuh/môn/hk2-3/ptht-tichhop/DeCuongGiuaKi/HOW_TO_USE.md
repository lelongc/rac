# HƯỚNG DẪN ÔN THI: CÁCH CHUYỂN ĐỔI LOGIC VÀ MẠNG NGAY TRONG PHÒNG THI

Nếu bài thi rơi vào bất kỳ cấu trúc nào trong PDF (`bai-tap-cac-tuan.md`), bạn KHÔNG CẦN code lại hay nhớ công thức, bạn chỉ cần mở các file tương ứng và bôi đen Un-comment `(Ctrl + /)` đoạn mã có sẵn. 

## I. MẸO CHUNG XỬ LÝ ĐƯỜNG DẪN KHI RUN (ECLIPSE)
- Nếu dùng Eclipse bấm Run, file txt sinh ra đôi khi rớt ra ngoài chứ không nằm trong thư mục Package.
- Mình đã định nghĩa sẵn biến số `DIR = "DeCuongGiuaKi/4_Socket_TCP/"` (nằm ở đầu hàm while trong tệp `WorkerThread.java`).
- => **Tùy biến:** Tùy theo việc bạn Mở Thư mục gốc (`Workspace`) là cái gì mà bạn đổi lại tên biến `DIR`. Bạn hãy thử chạy test 1 dạng in file để kiểm tra. Nếu chạy trơn tru, đi thi cứ làm theo.

## II. LÀM QUEN VỚI THƯ MỤC "4_Socket_TCP" (Quân Cờ Chủ Đạo)
Phần lớn các đề thi Giữa Kì (80%) nằm trong thư mục này. Nó tổng hợp đầy đủ các logic DẠNG TỪ 1 -> 20. 

### 1. Cách Chọn Dạng Bài Tập Logic
1. Mở tệp `WorkerThread.java`.  
2. Cuộn chuột xuống thấy khung `[PHAN CHON LOGIC XU LY]`.  
3. Có 20 khối code mang nhãn từ `DANG 1` đến `DANG 20`.  
4. Mặc định `DANG 16` (Máy Tính Mini) đang mở. Nếu đề thi ra dạng khác, CHỈ VIỆC BÔI ĐEN `DANG 16` -> ẤN `CTRL + /` ĐỂ ĐÓNG NÓ LẠI (COMMENT).  
5. Sau đó kéo tìm Dạng bài thi yêu cầu, BÔI ĐEN TOÀN BỘ KHỐI -> ẤN `CTRL + /` ĐỂ MỞ RA. Xong!

### 2. Cách Chọn Dạng Mạng: TCP / UDP / TRUYỀN FILE BINARY 
**Nếu đề thi yêu cầu Chat 2 Chiều (Liên tục nhập - in đan xen, không chờ đợi):**  
- Mở `Client.java`.  
- TÌM khối `[DẠNG BÀI 2 TUẦN 5: CHAT HAI CHIỀU]`. Đóng Comment cái Vòng lặp `while(true)` chuẩn phía trên lại, và Mở `Thread receiveThread...` phía dưới ra.  

**Nếu đề thi yêu cầu làm UDP thay vì TCP:**  
- **Cả Server.java và Client.java** đều có khối code đóng băng sẵn ở tận cùng đáy File mang tên `[BLOCK UDP SERVER]` và `[BLOCK UDP CLIENT]`.  
- Chỉ cần: Lấy con trỏ bôi từ chổ `try (ServerSocket...)` (ở Server) hoặc `try (Socket...)` (ở Client) xuống hết vùng đó -> **Comment lại**.  
- Kéo xuống đáy bôi đen -> **Uncomment UDP Block**. Khởi động! 

**Nếu đề thi ra bài 7 cực sốc (Ném File Ảnh Nhị Phân dung lượng bự):**  
- Khối code siêu cấp này mình giấu ở đáy file `WorkerThread.java`.  
- Phải dùng `DataInputStream` thay vì `BufferedReader` mới rặn nổi. Bạn kéo xuống đáy file `WorkerThread.java`, comment bỏ khối TCP Text bình thường, và uncomment cái Khối "KHOI MA THAY THE DANH RIENG CHO BAI 7". 

---

## III. NẾU THI RƠI VÀO CÁC TUẦN KHÁC (1, 2, 3, 4, 6)
Không cần suy nghĩ nhức não. Đã chia ngăn nắp thành từng folder nguyên bản theo tuần. Chỉ cần nhấn Run bài cần làm. 

- **Cần Check IP?** Vào Mở thư mục `6_InetAddress_CoBan`, chạy `java DomainInfo google.com`.  
- **Cần Đa Luồng Wait/Notify Cắt Kéo Tổng?** Vào Mở thư mục `3_BaiTapThread`, chạy `BufferApp.java`.  
- **Cần Các Mô Hình Class Kế Thừa Tính Tiền?** Mở `2_OOP_IOStream`, đủ hết.  
- **Cần File/Folder Search/Delete đệ quy?** Mở `1_File_Folder`, chạy ThaoTacFile.  

*Dặn dò cuối: Bạn có thể truyền Tham số Command Line kiểu `java Client 192.168.1.5 8080`. Code trong các Client.java đều đã trang bị hàm đón args thông minh `if (args.length >= 2)`.*
