# 🗂️ MODULES – PTHT TÍCH HỢP – HƯỚNG DẪN SỬ DỤNG KHI THI

## 📁 Vị trí: `ptht-tichhop/modules/`

---

## BẢNG MODULE → CHỌN THEO ĐỀ

| Module | File | Dùng khi đề có... |
|--------|------|-------------------|
| **M1** | `M1_OOP.java` | Lớp cha/con, kế thừa, tính lương/thuế/... |
| **M2** | `M2_Thread.java` | Thread cơ bản, song song, ghi file |
| **M3** | `M3_Thread_Sync.java` | Producer-Consumer, Kho, wait/notify |
| **M4** | `M4_Stream_IO.java` | Nhập liệu console, InputStream/BufferedReader |
| **M5** | `M5_TCP_DataStream.java` | TCP + int/long/String (DataInputStream) |
| **M6** | `M6_TCP_TextStream.java` | TCP + văn bản dòng (BufferedReader/PrintWriter) |
| **M7** | `M7_UDP.java` | UDP, DatagramSocket |
| **M8** | `M8_InetAddress.java` | Hiển thị IP, hostname, thông tin client |
| **M9** | `M9_Ghep_OOP_TCP_Thread.java` | Ghép OOP + TCP + Thread cùng lúc |

---

## 🔧 QUY TRÌNH KHI ĐỀ RA

### Bước 1 – Đọc đề, xác định module cần
```
Có "kế thừa / lớp cha con"    → M1
Có "Thread / song song"        → M2 hoặc M3
Có "TCP Server/Client"         → M5 hoặc M6
Có "UDP"                       → M7
Có "InetAddress / IP"          → M8
Có nhiều thứ cùng lúc          → M9 làm khung, ghép các M khác vào
```

### Bước 2 – Chọn stream (khi có TCP)
```
Đề truyền số (int/long)      → DataInputStream/DataOutputStream   (M5)
Đề truyền chuỗi/chat/text    → BufferedReader/PrintWriter          (M6)
Đề truyền byte thô (ký tự)   → InputStream/OutputStream            (M5 cách B)
```

### Bước 3 – Sửa TODO
Tìm comment `// TODO:` trong file chọn, sửa theo đề:
- Tên class, field, port
- Hàm `xuLy()` trong Handler
- Hàm `tinhToan()` trong OOP

---

## ✂️ SNIPPET HAY DÙNG

### Nhập liệu (console/client)
```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
String s   = br.readLine();
int    n   = Integer.parseInt(br.readLine().trim());
double d   = Double.parseDouble(br.readLine().trim());
```

### Mở stream trong TCP Handler
```java
// DataStream (int/String nhị phân):
DataInputStream  in  = new DataInputStream(socket.getInputStream());
DataOutputStream out = new DataOutputStream(socket.getOutputStream());
String msg = in.readUTF();     out.writeUTF("ket qua"); out.flush();
int    n   = in.readInt();     out.writeInt(n * 2);     out.flush();
long   v   = in.readLong();    out.writeLong(v);         out.flush();

// Text dòng:
BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
PrintWriter   writer = new PrintWriter(socket.getOutputStream(), true);
String msg = reader.readLine();    writer.println("ket qua");
```

### Server vòng lặp nhận nhiều client
```java
ServerSocket ss = new ServerSocket(PORT);
while (true) {
    Socket client = ss.accept();
    new ClientHandler(client).start();   // M2: extends Thread
}
```

### synchronized + wait/notify (M3 skeleton)
```java
public synchronized void produce(int x) throws InterruptedException {
    while (current + x > max) wait();
    current += x;  notifyAll();
}
public synchronized void consume(int x) throws InterruptedException {
    while (current < x) wait();
    current -= x;  notifyAll();
}
```

### Lấy IP client trong Handler
```java
socket.getInetAddress().getHostAddress()  // IP
socket.getPort()                          // port client
```

---

## 📌 THỨ TỰ CHẠY TRONG ECLIPSE
1. **Server** → Run As > Java Application → chờ "Server lang nghe..."
2. **Client** → Run As > Java Application (mở tab Console riêng)
3. Nếu `Connection refused` → Server chưa chạy hoặc sai port

## ⚡ LỖI NHANH
| Lỗi | Fix |
|-----|-----|
| `Connection refused` | Chạy Server trước |
| `Address already in use` | Đổi port hoặc Stop process cũ |
| Treo không phản hồi | Thiếu `out.flush()` sau writeUTF/writeInt |
| `NumberFormatException` | Bọc `try/catch`, kiểm tra `trim()` |
