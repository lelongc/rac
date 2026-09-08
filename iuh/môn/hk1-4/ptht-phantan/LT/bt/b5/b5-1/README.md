# Bài 5 - Phần 1 (b5-1): Phân Tích Mã Nguồn Giả Lập Ban Đầu (Slide Bài 1)

## 📌 Mã nguồn trong Slide Bài 1
Chương trình minh họa cách gọi hàm thông qua lớp `RPCServer` và `RPCClient`:
```java
class RPCServer {
    public int add(int a, int b) {
        System.out.println("Server nhận yêu cầu cộng: " + a + " + " + b);
        return a + b;
    }
}

public class RPCClient {
    public static void main(String[] args) {
        RPCServer server = new RPCServer();
        int result = server.add(5, 7); // giả lập remote call
        System.out.println("Kết quả nhận từ Server: " + result);
    }
}
```

---

## 📁 Cấu trúc các file mã nguồn
1. `RPCServer.java`: Định nghĩa lớp máy chủ cục bộ và phương thức `add(int a, int b)`.
2. `RPCClient.java`: Chứa hàm `main`, khởi tạo `RPCServer` và gọi hàm `add`.

---

## 🚀 Hướng dẫn biên dịch và chạy thử
```powershell
cd "d:\folder\rac\iuh\môn\hk1-4\ptht-phantan\LT\bt\b5\b5-1"
javac *.java
java RPCClient
```

---

## ❓ Trả lời 3 câu hỏi trong Slide Bài 1

### 1. Tại sao nói đoạn code trên CHƯA PHẢI là RPC thực sự?
* **Cùng không gian bộ nhớ (Same Memory / JVM):** Client tự tạo `new RPCServer()` ngay trong hàm `main`, cả Client và Server chạy chung trong 1 tiến trình và 1 không gian RAM của máy tính.
* **Là gọi hàm cục bộ:** Lệnh `server.add(5, 7)` chỉ là truy xuất con trỏ bộ nhớ RAM, **không hề có kết nối mạng (Socket TCP/IP)** và **không có cơ chế đóng gói dữ liệu (Marshalling)**.

### 2. RPC thật sự cần thêm những thành phần nào để chạy trên 2 máy khác nhau?
* **Remote Interface (`extends Remote`):** Bản hợp đồng giao diện dùng chung giữa Client và Server.
* **Client Stub (Proxy):** Đại diện phía Client, có nhiệm vụ **đóng gói (Marshalling)** tên hàm và tham số gửi qua mạng.
* **Server Skeleton / Dispatcher:** Lắng nghe trên mạng, **giải nén (Unmarshalling)**, gọi hàm thực thi trên Server và gửi kết quả về.
* **Hạ tầng mạng (TCP Sockets):** Truyền tải các gói tin Request - Reply giữa 2 máy.
* **Dịch vụ định danh (RMI Registry):** Cho phép Client tra cứu (Lookup) vị trí IP/Port của Server theo tên dịch vụ.

### 3. Muốn mở rộng nhiều hàm (`add`, `subtract`, `multiply`), ta cần thay đổi gì?
* **Interface:** Bổ sung khai báo `int subtract(int a, int b)` và `int multiply(int a, int b)`.
* **Server:** Viết mã thực thi xử lý cho `subtract` và `multiply`.
* **Client:** Gọi các hàm này thông qua Stub từ xa.
*(Hệ thống hoàn chỉnh này được triển khai đầy đủ ở thư mục `b5-2`).*
