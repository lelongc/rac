# T5 – Thread ghi File + Socket TCP (nhiều bài thực hành)

## Cấu trúc thư mục

```
t5/
├── FileThreadWriter.java   ← Thread ghi file
├── Main.java               ← Chạy 3 thread ghi 3 file
└── t5-2/
    ├── gui-nhan/           ← Socket TCP cơ bản (1 client, String)
    ├── gui-nhan-luong/     ← Socket TCP + Thread + InetAddress (byte/int)
    ├── nhieuServer-guitext/ ← Socket TCP multi-client (String, BufferedReader)
    └── cac-bai-co-ban/     ← 5 bài Socket thực hành
        ├── uppercase/      port 8888 – chuyển chữ hoa
        ├── lowercase/      port 8889 – chuyển chữ thường
        ├── countchar/      port 8890 – đếm ký tự
        ├── evenodd/        port 8891 – kiểm tra chẵn/lẻ
        └── sumnumbers/     port 8892 – tính tổng các số
```

---

## FileThreadWriter.java + Main.java – Thread Ghi File

| File | Vai trò |
|------|---------|
| `FileThreadWriter.java` | Thread ghi 10 số random vào file, nghỉ 100ms mỗi lần |
| `Main.java` | Tạo 3 thread → ghi file1.txt, file2.txt, file3.txt → `join()` chờ tất cả xong |

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\t5"
javac -encoding UTF-8 *.java
java Main
# Tạo ra file1.txt, file2.txt, file3.txt
```

---

## t5-2/gui-nhan/ – Socket TCP Cơ Bản (không có Thread)

| File | Vai trò | Chạy |
|------|---------|------|
| `TCPServer.java` | Server 1 client, dùng `BufferedReader` + `PrintWriter`, port **8888** | Chạy TRƯỚC |
| `TCPClient.java` | Client gửi `"Hello Server"`, nhận echo | Chạy SAU |

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\t5\t5-2\gui-nhan"
javac -encoding UTF-8 *.java
# Terminal 1:  java TCPServer
# Terminal 2:  java TCPClient
```

---

## t5-2/gui-nhan-luong/ – Socket TCP + Thread + InetAddress (byte/int)

| File | Vai trò | Chạy |
|------|---------|------|
| `tcpServer.java` | Server tạo thread cho mỗi client, port **5678** | Chạy TRƯỚC |
| `serverThread.java` | Thread xử lý: in **InetAddress** (IP/Port), đọc byte `is.read()`, echo lại | (server tự tạo) |
| `tcpClient.java` | Gửi ký tự `'0'` đến `'9'` (byte), nhận echo | Chạy SAU |

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\t5\t5-2\gui-nhan-luong"
javac -encoding UTF-8 *.java
# Terminal 1:  java tcpServer
# Terminal 2:  java tcpClient
```

---

## t5-2/nhieuServer-guitext/ – Socket Multi-Client (String, BufferedReader)

| File | Vai trò | Chạy |
|------|---------|------|
| `TCPServerMulti.java` | Server nhận nhiều client, tạo thread cho mỗi cái, port **8888** | Chạy TRƯỚC |
| `ClientHandlerMulti.java` | Thread xử lý: `readLine()` → echo lại, đến khi `null` thì đóng | (server tự tạo) |
| `TCPClientMulti.java` | Nhập tin nhắn từ bàn phím, gửi liên tục, gõ `exit` để thoát | Chạy SAU (mở nhiều terminal) |

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\t5\t5-2\nhieuServer-guitext"
javac -encoding UTF-8 *.java
# Terminal 1:           java TCPServerMulti
# Terminal 2, 3, 4...:  java TCPClientMulti   (chạy nhiều client cùng lúc)
```

---

## t5-2/cac-bai-co-ban/ – 5 Bài Socket Thực Hành

> Mỗi bài có **3 file**: `*Server.java` | `*Handler.java` | `*Client.java`
> Cách chạy giống nhau: `java XxxServer` (terminal 1) → `java XxxClient` (terminal 2)

| Thư mục | Server class | Port | Chức năng xử lý |
|---------|-------------|------|-----------------|
| `uppercase/` | `UpperCaseServer` | **8888** | `message.toUpperCase()` |
| `lowercase/` | `LowerCaseServer` | **8889** | `message.toLowerCase()` |
| `countchar/` | `CountCharServer` | **8890** | `message.length()` → đếm ký tự |
| `evenodd/` | `EvenOddServer` | **8891** | kiểm tra số chẵn/lẻ |
| `sumnumbers/` | `SumNumbersServer` | **8892** | tách chuỗi `split(" ")` → tính tổng |

```bash
# Ví dụ chạy uppercase:
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\t5\t5-2\cac-bai-co-ban\uppercase"
javac -encoding UTF-8 *.java
# Terminal 1: java UpperCaseServer
# Terminal 2: java UpperCaseClient
```

> **Lưu ý**: Các bài dùng **port khác nhau** (8888–8892), không bị xung đột nếu chạy cùng lúc

---

## So Sánh Các Kiểu Socket Trong t5

| | gui-nhan | gui-nhan-luong | nhieuServer-guitext |
|--|--|--|--|
| Stream | BufferedReader | InputStream (byte) | BufferedReader |
| Thread | ❌ Không | ✅ Có | ✅ Có |
| Multi-client | ❌ 1 client | ✅ Nhiều | ✅ Nhiều |
| InetAddress | ❌ | ✅ In IP/Port | ❌ |
| Dữ liệu | String | byte/int | String |
