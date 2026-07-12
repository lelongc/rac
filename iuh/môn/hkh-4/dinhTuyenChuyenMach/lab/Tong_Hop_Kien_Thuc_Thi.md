# BÍ KÍP TỪ SỐ 0 ĐẾN KỸ SƯ MẠNG: ĐỊNH TUYẾN CHUYỂN MẠCH

*Tài liệu này được viết theo ngôn ngữ "bình dân" nhất dành cho người chưa biết gì về mạng. Hãy đọc kỹ từng dòng, bạn sẽ hiểu bản chất vấn đề và không bao giờ phải học vẹt các dòng lệnh nữa.*

---

## KIẾN THỨC VỠ LÒNG: ROUTER VÀ ĐỊNH TUYẾN LÀ GÌ?

- **Router (Bộ định tuyến)**: Hãy tưởng tượng Router giống như một **"Trạm điều phối giao thông"**. Khi gói tin (một chiếc xe) mang dữ liệu đi tới ngã tư, Router sẽ nhìn vào địa chỉ đích và chỉ đường cho nó đi tiếp con đường nào là nhanh nhất.
- **IP Address (Địa chỉ IP)**: Số nhà của một thiết bị. (Ví dụ: `192.168.1.10`)
- **Subnet Mask (Mặt nạ mạng)**: Là một con số đi kèm với IP để xác định xem cái nhà đó nằm ở "Quận" nào, "Phường" nào. (Ví dụ: `255.255.255.0` tương đương việc nói rằng khu phố này có tối đa 254 cái nhà).
- **Interface (Cổng mạng)**: Là các chốt gác trên Router. Mỗi cổng phải được cấp một cái IP để làm cửa ngõ (Gateway) cho các máy tính đi qua.

---

## PHẦN 1: LÀM QUEN VỚI THIẾT BỊ CISCO & BẢO MẬT (LAB 1)

### 1. Ba nấc thang quyền lực trên Router Cisco

Khi mới bật Router lên, bạn chỉ là "người dân thường". Để chỉnh sửa được Router, bạn phải thăng cấp dần qua các dòng lệnh:

1. **User Mode (`Router>`)**: Cấp thấp nhất, chỉ ngó nghiêng được vài thứ cơ bản.
2. **Privileged Mode (`Router#`)**: Cấp Quản lý. Tại đây bạn có thể xem (show) mọi thứ trong Router xem nó đang chạy thế nào. Lệnh để leo lên cấp này là: `enable`.
3. **Global Config Mode (`Router(config)#`)**: Cấp cao nhất (Tổng tư lệnh). Tại đây bạn có quyền thêm, sửa, xóa cấu hình. Lệnh để leo lên cấp này là: `configure terminal`.

### 2. Giải thích từng chữ các lệnh bảo mật cơ bản

```bash
# --- Bước 1: Leo lên đỉnh quyền lực ---
enable
configure terminal

# --- Bước 2: Đổi tên thiết bị cho dễ quản lý ---
hostname R1

# --- Bước 3: Khóa cổng bằng Mật khẩu (Tránh người lạ chọc phá) ---
# Đặt mật khẩu để chặn người khác gõ lệnh "enable"
enable secret 1012enable       
# Giải thích: "secret" nghĩa là pass này sẽ được Router băm nát (mã hóa) chứ không lưu dạng chữ thường.

# Đặt mật khẩu cho cổng Console (Cổng cắm dây cáp vật lý trực tiếp vào Router)
line console 0
 password 08092023console        # Đặt pass là 08092023console
 login                           # Bắt buộc phải login mới cho vào

# Đặt mật khẩu cho cổng VTY (Cổng ảo để điều khiển từ xa qua mạng, vd Telnet/SSH)
line vty 0 4                     # Mở 5 luồng cho phép 5 người điều khiển cùng lúc (từ 0 đến 4)
 password 08092023vty
 login
```

### 3. SSH (Secure Shell) là gì?

- **Khái niệm**: Nếu bạn dùng Telnet để điều khiển từ xa, dữ liệu truyền đi là chữ thường, hacker bắt được sẽ đọc được pass của bạn. SSH bọc dữ liệu của bạn vào một "ống sắt" mã hóa, hacker bắt được cũng không đọc được.
- **Lệnh cấu hình SSH**:
  ```bash
  ip domain-name hotensv.net       # SSH bắt buộc phải có tên miền để tạo khóa mã hóa
  crypto key generate rsa          # Lệnh đúc chìa khóa mã hóa
  username svhk1012 password Tel1012@ssh # Tạo 1 tài khoản cho người quản trị

  line vty 0 4
   transport input ssh             # Ra lệnh: "Chỉ cho phép SSH qua cổng này, cấm Telnet"
   login local                     # Bắt buộc đăng nhập bằng tài khoản "svhk1012" vừa tạo
  ```

---

## PHẦN 2: ĐỊNH TUYẾN TĨNH VÀ DEFAULT ROUTE (LAB 1 & LAB 2)

**Định tuyến (Routing) là gì?**
Là quá trình vẽ bản đồ cho Router. Mặc định Router chỉ biết các mạng được cắm dây trực tiếp vào bụng nó. Nó bị "mù" với các mạng ở xa. Do đó ta phải dạy nó.

### 1. Định tuyến tĩnh (Static Route)

- **Bản chất**: Bạn tự tay cầm bút chì vẽ đường cho Router. "Muốn đi tới phường A, thì mày đi qua cái cầu B cho tao".
- **Lệnh**: `ip route [Mạng_Đích] [Subnet_Mask] [IP_Trạm_Tiếp_Theo]`
  - Ví dụ: `ip route 192.168.2.0 255.255.255.0 10.0.0.2`
  - *Giải thích nghĩa đen*: "Ê Router, nếu có ai muốn gửi đồ tới mạng `192.168.2.0`, mày hãy ném gói đồ đó sang cái cổng `10.0.0.2` (IP của con Router bên cạnh), nó sẽ biết làm gì tiếp theo".

### 2. Default Route (Tuyến đường mặc định)

- **Bản chất**: Bạn không thể vẽ tay hàng tỷ tuyến đường ra Internet được. Default Route đóng vai trò là cái **"Thùng rác"** hoặc **"Lối thoát hiểm"**. Nó bảo Router: "Thằng nào hỏi mượn đường mà mày không biết nó ở đâu, cứ tống hết nó qua đường này cho tao".
- **Lệnh**: `ip route 0.0.0.0 0.0.0.0 [IP_Trạm_Tiếp_Theo]`

---

## PHẦN 3: ĐỊNH TUYẾN ĐỘNG RIP (IPv4 & IPv6) (LAB 2)

Vẽ bằng tay (Static Route) rất mệt mỏi nếu mạng quá lớn. Người ta sinh ra Định tuyến động (Dynamic Routing). Lúc này các Router tự động nhắn tin cho nhau, tự trao đổi bản đồ cho nhau.

### 1. Giao thức RIP (Routing Information Protocol)

- **Bản chất**: RIP tìm đường bằng cách đếm "Số trạm phải nhảy qua" (Hop Count). Đường nào nhảy qua ít Router nhất thì RIP cho là đường tốt nhất. Giới hạn tối đa của RIP là 15 trạm, nhảy tới trạm 16 gói đồ sẽ bị vứt đi (Nên RIP chỉ dùng cho mạng nhỏ).
- **Lệnh RIPv2 (Cho IPv4)**:
  ```bash
  router rip                 # Khởi động giao thức RIP
   version 2                 # Dùng bản 2 (bản V1 quá ngu ngốc vì không hiểu mạng bị chia nhỏ)
   no auto-summary           # Bắt buộc có: Cấm RIP tự động gộp các dải IP lại với nhau gây lỗi
   network 192.168.1.0       # Bảo RIP: "Hãy quảng cáo cái mạng 192.168.1.0 của tao cho hàng xóm biết"
   default-information originate # Bảo RIP: "Khoe cho cả làng biết tao là đứa có đường ra Internet"
  ```

### 2. Giao thức RIPng (Cho IPv6)

- **Bản chất**: Cách RIP hoạt động trên địa chỉ IPv6 (Dải địa chỉ dài loằng ngoằng hệ Hexa như 2001:db8::1).
- **Lệnh**:
  ```bash
  ipv6 unicast-routing       # LỆNH MỞ KHÓA: Nếu không gõ lệnh này, Router bị mù IPv6 hoàn toàn

  interface e0/0             # Ở IPv6, ta không dùng lệnh network. Ta chui thẳng vào cổng mạng.
   ipv6 rip abc enable       # Bảo cổng này: "Hãy hòa mạng RIP đi, lấy tên nhóm RIP là 'abc'"
  ```

---

## PHẦN 4: ĐỊNH TUYẾN ĐỘNG OSPF (LAB 3)

### 1. Bản chất của OSPF

- **Metric (Trọng số)**: Nếu RIP đếm số trạm, thì OSPF thông minh hơn, nó dùng **Cost (Chi phí)**. Cổng cáp quang siêu tốc thì Cost thấp (giá đi đường cao tốc rẻ), cổng cáp đồng chậm rì thì Cost cao. OSPF luôn chọn đường có tổng Cost thấp nhất.
- **Chia Vùng (Area)**: OSPF chia mạng thành các Area. **Area 0** là vùng lõi (Thủ đô), các Area khác (Tỉnh lẻ) bắt buộc phải cắm dây vào Area 0 thì mới nói chuyện được với nhau. Việc chia vùng giúp OSPF không bị quá tải trí nhớ.
- **Lệnh OSPF**:
  ```bash
  router ospf 1              # Khởi động OSPF, số 1 là ID tiến trình (không quan trọng lắm)
   network 192.168.1.0 0.0.0.255 area 0 
  # Giải thích: "Tham gia OSPF cho mạng 192.168.1.0, nhét nó vào vùng Thủ đô (area 0)". 
  # Chú ý: 0.0.0.255 là Wildcard Mask (ngược lại của Subnet Mask 255.255.255.0). Nghĩa là 3 số đầu cố định, số cuối chạy từ 0-255.
  ```

### 2. Lớp trưởng DR và Lớp phó BDR

- **Bản chất**: Nếu 10 con Router cùng cắm vào 1 cục Switch, chúng nó sẽ thi nhau gửi bản đồ chéo cho nhau gây tắc nghẽn mạng. Thế là OSPF nghĩ ra trò "Bầu cử". Nó bầu 1 con làm DR (Lớp trưởng) và 1 con làm BDR (Lớp phó). Từ nay, các Router dân đen (DROther) chỉ nộp bản đồ cho Lớp trưởng, Lớp trưởng sẽ cầm loa phát lại cho cả làng nghe.
- **Quy tắc bầu cử**: Con nào có **Router-ID** lớn nhất thì làm Lớp trưởng. Router-ID giống như "Căn cước công dân" của Router, ta có thể tự phong chức cho nó bằng lệnh:
  ```bash
  router ospf 1
   router-id 9.9.9.9         # Ép con này có mã số to nhất để nó chắc chắn lên làm DR
  ```

### 3. Redistribute (Người phiên dịch)

- **Bản chất**: OSPF là tiếng Pháp, RIP là tiếng Anh. 2 vùng mạng này không thể giao tiếp. Ta phải bắt cái con Router đứng giữa (Cắm 1 chân vào vùng OSPF, 1 chân vào vùng RIP) làm người phiên dịch. Kỹ thuật này gọi là **Redistribute (Phân phối lại)**. Con Router đứng giữa này được tôn vinh là **ASBR** (Autonomous System Boundary Router).
- **Lệnh phiên dịch**:
  ```bash
  # Nói với hội tiếng Pháp (OSPF):
  router ospf 1
   redistribute rip subnets  # "Hãy dịch toàn bộ kiến thức của tụi RIP sang tiếng OSPF cho tao"

  # Nói với hội tiếng Anh (RIP):
  router rip
   redistribute ospf 1 metric 2 # "Hãy dịch OSPF sang tiếng RIP. Gán cho nó độ xa là 2 trạm (metric 2) để hội RIP nó hiểu được"
  ```

---

## PHẦN 5: CẨM NANG "BẮT MẠCH BẮT BỆNH" (TROUBLESHOOTING)

Khi thi vấn đáp thực hành, bị hỏi "Chứng minh", hãy thuộc nằm lòng các lệnh gõ ở chế độ Đặc quyền `Router#`:

1. **`show ip interface brief`**

   - **Tác dụng**: Khám sức khỏe các "cổng mạng".
   - **Cách đọc**: Phải thấy chữ `UP` ở cả 2 cột Status và Protocol. Nếu thấy `Administratively Down` nghĩa là bạn quên gõ lệnh `no shutdown` bật cổng. Nếu thấy `UP` - `DOWN` tức là cổng bật rồi nhưng chưa cắm dây mạng, hoặc dây bị đứt.
2. **`show ip route`**

   - **Tác dụng**: Mở bản đồ trong não Router ra xem.
   - **Cách đọc chữ cái đầu dòng**:
     - **C (Connected)**: Đường này cắm trực tiếp vào bụng nó.
     - **S (Static)**: Đường này do con người tự cấu hình bằng tay.
     - **S***: Đường Default Route do con người cấu hình.
     - **R (RIP)**: Học lỏm được từ thằng hàng xóm qua giao thức RIP.
     - **O (OSPF)**: Học được qua giao thức OSPF.
     - **O*E2**: Học được qua OSPF nhưng là mạng Default route do thằng OSPF khác phát tán vào.
   - **Cách đọc thông số trong ngoặc `[110/64]`**: `110` là AD (Độ tin cậy của OSPF). `64` là Metric (Cost của đoạn đường đó).
3. **`show ip ospf neighbor`**

   - **Tác dụng**: Xem danh sách "bạn bè" OSPF của Router.
   - **Cách đọc**: Nếu thấy chữ `FULL/DR`, chứng tỏ thằng bạn mình đang làm Lớp trưởng (Designated Router). Thấy chữ `FULL/BDR` là Lớp phó. Thấy `FULL/ -` nghĩa là mạng cắm cáp Serial thẳng 2 cục với nhau, chả cần bầu lớp trưởng làm gì cho mệt.
4. **`ping [IP]`**

   - **Tác dụng**: Gửi một gói tin dò đường xem mạng có thông không.
   - **Cách đọc**: Thấy dấu chấm than `!!!!!` (trên Router) hoặc Reply (Trên PC) là 100 điểm. Thấy dấu chấm `.....` là đường truyền bị đứt hoặc sai định tuyến. Lỗi ở đâu thì dùng `show ip route` kiểm tra lại ở đó.
