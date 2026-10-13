# BÁO CÁO & HƯỚNG DẪN NỘP BÀI KIỂM TRA THƯỜNG KỲ 1 (ĐỀ 2)
### MÔN: PHÁT TRIỂN HỆ THỐNG PHÂN TÁN - IUH

* **Sinh viên thực hiện:** Lê Thành Long
* **Mã số sinh viên (MSSV):** `23630851`
* **Docker Hub Account:** `shima594`
* **Tên Docker Image (yêu cầu đề bài):** `shima594/de2:23630851`
* **File nộp lên LMS:** `23630851_de2.rar`

---

## 📌 1. ĐÁP ỨNG CÁC YÊU CẦU CỦA ĐỀ BÀI

1. **Một image duy nhất cho cả Server và Client**: Đóng gói bằng `Dockerfile` Multi-stage build kết hợp `entrypoint.sh`, tự động điều phối chạy `ChatServer` hoặc `ChatClient`.
2. **Server quản lý nhiều phòng chat**:
   - Phòng mặc định: `general`.
   - Tin nhắn chỉ hiển thị cho các client cùng phòng.
3. **Client tham gia phòng và chuyển phòng**:
   - Nhập `Nickname` khi khởi động theo định dạng: `23630851_1`, `23630851_2`, ...
   - Chọn phòng khi bắt đầu hoặc nhấn Enter để vào phòng mặc định `general`.
   - Lệnh `/join <ten_phong>`: Chuyển đổi phòng chat linh hoạt trong khi đang trò chuyện.
4. **Ghi log `chatroom.log` đúng chuẩn định dạng**:
   - Định dạng: `[room][nickname][HH:MM:SS]: message`
   - Ví dụ thực tế trong file log:
     ```
     [general][23630851_1][19:11:36]: Xin chao phong general
     [room_cntt][23630851_1][19:11:36]: Toi da qua phong room_cntt roi
     ```

---

## 🚀 2. HƯỚNG DẪN CHẠY THỬ NGHIỆM

### Cách 1: Chạy bằng Docker Compose (Khuyên dùng)
```bash
# 1. Khởi động Chat Server ngầm:
docker compose up -d chat-server

# 2. Mở Terminal 1 - Bật Client 1 (Nickname: 23630851_1, phòng: general):
docker compose run --rm client-1

# 3. Mở Terminal 2 - Bật Client 2 (Nickname: 23630851_2, phòng: general):
docker compose run --rm client-2

# 4. Thử nghiệm chuyển phòng chat:
# Tại cửa sổ Client 1, gõ:
/join room_cntt
# Sau đó chat, tin nhắn chỉ hiển thị cho người trong phòng room_cntt.

# 5. Tắt hệ thống khi kết thúc:
docker compose down
```

---

### Cách 2: Chạy trực tiếp bằng Java thuần
```bash
# Biên dịch mã nguồn:
javac -encoding UTF-8 ChatServer.java ChatClient.java

# Terminal 1 - Chạy Server:
java ChatServer

# Terminal 2 - Chạy Client 1:
java ChatClient localhost 5000 23630851_1 general

# Terminal 3 - Chạy Client 2:
java ChatClient localhost 5000 23630851_2 general
```

---

## 📤 3. HƯỚNG DẪN NỘP BÀI TỪNG BƯỚC

### BƯỚC 1: Đẩy Image lên Docker Hub
Mở Terminal tại thư mục `TK1`:

```bash
# 1. Đăng nhập Docker Hub:
docker login

# 2. Build Image với đúng tag theo đề bài (Username/de2:MaSV):
docker build -t shima594/de2:23630851 .

# 3. Push Image lên Docker Hub:
docker push shima594/de2:23630851
```
> **Link kiểm tra trên Docker Hub:** `https://hub.docker.com/r/shima594/de2/tags`

---

### BƯỚC 2: Nén file `23630851_de2.rar` nộp lên LMS
Tập tin nộp lên LMS gồm các file:
- `ChatServer.java`
- `ChatClient.java`
- `Dockerfile`
- `docker-compose.yml`
- `entrypoint.sh`
- `chatroom.log`

#### Cách nén bằng chuột (WinRAR):
1. Chọn 6 file trên: `ChatServer.java`, `ChatClient.java`, `Dockerfile`, `docker-compose.yml`, `entrypoint.sh`, `chatroom.log`.
2. Bấm chuột phải $\rightarrow$ Chọn **Add to archive...** (Thêm vào tập tin nén).
3. Đặt tên file là **`23630851_de2.rar`** (hoặc `23630851_de2.zip` tùy yêu cầu hệ thống).
4. Bấm **OK**.

#### Cách nén nhanh bằng PowerShell (Nếu máy có WinRAR):
```powershell
& "C:\Program Files\WinRAR\WinRAR.exe" a -afzip "23630851_de2.zip" ChatServer.java ChatClient.java Dockerfile docker-compose.yml entrypoint.sh chatroom.log
```
Hoặc dùng lệnh nén Zip có sẵn của Windows:
```powershell
Compress-Archive -Path ChatServer.java, ChatClient.java, Dockerfile, docker-compose.yml, entrypoint.sh, chatroom.log, HUONG_DAN_NOP_BAI.md -DestinationPath 23630851_de2.zip -Force
```

---

### BƯỚC 3: Nộp lên hệ thống LMS
1. Truy cập vào mục Nộp bài Thường kỳ 1 - Đề 2 trên LMS.
2. Tải lên file **`23630851_de2.rar`** (hoặc `.zip`).
3. Trong phần ghi chú/nội dung nộp bài (nếu có), dán kèm link Docker Image:
   ```
   Docker Image: shima594/de2:23630851
   Lệnh kéo image: docker pull shima594/de2:23630851
   ```
