# 📌 NOTE GIỮA KỲ – PTHT TÍCH HỢP

> **Cách dùng:** Xem đề → Xác định chủ đề → Vào thư mục tương ứng → Copy code khung sườn → Chỉnh theo đề.

---

## MỤC LỤC NHANH

| Chủ đề | Thư mục | File chính |
|--------|---------|------------|
| OOP – Kế thừa (extends) | `t2/tuan2` | `NhanVien`, `NhanVienSanXuat`, `NhanVienVanPhong` |
| OOP – Kế thừa + Constructor | `t2/tuan2b` | `PhuongTien`, `Oto`, `XeMay` |
| Stream: InputStream byte | `t3/eg` | `ex1.java`, `ex2.java` |
| Stream: InputStreamReader + BufferedReader | `t3/eg` | `ex3.java` |
| Stream: OutputStream + PrintWriter | `t3/eg` | `ex4.java` |
| I/O cơ bản (int, String, switch/if) | `t3/tuan1` | `ex1~ex5.java` |
| Thread cơ bản (extends Thread) | `t4/tuan4/src/bai1` | `MyThread.java`, `ThreadSimple.java` |
| Thread ghi file (extends / Runnable) | `t4/tuan4/src/bai2` | `FileTWrite.java` |
| Thread đọc file (extends / Runnable) | `t4/tuan4/src/bai3` | `FileTReader.java` |
| Thread đồng bộ (synchronized/wait/notify) | `t4/tuan4/src/bai4` | `FileBuffer`, `FileWriterThread`, `FileReaderThread` |
| Thread Producer-Consumer | `t4/tuan4/src/bai5` | `Kho`, `NguoiSanXuat`, `NguoiTieuDung` |
| Thread + File Writer đơn giản | `t5/` | `FileThreadWriter.java`, `Main.java` |
| TCP Socket đơn giản (1 client) | `t5/t5-2/gui-nhan` | `TCPServer`, `TCPClient` |
| TCP Socket + Thread (nhiều client) | `t5/t5-2/gui-nhan-luong` | `tcpServer`, `serverThread`, `tcpClient` |
| TCP Multi-client (Echo text) | `t5/t5-2/nhieuServer-guitext` | `TCPServerMulti`, `ClientHandlerMulti`, `TCPClientMulti` |
| TCP: String – UpperCase / LowerCase | `t5/t5-2/cac-bai-co-ban/uppercase` `lowercase` | Server, Handler, Client |
| TCP: int – Chẵn/Lẻ | `t5/t5-2/cac-bai-co-ban/evenodd` | EvenOddServer, Handler, Client |
| TCP: int – Tổng các số | `t5/t5-2/cac-bai-co-ban/sumnumbers` | SumNumbersServer, Handler, Client |
| TCP: String – Đếm ký tự | `t5/t5-2/cac-bai-co-ban/countchar` | CountCharServer, Handler, Client |
| TCP GK – int: đọc số (0-9 → tiếng Việt) | `t5/tcp-tuan5-gk/b1` | `Server`, `ClientHandler`, `Client` |
| TCP GK – Chat Echo | `t5/tcp-tuan5-gk/b2` | `ChatServer`, `ClientHandler`, `ChatClient` |
| TCP GK – Chat Echo qua IP/Port args | `t5/tcp-tuan5-gk/b3` | `ChatServer`, `ClientHandler`, `ChatClient` |
| TCP GK – int menu: Time/Date/DateTime | `t5/tcp-tuan5-gk/b4` | `DateTimeServer`, `ClientHandler`, `DateTimeClient` |
| UDP GK – String menu: Time/Date/DateTime | `t5/tcp-tuan5-gk/b5` | `DateTimeUDPServer`, `DateTimeService`, `DateTimeUDPClient` |
| TCP+UDP GK – Tính toán dãy số | `t5/tcp-tuan5-gk/b6` | `TcpCalcServer`, `TcpClientHandler`, `CalcService`, `UdpCalcServer` |

---

## 1. OOP – KẾ THỪA

### Khung sườn
```
t2/tuan2/      → NhanVien (cha)  →  NhanVienSanXuat / NhanVienVanPhong (con)
t2/tuan2b/     → PhuongTien (cha) → Oto / XeMay (con + constructor super())
t3/tuan2/      → clone của tuan2 (NhanVien)
t3/tuan2b/     → clone của tuan2b (PhuongTien)
```

### Pattern nhớ
```java
// Lớp cha
class TenCha {
    String field1; int field2;
    public void nhapThongTin() { ... }      // Scanner hoặc BufferedReader
    public void hienThiThongTin() { ... }
}

// Lớp con
class TenCon extends TenCha {
    int fieldRieng;
    @Override public void nhapThongTin() { super.nhapThongTin(); ... }
    public double tinhToan() { return ...; }   // phuong thuc rieng
}
```

**File ví dụ:**
- `t2/tuan2/NhanVien.java` → có `nhapThongTin()`, `hienThiThongTin()`
- `t2/tuan2/NhanVienSanXuat.java` → `extends NhanVien`, gọi `super.nhapThongTin()`, thêm `tinhLuong()`
- `t2/tuan2b/PhuongTien.java` → constructor có tham số
- `t2/tuan2b/Oto.java` → `super(hang, nam, gia)`, thêm `tinhThue()`

---

## 2. THREAD

### 2.1 Thread đơn giản

```
t4/tuan4/src/bai1/ThreadSimple.java   → extends Thread, override run(), gọi t.start()
t4/tuan4/src/bai1/MyThread.java       → Thread tự gọi start() trong constructor
```

**Pattern extends Thread:**
```java
class TenThread extends Thread {
    @Override
    public void run() { /* xử lý */ }
}
// Dùng: new TenThread().start();
```

**Pattern implements Runnable:**
```java
class TenRunnable implements Runnable {
    @Override
    public void run() { /* xử lý */ }
}
// Dùng: new Thread(new TenRunnable()).start();
```

### 2.2 Thread ghi/đọc file song song

```
t4/tuan4/src/bai2/FileTWrite.java     → implements Runnable, ghi file random
t4/tuan4/src/bai2/Main.java           → khởi 3 thread ghi 3 file khác nhau
t4/tuan4/src/bai3/FileTReader.java    → implements Runnable, đọc file với BufferedReader
t5/FileThreadWriter.java              → extends Thread, ghi file random (dùng join())
t5/Main.java                          → khởi 3 FileThreadWriter, join() chờ tất cả xong
```

### 2.3 Thread đồng bộ (synchronized + wait/notify)

```
t4/tuan4/src/bai4/FileBuffer.java         → synchronized writeLine() / readNewLine()
t4/tuan4/src/bai4/FileWriterThread.java   → gọi buffer.writeLine()
t4/tuan4/src/bai4/FileReaderThread.java   → gọi buffer.readNewLine()
```

**Pattern synchronized:**
```java
class SharedBuffer {
    private boolean hasData = false;
    public synchronized void produce(String data) throws InterruptedException {
        while (hasData) wait();          // chờ consumer lấy xong
        // ... ghi data ...
        hasData = true;
        notifyAll();
    }
    public synchronized String consume() throws InterruptedException {
        while (!hasData) wait();         // chờ producer ghi xong
        // ... đọc data ...
        hasData = false;
        notifyAll();
        return data;
    }
}
```

### 2.4 Producer – Consumer (Kho)

```
t4/tuan4/src/bai5/Kho.java              → nhapKho() / xuatKho() synchronized
t4/tuan4/src/bai5/NguoiSanXuat.java     → extends Thread, gọi kho.nhapKho()
t4/tuan4/src/bai5/NguoiTieuDung.java    → extends Thread, gọi kho.xuatKho()
t4/tuan4/src/bai5/Demo.java             → khởi 2 NSX + 2 NTD
```

---

## 3. STREAM – ĐỌC GHI

### 3.1 Chuỗi kế thừa stream (CỐT LÕI)

```
InputStream (byte thô)
    └── InputStreamReader (byte → char, biết encoding)
            └── BufferedReader (đọc cả dòng: readLine())
```

**File ví dụ:**
```
t3/eg/ex1.java  → InputStream.read() → trả int (mã ASCII), cast (char)
t3/eg/ex2.java  → InputStream.available() + is.read(byte[]) + new String(bytes)
t3/eg/ex3.java  → InputStreamReader + BufferedReader, đọc vòng lặp readLine()
t3/eg/ex4.java  → OutputStream + PrintWriter: write(), println(), flush(), close()
```

### 3.2 Pattern nhập liệu chuẩn (dùng trong client/server)

```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
PrintWriter pw = new PrintWriter(System.out, true);   // true = auto-flush

String line = br.readLine();
int n = Integer.parseInt(br.readLine());
```
→ Xem: `t3/tuan1/ex1.java` đến `ex5.java` (đầy đủ: nhập String, int, switch, if/else)

---

## 4. TCP SOCKET – KHUNG SƯỜN 3 FILE

### Cấu trúc luôn dùng:

```
Server.java         → ServerSocket(port) → accept() → new ClientHandler(socket).start()
ClientHandler.java  → extends Thread, override run(), xử lý DataInputStream/DataOutputStream
Client.java         → new Socket(host, port) → gửi/nhận
```

### 4.1 Kết nối

```java
// SERVER
ServerSocket serverSocket = new ServerSocket(PORT);
Socket socket = serverSocket.accept();              // chặn chờ

// CLIENT  
Socket socket = new Socket("127.0.0.1", PORT);     // kết nối tới server
```

### 4.2 Xử lý Stream – Theo KIỂU DỮ LIỆU

#### Dùng DataInputStream / DataOutputStream (int, String thuần – b1~b6)

```java
DataInputStream  in  = new DataInputStream(socket.getInputStream());
DataOutputStream out = new DataOutputStream(socket.getOutputStream());

// Gửi/nhận String
out.writeUTF("nội dung");   String s = in.readUTF();
// Gửi/nhận int
out.writeInt(42);            int n = in.readInt();
// Gửi/nhận long
out.writeLong(123L);         long v = in.readLong();
out.flush();
```

**→ Dùng khi:** đề bài truyền **số nguyên** (menu choice, kết quả tính toán) hoặc **String đơn giản** (t5/tcp-tuan5-gk/b1 → b6)

#### Dùng BufferedReader / PrintWriter (text theo dòng – t5-2)

```java
// SERVER (trong ClientHandler)
BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);

String msg = reader.readLine();     // đọc 1 dòng
writer.println("Echo: " + msg);    // ghi 1 dòng + newline
```

**→ Dùng khi:** đề bài truyền **chuỗi văn bản** (uppercase, lowercase, đếm ký tự, tổng số)

```
t5/t5-2/gui-nhan/            → BufferedReader/PrintWriter, 1 client
t5/t5-2/nhieuServer-guitext/ → BufferedReader/PrintWriter, nhiều client (thread)
t5/t5-2/cac-bai-co-ban/      → uppercase/lowercase/evenodd/sumnumbers/countchar
```

### 4.3 Đóng kết nối

```java
// Trong try-with-resources (tự đóng):
try (Socket s = socket;
     DataInputStream in = new DataInputStream(s.getInputStream());
     DataOutputStream out = new DataOutputStream(s.getOutputStream())) {
    // ...
}

// Hoặc đóng thủ công:
reader.close(); writer.close(); socket.close(); serverSocket.close();
```

### 4.4 Thread xử lý (ClientHandler pattern)

```java
// t5/tcp-tuan5-gk/b1/ClientHandler.java  → xử lý int/String, DataStream
// t5/t5-2/nhieuServer-guitext/ClientHandlerMulti.java → xử lý text, BufferedReader
// t5/t5-2/gui-nhan-luong/serverThread.java → xử lý byte thô (InputStream/OutputStream)
public class ClientHandler extends Thread {
    private final Socket socket;
    public ClientHandler(Socket socket) { this.socket = socket; }
    @Override
    public void run() {
        try (Socket s = socket; /* mở stream */) {
            while (true) {
                String msg = in.readUTF();
                if ("exit".equalsIgnoreCase(msg)) break;
                out.writeUTF(xuLy(msg));
                out.flush();
            }
        } catch (IOException e) { /* bỏ qua hoặc log */ }
    }
}
```

---

## 5. BẢNG TRA THEO KIỂU DỮ LIỆU TRUYỀN

| Kiểu | Gửi (Client) | Nhận (Server Handler) | Ví dụ file |
|------|-----------|--------------------|------------|
| `int` | `out.writeInt(n)` | `in.readInt()` | b4 (menu 1/2/3), b6 (choice+n) |
| `String` (DataStream) | `out.writeUTF(s)` | `in.readUTF()` | b1, b2, b3 |
| `long` | `out.writeLong(v)` | `in.readLong()` | b6 (kết quả) |
| `String` (text/dòng) | `writer.println(s)` | `reader.readLine()` | t5-2 tất cả |
| `byte` thô | `os.write(b)` | `is.read()` | gui-nhan-luong |
| `byte[]` (UDP) | `ByteBuffer.allocate(8).putInt().putInt()` | `ByteBuffer.wrap().getInt()` | b6 UDP |

---

## 6. InetAddress (TCP + InetAddress)

```java
// Lấy IP client trong ServerHandler:
socket.getInetAddress().getHostAddress()   // → "192.168.x.x"
socket.getPort()                           // → port của client
socket.getLocalPort()                      // → port server đang dùng

// Resolve tên miền / IP:
InetAddress addr = InetAddress.getByName("localhost");
InetAddress addr = InetAddress.getByName("192.168.1.10");
```
→ Xem: `t5/t5-2/gui-nhan-luong/serverThread.java` (in IP, Port, thời gian kết nối)

---

## 7. CHỌN FILE THEO LOẠI ĐỀ BÀI

### Đề: "Viết server-client TCP, client gửi số nguyên, server xử lý và trả về"
→ `t5/tcp-tuan5-gk/b1` (int → tên tiếng Việt)  
→ `t5/t5-2/cac-bai-co-ban/evenodd` (int → chẵn/lẻ)  
→ `t5/tcp-tuan5-gk/b6` (int choice + int n → long result)  
→ Stream dùng: **DataInputStream/DataOutputStream** (`writeInt`, `readInt`, `writeUTF`)

### Đề: "Viết server-client TCP, client gửi chuỗi, server xử lý và trả về"
→ `t5/t5-2/cac-bai-co-ban/uppercase` (toUpperCase)  
→ `t5/t5-2/cac-bai-co-ban/lowercase` (toLowerCase)  
→ `t5/t5-2/cac-bai-co-ban/countchar` (đếm ký tự)  
→ `t5/t5-2/cac-bai-co-ban/sumnumbers` (tách số, tính tổng)  
→ Stream dùng: **BufferedReader / PrintWriter** (`readLine`, `println`)

### Đề: "Server phục vụ nhiều client cùng lúc"
→ Server luôn có vòng `while(true) { socket=accept(); new ClientHandler(socket).start(); }`  
→ `t5/tcp-tuan5-gk/b1/Server.java` hoặc `t5/t5-2/nhieuServer-guitext/TCPServerMulti.java`

### Đề: "Chat 2 chiều (client gửi, server trả về, lặp đến exit/quit)"
→ `t5/tcp-tuan5-gk/b2` hoặc `b3` (b3 thêm IP/port qua args)

### Đề: "Server trả về thời gian (Time/Date/DateTime) theo lựa chọn"
→ TCP: `t5/tcp-tuan5-gk/b4` (DataInputStream, `readInt`, LocalTime/LocalDate/LocalDateTime)  
→ UDP: `t5/tcp-tuan5-gk/b5` (DatagramSocket, DateTimeService, String lựa chọn "1"/"2"/"3")

### Đề: "Thread ghi/đọc file, không liên quan mạng"
→ `t4/tuan4/src/bai2` + `bai3` (ghi/đọc file song song)  
→ `t5/FileThreadWriter.java` + `t5/Main.java` (ghi file + join())

### Đề: "OOP kế thừa, tính lương / tính thuế / ..."
→ `t2/tuan2` (NhanVien → NhanVienSanXuat, NhanVienVanPhong)  
→ `t2/tuan2b` (PhuongTien → Oto, XeMay)

---

## 8. IMPORT HAY DÙNG

```java
// TCP Socket
import java.net.ServerSocket;
import java.net.Socket;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;

// Text stream
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;

// Nhập liệu console
import java.util.Scanner;

// UDP
import java.net.DatagramSocket;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.nio.ByteBuffer;

// Thời gian
import java.time.LocalTime;
import java.time.LocalDate;
import java.time.LocalDateTime;
```

---

## 9. LỖI HAY GẶP

| Lỗi | Nguyên nhân | Sửa |
|-----|-------------|-----|
| `Connection refused` | Server chưa chạy | Chạy Server trước, Client sau |
| `Address already in use` | Port đang bị chiếm | Đổi port hoặc tắt process cũ |
| `readUTF()` treo | Client không `flush()` | Thêm `out.flush()` sau mỗi lần ghi |
| Thread không dừng | Vòng while(true) thiếu break | Thêm điều kiện exit/quit |
| `NumberFormatException` | Parse sai định dạng | Bọc `try/catch NumberFormatException` |
