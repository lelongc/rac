# HƯỚNG DẪN CẤU HÌNH LAB 1: ĐỊNH TUYẾN (ROUTING) - BẢN CẬP NHẬT DẢI IP 11

> 📌 **BÀI TOÁN**: Cấu hình định tuyến giữa 2 dải mạng:
> * Mạng 1 (VMnet11): Dải IP **`192.168.11.0/24`**
> * Mạng 2 (VMnet12): Dải IP **`100.100.11.0/24`**

---

## I. THÔNG TIN MÔ HÌNH VÀ PHÂN HOẠCH IP MỚI

```
[Win7 (1)] <------ VMnet11 ------> [ Windows Server ] <------ VMnet12 ------> [Win7 (2)]
192.168.11.2                       Card 1: 192.168.11.1                       100.100.11.2
                                   Card 2: 100.100.11.1
```

### Bảng thông số chi tiết:

| Tên máy ảo | Card mạng VMware | Địa chỉ IP | Subnet Mask | Default Gateway |
| :--- | :--- | :--- | :--- | :--- |
| **Win7 (1)** | Custom: `VMnet11` | **`192.168.11.2`** | `255.255.255.0` | **`192.168.11.1`** |
| **Windows Server** | Card 1: `VMnet11` | **`192.168.11.1`** | `255.255.255.0` | *Để trống* |
| | Card 2: `VMnet12` | **`100.100.11.1`** | `255.255.255.0` | *Để trống* |
| **Win7 (2)** | Custom: `VMnet12` | **`100.100.11.2`** | `255.255.255.0` | **`100.100.11.1`** |

---

## BƯỚC 1: CẤU HÌNH MẠNG ẢO (VIRTUAL NETWORK EDITOR) TRÊN VMWARE

1. Vào VMware Workstation trên máy thật -> menu **Edit** -> chọn **Virtual Network Editor...**
2. Nhấn nút **Change Settings** (nếu cần quyền Admin).
3. **Cấu hình VMnet11**:
   * Chọn **VMnet11** -> tích **Host-only**.
   * **Subnet IP**: `192.168.11.0` | **Subnet mask**: `255.255.255.0`.
   * Bỏ tích *Use local DHCP service to distribute IP to VMs*.
4. **Cấu hình VMnet12**:
   * Chọn **VMnet12** -> tích **Host-only**.
   * **Subnet IP**: `100.100.11.0` | **Subnet mask**: `255.255.255.0`.
   * Bỏ tích *Use local DHCP service to distribute IP to VMs*.
5. Nhấn **Apply** -> **OK**.

---

## BƯỚC 2: GÁN CARD MẠNG TRÊN CÁC MÁY ẢO

1. **Win7 (1)**: Chuột phải chọn Settings -> Network Adapter -> Chọn **Custom: `VMnet11`**.
2. **Windows Server**: 
   * Card 1: Chọn **Custom: `VMnet11`**.
   * Card 2 (Add thêm): Chọn **Custom: `VMnet12`**.
3. **Win7 (2)**: Chuột phải chọn Settings -> Network Adapter -> Chọn **Custom: `VMnet12`**.

---

## BƯỚC 3: ĐẶT IP TĨNH CHÍNH XÁC CHO TỪNG MÁY

### 1. Trên máy Win7 (1):
* Vào `Control Panel` -> `Network and Sharing Center` -> `Change adapter settings`.
* Chuột phải `Local Area Connection` -> **Properties** -> `TCP/IPv4`:
  * **IP address**: `192.168.11.2`
  * **Subnet mask**: `255.255.255.0`
  * **Default gateway**: `192.168.11.1`

### 2. Trên máy Windows Server:
* Vào `Change adapter settings`:
* **Card 1 (`VMnet11`)**:
  * IP address: `192.168.11.1`
  * Subnet mask: `255.255.255.0`
  * Default gateway: *ĐỂ TRỐNG*
* **Card 2 (`VMnet12`)**:
  * IP address: `100.100.11.1`
  * Subnet mask: `255.255.255.0`
  * Default gateway: *ĐỂ TRỐNG*

### 3. Trên máy Win7 (2):
* Vào `Control Panel` -> `Network and Sharing Center` -> `Change adapter settings`.
* Chuột phải `Local Area Connection` -> **Properties** -> `TCP/IPv4`:
  * **IP address**: `100.100.11.2`
  * **Subnet mask**: `255.255.255.0`
  * **Default gateway**: `100.100.11.1`

---

## BƯỚC 4: TẮT WINDOWS FIREWALL TRÊN CẢ 3 MÁY

* Trên cả **Win7 (1)**, **Windows Server**, và **Win7 (2)**:
  1. Vào **Control Panel** -> **Windows Firewall**.
  2. Chọn **Turn Windows Firewall on or off**.
  3. Chọn **Turn off Windows Firewall** ở tất cả các vị trí -> Nhấn **OK**.

---

## BƯỚC 5: CẤU HÌNH DỊCH VỤ ROUTING (RRAS) TRÊN SERVER

1. **Cài Role Remote Access**:
   * Vào **Server Manager** -> **Manage** -> **Add Roles and Features**.
   * Chọn Role **`Remote Access`** -> ở bước Role Services tích chọn **`Routing`** -> **Install**.
2. **Kích hoạt LAN Routing**:
   * Vào **Server Manager** -> **Tools** -> **Routing and Remote Access**.
   * Chuột phải tên Server -> **Configure and Enable Routing and Remote Access**.
   * Chọn **Custom configuration** -> tích chọn **`LAN routing`** -> **Finish** -> **Start service**.

---

## BƯỚC 6: KIỂM TRA LỆNH PING

Mở **CMD** trên các máy để test:

1. **Trên Win7 (1)**:
   * `ping 192.168.11.1` -> OK
   * `ping 100.100.11.1` -> OK
   * `ping 100.100.11.2` -> **Thành công! (`Reply from 100.100.11.2...`)**

2. **Trên Win7 (2)**:
   * `ping 100.100.11.1` -> OK
   * `ping 192.168.11.1` -> OK
   * `ping 192.168.11.2` -> **Thành công! (`Reply from 192.168.11.2...`)**
