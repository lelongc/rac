# BÁO CÁO TRẠNG THÁI HỆ THỐNG 4 MÁY ÁO LAB GIỮA KỲ (GK-QTDVM)

**Thời gian cập nhật:** 09/10/2026  
**Trạng thái toàn hệ thống:** 🟢 **100% SẴN SÀNG CHO KỲ THI (ALL READY)**

---

## 1. SƠ ĐỒ ĐỊA CHỈ IP & THÔNG TIN TRUY CẬP

| Máy Áo | Hệ Điều Hành | Vai Trò | IP NAT (Quản trị SSH/Host) | IP Mạng LAB | Tài Khoản / Mật Khẩu | Trạng Thái Kết Nối |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **`gk-ubuntu-1`** | Ubuntu 22.04 LTS | Router / Server Chính | `192.168.1.150` | `192.168.5.2` (LAN 1)<br>`192.168.6.3` (LAN 2) | `neko` / `conmeo`<br>Sudo: `conmeo` | 🟢 SSH & Ping OK (<1ms) |
| **`gk-ubuntu-2`** | Ubuntu 22.04 LTS | Client / Sub-Server | `192.168.1.151` | `192.168.6.2` (LAN 2) | `neko` / `conmeo`<br>Sudo: `conmeo` | 🟢 SSH & Ping OK (<1ms) |
| **`gk-win7-1`** | Windows 7 Ultimate | Client LAN 1 | N/A | `192.168.5.11` (LAN 1) | N/A | 🟢 Ping & Telnet Port 23 OK |
| **`gk-win7-2`** | Windows 7 Ultimate | Client LAN 2 | N/A | `192.168.6.10` (LAN 2) | N/A | 🟢 Ping & Telnet Port 23 OK |

---

## 2. DANH SÁCH CÁC GÓI PHẦN MỀM ĐÃ TẢI SẴN (PRE-INSTALLED PACKAGES)

Tất cả các gói cần thiết cho các bài thi môn **Quản trị dịch vụ mạng (IUH)** đã được tải và cài đặt sẵn trên ổ đĩa máy ảo. **Không cần tốn thời gian tải gói khi đi thi.**

### 🖥️ Máy Server `gk-ubuntu-1`
- **DNS Server**: `bind9`, `dnsutils` (`dig`, `nslookup`), `bind9utils`
- **DHCP Server**: `isc-dhcp-server`
- **Samba File Sharing**: `samba`
- **NFS Storage**: `nfs-kernel-server`
- **Web Apache & SSL**: `apache2`
- **FTP Server**: `vsftpd`
- **Telnet & Remote Service**: `xinetd`, `telnetd`, `openssh-server`
- **Công cụ Mạng & Debug**: `net-tools` (`ifconfig`), `traceroute`, `curl`, `sshpass`

### 💻 Máy Client `gk-ubuntu-2`
- **DNS Lookup Client**: `dnsutils`, `bind9utils`
- **Samba Client**: `smbclient`, `cifs-utils`
- **NFS Client**: `nfs-common`
- **FTP & Telnet Client**: `ftp`, `telnet`
- **SSH Service**: `openssh-server`, `openssh-client`, `sshpass`
- **Công cụ Mạng**: `net-tools`, `traceroute`, `curl`

---

## 3. TRẠNG THÁI FILE CẤU HÌNH (CONFIG FILES)

Tất cả các file cấu hình dịch vụ đã được đưa về **trạng thái mặc định sạch 100% (Clean State)** để sẵn sàng cấu hình mới theo yêu cầu đề thi:

- 🟢 `/etc/bind/named.conf.local`: File trắng, sẵn sàng khai báo Zone DNS.
- 🟢 `/etc/dhcp/dhcpd.conf`: File mẫu mặc định, đã khai báo sẵn dải IP cơ bản.
- 🟢 `/etc/exports`: File trống, sẵn sàng khai báo thư mục chia sẻ NFS.
- 🟢 `/etc/samba/smb.conf`: Template Samba gốc, sẵn sàng khai báo `[share]`.
- 🟢 `/etc/vsftpd.conf`: Template VSFTPD gốc.
- 🟢 `/var/www/html/`: Có sẵn file tự động hóa `enable_telnet.bat`.

---

## 4. QUY TRÌNH HỖ TRỢ KHI ĐI THI

1. **Khởi động 4 máy ảo** trong VMware.
2. **Gửi đề thi** qua chat.
3. **AI sẽ tự động SSH vào 2 máy Ubuntu** để cấu hình toàn bộ các dịch vụ theo đề thi (DNS, DHCP, Samba, NFS, Web SSL, FTP...).
4. Trên 2 máy **Windows 7**, mở `cmd` gõ `ipconfig /renew` hoặc các lệnh test giao diện theo hướng dẫn.
