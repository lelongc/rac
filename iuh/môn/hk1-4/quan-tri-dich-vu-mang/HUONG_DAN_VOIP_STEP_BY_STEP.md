# HƯỚNG DẪN CẤU HÌNH HỆ THỐNG VOIP TỪ A - Z (IUH)

Tài liệu hướng dẫn từng bước (Step-by-Step) xây dựng hệ thống **Tổng đài VoIP Asterisk** trên **Ubuntu 22.04**, **2 máy ảo Windows 7 SP1 x86** và **1 Điện thoại di động thật**, đáp ứng trọn vẹn 6 yêu cầu đề bài môn Quản trị dịch vụ mạng.

---

## MỤC LỤC

1. [Sơ đồ Mạng &amp; Phân bổ IP / Extension](#1-sơ-đồ-mạng--phân-bổ-ip--extension)
2. [Bước 1: Cấu hình VMware Workstation &amp; Tạo Máy Ảo Mẫu](#bước-1-cấu-hình-vmware-workstation--tạo-máy-ảo-mẫu)
3. [Bước 2: Cài đặt &amp; Cấu hình Ubuntu 22.04 (VoIP Server)](#bước-2-cài-đặt--cấu-hình-ubuntu-2204-voip-server)
4. [Bước 3: Cấu hình 2 Máy Win 7 (Softphone MicroSIP)](#bước-3-cấu-hình-2-máy-win-7-softphone-microsip)
5. [Bước 4: Cấu hình Điện thoại Di động (App Zoiper / GS Wave)](#bước-4-cấu-hình-điện-thoại-di-động-app-zoiper--gs-wave)
6. [Bước 5: Kịch bản Test 6 Yêu cầu Đề bài](#bước-5-kịch-bản-test-6-yêu-cầu-đề-bài)

---

## 1. Sơ đồ Mạng & Phân bổ IP / Extension

```text
                        [ Router Wi-Fi / LAN Nhà / Trường ]
                                        │
             ┌──────────────────────────┼──────────────────────────┐
             │ Bridged                  │ Bridged                  │ Wi-Fi cùng dải
   [ Ubuntu 22.04 Server ]     [ Windows 7 - GiamDoc ]    [ Điện thoại Di Động ]
   - Static IP: 192.168.1.100  - Ext: 101                 - Ext: 103 (App Zoiper)
   - Dịch vụ: Asterisk PBX     - MicroSIP               
                                        │ Bridged
                               [ Windows 7 - PhongKD ]
                               - Ext: 102
                               - MicroSIP
```

### Bảng phân bổ thông số:

| Thiết bị                    | Card mạng | IP                          | Ext / Account | Mật khẩu | Vai trò                   |
| :---------------------------- | :--------- | :-------------------------- | :------------ | :--------- | :------------------------- |
| **Ubuntu 22.04**        | Bridged    | `192.168.1.100` (Ví dụ) | Server PBX    | -          | Tổng đài Asterisk       |
| **Win 7 - Máy 1**      | Bridged    | DHCP (Cùng dải)           | `101`       | `123456` | Giám đốc                |
| **Win 7 - Máy 2**      | Bridged    | DHCP (Cùng dải)           | `102`       | `123456` | Phòng Kinh doanh          |
| **Điện thoại thật** | Wi-Fi      | DHCP (Cùng dải)           | `103`       | `123456` | Di động                  |
| **Số Gọi Nhóm**      | -          | -                           | `600`       | -          | Đổ chuông 101, 102, 103 |
| **Số Tổng đài**     | -          | -                           | `100`       | -          | IVR Lời chào tự động  |

---

## Bước 1: Cấu hình VMware Workstation & Tạo Máy Ảo Mẫu

### 1.1 Tạo máy ảo Ubuntu Server 22.04

1. Bật VMware Workstation -> **File** -> **New Virtual Machine** -> Chọn **Custom (advanced)**.![1786018836552](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786018836552.png)![1786018842117](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786018842117.png)
2. Chọn ISO `ubuntu-22.04.x-live-server-amd64.iso`.![1786018852104](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786018852104.png)
3. Đặt thông số phần cứng:

   * **RAM**: `2048 MB` (2GB).![1786018896427](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786018896427.png)
   * **Processors**: `1 Processor`, `1 Core`.![1786018892228](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786018892228.png)
   * **Network Connection**: **Use bridged networking** (bước này để nat , cài xong ubuntu kèm ip rồi mới chỉnh lại thành bridge).![1786018909934](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786018909934.png)
   * **Disk**: `20 GB`.![1786018969688](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786018969688.png)

### 1.2 Tạo máy ảo Windows 7 SP1 x86 (Master Image)

1. Tạo máy ảo Win 7 với ISO `Windows 7 SP1 32-bit (x86)`.
2. Thông số phần cứng:
   * **RAM**: `1024 MB` (1GB).
   * **Processors**: `1 Processor`, `1 Core`.
   * **Network**: **Use bridged networking**.(bước này để nat , cài xong ip rồi mới chỉnh lại thành bridge
   * **Disk**: `20 GB`.
3. Cài xong Win 7 -> Cài **VMware Tools** -> Tắt máy ảo Win 7.
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

Cấu hình IP (thay `192.168.1.100` theo dải mạng Wi-Fi/LAN của bạn):

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
          via: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 1.1.1.1]
```

Áp dụng cấu hình:

```bash
sudo netplan apply
```

### 2.2 Chạy Script tự động cài đặt Asterisk

1. Copy file `setup_voip_ubuntu.sh` vào Ubuntu (hoặc tạo file mới `nano setup_voip_ubuntu.sh` rồi dán nội dung vào).
2. Phân quyền và chạy script:

```bash
chmod +x setup_voip_ubuntu.sh
sudo bash setup_voip_ubuntu.sh
```

### 2.3 Cấu hình Gmail để gửi cuộc gọi nhỡ (Yêu cầu 5)

1. Mở tài khoản Gmail -> **Quản lý Tài khoản Google** -> **Bảo mật** -> Bật **Xác minh 2 bước**.![1786019907879](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786019907879.png)![1786019936986](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786019936986.png)
2. Tạo **Mật khẩu ứng dụng (App Password)** cho Mail.![1786020018335](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786020018335.png)![1786020022981](image/HUONG_DAN_VOIP_STEP_BY_STEP/1786020022981.png)
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
2. Tải bản **MicroSIP Portable** (hoặc copy từ máy thật vào qua Shared Folder / Drag & Drop).
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

## Bước 4: Cấu hình Điện thoại Di động (App Zoiper / GS Wave)

1. Đảm bảo điện thoại di động kết nối **cùng mạng Wi-Fi** với máy thật.
2. Lên App Store (iOS) hoặc CH Play (Android) tải app **Zoiper** (hoặc **Grandstream Wave** / **Linphone**).
3. Mở Zoiper -> Chọn **Accounts** -> **Add Account** -> Chọn **SIP Account**:
   * **Account Name**: Di dong 103
   * **Host / Domain**: `192.168.1.100`
   * **Username**: `103`
   * **Password**: `123456`
4. Bấm **Save / Register**. Đợi báo **OK / Registration State: OK**.

---

## Bước 5: Kịch bản Test 6 Yêu cầu Đề bài

Dưới đây là thứ tự test từng yêu cầu để thực hiện báo cáo demo với giáo viên:

| STT         | Yêu cầu đề bài                  | Thao tác thực hiện Test                                                                                                          | Kết quả mong đợi                                                                                                                                                  |
| :---------- | :----------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | **Gọi nhóm**                 | Từ máy`101`, bấm gọi số **`600`**.                                                                                   | Cả máy Win7 (`102`) và Điện thoại (`103`) đồng thời đổ chuông. Máy nào nhấc máy trước sẽ bắt đàm thoại.                                    |
| **2** | **Gọi Di động**             | Từ Win7`101` bấm gọi số **`103`**.                                                                                    | App Zoiper trên điện thoại di động reo chuông, nhấc máy nghe rõ âm thanh 2 chiều.                                                                         |
| **3** | **Nhắn tin**                  | Trên MicroSIP (máy`101`), mở tab **Messages**, gõ nhắn tới `103`.                                                   | Điện thoại di động (`103`) nhận được tin nhắn POP-UP hiển thị nội dung tin nhắn.                                                                      |
| **4** | **Chặn cuộc gọi**           | **Lượt 1**: Từ Giám đốc (`101`) gọi `102`.**Lượt 2**: Từ Phòng KD (`102`) gọi Giám đốc (`101`).  | - Lượt 1: Gọi bình thường.- Lượt 2: Cuộc gọi bị **CHẶN** ngay lập tức, nghe tiếng báo không dịch vụ (`ss-noservice`) và ngắt cuộc gọi. |
| **5** | **Gửi Gmail cuộc gọi nhỡ** | Từ`102` gọi `101`, máy `101` không nghe máy. Sau 20 giây chuyển qua Voicemail. Nói 1 đoạn âm thanh rồi dúp máy. | Asterisk tự động gửi 1 Email kèm file ghi âm`.wav` đến địa chỉ Gmail đã cấu hình.                                                                    |
| **6** | **Gọi Tổng đài (IVR)**     | Từ bất kỳ máy nào bấm gọi số**`100`**.                                                                              | Nghe lời chào tự động: Bấm phím`1` cuộc gọi tự chuyển sang Giám đốc (`101`), bấm phím `2` chuyển sang Phòng KD (`102`).                     |

---

*Chúc bạn hoàn thành xuất sắc bài báo cáo demo môn Quản trị dịch vụ mạng!*
