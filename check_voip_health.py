import sys
import paramiko

sys.stdout.reconfigure(encoding='utf-8')

def check():
    print("=" * 65)
    print("   KIỂM TRA HỆ THỐNG TỔNG ĐÀI VOIP ASTERISK TRƯỚC KHI DEMO")
    print("=" * 65)
    
    # 1. SSH to Ubuntu
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('192.168.1.100', username='neko', password='conmeo', timeout=4)
    except Exception as e:
        print("\n[!] LỖI: Không kết nối được Ubuntu Server (192.168.1.100)!")
        print("    -> Hãy đảm bảo máy ảo Ubuntu đã khởi động xong trong VMware.")
        return

    # 2. Get Hotspot IP
    stdin, stdout, stderr = ssh.exec_command("ip -4 addr show ens37 | grep -oP '(?<=inet\\s)\\d+(\\.\\d+){3}'")
    hotspot_ip = stdout.read().decode().strip()
    
    print(f"\n[+] Ubuntu Server (LAN nội bộ Win 7): 192.168.1.100  [OK]")
    if hotspot_ip:
        print(f"[+] Ubuntu Server (Wi-Fi Hotspot 4G):  {hotspot_ip}   [OK]")
        print(f"    👉 Lưu ý: Trên Sipnetic của Điện thoại 103 & 104, hãy chắc chắn")
        print(f"       đang nhập Domain / Server là: {hotspot_ip}")
    else:
        print("[!] CẢNH BÁO: Chưa nhận được IP trên card Wi-Fi ens37!")
        print("    -> Hãy kiểm tra xem Laptop đã kết nối vào Hotspot của ĐT 103 chưa.")

    # 3. Check Asterisk PJSIP Contacts
    stdin, stdout, stderr = ssh.exec_command("sudo -S asterisk -rx 'pjsip show contacts'")
    stdin.write('conmeo\n')
    stdin.flush()
    contacts_out = stdout.read().decode()

    devices = {
        '101': ('Win 7 Máy 1 (Giám Đốc)', '101'),
        '102': ('Win 7 Máy 2 (Kinh Doanh)', '102'),
        '103': ('Điện thoại 1 (0987214065)', '103'),
        '104': ('Điện thoại 2 (0981647882)', '104')
    }

    print("\n" + "-" * 65)
    print(" DANH SÁCH THIẾT BỊ ĐÃ ĐĂNG KÝ VÀ TRẠNG THÁI SẴN SÀNG:")
    print("-" * 65)
    
    all_ok = True
    for ext, (name, num) in devices.items():
        found = False
        for line in contacts_out.splitlines():
            if line.strip().startswith(f"Contact:  {ext}/") or f"{ext}/sip:{ext}@" in line:
                status = "Avail" if "Avail" in line else ("NonQual" if "NonQual" in line else "ONLINE")
                # extract rtt
                parts = line.split()
                rtt = parts[-1] + " ms" if parts and parts[-1] != "nan" else "OK"
                print(f"  [{ext}] {name:<32} : ONLINE ({status} - {rtt})")
                found = True
                break
        if not found:
            print(f"  [{ext}] {name:<32} : CHƯA KẾT NỐI (OFFLINE)")
            all_ok = False

    print("-" * 65)
    if all_ok:
        print("  🎉 TẤT CẢ 4 THIẾT BỊ ĐÃ SẴN SÀNG ĐỂ DEMO 10 ĐIỂM!")
        print("  Bạn có thể mở kịch bản và tiến hành gọi thử từ Test 1 -> Test 7.")
    else:
        print("  ⚠️ Còn thiết bị chưa kết nối. Hãy mở app Sipnetic/MicroSIP")
        print("  để thiết bị tự động đăng ký lại vào tổng đài.")
    print("=" * 65)
    ssh.close()

if __name__ == '__main__':
    check()
