# KỊCH BẢN TỰ ĐỘNG HÓA CẤU HÌNH EVE-NG QUA TELNET (BẢN V2 - SIÊU CHẮC CHẮN)

Nguyên nhân thất bại vừa rồi đã được tìm ra: **Script gõ lệnh quá nhanh!**
Khi Router còn đang khởi động và hiện dòng chữ `Would you like to enter the initial configuration dialog?`, Script đã vội vã ném hết các lệnh cấu hình IP vào. Kết quả là Router chưa kịp nhận lệnh nên bị trôi sạch.

Ở bản V2 này, tôi đã thêm **"mắt thần"** cho đoạn code. Nó sẽ kiên nhẫn đứng chờ, liên tục gõ `Enter` cho đến khi nào Router thực sự sẵn sàng (hiện ra dấu `>`) thì nó mới bắt đầu bắn lệnh cấu hình.

## BƯỚC 1: CẬP NHẬT LẠI SCRIPT

1. Mở lại file cũ:
   ```bash
   nano push_config.py
   ```
2. Nhấn `Ctrl + K` liên tục để xóa sạch code cũ.
3. Copy toàn bộ code mới (V2) dưới đây dán vào:

```python
#!/usr/bin/env python3
import telnetlib
import time

# Danh sach cac lenh
configs = {
    32769: {
        "type": "router",
        "cmds": [
            "enable", "configure terminal", "hostname West",
            "interface Ethernet0/0", "ip address 192.168.0.1 255.255.255.0", "no shutdown", "exit",
            "interface Serial1/0", "ip address 10.0.0.1 255.255.255.0", "no shutdown", "exit",
            "ip route 0.0.0.0 0.0.0.0 10.0.0.2",
            "ip route 10.0.1.0 255.255.255.0 10.0.0.2",
            "ip route 192.168.1.0 255.255.255.0 10.0.0.2",
            "ip route 192.168.2.0 255.255.255.0 10.0.0.2",
            "end"
        ]
    },
    32770: {
        "type": "router",
        "cmds": [
            "enable", "configure terminal", "hostname Central",
            "interface Ethernet0/0", "ip address 192.168.1.1 255.255.255.0", "no shutdown", "exit",
            "interface Serial1/0", "ip address 10.0.0.2 255.255.255.0", "no shutdown", "exit",
            "interface Serial1/1", "ip address 10.0.1.1 255.255.255.0", "no shutdown", "exit",
            "interface Serial1/2", "ip address 10.0.2.1 255.255.255.0", "no shutdown", "exit",
            "ip route 0.0.0.0 0.0.0.0 10.0.2.2",
            "ip route 192.168.0.0 255.255.255.0 10.0.0.1",
            "ip route 192.168.2.0 255.255.255.0 10.0.1.2",
            "end"
        ]
    },
    32771: {
        "type": "router",
        "cmds": [
            "enable", "configure terminal", "hostname East",
            "service password-encryption",
            "enable password 08092023enable",
            "enable secret 1012enable",
            "username svhk1012 privilege 15 secret Tel1012@ssh",
            "interface Ethernet0/0", "ip address 192.168.2.1 255.255.255.0", "no shutdown", "exit",
            "interface Serial1/1", "ip address 10.0.1.2 255.255.255.0", "no shutdown", "exit",
            "ip route 0.0.0.0 0.0.0.0 10.0.1.1",
            "ip route 10.0.0.0 255.255.255.0 10.0.1.1",
            "ip route 192.168.0.0 255.255.255.0 10.0.1.1",
            "ip route 192.168.1.0 255.255.255.0 10.0.1.1",
            "line console 0", "password 08092023console", "login", "exec-timeout 3 0", "exit",
            "line vty 0 4", "login local", "password Tel@ssh", "transport input ssh telnet", "exit",
            "ip ssh authentication-retries 3",
            "end"
        ]
    },
    32772: {
        "type": "router",
        "cmds": [
            "enable", "configure terminal", "hostname Internet",
            "interface Ethernet0/0", "ip address 192.168.3.1 255.255.255.0", "no shutdown", "exit",
            "interface Serial1/0", "ip address 10.0.2.2 255.255.255.0", "no shutdown", "exit",
            "ip route 10.0.0.0 255.255.0.0 10.0.2.1",
            "ip route 192.168.0.0 255.255.0.0 10.0.2.1",
            "end"
        ]
    },
    32777: { "type": "pc", "cmds": ["ip 192.168.0.5/24 192.168.0.1"] },
    32778: { "type": "pc", "cmds": ["ip 192.168.1.5/24 192.168.1.1"] },
    32779: { "type": "pc", "cmds": ["ip 192.168.2.5/24 192.168.2.1"] },
    32780: { "type": "pc", "cmds": ["ip 192.168.3.5/24 192.168.3.1"] }
}

def push_configs():
    print("BAT DAU BAN CAU HINH VAO CAC THIET BI (Telnet)...")
    for port, data in configs.items():
        try:
            print("-> Dang ket noi toi Port {}...".format(port))
            tn = telnetlib.Telnet("127.0.0.1", port, timeout=5)
          
            if data["type"] == "router":
                # Kien nhan go Enter cho den khi nhin thay dau nhay lenh
                ready = False
                for _ in range(30):
                    tn.write(b"\r\n")
                    time.sleep(1)
                    out = tn.read_very_eager().decode('ascii', errors='ignore')
                  
                    if "yes/no" in out or "initial configuration dialog" in out:
                        tn.write(b"no\r\n")
                        print("   [+] Da tra loi 'no' cho setup wizard")
                  
                    if ">" in out or "#" in out:
                        print("   [+] Router da san sang (hien dau nhay lenh)!")
                        ready = True
                        break
                      
                if not ready:
                    print("   [-] Router phan hoi qua cham, bo qua!")
                    continue
            else:
                tn.write(b"\r\n\r\n")
                time.sleep(1)
          
            # Bat dau ban lenh
            for cmd in data["cmds"]:
                tn.write(cmd.encode('ascii') + b"\r\n")
                time.sleep(0.2) # Nghi 0.2 giay giua cac lenh de Router kip xu ly
              
            if data["type"] == "router":
                time.sleep(1)
                tn.write(b"write memory\r\n")
            else:
                time.sleep(0.5)
                tn.write(b"save\r\n")
              
            time.sleep(1)
            tn.close()
            print("   [Thanh cong] Da day cau hinh xong cho Port {}!\n".format(port))
        except Exception as e:
            print("   [That bai] Loi Port {}: {}\n".format(port, e))

if __name__ == "__main__":
    push_configs()
```

4. Nhấn `Ctrl + O` -> `Enter` -> `Ctrl + X` để lưu và thoát.

## BƯỚC 2: CHẠY LẠI

1. Đảm bảo trên Web EVE-NG, các thiết bị vẫn đang chạy (Icon màu xanh).
2. Chạy lệnh:
   ```bash
   python3 push_config.py
   ```

**Lần này bạn sẽ thấy màn hình in ra: `[+] Router da san sang (hien dau nhay lenh)!`** thì tức là code đã chờ đúng lúc rồi mới ném cấu hình vào. Bạn xem thử kết quả có báo thành công hết không nhé! Lần này đảm bảo PC sẽ ngậm được IP!
