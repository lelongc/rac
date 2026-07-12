# CẨM NANG TOÀN TẬP TỪ SỐ 0: MỌI KIẾN THỨC ĐỂ BẢO VỆ ĐỒ ÁN
*Viết cực kỳ chi tiết dựa trên ĐÚNG nội dung từng bài Lab 1 (5 bài), Lab 2 (5 bài), Lab 3 (5 bài). Giải thích từng lệnh, từng dòng output, mọi khái niệm cho người mất gốc.*

=====================================================================

# CHƯƠNG 0: KIẾN THỨC NỀN TẢNG (ĐỌC TRƯỚC KHI LÀM BẤT KỲ BÀI NÀO)

## 0.1. Router là gì? Switch là gì? PC là gì?
- **Router**: Thiết bị "chỉ đường" cho gói tin. Nó có nhiều cổng mạng, mỗi cổng nối vào một mạng khác nhau. Router quyết định gói tin sẽ đi theo ngã nào.
- **Switch**: Thiết bị "chia luồng" trong cùng 1 mạng LAN. Giống ổ chia điện, cắm nhiều PC vào chung 1 mạng. Switch KHÔNG cần cấu hình IP (trừ khi là Switch Layer 3).
- **PC (VPCS trong EVE-NG)**: Máy tính ảo dùng để test ping, trace.

## 0.2. Địa chỉ IP, Subnet Mask, Gateway
- **IP Address**: Số nhà của thiết bị. Ví dụ `192.168.1.10`.
- **Subnet Mask**: Xác định "khu phố" (mạng) mà IP thuộc về.
  - `255.255.255.0` = `/24` = Khu phố có 254 nhà (từ .1 đến .254).
  - `255.255.255.128` = `/25` = Khu phố bị chia đôi, chỉ còn 126 nhà.
  - `255.255.255.252` = `/30` = Mạng siêu nhỏ chỉ có 2 nhà (dùng nối 2 Router với nhau).
- **Default Gateway**: Cổng thoát. Khi PC muốn gửi đồ ra khỏi khu phố, nó phải đưa cho ông bảo vệ (Gateway = IP của Router gần nhất).
- **Wildcard Mask**: Ngược lại của Subnet Mask. OSPF bắt buộc dùng Wildcard thay vì Subnet Mask.
  - `255.255.255.0` → Wildcard = `0.0.0.255`
  - `255.255.255.252` → Wildcard = `0.0.0.3`

## 0.3. Các chế độ dòng lệnh (CLI Modes)
- `Router>` → **User Mode**: Chỉ xem, không sửa được gì.
- `Router#` → **Privileged Mode**: Xem mọi thứ, chạy lệnh show, ping, trace. Gõ `enable` để vào.
- `Router(config)#` → **Global Config**: Sửa cấu hình toàn bộ Router. Gõ `configure terminal` để vào.
- `Router(config-if)#` → **Interface Config**: Cấu hình 1 cổng cụ thể. Gõ `interface e0/0` để vào.
- `Router(config-router)#` → **Router Config**: Cấu hình giao thức định tuyến. Gõ `router rip` hoặc `router ospf 1`.

## 0.4. Các lệnh "sống còn" phải thuộc lòng
```
enable                       → Leo lên chế độ đặc quyền
configure terminal           → Vào chế độ cấu hình
interface e0/0               → Chui vào cổng Ethernet 0/0
ip address 192.168.1.1 255.255.255.0  → Đặt IP cho cổng
no shutdown                  → Bật cổng lên (mặc định cổng tắt!)
end                          → Thoát về chế độ đặc quyền
write memory (hoặc wr)       → LƯU cấu hình vào ổ cứng (Cực kỳ quan trọng!)
show ip interface brief      → Xem tổng quan trạng thái tất cả cổng
show ip route                → Xem bảng định tuyến (Bản đồ)
show running-config          → Xem toàn bộ cấu hình đang chạy
ping [IP]                    → Gửi gói tin thăm dò xem mạng có thông không
traceroute [IP] (trên Router) hoặc trace [IP] (trên PC) → Xem gói tin đi qua bao nhiêu trạm
```

## 0.5. Đọc hiểu bảng định tuyến (show ip route)
Đây là KỸ NĂNG QUAN TRỌNG NHẤT khi bị vấn đáp. Ví dụ một dòng:
```
R    192.168.4.0/24 [120/2] via 10.0.0.2, 00:00:15, Ethernet0/0
```
- **R**: Ký hiệu giao thức → Học qua RIP.
- **192.168.4.0/24**: Mạng đích (Muốn đi tới khu phố này).
- **[120/2]**: `120` = AD (Độ tin cậy của RIP). `2` = Metric (Phải nhảy qua 2 trạm).
- **via 10.0.0.2**: Trạm tiếp theo phải ném gói tin sang (Next-hop).
- **00:00:15**: Thông tin này cập nhật cách đây 15 giây.
- **Ethernet0/0**: Gói tin chui ra cổng e0/0 của chính Router này.

**Bảng ký hiệu đầy đủ:**
| Ký hiệu | Nghĩa | AD | Giải thích |
|----------|--------|-----|------------|
| C | Connected | 0 | Mạng cắm dây trực tiếp vào Router |
| L | Local | 0 | Chính cái IP của cổng Router đó |
| S | Static | 1 | Người quản trị tự cấu hình bằng tay |
| S* | Static Default | 1 | Đường mặc định (lối thoát hiểm ra Internet) |
| R | RIP | 120 | Học qua giao thức RIP |
| O | OSPF | 110 | Học qua giao thức OSPF (cùng Area) |
| O IA | OSPF Inter-Area | 110 | Học qua OSPF từ Area khác |
| O*E2 | OSPF External | 110 | Default Route học qua OSPF |

**AD nhỏ hơn = Ưu tiên cao hơn.** Nếu có 2 đường đến cùng 1 đích, Router chọn đường có AD thấp hơn.

=====================================================================

# CHƯƠNG 1: LAB TUẦN 1 (5 BÀI)

## Bài 1 (Lab1): Cài đặt EVE-NG
- Chỉ cài đặt phần mềm, không có lệnh cấu hình.

## Bài 2 (Lab1): Cấu hình Bảo mật Router

### Kiến thức cần nắm:
- **`enable password` vs `enable secret`**: Cả 2 đều đặt pass cho chế độ đặc quyền. Nhưng `enable password` lưu pass dạng chữ thường (ai cũng đọc được), còn `enable secret` tự động băm MD5. Khi cả 2 cùng tồn tại, `enable secret` luôn thắng (được ưu tiên hơn).
- **`service password-encryption`**: Mã hóa TẤT CẢ các password đang ở dạng chữ thường trong file cấu hình. Dùng mã hóa Type 7 (yếu hơn MD5 nhưng vẫn tốt hơn để trống).
- **Line Console 0**: Cổng vật lý, cắm dây cáp RJ-45 trực tiếp vào Router.
- **Line VTY 0 4**: 5 đường truy cập ảo, cho phép 5 người cùng lúc điều khiển Router từ xa qua mạng.
- **exec-timeout 3 0**: Tự động ngắt kết nối sau 3 phút 0 giây không thao tác.
- **ip ssh authentication-retries 3**: Cho phép nhập sai tối đa 3 lần rồi khóa.

### Toàn bộ lệnh cấu hình (Đề yêu cầu cho Router East):
```bash
enable
configure terminal
hostname East
service password-encryption          # Mã hóa toàn bộ password

# Bảo mật chế độ đặc quyền
enable password 08092023enable       # Pass enable dạng thường (sẽ bị mã hóa bởi lệnh trên)
enable secret 1012enable             # Pass enable dạng MD5 (luôn thắng, được ưu tiên)

# Bảo mật cổng Console (Cắm cáp trực tiếp)
line console 0
 password 08092023console
 login                               # Bắt buộc nhập pass mới cho vào
 exec-timeout 3 0                    # Tự ngắt sau 3 phút rảnh
 exit

# Cấu hình SSH (Truy cập từ xa mã hóa)
ip domain-name hotensv.net           # SSH BẮT BUỘC phải có tên miền
crypto key generate rsa              # Đúc chìa khóa mã hóa RSA (Chọn 1024 bits)
username svhk1012 privilege 15 secret Tel1012@ssh  # Tạo tài khoản quyền cao nhất
ip ssh authentication-retries 3      # Sai 3 lần thì khóa

# Cấu hình cổng VTY (Cho phép Telnet VÀ SSH từ xa)
line vty 0 4
 password Tel@ssh                    # Pass cho Telnet
 login local                         # Dùng username/password thay vì pass đơn giản
 transport input ssh telnet          # Cho phép cả 2 giao thức
 exit

end
copy running-config startup-config   # Lưu cấu hình vào bộ nhớ vĩnh viễn
```

## Bài 3 (Lab1): Cấu hình IP & Kiểm tra kết nối
### Kiến thức cần nắm:
- Sơ đồ: 3 Router (West, Central, East) nối nhau bằng cáp Serial, mỗi Router nối 1 Switch, mỗi Switch nối 1 PC.
- **Cổng Serial** (s1/0, s1/1): Dùng nối 2 Router với nhau (WAN link). Trên EVE-NG IOL phải bật "Serial portgroups = 1" khi tạo Router.
- **Cổng Ethernet** (e0/0): Dùng nối Router xuống Switch/PC (LAN link).
- **`no shutdown`**: Mặc định cổng của Router bị tắt. PHẢI gõ lệnh này để bật cổng.
- Cấu hình IP trên PC (VPCS): `ip 192.168.0.5/24 192.168.0.1` → Đặt IP .5, subnet /24, gateway .1.

### Lệnh kiểm tra:
- `show ip interface brief`: Xem tất cả cổng có UP chưa. Nếu Status = "administratively down" → Quên gõ `no shutdown`.
- `ping 10.0.0.2`: Test kết nối giữa 2 Router nối trực tiếp. Thấy `!!!!!` = Thành công. Thấy `.....` = Thất bại.

## Bài 4 (Lab1): Định tuyến Tĩnh (Static Routing)
### Kiến thức cần nắm:
- **Tại sao phải định tuyến?** Router chỉ tự biết mạng cắm trực tiếp (Connected). Các mạng ở xa, nó bị "mù". Ta phải chỉ đường cho nó.
- **Cú pháp**: `ip route [Mạng_Đích] [Subnet_Mask] [Next-Hop_IP]`
  - Nghĩa đen: "Muốn đi tới [Mạng_Đích], hãy ném gói tin cho thằng [Next-Hop_IP]".

### Lệnh trên từng Router (Sơ đồ West ↔ Central ↔ East):
```bash
# West: Chỉ biết mạng cắm trực tiếp (192.168.0.0 và 10.0.0.0). Cần chỉ đường tới 3 mạng xa.
ip route 10.0.1.0 255.255.255.0 10.0.0.2      # Mạng nối Central-East, đi qua Central
ip route 192.168.1.0 255.255.255.0 10.0.0.2   # LAN của Central, đi qua Central
ip route 192.168.2.0 255.255.255.0 10.0.0.2   # LAN của East, đi qua Central

# Central: Nằm giữa, chỉ cần chỉ 2 mạng LAN ở 2 bên.
ip route 192.168.0.0 255.255.255.0 10.0.0.1   # LAN West, đi qua West
ip route 192.168.2.0 255.255.255.0 10.0.1.2   # LAN East, đi qua East

# East: Chỉ biết mạng cắm trực tiếp (192.168.2.0 và 10.0.1.0). Cần chỉ đường tới 3 mạng xa.
ip route 10.0.0.0 255.255.255.0 10.0.1.1      # Mạng nối West-Central
ip route 192.168.0.0 255.255.255.0 10.0.1.1   # LAN West
ip route 192.168.1.0 255.255.255.0 10.0.1.1   # LAN Central
```

### Đọc kết quả `show ip route` trên Router West:
```
C    192.168.0.0/24 is directly connected, Ethernet0/0   ← Mạng cắm trực tiếp
C    10.0.0.0/24 is directly connected, Serial1/0         ← Mạng cắm trực tiếp
S    192.168.1.0/24 [1/0] via 10.0.0.2                    ← Static route, AD=1
S    192.168.2.0/24 [1/0] via 10.0.0.2                    ← Static route, AD=1
S    10.0.1.0/24 [1/0] via 10.0.0.2                       ← Static route, AD=1
```
→ Chữ **S** = Static (Cấu hình bằng tay). `[1/0]` = AD=1, Metric=0.

### Đọc kết quả `traceroute` từ PC1 tới PC3 (192.168.2.5):
```
trace to 192.168.2.5
1  192.168.0.1    ← Hop 1: Gateway của PC1 (Router West)
2  10.0.0.2       ← Hop 2: Router Central
3  10.0.1.2       ← Hop 3: Router East
4  192.168.2.5    ← Đích: PC3
```
→ Chứng minh gói tin đi qua 3 trạm (West → Central → East → PC3).

## Bài 5 (Lab1): Static Routing + Internet + Default Route
### Kiến thức cần nắm:
- **Default Route**: `ip route 0.0.0.0 0.0.0.0 [Next-Hop]` → "Mọi thứ không biết đi đâu thì ném qua đây".
- Sơ đồ mở rộng: Thêm Router Internet nối vào Central. Mạng WAN Central↔Internet dùng dải `10.0.2.0/24`, mạng LAN Internet dùng `192.168.3.0/24`.

### Chiến lược định tuyến:
- **West & East** (2 con ở rìa): Chỉ cần 1 lệnh Default Route trỏ về Central là đủ. Vì mọi gói tin muốn đi đâu cũng phải qua Central.
- **Central** (Trung tâm): Default Route trỏ lên Internet. Static Route trỏ xuống LAN West và LAN East.
- **Router Internet**: Static Route trỏ ngược về mạng nội bộ qua Central.

=====================================================================

# CHƯƠNG 2: LAB TUẦN 2 (5 BÀI)

## Bài 1 (Lab2): Định tuyến RIP Version 1
### Kiến thức cần nắm:
- **RIP (Routing Information Protocol)**: Giao thức định tuyến ĐỘNG. Router tự động trao đổi bảng định tuyến với nhau mỗi 30 giây. Không cần con người chỉ tay nữa.
- **Metric = Hop Count**: RIP đếm số Router phải nhảy qua. Đường nào nhảy ít nhất = Tốt nhất. Tối đa 15 hop (hop 16 = vô cực = vứt gói tin).
- **RIP v1**: Classful (Không gửi Subnet Mask kèm). Chỉ hiểu mạng chuẩn (Lớp A, B, C).

### Lệnh cấu hình RIPv1 (Trên Router West):
```bash
router rip                    # Bật RIP
 version 1                    # Dùng Version 1
 network 192.168.0.0          # "Quảng bá mạng 192.168.0.0 cho hàng xóm"
 network 10.0.0.0             # "Quảng bá mạng 10.0.0.0 cho hàng xóm"
```
**Giải thích lệnh `network`**: KHÔNG phải đặt IP. Mà là bảo RIP: "Hãy gửi bản đồ mạng này cho các Router hàng xóm. Đồng thời lắng nghe bản đồ từ các cổng thuộc mạng này."

### Đọc `show ip route` (Sau khi RIP hội tụ):
```
R    192.168.2.0/24 [120/2] via 10.0.0.2    ← Học qua RIP, nhảy 2 trạm
```
→ Chữ **R** = RIP. `[120/2]` = AD=120, Metric=2 hop.

## Bài 2 (Lab2): RIPv2 + VLSM + Internet + ACL
### Kiến thức cần nắm:
- **RIPv2**: Gửi Subnet Mask kèm theo (Classless). Hỗ trợ VLSM.
- **VLSM (Variable Length Subnet Masking)**: Chia mạng thành các khu phố to nhỏ khác nhau.
  - Ví dụ bài này: `222.100.100.0/25` (126 máy), `222.100.100.128/26` (62 máy), `222.100.100.192/27` (30 máy).
- **`no auto-summary`**: BẮT BUỘC có ở RIPv2. Nếu không, RIP tự gộp mạng con về mạng gốc, gây lỗi sai tuyến đường.
- **`default-information originate`**: Lệnh "Cầm loa hét": "Tao biết đường ra Internet, cả làng đi theo tao!". Phát tán Default Route cho toàn mạng RIP.
- **ACL (Access Control List)**: Bộ lọc gói tin. Cho phép (permit) hoặc chặn (deny) gói tin dựa theo IP nguồn.
  - `ip access-list standard 10` → Tạo ACL tên/số 10.
  - `permit 222.100.100.0 0.0.0.127` → Cho mạng /25 của West đi qua.
  - `deny any` → Chặn tất cả phần còn lại (Chặn East ra Internet).
  - `ip access-group 10 out` → Áp ACL lên cổng ra Internet.
- **Loopback Interface**: Cổng ảo trên Router, không cần cắm dây. Dùng để giả lập server hoặc mạng Internet (ví dụ `interface loopback 0` / `ip address 8.8.8.8 255.255.255.255`).

### Lệnh RIPv2 (Trên Router West):
```bash
router rip
 version 2                    # Dùng Version 2 (Classless)
 no auto-summary              # CẤM tự gộp mạng
 network 222.100.100.0        # Quảng bá mạng LAN
 network 220.100.100.32       # Quảng bá mạng WAN nối Central
```

## Bài 3 (Lab2): RIPng (IPv6)
### Kiến thức cần nắm:
- **IPv6**: Địa chỉ thế hệ mới, dạng hexa (ví dụ `2001:db8:0:10::1/64`). Ra đời vì IPv4 sắp hết số.
- **`ipv6 unicast-routing`**: LỜI THỀ BẮT BUỘC. Nếu không gõ lệnh này, Router bị "mù" IPv6 hoàn toàn, mọi cấu hình IPv6 sau đó đều vô nghĩa.
- **RIPng khác RIP IPv4**: Ở IPv4, ta dùng lệnh `network` trong mode `router rip`. Ở IPv6, ta KHÔNG dùng `network`. Thay vào đó, ta chui vào TỪNG CỔNG và gõ lệnh `ipv6 rip [tên] enable`.

### Lệnh RIPng:
```bash
ipv6 unicast-routing                  # BẮT BUỘC: Mở khóa IPv6

interface e0/0
 ipv6 address 2001:db8:0:10::1/64    # Đặt IPv6 cho cổng
 ipv6 rip MYRIPNG enable              # Bật RIPng trên cổng này (tên nhóm tùy đặt)
```

### Xem bảng định tuyến IPv6: `show ipv6 route`

## Bài 4 (Lab2): RIPv2 Vòng (Ring Topology) + Failover
### Kiến thức cần nắm:
- **Ring Topology**: 4 Router nối thành vòng tròn (R1↔R2↔R4↔R3↔R1). Tạo ra 2 đường đi cho mỗi cặp nguồn-đích.
- **Failover (Chuyển dự phòng)**: Khi 1 sợi dây bị đứt, RIP tự động tính toán lại và tìm đường đi vòng thay thế. Mạng KHÔNG bị sập.
- **Lệnh `shutdown`**: Tắt cổng mạng (Giả lập cắt cáp). `no shutdown` = Bật lại.

### Cách giải thích Failover cho thầy cô:
1. Bình thường: `trace 192.168.3.10` → VPC5 → R1 → R3 → VPC7 (Đi tắt, 1 hop).
2. Cắt cáp R1↔R3: Gõ `interface e0/2` → `shutdown` trên R1.
3. Chờ 30-60 giây cho RIP hội tụ lại.
4. Trace lại: VPC5 → R1 → **R2 → R4** → R3 → VPC7 (Đi vòng, 3 hop).
5. Bảng định tuyến thay đổi: `R 192.168.3.0/24 [120/2] via 10.0.12.2` (Metric tăng từ 1 lên 2).

## Bài 5 (Lab2): RIP chọn đường ngắn nhất (Hop Count)
### Kiến thức cần nắm:
- Bổ sung thêm 1 sợi cáp nối thẳng West↔East. Lúc này có 2 đường đi từ West đến LAN East:
  - Đường 1: West → Central → East (2 hop).
  - Đường 2: West → East (1 hop) ← **ĐI TẮT**.
- RIP luôn chọn đường có **Hop Count nhỏ nhất** → Chọn đường 2.
- Kết quả `show ip route`: `R 192.168.2.0/24 [120/1] via 10.0.2.1` (Metric = 1 hop, đi tắt).
- Trace: `PC_West → Router West → Router East → PC_East` (Bỏ qua Central).

=====================================================================

# CHƯƠNG 3: LAB TUẦN 3 (5 BÀI)

## Bài 1 (Lab3): OSPF Đơn vùng (Single Area)
### Kiến thức cần nắm:
- **OSPF**: Giao thức Link-State. Thông minh hơn RIP vì dùng **Cost** (dựa trên băng thông) thay vì Hop Count.
- **Area 0**: Vùng lõi (Backbone). Trong bài đơn vùng, tất cả Router đều ở Area 0.
- **Wildcard Mask**: OSPF bắt buộc dùng Wildcard (ngược Subnet Mask). `255.255.255.0` → `0.0.0.255`.

### Lệnh OSPF cơ bản:
```bash
router ospf 1                                # Bật OSPF (Process ID = 1, chọn số nào cũng được)
 network 192.168.1.0 0.0.0.255 area 0        # Quảng bá mạng LAN vào Area 0
 network 10.0.0.0 0.0.0.255 area 0           # Quảng bá mạng WAN vào Area 0
```

### Đọc kết quả `show ip route`:
```
O    192.168.2.0/24 [110/74] via 10.0.0.2    ← Học qua OSPF, Cost=74
```
→ Chữ **O** = OSPF. `[110/74]` = AD=110, Cost=74.

## Bài 2 (Lab3): OSPF Đa vùng (Multi-Area)
### Kiến thức cần nắm:
- **Tại sao chia Area?** Mạng lớn quá → Router xử lý chậm. Chia thành Area 0 (Trung tâm), Area 1, Area 2 (Ngoại vi) để giảm tải.
- **Quy tắc**: Mọi Area PHẢI nối trực tiếp vào Area 0.
- **ABR (Area Border Router)**: Router đứng giữa 2 Area, có 1 chân ở Area 0 và 1 chân ở Area khác.

### Đọc `show ip route` trên Router ngoại vi:
```
O IA  192.168.1.0/24 [110/84] via ...   ← "IA" = Inter-Area, học từ Area khác
```

## Bài 3 (Lab3): OSPF Đơn vùng nâng cao
### Kiến thức cần nắm:
- Tương tự Bài 1, nhưng có thêm Internet.

## Bài 4 (Lab3): OSPF Multi-Area + DHCP + DR/BDR + MD5 + Load Balancing
### Đây là bài PHỨC TẠP NHẤT, có nhiều kiến thức nhất:

### 4a. DHCP & DHCP Relay (ip helper-address)
- **DHCP**: Cấp IP tự động cho PC. Router R3 đóng vai DHCP Server.
- **Vấn đề**: PC ở mạng R1 muốn xin IP từ R3. Nhưng gói xin IP là gói Broadcast, mà Router KHÔNG cho Broadcast đi qua.
- **Giải pháp**: Dùng lệnh `ip helper-address 192.168.123.3` trên cổng LAN của R1. Lệnh này biến R1 thành "Đại lý DHCP" (Relay), bắt gói Broadcast, chuyển thành Unicast, gửi thẳng cho R3.
```bash
# Trên R3 (DHCP Server):
ip dhcp pool LAN_R1
 network 192.168.1.0 255.255.255.0
 default-router 192.168.1.1

# Trên R1 (Relay Agent):
interface e0/1
 ip helper-address 192.168.123.3   # IP của R3
```

### 4b. Bầu chọn DR/BDR
- **Khi nào bầu?** Khi nhiều Router cắm chung vào 1 Switch (Broadcast network). Ở bài này: R1, R2, R3 cùng cắm vào Switch R5 qua mạng 192.168.123.0/24.
- **DR (Designated Router)**: Lớp trưởng, nhận bảng định tuyến từ mọi người rồi phát lại.
- **BDR (Backup DR)**: Lớp phó, dự phòng nếu DR chết.
- **DROther**: Các Router còn lại, dân thường.
- **Tiêu chí bầu**: Priority cao nhất → Nếu hòa → Router-ID lớn nhất.
- **Router-ID**: "Căn cước" của Router trong OSPF.
```bash
router ospf 1
 router-id 3.3.3.3              # Ép Router-ID = 3.3.3.3 (Lớn nhất → Trúng DR)
```

### Lệnh kiểm tra: `show ip ospf neighbor`
```
Neighbor ID   Pri  State       Dead Time  Address          Interface
2.2.2.2        1   FULL/BDR    00:00:32   192.168.123.2    Ethernet0/0
3.3.3.3        1   FULL/DR     00:00:36   192.168.123.3    Ethernet0/0
```
→ R3 (ID 3.3.3.3) làm **DR**. R2 (ID 2.2.2.2) làm **BDR**. R1 là DROther.

### 4c. Xác thực MD5
- **Tại sao?** Chống hacker cắm Router lạ vào mạng để tiêm tuyến đường giả.
- **Cách hoạt động**: 2 Router phải khớp Key MD5 thì mới chịu kết bạn (Neighbor).
```bash
interface e0/0
 ip ospf authentication message-digest           # Bật chế độ xác thực MD5
 ip ospf message-digest-key 1 md5 cisco          # Key số 1, password là "cisco"
```
- Lệnh `show ip ospf interface e0/0` → Dòng `Message digest authentication enabled` xác nhận đã bật.

### 4d. Cân bằng tải (Load Balancing / ECMP)
- **Bản chất**: Khi có 2 đường đi đến cùng 1 đích có TỔNG COST BẰNG NHAU, OSPF sẽ đưa cả 2 đường vào bảng định tuyến và chia đều gói tin 50-50.
- **Cách ép Cost**: Dùng lệnh `ip ospf cost [số]` trên cổng mạng.
```bash
interface e0/0
 ip ospf cost 74                # Ép Cost cổng này = 74
```
- Nếu đường 1 (e0/0 cost 74 + 10 = 84) = Đường 2 (s1/0 cost 84) → Load Balancing.
- Kết quả `show ip route`: Xuất hiện 2 dòng cùng trỏ đến 1 mạng đích.

### 4e. Default Route ra Internet (OSPF)
```bash
# Trên R4 (Cắm ra Internet):
ip route 0.0.0.0 0.0.0.0 [IP_Internet]       # Tạo Default Route tĩnh
router ospf 1
 default-information originate                 # Phát tán Default Route cho cả mạng OSPF
```
- Kết quả: Trên các Router khác xuất hiện dòng `O*E2 0.0.0.0/0 [110/1] via ...`
- **O*E2**: External Type 2, Default Route nhận từ OSPF bên ngoài.

## Bài 5 (Lab3): Redistribute OSPF ↔ RIP
### Kiến thức cần nắm:
- **Sơ đồ**: R1 (OSPF) ↔ R2 (OSPF + RIP) ↔ R3 (RIP) ↔ R4 (RIP).
- **R2 = ASBR**: Autonomous System Boundary Router, con "Phiên dịch" đứng giữa 2 vùng.
- **Redistribute**: Dịch ngôn ngữ OSPF sang RIP và ngược lại.

### Lệnh Redistribute trên R2:
```bash
# Nạp mạng RIP vào OSPF (Để vùng OSPF thấy được mạng RIP)
router ospf 1
 redistribute rip subnets        # "subnets" = dịch cả mạng con chứ đừng gộp lại

# Nạp mạng OSPF vào RIP (Để vùng RIP thấy được mạng OSPF)
router rip
 redistribute ospf 1 metric 2   # "metric 2" = Nói dối RIP rằng mạng OSPF cách 2 hop
```

### Đọc `show ip route` trên R2 (Chứng minh Redistribute thành công):
```
O    192.168.1.0/24 [110/74] via 12.12.12.1    ← Học từ OSPF (Mạng LAN R1)
R    192.168.4.0/24 [120/1] via 23.23.23.2     ← Học từ RIP (Mạng LAN R3)
C    12.12.12.0/30 is directly connected        ← Nối trực tiếp
C    23.23.23.0/30 is directly connected        ← Nối trực tiếp
```
→ R2 vừa có chữ **O** (OSPF) vừa có chữ **R** (RIP) = Phiên dịch thành công!

### Đọc `show ip route` trên R4 (Router mới thêm):
```
R    192.168.1.0/24 [120/3] via 34.34.34.1     ← Học qua RIP, Metric=3 hop
R    192.168.0.0/24 [120/3] via 34.34.34.1
R    12.12.12.0/30 [120/2] via 34.34.34.1
```
→ Mặc dù R4 chỉ chạy RIP, nhưng vẫn thấy được mạng OSPF (192.168.1.0) nhờ R2 đã Redistribute. Metric = 3 hop vì gói tin phải nhảy R4→R3→R2→R1.

=====================================================================

# CHƯƠNG 4: CÁC CÂU HỎI VẤN ĐÁP "HACK NÃO" CỦA THẦY CÔ

**Q: Tại sao AD của OSPF (110) lại nhỏ hơn RIP (120)?**
A: Vì OSPF thông minh hơn RIP. AD nhỏ = Ưu tiên cao hơn. Nếu 1 Router đồng thời học được 1 mạng qua cả OSPF và RIP, nó sẽ chọn OSPF.

**Q: Lệnh `no auto-summary` trong RIP để làm gì?**
A: RIPv2 có tật tự gộp mạng con về lớp mạng gốc. Ví dụ mạng `192.168.1.0/24` và `192.168.2.0/24` bị gộp thành `192.168.0.0/16`. Gây ra lỗi định tuyến sai. Lệnh này cấm RIP tự gộp.

**Q: `enable password` và `enable secret` khác nhau thế nào?**
A: `enable password` lưu dạng text thường. `enable secret` tự động mã hóa MD5. Khi cả 2 cùng tồn tại, `secret` luôn thắng.

**Q: Wildcard Mask là gì? Tại sao OSPF dùng Wildcard mà không dùng Subnet Mask?**
A: Wildcard = Đảo ngược từng bit của Subnet Mask. `255.255.255.0` → `0.0.0.255`. OSPF dùng Wildcard vì thiết kế ban đầu của Cisco cho phép linh hoạt hơn khi chọn dải IP cần quảng bá.

**Q: Nếu ngắt cáp giữa 2 Router, mạng có sập không?**
A: Tùy. Nếu dùng Static Route → SẬP (vì Router không biết tự tìm đường mới). Nếu dùng RIP hoặc OSPF → KHÔNG SẬP (giao thức tự hội tụ lại, tìm đường vòng thay thế, mất khoảng 30-60 giây).

**Q: `default-information originate` dùng khi nào?**
A: Khi có 1 Router nắm đường ra Internet, muốn chia sẻ thông tin này cho toàn mạng. Gõ lệnh này trong mode `router rip` hoặc `router ospf`, lập tức các Router khác sẽ xuất hiện dòng Default Route tự động.

**Q: DHCP Relay (`ip helper-address`) hoạt động thế nào?**
A: PC gửi gói xin IP = Broadcast → Router bắt được → Chuyển thành Unicast → Gửi thẳng đến IP DHCP Server.

**Q: Cost OSPF tính thế nào?**
A: Công thức gốc: Cost = 10^8 / Bandwidth. Cổng FastEthernet 100Mbps → Cost = 10. Cổng Serial 1.544Mbps → Cost = 64. Ta có thể tự ép Cost bằng lệnh `ip ospf cost [số]`.

**Q: Phân biệt `show ip route` với `show ip protocols`?**
A: `show ip route` hiển thị bảng định tuyến (Bản đồ đường đi). `show ip protocols` hiển thị giao thức đang chạy (RIP hay OSPF), Timer bao lâu gửi 1 lần, các mạng đang quảng bá.
