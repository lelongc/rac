# ĐỀ CƯƠNG ÔN THI GIỮA KÌ
## Môn: Phát Triển Hệ Thống Tích Hợp

---

## CHỦ ĐỀ 1: OOP (Lập Trình Hướng Đối Tượng)

### Kiến thức cần nhớ
- **Class & Object**: khai báo lớp, tạo đối tượng
- **Kế thừa** (`extends`): lớp con dùng lại code lớp cha, gọi `super.method()`
- **Đa hình** (`@Override`): lớp con ghi đè method cha
- **Abstract class**: không thể tạo trực tiếp, bắt buộc lớp con implement
- **Constructor**: phương thức khởi tạo, cùng tên class

### Cấu trúc hay gặp
```
LopCha (abstract)
  ├── LopCon1 (extends LopCha)
  └── LopCon2 (extends LopCha)
```

### Code mẫu: `1-OOP/`
- `NhanVien.java` – lớp cha trừu tượng
- `NhanVienVanPhong.java` – lớp con (kế thừa)
- `NhanVienSanXuat.java` – lớp con (kế thừa)
- `Main.java` – chạy chương trình

---

## CHỦ ĐỀ 2: THREAD (Luồng)

### Kiến thức cần nhớ
- **Cách 1: extends Thread** → override `run()`, gọi `start()`
- **Cách 2: implements Runnable** → override `run()`, truyền vào `new Thread(obj).start()`
- `Thread.sleep(ms)` – tạm dừng luồng
- `thread.join()` – chờ luồng kết thúc trước khi tiếp tục
- Nhiều thread chạy **song song**, thứ tự KHÔNG đảm bảo

### Vòng đời Thread
```
new → start() → run() → [sleep()] → kết thúc
```

### Code mẫu: `2-Thread/`
- `C1_ExtendsThread.java` – cách 1: kế thừa Thread
- `C2_ImplementsRunnable.java` – cách 2: implements Runnable
- `C3_ThreadSleepJoin.java` – dùng sleep() và join()

---

## CHỦ ĐỀ 3: SOCKET TCP + THREAD + InetAddress

### 3 bước chính
```
KẾT NỐI  →  XỬ LÝ (Stream)  →  ĐÓNG KẾT NỐI
```

### InetAddress (thông tin địa chỉ)
```java
client.getInetAddress().getHostAddress()  // IP
client.getPort()                          // port phía client
client.getLocalPort()                     // port phía server
```

### Stream theo kiểu dữ liệu
| Kiểu       | Class                   | Đọc             | Ghi           |
|-----------|-------------------------|-----------------|---------------|
| `int` (byte) | `InputStream / OutputStream` | `is.read()` | `os.write(ch)` |
| `String`  | `BufferedReader / PrintWriter` | `br.readLine()` | `pw.println()` |

### Chuỗi Stream (String)
```
InputStream (byte)
    → InputStreamReader (byte → char)
        → BufferedReader (buffer + đọc theo dòng)
```

### Cấu trúc 3 file
```
tcpServer.java       – tạo ServerSocket, accept(), tạo Thread cho mỗi client
serverThread.java    – Thread xử lý 1 client (đọc/ghi stream, đóng socket)
tcpClient.java       – kết nối tới server, gửi/nhận dữ liệu
```

### Code mẫu kiểu `int` (byte): `3-Socket-int/`
- `tcpServer.java`
- `serverThread.java`
- `tcpClient.java`

### Code mẫu kiểu `String` (BufferedReader): `4-Socket-String/`
- `TCPServer.java`
- `ClientHandler.java`
- `TCPClient.java`

---

## TÓM TẮT LUỒNG HOẠT ĐỘNG SOCKET TCP

```
SERVER                          CLIENT
------                          ------
ServerSocket(port)              
accept() ──────────────────── new Socket("host", port)
new Thread(client).start()     
                                getOutputStream() → gửi
getInputStream() ← nhận        
getOutputStream() → phản hồi   
                                getInputStream() ← nhận
socket.close()                  socket.close()
```

---

## LƯU Ý QUAN TRỌNG

1. **Server** phải chạy trước **Client**
2. Mỗi `Socket` cần được `close()` sau khi dùng xong
3. `BufferedReader.readLine()` trả về `null` khi client ngắt kết nối
4. `InputStream.read()` trả về `-1` khi client ngắt kết nối
5. `PrintWriter(os, true)` → `true` = auto flush (tự gửi ngay)
6. Thread xử lý (`serverThread`) giúp server phục vụ **nhiều client cùng lúc**
