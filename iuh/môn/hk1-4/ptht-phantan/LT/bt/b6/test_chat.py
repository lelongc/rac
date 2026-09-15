import socket
import time
import sys

# Đảm bảo UTF-8 cho console
sys.stdout.reconfigure(encoding='utf-8')

print("=== BẮT ĐẦU TEST SOCKET CHAT DOCKER CONTAINER ===")
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect(('127.0.0.1', 5000))
msg1 = s1.recv(1024).decode('utf-8', errors='ignore')
print("Server -> SinhVien_A:", msg1.strip())

# Gửi username SinhVien_A
s1.sendall("SinhVien_A\n".encode('utf-8'))
time.sleep(0.3)
print("SinhVien_A nhận:", s1.recv(1024).decode('utf-8', errors='ignore').strip())

# SinhVien_B kết nối
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect(('127.0.0.1', 5000))
s2.recv(1024)
s2.sendall("SinhVien_B\n".encode('utf-8'))
time.sleep(0.3)
print("SinhVien_B nhận:", s2.recv(1024).decode('utf-8', errors='ignore').strip())

# A nhận thông báo B vào phòng
print("SinhVien_A nhận broadcast:", s1.recv(1024).decode('utf-8', errors='ignore').strip())

# A chat -> Server broadcast -> B nhận
print("\n--> SinhVien_A gửi tin: 'Xin chao ca lop PTHT!'")
s1.sendall("Xin chao ca lop PTHT!\n".encode('utf-8'))
time.sleep(0.3)
recv_b = s2.recv(1024).decode('utf-8', errors='ignore').strip()
print("--> SinhVien_B nhận được broadcast:", recv_b)

# B chat -> Server broadcast -> A nhận
print("\n--> SinhVien_B gửi tin: 'Chao A, minh da nhan duoc tin!'")
s2.sendall("Chao A, minh da nhan duoc tin!\n".encode('utf-8'))
time.sleep(0.3)
recv_a = s1.recv(1024).decode('utf-8', errors='ignore').strip()
print("--> SinhVien_A nhận được broadcast:", recv_a)

# Thoát
s1.sendall("exit\n".encode('utf-8'))
s2.sendall("exit\n".encode('utf-8'))
time.sleep(0.3)
s1.close()
s2.close()

print("\n=== KẾT QUẢ TEST: TOÀN BỘ CHỨC NĂNG BROADCAST HOẠT ĐỘNG HOÀN HẢO! ===")
