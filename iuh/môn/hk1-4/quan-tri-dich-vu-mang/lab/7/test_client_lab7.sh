#!/bin/bash
# ==============================================================================
# SCRIPT KIỂM THỬ TẤT CẢ DỊCH VỤ LAB 7 TỪ PHÍA CLIENT
# Thực hiện trên: Ubuntu_2 (LinuxB - 192.168.6.2 / 192.168.5.3)
# Target Server:  Ubuntu_1 (LinuxA - 192.168.6.3 / 192.168.5.2)
# ==============================================================================

SERVER_IP="192.168.6.3"

echo "=============================================================================="
echo "BẮT ĐẦU KIỂM THỬ HỆ THỐNG LAB 7 (XINETD, TELNET, OPENSSH, VSFTPD)"
echo "Target Server IP: $SERVER_IP"
echo "=============================================================================="

echo ""
echo "--- [1. KIỂM THỬ TELNET QUA CỔNG 23] ---"
python3 - << EOF
import telnetlib, time
try:
    tn = telnetlib.Telnet("$SERVER_IP", 23, timeout=4)
    time.sleep(1)
    idx, obj, text = tn.expect([b"login: ", b"Login: "], timeout=3)
    tn.write(b"neko\n")
    idx, obj, text = tn.expect([b"Password: ", b"password: "], timeout=3)
    tn.write(b"conmeo\n")
    time.sleep(1)
    tn.write(b"echo '--> TELNET AUTHENTICATION SUCCESSFUL!' && whoami\n")
    time.sleep(1)
    out = tn.read_very_eager().decode("latin1", errors="ignore")
    print(out)
    tn.write(b"exit\n")
    tn.close()
except Exception as e:
    print("[-] Telnet Error:", e)
EOF

echo ""
echo "--- [2. KIỂM THỬ OPENSSH BẢO MẬT & PHÂN QUYỀN TRUY CẬP] ---"
echo ">> Kiểm tra User testuser1 (Được phép đăng nhập):"
python3 - << EOF
import subprocess
res = subprocess.run(["ssh", "-o", "StrictHostKeyChecking=no", "-o", "ConnectTimeout=3", "testuser1@$SERVER_IP", "echo 'SUCCESS: testuser1 logged in via SSH!'"], capture_output=True, text=True)
print(res.stdout or res.stderr)
EOF

echo ""
echo "--- [3. KIỂM THỬ VSFTPD SERVER QUA CỔNG 21] ---"
python3 - << EOF
import ftplib, io
print(">> Thử nghiệm đăng nhập Anonymous (Cấm theo yêu cầu):")
try:
    ftp = ftplib.FTP("$SERVER_IP", timeout=4)
    ftp.login("anonymous", "")
    print("[-] Thất bại: Anonymous vẫn đăng nhập được!")
    ftp.quit()
except Exception as e:
    print("[+] THÀNH CÔNG: Anonymous bị chặn chính xác ->", e)

print("\n>> Thử nghiệm đăng nhập tài khoản hệ thống 'testuser1':")
try:
    ftp = ftplib.FTP("$SERVER_IP", timeout=4)
    ftp.login("testuser1", "123")
    print("[+] THÀNH CÔNG: testuser1 đăng nhập FTP thành công!")
    
    # Upload test
    data = io.BytesIO(b"Hello from Ubuntu 2 Client Lab 7 verification script!")
    ftp.storbinary("STOR client_test.txt", data)
    print("[+] THÀNH CÔNG: Upload file client_test.txt lên FTP Server!")
    
    # List files
    lines = []
    ftp.retrlines("LIST", lines.append)
    print("[+] Danh sách file trong thư mục cá nhân:")
    for line in lines:
        print("   ", line)
    ftp.quit()
except Exception as e:
    print("[-] FTP Error:", e)
EOF

echo ""
echo "=============================================================================="
echo "HOÀN TẤT KIỂM THỬ TẤT CẢ DỊCH VỤ LAB 7!"
echo "=============================================================================="
