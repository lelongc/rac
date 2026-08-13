# HƯỚNG DẪN CẤU HÌNH LAB 1: ĐỊNH TUYẾN (ROUTING) - CHUYỂN TỪ CARD NAT SANG VMNET11 & VMNET12

> 📌 **BÀI TÁN**: Hiện tại cả 3 máy ảo (`Win7 (1)`, `Server`, `Win7 (2)`) đều đang dùng card NAT (`VMnet8` - dải IP `192.168.1.x`). 
> Để làm bài lab định tuyến chuẩn và không bị đụng độ IP với mạng NAT, ta sẽ chuyển đổi và tạo 2 card mạng ảo mới là **`VMnet11`** và **`VMnet12`**.

---

## I. THÔNG TIN MÔ HÌNH VÀ PHÂN HOẠCH IP

```
[Win7 (1)] <------ VMnet11 ------> [ Windows Server ] <------ VMnet12 ------> [Win7 (2)]
192.168.11.2                       Card 1: 192.168.11.1                       100.100.12.2
                                   Card 2: 100.100.12.1
```

### Bảng thông số chi tiết:

| Tên máy ảo | Card mạng VMware | Địa chỉ IP | Subnet Mask | Default Gateway |
| :--- | :--- | :--- | :--- | :--- |
| **Win7 (1)** | Custom: `VMnet11` | `192.168.11.2` | `255.255.255.0` | `192.168.11.1` |
| **Windows Server** | Card 1: `VMnet11` | `192.168.11.1` | `255.255.255.0` | *Để trống* |
| | Card 2: `VMnet12` | `100.100.12.1` | `255.255.255.0` | *Để trống* |
| **Win7 (2)** | Custom: `VMnet12` | `100.100.12.2` | `255.255.255.0` | `100.100.12.1` |

---

## BƯỚC 1: CẤU HÌNH MẠNG ẢO (VIRTUAL NETWORK EDITOR) TRÊN VMWARE

Trước tiên, ta cần tạo 2 mạng ảo `VMnet11` và `VMnet12` trên phần mềm VMware Workstation máy thật:

1. Trên phần mềm **VMware Workstation** ở máy thật, vào menu **Edit** -> chọn **Virtual Network Editor...**
2. Nếu các tùy chọn bị mờ, nhấn vào nút **Change Settings** (góc dưới bên phải, có biểu tượng lá chắn Administrator).
3. **Thêm VMnet11**:
   * Nhấn nút **Add Network...** -> Chọn **`VMnet11`** -> Nhấn **OK**.
   * Chọn dòng **VMnet11**: tích chọn mục **Host-only** (Connect VMs internally...).
   * Tại mục **Subnet IP**: Điền `192.168.11.0` | **Subnet mask**: `255.255.255.0`.
   * **Bỏ tích** dòng *Use local DHCP service to distribute IP to VMs* (vì ta đặt IP tĩnh bằng tay).
4. **Thêm VMnet12**:
   * Nhấn nút **Add Network...** -> Chọn **`VMnet12`** -> Nhấn **OK**.
   * Chọn dòng **VMnet12**: tích chọn mục **Host-only**.
   * Tại mục **Subnet IP**: Điền `100.100.12.0` | **Subnet mask**: `255.255.255.0`.
   * **Bỏ tích** dòng *Use local DHCP service to distribute IP to VMs*.
5. Nhấn **Apply** -> Nhấn **OK** để lưu lại.

---

## BƯỚC 2: CHUYỂN ĐỔI CARD MẠNG NAT SANG VMNET11 & VMNET12 TRÊN CÁC MÁY ẢO

Bây giờ ta chuyển card NAT hiện tại trên các máy ảo sang card VMnet11 / VMnet12 tương ứng:

### 1. Trên máy ảo Win7 (1):
1. Tắt máy ảo hoặc chuột phải vào máy ảo **Win7 (1)** -> chọn **Settings...**
2. Chọn mục **Network Adapter** (Đang là NAT).
3. Chuyển từ *NAT* sang tích chọn **Custom: Specific virtual network**.
4. Chọn từ danh sách xổ xuống: **`VMnet11`**.
5. Nhấn **OK**.

### 2. Trên máy ảo Windows Server (Cần 2 Card Mạng):
1. Chuột phải vào máy ảo **Windows Server** -> chọn **Settings...**
2. **Cấu hình Card 1 (Card NAT cũ)**:
   * Chọn **Network Adapter** hiện tại -> Tích chọn **Custom: Specific virtual network** -> Chọn **`VMnet11`**.
3. **Thêm Card 2**:
   * Nhấn nút **Add...** ở phía dưới cửa sổ Settings.
   * Chọn **Network Adapter** -> Nhấn **Finish**.
   * Chọn vào **Network Adapter 2** vừa tạo -> Tích chọn **Custom: Specific virtual network** -> Chọn **`VMnet12`**.
4. Nhấn **OK**.

### 3. Trên máy ảo Win7 (2):
1. Chuột phải vào máy ảo **Win7 (2)** -> chọn **Settings...**
2. Chọn mục **Network Adapter** (Đang là NAT).
3. Chuyển sang tích chọn **Custom: Specific virtual network**.
4. Chọn từ danh sách xổ xuống: **`VMnet12`**.
5. Nhấn **OK**.

---

## BƯỚC 3: ĐẶT IP TĨNH TRONG HỆ ĐIỀU HÀNH THUỘC CÁC MÁY ẢO

Mở các máy ảo lên và tiến hành gán địa chỉ IP:

### 1. Trên máy Win7 (1):
1. Vào `Control Panel` -> `Network and Internet` -> `Network and Sharing Center` -> chọn `Change adapter settings`.
2. Chuột phải vào `Local Area Connection` -> chọn **Properties**.
3. Nhấp kép vào **Internet Protocol Version 4 (TCP/IPv4)**.
4. Tích chọn **Use the following IP address**:
   * **IP address**: `192.168.11.2`
   * **Subnet mask**: `255.255.255.0`
   * **Default gateway**: `192.168.11.1`
5. Nhấn **OK** -> **OK**.

### 2. Trên máy Windows Server:
1. Vào `Control Panel` -> `Network and Sharing Center` -> `Change adapter settings`.
2. Lúc này bạn sẽ thấy 2 card mạng. Nhấn F2 đổi tên để đỡ nhầm lẫn:
   * Card 1 (Nối VMnet11) -> Đổi tên thành `Card_VMnet11`
   * Card 2 (Nối VMnet12) -> Đổi tên thành `Card_VMnet12`
3. **Cấu hình Card_VMnet11**:
   * Chuột phải `Card_VMnet11` -> **Properties** -> chọn `TCP/IPv4` -> **Properties**.
   * IP address: `192.168.11.1`
   * Subnet mask: `255.255.255.0`
   * Default gateway: *ĐỂ TRỐNG (Không điền)*
   * Nhấn **OK**.
4. **Cấu hình Card_VMnet12**:
   * Chuột phải `Card_VMnet12` -> **Properties** -> chọn `TCP/IPv4` -> **Properties**.
   * IP address: `100.100.12.1`
   * Subnet mask: `255.255.255.0`
   * Default gateway: *ĐỂ TRỐNG (Không điền)*
   * Nhấn **OK**.

### 3. Trên máy Win7 (2):
1. Vào `Control Panel` -> `Network and Sharing Center` -> `Change adapter settings`.
2. Chuột phải `Local Area Connection` -> chọn **Properties** -> `TCP/IPv4`.
3. Tích chọn **Use the following IP address**:
   * **IP address**: `100.100.12.2`
   * **Subnet mask**: `255.255.255.0`
   * **Default gateway**: `100.100.12.1`
4. Nhấn **OK** -> **OK**.

---

## BƯỚC 4: TẮT WINDOWS FIREWALL TRÊN CẢ 3 MÁY (BẮT BUỘC)

> ⚠️ **Nếu không tắt Firewall, lệnh Ping giữa các dải mạng chắc chắn sẽ bị báo lỗi `Request timed out`!**

Thực hiện thao tác này trên cả **Win7 (1)**, **Windows Server**, và **Win7 (2)**:
1. Mở **Control Panel** -> gõ tìm kiếm hoặc chọn **Windows Firewall**.
2. Chọn mục **Turn Windows Firewall on or off** ở menu cột bên trái.
3. Tích chọn **Turn off Windows Firewall (not recommended)** ở cả mục *Domain*, *Private* và *Public network settings*.
4. Nhấn **OK**.

---

## BƯỚC 5: CÀI ĐẶT VÀ BẬT DỊCH VỤ ROUTING (RRAS) TRÊN WINDOWS SERVER

Để Windows Server hoạt động như một Router đóng vai trò chuyển tiếp gói tin giữa `VMnet11` và `VMnet12`:

### 5.1. Cài đặt Role Remote Access:
1. Mở **Server Manager** trên Windows Server.
2. Nhấn vào **Manage** (góc trên bên phải) -> chọn **Add Roles and Features**.
3. Nhấn **Next** -> Chọn **Role-based or feature-based installation** -> Nhấn **Next**.
4. Chọn Server hiện tại -> Nhấn **Next**.
5. Tại mục **Server Roles**, tìm và tích chọn **`Remote Access`** -> Nhấn **Next**.
6. Nhấn **Next** qua các trang hướng dẫn cho đến mục **Role Services**.
7. Tích chọn vào ô **`Routing`** -> Cửa sổ hiện ra chọn **Add Features**.
8. Nhấn **Next** -> Nhấn **Install**. Chờ thanh tiến trình chạy xong -> Nhấn **Close**.

### 5.2. Kích hoạt dịch vụ LAN Routing:
1. Trên **Server Manager**, chọn **Tools** -> chọn **Routing and Remote Access**.
2. Chuột phải vào tên Server ở cột bên trái (Đang có biểu tượng mũi tên màu đỏ hướng xuống) -> chọn **Configure and Enable Routing and Remote Access**.
3. Cửa sổ Wizard hiện ra -> Chọn **Next**.
4. Tại bước *Configuration*, tích chọn dòng thứ 5: **`Custom configuration`** -> Nhấn **Next**.
5. Tích chọn vào ô **`LAN routing`** -> Nhấn **Next** -> Nhấn **Finish**.
6. Hộp thoại thông báo hiện ra hỏi có kích hoạt dịch vụ không, chọn **`Start service`**.
7. Chờ vài giây đến khi biểu tượng tên Server chuyển sang màu **xanh lá cây** (Green) là thành công!

---

## BƯỚC 6: BƯỚC KIỂM TRA PING THÔNG TẤT CẢ CÁC MÁY

Mở cửa sổ dòng lệnh **CMD** (`Windows + R` -> gõ `cmd` -> nhấn `Enter`):

### 1. Kiểm tra trên máy Win7 (1):
* Gõ: `ping 192.168.11.1` (Ping card 1 Server) -> **Thành công**
* Gõ: `ping 100.100.12.1` (Ping card 2 Server) -> **Thành công**
* Gõ: `ping 100.100.12.2` (Ping sang máy Win7 (2) xuyên qua Server) -> **Thành công! `Reply from 100.100.12.2: bytes=32 time<1ms TTL=127`**

### 2. Kiểm tra trên máy Win7 (2):
* Gõ: `ping 100.100.12.1` (Ping card 2 Server) -> **Thành công**
* Gõ: `ping 192.168.11.1` (Ping card 1 Server) -> **Thành công**
* Gõ: `ping 192.168.11.2` (Ping sang máy Win7 (1) xuyên qua Server) -> **Thành công! `Reply from 192.168.11.2: bytes=32 time<1ms TTL=127`**

---

## IV. TROUBLESHOOTING (XỬ LÝ LỖI NẾU KHÔNG PING ĐƯỢC)

Nếu Win7 (1) ping Win7 (2) bị lỗi `Request timed out` hoặc `Destination host unreachable`:
1. **Kiểm tra Windows Firewall**: Đảm bảo cả 3 máy đã TẮT HOÀN TOÀN Windows Firewall.
2. **Kiểm tra Default Gateway**:
   * Win7 (1) phải trỏ Default Gateway về IP `192.168.11.1`.
   * Win7 (2) phải trỏ Default Gateway về IP `100.100.12.1`.
   * Server tuyệt đối **KHÔNG** điền Default Gateway ở cả 2 card mạng.
3. **Kiểm tra Card mạng VMware**: Nhìn góc dưới bên phải cửa sổ máy ảo VMware xem card mạng đã connected chưa, và đúng `VMnet11` / `VMnet12` chưa.
