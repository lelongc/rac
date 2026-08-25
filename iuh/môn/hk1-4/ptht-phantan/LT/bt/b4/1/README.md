# Bài Tập 4: Mô Hình Message Broker (Time-Coupled & Time-Uncoupled)

## 📌 Ý Nghĩa Của Đề Bài (Giải thích dễ hiểu)

Đề bài nhằm kiểm tra 2 tính chất cốt lõi của **Message Broker / Message Queue** trong Hệ Thống Phân Tán (Chương 4: Indirect Communication):

---

### 1. Kiểm tra 1.1: Consumer đang chạy (Xử lý trực tiếp thời gian thực)
* **Ý nghĩa**: Cả bên gửi (**Customer**) và bên nhận (**OrderService**) đều đang hoạt động cùng lúc.
* Khi Customer gửi `ORDER-001` tới `MessageBroker`, Broker chuyển tiếp ngay cho `OrderService` xử lý và hoàn tất ngay lập tức:
  ```text
  [Customer] Sending ORDER-001
  [Broker] Message received ORDER-001
  [OrderService] Received ORDER-001
  [OrderService] Completed ORDER-001

  [Customer] Sending ORDER-002
  ...
  ```

---

### 2. Kiểm tra 1.2: Consumer chưa chạy (Đặc tính Time-Uncoupled / Độc lập thời gian)
* **Ý nghĩa**: Đây là ưu điểm lớn nhất của Message Queue! Bên gửi và bên nhận **không cần phải chạy cùng một thời điểm**.
* **Kịch bản**:
  1. `OrderService` (Consumer) đang **tắt/chưa chạy**.
  2. Customer gửi liên tiếp `ORDER-001`, `ORDER-002`, `ORDER-003` vào `MessageBroker`.
  3. Broker lưu các message này an toàn trong **Hàng đợi (Queue)**.
  4. Sau đó, khi `OrderService` **khởi động lên**, Broker lập tức lấy toàn bộ message đang đợi trong hàng đợi ra gửi cho `OrderService` xử lý:
  ```text
  [OrderService] Received ORDER-001
  [OrderService] Received ORDER-002
  [OrderService] Received ORDER-003
  ```

---

## 🚀 Cách chạy trên Terminal (PowerShell / CMD)

### Bước 1: Di chuyển vào thư mục bài tập
```powershell
cd "d:\folder\rac\iuh\môn\hk1-4\ptht-phantan\LT\bt\b4\1"
```

### Bước 2: Biên dịch các file Java
```powershell
javac *.java
```

### Bước 3: Chạy chương trình

* **Chạy kiểm tra tổng hợp (cả 1.1 và 1.2):**
  ```powershell
  java Main
  ```

* **Hoặc chạy riêng từng bài kiểm tra:**
  * Kiểm tra 1.1: `java Test1_1`
  * Kiểm tra 1.2: `java Test1_2`
