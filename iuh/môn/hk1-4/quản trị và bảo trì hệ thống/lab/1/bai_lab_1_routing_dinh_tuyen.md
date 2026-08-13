# HƯỚNG DẪN CẤU HÌNH LAB 1: ĐỊNH TUYẾN (ROUTING) - BẢN CHI TIẾT ĐẦY ĐỦ KÈM KINH NGHIỆM XỬ LÝ LỖI

> 📌 **BÀI TOÁN**: Cấu hình máy Windows Server đóng vai trò Router để chuyển tiếp gói tin giữa 2 dải mạng:
> * Mạng 1 (VMnet11): Dải IP **`192.168.11.0/24`**
> * Mạng 2 (VMnet12): Dải IP **`100.100.11.0/24`**

---

## I. THÔNG TIN MÔ HÌNH VÀ BẢNG PHÂN HOẠCH IP CHUẨN

```
[Win7 (1)] <------ VMnet11 ------> [ Windows Server ] <------ VMnet12 ------> [Win7 (2)]
192.168.11.2                       Card 1: 192.168.11.1                       100.100.11.2
                                   Card 2: 100.100.11.1
```

### Bảng thông số IP chi tiết:

| Tên máy ảo | Card mạng VMware | Địa chỉ IP | Subnet Mask | Default Gateway |
| :--- | :--- | :--- | :--- | :--- |
| **Win7 (1)** | Custom: `VMnet11` | **`192.168.11.2`** *(Không để .1)* | `255.255.255.0` | **`192.168.11.1`** |
| **Windows Server** | Card 1: `VMnet11` | **`192.168.11.1`** | `255.255.255.0` | *Để trống* |
| | Card 2: `VMnet12` | **`100.100.11.1`** | `255.255.255.0` | *Để trống* |
| **Win7 (2)** | Custom: `VMnet12` | **`100.100.11.2`** | `255.255.255.0` | **`100.100.11.1`** |

---

## II. CÁC BƯỚC THỰC HIỆN CHI TIẾT (STEP-BY-STEP)

### BƯỚC 1: CẤU HÌNH MẠNG ẢO (VIRTUAL NETWORK EDITOR) TRÊN VMWARE

1. Vào VMware Workstation trên máy thật -> menu **Edit** -> chọn **Virtual Network Editor...**
2. Nhấn nút **Change Settings** (nếu cần quyền Administrator).
3. **Cấu hình VMnet11**:
   * Chọn **VMnet11** -> tích chọn **Host-only**.
   * **Subnet IP**: `192.168.11.0` | **Subnet mask**: `255.255.255.0`.
   * **Bỏ tích** dòng *Use local DHCP service to distribute IP to VMs*.
4. **Cấu hình VMnet12**:
   * Chọn **VMnet12** -> tích chọn **Host-only**.
   * **Subnet IP**: `100.100.11.0` | **Subnet mask**: `255.255.255.0`.
   * **Bỏ tích** dòng *Use local DHCP service to distribute IP to VMs*.
5. Nhấn **Apply** -> **OK**.

---

### BƯỚC 2: GÁN CARD MẠNG TRÊN CÁC MÁY ẢO

1. **Win7 (1)**: Chuột phải chọn Settings -> Network Adapter -> Chọn **Custom: `VMnet11`**.
2. **Windows Server**: 
   * Card 1: Chọn **Custom: `VMnet11`**.
   * Card 2 (Add thêm): Chọn **Custom: `VMnet12`**.
3. **Win7 (2)**: Chuột phải chọn Settings -> Network Adapter -> Chọn **Custom: `VMnet12`**.

---

### BƯỚC 3: ĐẶT IP TĨNH VÀ TẮT WINDOWS FIREWALL

#### 1. Trên máy Win7 (1):
* Vào `Control Panel` -> `Network and Sharing Center` -> `Change adapter settings`.
* Chuột phải `Local Area Connection` -> **Properties** -> `TCP/IPv4`:
  * **IP address**: `192.168.11.2`
  * **Subnet mask**: `255.255.255.0`
  * **Default gateway**: `192.168.11.1`
* Vào **Windows Firewall** -> Chọn **Turn off Windows Firewall** ở tất cả các vị trí.

#### 2. Trên máy Windows Server:
* Vào `Change adapter settings`:
  * **Card 1 (`VMnet11`)**: IP `192.168.11.1` | Subnet mask `255.255.255.0` | Gateway: *ĐỂ TRỐNG*.
  * **Card 2 (`VMnet12`)**: IP `100.100.11.1` | Subnet mask `255.255.255.0` | Gateway: *ĐỂ TRỐNG*.
* Vào **Windows Firewall** -> Chọn **Turn off Windows Firewall** ở cả 3 profile (*Domain, Private, Public*).

#### 3. Trên máy Win7 (2):
* Vào `Control Panel` -> `Network and Sharing Center` -> `Change adapter settings`.
* Chuột phải `Local Area Connection` -> **Properties** -> `TCP/IPv4`:
  * **IP address**: `100.100.11.2`
  * **Subnet mask**: `255.255.255.0`
  * **Default gateway**: `100.100.11.1`
* Vào **Windows Firewall** -> Chọn **Turn off Windows Firewall**.

---

### BƯỚC 4: CẤU HÌNH DỊCH VỤ ĐỊNH TUYẾN (RRAS) TRÊN SERVER

1. **Cài Role Remote Access**:
   * Vào **Server Manager** -> **Manage** -> **Add Roles and Features**.
   * Chọn Role **`Remote Access`** -> ở bước Role Services tích chọn **`Routing`** -> **Install**.
2. **Kích hoạt LAN Routing**:
   * Vào **Server Manager** -> **Tools** -> **Routing and Remote Access**.
   * Chuột phải tên Server -> **Configure and Enable Routing and Remote Access**.
   * Chọn **Custom configuration** -> tích chọn **`LAN routing`** -> **Finish** -> **Start service**.

---

### BƯỚC 5: KIỂM TRA LỆNH PING THÔNG TOÀN MẠNG

Mở **CMD** trên các máy để test:

1. **Trên Win7 (1)**:
   * `ping 192.168.11.1` -> OK
   * `ping 100.100.11.1` -> OK
   * `ping 100.100.11.2` -> **Thành công! (`Reply from 100.100.11.2...`)**

2. **Trên Win7 (2)**:
   * `ping 100.100.11.1` -> OK
   * `ping 192.168.11.1` -> OK
   * `ping 192.168.11.2` -> **Thành công! (`Reply from 192.168.11.2...`)**

---

## 🚨 V. CẢNH BÁO QUAN TRỌNG & BÀI HỌC XỬ LÝ LỖI IP RÁC `169.254.X.X` (APIPA)

### 🔴 Hiện tượng lỗi:
Đã gõ đặt IP tĩnh `192.168.11.1` cho Windows Server nhưng gõ `ipconfig` máy cứ nhảy về IP rác **`169.254.180.154`** và báo **`Autoconfiguration IPv4 Address`**.

### 🔍 Nguyên nhân cốt lõi (Xung đột IP):
Do máy **Win7 (1)** lỡ bị đặt trùng địa chỉ IP thành **`192.168.11.1`** (đúng ra phải là `192.168.11.2`). 
* Khi Windows Server cắm chung mạng `VMnet11` phát hiện địa chỉ `192.168.11.1` đã có máy Win7 (1) chiếm giữ, Windows Server tự động gắn cờ **`AddressState : Duplicate`** (Đụng độ IP) và tự động nhả IP đó ra, giật lùi về dải rác `169.254` để tránh sập mạng.

### 🛠️ Cách khắc phục triệt để:
1. **Tắt máy Win7 (1)** hoặc vào Win7 (1) sửa chuẩn địa chỉ IP thành **`192.168.11.2`**.
2. Ngay khi Win7 (1) nhả địa chỉ `.1` ra, Windows Server sẽ ăn ngay lập tức địa chỉ **`192.168.11.1`** một cách sạch sẽ và ổn định!
