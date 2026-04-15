# Tổng hợp Kiến thức Java RMI (Remote Method Invocation)

## 1. Khái niệm và Cách thức hoạt động
**Remote Method Invocation (RMI)** là một cơ chế trong Java phục vụ cho việc xây dựng các hệ thống phân tán. Nó cho phép một đối tượng (Object) chạy trên một máy ảo Java (JVM) này có thể triệu gọi (invoke) các phương thức của một đối tượng chạy trên một JVM khác.

### 1.1. Lớp trung gian: Stub và Skeleton
RMI không gọi trực tiếp mà thông qua các lớp trung gian:
- **Stub (Client-side):** Hoạt động như một gateway đại diện cho remote object phía Client.
  - Thiết lập kết nối tới JVM từ xa.
  - **Marshalling:** Đóng gói (serialize) các tham số.
  - Đợi kết quả và **Unmarshalling** giá trị trả về cho người gọi.
- **Skeleton (Server-side):** Hoạt động như gateway đại diện phía Server.
  - Nhận incoming request.
  - Unmarshalling tham số để gọi phương thức thực tế trên Server.
  - Marshalling kết quả trả về cho Client.

### 1.2. RMI Registry (Naming Service)
- Là một namespace (danh bạ) nơi Server đăng ký các đối tượng từ xa với một tên gọi riêng biệt (**bind name**).
- **Server:** Sử dụng `Naming.bind()` hoặc `Naming.rebind()` để đăng ký URL (ví dụ: `rmi://localhost:1099/MyService`).
- **Client:** Sử dụng `Naming.lookup()` với bind name để lấy về bản sao của Stub (reference).

---

## 2. Marshalling và Unmarshalling
- **Marshalling:** Quá trình đóng gói dữ liệu tham số vào một thông báo để truyền qua mạng. Nếu tham số là object, nó sẽ thực hiện **Serialization**.
- **Unmarshalling:** Quá trình giải nén thông báo để lấy lại dữ liệu thực tế. Nếu tham số là object, nó sẽ thực hiện **Deserialization**.
- **Lưu ý:** Đây cũng là nơi phát sinh các lỗ hổng bảo mật liên quan đến Deserialization.

---

## 3. Các bước xây dựng ứng dụng RMI
1. **Định nghĩa Remote Interface:**
   - Phải `extends Remote`.
   - Các phương thức phải ném ra `RemoteException`.
2. **Cài đặt triển khai (Implementation):**
   - Thường `extends UnicastRemoteObject` và `implements` interface vừa tạo.
3. **Cài đặt Server:**
   - Khởi tạo Registry: `LocateRegistry.createRegistry(port)`.
   - Đăng ký đối tượng: `Naming.rebind(url, object)`.
4. **Cài đặt Client:**
   - Tìm kiếm đối tượng: `(InterfaceName) Naming.lookup(url)`.
   - Triệu gọi phương thức như một đối tượng cục bộ.

---

## 4. Vấn đề Bảo mật và Khai thác (Security Labs)
RMI dựa trên cơ chế Serialization nên tiềm ẩn nhiều rủi ro về **Java Deserialization Vulnerability**.

### 4.1. JEP 290 (Java Enhancement Process)
Được giới thiệu từ bản **JDK 8u121**, nhằm hạn chế nguy cơ deserialization bằng cơ chế **Look Ahead Deserialization**.
- **Serialization Filters:** Kiểm tra tên lớp (Class Name) trước khi thực hiện deserialize thực tế.
- **Process-wide Filters:** Bộ lọc áp dụng cho toàn hệ thống thông qua tham số `-Djdk.serialFilter` hoặc file `java.security`.
- **Custom Filters:** Dev có thể ghi đè bộ lọc để tùy chỉnh whitelist/blacklist cho từng Stream cụ thể.

### 4.2. Khai thác ứng dụng (Exploit)
- **Trước JEP 290:** Sử dụng các tool như `ysoserial` (RMIRegistryExploit, JRMPClient) để gửi malicious serialized objects nếu trong classpath của server chứa các "gadget chain" (thư viện lỗi).
- **Sau JEP 290:** Oracle mặc định tạo ra các filter cho Registry và DGC (Distributed Garbage Collection) để chặn các gadget phổ biến. Tuy nhiên, vẫn có thể bị khai thác nếu Server cho phép truyền một Object tùy ý vào một phương thức (Method Argument type là `Object`). Khi đó, RMI server vẫn sẽ gọi `readObject()` để giải nén tham số mà không bị filter bảo vệ hoàn toàn.

---

## 5. Đặc tính nổi bật
- Là API bậc cao xây dựng trên nền tảng **Socket**.
- Truyền dữ liệu và mã lệnh (tham số) một cách trong suốt giữa các JVM.
- Cung cấp cơ chế **Callback** (Server gọi ngược lại phương thức ở Client).
- Sử dụng công cụ `rmic.exe` (trong các bản Java cũ) để tạo Stub và Skeleton.
