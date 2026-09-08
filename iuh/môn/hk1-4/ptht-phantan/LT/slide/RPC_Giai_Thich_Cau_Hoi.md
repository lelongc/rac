# Kiến Trúc RPC / Java RMI: Từ Giả Lập Đến Hệ Thống Chuẩn 4 File

---

## 1. Phân Tích Đoạn Code Giả Lập Ban Đầu (Slide Bài 1)

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

### ❓ Trả lời 3 câu hỏi trong slide:

1. **Tại sao nói đoạn code trên CHƯA PHẢI là RPC thực sự?**

   * **Cùng không gian bộ nhớ (Same Memory / JVM):** Client tự tạo `new RPCServer()` ngay trong hàm `main`, cả 2 chạy chung trong 1 tiến trình máy tính.
   * **Là gọi hàm cục bộ:** Lệnh `server.add(5, 7)` chỉ là truy xuất con trỏ bộ nhớ RAM, **không hề có kết nối mạng (Socket TCP/IP)** và **không có cơ chế đóng gói dữ liệu (Marshalling)**.
2. **RPC thật sự cần thêm những thành phần nào để chạy trên 2 máy khác nhau?**

   * **Remote Interface (`extends Remote`):** Bản hợp đồng giao diện dùng chung giữa Client và Server.
   * **Client Stub (Proxy):** Đại diện phía Client, có nhiệm vụ **đóng gói (Marshalling)** tên hàm và tham số gửi qua mạng.
   * **Server Skeleton / Dispatcher:** Lắng nghe trên mạng, **giải nén (Unmarshalling)**, gọi hàm thực thi trên Server và gửi kết quả về.
   * **Hạ tầng mạng (TCP Sockets):** Truyền tải các gói tin Request - Reply giữa 2 máy.
   * **Dịch vụ định danh (RMI Registry):** Cho phép Client tra cứu (Lookup) vị trí IP/Port của Server theo tên dịch vụ.
3. **Muốn mở rộng nhiều hàm (`add`, `subtract`, `multiply`), ta cần thay đổi gì?**

   * **Interface:** Bổ sung khai báo `int subtract(int a, int b)` và `int multiply(int a, int b)`.
   * **Server:** Viết mã thực thi xử lý cho `subtract` và `multiply`.
   * **Client:** Gọi các hàm này thông qua Stub từ xa.

---

## 2. Tại Sao Hệ Thống Java RMI (RPC) Chuẩn Cần Đúng 4 File?

Trong thực tế, một hệ thống Java RMI được phân chia thành **4 file độc lập** theo đúng kiến trúc phân tán:

```text
               ┌────────────────────────────────────────────────────────┐
               │         1. Calculator.java (Remote Interface)          │
               │   (Chứa khai báo: add, subtract, multiply)             │
               └───────────────────────────┬────────────────────────────┘
                                           │
                    ┌──────────────────────┴──────────────────────┐
                    ▼                                             ▼
┌────────────────────────────────────────┐   ┌────────────────────────────────────────┐
│ 2. CalculatorImpl.java (Business Logic)│   │                                        │
│   (Cài đặt logic tính toán thực tế)    │   │                                        │
├────────────────────────────────────────┤   │                                        │
│ 3. CalculatorServer.java (Server Host) │   │ 4. CalculatorClient.java (Client App)  │
│   - exportObject() tạo Stub            │   │   - lookup("CalcService") lấy Stub     │
│   - LocateRegistry.createRegistry(1099)│   │   - Gọi stub.add(10, 20) qua TCP Socket│
│   - registry.rebind("CalcService")     │   │                                        │
└────────────────────────────────────────┘   └────────────────────────────────────────┘
            [ MÁY CHỦ SERVER ]                           [ MÁY KHÁCH CLIENT ]
```

1. **`Calculator.java`**: Interface chung khai báo các hàm từ xa.
2. **`CalculatorImpl.java`**: Lớp cài đặt nghiệp vụ tính toán (thuần túy, không dính líu đến mạng).
3. **`CalculatorServer.java`**: Chương trình máy chủ (chứa hàm `main`, tạo Registry 1099, export đối tượng và đăng ký dịch vụ).
4. **`CalculatorClient.java`**: Chương trình máy khách (chứa hàm `main`, kết nối Registry, lấy Stub và gọi hàm từ xa).

---

## 3. Mã Nguồn Đầy Đủ 4 File Chuẩn (Bài 2 Hoàn Thiện Bài 1)

---

### 1️⃣ `Calculator.java` (Remote Interface)

```java
import java.rmi.Remote;
import java.rmi.RemoteException;

// Giao diện từ xa: Phải extends Remote và các hàm phải ném RemoteException
public interface Calculator extends Remote {
    int add(int a, int b) throws RemoteException;
    int subtract(int a, int b) throws RemoteException;
    int multiply(int a, int b) throws RemoteException;
}
```

---

### 2️⃣ `CalculatorImpl.java` (Lớp Thực Thi Nghiệp Vụ Trên Server)

```java
import java.rmi.RemoteException;

// Lớp nghiệp vụ thuần túy: implements Calculator (Không cần extends UnicastRemoteObject)
public class CalculatorImpl implements Calculator {
    @Override
    public int add(int a, int b) throws RemoteException {
        System.out.println("[Server] Thực hiện phép cộng: " + a + " + " + b);
        return a + b;
    }

    @Override
    public int subtract(int a, int b) throws RemoteException {
        System.out.println("[Server] Thực hiện phép trừ: " + a + " - " + b);
        return a - b;
    }

    @Override
    public int multiply(int a, int b) throws RemoteException {
        System.out.println("[Server] Thực hiện phép nhân: " + a + " * " + b);
        return a * b;
    }
}
```

---

### 3️⃣ `CalculatorServer.java` (Chương Trình Khởi Động Server)

```java
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class CalculatorServer {
    public static void main(String[] args) {
        try {
            // 1. Tạo đối tượng xử lý nghiệp vụ
            CalculatorImpl obj = new CalculatorImpl();

            // 2. Xuất đối tượng (Export) thành Remote Stub lắng nghe trên cổng ngẫu nhiên (port 0)
            Calculator stub = (Calculator) UnicastRemoteObject.exportObject(obj, 0);

            // 3. Khởi tạo RMI Registry tại cổng 1099
            Registry registry = LocateRegistry.createRegistry(1099);

            // 4. Đăng ký dịch vụ với tên định danh "CalcService"
            registry.rebind("CalcService", stub);

            System.out.println("[SERVER] Calculator RMI Server đã sẵn sàng phục vụ tại cổng 1099...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

---

### 4️⃣ `CalculatorClient.java` (Chương Trình Máy Khách Gọi Từ Xa)

```java
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class CalculatorClient {
    public static void main(String[] args) {
        try {
            // 1. Kết nối tới RMI Registry của Server (mặc định localhost cổng 1099)
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);

            // 2. Tra cứu (Lookup) dịch vụ qua tên "CalcService" để nhận về Stub đại diện
            Calculator stub = (Calculator) registry.lookup("CalcService");

            System.out.println("========== KẾT QUẢ GỌI HÀM TỪ XA (RPC / RMI) ==========");

            // 3. Gọi hàm từ xa: Stub tự động đóng gói qua Socket TCP tới Server và nhận kết quả
            int sum = stub.add(10, 20);
            System.out.println("Kết quả add(10, 20)       = " + sum);

            int diff = stub.subtract(50, 15);
            System.out.println("Kết quả subtract(50, 15)  = " + diff);

            int product = stub.multiply(6, 8);
            System.out.println("Kết quả multiply(6, 8)   = " + product);

            System.out.println("=======================================================");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

---

## 4. Giải Thích Điểm Quan Trọng: Tại Sao Bài 2 Lại Hoàn Thiện Hơn Bài 1?

| Tiêu chí                     | Bài 1 (Cách cũ / Giả lập)                                                       | Bài 2 (Cách chuẩn 4 file với`exportObject`) ⭐                                                |
| :----------------------------- | :----------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------- |
| **Số lượng file**     | 1 file gộp chung                                                                    | **Tách biệt rõ ràng 4 file** (Interface, Impl, Server, Client)                            |
| **Kế thừa Class**      | Server bị ép`extends UnicastRemoteObject` (Mất khả năng kế thừa lớp khác) | `CalculatorImpl` chỉ `implements Calculator`, **vẫn có thể kế thừa lớp cha khác** |
| **Cơ chế kích hoạt** | Tự động qua constructor                                                           | Dùng lệnh tường minh:`UnicastRemoteObject.exportObject(obj, 0)`                               |
| **Môi trường chạy**  | Chỉ chạy trên 1 máy                                                              | Chạy độc lập trên**2 máy tính riêng biệt qua mạng LAN / Internet**                  |

---

## 5. 🚀 Hướng Dẫn Chạy Thử Trên Terminal

1. **Biên dịch toàn bộ 4 file:**

   ```powershell
   javac Calculator.java CalculatorImpl.java CalculatorServer.java CalculatorClient.java
   ```
2. **Khởi động Server (Terminal 1):**

   ```powershell
   java CalculatorServer
   ```
3. **Khởi động Client (Terminal 2):**

   ```powershell
   java CalculatorClient
   ```

---

## 6. ❓ Trả Lời Chi Tiết Các Câu Hỏi Bài 2 Trong Slide

### **Câu 1: Trong ví dụ RMI, tại sao interface `Calculator` phải `extends Remote` và method phải `throws RemoteException`?**

* **`extends Remote`**:
  * `java.rmi.Remote` là một **Marker Interface** (Interface đánh dấu).
  * Nó báo hiệu cho máy ảo Java (JVM) và RMI Runtime biết rằng interface này chứa các phương thức có thể được **gọi từ xa (Remote Invocations)** từ một máy ảo Java khác qua mạng, chứ không chỉ là gọi hàm cục bộ.
* **`throws RemoteException`**:
  * Khi gọi hàm qua mạng, luôn tiềm ẩn nguy cơ xảy ra sự cố truyền thông phân tán (mất mạng, đứt cáp, server crash, timeout, lỗi đóng gói dữ liệu Marshalling...).
  * `RemoteException` là một **Checked Exception** bắt buộc, ép lập trình viên phía Client phải viết khối `try-catch` để xử lý sự cố mạng, đảm bảo tính chịu lỗi (Fault Tolerance) của hệ thống.

---

### **Câu 2: Ý nghĩa của lệnh `UnicastRemoteObject.exportObject(obj, 0)` trong server là gì?**

* **Ý nghĩa chính**:
  1. Biến đối tượng Java thông thường `obj` (thể hiện của `CalculatorImpl`) thành một **Remote Object (Stub)** có khả năng lắng nghe và nhận các lời gọi hàm từ xa qua giao thức TCP/IP.
  2. Trả về đối tượng đại diện **`stub`** để Server đem đi đăng ký vào danh bạ RMI Registry (`rebind`).
* **Ý nghĩa của số `0`**:
  * `0` đại diện cho **cổng ngẫu nhiên (Anonymous / Ephemeral Port)**.
  * Yêu cầu Hệ điều hành (OS) tự động cấp phát một cổng TCP trống bất kỳ để lắng nghe, tránh bị lỗi xung đột cổng (Port conflict) với các tiến trình khác.
* **Ưu điểm lớn**: Giúp lớp `CalculatorImpl` không bị bắt buộc phải kế thừa `UnicastRemoteObject`, nhờ đó vẫn có thể `extends` một lớp cha khác nếu cần (vì Java không hỗ trợ đa kế thừa class).

---

### **Câu 3: Nếu server chạy trên máy A (IP: `192.168.1.10`) và client chạy trên máy B, thì ta cần sửa dòng nào trong client?**

* **Dòng cần sửa trong `CalculatorClient.java`**:
  ```java
  // Dòng cũ (khi chạy cùng 1 máy):
  Registry registry = LocateRegistry.getRegistry("localhost", 1099);

  // Dòng sửa lại (để Client ở máy B kết nối sang Server ở máy A):
  Registry registry = LocateRegistry.getRegistry("192.168.1.10", 1099);
  ```
* **Giải thích**: Thay đổi tham số địa chỉ Host từ `"localhost"` (máy cục bộ) thành địa chỉ IP mạng thực tế của máy Server A là `"192.168.1.10"`.

---

### **Câu 4: So sánh điểm khác biệt chính giữa RPC và RMI trong Java.**

| Tiêu chí                              | RPC (Remote Procedure Call)                                                                                        | RMI (Remote Method Invocation)                                                                                                                                                                                 |
| :-------------------------------------- | :----------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mô hình lập trình**         | **Hướng thủ tục (Procedural):** Gọi các hàm/thủ tục (Functions / Procedures) độc lập.            | **Hướng đối tượng (Object-Oriented):** Gọi các phương thức (Methods) trên các đối tượng cụ thể (`Remote Objects`).                                                                  |
| **Hỗ trợ ngôn ngữ**           | Thường**đa ngôn ngữ** (ví dụ: gRPC, JSON-RPC, ONC RPC) kết nối giữa C, C++, Python, Java...        | Thiết kế**chuyên biệt cho ngôn ngữ Java** (Java-to-Java communication).                                                                                                                            |
| **Truyền dữ liệu**             | Chỉ truyền các kiểu dữ liệu nguyên thủy (primitive) hoặc cấu trúc dữ liệu phẳng (Struct, JSON, XML). | Có thể truyền cả**Đối tượng Java đầy đủ (Objects)** qua cơ chế Tuần tự hóa (**Java Serialization**) hoặc truyền tham chiếu đối tượng từ xa (**Remote References**). |
| **Cách định nghĩa Interface** | Cần dùng file IDL riêng (`.proto`, `.idl`) rồi biên dịch sinh mã nguồn.                                | Viết trực tiếp bằng ngôn ngữ Java thuần (`interface Calculator extends Remote`).                                                                                                                      |

---

### **Câu 5: Nếu muốn bổ sung thêm hàm `multiply(int a, int b)`, ta phải thay đổi những file nào?**

Ta cần cập nhật **cả 3 file** sau:

1. **`Calculator.java` (Interface)**: Khai báo thêm chữ ký phương thức:
   ```java
   int multiply(int a, int b) throws RemoteException;
   ```
2. **`CalculatorImpl.java` (Business Logic)**: Cài đặt xử lý thực tế cho phép nhân:
   ```java
   @Override
   public int multiply(int a, int b) throws RemoteException {
       return a * b;
   }
   ```
3. **`CalculatorClient.java` (Client App)**: Gọi hàm mới qua đối tượng Stub:
   ```java
   int product = stub.multiply(6, 8);
   System.out.println("Kết quả multiply(6, 8) = " + product);
   ```

*(Lưu ý: File `CalculatorServer.java` **không cần thay đổi**, vì nó chỉ làm nhiệm vụ export và đăng ký đối tượng `CalculatorImpl` lên Registry).*

---

# 7. Bài 3: Chương Trình Tính Giai Thừa Từ Xa (Chạy Trên 2 Máy Khác Nhau)

---

## 📌 Đoạn Code Giả Lập Trong Slide

```java
class RPCServer {
    public long factorial(int n) {
        if (n <= 1) return 1;
        return n * factorial(n - 1);
    }
}

public class RPCClient {
    public static void main(String[] args) {
        RPCServer server = new RPCServer(); // giả lập gọi remote
        int number = 5;
        long result = server.factorial(number);
        System.out.println("Giai thừa của " + number + " = " + result);
    }
}
```

---

## 💻 Chuyển Đổi Thành Hệ Thống RMI Chuẩn 4 File (Chạy Trên 2 Máy Khác Nhau)

---

### 1️⃣ `FactorialService.java` (Remote Interface)

```java
import java.rmi.Remote;
import java.rmi.RemoteException;

// Giao diện từ xa: Bắt buộc extends Remote và method ném RemoteException
public interface FactorialService extends Remote {
    long factorial(int n) throws RemoteException;
}
```

---

### 2️⃣ `FactorialServiceImpl.java` (Lớp Nghiệp Vụ Tính Giai Thừa Phía Server)

```java
import java.rmi.RemoteException;

// Cài đặt logic nghiệp vụ thuần túy
public class FactorialServiceImpl implements FactorialService {
    @Override
    public long factorial(int n) throws RemoteException {
        System.out.println("[Server] Nhận yêu cầu tính giai thừa của n = " + n);
        if (n < 0) {
            throw new IllegalArgumentException("Không tính được giai thừa cho số âm!");
        }
        long result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
}
```

---

### 3️⃣ `FactorialServer.java` (Chương Trình Server - Chạy trên Máy A)

```java
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class FactorialServer {
    public static final int PORT = 1099;
    public static final String SERVICE_NAME = "FactorialService";

    public static void main(String[] args) {
        try {
            // 1. Tạo đối tượng xử lý tính giai thừa
            FactorialServiceImpl obj = new FactorialServiceImpl();

            // 2. Xuất đối tượng (Export) thành Remote Stub trên cổng ngẫu nhiên (port 0)
            FactorialService stub = (FactorialService) UnicastRemoteObject.exportObject(obj, 0);

            // 3. Khởi tạo máy chủ danh bạ RMI Registry tại cổng 1099
            Registry registry = LocateRegistry.createRegistry(PORT);

            // 4. Đăng ký dịch vụ vào Registry với tên "FactorialService"
            registry.rebind(SERVICE_NAME, stub);

            System.out.println("==================================================================");
            System.out.println("[SERVER] Factorial RMI Server đang chạy và lắng nghe tại cổng " + PORT + "...");
            System.out.println("[SERVER] Đã đăng ký dịch vụ: '" + SERVICE_NAME + "'");
            System.out.println("==================================================================");

        } catch (Exception e) {
            System.err.println("[-] Lỗi khởi động Server: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
```

---

### 4️⃣ `FactorialClient.java` (Chương Trình Client - Chạy trên Máy B)

```java
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class FactorialClient {
    // Địa chỉ IP mặc định của máy Server (thay đổi hoặc truyền qua tham số dòng lệnh)
    public static final String DEFAULT_SERVER_IP = "localhost";
    public static final int PORT = 1099;
    public static final String SERVICE_NAME = "FactorialService";

    public static void main(String[] args) {
        // Cho phép nhập IP Server qua tham số dòng lệnh (ví dụ: java FactorialClient 192.168.1.10)
        String serverHost = (args.length > 0) ? args[0] : DEFAULT_SERVER_IP;

        try {
            System.out.println("[CLIENT] Đang kết nối tới Server RMI tại " + serverHost + ":" + PORT + "...");

            // 1. Kết nối tới RMI Registry của Máy Server A qua IP và Port
            Registry registry = LocateRegistry.getRegistry(serverHost, PORT);

            // 2. Tra cứu (Lookup) dịch vụ từ xa qua tên "FactorialService"
            FactorialService stub = (FactorialService) registry.lookup(SERVICE_NAME);

            System.out.println("[CLIENT] Kết nối thành công! Bắt đầu gọi hàm tính giai thừa từ xa:");
            System.out.println("------------------------------------------------------------------");

            // 3. Gọi hàm từ xa: Client Stub tự động Marshalling dữ liệu qua mạng TCP đến Server
            int number = 5;
            long result = stub.factorial(number);
            System.out.println(">>> Giai thừa của " + number + " (" + number + "!) nhận từ Server = " + result);

            // Thử thêm với các số khác
            int n2 = 10;
            System.out.println(">>> Giai thừa của " + n2 + " (" + n2 + "!) nhận từ Server = " + stub.factorial(n2));

            int n3 = 12;
            System.out.println(">>> Giai thừa của " + n3 + " (" + n3 + "!) nhận từ Server = " + stub.factorial(n3));

            System.out.println("------------------------------------------------------------------");

        } catch (Exception e) {
            System.err.println("[-] Lỗi kết nối hoặc gọi RMI: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
```

---

## 🌐 Hướng Dẫn Chạy Thực Tế Trên 2 Máy Tính Khác Nhau Qua Mạng LAN

Giả sử bạn có 2 máy tính kết nối chung một mạng Wi-Fi / LAN:

* **Máy A (Server)** có địa chỉ IP: `192.168.1.10`
* **Máy B (Client)** có địa chỉ IP: `192.168.1.20`

### Bước 1: Chuẩn bị trên Máy A (Server)

1. Mở Terminal / PowerShell trên Máy A:
   ```powershell
   javac FactorialService.java FactorialServiceImpl.java FactorialServer.java
   ```
2. Khởi chạy Server:
   ```powershell
   java FactorialServer
   ```

*(Lưu ý: Đảm bảo Windows Defender Firewall trên máy A cho phép Java kết nối qua cổng 1099).*

---

### Bước 2: Chuẩn bị trên Máy B (Client)

1. Copy 2 file: `FactorialService.java` (Interface) và `FactorialClient.java` sang Máy B.
2. Mở Terminal / PowerShell trên Máy B:
   ```powershell
   javac FactorialService.java FactorialClient.java
   ```
3. Khởi chạy Client và truyền IP của Máy A:
   ```powershell
   java FactorialClient 192.168.1.10
   ```

---

### 📋 Kết Quả Màn Hình:

* **Màn hình Máy A (Server):**

  ```text
  [SERVER] Factorial RMI Server đang chạy và lắng nghe tại cổng 1099...
  [SERVER] Đã đăng ký dịch vụ: 'FactorialService'
  [Server] Nhận yêu cầu tính giai thừa của n = 5
  [Server] Nhận yêu cầu tính giai thừa của n = 10
  [Server] Nhận yêu cầu tính giai thừa của n = 12
  ```
* **Màn hình Máy B (Client):**
  ```text
  [CLIENT] Đang kết nối tới Server RMI tại 192.168.1.10:1099...
  [CLIENT] Kết nối thành công! Bắt đầu gọi hàm tính giai thừa từ xa:
  ------------------------------------------------------------------
  >>> Giai thừa của 5 (5!) nhận từ Server = 120
  >>> Giai thừa của 10 (10!) nhận từ Server = 3628800
  >>> Giai thừa của 12 (12!) nhận từ Server = 479001600
  ------------------------------------------------------------------
  ```

---

## 8. ❓ Trả Lời Chi Tiết Các Câu Hỏi Bài 3 Trong Slide

---

### **Câu 1: Đoạn code này thực chất là gọi cục bộ, chưa phải RPC thật sự. Nêu ra 2 điểm khác biệt chính giữa đoạn code này và RPC thực sự.**

1. **Không gian bộ nhớ & Tiến trình (Memory Space & Process):**
   * *Đoạn code trong slide:* Client tự tạo đối tượng `new RPCServer()` ngay trong hàm `main`, cả Client và Server chạy chung trong **cùng 1 tiến trình và 1 không gian RAM (JVM)** trên 1 máy tính.
   * *RPC thực sự:* Client và Server là **2 tiến trình hoàn toàn độc lập** chạy trên **2 máy tính vật lý khác nhau** kết nối qua mạng (Space-uncoupled).
2. **Cơ chế truyền thông & Dữ liệu (Network & Marshalling):**
   * *Đoạn code trong slide:* Gọi hàm trực tiếp qua con trỏ bộ nhớ RAM (`server.factorial(number)`), dữ liệu truyền qua ngăn xếp CPU.
   * *RPC thực sự:* Lời gọi hàm phải thông qua **Client Stub** đóng gói dữ liệu thành luồng byte (**Marshalling**) ➡️ gửi qua giao thức mạng **TCP/IP Socket** ➡️ **Server Skeleton** giải nén (**Unmarshalling**) và thực thi, rồi gửi kết quả ngược lại qua mạng.

---

### **Câu 2: Nếu muốn chạy RPC trên 2 máy khác nhau, ta cần bổ sung thành phần gì?**

Cần bổ sung **4 thành phần cơ bản**:
1. **Remote Interface (`FactorialService extends Remote`):** Hợp đồng giao tiếp chung giữa 2 máy, khai báo phương thức `long factorial(int n) throws RemoteException`.
2. **Client Stub & Server Skeleton (`UnicastRemoteObject.exportObject`):** Đóng gói và giải nén tham số ở 2 đầu kết nối.
3. **Dịch vụ định danh (RMI Registry):** Chạy tại máy Server (cổng 1099) để Client từ máy khác có thể tra cứu (`lookup`) dịch vụ từ xa.
4. **Cấu hình IP Mạng & Mở Tường Lửa:** Phía Client cần đổi địa chỉ `"localhost"` thành **IP thực tế của máy Server** (ví dụ: `192.168.1.10`), và Server cần mở cổng tường lửa (Firewall) cho phép kết nối mạng vào cổng 1099.

---

### **Câu 3: Nếu input `n` rất lớn (ví dụ `50.000`), cần chú ý đến vấn đề gì khi dùng RPC?**

Khi $n = 50.000$, việc tính giai thừa $50.000!$ qua RPC sẽ đối mặt với **4 vấn đề nghiêm trọng**:

1. **Tràn số kiểu dữ liệu (Integer / Long Overflow):**
   * Kiểu `long` trong Java chỉ chứa được tối đa đến $20! \approx 2.43 \times 10^{18}$. Với $n = 50.000$, kết quả sẽ có hơn $200.000$ chữ số và bị tràn số nghiêm trọng (trả về `0` hoặc số âm sai lệch).
   * 👉 *Cách xử lý:* Phải đổi kiểu dữ liệu trả về thành **`BigInteger`** (hoặc `String`).

2. **Tràn ngăn xếp đệ quy (StackOverflowError trên Server):**
   * Code đệ quy ban đầu `n * factorial(n - 1)` sẽ tạo ra **50.000 khung ngăn xếp (Stack Frames)** trên Server, gây lỗi **`java.lang.StackOverflowError`** làm sập tiến trình Server.
   * 👉 *Cách xử lý:* Đổi từ đệ quy sang **vòng lặp `for` (Iterative)** hoặc thuật toán tính toán chia để trị / song song.

3. **Hiện tượng Treo Client / Quá thời gian chờ (RPC Network Timeout):**
   * Tính toán $50.000!$ với số siêu lớn tốn rất nhiều chu kỳ CPU và thời gian.
   * Lời gọi RPC đồng bộ (**Synchronous Blocking Call**) sẽ khiến Client bị treo cứng (freeze) chờ phản hồi, dễ dẫn đến lỗi **`SocketTimeoutException`** hoặc đứt kết nối mạng do timeout.
   * 👉 *Cách xử lý:* Cần cấu hình **Timeout hợp lý**, hoặc chuyển sang cơ chế **gọi hàm bất đồng bộ (Asynchronous RPC / Future / Callback)** hoặc Message Queue.

4. **Kích thước gói tin lớn & Tốn băng thông truyền mạng (Payload & Serialization Overhead):**
   * Kết quả $50.000!$ dạng chuỗi có kích thước hàng trăm Kilobytes. Quá trình tuần tự hóa (**Serialization**) và truyền dữ liệu lớn qua mạng sẽ làm tăng độ trễ (latency) và tiêu tốn băng thông.

