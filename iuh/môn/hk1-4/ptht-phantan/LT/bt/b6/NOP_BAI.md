# THÔNG TIN NỘP BÀI TẬP SOCKET CHAT DOCKER (BÀI 4 & 5)
(Dùng để copy-paste nộp vào form / link nộp bài của cô)

---

### THÔNG TIN TÀI KHOẢN DOCKER HUB:
* **Docker Hub Username:** `shima594`

---

### LINK VÀ LỆNH PULL IMAGE 1: SERVER
* **Link Image Docker Hub:** https://hub.docker.com/r/shima594/chat-server
* **Lệnh pull image:**
  ```bash
  docker pull shima594/chat-server:latest
  ```
* **Lệnh khởi chạy Server:**
  ```bash
  docker run -d -p 5000:5000 --name socket-chat-server shima594/chat-server:latest
  ```

---

### LINK VÀ LỆNH PULL IMAGE 2: CLIENT
* **Link Image Docker Hub:** https://hub.docker.com/r/shima594/chat-client
* **Lệnh pull image:**
  ```bash
  docker pull shima594/chat-client:latest
  ```
* **Lệnh khởi chạy Client (chạy ở nhiều terminal để chat đa người dùng):**
  ```bash
  docker run -it --rm --network host shima594/chat-client:latest
  ```

---

### TÓM TẮT CHỨC NĂNG ĐÃ THỰC HIỆN:
1. **Server (`ChatServer.java`):**
   - Sử dụng `ServerSocket` lắng nghe cổng `5000`.
   - Phục vụ đa Client đồng thời bằng kỹ thuật Multi-threading (mỗi client 1 luồng riêng biệt).
   - Quản lý danh sách Client an toàn với `CopyOnWriteArrayList`.
   - Khi bất kỳ Client nào gửi tin nhắn $\to$ Server tự động broadcast đến tất cả các Client khác kèm mốc thời gian và tên người gửi.
   - Xử lý thông báo khi Client tham gia hoặc thoát phòng (`exit`/`quit`).

2. **Client (`ChatClient.java`):**
   - Kết nối Socket tới Server.
   - Thiết kế 2 luồng độc lập: 1 luồng chuyên lắng nghe tin nhắn đến từ Server và in ra console, 1 luồng đọc bàn phím và gửi dữ liệu lên Server.

3. **Đóng gói Docker & Docker Hub:**
   - Sử dụng Docker multi-stage build trên nền Alpine nhẹ tối ưu dung lượng (~74 MB).
   - Đã kiểm thử thành công trên Docker Desktop cục bộ và đẩy (push) đầy đủ 2 Image lên Docker Hub công khai.
