1. [CÂU 1: NGUYÊN LÝ HOẠT ĐỘNG CÁC DỊCH VỤ CƠ BẢN (DHCP, DNS, SAMBA, NFS, FTP, WEB)](#câu-1-nguyên-lý-hoạt-động-các-dịch-vụ-cơ-bản)
2. [CÂU 2: GIẢI PHÁP WEB SERVER VÀ HỆ THỐNG THƯ ĐIỆN TỬ (EMAIL)](#câu-2-giải-pháp-web-server-và-hệ-thống-thư-điện-tử-email)
3. [CÂU 3: BÀI TOÁN CÔNG TY ABC (DHCP VÀ DHCP RELAY AGENT)](#câu-3-bài-toán-công-ty-abc-dhcp-và-dhcp-relay-agent)

- *3a. Sơ đồ mô hình mạng & Phân bổ IP*
- *3b. Giải pháp & Nguyên lý
- *3c. Mô tả quá trình cài đặt & triển khai* 

4. [CÂU 4: DỊCH VỤ VOIP (VOICE OVER IP)](#câu-4-dịch-vụ-voip-voice-over-ip)
5. [CÂU 5: DỊCH VỤ HTTPS &amp; CERTIFICATE SERVER (CA)](#câu-5-dịch-vụ-https--certificate-server-ca)
6. [BẢNG TRA CỨU NHANH CỔNG (PORT CHEAT-SHEET)](#bảng-tra-cứu-nhanh-cổng-port-cheat-sheet)

---

# CÂU 1: NGUYÊN LÝ HOẠT ĐỘNG CÁC DỊCH VỤ CƠ BẢN

### 1. Dịch vụ DHCP (Dynamic Host Configuration Protocol)

* **Vai trò:** Tự động cấp phát địa chỉ IP, Subnet Mask, Gateway, DNS cho máy trạm, chống trùng IP, quản lý tập trung.
* **Cổng giao thức:** **UDP 67** (Server/Relay lắng nghe), **UDP 68** (Client nhận).
* **Nguyên lý hoạt động (Chu trình DORA 4 bước):**
  1. `DHCP Discover` (Client Broadcast `255.255.255.255` tìm Server).
  2. `DHCP Offer` (Server đề nghị cấp IP, Mask, Lease Time).
  3. `DHCP Request` (Client Broadcast chấp nhận IP của Server đã chọn).
  4. `DHCP ACK` (Server xác nhận cấp phát, chính thức áp dụng).
* **Cơ chế gia hạn thuê (Lease Renewal):**
  * Tại **T1 = 50% thời gian thuê:** Client gửi Unicast `DHCP Request` xin gia hạn trực tiếp với Server ban đầu.
  * Tại **T2 = 87.5% thời gian thuê:** Client gửi Broadcast `DHCP Request` xin gia hạn với bất kỳ Server nào.
  * Hết **100% thời gian:** Nhả IP (`DHCP Release`) và xin lại từ đầu.

### 2. Dịch vụ DNS (Domain Name System)

* **Vai trò:** Phân giải tên miền (FQDN) thành địa chỉ IP (phân giải thuận) và ngược lại (phân giải nghịch).
* **Cổng giao thức:** **UDP 53** (truy vấn nhanh bình thường), **TCP 53** (chuyển vùng Zone Transfer hoặc gói tin > 512 bytes).
* **Nguyên lý hoạt động:**
  * **Cây phân cấp tên miền:** Root (`.`) $\rightarrow$ TLD (`.vn`, `.com`) $\rightarrow$ SLD (`iuh.edu.vn`) $\rightarrow$ Subdomain (`fit.iuh.edu.vn`).
  * **Truy vấn Đệ quy (Recursive):** Client hỏi Local DNS, Local DNS tìm đến cùng để trả kết quả cho Client.
  * **Truy vấn Tương tác (Iterative):** Local DNS hỏi lần lượt Root $\rightarrow$ TLD $\rightarrow$ Authoritative DNS.
* **Các bản ghi quan trọng:**
  * `A` (Hostname sang IPv4), `AAAA` (IPv6), `CNAME` (Bí danh Alias), `MX` (Máy chủ Mail), `PTR` (Phân giải nghịch từ IP ra tên miền), `NS` (Máy chủ Name Server), `SOA` (Bản ghi quản trị vùng).

### 3. Dịch vụ SAMBA (SMB/CIFS)

* **Vai trò:** Chia sẻ file và máy in tương thích đa nền tảng giữa Linux và Windows.
* **Cổng giao thức:** **TCP 445** (SMB trực tiếp), **TCP 139** & **UDP 137, 138** (NetBIOS cũ).
* **Tiến trình:** `smbd` (xử lý chia sẻ file, xác thực, phân quyền), `nmbd` (phân giải tên NetBIOS và duyệt mạng).
* **Nguyên lý phân quyền:** Quyền thực tế là giao điểm chặt nhất giữa **Quyền chia sẻ Samba** (trong `/etc/samba/smb.conf`) và **Quyền hệ thống tệp Linux** (`chmod`, `chown`).
* **Share ẩn:** Thêm dấu `$` vào sau tên thư mục chia sẻ (ví dụ `teacher$`) $\rightarrow$ Windows Explorer sẽ ẩn đi, bắt buộc gõ đúng đường dẫn UNC `\\IP\teacher$` mới vào được.

### 4. Dịch vụ NFS (Network File System)

* **Vai trò:** Gắn kết (mount) thư mục chia sẻ từ máy chủ Linux/Unix từ xa về máy cục bộ với tốc độ cao.
* **Cổng giao thức:** **TCP/UDP 2049** (NFS Server), **TCP/UDP 111** (dịch vụ `rpcbind` điều hướng RPC).
* **Tùy chọn cấu hình xuất khẩu (`/etc/exports`):**
  * `rw` (Đọc/Ghi), `ro` (Chỉ đọc), `sync` (Ghi đồng bộ an toàn dữ liệu), `no_subtree_check` (Tăng tốc độ truyền).
  * `root_squash` (Hạ quyền root từ xa thành user `nobody` để bảo vệ server), `no_root_squash` (Giữ quyền root).

### 5. Dịch vụ FTP (File Transfer Protocol)

* **Vai trò:** Truyền tải tệp tin dung lượng lớn giữa client và server.
* **Cổng & 2 kênh tách biệt:**
  * **Kênh Điều khiển (Control):** Cổng **TCP 21** (luôn mở để gửi lệnh và phản hồi trạng thái).
  * **Kênh Dữ liệu (Data):** Cổng **TCP 20** (Active) hoặc **Port ngẫu nhiên** (Passive Mode).
* **Active vs Passive Mode:**
  * **Active Mode:** Client mở port $N$, Server chủ động mở cổng TCP 20 nối vào port $N+1$ của Client (dễ bị Firewall/NAT của Client chặn).
  * **Passive Mode (PASV):** Client kết nối vào port ngẫu nhiên mà Server mở ra (vượt Firewall/NAT hoàn hảo).
* **Bảo mật:** Bật `chroot_local_user=YES` để "giam" người dùng trong thư mục cá nhân, cấm `anonymous_enable=NO`.

### 6. Dịch vụ Web (HTTP / HTTPS)

* **Vai trò:** Phân phối nội dung trang web/ứng dụng cho người dùng qua trình duyệt.
* **Cổng giao thức:** **TCP 80** (HTTP plain-text không mã hóa), **TCP 443** (HTTPS mã hóa TLS/SSL).
* **Cơ chế Virtual Host:** Chạy nhiều website trên 1 Server qua: Name-based (dựa vào domain request header), IP-based (mỗi web 1 IP), Port-based (mỗi web 1 port).

---

# CÂU 2: GIẢI PHÁP WEB SERVER VÀ HỆ THỐNG THƯ ĐIỆN TỬ (EMAIL)

### 2a. Lựa chọn giải pháp Web Server cho Công ty ABC

* **4 giải pháp xem xét:**
  1. *On-Premises (Đặt server tại văn phòng):* Tốn kém phần cứng, cần đường mạng IP tĩnh đắt, rủi ro mất điện/mạng.
  2. *Dedicated Server (Thuê server riêng ở Data Center):* Hiệu năng cao nhưng giá đắt (vài triệu/tháng), lãng phí công suất cho web công ty.
  3. *Cloud VPS (Thuê máy chủ ảo đám mây):* **TỐI ƯU NHẤT**.
  4. *Shared Hosting:* Rẻ nhưng dùng chung với web khác, giới hạn tính năng, dễ bị hack lây chéo.
* **CHỌN:** **Thuê Cloud VPS tại Data Center trong nước (Viettel, VNPT, FPT, PA Việt Nam).**
* **Lý do chọn:**
  * Tiết kiệm chi phí đầu tư ban đầu, giá thuê hợp lý (~150k - 300k/tháng).
  * Uptime cao $\ge 99.9\%$, có IP tĩnh riêng, tốc độ truy cập trong nước nhanh.
  * Toàn quyền cấu hình OS, cài đặt Web Server, bật SSL miễn phí (Let's Encrypt).
  * Dễ dàng nâng cấp CPU/RAM trong vài phút khi lượng truy cập tăng.
* **Ưu điểm & Nhược điểm:**
  * *Ưu điểm:* Độc lập tài nguyên, IP riêng, linh hoạt cấu hình, chi phí thấp, có snapshot sao lưu tự động.
  * *Nhược điểm:* Cần nhân viên IT biết quản trị hệ thống Linux/Windows để cài đặt và bảo mật.

---

### 2b. Các bước triển khai Web Server thực tế

1. **Thuê VPS:** Mua gói Cloud VPS (OS Ubuntu 22.04 LTS), nhận địa chỉ IP Public (VD: `203.162.10.50`).
2. **Cấu hình DNS `abc.com.vn`:**
   * Bản ghi `A`: host `@` $\rightarrow$ trỏ về IP `203.162.10.50`.
   * Bản ghi `CNAME`: host `www` $\rightarrow$ trỏ về `abc.com.vn`.
3. **Cài đặt Web Server:** Cài Nginx (`sudo apt install nginx`), tạo Virtual Host trỏ thư mục gốc `/var/www/abc.com.vn/html`.
4. **Upload mã nguồn & Phân quyền:** Đưa mã nguồn web lên thư mục qua SFTP, cấp quyền: `chown -R www-data:www-data`, thư mục `755`, tệp `644`.
5. **Cài chứng chỉ SSL/TLS:** Dùng Certbot cấp chứng chỉ Let's Encrypt miễn phí (`certbot --nginx -d abc.com.vn -d www.abc.com.vn`), tự động chuyển hướng HTTP sang HTTPS.
6. **Mở Firewall:** Cho phép port `22`, `80`, `443` trên UFW $\rightarrow$ Kiểm tra truy cập `https://abc.com.vn`.

---

### 2c. Sơ đồ hệ thống thư điện tử (Mail Server) & Giải thích

```text
[ Người gửi: MUA ] 
       | (SMTP: 587/465)
       v
[ Máy chủ gửi: MTA ] ----(Tra cứu MX qua DNS)----> [ DNS Internet ]
       |                                                    | (Trả về IP Mail Server nhận)
       | (SMTP: 25 qua Internet)                            v
       +---------------------------------------------> [ Máy chủ nhận: MTA ]
                                                               |
                                                               v
                                                       [ Phân phối: MDA ]
                                                               |
                                                               v
                                                     [ Hộp thư /var/mail ]
                                                               |
                                                       (POP3: 995 / IMAP: 993)
                                                               v
                                                       [ Người nhận: MUA ]
```

* **Các thành phần trong sơ đồ:**
  * **MUA (Mail User Agent):** Ứng dụng đọc/gửi mail của người dùng (Outlook, Thunderbird, Webmail).
  * **MTA (Mail Transfer Agent):** Máy chủ vận chuyển thư qua mạng Internet bằng giao thức **SMTP (port 25)** (Postfix, Sendmail, Exchange).
  * **MDA (Mail Delivery Agent):** Tiếp nhận thư từ MTA và phân phối ghi vào hộp thư cục bộ của người dùng (Dovecot LDA).
  * **Hộp thư (Mailbox):** Nơi lưu trữ thư trên ổ cứng Server (chuẩn `Maildir` - mỗi thư 1 file, hoặc `Mbox`).
  * **Giao thức đọc thư (POP3/IMAP):** Dovecot cung cấp để MUA tải/đọc thư.
  * **Bản ghi DNS Mail:**
    * `MX` (Mail Exchanger): Chỉ định IP máy chủ nhận mail của tên miền.
    * `SPF`, `DKIM`, `DMARC`: Xác thực chống giả mạo email và chống spam.
    * `PTR`: Phân giải nghịch xác thực IP máy chủ gửi thư hợp lệ.

---

### 2d. So sánh giao thức POP (POP3) và IMAP

| Tiêu chí                        | Giao thức POP (POP3)                                                                                  | Giao thức IMAP                                                                                                       |
| :-------------------------------- | :----------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| **Cơ chế hoạt động**   | **Tải về cục bộ (Download & Store):** Tải thư về máy rồi mặc định xóa trên Server. | **Đồng bộ hai chiều (Two-way Sync):** Thư lưu trữ tập trung trên Server, client đồng bộ hiển thị. |
| **Cổng kết nối**         | Cổng thường: **TCP 110** \| Cổng mã hóa SSL: **TCP 995**                             | Cổng thường: **TCP 143** \| Cổng mã hóa SSL: **TCP 993**                                            |
| **Hỗ trợ đa thiết bị** | **Kém:** Tải về máy này thì máy khác không thấy thư nữa.                             | **Rất tốt:** Đọc/xóa trên điện thoại thì máy tính tự cập nhật theo.                              |
| **Quản lý thư mục**     | Chỉ tải hộp thư đến (**Inbox**), không tạo/đồng bộ được thư mục con.             | Đồng bộ toàn bộ cây thư mục (Sent, Draft, Trash, thư mục tự tạo).                                         |
| **Dung lượng Server**     | Tốn rất ít dung lượng Server.                                                                     | Đòi hỏi Server phải có dung lượng lưu trữ lớn.                                                              |
| **Khi nào sử dụng?**     | Dùng duy nhất 1 máy tính cố định, dung lượng hòm thư ít.                                   | Người dùng hiện đại dùng đồng thời cả Laptop và Điện thoại.                                            |

---

# CÂU 3: BÀI TOÁN CÔNG TY ABC (DHCP VÀ DHCP RELAY AGENT)

### 3a. Sơ đồ mô hình mạng & Phân bổ IP

2. Sơ đồ mạng chi tiết:

```text
=== MẠNG LAN 1 (172.16.10.0/24) ========================================================
   [ Server 1: DHCP Server & DNS ] (172.16.10.1/24)
   [ Máy Giám đốc & Thiết bị ]     (IP Tĩnh: 172.16.10.2 - 172.16.10.30)
   [ Phòng Kế toán & Nhân sự ]     (DHCP Scope 1: 172.16.10.31 - 172.16.10.250)
               |
         (172.16.10.1)
        [ Router Server 1 ] (Nối qua đường mạng trung gian 192.168.1.0/24)
         (192.168.1.1)
               |
         (192.168.1.2)
        [ Router Server 2 ] (Router mềm kiêm DHCP Relay Agent)
         (10.10.10.1)
               |
=== MẠNG LAN 2 (10.10.10.0/24) =========================================================
   [ Phòng Đào tạo & Laptop ]      (DHCP Scope 2: 10.10.10.10 - 10.10.10.250)
   [ Gateway LAN 2 ]               (10.10.10.1 - Cổng của Server 2)
```

#### 3. Bảng phân bổ IP chép bài:

* **LAN 1 (`172.16.10.0/24`):**
  * Gateway / Server 1 IP: `172.16.10.1` (Mask: `255.255.255.0`).
  * Dải IP Tĩnh (Server & Giám đốc, Máy in): `172.16.10.2` đến `172.16.10.30`.
  * Dải cấp động Scope 1 (Nhân viên LAN 1): `172.16.10.31` đến `172.16.10.250`.
* **Đường nối 2 Server (`192.168.1.0/24`):** Server 1 là `192.168.1.1/24`, Server 2 là `192.168.1.2/24`.
* **LAN 2 (`10.10.10.0/24`):**
  * Gateway / Server 2 IP: `10.10.10.1` (Mask: `255.255.255.0`).
  * Dải cấp động Scope 2 (Đào tạo & Laptop): `10.10.10.10` đến `10.10.10.250`.
  * DNS chung: `172.16.10.1`.

---

### 3b. Giải pháp & Nguyên lý hoạt động

* **Nguyên nhân lỗi:** Gói tin `DHCP Discover` là gói Broadcast (`255.255.255.255`). Router mềm ngăn cách 2 mạng có tính năng phân tách Broadcast Domain nên **mặc định chặn (drop) toàn bộ gói Broadcast**, khiến DHCP Server ở LAN 1 không nhận được yêu cầu từ LAN 2.
* **Giải pháp:** Cài đặt dịch vụ **DHCP Relay Agent** trên Router mềm (Server 2).

> *- Đưa ra giải pháp phù hợp để cấp địa chỉ IP động cho hệ thống mạng LAN*
> *1. Gán địa chỉ cho server 1 như sau : x là số máy sinh viên ngồi*
> &nbsp;&nbsp;&nbsp;&nbsp;*NIC 172 : 172.16.x.1/24*
> &nbsp;&nbsp;&nbsp;&nbsp;*NIC 192 : 192.168.x.1/24*
> *2. Gán địa chỉ cho server 2*
> &nbsp;&nbsp;&nbsp;&nbsp;*NIC 10 : 10.10.x.1/24*
> &nbsp;&nbsp;&nbsp;&nbsp;*NIC 192 : 192.168.x.2/24*
> *3. Cấu hình cho server 1 và server 2 làm Router*
> *4. Cài DHCP trên server 1*
> *5. Tạo 2 dãy địa chỉ trên DHCP server*
> *6. Scope 1 : 172.16.10.1 – 172.16.10.100*
> *7. Scope 2 : 10.10.10.1 – 10.10.10.100*
> *8. Cấu hình DHCP option 003 Router cho từng scope*
> *9. Kích hoạt các scope đã tạo*
> *10 Cấu hình cho server 2 làm DHCP Relay Agent*
> *11 Chỉnh card mạng của client về chế độ lấy địa chỉ động*
> *12 Kiểm tra kết nối giữa các mạng sau khi client lấy được địa chỉ từ DHCP server : client 1 ping địa chỉ của client 2*

---

> #### (TRANG 4):
>
> **Quy trình cấp phát động (DHCP) cho LAN 1:**
> • *Khi máy client khởi động, máy sẽ gửi broadcast gói tin DHCPDISCOVER, yêu cầu một server phục vụ mình. Gói tin này cũng chứa địa chỉ MAC của máy client.*
> • *Các máy Server trên mạng khi nhận được gói tin yêu cầu đó, nếu còn khả năng cung cấp địa chỉ IP, đều gửi lại cho máy Client gói tin DHCPOFFER, đề nghị cho thuê một địa chỉ IP trong một khoảng thời gian nhất định, kèm theo là một subnet mask và địa chỉ của Server. Server sẽ không cấp phát địa chỉ IP vừa đề nghị cho những Client khác trong suốt quá trình thương thuyết.*
> • *Máy Client sẽ lựa chọn một trong những lời đề nghị (DHCPOFFER) và gửi broadcast lại gói tin DHCPREQUEST chấp nhận lời đề nghị đó. Điều này cho phép các lời đề nghị không được chấp nhận sẽ được các Server rút lại và dùng đề cấp phát cho Client khác.*
> *Máy Server được Client chấp nhận sẽ gửi ngược lại một gói tin DHCPACK như là một lời xác nhận, cho biết là địa chỉ IP đó, subnet mask đó và thời hạn cho sử dụng đó sẽ chính thức được áp dụng. Ngoài ra Server còn gửi kèm theo những thông tin cấu hình bổ sung như địa chỉ của gateway mặc định, địa chỉ DNS Server,…*
>
> **Quy trình cấp phát động (DHCP Relay Agent) cho LAN 2:**
> • *DHCP Relay Agent là bộ trung chuyển DHCP Discover (hoặc DHCP Request) đến DHCP Server. DHCP Relay Agent cho phép forward các truy vấn của DHCP Client đến DHCP server và trả lại IP cho Clients (làm nhiệm vụ như Proxy)*
> • *Trong trường hợp DHCP Client và DHCP Server không nằm cùng subnet và được kết nối qua bộ định tuyến (router) thì cần phải có giải pháp cho phép truy vấn từ DHCP Client vượt qua router để đến DHCP Server. DHCP Relay Agent (tác nhân chuyển tiếp DHCP) được dùng cho mục đích này. DHCP Relay Agent là một thực thể trung gian cho phép chuyển tiếp (relay) các DHCP Discover (hoặc DHCP Request), mà thường bị chặn ở ngay router, từ DHCP Client đến DHCP Server.*
> • *DHCP Client phát gói tin DHCP Discover sẽ được DHCP Relay Agent đóng vai trò như 1 DHCP Client phát lại gói tin DHCP Discover đến DHCP Server .*

---

### 3c. Mô tả quá trình cài đặt và triển khai DHCP mà đã đưa ra giải pháp

> #### (TRANG 5):
>
> *Mô tả quá trình cài đặt*
> *Quá trình cài đặt DHCP server.*
> *Vào server manager- Role chọn Add role chọn DHCP server. Disable DHCPv6 stateless mode, next Sau đó một vài giây, DHCP Server sẽ được cài đặt.*
> *Sau khi cài đặt xong ta vào start …..*
> *- Thực hiện triển khai DHCP đã đưa ra giải pháp*
> *LAN 1: Nhận được IP động của 172.16.x.1/24*
> *LAN 2: Nhận được IP động của 10.10.x.1/24*

#### ✍️ BỔ SUNG CÁC BƯỚC CHI TIẾT TIẾP THEO (ĐỂ HOÀN THIỆN ĐẦY ĐỦ BÀI LÀM):

##### 1. Cấu hình tiếp trên Server 1 (Windows Server):

* Vào **Start** $\rightarrow$ **Administrative Tools** $\rightarrow$ Mở **DHCP**.
* Tạo **Scope 1 (LAN 1):** Click chuột phải `IPv4` $\rightarrow$ `New Scope` $\rightarrow$ Name: `LAN1` $\rightarrow$ Dải IP: `172.16.10.31` đến `172.16.10.250`, Subnet Mask: `255.255.255.0` $\rightarrow$ **Option 003 Router:** `172.16.10.1` $\rightarrow$ **Option 006 DNS:** `172.16.10.1` $\rightarrow$ Activate Scope.
* Tạo **Scope 2 (LAN 2):** Click chuột phải `IPv4` $\rightarrow$ `New Scope` $\rightarrow$ Name: `LAN2` $\rightarrow$ Dải IP: `10.10.10.10` đến `10.10.10.250`, Subnet Mask: `255.255.255.0` $\rightarrow$ **Option 003 Router:** **`10.10.10.1`** (Gateway của LAN 2) $\rightarrow$ **Option 006 DNS:** `172.16.10.1` $\rightarrow$ Activate Scope.

##### 2. Cấu hình trên Server 2 (Router mềm & DHCP Relay Agent):

* **Bật Router:** Vào Server Manager $\rightarrow$ Add Roles: **Remote Access / Routing** $\rightarrow$ Mở **Routing and Remote Access (RRAS)** $\rightarrow$ Chuột phải Server chọn **Configure and Enable** $\rightarrow$ Chọn **Custom configuration** $\rightarrow$ Tích chọn **LAN routing** $\rightarrow$ Finish & Start service.
* **Cấu hình DHCP Relay Agent:**
  * Trong RRAS $\rightarrow$ bung `IPv4` $\rightarrow$ chuột phải **General** $\rightarrow$ **New Routing Protocol...** $\rightarrow$ Chọn **DHCP Relay Agent**.
  * Chuột phải vào **DHCP Relay Agent** vừa thêm $\rightarrow$ **Properties** $\rightarrow$ Nhập IP của Server 1: **`192.168.1.1`** (hoặc `172.16.10.1`) $\rightarrow$ Bấm **Add** $\rightarrow$ OK.
  * Chuột phải vào **DHCP Relay Agent** $\rightarrow$ **New Interface...** $\rightarrow$ Chọn Card mạng nối với **LAN 2** $\rightarrow$ Đảm bảo chọn **Relay DHCP packets** $\rightarrow$ OK.

##### 3. Kiểm tra trên Client:

* Tại Client 1 (LAN 1): Chạy `ipconfig /renew` $\rightarrow$ Nhận IP `172.16.10.x`, Gateway `172.16.10.1`.
* Tại Client 2 (LAN 2): Chạy `ipconfig /renew` $\rightarrow$ Nhận IP `10.10.10.x` qua Relay, Gateway `10.10.10.1`.
* Chạy lệnh `ping` thông giữa Client 1 và Client 2 để xác nhận thông tuyến 100%.

---

# CÂU 4: DỊCH VỤ VOIP (VOICE OVER IP)

### 1. Cơ chế hoạt động của VoIP

* **Bản chất:** Chuyển đổi giọng nói analog thành gói tin số IP để truyền qua mạng LAN/Internet thời gian thực.
* **Kiến trúc phân tách 2 kênh:**
  1. **Kênh Báo hiệu (Signaling):** Dùng giao thức **SIP (Session Initiation Protocol)** cổng **UDP/TCP 5060** kết hợp **SDP** để thiết lập, định tuyến và ngắt cuộc gọi.
  2. **Kênh Truyền thông thoại (Media Stream):** Dùng giao thức **RTP (Real-time Transport Protocol)** trên nền **UDP cổng ngẫu nhiên (10000 - 20000)** để truyền âm thanh trực tiếp hai chiều; đi kèm **RTCP** giám sát chất lượng (trễ Jitter, mất gói).
* **Chu trình cuộc gọi 6 bước:**
  * `INVITE` (A gọi B) $\rightarrow$ `100 Trying` (Tổng đài định tuyến) $\rightarrow$ `180 Ringing` (B reo chuông) $\rightarrow$ `200 OK` (B nhấc máy) $\rightarrow$ `ACK` (Xác nhận kết nối) $\rightarrow$ Truyền âm thanh qua RTP $\rightarrow$ `BYE` (Gác máy).
* **Codecs âm thanh:** **G.711** (64 Kbps, không nén, chất lượng chuẩn thoại, dùng cho LAN), **G.729** (8 Kbps, nén cao, tiết kiệm băng thông khi gọi qua Internet).

### 2. Triển khai VoIP (Tổng đài Asterisk & Softphone)

1. **Cài đặt:** Trên Linux chạy `sudo apt install asterisk -y`.
2. **Khai báo máy nhánh trong `/etc/asterisk/pjsip.conf`:** Tạo các extension (máy nhánh) như `101`, `102` với mật khẩu xác thực và loại codec (`ulaw,alaw`).
3. **Cấu hình định tuyến cuộc gọi trong `/etc/asterisk/extensions.conf` (Dialplan):**
   * `exten => 101,1,Dial(PJSIP/101,20)` (gọi 101 đổ chuông 20 giây).
   * `exten => 102,1,Dial(PJSIP/102,20)` (gọi 102 đổ chuông 20 giây).
4. **Softphone Client:** Dùng ứng dụng **MicroSIP** (trên Windows) hoặc **Zoiper** (trên điện thoại) điền IP Tổng đài, Extension `101`, Password để đăng nhập và gọi thử.

### 3. Quản trị hệ thống VoIP

* **Bảo mật:** Đổi cổng SIP mặc định (khác 5060), đặt mật khẩu máy nhánh phức tạp, cài **Fail2ban** chống dò quét mật khẩu (SIP brute force).
* **Xử lý NAT Traversal:** Cấu hình `localnet`, `external_media_address` hoặc dùng STUN Server để khắc phục lỗi cuộc gọi bị mất tiếng một chiều (One-way Audio).
* **Tính năng doanh nghiệp:**
  * **Ring Group:** Gom nhóm các máy nhánh (gọi 1 số chung đổ chuông toàn bộ phòng ban).
  * **IVR (Interactive Voice Response):** Lời chào tự động ("Bấm phím 1 gặp Kế toán...").
  * **Voicemail & Call Recording:** Ghi âm tin nhắn thoại và ghi âm cuộc gọi.

---

# CÂU 5: DỊCH VỤ HTTPS & CERTIFICATE SERVER (CA)

### 1. Cơ chế hoạt động của HTTPS

* **Bản chất:** Giao thức HTTP chạy trên nền tầng mã hóa bảo mật **TLS/SSL**, cổng mặc định **TCP 443**.
* **Đảm bảo 3 mục tiêu an ninh (CIA):**
  1. *Bảo mật (Confidentiality):* Mã hóa toàn bộ dữ liệu, chống nghe lén.
  2. *Toàn vẹn (Integrity):* Dữ liệu không bị chỉnh sửa trên đường truyền (nhờ mã băm HMAC).
  3. *Xác thực (Authentication):* Xác thực đúng danh tính máy chủ qua Chứng chỉ số (Certificate), chống giả mạo trang web.
* **Kết hợp 2 loại mã hóa:**
  * **Bất đối xứng (RSA/ECC):** Dùng cặp khóa Public/Private Key trong bước Handshake để trao đổi khóa an toàn.
  * **Đối xứng (AES-256):** Dùng khóa chung (Session Key) để mã hóa toàn bộ dữ liệu truyền tải với tốc độ cao.
* **4 bước bắt tay TLS Handshake:**
  1. `ClientHello`: Client gửi phiên bản TLS, danh sách thuật toán Cipher Suites, chuỗi ngẫu nhiên Client Random.
  2. `ServerHello & Certificate`: Server chọn thuật toán, gửi Server Random kèm Chứng chỉ số (chứa Public Key của Server).
  3. `Client Key Exchange`: Client xác thực chứng chỉ, tạo chuỗi bí mật `Premaster Secret`, mã hóa bằng Public Key của Server và gửi sang. Hai bên cùng tạo ra `Session Key`.
  4. `Finished`: Xác nhận bắt tay thành công $\rightarrow$ Bắt đầu truyền dữ liệu HTTP mã hóa bằng Session Key.

### 2. Triển khai Certificate Server (CA)

* **Khái niệm:** CA (Certificate Authority) là tổ chức/máy chủ tin cậy đứng ra ký số chứng nhận danh tính cho các máy chủ khác.
* **Trên Windows Server:** Cài đặt Role **Active Directory Certificate Services (AD CS)** qua Server Manager $\rightarrow$ Chọn loại **Root CA**, thuật toán SHA256, RSA 2048-bit $\rightarrow$ Cấp phát qua trang Web Enrollment `http://Server_IP/certsrv`.
* **Trên Linux (OpenSSL):** Tạo Root CA nội bộ bằng lệnh:
  `openssl req -x509 -new -nodes -key ca.key -sha256 -days 3650 -out ca.crt`.

### 3. Triển khai HTTPS trên Web Server

1. **Tạo Private Key & CSR:** Chạy `openssl req -new -newkey rsa:2048 -nodes -keyout abc.key -out abc.csr`.
2. **Gửi CSR lên CA:** CA ký xác nhận và xuất file chứng chỉ `abc.crt`.
3. **Cấu hình Web Server:**
   * *Nginx:* Khai báo `listen 443 ssl;`, trỏ đường dẫn `ssl_certificate /path/abc.crt;` và `ssl_certificate_key /path/abc.key;`.
   * *IIS:* Vào Server Certificates hoàn tất Certificate Request $\rightarrow$ Vào Site Bindings thêm cổng `443` HTTPS và chọn Certificate.

### 4. Quản trị HTTPS

* **Bắt buộc chuyển hướng (Force 301 Redirect):** Cấu hình tự động chuyển toàn bộ truy cập từ cổng 80 sang cổng 443 (`return 301 https://$host$request_uri;`).
* **Bật HSTS (HTTP Strict Transport Security):** Thêm Header HSTS ép trình duyệt chỉ kết nối HTTPS để chống tấn công hạ cấp SSL Stripping.
* **Tối ưu hóa bảo mật:** Tắt hoàn toàn SSLv2, SSLv3, TLS 1.0, TLS 1.1; chỉ bật **TLS 1.2 và TLS 1.3**.
* **Gia hạn tự động:** Cài đặt gia hạn chứng chỉ tự động định kỳ với Certbot (`certbot renew`).

---
