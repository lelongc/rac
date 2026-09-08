# Bài 5 - Phần 3 (b5-3): Dịch Vụ Tính Giai Thừa Phân Tán (Java RMI Trên 2 Máy Khác Nhau)

## 📌 Tổng quan bài tập (Ứng với Bài 3 trong Slide)
Xây dựng ứng dụng tính giai thừa từ xa chạy trên **hai máy tính vật lý khác nhau** (hoặc 2 tiến trình độc lập kết nối qua mạng LAN/Internet) bằng công nghệ **Java RMI**:
- **Máy A (Server Host)**: Tiếp nhận yêu cầu, thực thi thuật toán tính giai thừa, kiểm soát giới hạn tràn số và trả kết quả.
- **Máy B (Client App)**: Tra cứu dịch vụ qua địa chỉ IP của Máy A, đóng gói tham số (Marshalling) và hiển thị kết quả.

---

## 📁 Cấu trúc các file mã nguồn
1. `FactorialService.java`: Giao diện từ xa (Remote Interface) kế thừa `java.rmi.Remote`.
2. `FactorialServiceImpl.java`: Lớp cài đặt nghiệp vụ tính giai thừa phía Server (sử dụng vòng lặp chống tràn ngăn xếp `StackOverflowError`).
3. `FactorialServer.java`: Khởi động RMI Registry tại cổng `1099`, export đối tượng và đăng ký dịch vụ `"FactorialService"`.
4. `FactorialClient.java`: Kết nối đến Server qua IP và Port, gọi hàm từ xa và hiển thị kết quả.

---

## 🚀 Hướng dẫn chạy

### Cách 1: Chạy thử nghiệm trên cùng 1 máy tính (Localhost)
1. **Biên dịch:**
   ```powershell
   cd "d:\folder\rac\iuh\môn\hk1-4\ptht-phantan\LT\bt\b5\b5-3"
   javac *.java
   ```
2. **Khởi động Server (Terminal 1):**
   ```powershell
   java FactorialServer
   ```
3. **Chạy Client (Terminal 2):**
   ```powershell
   java FactorialClient
   ```

---

### Cách 2: Chạy thực tế trên 2 máy tính khác nhau qua mạng LAN / Wi-Fi
- **Máy A (Server):** Giả sử có IP LAN là `192.168.1.10`
- **Máy B (Client):** Kết nối chung mạng Wi-Fi/LAN với Máy A

1. **Trên Máy A:**
   - Biên dịch:
     ```powershell
     javac FactorialService.java FactorialServiceImpl.java FactorialServer.java
     ```
   - Chạy Server:
     ```powershell
     java FactorialServer
     ```
   - *(Lưu ý: Đảm bảo Windows Firewall trên máy A cho phép Java lắng nghe qua cổng 1099).*

2. **Trên Máy B:**
   - Chỉ cần copy 2 file: `FactorialService.java` và `FactorialClient.java`.
   - Biên dịch:
     ```powershell
     javac FactorialService.java FactorialClient.java
     ```
   - Chạy Client với tham số IP của Máy A:
     ```powershell
     java FactorialClient 192.168.1.10
     ```

---

## ❓ Trả lời các câu hỏi Bài 3 trong Slide
1. **Khác biệt cốt lõi giữa gọi cục bộ và RPC/RMI thật sự:**
   - *Cục bộ:* Chung không gian bộ nhớ RAM / JVM, gọi trực tiếp qua địa chỉ con trỏ, không qua mạng.
   - *RMI/RPC:* Hai tiến trình độc lập trên 2 máy khác nhau, dữ liệu phải được tuần tự hóa (Marshalling/Serialization) và truyền qua giao thức mạng TCP/IP Socket.
2. **Cần bổ sung gì để chạy trên 2 máy khác nhau?**
   - Remote Interface (`FactorialService extends Remote`).
   - Stub/Skeleton thông qua `exportObject`.
   - RMI Registry tại Server (cổng 1099).
   - Đổi địa chỉ kết nối của Client thành IP thực của Server (ví dụ `192.168.1.10`).
3. **Vấn đề khi đầu vào $n$ rất lớn (ví dụ $n = 50.000$):**
   - **Tràn số:** Kiểu `long` chỉ chứa tối đa $20!$. Với $n = 50.000$ cần dùng `BigInteger`.
   - **Tràn ngăn xếp:** Thuật toán đệ quy sẽ gây lỗi `StackOverflowError` làm sập Server, phải thay bằng vòng lặp (`for`/`while`).
   - **Timeout mạng:** Tính toán số quá lớn tốn thời gian khiến Client bị block treo ứng dụng hoặc timeout, cần dùng cơ chế Asynchronous RPC / Future.
   - **Tải mạng:** Dữ liệu kết quả có hàng trăm nghìn chữ số gây tốn băng thông đường truyền.
