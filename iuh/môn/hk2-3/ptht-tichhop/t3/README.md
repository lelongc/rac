# T3 – Stream (InputStream, BufferedReader, PrintWriter) + OOP

## Cấu trúc thư mục

```
t3/
├── eg/       ← Ví dụ Stream cơ bản (InputStream, BufferedReader, PrintWriter)
├── tuan1/    ← Bài tập Stream đầy đủ (BufferedReader + PrintWriter)
├── tuan2/    ← OOP NhanVien dùng BufferedReader (có try-catch)
└── tuan2b/   ← OOP PhuongTien dùng BufferedReader (có try-catch)
```

---

## eg/ – Ví dụ Stream Cơ Bản

| File | Nội dung | Chạy |
|------|----------|------|
| `ex1.java` | **InputStream** đọc từng byte từ bàn phím, in `(char)ch`, gõ `q` để thoát | `java eg.ex1` |
| `ex2.java` | **InputStream** đọc block byte (`is.available()` + `read(byte[])`), chờ nếu chưa có data | `java eg.ex2` |
| `ex3.java` | **BufferedReader** = `InputStreamReader(System.in)` → `readLine()`, gõ `exit` để thoát | `java eg.ex3` |
| `ex4.java` | **PrintWriter** – demo `write()`, `println()`, `flush()`, `close()` | `java eg.ex4` |

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\t3\eg"
javac -encoding UTF-8 *.java
java eg.ex1     # hoặc ex2, ex3, ex4
```

---

## tuan1/ – Bài Tập Stream Tổng Hợp (5 bài liên tiếp)

| File | Nội dung |
|------|----------|
| `ex1.java` | **5 bài gộp**: in chuỗi, nhập tên, tính tổng A+B, kiểm tra chẵn/lẻ, tên tháng tiếng Anh |
| `ex2.java` | Nhập tên bằng `Scanner.nextLine()` |
| `ex3.java` | Nhập 2 số nguyên A, B → tính tổng |
| `ex4.java` | Nhập số → kiểm tra chẵn/lẻ |
| `ex5.java` | Nhập tháng (1-12) → in tên tiếng Anh |

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\t3\tuan1"
javac -encoding UTF-8 *.java
java tuan1.ex1   # chạy tất cả 5 bài cùng lúc (file ex1 gộp hết)
java tuan1.ex2   # hoặc chạy từng bài riêng
```

> **Lưu ý**: `ex1.java` dùng `BufferedReader + PrintWriter`. Các file ex2-ex5 dùng `Scanner`

---

## tuan2/ – OOP NhanVien + Stream (BufferedReader + PrintWriter)

| File | Vai trò |
|------|---------|
| `NhanVien.java` | Lớp cha – nhập `maNV`, `hoTen` qua `BufferedReader`, in qua `PrintWriter` |
| `NhanVienVanPhong.java` | Lớp con – thêm `luongCoBan`, `tinhLuong()` |
| `NhanVienSanXuat.java` | Lớp con – thêm `soSanPham` + `donGia`, `tinhLuong()` |
| `Main.java` | **Chạy chính** – tạo BR + PW, truyền vào các method nhập/hiển thị |

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\t3\tuan2"
javac -encoding UTF-8 *.java
java tuan2.Main
```

---

## tuan2b/ – OOP PhuongTien + Stream (BufferedReader + PrintWriter)

| File | Vai trò |
|------|---------|
| `PhuongTien.java` | Lớp cha – `hangSanXuat`, `namSanXuat`, `giaBan`; nhập/in qua Stream |
| `XeMay.java` | Lớp con – thêm `dungTichXiLanh`, `tinhThue()` = giaBan × 5% |
| `Oto.java` | Lớp con – thêm `soGhe`, `tinhThue()` = giaBan × 10% |
| `Main.java` | **Chạy chính** – tạo BR + PW, nhập 1 XeMay + 1 Oto, in kết quả |

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\t3\tuan2b"
javac -encoding UTF-8 *.java
java tuan2b.Main
```

---

## Chuỗi Stream cần nhớ

```
System.in (InputStream, byte)
    └─→ InputStreamReader   (byte → char)
            └─→ BufferedReader  (buffer + readLine())

System.out (OutputStream, byte)
    └─→ PrintWriter  (println / flush / close)
```
