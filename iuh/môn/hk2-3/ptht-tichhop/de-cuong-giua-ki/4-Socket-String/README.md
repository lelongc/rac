# CHỦ ĐỀ 4: SOCKET TCP – KIỂU STRING (BufferedReader / PrintWriter)

## Các file trong thư mục này

| File | Vai trò | Chạy |
|------|---------|------|
| `TCPServer.java` | **SERVER** – tạo `ServerSocket`, vòng lặp `accept()`, mỗi client → tạo 1 `ClientHandler` | Chạy **TRƯỚC** |
| `ClientHandler.java` | **THREAD XỬ LÝ** – nhận Socket, đọc String (`readLine()`), gửi String (`println()`) | (server tự tạo) |
| `TCPClient.java` | **CLIENT** – kết nối, đọc từ bàn phím, gửi chuỗi, nhận phản hồi, gõ `exit` để thoát | Chạy **SAU** |

---

## Cách chạy bằng terminal

> **Mở 2 cửa sổ terminal riêng**

**Terminal 1 – Chạy Server trước:**
```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\de-cuong-giua-ki\4-Socket-String"
javac -encoding UTF-8 *.java
java TCPServer
```
Kết quả mong đợi:
```
Server da tao (port: 8888)
Dang cho ket noi tu client...
```

**Terminal 2 – Chạy Client sau:**
```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\de-cuong-giua-ki\4-Socket-String"
java TCPClient
```
Kết quả mong đợi:
```
Da ket noi toi server!
Nhap tin nhan (exit de thoat): hello
Nhan tu server: Server phan hoi: HELLO
```

> Mở thêm Terminal 3, 4... chạy thêm `java TCPClient` để test nhiều client cùng lúc

---

## Chuỗi Stream (String) – Quan trọng cần nhớ

```
InputStream (byte)
    └─→ InputStreamReader (byte → char)
            └─→ BufferedReader (buffer + đọc theo dòng)
                    └─→ readLine()  // đọc 1 dòng String
```

**Code:**
```java
BufferedReader reader = new BufferedReader(
        new InputStreamReader(socket.getInputStream()));

PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
//                                                              ^^^^
//                                               true = auto flush (gửi ngay)
```

---

## So sánh với kiểu int (folder 3-Socket-int)

| | Kiểu int (byte) | Kiểu String |
|--|--|--|
| Stream đọc | `InputStream` | `BufferedReader` |
| Stream ghi | `OutputStream` | `PrintWriter` |
| Đọc | `is.read()` → int | `br.readLine()` → String |
| Ghi | `os.write(ch)` | `pw.println(str)` |
| Kết thúc | trả `-1` | trả `null` |
| Dùng khi | gửi byte đơn lẻ | gửi chuỗi/dòng văn bản |

---

## Điểm quan trọng

- `readLine()` trả **`null`** khi client ngắt → dùng làm điều kiện vòng lặp
- `PrintWriter(os, true)` → `true` = **auto flush** (không cần gọi `flush()` thủ công)
- Luôn `close()` stream trước khi `close()` socket
