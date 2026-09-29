# BÀI TẬP 3: HỆ THỐNG ĐẤU GIÁ TRỰC TUYẾN PHÂN TÁN (RMI + SOCKET TCP + MULTI-THREADING)

* **Học phần:** Phát triển hệ thống phân tán - Đại học Công nghiệp TP.HCM (IUH)
* **Sinh viên:** Lê Thành Long - MSSV: `23630851`
* **Công nghệ:** Java RMI, Java Socket TCP, Java Multi-threading, Docker Multi-stage Build, Docker Compose.

---

## 📌 1. MÔ TẢ ĐỀ BÀI VÀ YÊU CẦU

1. **Server chính (qua RMI):** Quản lý danh sách sản phẩm, các phiên đấu giá và người tham gia.
2. **Kênh Socket TCP:** Khi người dùng đặt giá, Server phát sóng trực tiếp thông tin chi tiết phiên đấu giá (giá mới nhất, người giữ giá cao nhất) đến các Client đang kết nối.
3. **Đa luồng (Multi-threading):** Sử dụng Thread để hỗ trợ nhiều người tham gia đồng thời, đặt giá và cập nhật liên tục mà không gây nghẽn.
4. **Đóng gói Docker:** Build Docker Image và chạy thử nghiệm trên Docker Desktop.

---

## 🚀 2. HƯỚNG DẪN KHỞI CHẠY HỆ THỐNG

### Cách 1: Khởi chạy bằng 2 Image tách biệt (`auction-server` & `auction-client`) [Khuyên dùng]

#### 1. Build 2 Image riêng biệt:
```bash
# Build Server từ Dockerfile.server:
docker build -f Dockerfile.server -t auction-server:latest .

# Build Client từ Dockerfile.client:
docker build -f Dockerfile.client -t auction-client:latest .
```

#### 2. Khởi chạy hệ thống:
```bash
# Bước 1: Tạo mạng ảo Docker nội bộ (chỉ chạy 1 lần):
docker network create auction-net

# Bước 2: Khởi động Server:
docker run -d --name auction-server --network auction-net -p 1099:1099 -p 5000:5000 -e RMI_HOST=auction-server auction-server:latest

# Bước 3: Mở Terminal 1 - Bật Client A:
docker run -it --rm --network auction-net -e SERVER_HOST=auction-server -e AUCTION_USER=SinhVien_A auction-client:latest

# Bước 4: Mở Terminal 2 - Bật Client B:
docker run -it --rm --network auction-net -e SERVER_HOST=auction-server -e AUCTION_USER=SinhVien_B auction-client:latest
```

---

### Cách 2: Khởi chạy bằng Docker Compose (Tiện lợi nhất)

```bash
# 1. Khởi động Server đấu giá ngầm:
docker compose up -d auction-server

# 2. Mở Terminal 1 - Bật Client A:
docker compose run --rm client-1

# 3. Mở Terminal 2 - Bật Client B:
docker compose run --rm client-2

# 4. Tắt hệ thống khi kết thúc:
docker compose down
```

---

### Cách 2: Khởi chạy bằng Docker Run độc lập

```bash
# Bước 1: Tạo mạng ảo Docker nội bộ (chỉ chạy 1 lần):
docker network create auction-net

# Bước 2: Build Image:
docker build -t auction-system:latest .

# Bước 3: Khởi động Server:
docker run -d --name auction-server --network auction-net -p 1099:1099 -p 5000:5000 -e RMI_HOST=auction-server auction-system:latest

# Bước 4: Mở Terminal 1 - Chạy Client A:
docker run -it --rm --network auction-net auction-system:latest client auction-server 1099 SinhVien_A

# Bước 5: Mở Terminal 2 - Chạy Client B:
docker run -it --rm --network auction-net auction-system:latest client auction-server 1099 SinhVien_B
```

---

### Cách 3: Chạy trực tiếp bằng Java thuần (Không cần Docker)

```bash
# Biên dịch toàn bộ file Java:
javac -encoding UTF-8 *.java

# Terminal 1 - Bật Server:
java AuctionServer

# Terminal 2 - Bật Client A:
java AuctionClient localhost 1099 SinhVien_A

# Terminal 3 - Bật Client B:
java AuctionClient localhost 1099 SinhVien_B
```

---

## 💡 3. NGUYÊN LÝ HOẠT ĐỘNG VÀ KIẾN TRÚC HỆ THỐNG

### 1. Phân chia vai trò giữa RMI và Socket TCP:
* **Java RMI (Cổng 1099):**
  * Đăng ký đối tượng điều khiển từ xa `AuctionService`.
  * Cung cấp các hàm triệu gọi RPC: `getItems()`, `getItem()`, `registerUser()`, `getParticipants()`, `placeBid()`.
  * Giúp Client thao tác với dữ liệu trên Server như hàm nội bộ.
* **Java Socket TCP (Cổng 5000):**
  * Mỗi Client khi khởi động sẽ mở một Socket TCP kết nối tới Server.
  * Server duy trì danh sách kết nối Socket của các người tham gia.
  * Khi có bất kỳ ai đặt giá thành công qua RMI, Server lập tức phát sóng qua luồng Socket TCP thông tin: Mã SP, Tên SP, Giá mới nhất, Người giữ giá cao nhất đến toàn bộ Client theo thời gian thực.

### 2. Xử lý Đa luồng (Multi-threading):
* **Phía Server:**
  * Luồng ServerSocket chạy độc lập để liên tục lắng nghe kết nối Client mới.
  * Mỗi kết nối Socket từ Client được cấp một luồng `SocketClientHandler` riêng.
  * Dữ liệu sản phẩm và người tham gia được đồng bộ thread-safe bằng `ConcurrentHashMap`, `CopyOnWriteArrayList` và khối `synchronized` khi cập nhật giá thầu để tránh xung đột tranh chấp dữ liệu khi nhiều người đặt giá cùng một thời điểm.
* **Phía Client:**
  * **Luồng nền (Background Daemon Thread):** Chuyên đọc dữ liệu từ Socket TCP Server gửi về và in ra màn hình ngay khi có cập nhật giá mới mà không làm khóa giao diện bàn phím.
  * **Luồng chính (Main Thread):** Xử lý nhập liệu từ người dùng qua bàn phím và gọi các phương thức RMI.

---

## 📁 4. CẤU TRÚC THƯ MỤC

```
TK/
├── AuctionItem.java          # Đối tượng dữ liệu sản phẩm đấu giá (Serializable)
├── AuctionService.java       # Interface RMI định nghĩa các phương thức từ xa
├── AuctionServiceImpl.java   # Cài đặt dịch vụ RMI và cơ chế broadcast Socket TCP
├── AuctionServer.java        # Khởi động RMI Registry (1099) và ServerSocket TCP (5000)
├── AuctionClient.java        # Client gọi RMI và nhận thông báo trực tiếp từ Socket TCP
├── SocketClientHandler.java  # Xử lý luồng kết nối Socket TCP cho từng Client
├── Dockerfile                # Multi-stage build đóng gói ứng dụng (Temurin 21)
├── docker-compose.yml        # Điều phối cụm container Server và các Client trong mạng ảo
├── entrypoint.sh             # Script chuyển đổi vai trò Server / Client
└── README.md                 # Hướng dẫn chi tiết
```
