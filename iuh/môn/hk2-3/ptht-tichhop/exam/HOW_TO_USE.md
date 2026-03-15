# 📋 exam/ – 3 FILE ĐI THI

## Thư mục: `ptht-tichhop/exam/`

```
exam/
├── Server.java      ← chạy TRƯỚC
├── Handler.java     ← thread xử lý mỗi client
└── Client.java      ← chạy SAU
```

---

## ⚡ QUY TRÌNH KHI THI (5 BƯỚC)

```
1. Đọc đề  →  xác định loại stream cần dùng (xem bảng dưới)
2. Server.java: uncomment đúng [SERVER-?]
3. Handler.java: uncomment đúng [STREAM-?] + uncomment [XU-LY-?]
4. Client.java: uncomment đúng [CLIENT-?]  (phải KHỚP stream với Handler)
5. Run Server → Run Client
```

---

## 🗺️ BẢNG CHỌN NHANH THEO ĐỀ

| Loại đề bài | Server | Handler | Client |
|-------------|--------|---------|--------|
| TCP nhiều client (hầu hết) | `SERVER-1` | `STREAM-A` hoặc `B` | `CLIENT-A` hoặc `D` |
| TCP 1 client | `SERVER-2` | `STREAM-A` | `CLIENT-A` |
| UDP | `SERVER-3` | `xuLyUDP()` | `CLIENT-E` |
| Truyền **String** (uppercase/lowercase/đếm ký tự) | `SERVER-1` | `STREAM-A` + `XU-LY-1/2/3` | `CLIENT-A` |
| Truyền **String text dòng** (chat, echo) | `SERVER-1` | `STREAM-B` + `XU-LY-7` | `CLIENT-D` |
| Truyền **int menu** (Time/Date) | `SERVER-1` | `STREAM-A` + `xuLyMenu()` | `CLIENT-B` |
| Truyền **2 int** (tính toán dãy số) | `SERVER-1` | `STREAM-A` + `tinhToan()` | `CLIENT-C` |
| Chat realtime (nhận bất kỳ lúc) | `SERVER-1` | `STREAM-A` + `XU-LY-7` | `CLIENT-F` |
| Kế thừa OOP + TCP | `SERVER-1` | `STREAM-A` + OOP class bên dưới | `CLIENT-A` |
| Producer-Consumer + TCP | `SERVER-1` | `STREAM-A` + SharedKho class | `CLIENT-A` |

---

## 📌 XU-LY TRONG Handler.java – CHỌN THEO ĐỀ

| Variant | Dùng khi |
|---------|----------|
| `XU-LY-1` | Chuyển chữ HOA |
| `XU-LY-2` | Chuyển chữ thường |
| `XU-LY-3` | Đếm số ký tự |
| `XU-LY-4` | Kiểm tra chẵn/lẻ |
| `XU-LY-5` | Tổng các số trong chuỗi |
| `XU-LY-6` | Đọc số 0-9 tiếng Việt |
| `XU-LY-7` | Echo lại (chat cơ bản) |
| `xuLyMenu()` | Đề có menu int (1/2/3/0) |
| `tinhToan()` | Đề tính toán dãy số |
| `xuLyUDP()` | Đề UDP |

---

## 🔧 HAY PHẢI SỬA

| Chỗ cần sửa | Vị trí |
|-------------|--------|
| PORT | `Server.java` dòng đầu + `Client.java` dòng đầu (phải trùng nhau) |
| HOST | `Client.java` dòng đầu (`127.0.0.1` = cùng máy) |
| Logic xử lý | `Handler.java` hàm `xuLy()` hoặc `xuLyMenu()` |
| OOP class | `Handler.java` phần dưới cùng |

---

## ❗ LỖI HAY GẶP

| Lỗi | Nguyên nhân | Fix |
|-----|-------------|-----|
| `Connection refused` | Server chưa chạy | Run Server trước |
| `Address already in use` | Port bị chiếm | Đổi PORT hoặc tắt Eclipse rồi restart |
| Client treo không nhận | Thiếu `out.flush()` | Thêm sau mỗi lần ghi |
| `NumberFormatException` | Parse sai | Kiểm tra `.trim()`, bọc try/catch |
| 2 class trong 1 file | Handler dùng inner class | Dùng `static class` bên trong Handler |
