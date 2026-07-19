# ĐỀ THI CUỐI KỲ - ĐỊNH TUYẾN CHUYỂN MẠCH (DHCNTT18)
# Ngày thi: T13-14, 06/11/2025 | Thời gian: 70 phút | Được sử dụng tài liệu giấy

=====================================================================
CÂU 1 (2 điểm - CLO 02): CẤU HÌNH BẢO MẬT ROUTER
=====================================================================

ĐỀ BÀI:
1. Line Console yêu cầu password: 052025console
2. Enable mode yêu cầu pass: 2710enable (mã hóa)
3. Telnet và SSH:
   a. SSH domain: ck2025.net, Username: user2025, Password: Tel@ssh25, toàn quyền
   b. Không sử dụng trong 02 phút -> ngắt. Đăng nhập sai tối đa 03 lần
4. Toàn bộ password phải được mã hóa

---------------------------------------------------------------------
BÀI GIẢI CÂU 1:
---------------------------------------------------------------------

enable
configure terminal

! 0. Đổi hostname (BẮT BUỘC để tạo RSA key cho SSH)
hostname R1

! 1. Mã hóa toàn bộ password
service password-encryption

! 2. Line Console
line console 0
 password 052025console
 login
 exit

! 3. Enable mode (mã hóa)
enable secret 2710enable

! 4a. SSH
ip domain-name ck2025.net
crypto key generate rsa modulus 1024
username user2025 privilege 15 secret Tel@ssh25

! 4b. VTY (Telnet + SSH)
line vty 0 4
 login local
 transport input ssh telnet
 exec-timeout 2 0
 exit

! 4c. Giới hạn đăng nhập sai
ip ssh authentication-retries 3

end
write memory

GIẢI THÍCH TỪNG DÒNG:
- hostname R1             : BẮT BUỘC đổi tên trước khi crypto key, nếu không RSA bị từ chối
- service password-encryption : Mã hóa tất cả password plaintext (type 7)
- enable secret           : Tự động mã hóa MD5 (type 5), mạnh hơn enable password
- login (console)         : Kích hoạt yêu cầu nhập password khi kết nối Console
- login local (vty)       : Xác thực bằng username/password cục bộ
- privilege 15            : Cấp toàn quyền cho user
- transport input ssh telnet : Cho phép cả SSH và Telnet kết nối từ xa
- exec-timeout 2 0       : Tự động ngắt sau 2 phút 0 giây không hoạt động
- ip ssh authentication-retries 3 : Sau 3 lần nhập sai -> khóa phiên SSH


=====================================================================
CÂU 2 (6 điểm - CLO 2,3): ĐỊNH TUYẾN + ACL
=====================================================================

ĐỀ BÀI (đọc từ sơ đồ):
- Vùng RIP (trái): R2 + SwitchServer + VPC_Vlan_11 + VPC_Vlan_12
  VLAN 11: 192.168.11.0/24
  VLAN 12: 192.168.12.0/24
  R2 (s1/0) nối R1 (s1/0): mạng 228.224.11.0/30
- R1 (trung tâm): Internet (e0/0) + Redistribution OSPF <-> RIP
- Vùng OSPF (phải): R3 + VPC + LocalServerWebFile
  R1 (s1/1) nối R3 (s1/1): mạng 228.224.11.16/30
  R3 (e0/0): 172.16.30.0/24 (Server IP: 172.16.30.10)
  R3 (e0/1): 172.16.31.0/24 (VPC)

YÊU CẦU:
1. (4đ) Định tuyến thông mạng: VLAN, OSPF, RIP, OSPF <-> RIP, Internet
2. (2đ) ACL:
   a. Cho phép PC vùng OSPF truy cập FTP Server 172.16.30.10
   b. Cấm VLAN 11 dùng dịch vụ Web trên Server 172.16.30.10

LƯU Ý ĐỀ: Router và VPC đã gán IP, VLAN Database đã tồn tại
           nhưng CHƯA định tuyến các VLAN, CHƯA gán IP vào VLAN.

---------------------------------------------------------------------
BÀI GIẢI CÂU 2:
---------------------------------------------------------------------

=== 1. SwitchServer ===
enable
configure terminal
interface e0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
 no shutdown
interface e0/2
 switchport mode access
 switchport access vlan 11
 no shutdown
interface e0/1
 switchport mode access
 switchport access vlan 12
 no shutdown
end
write memory

=== 2. R2 (Router-on-a-stick + RIP) ===
enable
configure terminal
interface e0/0
 no shutdown
interface e0/0.11
 encapsulation dot1Q 11
 ip address 192.168.11.1 255.255.255.0
interface e0/0.12
 encapsulation dot1Q 12
 ip address 192.168.12.1 255.255.255.0
interface s1/0
 ip address 228.224.11.1 255.255.255.252
 no shutdown

router rip
 version 2
 no auto-summary
 network 192.168.11.0
 network 192.168.12.0
 network 228.224.11.0
end
write memory

=== 3. R1 (Trung tâm - Redistribution + NAT) ===
enable
configure terminal
interface s1/0
 ip address 228.224.11.2 255.255.255.252
 ip nat inside
 no shutdown
interface s1/1
 ip address 228.224.11.17 255.255.255.252
 ip nat inside
 no shutdown
interface e0/0
 ip address dhcp
 ip nat outside
 no shutdown

access-list 1 permit any
ip nat inside source list 1 interface e0/0 overload

router rip
 version 2
 no auto-summary
 network 228.224.11.0
 redistribute ospf 1 metric 2
 default-information originate

router ospf 1
 network 228.224.11.16 0.0.0.3 area 0
 redistribute rip subnets
 default-information originate

end
write memory

=== 4. R3 (OSPF) ===
enable
configure terminal
interface s1/1
 ip address 228.224.11.18 255.255.255.252
 no shutdown
interface e0/0
 ip address 172.16.30.1 255.255.255.0
 no shutdown
interface e0/1
 ip address 172.16.31.1 255.255.255.0
 no shutdown

router ospf 1
 network 228.224.11.16 0.0.0.3 area 0
 network 172.16.30.0 0.0.0.255 area 0
 network 172.16.31.0 0.0.0.255 area 0
end
write memory

=== 5. IP CÁC VPC ===
VPC_of_Vlan_11:  ip 192.168.11.10 255.255.255.0 192.168.11.1
VPC_of_Vlan_12:  ip 192.168.12.10 255.255.255.0 192.168.12.1
VPC (OSPF):      ip 172.16.31.10 255.255.255.0 172.16.31.1
Server (đã có):  ip 172.16.30.10 255.255.255.0 172.16.30.1

=== 6. ACL ===

PHÂN TÍCH:
- 2a: Cho phép FTP từ OSPF -> Server = permit tcp ... eq ftp, eq ftp-data
- 2b: Cấm VLAN 11 dùng Web -> Server = deny tcp ... eq 80, eq 443
- Extended ACL đặt GẦN NGUỒN -> Trên R1 interface s1/0 (in) lọc traffic từ RIP

Trên R1:
enable
configure terminal
ip access-list extended ACL_SERVER
 deny tcp 192.168.11.0 0.0.0.255 host 172.16.30.10 eq 80
 deny tcp 192.168.11.0 0.0.0.255 host 172.16.30.10 eq 443
 permit ip any any
exit
interface s1/0
 ip access-group ACL_SERVER in
exit
end
write memory

GIẢI THÍCH LOGIC ACL:
1. deny tcp 192.168.11.0 0.0.0.255 host 172.16.30.10 eq 80
   -> Chặn VLAN 11 gửi HTTP (port 80) tới Server
2. deny tcp 192.168.11.0 0.0.0.255 host 172.16.30.10 eq 443
   -> Chặn VLAN 11 gửi HTTPS (port 443) tới Server
3. permit ip any any
   -> Cho tất cả còn lại đi qua (gồm FTP từ OSPF, ping, Internet)

LƯU Ý: Yêu cầu 2a "cho phép FTP từ OSPF" đã thỏa mãn mặc định vì
không có luật nào chặn FTP. Dòng "permit ip any any" đã bao gồm FTP.


=====================================================================
CÂU 3 (2 điểm - CLO 3): GIẢI THÍCH ACL LÝ THUYẾT
=====================================================================

ĐỀ BÀI 3.1:
Cho sơ đồ: VPC2 (172.16.3.0) -> Router1 (e0/0, e0/1, e0/3) -> WebServer (172.16.4.5)

  Router1(config)# access-list 1 permit 172.16.3.0 0.0.0.15
  Router1(config)# interface ethernet 0/3
  Router1(config-if)# ip access-group 1 out

---------------------------------------------------------------------
BÀI GIẢI CÂU 3.1:
---------------------------------------------------------------------

LOẠI ACL: Standard ACL (số hiệu 1, nằm trong khoảng 1-99)

CÔNG DỤNG: Lọc lưu lượng dựa trên ĐỊA CHỈ IP NGUỒN.
Chỉ cho phép IP từ 172.16.3.0 đến 172.16.3.15 (16 IP) gửi gói tin
ra cổng e0/3 hướng tới WebServer. IP khác bị chặn bởi implicit deny.

PHÂN TÍCH TỪNG THÀNH PHẦN:
- access-list    : Lệnh khai báo danh sách kiểm soát truy cập
- 1              : Số hiệu ACL. Standard ACL (1-99) chỉ lọc IP nguồn
- permit         : Hành động cho phép gói tin đi qua
- 172.16.3.0     : Địa chỉ IP nguồn bắt đầu kiểm tra
- 0.0.0.15       : Wildcard Mask -> cho 16 IP (từ .0 đến .15)
                   Tính: 255.255.255.255 - 255.255.255.240 = 0.0.0.15
- interface e0/3 : Cổng áp dụng ACL (nối hướng WebServer)
- ip access-group 1 out : Lọc gói tin đi RA (outbound) khỏi cổng e0/3

IMPLICIT DENY: Cuối ACL luôn có lệnh ngầm "deny any" chặn tất cả.
IP không thuộc dải .0-.15 sẽ bị cấm gửi dữ liệu ra e0/3.


---------------------------------------------------------------------
BÀI GIẢI CÂU 3.2:
---------------------------------------------------------------------

ĐỀ BÀI: Dùng ACL cấu hình cho host CHỈ ĐƯỢC PHÉP truy cập Web
         trên WebServer (172.16.4.5/24).

Router1(config)# ip access-list extended WEB_ONLY
Router1(config-ext-nacl)# permit tcp any host 172.16.4.5 eq 80
Router1(config-ext-nacl)# permit tcp any host 172.16.4.5 eq 443
Router1(config-ext-nacl)# deny ip any host 172.16.4.5
Router1(config-ext-nacl)# permit ip any any
Router1(config-ext-nacl)# exit
Router1(config)# interface e0/1
Router1(config-if)# ip access-group WEB_ONLY out

GIẢI THÍCH:
1. permit tcp any host 172.16.4.5 eq 80   -> Cho phép HTTP tới Server
2. permit tcp any host 172.16.4.5 eq 443  -> Cho phép HTTPS tới Server
3. deny ip any host 172.16.4.5            -> Cấm mọi thứ khác (ping, ftp...) tới Server
4. permit ip any any                      -> Cho traffic đến đích KHÁC đi qua bình thường
5. Áp vào e0/1 chiều out (cổng nối tới WebServer)

TẠI SAO DÙNG EXTENDED? Vì Standard chỉ lọc IP nguồn, KHÔNG lọc port.
Muốn phân biệt Web (80/443) với FTP (21) thì BẮT BUỘC dùng Extended.


=====================================================================
=====================================================================
       MẪU THAY SỐ NHANH ĐI THI (CHỈ CẦN THAY GIÁ TRỊ TRONG [ ])
=====================================================================
=====================================================================

=== MẪU CÂU 1: BẢO MẬT ROUTER ===

enable
configure terminal
hostname [TÊN_ROUTER]
service password-encryption

line console 0
 password [PASS_CONSOLE]
 login
 exit

enable secret [PASS_ENABLE]

ip domain-name [DOMAIN]
crypto key generate rsa modulus 1024
username [USERNAME] privilege 15 secret [PASS_SSH]

line vty 0 4
 login local
 transport input ssh telnet
 exec-timeout [SỐ_PHÚT] 0
 exit

ip ssh authentication-retries [SỐ_LẦN_SAI]
end
write memory


=== MẪU CÂU 2: SWITCH (Gán VLAN + Trunk) ===

enable
configure terminal
interface [CỔNG_NỐI_ROUTER]
 switchport trunk encapsulation dot1q
 switchport mode trunk
 no shutdown
interface [CỔNG_VPC_A]
 switchport mode access
 switchport access vlan [SỐ_VLAN_A]
interface [CỔNG_VPC_B]
 switchport mode access
 switchport access vlan [SỐ_VLAN_B]
end
write memory


=== MẪU CÂU 2: ROUTER-ON-A-STICK (Router có VLAN) ===

enable
configure terminal
interface [CỔNG_NỐI_SWITCH]
 no shutdown
interface [CỔNG].X
 encapsulation dot1Q [SỐ_VLAN_X]
 ip address [IP_GATEWAY_X] [MASK]
interface [CỔNG].Y
 encapsulation dot1Q [SỐ_VLAN_Y]
 ip address [IP_GATEWAY_Y] [MASK]
interface [SERIAL_NỐI_R1]
 ip address [IP_SERIAL] 255.255.255.252
 no shutdown
router rip
 version 2
 no auto-summary
 network [MẠNG_VLAN_X]
 network [MẠNG_VLAN_Y]
 network [MẠNG_SERIAL]
end
write memory


=== MẪU CÂU 2: R1 TRUNG TÂM (Redistribution + NAT) ===

enable
configure terminal
interface [SERIAL_RIP]
 ip address [IP] 255.255.255.252
 ip nat inside
 no shutdown
interface [SERIAL_OSPF]
 ip address [IP] 255.255.255.252
 ip nat inside
 no shutdown
interface [CỔNG_INTERNET]
 ip address dhcp
 ip nat outside
 no shutdown

access-list 1 permit any
ip nat inside source list 1 interface [CỔNG_INTERNET] overload

router rip
 version 2
 no auto-summary
 network [MẠNG_SERIAL_RIP]
 redistribute ospf 1 metric 2
 default-information originate

router ospf 1
 network [MẠNG_SERIAL_OSPF] [WILDCARD] area 0
 redistribute rip subnets
 default-information originate
end
write memory


=== MẪU CÂU 2: ROUTER OSPF THUẦN ===

enable
configure terminal
interface [SERIAL]
 ip address [IP] 255.255.255.252
 no shutdown
interface [LAN_1]
 ip address [IP] [MASK]
 no shutdown
interface [LAN_2]
 ip address [IP] [MASK]
 no shutdown

router ospf 1
 network [MẠNG_SERIAL] [WILDCARD] area 0
 network [MẠNG_LAN_1] [WILDCARD] area 0
 network [MẠNG_LAN_2] [WILDCARD] area 0
end
write memory


=== MẪU ACL: CẤM DỊCH VỤ CỤ THỂ ===

ip access-list extended [TÊN_ACL]
 deny tcp [IP_NGUỒN] [WILDCARD] host [IP_SERVER] eq [PORT]
 permit ip any any
exit
interface [CỔNG]
 ip access-group [TÊN_ACL] in
end
write memory


=== BẢNG PORT PHỔ BIẾN ===

Dịch vụ     | Port | Keyword
------------|------|--------
HTTP (Web)  | 80   | eq 80 hoặc eq www
HTTPS       | 443  | eq 443
FTP Control | 21   | eq ftp
FTP Data    | 20   | eq ftp-data
Telnet      | 23   | eq telnet hoặc eq 23
SSH         | 22   | eq 22
DNS         | 53   | eq domain
PING        | -    | Dùng "deny icmp" thay vì "deny tcp"


=== WILDCARD MASK NHANH ===

16 IP  (.0-.15)  : 0.0.0.15
32 IP  (.0-.31)  : 0.0.0.31
64 IP  (.0-.63)  : 0.0.0.63
128 IP (.0-.127) : 0.0.0.127
256 IP (.0-.255) : 0.0.0.255
1 host           : host [IP]
Tất cả           : any


=== MẪU GIẢI THÍCH ACL (Viết vào giấy thi) ===

"Đây là [Standard/Extended] ACL số [X].
- Loại: [Standard chỉ lọc IP nguồn | Extended lọc IP nguồn, đích, giao thức, port].
- Hành động: permit cho phép / deny chặn gói tin khớp điều kiện.
- Wildcard Mask [Z]: Cho phép dải IP từ [A] đến [B] (tổng [N] IP).
- Áp dụng: Cổng [e0/X] chiều [in = vào / out = ra].
- Implicit Deny: Cuối ACL luôn có lệnh ngầm deny any chặn mọi gói tin không khớp."
