# HƯỚNG DẪN CHI TIẾT BÀI LAB 7: XINETD, REMOTE ACCESS (TELNET, OPENSSH) & FTP SERVER (VSFTPD)

**Môn học:** Quản trị dịch vụ mạng (IUH)
**Môi trường thử nghiệm:** Hệ thống chuẩn **4 máy ảo** (2 Ubuntu 22.04 LTS Server + 2 Windows 7 SP1)
**Tài liệu tham chiếu:** Slide bài giảng *Bài tập 7: Xinetd & Remote Access*

---

## 📌 1. TỔNG QUAN KIẾN TRÚC MẠNG & 4 MÁY ẢO

Hệ thống triển khai bài Lab 7 trên đúng mô hình 4 máy ảo chuẩn của phòng thực hành IUH:

```
                  [ MÁY THẬT (HOST WINDOWS) ]
                               │
                 VMnet8 (NAT: 192.168.1.0/24)
          ┌────────────────────┴────────────────────┐
          │ (ens33: 192.168.1.150)                  │ (Không có card NAT)
   ┌──────┴──────────────┐                   ┌──────┴──────────────┐
   │ Ubuntu_1 (LinuxA)   │                   │ Ubuntu_2 (LinuxB)   │
   │ - Xinetd Server     │                   │ - Telnet Client     │
   │ - Telnetd Server    │                   │ - OpenSSH Client    │
   │ - OpenSSH Server    │                   │ - FTP Client        │
   │ - vsftpd Server     │                   │                     │
   └──────┬──────────────┘                   └──────┬──────────────┘
          │ (ens37: 192.168.5.2)                    │ (ens37: 192.168.6.2)
          │                                         │ (ens37:0: 192.168.5.3)
   VMnet2 (LAN 1: 192.168.5.0/24)            VMnet3 (LAN 2: 192.168.6.0/24)
          │                                         │
          │ (ens38: 192.168.6.3)                    │
          └───────────────────┬─────────────────────┘
                              │
          ┌───────────────────┴─────────────────────┐
          │                                         │
   ┌──────┴──────────────┐                   ┌──────┴──────────────┐
   │ Win7_A (Client 1)   │                   │ Win7_B (Client 2)   │
   │ IP: 192.168.5.1     │                   │ IP: 192.168.6.1     │
   │ - Telnet Client     │                   │ - Telnet Client     │
   │ - FTP Client        │                   │ - FTP Client        │
   └─────────────────────┘                   └─────────────────────┘
```

### Bảng phân bổ địa chỉ IP & Vai trò trong Lab 7:

| STT | Tên Máy ảo                   | Hệ điều hành        | Card mạng VMware                                                                    | Interface / IP Subnet                                                             | Vai trò trong Bài Lab 7                                                                                                                                                                                 |
| :-- | :------------------------------ | :---------------------- | :----------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Ubuntu_1** *(LinuxA)* | Ubuntu 22.04 LTS Server | - Card 1: NAT (`VMnet8`)- Card 2: Custom (`VMnet2`)- Card 3: Custom (`VMnet3`) | `ens33`: `192.168.1.150/24ens37`: `192.168.5.2/24ens38`: `192.168.6.3/24` | **Server chính**:- Quản lý siêu dịch vụ **Xinetd**- **Telnet Server** (`telnetd`)- **OpenSSH Server** (`sshd`)- **FTP Server** (`vsftpd` - Standalone & Xinetd) |
| 2   | **Ubuntu_2** *(LinuxB)* | Ubuntu 22.04 LTS Server | - Card 1: Custom (`VMnet3`)                                                        | `ens37`: `192.168.6.2/24ens37:0`: `192.168.5.3/24`                          | **Linux Client**:- Kiểm thử dòng lệnh: `telnet`, `ssh`, `scp`, `sftp`, `ftp`                                                                                                          |
| 3   | **Win7_A** *(Host A)*   | Windows 7 SP1           | Custom (`VMnet2`)                                                                  | Local Area Connection:`192.168.5.1/24` (GW: `192.168.5.2`)                    | **Windows Client 1 (LAN 1)**:- Kiểm thử Telnet và FTP từ giao diện Windows                                                                                                                     |
| 4   | **Win7_B** *(Host B)*   | Windows 7 SP1           | Custom (`VMnet3`)                                                                  | Local Area Connection:`192.168.6.1/24` (GW: `192.168.6.3`)                    | **Windows Client 2 (LAN 2)**:- Kiểm thử Telnet và FTP từ giao diện Windows                                                                                                                     |

> **Tài khoản đăng nhập mặc định trên Ubuntu:**
>
> - Username: `neko`
> - Password: `conmeo` (Mật khẩu quyền root / sudo: `conmeo`)
> - User thực nghiệm bảo mật: `testuser1` (Pass: `123`), `testuser2` (Pass: `123`)

---

## 🎯 2. NỘI DUNG VÀ MỤC TIÊU CỐT LÕI CỦA BÀI LAB 7

Bài Lab 7 tập trung vào **3 chuyên đề lớn** của dịch vụ mạng nâng cao:

1. **Xinetd (Super-server / Super-daemon)**:
   * Hiểu bản chất cơ chế hoạt động của siêu dịch vụ lắng nghe tập trung, giải phóng tài nguyên CPU/RAM khi dịch vụ không có phiên làm việc.
   * Nắm vững cú pháp file cấu hình chung `/etc/xinetd.conf` và các file cấu hình dịch vụ thành phần trong `/etc/xinetd.d/`.
2. **Truy cập từ xa (Remote Access) — Telnet vs OpenSSH**:
   * Cài đặt và đưa dịch vụ **Telnet** (Port 23) vào quản lý qua `xinetd`.
   * Cấu hình dịch vụ **OpenSSH Server** (Port 22), thiết lập chính sách bảo mật kiểm soát người dùng (`AllowUsers`, `DenyUsers`, `PermitRootLogin`).
   * Sử dụng thành thạo các công cụ mã hóa bảo mật: `ssh`, `scp`, `sftp`, xác thực khóa công khai (SSH Key Pair không cần mật khẩu).
3. **Dịch vụ chia sẻ file FTP Server (vsftpd)**:
   * **Demo 1 (Standalone Mode)**: Cấu hình `vsftpd` chạy độc lập, quản lý bằng `systemctl`. Vô hiệu hóa người dùng nặc danh (`anonymous_enable=NO`), cấp quyền cho người dùng cục bộ (`local_enable=YES`, `write_enable=YES`) và khóa thư mục gốc `chroot`.
   * **Demo 2 (Xinetd Mode)**: Chuyển đổi dịch vụ `vsftpd` sang chạy dưới sự điều khiển của `xinetd` (`listen=NO` và tạo file `/etc/xinetd.d/vsftpd`).

---

## ⚙️ 3. PHẦN 1: DỊCH VỤ XINETD & TELNET SERVER (DEMO 1)

### 3.1 Lý thuyết cơ chế Super-server (Xinetd)

* **Vấn đề của Standalone Daemons:** Mỗi dịch vụ mạng (FTP, Telnet, POP3, IMAP,...) nếu đều chạy nền liên tục sẽ chiếm dụng socket, bộ nhớ RAM và tiến trình CPU, dù cả ngày có thể chỉ có vài lượt kết nối.
* **Giải pháp của Xinetd:**
  * `xinetd` đóng vai trò là "người gác cổng" duy nhất, lắng nghe tất cả các cổng của các dịch vụ mà nó quản lý (ví dụ: Port 23 của Telnet, Port 21 của FTP).
  * Khi có gói tin yêu cầu kết nối từ Client gửi tới cổng tương ứng, `xinetd` mới khởi động tiến trình con (daemon thực sự như `in.telnetd` hoặc `vsftpd`) để phục vụ.
  * Khi phiên kết nối kết thúc, tiến trình con tự động giải phóng khỏi bộ nhớ RAM.
* **Cấu trúc thư mục:**
  * File cấu hình toàn cục: `/etc/xinetd.conf`
  * Thư mục chứa cấu hình từng dịch vụ: `/etc/xinetd.d/` (mỗi dịch vụ là một file riêng biệt như `telnet`, `ftp`, `daytime`, `echo`,...)

---

### 3.2 Các bước cấu hình Telnet qua Xinetd trên Server (Ubuntu_1)

#### Bước 1: Cài đặt gói `xinetd` và `telnetd`

Đăng nhập vào **Ubuntu_1** (`192.168.1.150`) và thực hiện lệnh:

```bash
sudo apt-get update
sudo apt-get install -y xinetd telnetd
```

#### Bước 2: Tạo file cấu hình dịch vụ Telnet cho Xinetd

Tạo mới file `/etc/xinetd.d/telnet` bằng lệnh:

```bash
sudo nano /etc/xinetd.d/telnet
```

Nhập nội dung cấu hình chuẩn theo slide bài giảng:

```text
service telnet
{
    flags           = REUSE
    socket_type     = stream
    protocol        = tcp
    wait            = no
    user            = root
    server          = /usr/sbin/in.telnetd
    log_on_failure  += USERID
    disable         = no
}
```

> **Giải thích ý nghĩa từng tham số:**
>
> * `service telnet`: Tên dịch vụ, được định nghĩa đối chiếu trong file `/etc/services` (Port 23/TCP).
> * `socket_type = stream`: Kiểu socket truyền dữ liệu theo luồng hướng kết nối (TCP).
> * `protocol = tcp`: Giao thức tầng vận chuyển TCP.
> * `wait = no`: Không chờ kết thúc phiên trước, cho phép phục vụ nhiều kết nối đồng thời (multithreaded).
> * `user = root`: Quyền thực thi chương trình daemon khi được gọi.
> * `server = /usr/sbin/in.telnetd`: Đường dẫn thực thi file nhị phân của dịch vụ Telnet.
> * `disable = no`: **BẬT** dịch vụ. (Nếu muốn tạm ngưng dịch vụ, chỉ cần sửa thành `disable = yes`).

#### Bước 3: Khởi động và kích hoạt Xinetd

```bash
sudo systemctl enable xinetd
sudo systemctl restart xinetd
```

#### Bước 4: Kiểm tra trạng thái cổng 23

Kiểm tra xem cổng 23 đã được `xinetd` lắng nghe hay chưa:

```bash
sudo ss -tlnp | grep :23
# hoặc:
sudo netstat -tlpn | grep :23
```

**Kết quả hiển thị thành công:**

```text
LISTEN 0 64 *:23 *:* users:(("xinetd",pid=4468,fd=5))
```

*(Ghi chú: Tiến trình sở hữu cổng 23 chính là `xinetd`, chứng minh dịch vụ Telnet đang nằm dưới sự kiểm soát của Super-server).*

---

### 3.3 Kiểm thử kết nối Telnet từ Client

#### Thử nghiệm 1: Từ Client Ubuntu_2 (`192.168.6.2`)

Trên **Ubuntu_2**, gõ lệnh kết nối đến IP của Ubuntu_1 trên mạng LAN 2:

```bash
telnet 192.168.6.3
```

* Màn hình xuất hiện lời chào: `Welcome to Ubuntu 22.04.3 LTS`
* Nhập `login:` `neko`
* Nhập `Password:` `conmeo`
* Sau khi đăng nhập thành công, chạy các lệnh kiểm tra:
  ```bash
  whoami          # Hiển thị: neko
  hostname        # Hiển thị: ubuntu2204 (Tên máy Ubuntu_1)
  ip -br a        # Hiển thị danh sách card mạng của Ubuntu_1
  exit            # Thoát phiên Telnet
  ```

#### Thử nghiệm 2: Từ Windows 7 (Win7_A - `192.168.5.1`)

Trên **Win7_A**, mở CMD và gõ:

```cmd
telnet 192.168.5.2
```

Nhập tài khoản `neko` / `conmeo`. Mọi thao tác quản trị dòng lệnh đều được thực hiện từ xa trên Windows 7.

#### Thử nghiệm 3: Thử tắt dịch vụ qua Xinetd (Kiểm tra cơ chế `disable`)

Trên **Ubuntu_1**, mở file `/etc/xinetd.d/telnet`, sửa:

```text
disable = yes
```

Reload lại xinetd:

```bash
sudo systemctl restart xinetd
```

Quay lại Client kết nối:

```bash
telnet 192.168.6.3
```

**Kết quả:** Client nhận thông báo lỗi ngay lập tức: `telnet: Unable to connect to remote host: Connection refused`. Điều này chứng minh Xinetd đã đóng cổng 23.

---

## 🔒 4. PHẦN 2: DỊCH VỤ OPENSSH SERVER & BẢO MẬT TRUY CẬP (DEMO 1, 2, 3)

### 4.1 So sánh giữa Telnet và OpenSSH

| Đặc điểm                    | Telnet                                                                                                                             | OpenSSH (Secure Shell)                                                                                         |
| :------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------- |
| **Cổng mặc định**     | Port 23 / TCP                                                                                                                      | Port 22 / TCP                                                                                                  |
| **Mã hóa dữ liệu**    | **KHÔNG** mã hóa (Plaintext). Mật khẩu và câu lệnh truyền trần trên mạng, dễ bị bắt gói tin bằng Wireshark. | **MÃ HÓA TOÀN BỘ** dữ liệu (AES, RSA, ChaCha20,...). Bảo mật tuyệt đối trước kẻ nghe lén. |
| **Xác thực**            | Chỉ hỗ trợ Mật khẩu truyền thống                                                                                            | Hỗ trợ Mật khẩu, Khóa công khai (Public Key), Chứng chỉ số.                                           |
| **Tính năng kèm theo** | Chỉ dòng lệnh terminal thuần                                                                                                   | Hỗ trợ Terminal, truyền file bảo mật (`scp`, `sftp`), tạo đường hầm (SSH Tunneling, VPN).        |

---

### 4.2 Cài đặt & Cấu hình OpenSSH Server trên Ubuntu_1

Gói `openssh-server` đã được cài đặt sẵn:

* Daemon quản lý: `sshd`
* File cấu hình chính: `/etc/ssh/sshd_config`
* Lệnh khởi động lại dịch vụ: `sudo systemctl restart ssh`

---

### 4.3 Demo 1: Thiết lập truy cập từ xa bằng SSH

Từ **Ubuntu_2** hoặc **Máy thật Windows**, thực hiện lệnh:

```bash
ssh neko@192.168.6.3
# hoặc:
ssh -l neko 192.168.6.3
```

* Lần đầu kết nối, SSH sẽ hỏi xác nhận vân tay khóa máy chủ (Host key fingerprint): gõ `yes`.
* Nhập mật khẩu: `conmeo` ➜ Đăng nhập thành công vào phiên làm việc bảo mật.

---

### 4.4 Demo 2: Cấu hình giới hạn & Bảo mật người dùng (Access Control)

Yêu cầu thực tế của đề thi & quản trị viên:

1. **Cấm tài khoản `root`** đăng nhập trực tiếp từ xa (tránh hacker tấn công brute-force tài khoản tối cao).
2. **Chỉ định danh sách người dùng được phép:** Chỉ cho phép `neko` và `testuser1` truy cập SSH. Tất cả người dùng khác (kể cả có mật khẩu đúng như `testuser2`) đều bị cấm.

#### Bước 1: Tạo các user thử nghiệm trên Ubuntu_1

```bash
# Tạo user testuser1 (Được phép)
sudo useradd -m -s /bin/bash testuser1
echo "testuser1:123" | sudo chpasswd

# Tạo user testuser2 (Bị chặn)
sudo useradd -m -s /bin/bash testuser2
echo "testuser2:123" | sudo chpasswd
```

#### Bước 2: Cấu hình file `/etc/ssh/sshd_config`

Mở file cấu hình SSH Server:

```bash
sudo nano /etc/ssh/sshd_config
```

Thêm/sửa các dòng cấu hình sau ở cuối file:

```text
# 1. Cấm tài khoản root đăng nhập trực tiếp
PermitRootLogin no

# 2. Chỉ cho phép các user được chỉ định rõ ràng
AllowUsers neko testuser1
```

> **Ghi chú về các chỉ thị phân quyền trong SSH:**
>
> * `AllowUsers user1 user2`: Chỉ cho phép danh sách user này đăng nhập. Mọi user khác bị từ chối.
> * `DenyUsers user3`: Cấm cụ thể user3 đăng nhập.
> * `AllowGroups group1`: Cho phép thành viên của group1.
> * `DenyGroups group2`: Cấm thành viên của group2.
> * `Port 2222`: Thay đổi port mặc định từ 22 sang cổng khác để tránh scan tự động.

#### Bước 3: Kiểm tra lỗi cú pháp và khởi động lại dịch vụ SSH

```bash
# Kiểm tra cú pháp xem có bị gõ sai không
sudo sshd -t

# Khởi động lại dịch vụ
sudo systemctl restart ssh
```

#### Bước 4: Kiểm thử chính sách bảo mật từ Client (Ubuntu_2)

* **Kiểm tra 1: Thử đăng nhập bằng `testuser1` (User nằm trong AllowUsers):**

  ```bash
  ssh testuser1@192.168.6.3
  ```

  ➜ Nhập pass `123` ➜ **THÀNH CÔNG!**
* **Kiểm tra 2: Thử đăng nhập bằng `testuser2` (User KHÔNG nằm trong AllowUsers):**

  ```bash
  ssh testuser2@192.168.6.3
  ```

  ➜ Dù nhập đúng mật khẩu `123`, SSH vẫn báo: `Permission denied, please try again.` ➜ **BỊ CHẶN CHÍNH XÁC!**
* **Kiểm tra 3: Thử đăng nhập bằng `root`:**

  ```bash
  ssh root@192.168.6.3
  ```

  ➜ Nhập mật khẩu ➜ Bị từ chối `Permission denied` do chỉ thị `PermitRootLogin no`.

---

### 4.5 Demo 3: Sử dụng các công cụ SCP, SFTP & Xác thực SSH Key không cần mật khẩu

#### A. Công cụ sao chép file an toàn (`scp` - Secure Copy)

Cú pháp: `scp [options] source destination`

* **Sao chép file từ Client lên Server:**

  ```bash
  # Tạo file mẫu trên Client
  echo "Noi dung file tu Client" > /tmp/baocao.txt

  # Đẩy file lên thư mục cá nhân của testuser1 trên Server
  scp /tmp/baocao.txt testuser1@192.168.6.3:/home/testuser1/
  ```
* **Sao chép file từ Server về Client:**

  ```bash
  scp testuser1@192.168.6.3:/home/testuser1/baocao.txt /home/neko/
  ```
* **Sao chép toàn bộ thư mục (thêm cờ `-r`):**

  ```bash
  scp -r /tmp/tailieu testuser1@192.168.6.3:/home/testuser1/
  ```

#### B. Công cụ truyền file tương tác (`sftp`)

Trên Client, khởi tạo phiên làm việc SFTP:

```bash
sftp testuser1@192.168.6.3
```

Các lệnh thông dụng trong giao diện tương tác SFTP:

* `put filename`: Tải file từ Client lên Server.
* `get filename`: Tải file từ Server về Client.
* `ls`: Xem danh sách file trên Server từ xa.
* `lls`: Xem danh sách file trên máy Client cục bộ.
* `pwd`: Xem thư mục hiện tại trên Server.
* `lpwd`: Xem thư mục hiện tại trên Client.
* `mkdir folder_name`: Tạo thư mục trên Server.
* `bye` hoặc `quit`: Thoát khỏi SFTP.

#### C. Cấu hình xác thực bằng cặp khóa (SSH Key Pair - Đăng nhập không cần gõ mật khẩu)

Thay vì dùng mật khẩu dễ bị lộ, quản trị viên sử dụng cặp khóa công khai / riêng tư (Public/Private Key):

1. **Trên Client (Ubuntu_2):** Tạo cặp khóa RSA 2048-bit:
   ```bash
   ssh-keygen -t rsa -b 2048
   # Bấm Enter liên tục 3 lần để chấp nhận đường dẫn mặc định ~/.ssh/id_rsa và không đặt passphrase
   ```
2. **Đẩy khóa công khai (Public Key) lên Server (Ubuntu_1):**
   ```bash
   ssh-copy-id neko@192.168.6.3
   ```

   *(Nhập mật khẩu `conmeo` của neko một lần duy nhất).*
3. **Kiểm tra đăng nhập lại:**
   ```bash
   ssh neko@192.168.6.3
   ```

   ➜ **Hệ thống vào thẳng terminal Server ngay lập tức mà không yêu cầu gõ mật khẩu!**

---

## 📂 5. PHẦN 3: DỊCH VỤ FTP SERVER VSFTPD (DEMO 1 & DEMO 2)

Dịch vụ FTP (File Transfer Protocol) hoạt động trên 2 cổng TCP:

* **Port 21 (Control/Command Connection):** Truyền nhận lệnh điều khiển, tài khoản, mật khẩu.
* **Port 20 (Data Connection):** Truyền nhận dữ liệu nội dung file thực tế.

`vsftpd` (Very Secure FTP Daemon) là máy chủ FTP an toàn, ổn định và hiệu năng cao nhất trên Linux. Đề bài yêu cầu triển khai theo **2 phương thức quản trị**:

---

### 5.1 Demo 1: Cài đặt và cấu hình VSFTPD ở chế độ Standalone

Ở chế độ này, tiến trình `vsftpd` chạy thường trực trong hệ thống, tự động chiếm giữ và lắng nghe trên Port 21 dưới sự quản lý của Systemd.

#### Bước 1: Cài đặt gói `vsftpd` và `ftp`

```bash
sudo apt-get update
sudo apt-get install -y vsftpd ftp
```

#### Bước 2: Cấu hình file `/etc/vsftpd.conf`

Tạo bản sao lưu và mở file cấu hình:

```bash
sudo cp /etc/vsftpd.conf /etc/vsftpd.conf.bak
sudo nano /etc/vsftpd.conf
```

Soạn thảo nội dung cấu hình chuẩn cho chế độ Standalone:

```ini
# Lắng nghe độc lập trên IPv4
listen=YES
listen_ipv6=NO

# Yêu cầu đề bài: KHÔNG cho phép người dùng ẩn danh (Anonymous)
anonymous_enable=NO

# Cho phép tài khoản người dùng cục bộ trên Linux đăng nhập
local_enable=YES

# Cho phép thực hiện các thao tác ghi (Upload, đổi tên, xóa file, tạo thư mục)
write_enable=YES

# Mặt nạ quyền mặc định umask 022 (Thư mục tạo ra quyền 755, file quyền 644)
local_umask=022

dirmessage_enable=YES
use_localtime=YES
xferlog_enable=YES
connect_from_port_20=YES

# Khóa người dùng vào thư mục cá nhân (Chroot jail) - Không cho phép duyệt ra thư mục /etc, /var,...
chroot_local_user=YES
allow_writeable_chroot=YES

# Thư mục an toàn bắt buộc của Ubuntu vsftpd
secure_chroot_dir=/var/run/vsftpd/empty
pam_service_name=vsftpd
rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
ssl_enable=NO
```

> **Lưu ý đặc biệt quan trọng (Tránh lỗi điểm liệt):**
>
> * Khi bật `chroot_local_user=YES`, người dùng khi đăng nhập sẽ bị giam trong thư mục `/home/username`.
> * Theo cơ chế bảo mật của `vsftpd`, nếu thư mục gốc của chroot có quyền ghi (`writeable`), dịch vụ sẽ báo lỗi: `500 OOPS: vsftpd: refusing to run with writable root inside chroot()`.
> * Để xử lý triệt để lỗi này, **BẮT BUỘC** phải có dòng: `allow_writeable_chroot=YES`.

#### Bước 3: Khởi động và kiểm tra dịch vụ

```bash
sudo systemctl enable vsftpd
sudo systemctl restart vsftpd

# Kiểm tra trạng thái cổng 21
sudo ss -tlnp | grep :21
```

**Kết quả hiển thị:**

```text
LISTEN 0 32 0.0.0.0:21 0.0.0.0:* users:(("vsftpd",pid=5570,fd=3))
```

*(Tiến trình trực tiếp lắng nghe là `vsftpd`).*

#### Bước 4: Kiểm thử kết nối Standalone từ Client

* **Thử nghiệm 1: Kiểm tra tài khoản `anonymous` (Phải bị chặn theo đề bài):**
  Từ Client (Ubuntu_2), gõ:

  ```bash
  ftp 192.168.6.3
  ```

  Nhập Name: `anonymous`Nhập Password: *(Enter)*➜ **Kết quả:** `530 Login incorrect. Login failed.` ➜ **CHẶN ANONYMOUS THÀNH CÔNG!**
* **Thử nghiệm 2: Kiểm tra tài khoản người dùng cục bộ (`testuser1`):**
  Gõ lệnh:

  ```bash
  ftp 192.168.6.3
  ```

  Nhập Name: `testuser1`
  Nhập Password: `123`
  ➜ **Kết quả:** `230 Login successful.`

  Thực hiện các thao tác file thực tế trong phiên FTP:

  ```ftp
  ftp> pwd                          # Xem thư mục hiện tại: hiển thị "/" (đã bị chroot)
  ftp> !echo "Noi dung upload" > test.txt  # Tạo file cục bộ ngay trong FTP client
  ftp> put test.txt                 # Upload file lên server
  ftp> ls                           # Liệt kê danh sách file trên server
  ftp> get test.txt download.txt    # Tải file về máy client
  ftp> mkdir thu_muc_moi            # Tạo thư mục mới trên server
  ftp> quit                         # Thoát khỏi FTP
  ```

---

### 5.2 Demo 2: Chuyển đổi VSFTPD sang quản lý bằng Xinetd (Super-server)

Ở chế độ này, tiến trình `vsftpd` **KHÔNG** chạy nền liên tục. Cổng 21 sẽ được bàn giao cho `xinetd` quản lý. Chỉ khi có Client kết nối tới cổng 21, `xinetd` mới đánh thức `vsftpd` dậy phục vụ.

#### Bước 1: Sửa cấu hình `vsftpd.conf`

Mở file `/etc/vsftpd.conf`:

```bash
sudo nano /etc/vsftpd.conf
```

Tìm dòng `listen=YES` và sửa thành:

```ini
listen=NO
```

*(Ghi chú: Phải đặt `listen=NO` vì nếu để `YES`, vsftpd sẽ cố chiếm cổng 21 và gây lỗi xung đột `Address already in use` với xinetd).*

#### Bước 2: Tắt và vô hiệu hóa dịch vụ Standalone vsftpd

```bash
sudo systemctl stop vsftpd
sudo systemctl disable vsftpd
```

#### Bước 3: Tạo file cấu hình dịch vụ FTP cho Xinetd (`/etc/xinetd.d/vsftpd`)

```bash
sudo nano /etc/xinetd.d/vsftpd
```

Soạn thảo nội dung cấu hình:

```text
service ftp
{
    socket_type     = stream
    protocol        = tcp
    wait            = no
    user            = root
    server          = /usr/sbin/vsftpd
    server_args     = /etc/vsftpd.conf
    disable         = no
}
```

> **Giải thích tham số:**
>
> * `service ftp`: Tên dịch vụ chuẩn được map với Port 21 trong `/etc/services`.
> * `server = /usr/sbin/vsftpd`: Chương trình thực thi daemon của vsftpd.
> * `server_args = /etc/vsftpd.conf`: Tham số truyền vào chỉ rõ file cấu hình cần nạp.
> * `disable = no`: Kích hoạt dịch vụ.

#### Bước 4: Khởi động lại Xinetd và kiểm tra cổng 21

```bash
sudo systemctl restart xinetd
sudo ss -tlnp | grep :21
```

**Kết quả hiển thị:**

```text
LISTEN 0 64 *:21 *:* users:(("xinetd",pid=6183,fd=6))
```

*(Cực kỳ quan trọng: Quan sát thấy `users:(("xinetd",...))` quản lý cổng 21 thay vì `vsftpd`).*

#### Bước 5: Kiểm thử từ Client

Từ Ubuntu_2 hoặc Windows 7, kết nối lại FTP:

```bash
ftp 192.168.6.3
```

* Đăng nhập `anonymous` ➜ Bị từ chối (`530 Login incorrect`).
* Đăng nhập `testuser1` / `123` ➜ **Thành công 100%!**
* Thực hiện upload / download bình thường.
* 👉 Đối với người dùng Client, trải nghiệm dịch vụ hoàn toàn giống hệt Standalone, nhưng đối với hệ điều hành máy chủ, RAM được giải phóng tối đa khi không có ai kết nối!

---

## 🛠️ 6. BỘ SCRIPT TỰ ĐỘNG HÓA CÓ SẴN TRONG THƯ MỤC LAB 7

Trong thư mục `d:\folder\rac\iuh\môn\hk1-4\quan-tri-dich-vu-mang\lab\7\`, các script đã được lập trình sẵn để bạn thực thi hoặc mang đi nộp / thực hành:

1. **`setup_xinetd_telnet.sh`**: Tự động cài `xinetd`, `telnetd`, sinh cấu hình `/etc/xinetd.d/telnet` và kích hoạt dịch vụ.
2. **`setup_openssh_security.sh`**: Tự động tạo user `testuser1`, `testuser2`, cấu hình `AllowUsers neko testuser1`, `PermitRootLogin no`.
3. **`setup_vsftpd_standalone.sh`**: Tự động cài đặt và cấu hình vsftpd ở chế độ Standalone (`anonymous_enable=NO`, `write_enable=YES`, `chroot`).
4. **`setup_vsftpd_xinetd.sh`**: Tự động chuyển đổi vsftpd sang quản lý qua Xinetd (sửa `listen=NO`, tạo `/etc/xinetd.d/vsftpd`).
5. **`test_client_lab7.sh`**: Script kiểm thử toàn bộ 3 dịch vụ (Telnet, OpenSSH, FTP) chạy trực tiếp trên Client Ubuntu_2.
6. **`win7_test_telnet_ftp.bat`**: File batch click đúp chạy trên Windows 7 để tự động test ping, port 23 và đăng nhập FTP.

---

## 💡 7. BẢNG TỔNG HỢP CÁC LỖI THƯỜNG GẶP & CÁCH XỬ LÝ (TROUBLESHOOTING)

| Lỗi gặp phải                                                                    | Nguyên nhân                                                                                                                    | Cách khắc phục triệt để                                                                                                                                                                                                       |
| :--------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`telnet: Unable to connect: Connection refused`**                        | 1. Dịch vụ Xinetd chưa chạy.2. Cờ `disable = yes` trong `/etc/xinetd.d/telnet`.                                         | 1. Chạy`sudo systemctl restart xinetd`.2. Sửa thành `disable = no` rồi restart lại xinetd.3. Kiểm tra bằng `sudo ss -tlnp \| grep :23`.                                                                                 |
| **`500 OOPS: vsftpd: refusing to run with writable root inside chroot()`** | Tính năng`chroot_local_user=YES` khóa user vào thư mục home nhưng thư mục home lại có quyền ghi.                   | Thêm dòng cấu hình sau vào`/etc/vsftpd.conf`:`allow_writeable_chroot=YES`Sau đó khởi động lại dịch vụ.                                                                                                             |
| **Lỗi cổng 21 bị xung đột: `Address already in use`**                 | Khi cấu hình vsftpd qua Xinetd nhưng quên chưa dừng dịch vụ`vsftpd` standalone, cả 2 cùng đòi lắng nghe cổng 21. | 1. Mở`/etc/vsftpd.conf`, đổi `listen=NO`.2. Chạy: `sudo systemctl stop vsftpd && sudo systemctl disable vsftpd`.3. Khởi động lại: `sudo systemctl restart xinetd`.                                                  |
| **SSH báo `Permission denied, please try again.` dù gõ đúng pass**    | User đăng nhập không nằm trong danh sách chỉ thị`AllowUsers` trong `/etc/ssh/sshd_config`.                           | Mở file`/etc/ssh/sshd_config`, thêm tên user đó vào sau chỉ thị `AllowUsers` (ví dụ: `AllowUsers neko testuser1 username_moi`) rồi chạy `sudo systemctl restart ssh`.                                           |
| **Client Windows 7 gõ lệnh `telnet` báo không nhận diện lệnh**      | Dịch vụ Telnet Client trên Windows 7 chưa được bật.                                                                      | Vào**Control Panel** -> **Programs and Features** -> **Turn Windows features on or off** -> Tích chọn **Telnet Client** -> Bấm OK. Hoặc chạy file `enable_telnet.bat` có sẵn trong thư mục lab. |

---

## 📋 8. CHECKLIST ĐÁNH GIÁ ĐẠT ĐIỂM TỐI ĐA LAB 7

* [X] **Xinetd Telnet:** Port 23 mở, hiển thị tiến trình sở hữu là `xinetd`, kết nối Telnet từ Ubuntu_2 và Win7 hiển thị shell đăng nhập thành công.
* [X] **OpenSSH Security:**
  * `testuser1` đăng nhập được.
  * `testuser2` bị từ chối truy cập.
  * `root` bị từ chối truy cập từ xa.
  * Sao chép file `scp` và `sftp` thành công.
  * Đăng nhập bằng cặp khóa SSH Key không cần nhập mật khẩu.
* [X] **VSFTPD Standalone:** Cổng 21 mở bởi `vsftpd`, đăng nhập `anonymous` bị chặn (`530 Login incorrect`), đăng nhập `testuser1` thành công, upload/download file mượt mà.
* [X] **VSFTPD Xinetd:** Dịch vụ standalone đã tắt, cổng 21 mở bởi `xinetd`, đăng nhập và truyền file qua FTP hoàn toàn trong suốt.
