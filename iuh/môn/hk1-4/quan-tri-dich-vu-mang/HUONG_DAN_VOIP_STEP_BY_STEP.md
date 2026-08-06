# HƯỚNG DẪN CẤU HÌNH HỆ THỐNG VOIP TỪ A - Z (IUH)

Tài liệu hướng dẫn từng bước (Step-by-Step) xây dựng hệ thống **Tổng đài VoIP Asterisk** trên **Ubuntu 22.04**, **2 máy ảo Windows 7 SP1 x86** và **1 Điện thoại di động thật**, đáp ứng trọn vẹn 6 yêu cầu đề bài môn Quản trị dịch vụ mạng.

---

## MỤC LỤC

1. [Bí quyết Chuẩn hóa Mạng VMware (Không bao giờ mất/đổi IP)](#1-bí-quyết-chuẩn-hóa-mạng-vmware-không-bao-giờ-mấtđổi-ip)
2. [Sơ đồ Mạng &amp; Phân bổ IP / Extension](#2-sơ-đồ-mạng--phân-bổ-ip--extension)
3. [Bước 1: Cấu hình VMware Workstation &amp; Tạo Máy Ảo Mẫu](#bước-1-cấu-hình-vmware-workstation--tạo-máy-ảo-mẫu)
4. [Bước 2: Cài đặt &amp; Cấu hình Ubuntu 22.04 (VoIP Server)](#bước-2-cài-đặt--cấu-hình-ubuntu-2204-voip-server)
5. [Bước 3: Cấu hình 2 Máy Win 7 (Softphone MicroSIP)](#bước-3-cấu-hình-2-máy-win-7-softphone-microsip)
6. [Bước 4: Cấu hình Điện thoại Di động (App Linphone)](#bước-4-cấu-hình-điện-thoại-di-động-app-linphone)
7. [Bước 5: Kịch bản Test 6 Yêu cầu Đề bài](#bước-5-kịch-bản-test-6-yêu-cầu-đề-bài)
8. [Tổng hợp Các Bước Sửa Lỗi Thường Gặp (Troubleshooting)](#8-tổng-hợp-các-bước-sửa-lỗi-thường-gặp-troubleshooting)

---

## 1. Bí quyết Chuẩn hóa Mạng VMware (Không bao giờ mất/đổi IP)

Để tránh lỗi nhảy IP khi mang laptop đến trường, ở nhà hoặc kết nối Wi-Fi khác nhau, ta sẽ **cấu hình dải mạng NAT (VMnet8) cố định dải `192.168.1.0/24`**:

1. Trên cửa sổ VMware Workstation: Chọn **Edit** -> **Virtual Network Editor...**
2. Bấm nút **Change Settings** (góc dưới bên phải để cấp quyền Admin).
3. Chọn dòng **VMnet8** (loại NAT).
4. Tại ô **Subnet IP**: Đổi thành **`192.168.1.0`**, Subnet Mask: `255.255.255.0`.
5. Bấm vào nút **NAT Settings...**:
   * Mục **Gateway IP**: Kiểm tra/đổi thành **`192.168.1.2`** (hoặc `192.168.1.1`) -> Bấm **OK**.
6. Bấm **Apply** -> **OK**.

👉 **Lợi ích**:

* Máy Ubuntu giữ cố định IP tĩnh `192.168.1.100`.
* Các máy Win 7 có IP dạng `192.168.1.x` (ví dụ `192.168.1.128`).
* Tất cả máy ảo vừa thông nhau 100%, vừa có Internet và SSH từ máy thật luôn hoạt động!

---

## 2. Sơ đồ Mạng & Phân bổ IP / Extension

```text
                        [ Laptop Máy Thật (Windows) ]
                                      │
                   ┌──────────────────┴──────────────────┐
                   │ VMware VMnet8 NAT (192.168.1.0/24)  │
                   │                                     │
         [ Ubuntu 22.04 Server ]                 [ Windows 7 - GiamDoc ]
         - Static IP: 192.168.1.100              - IP: 192.168.1.128 (hoặc tĩnh 101)
         - Dịch vụ: Asterisk PBX                 - Ext: 101 (MicroSIP)
                                                         │
                                                 [ Windows 7 - PhongKD ]
                                                 - IP: 192.168.1.129 (hoặc tĩnh 102)
                                                 - Ext: 102 (MicroSIP)
```

### Bảng phân bổ thông số:

| Thiết bị                    | Card mạng          | IP                                | Ext / Account | Mật khẩu | Vai trò                   |
| :---------------------------- | :------------------ | :-------------------------------- | :------------ | :--------- | :------------------------- |
| **Ubuntu 22.04**        | NAT (VMnet8)        | `192.168.1.100` (Tĩnh)         | Server PBX    | -          | Tổng đài Asterisk       |
| **Win 7 - Máy 1**      | NAT (VMnet8)        | `192.168.1.128` (hoặc `101`) | `101`       | `123456` | Giám đốc                |
| **Win 7 - Máy 2**      | NAT (VMnet8)        | `192.168.1.129` (hoặc `102`) | `102`       | `123456` | Phòng Kinh doanh          |
| **Điện thoại thật** | Wi-Fi Hotspot / LAN | Dải mạng kết nối              | `103`       | `123456` | Di động (App Linphone)   |
| **Số Gọi Nhóm**      | -                   | -                                 | `600`       | -          | Đổ chuông 101, 102, 103 |
| **Số Tổng đài**     | -                   | -                                 | `100`       | -          | IVR Lời chào tự động  |

---

## Bước 1: Cấu hình VMware Workstation & Tạo Máy Ảo Mẫu

### 1.1 Tạo máy ảo Ubuntu Server 22.04

1. Bật VMware Workstation -> **File** -> **New Virtual Machine** -> Chọn **Custom (advanced)**.
   ![1786018836552](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786018836552.png)
   ![1786018842117](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786018842117.png)
2. Chọn ISO `ubuntu-22.04.x-live-server-amd64.iso`.
   ![1786018852104](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786018852104.png)
   ![1786018865927](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786018865927.png)
   ![1786018872381](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786018872381.png)
3. Đặt thông số phần cứng:

   * **RAM**: `2048 MB` (2GB).
     ![1786018896427](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786018896427.png)
   * **Processors**: `1 Processor`, `1 Core`.
     ![1786018892228](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786018892228.png)
   * **Network Connection**: Chọn **NAT** (Dùng dải mạng NAT VMnet8).
     ![1786018909934](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786018909934.png)
   * **Disk**: `20 GB`.
     ![1786018969688](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786018969688.png)

### 1.2 Tạo máy ảo Windows 7 SP1 x86 (Master Image)

1. Tạo máy ảo Win 7 với ISO `Windows 7 Professional SP1 32-bit (x86)`.
2. Thông số phần cứng:
   * **RAM**: `1024 MB` (1GB).
   * **Processors**: `1 Processor`, `1 Core`.
   * **Network**: Chọn **NAT**.
   * **Disk**: `20 GB`.
3. Cài xong Win 7  -> Tắt máy ảo Win 7.
4. **TẠO SNAPSHOT BẢN SẠCH**:
   * Chuột phải máy ảo Win 7 gốc -> **Snapshot** -> **Take Snapshot**.
   * Đặt tên: `00_CLEAN_BASE`. (Snapshot này giữ nguyên để dùng lại cho các môn học khác).

### 1.3 Tạo 2 máy Win 7 cho bài VoIP bằng Linked Clone

1. Chuột phải máy Win 7 gốc -> **Manage** -> **Clone**.
2. Chọn **An existing snapshot** -> Chọn `00_CLEAN_BASE`.
3. Chọn **Create a linked clone**.
4. Đặt tên máy 1: `Win7_GiamDoc`.
5. Làm tương tự tạo máy 2: `Win7_PhongKD`.

---

## Bước 2: Cài đặt & Cấu hình Ubuntu 22.04 (VoIP Server)

### 2.1 Đặt IP tĩnh cho Ubuntu

Mở Terminal trên Ubuntu 22.04 và sửa file netplan:

```bash
sudo nano /etc/netplan/00-installer-config.yaml
```



![1786024108125](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786024108125.png)Cấu hình IP chuẩn theo dải mạng VMnet8 NAT:

```yaml
network:
  version: 2
  ethernets:
    ens33: # (Thay bằng tên card mạng của bạn, check bằng `ip a`)
      dhcp4: no
      addresses:
        - 192.168.1.100/24
      routes:
        - to: default
          via: 192.168.1.2
      nameservers:
        addresses: [8.8.8.8, 1.1.1.1]
```

Áp dụng cấu hình:

```bash
sudo netplan apply
```

### 2.2 Chạy Script tự động cài đặt Asterisk

1. Copy file `setup_voip_ubuntu.sh` vào Ubuntu (hoặc dùng SSH / SCP từ máy thật).![1786024140666](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786024140666.png)
2. Phân quyền và chạy script:

```bash
chmod +x setup_voip_ubuntu.sh
sudo bash setup_voip_ubuntu.sh
```

### 2.3 Cấu hình Gmail để gửi cuộc gọi nhỡ (Yêu cầu 5)

1. Mở tài khoản Gmail -> **Quản lý Tài khoản Google** -> **Bảo mật** -> Bật **Xác minh 2 bước**.
   ![1786019907879](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786019907879.png)
   ![1786019936986](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786019936986.png)
2. Tạo **Mật khẩu ứng dụng (App Password)** cho Mail.
   ![1786020018335](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786020018335.png)
   ![1786020022981](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786020022981.png)
   ![1786020514567](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786020514567.png)
   ![1786020518014](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786020518014.png)
3. Trên Ubuntu, mở file `/etc/msmtprc`:

```bash
sudo nano /etc/msmtprc
```

Điền Gmail và App Password của bạn vào:

```ini
user       email_cua_ban@gmail.com
password   xxxx xxxx xxxx xxxx  # (Mật khẩu ứng dụng 16 ký tự)
```

Vào `/etc/asterisk/voicemail.conf` sửa email người nhận ở dòng `101`:

```ini
101 => 1234,Giam Doc,email_giamdoc_nhan_mail@gmail.com
```

Khởi động lại Asterisk: `sudo systemctl restart asterisk`.

---

## Bước 3: Cấu hình 2 Máy Win 7 (Softphone MicroSIP)

1. Mở máy ảo `Win7_GiamDoc` và `Win7_PhongKD`.
   ![1786023186525](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786023186525.png)
   ![1786023196056](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786023196056.png)
2. Kiểm tra IP bằng `cmd` -> `ipconfig` (đảm bảo ở dải `192.168.1.x`).
3. Mở **MicroSIP** -> Bấm dấu mũi tên ở góc trên bên phải -> Chọn **Add Account...**:

#### Đăng ký cho máy Win7_GiamDoc:

* **Account Name**: Giám đốc
* **SIP Server**: `192.168.1.100` (IP máy Ubuntu)
* **User**: `101`
* **Domain**: `192.168.1.100`
* **Password**: `123456`
* Bấm **Save**. Trạng thái hiển thị **Online** là thành công!

#### Đăng ký cho máy Win7_PhongKD:

* Làm tương tự với **User**: `102`, **Password**: `123456`.

---

## Bước 4: Cấu hình Điện thoại Di động (App Linphone)

1. Đảm bảo điện thoại di động kết nối **cùng mạng Wi-Fi** hoặc **Hotspot** của laptop.
2. Tải app **Linphone** (Miễn phí 100%, Mã nguồn mở) từ App Store hoặc CH Play.
3. Mở app **Linphone** -> Chọn **USE SIP ACCOUNT**:
   * **Username**: `103`
   * **SIP Domain**: `192.168.1.100` (Địa chỉ IP máy Ubuntu)
   * **Password**: `123456`
   * **Transport**: Chọn **UDP**
4. Bấm **LOGIN**. Đợi màn hình hiển thị chấm xanh **Connected** là hoàn tất!

---

## Bước 5: Kịch bản Test 6 Yêu cầu Đề bài

Dưới đây là thứ tự test từng yêu cầu để thực hiện báo cáo demo với giáo viên:

| STT         | Yêu cầu đề bài                  | Thao tác thực hiện Test                                                                                                          | Kết quả mong đợi                                                                                                                                                  |
| :---------- | :----------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | **Gọi nhóm**                 | Từ máy`101`, bấm gọi số **`600`**.                                                                                   | Cả máy Win7 (`102`) và Điện thoại Linphone (`103`) đồng thời đổ chuông. Máy nào nhấc máy trước sẽ bắt đàm thoại.                           |
| **2** | **Gọi Di động**             | Từ Win7`101` bấm gọi số **`103`**.                                                                                    | App Linphone trên điện thoại di động reo chuông, nhấc máy nghe rõ âm thanh 2 chiều.                                                                       |
| **3** | **Nhắn tin**                  | Trên MicroSIP (máy`101`), mở tab **Messages**, gõ nhắn tới `103`.                                                   | App Linphone (`103`) nhận được tin nhắn POP-UP hiển thị nội dung tin nhắn.                                                                                 |
| **4** | **Chặn cuộc gọi**           | **Lượt 1**: Từ Giám đốc (`101`) gọi `102`.**Lượt 2**: Từ Phòng KD (`102`) gọi Giám đốc (`101`).  | - Lượt 1: Gọi bình thường.- Lượt 2: Cuộc gọi bị **CHẶN** ngay lập tức, nghe tiếng báo không dịch vụ (`ss-noservice`) và ngắt cuộc gọi. |
| **5** | **Gửi Gmail cuộc gọi nhỡ** | Từ`102` gọi `101`, máy `101` không nghe máy. Sau 20 giây chuyển qua Voicemail. Nói 1 đoạn âm thanh rồi dúp máy. | Asterisk tự động gửi 1 Email kèm file ghi âm`.wav` đến địa chỉ Gmail đã cấu hình.                                                                    |
| **6** | **Gọi Tổng đài (IVR)**     | Từ bất kỳ máy nào bấm gọi số**`100`**.                                                                              | Nghe lời chào tự động: Bấm phím`1` cuộc gọi tự chuyển sang Giám đốc (`101`), bấm phím `2` chuyển sang Phòng KD (`102`).                     |

---

## 8. Tổng hợp Các Bước Sửa Lỗi Thường Gặp (Troubleshooting)

### 🔴 Lỗi 1: Màn hình Ubuntu treo ở bước "Rebooting..." khi cài xong

* **Khắc phục**: Click chuột vào máy ảo nhấn phím **ENTER**. Nếu không được, chọn menu VMware: **VM** -> **Power** -> **Restart Guest** (Reset).

### 🔴 Lỗi 2: Bị lỗi `Temporary failure resolving 'vn.archive.ubuntu.com'` hoặc không có Internet (Mạng Trường)

* **Nguyên nhân**: Mạng Wi-Fi trường bắt đăng nhập web, máy ảo Bridged bị chặn.
* **Khắc phục**:
  1. Đổi Card mạng trên VMware sang **NAT**.
  2. Trên Ubuntu gõ lệnh thêm DNS Google:
     ```bash
     echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
     ```

### 🔴 Lỗi 3: Báo lỗi `file:/cdrom jammy Release` chữ màu đỏ khi `apt update`

* **Khắc phục**: Gõ lệnh ẩn ổ đĩa CDROM ảo:
  ```bash
  sudo sed -i 's/^deb cdrom/# deb cdrom/' /etc/apt/sources.list
  ```

### 🔴 Lỗi 4: Không SSH được từ máy thật vào Ubuntu (`Connection timed out` / `Connection refused`)

* **Khắc phục**:
  1. Đảm bảo trên Ubuntu đã bật SSH: `sudo apt install openssh-server -y`.
  2. Kiểm tra dải IP máy thật và máy Ubuntu đã cùng dải `192.168.1.x` chưa.
  3. Lệnh SSH chuẩn từ PowerShell máy thật: `ssh neko@192.168.1.100`.

### 🔴 Lỗi 5: Đẩy file script `setup_voip_ubuntu.sh` từ máy thật sang Ubuntu cực nhanh

* **Cách làm**: Mở PowerShell trên máy thật gõ lệnh SCP:
  ```powershell
  scp "d:\folder\rac\iuh\môn\hk1-4\quan-tri-dich-vu-mang\setup_voip_ubuntu.sh" neko@192.168.1.100:~/
  ```

---

*Chúc bạn hoàn thành xuất sắc bài báo cáo demo môn Quản trị dịch vụ mạng!*
