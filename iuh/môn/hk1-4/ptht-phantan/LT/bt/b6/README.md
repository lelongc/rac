# BÀI TẬP 4 & 5: HỆ THỐNG CHAT CLIENT - SERVER BẰNG JAVA SOCKET TRONG DOCKER

* **Học phần:** Phát triển hệ thống phân tán - Đại học Công nghiệp TP.HCM (IUH)
* **Sinh viên:** Lê Thành Long - MSSV: `23630851`
* **Docker Hub Repository:** `https://hub.docker.com/u/shima594`

---

## 📌 1. DANH SÁCH DOCKER IMAGES ĐÃ PUBLIC TRÊN DOCKER HUB

| Tên Image | Mục đích | Link Docker Hub | Kích thước |
|---|---|---|---|
| **`shima594/socket-chat:latest`** | **1 Image gộp cả Server & Client** | [hub.docker.com/r/shima594/socket-chat](https://hub.docker.com/r/shima594/socket-chat) | ~74 MB |
| **`shima594/chat-server:latest`** | Image riêng cho Server | [hub.docker.com/r/shima594/chat-server](https://hub.docker.com/r/shima594/chat-server) | ~74 MB |
| **`shima594/chat-client:latest`** | Image riêng cho Client | [hub.docker.com/r/shima594/chat-client](https://hub.docker.com/r/shima594/chat-client) | ~74 MB |

---

## 🛠️ 2. TOÀN BỘ CÁC BƯỚC BUILD, ĐÓNG GÓI VÀ PUSH LÊN DOCKER HUB

### Bước 2.1: Biên dịch thử nghiệm mã nguồn Java cục bộ
```bash
# Di chuyển vào thư mục dự án
cd d:\folder\rac\iuh\môn\hk1-4\ptht-phantan\LT\bt\b6

# Biên dịch mã nguồn Java
javac -encoding UTF-8 ChatServer.java ChatClient.java
```

### Bước 2.2: Build Docker Image từ Dockerfile
Hệ thống sử dụng kỹ thuật **Multi-stage build**:
- **Stage 1 (Builder):** Dùng `eclipse-temurin:21-jdk-alpine` để biên dịch file `.java` thành `.class`.
- **Stage 2 (Runtime):** Chỉ sao chép các file `.class` sang `eclipse-temurin:21-jre-alpine` (chỉ chứa JRE tối giản, bỏ toàn bộ trình biên dịch JDK để giảm kích thước từ >400MB xuống chỉ còn ~74MB).

#### A. Build Image gộp `socket-chat` (Cả Server & Client):
```bash
docker build -t shima594/socket-chat:latest .
```

#### B. Build 2 Image riêng biệt (Nếu cần nộp link tách rời):
```bash
# 1. Build Server từ Dockerfile.server
docker build -f Dockerfile.server -t shima594/chat-server:latest .

# 2. Build Client từ Dockerfile.client
docker build -f Dockerfile.client -t shima594/chat-client:latest .
```

### Bước 2.3: Đăng nhập và Push lên Docker Hub
```bash
# Đăng nhập vào tài khoản Docker Hub
docker login -u shima594

# Push Image gộp
docker push shima594/socket-chat:latest

# Push 2 Image tách biệt
docker push shima594/chat-server:latest
docker push shima594/chat-client:latest
```

---

## 🚀 3. HƯỚNG DẪN KHỞI CHẠY VÀ SỬ DỤNG HỆ THỐNG

### Cách 1: Khởi chạy bằng Docker Compose (Khuyên dùng - Nhanh nhất)
File `docker-compose.yml` đã thiết lập sẵn toàn bộ mạng `chat-net` và liên kết giữa Server với các Client:

1. **Khởi động Server ngầm:**
   ```bash
   docker compose up -d chat-server
   ```
2. **Kiểm tra trạng thái Server:**
   ```bash
   docker logs socket-chat-server
   ```
3. **Chạy Client A (Terminal 1):**
   ```bash
   docker compose run --rm client-1
   ```
4. **Chạy Client B (Terminal 2):**
   ```bash
   docker compose run --rm client-2
   ```
5. **Dừng và dọn dẹp:**
   ```bash
   docker compose down
   ```

---

### Cách 2: Khởi chạy thủ công bằng Docker Run (Độc lập)

#### 🌟 Phương án A: Dùng 2 Image tách biệt (`chat-server` & `chat-client`) qua Docker Network `chat-net` (Khuyên dùng - Chuẩn nhất mọi OS):
```bash
# Bước 1: Tạo mạng ảo Docker nội bộ (chỉ cần chạy 1 lần duy nhất):
docker network create chat-net

# Bước 2: Bật Server trong mạng chat-net:
docker run -d --name socket-chat-server --network chat-net -p 5000:5000 shima594/chat-server:latest

# Bước 3: Bật Client 1 (ở Terminal 1 - kết nối qua hostname 'socket-chat-server'):
docker run -it --rm --network chat-net -e SERVER_HOST=socket-chat-server -e CHAT_USER=SinhVien_A shima594/chat-client:latest

# Bước 4: Bật Client 2 (ở Terminal 2 - cùng tham gia phòng chat):
docker run -it --rm --network chat-net -e SERVER_HOST=socket-chat-server -e CHAT_USER=SinhVien_B shima594/chat-client:latest
```

> **💡 Tại sao nên dùng Docker Network (`--network chat-net`):**
> - Các container tự động phân giải tên miền nội bộ của nhau (container Server đặt tên là `socket-chat-server` thì Client chỉ cần trỏ `SERVER_HOST=socket-chat-server`).
> - Hoạt động độc lập và hoàn hảo trên mọi hệ điều hành (Windows, macOS, Linux) mà không bị phụ thuộc vào WSL2 hay cấu hình port máy host.

#### 🌟 Phương án B: Dùng 1 Image gộp đa năng `shima594/socket-chat:latest`:
```bash
# Bước 1: Tạo mạng ảo Docker nội bộ (nếu chưa tạo):
docker network create chat-net

# Bước 2: Bật Server trong mạng chat-net:
docker run -d --name socket-chat-server --network chat-net -p 5000:5000 shima594/socket-chat:latest

# Bước 3: Bật Client 1 (ở Terminal 1):
docker run -it --rm --network chat-net shima594/socket-chat:latest client socket-chat-server 5000 SinhVien_A

# Bước 4: Bật Client 2 (ở Terminal 2):
docker run -it --rm --network chat-net shima594/socket-chat:latest client socket-chat-server 5000 SinhVien_B
```

---

### Cách 3: Chạy trực tiếp bằng Java CLI (Không cần Docker)
```bash
# Terminal 1: Bật Server
java ChatServer

# Terminal 2: Bật Client 1
java ChatClient localhost 5000 SinhVien_A

# Terminal 3: Bật Client 2
java ChatClient localhost 5000 SinhVien_B
```

---

## 📋 4. BẰNG CHỨNG KẾT QUẢ KIỂM THỬ THỰC TẾ

```
[SERVER] Đang khởi động Server trên cổng: 5000...
[SERVER] Server đã sẵn sàng lắng nghe kết nối từ các Client!
[SERVER] Phát hiện kết nối mới từ: /172.18.0.3:54210
[SERVER] Số lượng Client hiện tại: 1
[LOG HỆ THỐNG] [13:13:41] [HỆ THỐNG] SinhVien_A đã tham gia phòng chat.
[SERVER] Phát hiện kết nối mới từ: /172.18.0.4:54218
[SERVER] Số lượng Client hiện tại: 2
[LOG HỆ THỐNG] [13:13:42] [HỆ THỐNG] SinhVien_B đã tham gia phòng chat.
[LOG TIN NHẮN] [13:13:45] SinhVien_A: Xin chao ca lop PTHT IUH!
[LOG TIN NHẮN] [13:13:48] SinhVien_B: Chao ban A, minh nhan duoc tin roi nhe!
```

---

## 📁 5. CẤU TRÚC FILE DỰ ÁN

```
b6/
├── ChatServer.java       # ServerSocket TCP cổng 5000, xử lý đa luồng, broadcast tin nhắn
├── ChatClient.java       # Socket Client, gồm 2 thread (đọc tin nhắn từ server & gửi từ console)
├── Dockerfile            # Multi-stage build gộp cả Server và Client vào 1 image duy nhất
├── Dockerfile.server     # Dockerfile riêng cho Server
├── Dockerfile.client     # Dockerfile riêng cho Client
├── entrypoint.sh         # Script điều hướng chạy Server (mặc định) hoặc Client
├── docker-compose.yml    # File compose quản lý cụm mạng container chat-net
├── test_chat.py          # Script Python tự động test kịch bản nhiều client chat đồng thời
├── README.md             # Tài liệu dự án đầy đủ
└── NOP_BAI.md            # Tài liệu nộp bài chuẩn chỉnh
```

---

## 💡 6. NGUYÊN LÝ HOẠT ĐỘNG & KIẾN TRÚC HỆ THỐNG

### 1. Kiến trúc Java Socket TCP Đa luồng (Multi-threading):
* **Phía Server (`ChatServer.java`):**
  - Mở cổng `ServerSocket(5000)` chạy trong vòng lặp vô tận `while(running)` để lắng nghe kết nối mới.
  - Khi có Client kết nối (`serverSocket.accept()`), Server tạo một đối tượng `ClientHandler` chạy trên một luồng độc lập (`new Thread(clientHandler).start()`).
  - Danh sách Client được quản lý an toàn bằng `CopyOnWriteArrayList<ClientHandler>` để tránh lỗi xung đột luồng (`ConcurrentModificationException`) khi vừa broadcast tin nhắn vừa có Client kết nối/ngắt kết nối.
  - Cơ chế **Broadcast**: Duyệt qua danh sách các Client đang online và gửi dữ liệu qua `PrintWriter.println()`.
  - Cơ chế **Dọn dẹp kết nối (Cleanup)**: Khi Client ngắt kết nối hoặc gửi lệnh thoát, Server tự động gỡ Client khỏi danh sách, đóng socket/stream và gửi thông báo rời phòng tới toàn thể Client còn lại.

* **Phía Client (`ChatClient.java`):**
  - Khởi tạo kết nối TCP tới Server qua `new Socket(host, port)`.
  - Sử dụng **2 luồng chạy song song độc lập**:
    1. **Luồng đọc (Read Thread):** Chạy ngầm liên tục lắng nghe các tin nhắn từ Server và in ra màn hình console ngay lập tức mà không chặn bàn phím.
    2. **Luồng chính (Main Thread):** Nhận dữ liệu nhập từ bàn phím người dùng qua `Scanner(System.in)` và gửi lên Server.

### 2. Kỹ thuật Đóng gói Docker Tối ưu:
* **Multi-stage Build:**
  - **Stage 1 (Builder):** Dùng `eclipse-temurin:21-jdk-alpine` chỉ để biên dịch file `.java` thành `.class`.
  - **Stage 2 (Runtime):** Chỉ dùng `eclipse-temurin:21-jre-alpine` (loại bỏ hoàn toàn trình biên dịch JDK cồng kềnh và các công cụ phát triển không cần thiết).
  - **Kết quả:** Kích thước image giảm từ **~450MB** xuống chỉ còn **~74MB** (giảm hơn 80%), khởi động cực nhanh và tiết kiệm tài nguyên.
* **Mạng ảo Docker Network (`chat-net`):**
  - Định tuyến các container qua mạng Bridge nội bộ.
  - Docker tự động tích hợp dịch vụ phân giải tên miền (Embedded DNS Server), giúp container Client kết nối trực tiếp tới container Server thông qua tên `--name socket-chat-server` mà không cần quan tâm IP cụ thể hay phụ thuộc hệ điều hành.
