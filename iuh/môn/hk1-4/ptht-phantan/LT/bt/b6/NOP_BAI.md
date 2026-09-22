# THÔNG TIN BÁO CÁO & NỘP BÀI TẬP SOCKET CHAT DOCKER (BÀI 4 & 5)

* **Học phần:** Phát triển hệ thống phân tán - IUH (Đại học Công nghiệp TP.HCM)
* **Sinh viên thực hiện:** Lê Thành Long - MSSV: `23630851`
* **Tài khoản Docker Hub:** `shima594`
* **Công nghệ sử dụng:** Java Socket TCP (ServerSocket, Socket, Multi-threading), Docker Multi-stage Build (`eclipse-temurin:21-jre-alpine`), Docker Compose.

---

## 🔗 1. DANH SÁCH IMAGE TRÊN DOCKER HUB

| Tên Image                                | Mục đích                                                | Link Docker Hub                                                                       | Lệnh Pull                                  |
| ----------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------- |
| **`shima594/socket-chat:latest`** | **1 Image gộp cả Server & Client** (Khuyên dùng) | [hub.docker.com/r/shima594/socket-chat](https://hub.docker.com/r/shima594/socket-chat) | `docker pull shima594/socket-chat:latest` |
| **`shima594/chat-server:latest`** | Image chuyên chạy Server                                 | [hub.docker.com/r/shima594/chat-server](https://hub.docker.com/r/shima594/chat-server) | `docker pull shima594/chat-server:latest` |
| **`shima594/chat-client:latest`** | Image chuyên chạy Client                                 | [hub.docker.com/r/shima594/chat-client](https://hub.docker.com/r/shima594/chat-client) | `docker pull shima594/chat-client:latest` |

---

## 🛠️ 2. QUY TRÌNH BUILD VÀ PUSH LÊN DOCKER HUB (TỪ A ĐẾN Z)

Dưới đây là **toàn bộ các bước thực tế đã thực hiện** từ khi có file code Java cho đến lúc đóng gói thành Docker Image và đẩy lên Docker Hub:

### Bước 2.1: Biên dịch và chạy thử nghiệm Java thuần cục bộ

Trước khi đóng gói Docker, mã nguồn Java được biên dịch và kiểm tra tính tương thích:

```bash
# Di chuyển vào thư mục dự án
cd d:\folder\rac\iuh\môn\hk1-4\ptht-phantan\LT\bt\b6

# Biên dịch mã nguồn Java với bảng mã UTF-8
javac -encoding UTF-8 ChatServer.java ChatClient.java
```

---

### Bước 2.2: Đóng gói (Build) Docker Image

#### 🌟 Cách A: Build Image gộp đa năng `socket-chat` (Dùng Dockerfile)

Sử dụng kỹ thuật **Multi-stage build** với Base Image `eclipse-temurin:21-jdk-alpine` để biên dịch và `eclipse-temurin:21-jre-alpine` để chạy, giúp Image siêu nhẹ (chỉ ~74 MB):

```bash
# Lệnh build Image gộp Server & Client
docker build -t shima594/socket-chat:latest .
```

*(Cờ `-t shima594/socket-chat:latest`: Đặt tên tag cho image gồm `<Username>/<Tên_Repo>:<Tag>`)*.

#### 🌟 Cách B: Build 2 Image tách rời (Server riêng, Client riêng)

Dành cho trường hợp nộp bài yêu cầu tách thành 2 Repository độc lập:

```bash
# 1. Build Image Server từ Dockerfile.server
docker build -f Dockerfile.server -t shima594/chat-server:latest .

# 2. Build Image Client từ Dockerfile.client
docker build -f Dockerfile.client -t shima594/chat-client:latest .
```

*(Cờ `-f Dockerfile.server`: Chỉ định rõ file Dockerfile cụ thể để build thay vì lấy mặc định)*.

---

### Bước 2.3: Đăng nhập và Đẩy (Push) Image lên Docker Hub

```bash
# 1. Đăng nhập vào tài khoản Docker Hub trên máy
docker login -u shima594

# 2. Push Image gộp socket-chat lên Docker Hub
docker push shima594/socket-chat:latest

# 3. Push 2 Image tách rời lên Docker Hub
docker push shima594/chat-server:latest
docker push shima594/chat-client:latest
```

Sau khi lệnh push hoàn tất 100%, Image đã xuất hiện công khai trên Docker Hub của tài khoản `shima594`.

---

## 🚀 3. HƯỚNG DẪN CHẠY VÀ TEST HỆ THỐNG ĐÃ ĐÓNG GÓI

### 📌 PHƯƠNG ÁN 1: CHẠY BẰNG DOCKER COMPOSE TỪ 1 IMAGE GỘP (KHUYÊN DÙNG)

File `docker-compose.yml` được cấu hình để cùng lúc khởi tạo Server và các Client thông qua mạng ảo nội bộ `chat-net`:

1. **Khởi động Server ngầm:**
   ```bash
   docker compose up -d chat-server
   ```
2. **Xem Server đã bật và lắng nghe cổng 5000:**
   ```bash
   docker logs socket-chat-server
   ```
3. **Mở Terminal 1 - Chạy Client A:**
   ```bash
   docker compose run --rm client-1
   ```
4. **Mở Terminal 2 - Chạy Client B (ở cửa sổ dòng lệnh khác):**
   ```bash
   docker compose run --rm client-2
   ```
5. **Dừng và dọn dẹp hệ thống khi test xong:**
   ```bash
   docker compose down
   ```

---

### 📌 PHƯƠNG ÁN 2: CHẠY BẰNG LỆNH DOCKER RUN THỦ CÔNG (ĐỘC LẬP)

#### 🌟 Cách A: Dùng 2 Image tách biệt (`chat-server` & `chat-client`) qua Docker Network `chat-net` (Khuyên dùng - Chuẩn nhất mọi OS):

```bash
# Bước 1: Tạo mạng ảo Docker nội bộ (chỉ cần chạy 1 lần duy nhất):
docker network create chat-net

# Bước 2: Khởi động Server gắn vào mạng chat-net:
docker run -d --name socket-chat-server --network chat-net -p 5000:5000 shima594/chat-server:latest

# Bước 3: Mở Terminal 1 - Bật Client A (tự động phân giải hostname 'socket-chat-server'):
docker run -it --rm --network chat-net -e SERVER_HOST=socket-chat-server -e CHAT_USER=SinhVien_A shima594/chat-client:latest

# Bước 4: Mở Terminal 2 - Bật Client B (cùng tham gia phòng chat):
docker run -it --rm --network chat-net -e SERVER_HOST=socket-chat-server -e CHAT_USER=SinhVien_B shima594/chat-client:latest
```

> **💡 Tại sao dùng Docker Network (`--network chat-net`) là chuẩn nhất:**
>
> - **Tự động phân giải DNS nội bộ:** Container Server có tên `--name socket-chat-server` thì container Client chỉ cần trỏ `SERVER_HOST=socket-chat-server` là tự động tìm thấy nhau.
> - **Tương thích 100% mọi nền tảng:** Không bị phụ thuộc vào môi trường máy ảo WSL2 của Windows Docker Desktop, không lo xung đột port và hoàn toàn giống với kiến trúc microservices thực tế.

---

#### 🌟 Cách B: Dùng 1 Image gộp đa năng `shima594/socket-chat:latest` qua Docker Network `chat-net`:

```bash
# Bước 1: Tạo mạng ảo Docker nội bộ (nếu chưa tạo):
docker network create chat-net

# Bước 2: Bật Server trong mạng chat-net:
docker run -d --name socket-chat-server --network chat-net -p 5000:5000 shima594/socket-chat:latest

# Bước 3: Bật Client A (Mở terminal 1):
docker run -it --rm --network chat-net shima594/socket-chat:latest client socket-chat-server 5000 SinhVien_A

# Bước 4: Bật Client B (Mở terminal 2):
docker run -it --rm --network chat-net shima594/socket-chat:latest client socket-chat-server 5000 SinhVien_B
```

*(Ghi chú: Nếu chạy trên Linux thuần, bạn cũng có thể dùng cờ `--network host` và trỏ `localhost 5000`)*.

---

## 📋 4. BẰNG CHỨNG KẾT QUẢ TEST THỰC TẾ (LOG TERMINAL)

Hệ thống đã được test thực tế truyền nhận tin nhắn giữa các Container:

### Log tại Server (`docker logs socket-chat-server`):

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

### Màn hình Client 1 (SinhVien_A):

```
[CLIENT] Đang kết nối tới Server chat-server:5000...
[CLIENT] Kết nối thành công tới Server!
[HỆ THỐNG] [13:13:42] [HỆ THỐNG] SinhVien_B đã tham gia phòng chat.
> Xin chao ca lop PTHT IUH!
[13:13:48] SinhVien_B: Chao ban A, minh nhan duoc tin roi nhe!
```

### Màn hình Client 2 (SinhVien_B):

```
[CLIENT] Đang kết nối tới Server chat-server:5000...
[CLIENT] Kết nối thành công tới Server!
[13:13:45] SinhVien_A: Xin chao ca lop PTHT IUH!
> Chao ban A, minh nhan duoc tin roi nhe!
```

---

## ⚙️ 5. CẤU TRÚC THƯ MỤC DỰ ÁN

```
b6/
├── ChatServer.java       # Mã nguồn Server đa luồng (ServerSocket, CopyOnWriteArrayList, broadcast)
├── ChatClient.java       # Mã nguồn Client 2 luồng (Socket, đọc tin nhắn song song với gửi)
├── Dockerfile            # Multi-stage build đóng gói CẢ Server VÀ Client vào 1 Image duy nhất
├── Dockerfile.server     # Dockerfile riêng cho Server
├── Dockerfile.client     # Dockerfile riêng cho Client
├── entrypoint.sh         # Script shell điều phối container (chạy Server hoặc Client linh hoạt)
├── docker-compose.yml    # Cấu hình tự động khởi chạy cụm mạng Server + Client đa container
├── test_chat.py          # Script Python tự động kiểm thử kết nối đa client & broadcast
├── README.md             # Tài liệu kỹ thuật chi tiết của dự án
└── NOP_BAI.md            # Tài liệu tổng hợp nộp bài chuẩn chỉnh
```

---

## 💡 6. NGUYÊN LÝ HOẠT ĐỘNG & KIẾN TRÚC HỆ THỐNG

### 1. Kiến trúc Java Socket TCP Đa luồng (Multi-threading):

* **Phía Server (`ChatServer.java`):**

  - Mở cổng `ServerSocket(5000)` chạy trong vòng lặp vô tận `while(running)` để liên tục lắng nghe kết nối mới từ Client.
  - Mỗi khi có một Client kết nối (`serverSocket.accept()`), Server khởi tạo một đối tượng `ClientHandler` chạy trên một Thread độc lập (`new Thread(clientHandler).start()`).
  - Danh sách Client kết nối được quản lý an toàn bằng `CopyOnWriteArrayList<ClientHandler>` nhằm loại bỏ hoàn toàn lỗi tranh chấp tài nguyên luồng (`ConcurrentModificationException`) khi vừa broadcast tin nhắn vừa có Client gia nhập hoặc thoát.
  - Cơ chế **Broadcast**: Duyệt qua danh sách toàn bộ Client đang kết nối để gửi dữ liệu bằng `PrintWriter.println()`.
  - Cơ chế **Dọn dẹp kết nối (Cleanup)**: Khi Client ngắt kết nối hoặc gửi lệnh `exit`/`quit`, Server xóa Client khỏi danh sách, đóng socket/stream và tự động thông báo rời phòng tới các Client còn lại.
* **Phía Client (`ChatClient.java`):**

  - Mở kết nối Socket TCP tới Server thông qua `new Socket(host, port)`.
  - Thiết kế **2 luồng song song không đồng bộ**:
    1. **Luồng đọc (Read Thread):** Chạy ngầm độc lập để lắng nghe các tin nhắn broadcast gửi từ Server và in ra console ngay khi có tin nhắn mới mà không gây nghẽn (non-blocking).
    2. **Luồng chính (Main Thread):** Đọc ký tự từ bàn phím console qua `Scanner(System.in)` và gửi lên Server.

### 2. Kỹ thuật Đóng gói Docker Tối ưu:

* **Multi-stage Build:**
  - **Stage 1 (Builder):** Dùng `eclipse-temurin:21-jdk-alpine` chỉ để biên dịch file `.java` thành bytecode `.class`.
  - **Stage 2 (Runtime):** Sử dụng `eclipse-temurin:21-jre-alpine` (loại bỏ hoàn toàn trình biên dịch JDK cồng kềnh và tài liệu).
  - **Hiệu quả:** Kích thước image giảm từ **~450MB** xuống chỉ còn **~74MB** (giảm hơn 80%), tốc độ pull và khởi động nhanh vượt trội.
* **Mạng ảo Docker Network (`chat-net`):**
  - Sử dụng mạng Bridge ảo do Docker quản lý.
  - Tích hợp sẵn cơ chế phân giải tên miền nội bộ (Embedded DNS Server), giúp container Client kết nối trực tiếp tới Server qua hostname `socket-chat-server` mà không cần phụ thuộc IP máy host hay hệ điều hành bên ngoài.
