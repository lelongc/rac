# Bài 5 - Phần 2 (b5-2): Hệ Thống Máy Tính Từ Xa Java RMI Chuẩn 4 File

## 📌 Tổng quan bài tập (Ứng với Bài 2 trong Slide)
Chuyển đổi bài toán gọi hàm từ xa (RPC/RMI) từ dạng mã nguồn giả lập ban đầu sang **mô hình hệ thống phân tán chuẩn 4 file** trong Java RMI:
- **Tách biệt vai trò**: Giao diện (Interface), Nghiệp vụ (Implementation), Máy chủ (Server), Máy khách (Client).
- **Tính năng**: Thực hiện các phép tính số học từ xa: `add`, `subtract`, `multiply`.
- **Cơ chế**: Sử dụng `UnicastRemoteObject.exportObject(obj, 0)` giúp lớp nghiệp vụ không bị ràng buộc kế thừa cứng với `UnicastRemoteObject`.

---

## 📁 Cấu trúc các file mã nguồn
1. `Calculator.java`: Giao diện từ xa (Remote Interface), kế thừa `java.rmi.Remote`, khai báo các hàm ném `RemoteException`.
2. `CalculatorImpl.java`: Lớp cài đặt nghiệp vụ tính toán (thuần túy `implements Calculator`).
3. `CalculatorServer.java`: Khởi tạo RMI Registry tại cổng `1099`, export đối tượng và đăng ký dịch vụ `"CalcService"`.
4. `CalculatorClient.java`: Kết nối đến Registry, tra cứu stub và gọi các hàm từ xa.

---

## 🚀 Hướng dẫn biên dịch và chạy

### Bước 1: Mở Terminal và di chuyển vào thư mục bài tập
```powershell
cd "d:\folder\rac\iuh\môn\hk1-4\ptht-phantan\LT\bt\b5\b5-2"
```

### Bước 2: Biên dịch tất cả các file Java
```powershell
javac *.java
```

### Bước 3: Khởi động Server (Terminal 1)
```powershell
java CalculatorServer
```

### Bước 4: Chạy Client (Terminal 2)
```powershell
# Chạy trên máy cục bộ (localhost):
java CalculatorClient

# Hoặc truyền địa chỉ IP nếu Server ở máy tính khác trong mạng LAN:
java CalculatorClient 192.168.1.10
```

---

## ❓ Trả lời các câu hỏi Bài 2 trong Slide
1. **Tại sao `Calculator` phải `extends Remote` và các method phải `throws RemoteException`?**
   - `Remote` là marker interface thông báo cho JVM và RMI runtime rằng đối tượng có thể được gọi từ xa qua mạng.
   - `RemoteException` là Checked Exception bắt buộc để xử lý các sự cố mạng tiềm ẩn (mất mạng, server crash, lỗi marshalling...).
2. **Ý nghĩa của `UnicastRemoteObject.exportObject(obj, 0)`:**
   - Xuất đối tượng thông thường thành remote stub có thể tiếp nhận kết nối TCP từ xa. Cổng `0` yêu cầu hệ điều hành tự động cấp một cổng trống ngẫu nhiên. Giúp class giữ được khả năng kế thừa lớp cha khác.
3. **Nếu Server chạy trên máy A (IP: 192.168.1.10) và Client trên máy B:**
   - Sửa dòng tra cứu Registry trong Client thành: `LocateRegistry.getRegistry("192.168.1.10", 1099);`.
4. **Khi mở rộng thêm hàm `multiply`:**
   - Cần cập nhật 3 file: `Calculator.java` (thêm chữ ký), `CalculatorImpl.java` (cài đặt logic), và `CalculatorClient.java` (lời gọi hàm). Server không cần sửa đổi.
