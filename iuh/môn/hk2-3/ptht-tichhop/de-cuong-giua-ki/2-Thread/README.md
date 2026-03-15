# CHỦ ĐỀ 2: THREAD

## Các file trong thư mục này

| File | Vai trò | Cách chạy |
|------|---------|-----------|
| `C1_ExtendsThread.java` | **Cách 1**: kế thừa `Thread`, override `run()`, gọi `start()` | `java thread.C1_ExtendsThread` |
| `C2_ImplementsRunnable.java` | **Cách 2**: implements `Runnable`, truyền vào `new Thread(obj)` | `java thread.C2_ImplementsRunnable` |
| `C3_ThreadSleepJoin.java` | **Nâng cao**: dùng `Thread.sleep(ms)` và `join()` | `java thread.C3_ThreadSleepJoin` |

---

## Cách chạy bằng terminal

```bash
# Bước 1: vào thư mục
cd "d:\folder\rac\iuh\môn\hk2-3\ptht-tichhop\de-cuong-giua-ki\2-Thread"

# Bước 2: biên dịch
javac -encoding UTF-8 *.java

# Bước 3: chạy từng file (chạy file nào cũng được, mỗi file là 1 bài độc lập)
java thread.C1_ExtendsThread
java thread.C2_ImplementsRunnable
java thread.C3_ThreadSleepJoin
```

> Nếu lỗi package, xóa dòng `package thread;` rồi chạy: `java C1_ExtendsThread`

---

## So sánh nhanh

| | extends Thread | implements Runnable |
|--|--|--|
| Khai báo | `class X extends Thread` | `class X implements Runnable` |
| Chạy | `new X().start()` | `new Thread(new X()).start()` |
| Hạn chế | Không kế thừa thêm được | Linh hoạt hơn |

---

## Điểm quan trọng

- `start()` → JVM tạo luồng mới → tự gọi `run()`  
- KHÔNG gọi `run()` trực tiếp (sẽ chạy tuần tự, không phải song song)
- `Thread.sleep(500)` → ngủ 500ms, cần try-catch `InterruptedException`
- `join()` → main chờ thread đó xong mới chạy tiếp
