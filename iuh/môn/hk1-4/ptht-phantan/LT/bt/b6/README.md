# BÀI TẬP 4 & 5: CHAT CLIENT-SERVER BẰNG SOCKET TRONG DOCKER

**Học phần:** Phát triển hệ thống phân tán - IUH (Đại học Công nghiệp TP.HCM)
**Tài khoản Docker Hub:** `shima594`

---

## 📌 1. THÔNG TIN NỘP BÀI DOCKER HUB (THEO YÊU CẦU CỦA CÔ)

### 🔹 Image 1: CHAT SERVER

* **Link Docker Hub:** [https://hub.docker.com/r/shima594/chat-server](https://hub.docker.com/r/shima594/chat-server)
* **Lệnh kéo Image (Pull):**
  ```bash
  docker pull shima594/chat-server:latest
  ```
* **Lệnh chạy Server (Run):**
  ```bash
  docker run -d -p 5000:5000 --name socket-chat-server shima594/chat-server:latest
  ```

  *(Server sẽ lắng nghe kết nối TCP trên cổng 5000 và ghi log kết nối/broadcast)*

---

### 🔹 Image 2: CHAT CLIENT

* **Link Docker Hub:** [https://hub.docker.com/r/shima594/chat-client](https://hub.docker.com/r/shima594/chat-client)
* **Lệnh kéo Image (Pull):**
  ```bash
  docker pull shima594/chat-client:latest
  ```
* **Lệnh chạy Client (Mở nhiều terminal để chat đa người dùng):**
  - **Trên cùng máy (Localhost):**
    ```bash
    # Chạy Client thứ nhất
    docker run -it --rm --network host -e CHAT_USER=SinhVien_A shima594/chat-client:latest

    # Chạy Client thứ hai (ở terminal khác)
    docker run -it --rm --network host -e CHAT_USER=SinhVien_B shima594/chat-client:latest
    ```
  - **Kết nối tới IP Server khác máy:**
    ```bash
    docker run -it --rm -e SERVER_HOST=<IP_CỦA_SERVER> -e SERVER_PORT=5000 shima594/chat-client:latest
    ```

---

## 🛠️ 2. CẤU TRÚC MÃ NGUỒN VÀ DỰ ÁN

```
b6/
├── ChatServer.java       # ServerSocket đa luồng (CopyOnWriteArrayList, broadcast tin nhắn)
├── ChatClient.java       # Client Socket 2 luồng (Đọc từ server + gửi từ console)
├── Dockerfile.server     # Dockerfile tối ưu Alpine đóng gói Server
├── Dockerfile.client     # Dockerfile tối ưu Alpine đóng gói Client
├── Dockerfile            # Dockerfile đa năng
├── docker-compose.yml    # Chạy nhanh toàn bộ hệ thống bằng Docker Compose
├── test_chat.py          # Script tự động kiểm thử kết nối đa client & broadcast
├── README.md             # Tài liệu dự án
└── NOP_BAI.md            # Mẫu văn bản nộp bài copy nộp ngay
```

---

## 🚀 3. HƯỚNG DẪN CHẠY VÀ KIỂM THỬ TRÊN IDE HOẶC LOCAL JAVA

### Cách 1: Chạy bằng Java thuần (CLI / IDE Eclipse / VS Code / IntelliJ)

1. **Biên dịch:**
   ```bash
   javac -encoding UTF-8 ChatServer.java ChatClient.java
   ```
2. **Bật Server:**
   ```bash
   java ChatServer
   ```
3. **Mở terminal khác để bật Client 1:**
   ```bash
   java ChatClient localhost 5000 SinhVien_A
   ```
4. **Mở terminal khác để bật Client 2:**
   ```bash
   java ChatClient localhost 5000 SinhVien_B
   ```

---

## 🐳 4. HƯỚNG DẪN CHẠY BẰNG DOCKER COMPOSE

Chỉ cần 1 lệnh để dựng Server:

```bash
docker compose up -d
```

Xem log Server trực tiếp:

```bash
docker logs -f socket-chat-server
```

Dừng hệ thống:

```bash
docker compose down
```

---

## ✅ 5. KẾT QUẢ KIỂM THỬ THỰC TẾ (TEST LOG)

Chương trình đã được kiểm thử thực tế trên Docker Desktop:

```
[SERVER] Đang khởi động Server trên cổng: 5000...
[SERVER] Server đã sẵn sàng lắng nghe kết nối từ các Client!
[SERVER] Phát hiện kết nối mới từ: /172.17.0.1:59972
[SERVER] Số lượng Client hiện tại: 1
[LOG HỆ THỐNG] [13:13:41] [HỆ THỐNG] SinhVien_A đã tham gia phòng chat.
[SERVER] Phát hiện kết nối mới từ: /172.17.0.1:59984
[SERVER] Số lượng Client hiện tại: 2
[LOG HỆ THỐNG] [13:13:42] [HỆ THỐNG] SinhVien_B đã tham gia phòng chat.
[LOG TIN NHẮN] [13:13:42] SinhVien_A: Xin chao ca lop PTHT!
[LOG TIN NHẮN] [13:13:42] SinhVien_B: Chao A, minh da nhan duoc tin!
```

Client gửi tin nhắn $\to$ Server broadcast ngay lập tức tới tất cả client khác trong phòng theo đúng yêu cầu slide đề bài.
