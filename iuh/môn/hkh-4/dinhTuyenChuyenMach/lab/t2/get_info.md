# SCRIPT LẤY TOÀN BỘ THÔNG TIN TỪ CÁC THIẾT BỊ ĐANG CHẠY

Tuyệt vời! Ping thông nghĩa là mạng đã hoàn toàn liền mạch. 
Nhưng để "ăn ngon ngủ yên" và có bằng chứng (Log/Report) cho báo cáo, tôi đã viết cho bạn một kịch bản siêu đẳng khác: **Tự động đăng nhập vào 8 thiết bị (Router + PC), lấy toàn bộ bảng định tuyến, IP, cấu hình bảo mật và lưu thành 1 file báo cáo duy nhất.**

## CÁCH THỰC HIỆN
1. Tại cửa sổ lệnh EVE-NG, tạo file mới:
   ```bash
   nano get_info.py
   ```
2. Copy đoạn code dưới đây dán vào:

```python
#!/usr/bin/env python3
import telnetlib
import time

nodes = {
    32769: {"name": "Router West", "type": "router"},
    32770: {"name": "Router Central", "type": "router"},
    32771: {"name": "Router East", "type": "router"},
    32772: {"name": "Router Internet", "type": "router"},
    32777: {"name": "PC 1", "type": "pc"},
    32778: {"name": "PC 2", "type": "pc"},
    32779: {"name": "PC 3", "type": "pc"},
    32780: {"name": "PC 4", "type": "pc"}
}

def get_configs():
    print("BAT DAU THU THAP THONG TIN TU CAC THIET BI (Telnet)...")
    with open("report_bai5.txt", "w") as f:
        f.write("========== BAO CAO CAU HINH LAB 5 ==========\n\n")
        
    for port, data in nodes.items():
        try:
            print("-> Dang lay thong tin tu {} (Port {})...".format(data["name"], port))
            tn = telnetlib.Telnet("127.0.0.1", port, timeout=5)
            
            output = ""
            if data["type"] == "router":
                tn.write(b"\r\n\r\n")
                time.sleep(0.5)
                tn.write(b"enable\r\n")
                time.sleep(0.5)
                
                # Xu ly nhap mat khau neu Router hoi (Router East)
                out = tn.read_very_eager().decode('ascii', errors='ignore')
                if "Password:" in out:
                    tn.write(b"1012enable\r\n")
                    time.sleep(0.5)
                
                # Lenh nay giup 'show run' khong bi ngat trang (More)
                tn.write(b"terminal length 0\r\n") 
                time.sleep(0.5)
                
                # Bat dau lay thong tin
                tn.write(b"show ip interface brief\r\n")
                time.sleep(1)
                tn.write(b"show ip route\r\n")
                time.sleep(1)
                tn.write(b"show running-config\r\n")
                time.sleep(3) # Doi 3 giay de router in het cau hinh
                
                output = out + tn.read_very_eager().decode('ascii', errors='ignore')
            else:
                tn.write(b"\r\n\r\n")
                time.sleep(0.5)
                tn.write(b"show ip\r\n")
                time.sleep(1)
                output = tn.read_very_eager().decode('ascii', errors='ignore')
                
            tn.close()
            
            with open("report_bai5.txt", "a") as f:
                f.write("========== {} ==========\n".format(data["name"]))
                f.write(output)
                f.write("\n\n")
                
            print("   [+] Da luu thong tin {}".format(data["name"]))
        except Exception as e:
            print("   [-] Loi ket noi den {}: {}".format(data["name"], e))
            
    print("\n=> HOAN TAT! Toan bo thong tin da duoc luu vao file 'report_bai5.txt'.")
    print("Ban co the xem file nay bang lenh: cat report_bai5.txt")

if __name__ == "__main__":
    get_configs()
```

3. Nhấn `Ctrl + O` -> `Enter` -> `Ctrl + X` để lưu.
4. Gõ lệnh chạy:
   ```bash
   python3 get_info.py
   ```

Khi chạy xong, Script sẽ tổng hợp bảng IP, bảng định tuyến và toàn bộ dòng lệnh đã lưu của tất cả các Router, các IP của các PC vào chung một file tên là **`report_bai5.txt`**. 
Bạn chỉ việc gõ lệnh `cat report_bai5.txt` để xem, hoặc copy nó ra ngoài máy tính Windows là yên tâm kê cao gối ngủ nhé! Lần tới đi thi gặp bài tương tự là bạn nắm chắc trong tay bộ tool ăn điểm 10 rồi!
