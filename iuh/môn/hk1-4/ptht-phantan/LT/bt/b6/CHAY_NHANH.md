# HƯỚNG DẪN CÁC LỆNH CHẠY HỆ THỐNG (CHẠY NHANH)

---

## 🚀 CÁCH 1: DÙNG DOCKER NETWORK (KHUYÊN DÙNG - 1 IMAGE GỘP)

```bash
# 1. Tạo mạng nội bộ (chỉ cần chạy 1 lần):
docker network create chat-net

# 2. Bật Server:
docker run -d --name socket-chat-server --network chat-net -p 5000:5000 shima594/socket-chat:latest

# 3. Mở Terminal 1 - Bật Client A:
docker run -it --rm --network chat-net shima594/socket-chat:latest client socket-chat-server 5000 SinhVien_A

# 4. Mở Terminal 2 - Bật Client B:
docker run -it --rm --network chat-net shima594/socket-chat:latest client socket-chat-server 5000 SinhVien_B
```

---

## ⚡ CÁCH 2: DÙNG DOCKER COMPOSE (TIỆN LỢI NHẤT)

*(Chạy trong thư mục `b6`)*

```bash
# 1. Bật Server ngầm:
docker compose up -d chat-server

# 2. Mở Terminal 1 - Bật Client 1:
docker compose run --rm client-1

# 3. Mở Terminal 2 - Bật Client 2:
docker compose run --rm client-2

# 4. Tắt và dọn dẹp hệ thống:
docker compose down
```

---

## 📦 CÁCH 3: DÙNG 2 IMAGE TÁCH RỜI (SERVER & CLIENT RIÊNG)

```bash
# 1. Tạo mạng (nếu chưa tạo):
docker network create chat-net

# 2. Bật Server:
docker run -d --name socket-chat-server --network chat-net -p 5000:5000 shima594/chat-server:latest

# 3. Mở Terminal 1 - Bật Client A:
docker run -it --rm --network chat-net -e SERVER_HOST=socket-chat-server -e CHAT_USER=SinhVien_A shima594/chat-client:latest

# 4. Mở Terminal 2 - Bật Client B:
docker run -it --rm --network chat-net -e SERVER_HOST=socket-chat-server -e CHAT_USER=SinhVien_B shima594/chat-client:latest
```

---

## ☕ CÁCH 4: CHẠY TRỰC TIẾP BẰNG JAVA THUẦN (KHÔNG CẦN DOCKER)

```bash
# Terminal 1 - Bật Server:
java ChatServer

# Terminal 2 - Bật Client A:
java ChatClient localhost 5000 SinhVien_A

# Terminal 3 - Bật Client B:
java ChatClient localhost 5000 SinhVien_B
```

---

## 🛠️ LỆNH DỌN DẸP KHI CẦN RESET (NẾU BỊ TRÙNG TÊN/PORT):

```bash
# Xóa container Server cũ:
docker rm -f socket-chat-server
```
