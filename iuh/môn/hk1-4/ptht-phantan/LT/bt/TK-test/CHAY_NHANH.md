# LỆNH CHẠY HỆ THỐNG ĐẤU GIÁ (QUICK START)

---

## 🌟 PHƯƠNG ÁN 1: DÙNG 2 IMAGE TÁCH BIỆT (AUCTION-SERVER & AUCTION-CLIENT) [CHUẨN NHẤT]

### 1. Build 2 Image riêng biệt:

```bash
# 1. Build Server từ Dockerfile.server:
docker build -f Dockerfile.server -t auction-server:latest .

# 2. Build Client từ Dockerfile.client:
docker build -f Dockerfile.client -t auction-client:latest .
```

### 2. Khởi chạy hệ thống:

```bash
# Bước 1: Tạo mạng nội bộ (chỉ chạy 1 lần):
docker network create auction-net

# Bước 2: Bật Server:
docker run -d --name auction-server --network auction-net -p 1099:1099 -p 5000:5000 -e RMI_HOST=auction-server auction-server:latest

# Bước 3: Mở Terminal 1 - Bật Client A:
docker run -it --rm --network auction-net -e SERVER_HOST=auction-server -e AUCTION_USER=SinhVien_A auction-client:latest

# Bước 4: Mở Terminal 2 - Bật Client B:
docker run -it --rm --network auction-net -e SERVER_HOST=auction-server -e AUCTION_USER=SinhVien_B auction-client:latest
```

---

## ⚡ PHƯƠNG ÁN 2: DÙNG DOCKER COMPOSE (TIỆN LỢI NHẤT)

```bash
# 1. Bật Server:
docker compose up -d auction-server

# 2. Terminal 1 - Bật Client A:
docker compose run --rm client-1

# 3. Terminal 2 - Bật Client B:
docker compose run --rm client-2

# 4. Tắt hệ thống:
docker compose down
```

---

## 🚀 PHƯƠNG ÁN 3: DÙNG 1 IMAGE GỘP (AUCTION-SYSTEM)

```bash
# 1. Bật Server:
docker run -d --name auction-server --network auction-net -p 1099:1099 -p 5000:5000 -e RMI_HOST=auction-server auction-system:latest

# 2. Terminal 1 - Bật Client A:
docker run -it --rm --network auction-net auction-system:latest client auction-server 1099 SinhVien_A

# 3. Terminal 2 - Bật Client B:
docker run -it --rm --network auction-net auction-system:latest client auction-server 1099 SinhVien_B
```

---

## ☕ PHƯƠNG ÁN 4: CHẠY BẰNG JAVA THUẦN (KHÔNG DÙNG DOCKER)

```bash
# Biên dịch:
javac -encoding UTF-8 *.java

# Terminal 1 - Bật Server:
java AuctionServer

# Terminal 2 - Bật Client A:
java AuctionClient localhost 1099 SinhVien_A

# Terminal 3 - Bật Client B:
java AuctionClient localhost 1099 SinhVien_B
```

---

## 🛠️ LỆNH DỌN DẸP / RESET:

```bash
docker rm -f auction-server
```
