# 📖 HƯỚNG DẪN TỰ TRIỂN KHAI TỔNG ĐÀI VOIP ASTERISK TỪ A ĐẾN Z

### (DÀNH CHO BẠN BÈ / THÀNH VIÊN NHÓM TỰ CẤU HÌNH BÀI LAB CỦA RIÊNG MÌNH)

Tài liệu này được thiết kế để **bất kỳ ai cũng có thể tự cài đặt hoàn chỉnh hệ thống Tổng đài VoIP Asterisk** trên máy ảo Ubuntu Server 22.04 chỉ bằng **1 lần chạy script**.
Bạn chỉ cần thay đổi thông tin cá nhân của bạn ở phần đầu, toàn bộ hệ thống sẽ tự động cấu hình và kích hoạt 100%!

---

## 🎯 PHẦN 1: BẢNG KHAI BÁO THÔNG TIN CÁ NHÂN (CHỈ CẦN SỬA MỤC NÀY)

Trước khi chạy, bạn chỉ cần chuẩn bị 4 thông tin sau của bạn:

| Tên biến cấu hình           | Ý nghĩa                                                | Ví dụ mẫu             | Bạn điền thông tin của bạn vào đây |
| :------------------------------ | :------------------------------------------------------- | :----------------------- | :------------------------------------------ |
| **`MY_GMAIL`**          | Địa chỉ Gmail nhận file ghi âm Voicemail            | `nguyenvana@gmail.com` | `...................................`     |
| **`MY_GMAIL_APP_PASS`** | Mật khẩu ứng dụng Google (16 ký tự)                | `abcd efgh ijkl mnop`  | `...................................`     |
| **`PHONE_1_REAL`**      | Số điện thoại di động thật của bạn (Máy 103)   | `0987214065`           | `...................................`     |
| **`PHONE_2_REAL`**      | Số điện thoại di động thật của bạn 2 (Máy 104) | `0981647882`           | `...................................`     |
| **`SIP_PASSWORD`**      | Mật khẩu chung đăng nhập các máy nhánh           | `123456`               | `123456`                                  |

> 🔑 **CÁCH LẤY MẬT KHẨU ỨNG DỤNG GMAIL (APP PASSWORD 16 KÝ TỰ):**
>
> 1. Mở trình duyệt vào tài khoản Google: [https://myaccount.google.com/security](https://myaccount.google.com/security)
> 2. Đảm bảo đã bật **Xác minh 2 bước (2-Step Verification)**.
> 3. Tìm ô tìm kiếm gõ từ khóa: **`Mật khẩu ứng dụng`** (hoặc `App passwords`).
> 4. Đặt tên ứng dụng là `Asterisk VoIP` ➔ Bấm **Tạo**.
> 5. Google sẽ cấp cho bạn một chuỗi **16 chữ cái** (VD: `nwzl sjvs owce dizo`). Hãy copy chuỗi này (xóa các dấu cách đi).

---

## 🚀 PHẦN 2: SCRIPT TỰ ĐỘNG HÓA 1-CLICK (`setup_voip_all_in_one.sh`)

Hãy tạo một file tên là **`setup_voip_all_in_one.sh`** trên máy ảo Ubuntu 22.04 của bạn bằng lệnh:

```bash
nano setup_voip_all_in_one.sh
```

Dán toàn bộ đoạn mã bên dưới vào. **Chú ý: Hãy sửa 4 dòng thông tin cá nhân ở ngay đầu file!**

```bash
#!/bin/bash
# ==============================================================================
# HỆ THỐNG TỰ ĐỘNG CÀI ĐẶT & CẤU HÌNH TỔNG ĐÀI VOIP ASTERISK CHUẨN ĐIỂM 10 (IUH)
# ==============================================================================

# ------------------------------------------------------------------------------
# [BƯỚC 1]: THAY ĐỔI CÁC THÔNG TIN CỦA BẠN TẠI ĐÂY
# ------------------------------------------------------------------------------
MY_GMAIL="lelong191001@gmail.com"           # Thay bằng Gmail của bạn
MY_GMAIL_APP_PASS="nwzlsjvsowcedizo"        # Thay bằng Mật khẩu ứng dụng 16 ký tự của bạn
PHONE_1_REAL="0987214065"                   # Số di động thật của máy 1 (Ext 103)
PHONE_2_REAL="0981647882"                   # Số di động thật của máy 2 (Ext 104)
SIP_PASSWORD="123456"                       # Mật khẩu đăng nhập các máy nhánh

# ------------------------------------------------------------------------------
# BẮT ĐẦU QUÁ TRÌNH TỰ ĐỘNG CẤU HÌNH (KHÔNG CẦN CHỈNH SỬA PHÍA DƯỚI)
# ------------------------------------------------------------------------------
if [ "$EUID" -ne 0 ]; then
  echo -e "\e[31m[LỖI] Vui lòng chạy script với quyền root: sudo ./setup_voip_all_in_one.sh\e[0m"
  exit 1
fi

echo -e "\e[36m=== [1/7] KIỂM TRA MẠNG & LẤY ĐỊA CHỈ IP TỰ ĐỘNG ===\e[0m"
# Nhận diện card NAT ens33 và card Bridged/Wi-Fi ens37
LAN_IP=$(ip -4 addr show ens33 2>/dev/null | grep -oP '(?<=inet\s)\d+(\.\d+){3}' | head -n 1)
[ -z "$LAN_IP" ] && LAN_IP="192.168.1.100"

WIFI_IP=$(ip -4 addr show ens37 2>/dev/null | grep -oP '(?<=inet\s)\d+(\.\d+){3}' | head -n 1)
[ -z "$WIFI_IP" ] && WIFI_IP="$LAN_IP"

# Lấy Gateway của mạng Wi-Fi Hotspot để định tuyến âm thanh 2 chiều
HOTSPOT_GW=$(ip route show dev ens37 2>/dev/null | grep -oP '(?<=via\s)\d+(\.\d+){3}' | head -n 1)

echo "-> IP mạng LAN nội bộ (Win 7): $LAN_IP"
echo "-> IP mạng Wi-Fi/Hotspot (Điện thoại): $WIFI_IP"

echo -e "\n\e[36m=== [2/7] CÀI ĐẶT ASTERISK VÀ CÔNG CỤ GỬI MAIL MSMTP ===\e[0m"
apt-get update -y
DEBIAN_FRONTEND=noninteractive apt-get install -y asterisk msmtp msmtp-mta ca-certificates

echo -e "\n\e[36m=== [3/7] CẤU HÌNH PJSIP (TÀI KHOẢN SIP 101, 102, 103, 104, 105) ===\e[0m"
cat <<EOF > /etc/asterisk/pjsip.conf
[global]
type=global
user_agent=IUH-VoIP-Asterisk
message_context=send-message

[transport-udp]
type=transport
protocol=udp
bind=0.0.0.0:5060
local_net=192.168.1.0/24
local_net=192.168.5.0/24
local_net=192.168.6.0/24
local_net=10.0.0.0/8
local_net=100.64.0.0/10
external_signaling_address=$WIFI_IP
external_media_address=$WIFI_IP

[endpoint-template](!)
type=endpoint
context=nhanvien-context
message_context=send-message
disallow=all
allow=ulaw,alaw,g722,gsm
direct_media=no
rewrite_contact=yes
rtp_symmetric=yes
force_rport=yes
auth=auth-template
aors=aor-template

[auth-template](!)
type=auth
auth_type=userpass

[aor-template](!)
type=aor
max_contacts=5
remove_existing=yes

; --- EXTENSION 101: GIÁM ĐỐC (Win 7) ---
[101](endpoint-template)
auth=auth-101
aors=101
context=giamdoc-context
mailboxes=101@default

[auth-101](auth-template)
username=101
password=$SIP_PASSWORD

[101](aor-template)

; --- EXTENSION 102: PHÒNG KINH DOANH (Win 7) ---
[102](endpoint-template)
auth=auth-102
aors=102
context=nhanvien-context
mailboxes=102@default

[auth-102](auth-template)
username=102
password=$SIP_PASSWORD

[102](aor-template)

; --- EXTENSION 103: ĐIỆN THOẠI DI ĐỘNG 1 ---
[103](endpoint-template)
auth=auth-103
aors=103
context=nhanvien-context
mailboxes=103@default
media_address=$WIFI_IP
bind_rtp_to_media_address=yes

[auth-103](auth-template)
username=103
password=$SIP_PASSWORD

[103](aor-template)

; --- EXTENSION 104: ĐIỆN THOẠI DI ĐỘNG 2 ---
[104](endpoint-template)
auth=auth-104
aors=104
context=nhanvien-context
mailboxes=104@default
media_address=$WIFI_IP
bind_rtp_to_media_address=yes

[auth-104](auth-template)
username=104
password=$SIP_PASSWORD

[104](aor-template)

; --- EXTENSION 105: ĐIỆN THOẠI DI ĐỘNG 3 (DỰ PHÒNG) ---
[105](endpoint-template)
auth=auth-105
aors=105
context=nhanvien-context
mailboxes=105@default

[auth-105](auth-template)
username=105
password=$SIP_PASSWORD

[105](aor-template)
EOF

echo -e "\n\e[36m=== [4/7] CẤU HÌNH DIALPLAN (GỌI SỐ THẬT, GỌI NHÓM 600, CHẶN 101, IVR 100) ===\e[0m"
cat <<EOF > /etc/asterisk/extensions.conf
[general]
static=yes
writeprotect=no
clearglobalvars=no

[send-message]
exten => $PHONE_1_REAL,1,Set(MESSAGE(to)=sip:103@\${SERVER_IP})
same => n,MessageSend(pjsip:103)
same => n,Hangup()

exten => $PHONE_2_REAL,1,Set(MESSAGE(to)=sip:104@\${SERVER_IP})
same => n,MessageSend(pjsip:104)
same => n,Hangup()

exten => _X.,1,Set(MESSAGE(to)=sip:\${EXTEN}@\${SERVER_IP})
same => n,MessageSend(pjsip:\${EXTEN})
same => n,Hangup()

[giamdoc-context]
exten => 101,1,Dial(PJSIP/101,20)
same => n,Voicemail(101@default,u)
same => n,Hangup()

exten => $PHONE_1_REAL,1,Dial(PJSIP/103,20)
same => n,Voicemail(103@default,u)
same => n,Hangup()

exten => $PHONE_2_REAL,1,Dial(PJSIP/104,20)
same => n,Voicemail(104@default,u)
same => n,Hangup()

exten => _10X,1,Dial(PJSIP/\${EXTEN},20)
same => n,Voicemail(\${EXTEN}@default,u)
same => n,Hangup()

exten => 600,1,Goto(internal-common,600,1)
exten => 100,1,Goto(internal-common,100,1)

[nhanvien-context]
; Chặn cuộc gọi tới Giám đốc (101)
exten => 101,1,NoOp(--- CHẶN GỌI GIÁM ĐỐC ---)
same => n,Answer()
same => n,Playback(ss-noservice)
same => n,Hangup(17)

; Gọi số di động thật của máy 1 (103)
exten => $PHONE_1_REAL,1,Dial(PJSIP/103,20)
same => n,Voicemail(103@default,u)
same => n,Hangup()

; Gọi số di động thật của máy 2 (104)
exten => $PHONE_2_REAL,1,Dial(PJSIP/104,20)
same => n,Voicemail(104@default,u)
same => n,Hangup()

; Gọi các số máy nhánh ngắn 102, 103, 104, 105
exten => _10[2-9],1,Dial(PJSIP/\${EXTEN},20)
same => n,Voicemail(\${EXTEN}@default,u)
same => n,Hangup()

exten => 600,1,Goto(internal-common,600,1)
exten => 100,1,Goto(internal-common,100,1)

[internal-common]
; Yêu cầu 1: Gọi nhóm (Ext 600) rung tất cả các máy
exten => 600,1,Answer()
same => n,Dial(PJSIP/101&PJSIP/102&PJSIP/103&PJSIP/104&PJSIP/105,30)
same => n,Hangup()

; Yêu cầu 6: Tổng đài IVR (Ext 100)
exten => 100,1,Answer()
same => n,Background(demo-congrats)
same => n,WaitExten(10)

exten => 1,1,Dial(PJSIP/101,20)
same => n,Voicemail(101@default,u)
same => n,Hangup()

exten => 2,1,Dial(PJSIP/102,20)
same => n,Hangup()

exten => i,1,Playback(invalid)
same => n,Goto(100,1)

exten => t,1,Hangup()
EOF

echo -e "\n\e[36m=== [5/7] CẤU HÌNH HỘP THƯ THOẠI (VOICEMAIL & RTP SOUND) ===\e[0m"
cat <<EOF > /etc/asterisk/voicemail.conf
[general]
format=wav
attach=yes
maxmsg=100
maxmessage=300
minmessage=1
serveremail=$MY_GMAIL
emaildateformat=%A, %B %d, %Y at %r
emailsubject=[IUH-VoIP] Cuoc goi nho tu \${VM_CALLERID}
emailbody=Chao \${VM_NAME},\n\nBan co mot cuoc goi nho / loi nhan thoai tu so \${VM_CALLERID} vao luc \${VM_DATE}.\nFile ghi am loi nhan duoc dinh kem theo email nay.\n\nTran trong,\nTong dai VoIP IUH.

mailcmd=/usr/bin/msmtp -t

[default]
101 => 1234,Giam Doc IUH,$MY_GMAIL
102 => 1234,Phong Kinh Doanh,$MY_GMAIL
103 => 1234,Di Dong 1 ($PHONE_1_REAL),$MY_GMAIL
104 => 1234,Di Dong 2 ($PHONE_2_REAL),$MY_GMAIL
105 => 1234,Di Dong 3,$MY_GMAIL
EOF

# Tối ưu bắt âm thanh 2 chiều mượt mà không bị rớt gói
cat <<EOF > /etc/asterisk/rtp.conf
[general]
rtpstart=10000
rtpend=20000
strictrtp=no
probation=1
icesupport=false
EOF

echo -e "\n\e[36m=== [6/7] CẤU HÌNH GỬI EMAIL THẬT QUA GMAIL (MSMTP) ===\e[0m"
cat <<EOF > /etc/msmtprc
defaults
auth           on
tls            on
tls_trust_file /etc/ssl/certs/ca-certificates.crt
logfile        /var/log/msmtp.log

account        gmail
host           smtp.gmail.com
port           587
from           $MY_GMAIL
user           $MY_GMAIL
password       $MY_GMAIL_APP_PASS

account default : gmail
EOF

chmod 644 /etc/msmtprc
chown root:asterisk /etc/msmtprc 2>/dev/null || true
touch /var/log/msmtp.log
chmod 666 /var/log/msmtp.log

# Định tuyến âm thanh Hotspot điện thoại nếu có gateway
if [ -n "$HOTSPOT_GW" ]; then
    ip route del 10.0.0.0/8 2>/dev/null || true
    ip route del 100.64.0.0/10 2>/dev/null || true
    ip route add 10.0.0.0/8 via $HOTSPOT_GW dev ens37 2>/dev/null || true
    ip route add 100.64.0.0/10 via $HOTSPOT_GW dev ens37 2>/dev/null || true
fi

# Phân quyền cho Asterisk
chown -R asterisk:asterisk /etc/asterisk/
chmod 640 /etc/asterisk/*.conf

echo -e "\n\e[36m=== [7/7] KHỞI ĐỘNG LẠI DỊCH VỤ ASTERISK & TEST EMAIL ===\e[0m"
systemctl restart asterisk
systemctl enable asterisk

# Gửi thử 1 email kiểm tra kết nối Google
echo -e "Subject: [IUH-VoIP] Test ket noi Asterisk Gmail thanh cong!\n\nChuc mung ban! He thong VoIP da gui mail thanh cong." | msmtp -t "$MY_GMAIL" 2>/dev/null
if [ $? -eq 0 ]; then
    echo -e "\e[32m-> ĐÃ GỬI TEST EMAIL THÀNH CÔNG TỚI: $MY_GMAIL\e[0m"
else
    echo -e "\e[33m-> Lưu ý: Chưa gửi được test email. Hãy kiểm tra lại kết nối Internet hoặc App Password Gmail.\e[0m"
fi

echo -e "\n\e[32m=============================================================\e[0m"
echo -e "\e[32m      CHÚC MỪNG! HỆ THỐNG TỔNG ĐÀI VOIP ĐÃ SẴN SÀNG 100%    \e[0m"
echo -e "\e[32m=============================================================\e[0m"
echo -e "\e[33mTHÔNG TIN KẾT NỐI:\e[0m"
echo -e "  * Server IP cho máy ảo Win 7     : \e[32m$LAN_IP\e[0m"
echo -e "  * Server IP cho Điện thoại Wi-Fi : \e[32m$WIFI_IP\e[0m"
echo -e "  * Cổng SIP (UDP)                 : \e[32m5060\e[0m"
echo -e "\n\e[33mDANH SÁCH MÁY NHÁNH:\e[0m"
echo -e "  - Ext 101 : Giám đốc (Pass: $SIP_PASSWORD)"
echo -e "  - Ext 102 : Phòng Kinh Doanh (Pass: $SIP_PASSWORD)"
echo -e "  - Ext 103 : Di động 1 (Số thật: \e[36m$PHONE_1_REAL\e[0m) (Pass: $SIP_PASSWORD)"
echo -e "  - Ext 104 : Di động 2 (Số thật: \e[36m$PHONE_2_REAL\e[0m) (Pass: $SIP_PASSWORD)"
echo -e "  - Ext 105 : Di động 3 dự phòng (Pass: $SIP_PASSWORD)"
echo -e "  - Số Gọi nhóm : \e[32m600\e[0m (Tất cả các máy cùng reo)"
echo -e "  - Số IVR      : \e[32m100\e[0m (Tổng đài tự động)"
echo -e "\e[32m=============================================================\e[0m"
```

---

## ⚡ PHẦN 3: HƯỚNG DẪN CHẠY SCRIPT TRÊN UBUNTU (CHỈ 2 LỆNH)

1. Cấp quyền thực thi cho script:
   ```bash
   chmod +x setup_voip_all_in_one.sh
   ```
2. Chạy script với quyền root:
   ```bash
   sudo ./setup_voip_all_in_one.sh
   ```

*Chờ khoảng **15 - 30 giây**, toàn bộ hệ thống tổng đài Asterisk sẽ được cài đặt và cấu hình hoàn chỉnh 100%!*

---

## 📱 PHẦN 4: CÁCH ĐĂNG NHẬP TRÊN THIẾT BỊ (CLIENT)

### 1. Trên 2 máy ảo Windows 7 (Dùng phần mềm MicroSIP):

- **Máy 1 (Giám đốc):**
  - Account Name / Display Name: `Giám Đốc`
  - SIP Server / Domain: `192.168.1.100` (Điền IP LAN của Ubuntu)
  - Username / Login: **`101`**
  - Password: **`123456`**
- **Máy 2 (Kinh Doanh):**
  - Account Name / Display Name: `Kinh Doanh`
  - SIP Server / Domain: `192.168.1.100`
  - Username / Login: **`102`**
  - Password: **`123456`**

### 2. Trên 2 Điện thoại Di động thật (Cài App Sipnetic hoặc Zoiper):

> *Bắt buộc 2 điện thoại phải kết nối chung Wi-Fi (hoặc bắt chung điểm phát sóng 4G Hotspot) với Laptop.*

- **Điện thoại 1:**
  - Username / Account: **`103`**
  - Password: **`123456`**
  - Domain / Server: Điền IP Wi-Fi của Ubuntu (Ví dụ: `10.160.130.164`)
- **Điện thoại 2:**
  - Username / Account: **`104`**
  - Password: **`123456`**
  - Domain / Server: Điền IP Wi-Fi của Ubuntu (Ví dụ: `10.160.130.164`)

---

## 🧪 PHẦN 5: BẢNG KỊCH BẢN DEMO 5 PHÚT ĂN TRỌN ĐIỂM 10 CỦA THẦY

|     STT     | Bài Test                              | Cách thao tác                                                 | Kết quả thực tế đạt điểm 10                                    |
| :---------: | :------------------------------------- | :-------------------------------------------------------------- | :--------------------------------------------------------------------- |
| **1** | **Gọi số thật 10 chữ số**   | Bấm đúng số di động thật của bạn (VD:`0987214065`)   | Điện thoại thật trên tay đổ chuông to rõ, nghe nói 2 chiều. |
| **2** | **Gọi nhóm (Ring Group)**      | Bấm gọi số**`600`**                                  | Cả 4 máy (Win 7 và 2 Điện thoại) cùng reo chuông một lúc!    |
| **3** | **Gọi số ngắn nội bộ**      | Bấm số**`103`** hoặc **`104`**               | Kết nối ngay tức thì, âm thanh rõ nét.                          |
| **4** | **Nhắn tin tức thời (SIP)**   | Mở tab Messages gửi văn bản tới số`103` / số thật     | Màn hình điện thoại hiện tin nhắn Pop-up tức thì.             |
| **5** | **Chặn gọi tới Giám đốc**  | Từ máy`102` hoặc điện thoại bấm gọi **`101`** | **Bị chặn ngay lập tức**, nghe thông báo *ss-noservice*. |
| **6** | **Hộp thư thoại gửi Gmail**  | Gọi vào để lại lời nhắn sau tiếng bíp rồi cúp máy   | Nhận ngay 1 email có file đính kèm`.wav` trong Gmail.           |
| **7** | **Tổng đài tự động (IVR)** | Bấm gọi số**`100`**                                  | Nghe lời chào tự động: Phím 1 gặp Sếp, Phím 2 gặp KD.        |
