# Bài Tập 4: Mô Hình Message Broker (Hệ Thống Phân Tán)

## 📌 Tổng Quan 3 Bài Kiểm Tra

---

### 1. Kiểm tra 1.1: Consumer đang chạy (Real-time Message Dispatch)
* **Ý nghĩa**: Cả bên gửi (`Customer`) và bên nhận (`OrderService`) đều đang online.
* Khi `Customer` gửi đơn, Broker chuyển tiếp ngay cho `OrderService` xử lý và hoàn tất ngay:
  ```text
  [Customer] Sending ORDER-001
  [Broker] Message received ORDER-001
  [OrderService] Received ORDER-001
  [OrderService] Completed ORDER-001
  ```

---

### 2. Kiểm tra 1.2: Consumer chưa chạy (Time-Uncoupled / Message Queue)
* **Ý nghĩa**: Tính chất độc lập thời gian của hàng đợi thông điệp.
* `Customer` gửi `ORDER-001`, `ORDER-002`, `ORDER-003` vào `MessageBroker` khi `OrderService` **chưa bật**.
* Broker lưu trữ vào hàng đợi (Queue). Khi `OrderService` khởi động lên, Broker tự động chuyển tiếp toàn bộ đơn hàng tồn đọng:
  ```text
  [OrderService] Received ORDER-001
  [OrderService] Received ORDER-002
  [OrderService] Received ORDER-003
  ```

---

### 3. Kiểm tra 3: Nhiều người tiêu dùng (Competing Consumers / Load Balancing)
* **Ý nghĩa**: Mô hình hàng đợi cạnh tranh (Competing Consumers). Khi có nhiều worker/service (`Service-1`, `Service-2`) cùng lắng nghe một hàng đợi, Broker sẽ chia tải theo cơ chế **Round-Robin** để mỗi đơn hàng chỉ được xử lý bởi **MỘT** Service duy nhất (không bị xử lý trùng lặp):
  ```text
  ORDER-001 → Service-1
  ORDER-002 → Service-2
  ORDER-003 → Service-1
  ORDER-004 → Service-2
  ```

---

## 🚀 Hướng Dẫn Chạy Trên Terminal (PowerShell / CMD)

```powershell
cd "d:\folder\rac\iuh\môn\hk1-4\ptht-phantan\LT\bt\b4\1"
javac *.java
```

* **Chạy toàn bộ 3 bài kiểm tra:**
  ```powershell
  java Main
  ```

* **Hoặc chạy riêng từng bài kiểm tra:**
  * Kiểm tra 1.1: `java Test1_1`
  * Kiểm tra 1.2: `java Test1_2`
  * Kiểm tra 3: `java Test3`
