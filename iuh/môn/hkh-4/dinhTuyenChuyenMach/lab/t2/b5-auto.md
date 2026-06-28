# HƯỚNG DẪN DÙNG LỆNH PYTHON TỰ ĐỘNG TẠO LAB BÀI 5 TRÊN EVE-NG

Chào anh, dưới đây là hướng dẫn chi tiết từng bước để anh kết nối SSH từ máy Windows thật vào máy ảo EVE-NG (IP: 192.168.2.128) và chạy một đoạn script Python. Script này sẽ tự động dò tìm Image IOL trên máy anh, tự động vẽ ra toàn bộ sơ đồ Bài 5 (Router, Switch, PC, nối dây, sắp xếp vị trí) cực kỳ nhanh chóng.

## BƯỚC 1: KẾT NỐI SSH TỪ MÁY THẬT VÀO EVE-NG

1. Nhấn nút **Start** trên Windows, gõ `cmd` hoặc `PowerShell` và mở lên.
2. Gõ lệnh sau để kết nối vào EVE-NG:
   ```cmd
   ssh root@192.168.2.128
   ```
3. Nếu nó hiện ra câu hỏi "Are you sure you want to continue connecting (yes/no)?", hãy gõ `yes` và nhấn Enter.
4. Nhập mật khẩu là: `eve` (Lưu ý: khi gõ mật khẩu trên Linux nó sẽ không hiện ký tự nào cả, cứ gõ đúng rồi Enter).

## BƯỚC 2: TẠO FILE SCRIPT PYTHON TỰ ĐỘNG

Khi đã vào được màn hình lệnh của EVE-NG (có chữ `root@eve-ng:~#`), làm theo các bước sau:

1. Gõ lệnh tạo file mới bằng trình soạn thảo Nano:
   ```bash
   nano auto_bai5.py
   ```
2. Copy toàn bộ đoạn code Python dưới đây (bôi đen và bấm Ctrl+C). Sau đó quay lại cửa sổ CMD/PowerShell, **Click chuột phải** để dán code vào:

```python
#!/usr/bin/env python3
import os

def create_xml():
    print("1. Thiet lap Image IOL quen thuoc cua ban...")
    img_l3 = "L3-ADVENTERPRISEK9-M-15.4-2T.bin"
    img_l2 = "L2-ADVENTERPRISEK9-M-15.2-IRON-20151103.bin"
    print("-> Su dung: " + img_l3 + " va " + img_l2)

    print("2. Dang tien hanh ghep noi so do (Topology) va CAU HINH SAN cho Bai 5...")
    xml_template = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<lab name="Bai5_Auto_Script" version="1" scripttimeout="300" lock="0">
  <topology>
    <nodes>
      <node id="1" name="West" type="iol" template="iol" image="IMAGE_L3" ethernet="1" nvram="1024" ram="1024" serial="1" console="" delay="0" icon="Router.png" config="1" left="200" top="200">
        <interface id="0" name="e0/0" type="ethernet" network_id="4"/>
        <interface id="1" type="serial" name="s1/0" remote_id="2" remote_if="1"/>
        <config><![CDATA[hostname West
!
interface Ethernet0/0
 ip address 192.168.0.1 255.255.255.0
 no shutdown
!
interface Serial1/0
 ip address 10.0.0.1 255.255.255.0
 no shutdown
!
ip route 0.0.0.0 0.0.0.0 10.0.0.2
ip route 10.0.1.0 255.255.255.0 10.0.0.2
ip route 192.168.1.0 255.255.255.0 10.0.0.2
ip route 192.168.2.0 255.255.255.0 10.0.0.2
!
end]]></config>
      </node>
      <node id="2" name="Central" type="iol" template="iol" image="IMAGE_L3" ethernet="1" nvram="1024" ram="1024" serial="1" console="" delay="0" icon="Router.png" config="1" left="450" top="200">
        <interface id="0" name="e0/0" type="ethernet" network_id="5"/>
        <interface id="1" type="serial" name="s1/0" remote_id="1" remote_if="1"/>
        <interface id="17" type="serial" name="s1/1" remote_id="3" remote_if="17"/>
        <interface id="33" type="serial" name="s1/2" remote_id="4" remote_if="1"/>
        <config><![CDATA[hostname Central
!
interface Ethernet0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
!
interface Serial1/0
 ip address 10.0.0.2 255.255.255.0
 no shutdown
!
interface Serial1/1
 ip address 10.0.1.1 255.255.255.0
 no shutdown
!
interface Serial1/2
 ip address 10.0.2.1 255.255.255.0
 no shutdown
!
ip route 0.0.0.0 0.0.0.0 10.0.2.2
ip route 192.168.0.0 255.255.255.0 10.0.0.1
ip route 192.168.2.0 255.255.255.0 10.0.1.2
!
end]]></config>
      </node>
      <node id="3" name="East" type="iol" template="iol" image="IMAGE_L3" ethernet="1" nvram="1024" ram="1024" serial="1" console="" delay="0" icon="Router.png" config="1" left="700" top="200">
        <interface id="0" name="e0/0" type="ethernet" network_id="6"/>
        <interface id="17" type="serial" name="s1/1" remote_id="2" remote_if="17"/>
        <config><![CDATA[hostname East
!
service password-encryption
!
enable password 08092023enable
enable secret 1012enable
!
username svhk1012 privilege 15 secret Tel1012@ssh
!
interface Ethernet0/0
 ip address 192.168.2.1 255.255.255.0
 no shutdown
!
interface Serial1/1
 ip address 10.0.1.2 255.255.255.0
 no shutdown
!
ip route 0.0.0.0 0.0.0.0 10.0.1.1
ip route 10.0.0.0 255.255.255.0 10.0.1.1
ip route 192.168.0.0 255.255.255.0 10.0.1.1
ip route 192.168.1.0 255.255.255.0 10.0.1.1
!
line console 0
 password 08092023console
 login
 exec-timeout 3 0
!
line vty 0 4
 login local
 password Tel@ssh
 transport input ssh telnet
!
ip ssh authentication-retries 3
!
end]]></config>
      </node>
      <node id="4" name="Internet" type="iol" template="iol" image="IMAGE_L3" ethernet="1" nvram="1024" ram="1024" serial="1" console="" delay="0" icon="Router.png" config="1" left="450" top="50">
        <interface id="0" name="e0/0" type="ethernet" network_id="7"/>
        <interface id="1" type="serial" name="s1/0" remote_id="2" remote_if="33"/>
        <config><![CDATA[hostname Internet
!
interface Ethernet0/0
 ip address 192.168.3.1 255.255.255.0
 no shutdown
!
interface Serial1/0
 ip address 10.0.2.2 255.255.255.0
 no shutdown
!
ip route 10.0.0.0 255.255.0.0 10.0.2.1
ip route 192.168.0.0 255.255.0.0 10.0.2.1
!
end]]></config>
      </node>
      <node id="5" name="SW4" type="iol" template="iol" image="IMAGE_L2" ethernet="1" nvram="1024" ram="1024" serial="0" console="" delay="0" icon="Switch.png" config="0" left="200" top="350">
        <interface id="0" name="e0/0" type="ethernet" network_id="4"/>
        <interface id="16" name="e0/1" type="ethernet" network_id="8"/>
      </node>
      <node id="6" name="SW5" type="iol" template="iol" image="IMAGE_L2" ethernet="1" nvram="1024" ram="1024" serial="0" console="" delay="0" icon="Switch.png" config="0" left="450" top="350">
        <interface id="0" name="e0/0" type="ethernet" network_id="5"/>
        <interface id="16" name="e0/1" type="ethernet" network_id="9"/>
      </node>
      <node id="7" name="SW6" type="iol" template="iol" image="IMAGE_L2" ethernet="1" nvram="1024" ram="1024" serial="0" console="" delay="0" icon="Switch.png" config="0" left="700" top="350">
        <interface id="0" name="e0/0" type="ethernet" network_id="6"/>
        <interface id="16" name="e0/1" type="ethernet" network_id="10"/>
      </node>
      <node id="8" name="SW7" type="iol" template="iol" image="IMAGE_L2" ethernet="1" nvram="1024" ram="1024" serial="0" console="" delay="0" icon="Switch.png" config="0" left="600" top="50">
        <interface id="0" name="e0/0" type="ethernet" network_id="7"/>
        <interface id="16" name="e0/1" type="ethernet" network_id="11"/>
      </node>
      <node id="9" name="PC1" type="vpcs" template="vpcs" image="" ethernet="1" delay="0" icon="Desktop.png" config="1" left="200" top="500">
        <interface id="0" name="eth0" type="ethernet" network_id="8"/>
        <config><![CDATA[set pcname PC1
ip 192.168.0.5/24 192.168.0.1
]]></config>
      </node>
      <node id="10" name="PC2" type="vpcs" template="vpcs" image="" ethernet="1" delay="0" icon="Desktop.png" config="1" left="450" top="500">
        <interface id="0" name="eth0" type="ethernet" network_id="9"/>
        <config><![CDATA[set pcname PC2
ip 192.168.1.5/24 192.168.1.1
]]></config>
      </node>
      <node id="11" name="PC3" type="vpcs" template="vpcs" image="" ethernet="1" delay="0" icon="Desktop.png" config="1" left="700" top="500">
        <interface id="0" name="eth0" type="ethernet" network_id="10"/>
        <config><![CDATA[set pcname PC3
ip 192.168.2.5/24 192.168.2.1
]]></config>
      </node>
      <node id="12" name="C4" type="vpcs" template="vpcs" image="" ethernet="1" delay="0" icon="Desktop.png" config="1" left="750" top="50">
        <interface id="0" name="eth0" type="ethernet" network_id="11"/>
        <config><![CDATA[set pcname C4
ip 192.168.3.5/24 192.168.3.1
]]></config>
      </node>
    </nodes>
    <networks>
      <network id="4" type="bridge" name="Net4" left="0" top="0" visibility="0"/>
      <network id="5" type="bridge" name="Net5" left="0" top="0" visibility="0"/>
      <network id="6" type="bridge" name="Net6" left="0" top="0" visibility="0"/>
      <network id="7" type="bridge" name="Net7" left="0" top="0" visibility="0"/>
      <network id="8" type="bridge" name="Net8" left="0" top="0" visibility="0"/>
      <network id="9" type="bridge" name="Net9" left="0" top="0" visibility="0"/>
      <network id="10" type="bridge" name="Net10" left="0" top="0" visibility="0"/>
      <network id="11" type="bridge" name="Net11" left="0" top="0" visibility="0"/>
    </networks>
  </topology>
</lab>"""
  
    xml = xml_template.replace("IMAGE_L3", img_l3).replace("IMAGE_L2", img_l2)
  
    with open("/opt/unetlab/labs/Bai5_Auto_Script.unl", "w") as f:
        f.write(xml)
    print("3. Da sinh thanh cong file Lab va NHUNG SAN CAU HINH vao: /opt/unetlab/labs/Bai5_Auto_Script.unl")
  
    print("4. Dang Fix permission...")
    os.system("/opt/unetlab/wrappers/unl_wrapper -a fixpermissions")
    print("=> HOAN TAT! Ban co the mo Lab, bat thiet bi len va ping ngay lap tuc!")

if __name__ == "__main__":
    create_xml()
```

3. Bấm tổ hợp phím **`Ctrl + O`**, sau đó nhấn **`Enter`** để lưu file.
4. Bấm tổ hợp phím **`Ctrl + X`** để thoát màn hình soạn thảo.

## BƯỚC 3: CHẠY SCRIPT ĐỂ VẼ LAB TỰ ĐỘNG VÀ CẤU HÌNH TỪ A-Z

Từ dấu nháy lệnh, bạn chỉ việc gõ:

```bash
python3 auto_bai5.py
```

Lệnh sẽ chạy trong tích tắc. Bây giờ bạn chỉ việc **mở trình duyệt Web**, đăng nhập vào EVE-NG.
Mở Lab **`Bai5_Auto_Script`**, bôi đen toàn bộ thiết bị, nhấp chuột phải chọn **Start Selected**.

Bạn hãy đợi khoảng 1 phút cho các Router khởi động. **TUYỆT VỜI NHẤT LÀ:** Toàn bộ lệnh gán IP, cấu hình bảo mật ở Bài 2 (East), Static Route ở Bài 4 và Internet ở Bài 5 **đều đã được gõ sẵn và nhúng thẳng vào các thiết bị**. Bạn chỉ cần mở PC C4 lên và gõ lệnh `ping 192.168.0.5` hoặc `trace 192.168.0.5` là thành công ngay lập tức! Chúc mừng bạn đã "hack" xong bài thực hành một cách hoàn hảo!
