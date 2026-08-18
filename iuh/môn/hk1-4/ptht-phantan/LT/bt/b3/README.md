# Bài 3: Trò Chơi Đoán Số Nhiều Người Chơi Qua Java RMI

## 📌 Yêu cầu đề bài
Phát triển trò chơi đoán số nhiều người chơi (Multiplayer Number Guessing Game) qua công nghệ **Java RMI (Remote Method Invocation)**:
- **Server**: Quản lý danh sách người chơi, điểm số, tạo số bí mật ngẫu nhiên (1 - 100) theo từng vòng chơi, cập nhật bảng xếp hạng.
- **Người chơi (Client)**: Tham gia phòng bằng Nickname/Tên, nhập số dự đoán, nhận gợi ý (`>` hoặc `<`) từ Server.
- **Tính điểm & Đồng bộ**: Khi có người đoán đúng số bí mật, Server cộng điểm (+10 điểm) cho người đó và tự động tạo số bí mật mới cho vòng tiếp theo cho tất cả người chơi trong phòng.

---

## 📁 Cấu trúc các file mã nguồn
- `GameService.java`: Giao diện từ xa (Remote Interface) kế thừa `java.rmi.Remote`.
- `GameServiceImpl.java`: Lớp cài đặt (Remote Object) kế thừa `UnicastRemoteObject`, xử lý logic trò chơi và tính điểm.
- `RMIServer.java`: Chương trình khởi tạo RMI Registry tại cổng `1099` và đăng ký dịch vụ `GameService`.
- `RMIClient.java`: Chương trình Client kết nối RMI Registry, cho phép người chơi tương tác, nhập số đoán, xem điểm và bảng xếp hạng.

---

## 🚀 Hướng dẫn biên dịch và chạy trên Terminal (PowerShell / CMD)

### Bước 1: Mở Terminal và di chuyển vào thư mục bài tập
```powershell
cd "d:\folder\rac\iuh\môn\hk1-4\ptht-phantan\LT\bt\b3"
```

### Bước 2: Biên dịch toàn bộ các file Java
```powershell
javac *.java
```

### Bước 3: Chạy Server (Mở ở Terminal 1)
```powershell
java RMIServer
```
*Server sẽ tự động kích hoạt RMI Registry trên cổng 1099 và lắng nghe kết nối từ các người chơi.*

### Bước 4: Chạy các Client (Mở ở Terminal 2, Terminal 3...)
Mở thêm các cửa sổ Terminal mới để đóng vai trò các người chơi khác nhau:

* **Người chơi 1 (Terminal 2):**
  ```powershell
  cd "d:\folder\rac\iuh\môn\hk1-4\ptht-phantan\LT\bt\b3"
  java RMIClient
  ```

* **Người chơi 2 (Terminal 3):**
  ```powershell
  cd "d:\folder\rac\iuh\môn\hk1-4\ptht-phantan\LT\bt\b3"
  java RMIClient
  ```

---

## 🎮 Các lệnh hỗ trợ trong trò chơi (Client):
* Nhập một số bất kỳ từ `1` đến `100` để đoán.
* Gõ `bxh` để xem bảng xếp hạng điểm của tất cả người chơi trong phòng.
* Gõ `diem` để xem điểm hiện tại của chính mình.
* Gõ `thoat` để rời khỏi phòng chơi.
