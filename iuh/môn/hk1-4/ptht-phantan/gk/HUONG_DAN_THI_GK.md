# CẨM NANG ÔN THI & TEMPLATE GIỮA KỲ (GK) - PHÁT TRIỂN HỆ THỐNG PHÂN TÁN (IUH)

---

## I. HƯỚNG DẪN IMPORT VÀO ECLIPSE (TỰ ĐỘNG MAP CODE, KHÔNG BỊ COPY)

Thư mục `gk` đã được cấu hình sẵn 2 file chuẩn của Eclipse là `.project` và `.classpath` với cấu trúc `src/` và `bin/`. Do đó, mọi phiên bản Eclipse (từ Eclipse cũ ở phòng máy trường đến Eclipse 2025 ở máy bạn) đều nhận diện ngay lập tức là Java Project chuẩn.

### 📌 Các bước Import trực tiếp (In-place Mapping):
1. **Mở Eclipse** (Eclipse 2025 hoặc Eclipse trên phòng máy trường).
2. Chọn menu: **File -> Open Projects from File System...** 
   *(Hoặc: **File -> Import... -> General -> Existing Projects into Workspace** -> Next)*.
3. Tại ô **Import source** (hoặc **Select root directory**), bấm nút **Directory...** (hoặc **Browse...**):
   - Trỏ tới đúng thư mục: `d:\folder\rac\iuh\môn\hk1-4\ptht-phantan\gk`
4. **⚠️ LƯU Ý SỐNG CÒN (ĐỂ TỰ MAP CODE):**
   - **TUYỆT ĐỐI KHÔNG TÍCH** vào ô checkbox: `[ ] Copy projects into workspace`.
   - Nếu bạn tích vào ô này, Eclipse sẽ copy một bản sao khác vào thư mục workspace, lúc đó sửa code ở ngoài sẽ KHÔNG map vào Eclipse!
   - Bỏ tích ô đó -> Bấm **Finish**.
5. **Kích hoạt tự động làm mới (Auto Refresh):**
   - Vào menu: **Window -> Preferences -> General -> Workspace**.
   - Tích chọn ô: **`[x] Refresh using native hooks or polling`** -> Bấm **Apply and Close**.
   - *Mẹo:* Khi bạn sửa file ở ngoài (bằng VS Code / Notepad / Antigravity), khi quay lại Eclipse, nếu chưa thấy cập nhật thì chỉ cần bấm chuột vào Project `gk` trong tab *Package Explorer* và nhấn phím **F5** (Refresh).

---

## II. MA TRẬN ĐỐI CHIẾU 100% CÁC BÀI THỰC HÀNH (TH TUẦN 1 - 6) VÀ ĐỀ THI

| Tuần / Nội dung TH | Yêu cầu bài toán | Tương ứng trong bộ template `gk` | Khả năng ra thi |
| :--- | :--- | :--- | :---: |
| **Đề thi mẫu GK (Câu 1)** | UDP Socket: Chuyển số thành chữ (VD: `"3432"` -> `"3432: ba bốn ba hai"`). | `src/gkudp/ThreadProcess.java` (Bài 32) & `src/gkrmi/` (`doiSoThanhChu`) | **95%** |
| **Đề thi mẫu GK (Câu 2)** | TCP Socket: Tìm thông tin người dùng theo Email (lưu bằng Mảng hoặc File văn bản). | `src/gk/ThreadProcess.java` (Bài 33) & `users.txt` & `src/gkrmi/` (`timNguoiDungTheoEmail`) | **95%** |
| **TH Tuần 6 (RMI)** | RMI: Registry 1099, args IP/Port, 4 phép tính (+ - * /), giải PT, Chuỗi, Dãy số, Đối tượng. | Toàn bộ package `src/gkrmi/` (`IRemoteService`, `RemoteServiceImpl`, `RMIServer`, `RMIClient`) | **90%** |
| **TH Tuần 5 (Lab 5)** | TCP Socket: Sắp xếp dãy số (In chuỗi gốc, sắp giảm dần, sắp tăng dần). | `src/gk/ThreadProcess.java` (Bài 34) & `src/gkrmi/` (`sapXepDaySo`) | **85%** |
| **TH Tuần 4** | TCP Socket Multi-client: Chat Group, Server làm trung gian broadcast cho các client. | Package `src/gkchat/` (`ChatServer.java` & `ChatClient.java`) | **50%** |
| **TH Tuần 3 (Streams)** | Đọc ghi file văn bản, Serializable Object (`Student`), Data streams. | File `users.txt`, `SinhVien.java`, Bài 36 (Đọc file từ xa qua Socket). | **Lồng ghép** |
| **TH Tuần 1 (OOP)** | Class Học sinh/Sinh viên: Mã, Tên, Điểm TB, hàm `rank()` xếp loại. | `src/gkrmi/SinhVien.java` & Bài 35 (Xếp loại sinh viên). | **Lồng ghép** |

---

## III. CẤU TRÚC GÓI MÃ NGUỒN TRONG ECLIPSE

```text
gk/ (Java Project)
├── .project                   <- File cấu hình Project Eclipse
├── .classpath                 <- File cấu hình Build Path tự nhận JRE máy trường & máy nhà
├── users.txt                  <- File văn bản dữ liệu người dùng mẫu (Câu 2 đề thi)
├── bin/                       <- Thư mục chứa file biên dịch .class
└── src/
    ├── gk/                    <- [BỘ 1: TCP SOCKET REQUEST-RESPONSE]
    │   ├── Server.java        <- TCP Server đa luồng (Port 5000)
    │   ├── Client.java        <- TCP Client Console
    │   └── ThreadProcess.java <- Thư viện 36 BÀI TOÁN XỬ LÝ (Có đủ đề thi & bài TH)
    │
    ├── gkudp/                 <- [BỘ 2: UDP SOCKET]
    │   ├── Server.java        <- UDP Server (Port 5000)
    │   ├── Client.java        <- UDP Client
    │   └── ThreadProcess.java <- Thư viện 36 BÀI TOÁN XỬ LÝ
    │
    ├── gkrmi/                 <- [BỘ 3: JAVA RMI HOÀN CHỈNH]
    │   ├── IRemoteService.java    <- Interface Remote (Toán, Chuỗi, Mảng số, Đối tượng)
    │   ├── RemoteServiceImpl.java <- Cài đặt chi tiết tất cả các hàm
    │   ├── RMIServer.java         <- Tự động tạo Registry 1099 & Naming.rebind
    │   ├── RMIClient.java         <- Client gọi hàm từ xa (Có sẵn 5 mẫu chạy thử)
    │   └── SinhVien.java          <- Model Serializable chuẩn OOP Tuần 1 & Tuần 3
    │
    └── gkchat/                <- [BỘ 4: TCP CHAT GROUP MULTI-CLIENT TUẦN 4]
        ├── ChatServer.java    <- Server trung gian Broadcast Vector<ClientHandler>
        └── ChatClient.java    <- Client 2 luồng (vừa nghe tin nhắn, vừa gõ phím)
```

---

## IV. HƯỚNG DẪN "ĐI THI BIẾT XÓA CÁI GÌ, CHỪA LẠI CÁI GÌ"

### 1. Đề thi ra TCP SOCKET (dùng package `gk`):
- **Server.java** & **Client.java**: Giữ nguyên 100%. (Đổi biến `PORT` nếu đề chỉ định cổng).
- **ThreadProcess.java**: 
  - Mở hàm `processData(String data)`.
  - Tìm bài tương ứng theo comment:
    + Câu 1 GK (Đổi số thành chữ): Tìm `BAI 32`, bỏ dấu `//`.
    + Câu 2 GK (Tìm Email): Tìm `BAI 33`, bỏ dấu `//`.
    + Lab 5 (Sắp xếp dãy số): Tìm `BAI 34`, bỏ dấu `//`.
    + Lab 1 (Xếp loại SV): Tìm `BAI 35`, bỏ dấu `//`.
    + Đọc file Server: Tìm `BAI 36`, bỏ dấu `//`.
    + Toán / Chuỗi khác: Chọn từ Bài 1 đến Bài 31.
  - Xóa hoặc để comment các bài còn lại.

### 2. Đề thi ra UDP SOCKET (dùng package `gkudp`):
- **Server.java** & **Client.java**: Giữ nguyên 100%.
- **ThreadProcess.java**: Thao tác uncomment đúng bài cần làm như TCP.

### 3. Đề thi ra JAVA RMI (dùng package `gkrmi`):
- **RMIServer.java**: Giữ nguyên 100%.
- **IRemoteService.java**: Chừa lại đúng hàm đề yêu cầu, xóa các hàm thừa.
- **RemoteServiceImpl.java**: Giữ lại các hàm tương ứng, xóa các hàm thừa. Cập nhật dữ liệu trong `userDatabase` hoặc `users.txt` nếu có.
- **RMIClient.java**: Uncomment 1 trong 5 khối Demo có sẵn tương ứng với bài, xóa các khối còn lại.
- **SinhVien.java**: Giữ lại nếu đề có xử lý đối tượng.

### 4. Đề thi ra TCP CHAT GROUP / BROADCAST (dùng package `gkchat`):
- Chạy `ChatServer.java` trên 1 tab Console.
- Chạy 2 hoặc nhiều lần `ChatClient.java` trên các tab Console khác nhau để chat qua lại.

---

## V. ĐẢM BẢO TƯƠNG THÍCH MỌI PHIÊN BẢN ECLIPSE & JAVA
- Toàn bộ mã nguồn đã được chuẩn hóa để tuân thủ **Java 8+**, hoàn toàn loại bỏ các hàm chỉ có ở Java 11+ (như `isBlank()`) và Java 16+ (như `.toList()`).
- File `.classpath` sử dụng biến generic `JRE_CONTAINER`, tự động thích ứng với bất kỳ phiên bản JDK/JRE nào có sẵn trên máy của trường và Eclipse 2025.
