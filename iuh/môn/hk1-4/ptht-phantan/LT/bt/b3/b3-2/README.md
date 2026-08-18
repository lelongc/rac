# Bài 2 (Bài 3.2): Hệ Thống Quản Lý Vé Xe Trực Tuyến (RMI + TCP Socket + Multi-Threading)

## 📌 Yêu cầu đề bài
Xây dựng hệ thống quản lý và đặt vé xe trực tuyến phân tán:
1. **Server RMI**: Quản lý danh sách các chuyến xe, lộ trình, giá vé và số lượng ghế trống (`Trip`, `TicketService`).
2. **Xác nhận qua TCP Socket**: Khi client thực hiện đặt vé thành công qua RMI, Server sẽ mở một kết nối **Socket TCP** để truyền toàn bộ nội dung xác nhận và **hóa đơn điện tử** về máy Client.
3. **Xử lý Đa Luồng (Thread)**:
   - Sử dụng cơ chế đồng bộ (`synchronized`) khi trừ ghế để đảm bảo không bị xung đột (tránh overbooking) khi nhiều người cùng đặt 1 chuyến tại 1 thời điểm.
   - Sử dụng **Thread** riêng biệt khi Server gửi hóa đơn qua TCP để không làm nghẽn RMI Server khi có nhiều yêu cầu đặt vé cùng lúc.
   - Client sử dụng một **Daemon Thread** chạy `ServerSocket` để tự động lắng nghe và nhận hóa đơn từ Server gửi về.

---

## 📁 Cấu trúc các file mã nguồn
- `Trip.java`: Đối tượng đại diện cho chuyến xe (mã chuyến, tuyến đường, thời gian, số ghế trống, giá vé) với phương thức đặt ghế an toàn luồng (`synchronized boolean bookSeats(int count)`).
- `TicketService.java`: Giao diện từ xa (Remote Interface) khai báo các phương thức RMI: `getTripList()`, `checkTrip()`, `bookTicket()`.
- `TicketServiceImpl.java`: Lớp cài đặt (Remote Object) quản lý chuyến xe và kích hoạt **Thread** gửi hóa đơn qua **TCP Socket**.
- `TicketServer.java`: Khởi động RMI Registry tại cổng `1099` và đăng ký dịch vụ `TicketService`.
- `TicketClient.java`: Ứng dụng Client giao diện dòng lệnh, tạo luồng nhận hóa đơn qua TCP và gọi RMI để tra cứu & đặt vé.

---

## 🚀 Hướng dẫn biên dịch và chạy trên Terminal (PowerShell / CMD)

### Bước 1: Mở Terminal và di chuyển vào thư mục bài tập
```powershell
cd "d:\folder\rac\iuh\môn\hk1-4\ptht-phantan\LT\bt\b3\b3-2"
```

### Bước 2: Biên dịch toàn bộ các file Java
```powershell
javac *.java
```

### Bước 3: Khởi động Server (Terminal 1)
```powershell
java TicketServer
```
*Server sẽ khởi tạo RMI Registry tại cổng 1099 và sẵn sàng phục vụ các yêu cầu tra cứu và đặt vé.*

### Bước 4: Chạy các Client đặt vé (Mở Terminal 2, Terminal 3...)
Mỗi Terminal đóng vai trò là một khách hàng đang truy cập hệ thống đặt vé:

* **Khách hàng 1 (Terminal 2):**
  ```powershell
  cd "d:\folder\rac\iuh\môn\hk1-4\ptht-phantan\LT\bt\b3\b3-2"
  java TicketClient
  ```

* **Khách hàng 2 (Terminal 3):**
  ```powershell
  cd "d:\folder\rac\iuh\môn\hk1-4\ptht-phantan\LT\bt\b3\b3-2"
  java TicketClient
  ```

---

## 📋 Danh sách chuyến xe mẫu có sẵn trong hệ thống:
| Mã chuyến | Tuyến đường | Giờ khởi hành | Số ghế | Giá vé |
| :--- | :--- | :--- | :--- | :--- |
| **CX01** | TP.HCM -> Đà Lạt | 20:00 20/08 | 30 chỗ | 250,000 VND |
| **CX02** | TP.HCM -> Nha Trang | 21:30 20/08 | 28 chỗ | 280,000 VND |
| **CX03** | TP.HCM -> Vũng Tàu | 07:00 21/08 | 16 chỗ | 150,000 VND |
| **CX04** | TP.HCM -> Cần Thơ | 09:00 21/08 | 34 chỗ | 180,000 VND |
