# Hướng dẫn chi tiết cài đặt EVE-NG và tích hợp IOL (Step-by-Step)

Tài liệu này hướng dẫn chi tiết các bước cài đặt phần mềm giả lập mạng EVE-NG (Emulated Virtual Environment – Next Generation) và tích hợp các image IOL (IOS on Linux) dựa trên slide bài giảng của thầy Phạm Thái Khanh.

## Phần 1: Tải và cài đặt máy ảo EVE-NG

**Bước 1: Tải phần mềm**
- Truy cập trang chủ EVE-NG: [https://www.eve-ng.net/index.php/download/](https://www.eve-ng.net/index.php/download/)
- Tải file máy ảo **EVE-COMM-VM** (bản Community miễn phí) và phần mềm **VMware** (nếu máy bạn chưa có).

**Bước 2: Import máy ảo vào VMware**
- Mở VMware, chọn **Open a Virtual Machine**.
- Trỏ đường dẫn đến thư mục chứa file EVE-COMM-VM vừa tải về và chọn Open.
- Nhập tên cho máy ảo (VD: `EVE-NG`) và chọn nơi lưu trữ, sau đó bấm **Import**.

**Bước 3: Cấu hình phần cứng cho máy ảo (Edit Virtual Machine Settings)**
- Tuỳ thuộc vào cấu hình máy tính thật của bạn, hãy cấp phát phần cứng cho máy ảo EVE-NG một cách phù hợp. Các thông số cần lưu ý:
  - **RAM**
  - **CPU**
  - **HDD**
  - **Network Adapter**
- Nhấn **OK** và bấm **Start** để khởi động máy ảo lên.

## Phần 2: Thiết lập ban đầu cho EVE-NG

**Bước 1: Đăng nhập lần đầu**
- Sau khi máy ảo khởi động xong, màn hình console đen sẽ hiện ra.
- Đăng nhập với tài khoản mặc định: 
  - Username: **`root`**
  - Password: **`eve`**
- Ngay sau đó, hệ thống sẽ yêu cầu bạn nhập mật khẩu mới và xác nhận lại mật khẩu mới.

**Bước 2: Thiết lập thông số mạng và hệ thống**
Màn hình cài đặt màu xanh sẽ tự động hiện ra, bạn làm theo các bước sau (dùng phím mũi tên để di chuyển, phím Space để chọn/bỏ chọn, phím Enter để tiếp tục):
- **Hostname:** Đặt tên cho máy ảo (VD: `EVE_Trung`).
- **DNS domain name:** Nhập domain có chứa MSSV và tên (VD: `17181921trung.com`).
- **Cấu hình IP (IP address):** 
  - Chọn **DHCP** (khuyên dùng để làm lab cho nhanh). 
  - Chọn **Static** nếu bạn muốn gán IP tĩnh (thường dùng khi đưa vào hệ thống thực tế).
- **NTP Server:** Để trống nếu không dùng hệ thống đồng bộ thời gian.
- **Proxy Server:** Chọn **direct connection** (kết nối trực tiếp).

**Bước 3: Cập nhật hệ thống (Update & Upgrade)**
- Sau khi thiết lập xong, máy ảo sẽ tự khởi động lại. Đăng nhập lại vào màn hình đen với tài khoản `root` và mật khẩu mới của bạn.
- Chạy lệnh cập nhật danh sách gói tin:
  ```bash
  apt-get update
  ```
- Chạy lệnh nâng cấp hệ thống (gõ Y và chấp nhận tất cả nếu được hỏi):
  ```bash
  apt-get upgrade
  ```

**Bước 4: Đăng nhập giao diện Web**
- Xem địa chỉ IP của EVE-NG hiển thị trên màn hình console máy ảo.
- Mở trình duyệt web (Chrome, Firefox...) trên máy tính thật và nhập địa chỉ IP đó vào.
- Đăng nhập với tài khoản mặc định của giao diện Web:
  - Username: **`admin`**
  - Password: **`eve`**

## Phần 3: Cài đặt công cụ hỗ trợ Windows Client Side

Bộ công cụ này cung cấp mọi thứ cần thiết (Putty, Wireshark, UltraVNC...) để khi bạn click đúp vào thiết bị trên Web, EVE-NG sẽ tự gọi phần mềm tương ứng dưới máy tính lên để cấu hình.

**Bước 1:** Lên lại trang tải của EVE-NG ([https://www.eve-ng.net/index.php/download/](https://www.eve-ng.net/index.php/download/)).
**Bước 2:** Tìm và tải bộ cài đặt **Windows Client Side**.
**Bước 3:** Chạy file cài đặt với quyền quản trị (**Run as Administrator**) và tiến hành cài đặt bình thường cho đến khi hoàn tất.

## Phần 4: Đưa Image IOL (Router/Switch) vào EVE-NG

IOL (IOS on Linux) là hệ điều hành ảo hóa của Cisco dùng để giả lập Router/Switch rất nhẹ trên EVE-NG. Bản EVE Free chưa có sẵn Image IOL, bạn phải tự chép vào từ bên ngoài.
*Một số bản thông dụng: L3-ADVENTERPRISEK9... (Router), L2-ADVENTERPRISEK9... (Switch).*

**Thư mục đích chứa IOL trên EVE-NG:** `/opt/unetlab/addons/iol/bin/`

**Bước 1: Chép file Image IOL vào EVE-NG**
- Dùng phần mềm **WinSCP** (hoặc FileZilla).
- Kết nối vào EVE-NG bằng IP của máy ảo, Username: **`root`**, Password của máy ảo.
- Ở cửa sổ bên phải (EVE-NG), truy cập theo đúng đường dẫn: `/opt/unetlab/addons/iol/bin/`.
- Ở cửa sổ bên trái (Máy tính của bạn), kéo thả các file IOL dạng `.bin` sang cửa sổ bên phải.

**Bước 2: Tạo file bản quyền (License iourc)**
Để IOL chạy được, cần có file bản quyền `iourc` kèm theo. 
- Mở màn hình console của máy ảo EVE-NG (hoặc dùng Putty SSH vào).
- Di chuyển vào thư mục chứa IOL:
  ```bash
  cd /opt/unetlab/addons/iol/bin
  ```
- Kiểm tra danh sách file (lệnh `ls -l`), chạy file script sinh key (CiscoIOUKeygen.py):
  ```bash
  python CiscoIOUKeygen.py
  ```
- Kết quả trả về trên màn hình sẽ có một đoạn mã license. Hãy copy đoạn mã đó và dùng lệnh `echo` tạo ra file `iourc`, ví dụ:
  ```bash
  echo '[license]
  eve-ng = 972f30267ef51616;' >> iourc
  ```
*(Mẹo nhỏ: Bạn cũng có thể mở WinSCP, chuột phải tạo một file text trống tên là `iourc` ngay trong thư mục `/opt/unetlab/addons/iol/bin/`, dán đoạn text bản quyền vào rồi Save lại).*

**Bước 3: Fix Permission (QUAN TRỌNG NHẤT)**
Mỗi khi bạn chép thêm bất kỳ file image nào vào EVE-NG, bạn BẮT BUỘC phải chạy lệnh cấp lại quyền truy cập, nếu không thiết bị bật lên sẽ bị tắt ngay lập tức.
- Chạy lệnh sau trên console EVE-NG:
  ```bash
  /opt/unetlab/wrappers/unl_wrapper -a fixpermissions
  ```

Đến đây, quá trình cài đặt EVE-NG và tích hợp thành công IOL đã tạm hoàn tất. Bạn có thể vào trình duyệt web, tạo bài Lab mới và chọn thiết bị Cisco IOL ra để sử dụng!
