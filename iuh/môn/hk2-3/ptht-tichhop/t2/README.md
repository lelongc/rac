# T2 – OOP (Lập Trình Hướng Đối Tượng)

## Cấu trúc thư mục

```
t2/
├── tuan2/     ← OOP + Scanner (nhập từng dòng đơn giản)
└── tuan2b/    ← OOP + BufferedReader/PrintWriter (cách cô dạy dùng Stream)
```

---

## tuan2/ – Nhân Viên (dùng Scanner)

| File | Vai trò |
|------|---------|
| `NhanVien.java` | Lớp cha – `maNV`, `hoTen`, `nhapThongTin()`, `hienThiThongTin()` |
| `NhanVienVanPhong.java` | Lớp con – thêm `luongCoBan`, method `nhapThongTinVP()`, `tinhLuong()` |
| `NhanVienSanXuat.java` | Lớp con – thêm `soSanPham` + `donGia`, method `nhapThongTinSX()`, `tinhLuong()` |
| `Main.java` | **Chạy chính** – tạo 2 nhân viên, nhập, in kết quả |

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\t2\tuan2"
javac -encoding UTF-8 *.java
java tuan2.Main
```

---

## tuan2b/ – Phương Tiện (dùng BufferedReader + PrintWriter)

| File | Vai trò |
|------|---------|
| `PhuongTien.java` | Lớp cha – `hangSanXuat`, `namSanXuat`, `giaBan`; nhập qua `BufferedReader` |
| `XeMay.java` | Lớp con – thêm `dungTichXiLanh`, `tinhThue()` = giaBan × 5% |
| `Oto.java` | Lớp con – thêm `soGhe`, `tinhThue()` = giaBan × 10% |
| `Main.java` | **Chạy chính** – tạo XeMay và Oto hardcode, in thông tin + thuế |

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\t2\tuan2b"
javac -encoding UTF-8 *.java
java tuan2b.Main
```

> **Khác biệt tuan2 vs tuan2b**: tuan2 dùng `Scanner`, tuan2b dùng `BufferedReader` + `PrintWriter` (chuẩn Stream hơn)
