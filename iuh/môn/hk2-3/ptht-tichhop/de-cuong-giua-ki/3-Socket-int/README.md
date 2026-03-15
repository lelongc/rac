# CHỦ ĐỀ 3: SOCKET TCP – KIỂU INT (InputStream / byte)

## Các file trong thư mục này

| File | Vai trò | Chạy |
|------|---------|------|
| `tcpServer.java` | **SERVER** – tạo `ServerSocket`, vòng lặp `accept()`, mỗi client → tạo 1 `serverThread` | Chạy **TRƯỚC** |
| `serverThread.java` | **THREAD XỬ LÝ** – nhận Socket, in InetAddress, đọc byte (`is.read()`), gửi byte (`os.write()`) | (server tự tạo) |
| `tcpClient.java` | **CLIENT** – kết nối tới server, gửi ký tự 'a'→'e', nhận byte kết quả | Chạy **SAU** |

---

## Cách chạy bằng terminal

> **Mở 2 cửa sổ terminal riêng**

**Terminal 1 – Chạy Server trước:**
```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\de-cuong-giua-ki\3-Socket-int"
javac -encoding UTF-8 *.java
java tcpServer
```
Kết quả mong đợi:
```
Server da tao (port: 5678)
Dang cho ket noi tu client...
```

**Terminal 2 – Chạy Client sau:**
```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\de-cuong-giua-ki\3-Socket-int"
java tcpClient
```
Kết quả mong đợi:
```
Da ket noi toi server!
Gui: a  |  Nhan lai: A
Gui: b  |  Nhan lai: B
...
```

---

## Luồng Stream (kiểu int/byte)

```
CLIENT                          SERVER (serverThread)
------                          --------------------
os.write(i)    ──────────────→  ch = is.read()          // đọc byte
               ←──────────────  os.write(toUpperCase)   // gửi byte
kq = is.read()
```

## Điểm quan trọng

- `is.read()` trả **`-1`** khi client ngắt → dùng làm điều kiện `break`
- Đọc/ghi từng **byte** (int), cast sang `(char)` để in ra chữ
- `serverThread` chạy riêng → server phục vụ được **nhiều client cùng lúc**
- InetAddress: `client.getInetAddress().getHostAddress()` → lấy IP
