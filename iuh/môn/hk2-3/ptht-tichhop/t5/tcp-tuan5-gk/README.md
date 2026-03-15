# TCP-TUAN5-GK – Bài Tập TCP/UDP Nâng Cao (Giữa Kì)

## Cấu trúc thư mục

```
tcp-tuan5-gk/
├── b1/   ← TCP: đọc số viết chữ (DataInputStream/DataOutputStream)
├── b2/   ← TCP Chat: server echo, client có thread nhận riêng
├── b3/   ← TCP Chat: giống b2, server nhận port từ args[]
├── b4/   ← TCP: hỏi Time/Date/DateTime (gửi int, nhận String)
├── b5/   ← UDP: hỏi Time/Date/DateTime (DatagramSocket/Packet)
└── b6/   ← TCP + UDP: tính toán chuỗi số (gửi int, nhận long)
```

> **Tất cả bài TCP port 5000**, b5 UDP port 5000, b6 UDP port 6000

---

## Stream kiểu DataInputStream / DataOutputStream (dùng trong b1-b6)

> **Khác với BufferedReader** – đây là stream nhị phân, gửi/nhận kiểu nguyên thủy trực tiếp

```
DataOutputStream.writeUTF(String)    ↔  DataInputStream.readUTF()   → String
DataOutputStream.writeInt(int)       ↔  DataInputStream.readInt()   → int
DataOutputStream.writeLong(long)     ↔  DataInputStream.readLong()  → long
```

---

## b1/ – Đọc Số Viết Chữ (TCP)

| File | Vai trò |
|------|---------|
| `Server.java` | Server multi-client, port **5000** |
| `ClientHandler.java` | Thread: nhận ký tự `'0'-'9'` → trả về chữ tiếng Việt (writeUTF/readUTF) |
| `Client.java` | Nhập 1 ký tự → gửi → in kết quả. Gõ `exit` để thoát |

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\t5\tcp-tuan5-gk\b1"
javac -encoding UTF-8 *.java
# Terminal 1:  java b1.Server
# Terminal 2:  java b1.Client
```

Ví dụ:
```
Nhap: 5  →  Server tra ve: năm
Nhap: 9  →  Server tra ve: chín
```

---

## b2/ – TCP Chat (Client có thread nhận song song)

| File | Vai trò |
|------|---------|
| `ChatServer.java` | Server multi-client, port **5000** |
| `ClientHandler.java` | Thread: chào client → echo lại tin nhắn. Gõ `/quit` để thoát |
| `ChatClient.java` | **Tạo thêm 1 thread riêng để nhận tin** (in cùng lúc với nhập), gõ `/quit` thoát |

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\t5\tcp-tuan5-gk\b2"
javac -encoding UTF-8 *.java
# Terminal 1:        java b2.ChatServer
# Terminal 2, 3...:  java b2.ChatClient
```

> **Điểm đặc biệt b2**: Client có **2 thread** – 1 thread gửi (main), 1 thread nhận (lambda thread):
> ```java
> new Thread(() -> { while(true) { System.out.println(in.readUTF()); } }).start();
> ```

---

## b3/ – TCP Chat Nâng Cao (nhận port từ dòng lệnh)

> Giống b2 hoàn toàn, **chỉ khác**: Server có thể nhận port qua `args[0]`

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\t5\tcp-tuan5-gk\b3"
javac -encoding UTF-8 *.java
# Terminal 1 (dùng port mặc định):  java b3.ChatServer
# Terminal 1 (chỉ định port):       java b3.ChatServer 6789
# Terminal 2:                        java b3.ChatClient
```

---

## b4/ – Hỏi Ngày Giờ qua TCP

| File | Vai trò |
|------|---------|
| `DateTimeServer.java` | Server multi-client, port **5000** |
| `ClientHandler.java` | Thread: gửi menu → nhận **int** (`readInt()`) → trả String ngày/giờ |
| `DateTimeClient.java` | Nhập IP + port → nhận menu → nhập 1/2/3 → in kết quả. `0` để thoát |

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\t5\tcp-tuan5-gk\b4"
javac -encoding UTF-8 *.java
# Terminal 1: java b4.DateTimeServer
# Terminal 2: java b4.DateTimeClient
#   → Nhap IP server: 127.0.0.1
#   → Nhap port: 5000
#   → Chon: 1  →  Time: 08:02:18
#   → Chon: 2  →  Date: 2026-03-15
#   → Chon: 0  →  Bye!
```

| Choice | Kết quả |
|--------|---------|
| 1 | `LocalTime.now()` |
| 2 | `LocalDate.now()` |
| 3 | `LocalDateTime.now()` |
| 0 | Thoát |

---

## b5/ – Hỏi Ngày Giờ qua UDP

| File | Vai trò |
|------|---------|
| `DateTimeService.java` | Helper – xử lý chuỗi `"1"/"2"/"3"` → trả String ngày/giờ |
| `DateTimeUDPServer.java` | UDP Server port **5000**: nhận packet text → gọi Service → gửi lại |
| `DateTimeUDPClient.java` | UDP Client: nhập IP/port → gửi `DatagramPacket` → nhận phản hồi |

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\t5\tcp-tuan5-gk\b5"
javac -encoding UTF-8 *.java
# Terminal 1: java b5.DateTimeUDPServer
# Terminal 2: java b5.DateTimeUDPClient
```

> **UDP khác TCP**:
> - Không cần `accept()` / `connect()` – gửi/nhận từng `DatagramPacket`
> - Dùng `DatagramSocket` thay vì `Socket`
> - `socket.receive(packet)` → `socket.send(packet)`

---

## b6/ – Tính Toán Chuỗi Số (TCP + UDP song song)

| File | Vai trò |
|------|---------|
| `CalcService.java` | Logic tính: 3 công thức (gửi int choice + int n, nhận long) |
| `TcpCalcServer.java` | TCP Server multi-client, port **5000** |
| `TcpClientHandler.java` | Thread TCP: nhận `readInt()` (choice) + `readInt()` (n) → `writeLong()` kết quả |
| `TcpCalcClient.java` | Client TCP: chọn công thức → nhập n → in kết quả |
| `UdpCalcServer.java` | UDP Server, port **6000**: nhận 8 byte (int choice + int n) → gửi 8 byte (long) |
| `UdpCalcClient.java` | Client UDP (nếu có) |

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\t5\tcp-tuan5-gk\b6"
javac -encoding UTF-8 *.java

# Chạy TCP:
# Terminal 1: java b6.TcpCalcServer
# Terminal 2: java b6.TcpCalcClient

# Chạy UDP (cổng khác, có thể cùng lúc với TCP):
# Terminal 3: java b6.UdpCalcServer
```

| Choice | Công thức | Ví dụ n=3 |
|--------|-----------|-----------|
| 1 | 1+3+5+...+(2n+1) = (n+1)² | = 16 |
| 2 | 1×2 + 2×3 + ... + n×(n+1) | = 20 |
| 3 | 1-2+3-4+...+(2n+1) = n+1 | = 4 |
| 0 | Thoát | – |

---

## Tóm Tắt Nhanh Cách Chạy

| Bài | Server | Client | Port |
|-----|--------|--------|------|
| b1 | `java b1.Server` | `java b1.Client` | TCP 5000 |
| b2 | `java b2.ChatServer` | `java b2.ChatClient` | TCP 5000 |
| b3 | `java b3.ChatServer` | `java b3.ChatClient` | TCP 5000 |
| b4 | `java b4.DateTimeServer` | `java b4.DateTimeClient` | TCP 5000 |
| b5 | `java b5.DateTimeUDPServer` | `java b5.DateTimeUDPClient` | UDP 5000 |
| b6 TCP | `java b6.TcpCalcServer` | `java b6.TcpCalcClient` | TCP 5000 |
| b6 UDP | `java b6.UdpCalcServer` | *(UdpCalcClient)* | UDP 6000 |

> ⚠️ **Lưu ý**: Các bài b1-b6 cùng dùng port 5000, **không chạy 2 server cùng lúc**!
> Phải `Ctrl+C` tắt server bài này rồi mới chạy bài khác.
