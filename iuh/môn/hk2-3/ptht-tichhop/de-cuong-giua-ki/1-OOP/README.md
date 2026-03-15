# CHỦ ĐỀ 1: OOP

## Các file trong thư mục này

| File | Vai trò |
|------|---------|
| `NhanVien.java` | **Lớp cha (abstract)** – khai báo `maNV`, `hoTen`, method `nhapThongTin()`, `hienThiThongTin()`, và abstract `tinhLuong()` |
| `NhanVienVanPhong.java` | **Lớp con** – kế thừa NhanVien, thêm `luongCoBan`, override `tinhLuong()` |
| `NhanVienSanXuat.java` | **Lớp con** – kế thừa NhanVien, thêm `soSanPham` + `donGia`, override `tinhLuong()` |
| `Main.java` | **Chạy chính** – tạo đối tượng, nhập thông tin, in kết quả |

---

## Cách chạy bằng terminal

```bash
# Bước 1: vào đúng thư mục chứa các file .java
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\de-cuong-giua-ki\1-OOP"

# Bước 2: biên dịch tất cả file cùng lúc
javac -encoding UTF-8 *.java

# Bước 3: chạy (tên class có main, kèm package nếu có)
java oop.Main
```

> Nếu lỗi package, xóa dòng `package oop;` trong từng file rồi chạy lại: `java Main`

---

## Luồng hoạt động

```
Main.java
  → tạo NhanVienVanPhong → nhapThongTinVP() → tinhLuong()
  → tạo NhanVienSanXuat  → nhapThongTinSX() → tinhLuong()
  → in kết quả cả 2
```
