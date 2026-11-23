# BẢNG TRA CỨU NHANH PHÒNG THI CUỐI KỲ (CHEAT SHEET CK)
**Môn: Phát triển hệ thống phân tán (Distributed Systems - IUH)**  
**Họ tên SV: Lê Thành Long | MSSV: 23630851 | DockerHub: shima594**

---

## ⚡ PHẦN 1: TÓM TẮT LÝ THUYẾT TRẢ LỜI NHANH (1 PHÚT)

### 1. Hệ thống phân tán
* **Định nghĩa**: Tập hợp các máy tính độc lập liên kết mạng, giao tiếp và phối hợp hành động **chỉ bằng truyền thông điệp**, xuất hiện trước người dùng như **một hệ thống đơn nhất**.
* **3 Đặc trưng cốt lõi**:
  1. *Tính đồng thời (Concurrency)*: Các tiến trình chạy song song, chia sẻ tài nguyên.
  2. *Lỗi độc lập (Independent Failures)*: Một máy sập không làm hỏng cả hệ thống.
  3. *Không có đồng hồ toàn cục (Lack of a Global Clock)*: Không có thời gian chuẩn tuyệt đối duy nhất.
* **8 Dạng trong suốt (Transparencies)**:
  - **Access**: Truy cập cục bộ hay từ xa đều dùng cùng thao tác.
  - **Location**: Che giấu vị trí vật lý (dùng URL/định danh thay vì IP).
  - **Concurrency**: Nhiều người dùng đồng thời không làm sai lệch dữ liệu.
  - **Replication**: Che giấu việc nhân bản dữ liệu ra nhiều server.
  - **Failure**: Che giấu lỗi phần cứng/mạng, tự phục hồi hoặc chuyển hướng.
  - **Mobility (Migration)**: Tài nguyên/client di chuyển mà không gián đoạn kết nối.
  - **Performance**: Tự tái cấu trúc/cân bằng tải khi lưu lượng biến động.
  - **Scaling**: Mở rộng quy mô người dùng/thiết bị mà không đổi cấu trúc thuật toán.
* **8 Sai lầm (Fallacies)**: (1) Mạng tin cậy; (2) Độ trễ = 0; (3) Băng thông vô hạn; (4) Mạng an toàn; (5) Topo cố định; (6) 1 người quản trị; (7) Chi phí vận chuyển = 0; (8) Mạng đồng nhất.

### 2. Web Service & RESTful
* **Kiến trúc SOA 3 vai trò**: Service Provider (Cung cấp & Publish) -> Service Registry (Lưu danh bạ) -> Service Requester (Tìm Find & Gọi Bind).
* **SOAP vs RESTful**:
  - *RESTful*: Là kiểu kiến trúc (Style), dùng **JSON** (nhẹ, nhanh), chạy trên HTTP, dễ học, dùng cho Web/Mobile API.
  - *SOAP*: Là giao thức (Protocol), chỉ dùng **XML** (nặng, phức tạp), độc lập giao thức, có WSDL & WS-Security, dùng cho Ngân hàng/Enterprise.
* **6 Ràng buộc REST**: (1) Client-Server; (2) Stateless (Phi trạng thái, không lưu session); (3) Cacheable (Có thể cache); (4) Uniform Interface (Giao diện chuẩn URI + JSON); (5) Layered System (Đa tầng); (6) Code on Demand.
* **Quy tắc HTTP Method & Status Code**:
  - `GET /api/items`: Lấy danh sách (200 OK) - *Safe, Idempotent*
  - `GET /api/items/{id}`: Xem chi tiết (200 OK hoặc 404 Not Found) - *Safe, Idempotent*
  - `POST /api/items`: Tạo mới (201 Created) - *Non-idempotent*
  - `PUT /api/items/{id}`: Sửa toàn bộ (200 OK) - *Idempotent*
  - `DELETE /api/items/{id}`: Xóa (200 OK hoặc 204 No Content) - *Idempotent*

---

## 🚀 PHẦN 2: QUY TRÌNH 5 BƯỚC THỰC HÀNH THI TRÊN MÁY (15 PHÚT HOÀN THÀNH)

### Bước 1: Build mã nguồn ra file JAR
Mở terminal tại thư mục dự án (`rest-api-template`):
```powershell
.\mvnw.cmd clean package -DskipTests
```
*(File JAR xuất ra tại: `target/rest-service-0.0.1-SNAPSHOT.jar`)*

---

### Bước 2: Build Docker Image
Định dạng tên image theo đúng quy ước đề thi: `Username/c2:MaSV`
```powershell
docker build -t shima594/c2:23630851 .
```

---

### Bước 3: Chạy Container trên cổng 8080
```powershell
docker run -d -p 8080:8080 --name product-service shima594/c2:23630851
```
Kiểm tra trạng thái:
```powershell
docker ps
```

---

### Bước 4: Test cURL trên PowerShell & Chụp màn hình nộp bài
> **MẸO VÀNG POWERSHELL**: Khi gửi JSON bằng `curl.exe` trên PowerShell, **LUÔN DÙNG CÚ PHÁP PIPELINE `'{...}' | curl.exe ... -d @-`** để không bao giờ bị lỗi mất ngoặc kép (400 Bad Request)!

#### 1. Test GET (Lấy tất cả):
```powershell
curl.exe -s -X GET http://localhost:8080/api/items
```
*(Code mẫu đã hỗ trợ cả các route: `/api/products`, `/api/students`, `/items`, `/products`)*

#### 2. Test GET by ID (Lấy sản phẩm ID=1):
```powershell
curl.exe -s -X GET http://localhost:8080/api/items/1
```

#### 3. Test POST (Thêm mới sản phẩm):
```powershell
'{"name":"MacBook Air M2","code":"APL-M2","price":24500000.0,"category":"Laptop","quantity":8}' | curl.exe -s -X POST http://localhost:8080/api/items -H "Content-Type: application/json" -d @-
```

#### 4. Test PUT (Cập nhật sản phẩm ID=1):
```powershell
'{"name":"Laptop Dell XPS 15 2024","price":28000000.0}' | curl.exe -s -X PUT http://localhost:8080/api/items/1 -H "Content-Type: application/json" -d @-
```

#### 5. Test DELETE (Xóa sản phẩm ID=2):
```powershell
curl.exe -s -X DELETE http://localhost:8080/api/items/2
```

---

### Bước 5: Nộp bài theo yêu cầu
1. **Lệnh gửi vào Chat Zoom / Google Form**:
   ```text
   docker run -d -p 8080:8080 --name product-service shima594/c2:23630851
   ```
2. **Đẩy image lên Docker Hub (nếu đề yêu cầu)**:
   ```powershell
   docker push shima594/c2:23630851
   ```
3. **Ảnh chụp nộp bài PDF**:
   - Chụp rõ cửa sổ Terminal gồm: Dòng lệnh curl + Kết quả JSON trả về + Nhãn Họ tên SV & MSSV: `Lê Thành Long - 23630851`.

---

## 🛠️ PHẦN 3: KỸ THUẬT LÁCH & TÙY BIẾN ĐỀ BÀI TRONG 30 GIÂY

Dự án mẫu `rest-api-template` đã được thiết kế sẵn để **đáp ứng 100% mọi đề thi**:
1. **Nếu đề yêu cầu quản lý Product (Sản phẩm)**:
   - Các trường có sẵn: `id`, `name`, `price`, `quantity`, `category`.
   - Các endpoint hoạt động ngay: `/api/products`, `/products`.
2. **Nếu đề yêu cầu quản lý Student (Sinh viên)**:
   - Các trường map tương ứng: `id` (Mã SV), `name` (Họ tên), `code` (Lớp/Khoa), `price` (Điểm số), `category` (Ngành học).
   - Các endpoint hoạt động ngay: `/api/students`, `/students`.
3. **Nếu đề bài yêu cầu thêm chức năng Tìm kiếm (Search) hoặc Lọc (Filter)**:
   - Đã tích hợp sẵn:
     * `GET http://localhost:8080/api/items/search?keyword=dell`
     * `GET http://localhost:8080/api/items/filter?minPrice=1000000&maxPrice=25000000`
4. **Nếu đề cho đoạn code khuyết và hỏi "Cần bổ sung gì?"**:
   - Mở ngay file `2_LY_THUYET_WEB_SERVICE_REST.md` Mục VI, chép nguyên văn danh sách các Annotation `@RestController`, `@RequestMapping`, `@GetMapping`, `@PostMapping`, `@RequestBody`, `@PathVariable` và cấu hình `pom.xml`.
