# TUAN4 – Thread (5 bài tăng dần độ khó)

## Cấu trúc thư mục

```
tuan4/
├── bai1/   ← Thread cơ bản: extends Thread
├── bai2/   ← Thread ghi file: extends Thread vs implements Runnable
├── bai3/   ← Thread đọc file: extends Thread vs implements Runnable
├── bai4/   ← Thread synchronized: ghi/đọc file dùng wait/notifyAll
└── bai5/   ← Thread Producer-Consumer: Kho + NguoiSanXuat + NguoiTieuDung
```

---

## bai1/ – Thread Cơ Bản (extends Thread)

| File | Vai trò |
|------|---------|
| `ThreadSimple.java` | Thread đơn giản nhất: override `run()`, gọi `start()` |
| `MyThread.java` | Thread có tên + số lần lặp, tạo 4 thread chạy song song |

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\tuan4\bai1"
javac -encoding UTF-8 *.java
java bai1.ThreadSimple    # 1 thread đơn giản
java bai1.MyThread        # 4 thread chạy song song (n=1000 lần)
```

---

## bai2/ – Thread Ghi File

| File | Vai trò |
|------|---------|
| `FileTWrite.java` | Ghi 10 số random vào file. **C1** (comment): `extends Thread`. **C2** (đang chạy): `implements Runnable` |
| `Main.java` | Tạo 3 thread, mỗi thread ghi 1 file (file11.txt, file22.txt, file33.txt) |

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\tuan4\bai2"
javac -encoding UTF-8 *.java
java bai2.Main
# Kết quả: tạo ra 3 file txt trong thư mục hiện tại
```

---

## bai3/ – Thread Đọc File

| File | Vai trò |
|------|---------|
| `FileTReader.java` | Đọc file bằng `BufferedReader`. **C1** (comment): `extends Thread`. **C2** (đang chạy): `implements Runnable` |
| `Main.java` | Tạo 3 thread, mỗi thread đọc 1 file (file11.txt, file22.txt, file33.txt) |

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\tuan4\bai3"
javac -encoding UTF-8 *.java
java bai3.Main
# LƯU Ý: cần có sẵn các file file11.txt, file22.txt, file33.txt (chạy bai2 trước)
```

---

## bai4/ – Thread Synchronized (ghi/đọc file luân phiên)

| File | Vai trò |
|------|---------|
| `FileBuffer.java` | **Trung gian** – dùng `synchronized` + `wait()` + `notifyAll()` đảm bảo ghi xong mới đọc |
| `FileWriterThread.java` | Thread ghi 10 dòng random vào file qua `FileBuffer` |
| `FileReaderThread.java` | Thread đọc từng dòng mới từ file qua `FileBuffer` |
| `Main.java` | Tạo 1 buffer, 1 writer, 1 reader → chạy đồng thời |

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\tuan4\bai4"
javac -encoding UTF-8 *.java
java bai4.Main
# Kết quả: Writer ghi 1 dòng → Reader đọc dòng đó → lặp 10 lần
```

> **Từ khóa quan trọng**: `synchronized` (khóa method), `wait()` (nhả lock + chờ), `notifyAll()` (đánh thức tất cả thread đang chờ)

---

## bai5/ – Producer-Consumer (Kho hàng)

| File | Vai trò |
|------|---------|
| `Kho.java` | **Kho chung** – dùng `synchronized` + `wait/notifyAll`; có `nhapKho()` và `xuatKho()` |
| `NguoiSanXuat.java` | Thread nhập kho ngẫu nhiên 1-5 sản phẩm, nghỉ 500-1500ms |
| `NguoiTieuDung.java` | Thread xuất kho ngẫu nhiên, nghỉ ngẫu nhiên |
| `Demo.java` | **Chạy chính** – tạo 1 kho (sức chứa 10), 2 NSX, 2 NTD |

```bash
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\tuan4\bai5"
javac -encoding UTF-8 *.java
java bai5.Demo
# Ctrl+C để dừng (chạy vô tận)
```

> **Luồng hoạt động**: NSX nhập kho → nếu đầy thì `wait()` → NTD xuất xong `notifyAll()` → NSX tiếp tục

---

## Tóm Tắt Kiến Thức Thread qua 5 Bài

| Bài | Kỹ thuật | Từ khóa |
|-----|----------|---------|
| bai1 | Thread cơ bản | `extends Thread`, `run()`, `start()` |
| bai2 | Ghi file đa luồng | `implements Runnable`, `new Thread(obj)` |
| bai3 | Đọc file đa luồng | `BufferedReader`, `readLine()` |
| bai4 | Đồng bộ ghi/đọc | `synchronized`, `wait()`, `notifyAll()` |
| bai5 | Producer-Consumer | `synchronized`, `wait()`, `notifyAll()` |
