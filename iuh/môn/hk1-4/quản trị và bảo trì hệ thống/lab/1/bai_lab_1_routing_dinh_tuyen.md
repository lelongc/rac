# HƯỚNG DẪN CẤU HÌNH LAB 1: ĐỊNH TUYẾN (ROUTING) ĐỂ PING THÔNG CÁC MÁY

Tài liệu hướng dẫn chi tiết từng bước (Step-by-step) cài đặt và cấu hình mô hình định tuyến giữa 2 mạng khác dải IP thông qua máy Windows Server.

---

## I. THÔNG TIN MÔ HÌNH MẠNG (SƠ ĐỒ TRÊN BẢNG)

```
[Win7 (1)] <------ VMnet1 ------> [ Windows Server ] <------ VMnet2 ------> [Win7 (2)]
192.168.1.2                       Card 1: 192.168.1.1                        100.100.1.2
                                  Card 2: 100.100.1.1
```

* **Win7 (1)**: 
  * Network Adapter: **Custom (VMnet1)**
  * IP: `192.168.1.2` / Subnet Mask: `255.255.255.0`
  * Default Gateway: `192.168.1.1`
* **Windows Server** (Có 2 Card mạng):
  * Card 1 (Nối VMnet1): IP `192.168.1.1` / Subnet Mask: `255.255.255.0` / Gateway: *Để trống*
  * Card 2 (Nối VMnet2): IP `100.100.1.1` / Subnet Mask: `255.255.255.0` (hoặc `255.0.0.0`) / Gateway: *Để trống*
* **Win7 (2)**: 
  * Network Adapter: **Custom (VMnet2)**
  * IP: `100.100.1.2` / Subnet Mask: `255.255.255.0` (hoặc `255.0.0.0`)
  * Default Gateway: `100.100.1.1`

---

## II. CÁC BƯỚC THỰC HIỆN CHI TIẾT (STEP-BY-STEP)

### BƯỚC 1: CẤU HÌNH CARD MẠNG TRÊN PHẦN MỀM MÁY ẢO (VMware Workstation)

1. **Trên máy ảo Win7 (1)**:
   * Nhấp chuột phải vào máy ảo Win7 (1) -> chọn **Settings**.
   * Chọn **Network Adapter** -> Tích vào **Custom: Specific virtual network** -> Chọn **`VMnet1`**.
2. **Trên máy ảo Windows Server**:
   * Vào **Settings** -> **Network Adapter** thứ nhất -> Chọn **Custom: `VMnet1`**.
   * Nhấn nút **Add...** bên dưới -> Chọn **Network Adapter** -> Nhấn **Finish** để thêm card mạng thứ 2.
   * Chọn **Network Adapter 2** mới thêm -> Tích vào **Custom: `VMnet2`**.
3. **Trên máy ảo Win7 (2)**:
   * Vào **Settings** -> **Network Adapter** -> Chọn **Custom: `VMnet2`**.

---

### BƯỚC 2: ĐẶT ĐỊA CHỈ IP TĨNH CHO CÁC MÁY

#### 1. Đặt IP trên máy Win7 (1):
* Vào `Control Panel` -> `Network and Sharing Center` -> `Change adapter settings`.
* Chuột phải `Local Area Connection` -> **Properties** -> chọn `TCP/IPv4` -> **Properties**.
* Điền thông số:
  * **IP address**: `192.168.1.2`
  * **Subnet mask**: `255.255.255.0`
  * **Default gateway**: `192.168.1.1`
* Nhấn **OK**.

#### 2. Đặt IP trên máy Windows Server:
* Vào `Change adapter settings` (Sẽ thấy 2 card mạng, đổi tên thành `VMnet1` và `VMnet2` cho dễ phân biệt).
* **Card VMnet1**:
  * IP address: `192.168.1.1`
  * Subnet mask: `255.255.255.0`
  * Default gateway: *Để trống*
* **Card VMnet2**:
  * IP address: `100.100.1.1`
  * Subnet mask: `255.255.255.0`
  * Default gateway: *Để trống*

#### 3. Đặt IP trên máy Win7 (2):
* Chuột phải `Local Area Connection` -> **Properties** -> chọn `TCP/IPv4` -> **Properties**.
* Điền thông số:
  * **IP address**: `100.100.1.2`
  * **Subnet mask**: `255.255.255.0`
  * **Default gateway**: `100.100.1.1`
* Nhấn **OK**.

---

### BƯỚC 3: TẮT WINDOWS FIREWALL TRÊN CẢ 3 MÁY (CỰC KỲ QUAN TRỌNG)

Mặc định Windows Firewall sẽ chặn gói tin **Ping (ICMP)** nên nếu không tắt Firewall thì các máy sẽ báo lỗi `Request timed out`.

* Trên cả 3 máy (`Win7 (1)`, `Server`, `Win7 (2)`):
  1. Vào **Control Panel** -> **Windows Firewall**.
  2. Chọn **Turn Windows Firewall on or off** (ở cột bên trái).
  3. Tích chọn **Turn off Windows Firewall** cho cả *Domain*, *Private* và *Public network*.
  4. Nhấn **OK**.

---

### BƯỚC 4: CẤU HÌNH DỊCH VỤ ĐỊNH TUYẾN (RRAS) TRÊN WINDOWS SERVER

Để Windows Server chuyển tiếp gói tin từ mạng `192.168.1.0` sang mạng `100.100.1.0`, ta cần cài dịch vụ **Routing and Remote Access (RRAS)**.

#### 4.1. Cài đặt Role Remote Access:
1. Trên Windows Server, mở **Server Manager**.
2. Nhấn vào **Manage** (góc trên bên phải) -> chọn **Add Roles and Features**.
3. Nhấn **Next** -> chọn **Role-based or feature-based installation** -> **Next**.
4. Chọn Server hiện tại -> **Next**.
5. Tại mục **Server Roles**, tích chọn **`Remote Access`** -> Nhấn **Next**.
6. Nhấn **Next** tiếp tục cho đến bước **Role Services**.
7. Tích chọn vào mục **`Routing`** (Nó sẽ tự động tích kèm *DirectAccess and VPN (RAS)*) -> Chọn **Add Features**.
8. Nhấn **Next** -> Nhấn **Install** và chờ quá trình cài đặt hoàn tất -> Chọn **Close**.

#### 4.2. Kích hoạt và cấu hình dịch vụ Routing:
1. Mở **Server Manager** -> chọn **Tools** (góc trên bên phải) -> chọn **Routing and Remote Access**.
2. Chuột phải vào tên Server (ở cột bên trái) -> chọn **Configure and Enable Routing and Remote Access**.
3. Màn hình Wizard xuất hiện, chọn **Next**.
4. Tại bước *Configuration*, chọn dòng **`Custom configuration`** -> **Next**.
5. Tích chọn vào ô **`LAN routing`** -> **Next** -> **Finish**.
6. Hệ thống hỏi có muốn start service không, nhấn chọn **`Start service`**.
7. Chờ biểu tượng tên Server chuyển sang màu **xanh lá cây** là hoàn thành.

---

### BƯỚC 5: KIỂM TRA PING THÔNG CÁC MÁY (TESTING)

Mở cửa sổ dòng lệnh **CMD** (`Windows + R` -> gõ `cmd`) trên từng máy để kiểm tra kết nối:

1. **Trên máy Win7 (1)**:
   * Gõ: `ping 192.168.1.1` (Ping card VMnet1 của Server -> Thành công)
   * Gõ: `ping 100.100.1.1` (Ping card VMnet2 của Server -> Thành công)
   * Gõ: `ping 100.100.1.2` (Ping sang máy Win7 (2) xuyên qua Server -> **Thành công `Reply from 100.100.1.2...`**)

2. **Trên máy Win7 (2)**:
   * Gõ: `ping 100.100.1.1` (Ping card VMnet2 của Server -> Thành công)
   * Gõ: `ping 192.168.1.1` (Ping card VMnet1 của Server -> Thành công)
   * Gõ: `ping 192.168.1.2` (Ping sang máy Win7 (1) xuyên qua Server -> **Thành công `Reply from 192.168.1.2...`**)

---

## III. TỔNG KẾT BÀI LAB

* Khi máy Win7 (1) gửi gói tin đến `100.100.1.2`, vì khác dải IP nên nó sẽ đẩy gói tin đến **Default Gateway (`192.168.1.1`)**.
* Máy Windows Server nhận được gói tin, nhờ dịch vụ **LAN Routing (RRAS)** đã kích hoạt, nó sẽ tra bảng định tuyến và chuyển tiếp gói tin qua card VMnet2 (`100.100.1.1`) để tới đích `100.100.1.2`.
