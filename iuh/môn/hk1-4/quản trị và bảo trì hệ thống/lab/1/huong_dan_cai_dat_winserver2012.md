# HƯỚNG DẪN CÀI ĐẶT WINDOWS SERVER 2012 R2 (STEP-BY-STEP)

Tài liệu hướng dẫn chi tiết từng bước cài đặt Windows Server 2012 R2 trên phần mềm máy ảo (VMware Workstation / VirtualBox) phục vụ các bài thực hành môn **Quản trị và Bảo trì Hệ thống (IUH)**.

---

## I. CHUẨN BỊ

1. **File ISO Windows Server 2012 R2** (Bản Standard / Evaluation 64-bit).
2. **Phần mềm máy ảo**: VMware Workstation Pro / Player hoặc Oracle VM VirtualBox.
3. **Cấu hình máy ảo khuyến nghị**:
   * **RAM**: 2048 MB (2 GB) hoặc 4048 MB (4 GB) nếu máy host đủ dung lượng.
   * **CPU**: 1 - 2 Cores.
   * **Ổ cứng (Disk)**: 40 GB - 60 GB (Loại Dynamic / Store single file).
   * **Network Adapter**: Card **Host-only** hoặc **Custom (LAN Segment)** để tạo mạng lab nội bộ giữa WinServer và 2 máy Win7.

---

## II. CÁC BƯỚC CÀI ĐẶT CHI TIẾT (STEP-BY-STEP)

### Bước 1: Khởi động từ File ISO
1. Gắn file ISO **Windows Server 2012 R2** vào ổ CD/DVD của máy ảo.
2. Khởi động máy ảo. Màn hình đầu tiên xuất hiện yêu cầu chọn ngôn ngữ và định dạng:
   * **Language to install**: English
   * **Time and currency format**: English (United States)
   * **Keyboard or input method**: US
3. Nhấn **Next**, sau đó nhấn nút **Install now**.

---

### Bước 2: Chọn phiên bản hệ điều hành (QUAN TRỌNG)
Màn hình **Select the operating system you want to install** xuất hiện 4 lựa chọn:

1. `Windows Server 2012 R2 Standard Evaluation (Server Core Installation) x64`
2. **`Windows Server 2012 R2 Standard Evaluation (Server with a GUI) x64`**  👈 **[CHỌN DÒNG NÀY]**
3. `Windows Server 2012 R2 Datacenter Evaluation (Server Core Installation) x64`
4. `Windows Server 2012 R2 Datacenter Evaluation (Server with a GUI) x64`

> ⚠️ **LƯU Ý CỰC KỲ QUAN TRỌNG**: 
> * Bạn **BẮT BUỘC** phải chọn dòng có chữ **`(Server with a GUI)`** để có giao diện cửa sổ đồ họa. 
> * Nếu chọn bản *Server Core*, máy sẽ chỉ có màn hình dòng lệnh CMD/PowerShell, không thể thực hiện các bài lab quản trị theo tài liệu thực hành.
> * Chọn bản **Standard** giúp máy chạy nhẹ nhàng, tối ưu tài nguyên cho máy ảo.

Nhấn **Next** để tiếp tục.

---

### Bước 3: Chấp nhận điều khoản sử dụng
* Tích chọn vào ô **I accept the license terms**.
* Nhấn **Next**.

---

### Bước 4: Chọn kiểu cài đặt
Màn hình hỏi **Which type of installation do you want?**:
* Chọn **`Custom: Install Windows only (advanced)`**.

---

### Bước 5: Phân vùng ổ đĩa
* Chọn phân vùng ổ đĩa chưa định dạng (**Drive 0 Unallocated Space**).
* Nhấn **Next** (Hệ thống sẽ tự động tạo phân vùng và định dạng đĩa).

---

### Bước 6: Quá trình sao chép và cài đặt
* Hệ thống sẽ tự động thực hiện các bước: *Copying Windows files*, *Getting files ready*, *Installing features*, *Installing updates*.
* Quá trình này mất khoảng 5 - 10 phút. Sau khi hoàn tất, máy ảo sẽ tự động khởi động lại (Restart).

---

### Bước 7: Thiết lập Mật khẩu cho tài khoản Administrator
Sau khi khởi động lại, màn hình **Settings** yêu cầu đặt mật khẩu cho tài khoản quản trị tối cao:

* **User name**: `Administrator` (Mặc định).
* **Re-enter password / Password**: Đặt mật khẩu đáp ứng độ phức tạp của Windows Server (bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt).
  * *Ví dụ mật khẩu hợp lệ*: `P@ssw0rd123` hoặc `Admin@1234`.
* Nhấn **Finish** để hoàn tất.

---

## III. CÁC THIẾT LẬP CẦN THIẾT SAU KHI CÀI ĐẶT (CHO BÀI LAB)

Sau khi đăng nhập vào hệ thống (nhấn `Ctrl + Alt + Delete` hoặc dùng menu của máy ảo), thực hiện các bước tối ưu sau:

### 1. Cài đặt VMware Tools / Guest Additions
* Trên menu phần mềm máy ảo, chọn **VMware Tools** (hoặc *Insert Guest Additions CD Image* trong VirtualBox).
* Mở ổ đĩa CD trong máy ảo, chạy file `setup.exe` để cài đặt đĩa driver giúp màn hình hiển thị chuẩn, mượt mà và copy-paste dễ dàng.

### 2. Đổi tên máy Server (Computer Name)
1. Mở **Server Manager** (hoặc nhấn chuột phải vào *This PC* -> chọn *Properties*).
2. Chọn **Change settings** tại mục *Computer name, domain, and workgroup settings*.
3. Nhấn nút **Change...**, đổi tên máy thành `Server2012` hoặc `R1` (theo yêu cầu bài lab).
4. Khởi động lại máy ảo để áp dụng tên mới.

### 3. Đặt IP Tĩnh (Static IP) & Trỏ DNS
1. Mở **Control Panel** -> **Network and Sharing Center** -> **Change adapter settings**.
2. Nhấn chuột phải vào card mạng `Ethernet` -> chọn **Properties**.
3. Chọn **Internet Protocol Version 4 (TCP/IPv4)** -> chọn **Properties**.
4. Chọn **Use the following IP address**:
   * **IP address**: `192.168.1.1` (Hoặc theo sơ đồ bài lab).
   * **Subnet mask**: `255.255.255.0`.
   * **Preferred DNS server**: `192.168.1.1` (Trỏ về chính IP của Server vì Server sẽ làm Domain Controller & DNS Server).
5. Nhấn **OK** -> **Close**.

### 4. Tắt IE Enhanced Security Configuration (Tùy chọn)
Giúp duyệt web/tải file nội bộ không bị cảnh báo phiền phức:
1. Mở **Server Manager** -> chọn **Local Server**.
2. Tìm mục **IE Enhanced Security Configuration**, chuyển từ *On* sang **Off** cho cả Administrators và Users.
