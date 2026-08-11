# Bài 4: Chương Trình Đoán Số (Client-Server TCP & UDP)

## 📌 Đề bài
Viết chương trình đoán số hoạt động theo mô hình Client-Server bằng Java:
1. Khi Client kết nối, Server tạo ngẫu nhiên một số nguyên $n \le 100$ (từ 1 đến 100).
2. Client đoán số, Server trả về gợi ý: số vừa đoán **LỚN HƠN** hay **NHỎ HƠN** số bí mật $n$.
3. Quá trình lặp lại liên tục cho đến khi Client đoán đúng ($= n$).
4. Server in ra thống kê: **Số lần đoán** và **Tổng thời gian đoán** (tính bằng giây).

---

## 📁 Cấu trúc File
- `TCPServer.java`: Server TCP xử lý đa luồng (Multi-threading).
- `TCPClient.java`: Client TCP kết nối và tương tác với người dùng.
- `UDPServer.java`: Server UDP quản lý phiên chơi qua `DatagramSocket`.
- `UDPClient.java`: Client UDP kết nối và tương tác với người dùng.

---

## 🚀 Hướng Dẫn Chạy Trên Terminal (PowerShell / CMD)

### Cách 1: Chạy chương trình TCP (Giao thức TCP Socket - Đề Bài Yêu Cầu)

#### 1. Mở Terminal thứ nhất và di chuyển vào thư mục bài tập:
```powershell
cd "d:\folder\rac\iuh\môn\hk1-4\ptht-phantan\LT\bt\b2"
```

#### 2. Biên dịch mã nguồn Java:
```powershell
javac TCPServer.java TCPClient.java
```

#### 3. Chạy Server trước:
```powershell
java TCPServer
```

#### 4. Mở thêm 1 Terminal thứ hai (hoặc nhiều hơn) để chạy Client:
```powershell
cd "d:\folder\rac\iuh\môn\hk1-4\ptht-phantan\LT\bt\b2"
java TCPClient
```

---

### Cách 2: Chạy chương trình UDP (Giao thức UDP DatagramSocket)

#### 1. Biên dịch:
```powershell
javac UDPServer.java UDPClient.java
```

#### 2. Chạy UDP Server ở Terminal 1:
```powershell
java UDPServer
```

#### 3. Chạy UDP Client ở Terminal 2:
```powershell
java UDPClient
```
