# THÔNG TIN NỘP BÀI TẬP SOCKET CHAT DOCKER (BÀI 4 & 5)

**Học phần:** Phát triển hệ thống phân tán - IUH
**Docker Hub Username:** `shima594`

---

## 🌟 PHƯƠNG ÁN 1: CHẠY GỘP TOÀN BỘ HỆ THỐNG TỪ 1 IMAGE DUY NHẤT (THEO ĐÚNG Ý CÔ)

> **Ưu điểm:** Chỉ cần 1 Image duy nhất `shima594/socket-chat:latest` là có thể tự động sinh ra cả Server và nhiều Client cùng lúc thông qua `docker-compose.yml` hoặc dòng lệnh Docker thông thường.

* **Link Image trên Docker Hub:** [https://hub.docker.com/r/shima594/socket-chat](https://hub.docker.com/r/shima594/socket-chat)
* **Lệnh kéo Image về máy (Pull):**
  ```bash
  docker pull shima594/socket-chat:latest
  ```

### Cách 1.1: Khởi chạy gộp tự động bằng Docker Compose (Khuyên dùng)

1. **Khởi động cùng lúc Server và 2 Client:**
   ```bash
   docker compose up -d
   ```
2. **Xem Server nhận kết nối và ghi nhận log:**
   ```bash
   docker logs socket-chat-server
   ```
3. **Mở terminal để chat trực tiếp:**
   - Chat với vai trò **Client 1**:
     ```bash
     docker attach socket-chat-client-1
     ```
   - Chat với vai trò **Client 2** (mở thêm terminal khác):
     ```bash
     docker attach socket-chat-client-2
     ```
4. **Dừng và dọn dẹp hệ thống khi xong:**
   ```bash
   docker compose down
   ```

# Terminal 1: Chạy Client 1

docker compose run --rm client-1

# Terminal 2: Chạy Client 2

docker compose run --rm client-2

### Cách 1.2: Chạy lẻ từng container thủ công từ 1 Image này

* **Chạy Server:**
  ```bash
  docker run -d -p 5000:5000 --name socket-chat-server shima594/socket-chat:latest
  ```
* **Chạy Client (mở nhiều terminal để chat đa máy/đa người dùng):**
  ```bash
  docker run -it --rm --network host shima594/socket-chat:latest client
  ```

---

## 📋 PHƯƠNG ÁN 2: DÀNH CHO FORM NỘP BÀI YÊU CẦU 2 LINK IMAGE TÁCH RỜI

### 🔹 Image 1: CHAT SERVER

* **Link Image Docker Hub:** [https://hub.docker.com/r/shima594/chat-server](https://hub.docker.com/r/shima594/chat-server)
* **Lệnh pull image:**
  ```bash
  docker pull shima594/chat-server:latest
  ```
* **Lệnh chạy Server:**
  ```bash
  docker run -d -p 5000:5000 --name socket-chat-server shima594/chat-server:latest
  ```

### 🔹 Image 2: CHAT CLIENT

* **Link Image Docker Hub:** [https://hub.docker.com/r/shima594/chat-client](https://hub.docker.com/r/shima594/chat-client)
* **Lệnh pull image:**
  ```bash
  docker pull shima594/chat-client:latest
  ```
* **Lệnh chạy Client:**
  ```bash
  docker run -it --rm --network host shima594/chat-client:latest
  ```

---

## ⚙️ TÓM TẮT CHỨC NĂNG KỸ THUẬT ĐÃ HOÀN THÀNH:

1. **Server (`ChatServer.java`):**

   - Sử dụng `ServerSocket` TCP cổng `5000`.
   - Phục vụ nhiều Client đồng thời qua cơ chế đa luồng (Multi-threading).
   - Quản lý danh sách kết nối thread-safe bằng `CopyOnWriteArrayList`.
   - Nhận tin nhắn từ bất kỳ Client nào $\to$ Broadcast thời gian thực tới tất cả các Client khác trong phòng chat kèm dấu thời gian `[HH:mm:ss]`.
   - Xử lý mượt mà sự kiện tham gia phòng và rời phòng khi gõ `exit`/`quit`.
2. **Client (`ChatClient.java`):**

   - Kết nối Socket tới Server.
   - Kiến trúc 2 luồng độc lập: 1 luồng đọc tin nhắn liên tục từ Server, 1 luồng nhập liệu từ bàn phím và gửi lên Server.
3. **Đóng gói Docker & Docker Compose:**

   - Multi-stage build trên nền `eclipse-temurin:21-jre-alpine` siêu nhẹ (~74 MB).
   - Entrypoint script tự động điều phối: mặc định chạy Server, nhận tham số `client` để chạy Client.
   - `docker-compose.yml` thiết lập sẵn toàn bộ mạng nội bộ `chat-net` và tự động liên kết các container từ duy nhất 1 Image.
   - Đã kiểm thử thành công trên Docker Desktop và đẩy đầy đủ lên Docker Hub `shima594`.
