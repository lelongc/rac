# HƯỚNG DẪN KIỂM THỬ RESTFUL API (CRUD 4 PHƯƠNG THỨC: GET, POST, PUT, DELETE) BẰNG POSTMAN & MOCKAPI.IO

Tài liệu này hướng dẫn chi tiết từ A-Z cách sử dụng phần mềm **Postman** và trang web **MockAPI.io** để test Web Service RESTful API.

---

## 🚀 CÁCH KHỞI ĐỘNG REST API SERVER TRÊN ECLIPSE:

1. Import dự án **`b3_rest_crud`** vào Eclipse.
2. Mở file `src/api/ServerB3.java` ➔ nhấp chuột phải chọn **Run As ➔ Java Application**.
3. Server sẽ lắng nghe tại địa chỉ Endpoint: **`http://localhost:8083/api/products`**

---

## 📮 PHẦN 1: HƯỚNG DẪN TEST API TRÊN PHẦN MỀM POSTMAN

### **1. Test Phương Thức `GET` (Lấy danh sách tất cả sản phẩm)**
- **HTTP Method**: Chọn `GET`
- **URL**: `http://localhost:8083/api/products`
- **Bấm nút**: `Send`
- **Kết quả trả về**: Mã `200 OK` kèm mảng JSON chứa tất cả sản phẩm.

### **2. Test Phương Thức `GET` (Tìm sản phẩm theo ID)**
- **HTTP Method**: Chọn `GET`
- **URL**: `http://localhost:8083/api/products?id=SP01`
- **Bấm nút**: `Send`
- **Kết quả**: Trả về 1 đối tượng JSON duy nhất của sản phẩm `SP01`.

### **3. Test Phương Thức `POST` (Thêm mới 1 sản phẩm)**
- **HTTP Method**: Chọn `POST`
- **URL**: `http://localhost:8083/api/products`
- **Chuyển sang thẻ Body**:
  - Chọn `x-www-form-urlencoded` (hoặc `raw` kiểu `JSON`).
  - Điền các cặp KEY - VALUE:
    * `id`: `SP05`
    * `name`: `Chuột không dây MX Master 3S`
    * `price`: `2600000`
    * `quantity`: `15`
    * `category`: `Phụ kiện`
- **Bấm nút**: `Send`
- **Kết quả**: Trả về `{"status":"success","message":"Them san pham thanh cong",...}`.

### **4. Test Phương Thức `PUT` (Cập nhật thông tin sản phẩm)**
- **HTTP Method**: Chọn `PUT`
- **URL**: `http://localhost:8083/api/products?id=SP05&name=Chuot MX Master 3S Pro&price=2800000&quantity=20&category=Phu kien`
- **Bấm nút**: `Send`
- **Kết quả**: Trả về `{"status":"success","message":"Cap nhat san pham thanh cong",...}`.

### **5. Test Phương Thức `DELETE` (Xóa sản phẩm theo ID)**
- **HTTP Method**: Chọn `DELETE`
- **URL**: `http://localhost:8083/api/products?id=SP05`
- **Bấm nút**: `Send`
- **Kết quả**: Trả về `{"status":"success","message":"Xoa san pham thanh cong ID=SP05"}`.

---

## 🌐 PHẦN 2: HƯỚNG DẪN TẠO VÀ TEST MOCK API TRÊN MOCKAPI.IO

Khi làm bài tập lớn hoặc đi thi không có sẵn Server backend Java, bạn có thể tạo Fake Server cực kỳ nhanh bằng **MockAPI.io**:

### **Các bước tạo Fake REST API trên MockAPI.io**:
1. Truy cập trang web: [https://mockapi.io](https://mockapi.io) và đăng nhập bằng Google/Github.
2. Bấm nút **New Project** ➔ Nhập tên Project (VD: `ProductAPI`) ➔ Bấm **Create**.
3. Bấm nút **New Resource**:
   - Resource name: `products`
   - Khai báo Schema các trường dữ liệu:
     * `id`: (autoincrement)
     * `name`: (string)
     * `price`: (number)
     * `quantity`: (number)
     * `category`: (string)
   - Bấm **Create**.
4. Bạn sẽ nhận được 1 đường dẫn Endpoint giả định có dạng:
   `https://66bb123456.mockapi.io/api/v1/products`

### **Sử dụng đường dẫn MockAPI trong ứng dụng Web Client**:
Trong file JavaScript Client (`app.js`), chỉ cần thay đổi đường dẫn `API_BASE`:
```javascript
// Thay vì http://localhost:8083/api/products
const API_BASE = "https://66bb123456.mockapi.io/api/v1/products";
```
MockAPI.io hỗ trợ tự động toàn bộ 4 HTTP Verbs (`GET`, `POST`, `PUT`, `DELETE`) chuẩn RESTful!
