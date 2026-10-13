# HƯỚNG DẪN DEMO VÀ NỘP BÀI KIỂM TRA THƯỜNG KỲ 2 (ĐỀ 2)
### MÔN: PHÁT TRIỂN HỆ THỐNG PHÂN TÁN - IUH

* **Sinh viên:** Lê Thành Long
* **Mã số sinh viên (MSSV):** `23630851`
* **Docker Hub Repository:** `shima594/c2:23630851`
* **File báo cáo PDF:** `LeThanhLong_c2de2.pdf` (hoặc `Hoten_c2de2.pdf`)

---

## 📌 1. THÔNG TIN BÀI NỘP

1. **Docker Hub Image:**
   - Image Name: `shima594/c2:23630851` (Đã push lên Docker Hub thành công)
   - Lệnh kéo image: `docker pull shima594/c2:23630851`

2. **Lệnh chạy Docker Run theo yêu cầu gửi form:**
   ```bash
   docker run -d -p 8080:8080 --name product-service shima594/c2:23630851
   ```

3. **Link nộp bài trên Google Form (theo đề bài):**
   - [Link Google Form nộp bài](https://docs.google.com/forms/d/e/1FAIpQLSf467dObsmXAgSmVKU19GLkZifEqTPmecIXKud73grRy-SHDA/viewform?usp=publish-editor)

4. **File PDF nộp báo cáo kết quả cURL:**
   - File: `LeThanhLong_c2de2.pdf` (nằm sẵn trong thư mục `TK2`)
   - Mỗi hình chụp trong PDF đều có chứa đầy đủ Họ tên `Lê Thành Long` và MSSV `23630851`.

---

## 🚀 2. CÁC BƯỚC TỰ DEMO LẠI TRÊN TERMINAL (POWERSHELL / CMD)

Mở Terminal (PowerShell) tại thư mục `TK2`:

### Bước 1: Khởi động service bằng Docker container
```powershell
docker run -d -p 8080:8080 --name product-service shima594/c2:23630851
```

### Bước 2: Kiểm tra container đang chạy
```powershell
docker ps
```

### Bước 3: Lấy danh sách sản phẩm ban đầu (GET)
```powershell
curl.exe -s http://localhost:8080/api/products
```

### Bước 4: Thêm sản phẩm mới (POST)
```powershell
'{"name": "Tai nghe Sony WH-1000XM5", "price": 8490000.0}' | curl.exe -s -X POST http://localhost:8080/api/products -H "Content-Type: application/json" -d '@-'
```
*(Nếu chạy trong Command Prompt (CMD) thông thường):*
```cmd
curl -s -X POST http://localhost:8080/api/products -H "Content-Type: application/json" -d "{\"name\": \"Tai nghe Sony WH-1000XM5\", \"price\": 8490000.0}"
```

### Bước 5: Kiểm tra lại danh sách để thấy sản phẩm vừa thêm (GET)
```powershell
curl.exe -s http://localhost:8080/api/products
```

### Bước 6: Xóa sản phẩm theo ID = 1 (DELETE)
```powershell
curl.exe -s -X DELETE http://localhost:8080/api/products/1
```

### Bước 7: Kiểm tra lại danh sách xác nhận ID = 1 đã bị xóa (GET)
```powershell
curl.exe -s http://localhost:8080/api/products
```

### Bước 8: Dọn dẹp sau khi demo xong
```powershell
docker stop product-service
docker rm product-service
```
