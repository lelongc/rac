#!/usr/bin/env bash
# ==============================================================================
# SCRIPT TỰ ĐỘNG CẤU HÌNH TỔNG ĐÀI VOIP ASTERISK TRÊN UBUNTU SERVER 22.04
# Môn: Quản trị dịch vụ mạng - IUH
# Đủ 6 yêu cầu: Gọi nhóm, Di động, Nhắn tin, Chặn cuộc gọi, Mail Gmail, IVR
# ==============================================================================

set -e

GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${CYAN}=====================================================${NC}"
echo -e "${CYAN}   KHỞI TẠO CẤU HÌNH TỔNG ĐÀI VOIP ASTERISK (IUH)    ${NC}"
echo -e "${CYAN}=====================================================${NC}"

if [ "$EUID" -ne 0 ]; then
  echo -e "${RED}Vui lòng chạy script với quyền root (sudo bash setup_voip_ubuntu.sh)${NC}"
  exit 1
fi

# Tắt hỏi đáp giao diện tương tác debconf khi apt install
export DEBIAN_FRONTEND=noninteractive

# 0. Tự động xóa triệt để dòng CDROM và bổ sung DNS Google 8.8.8.8
echo -e "${YELLOW}[0/5] Tự động dọn dẹp nguồn CDROM và thiết lập DNS Google...${NC}"
sed -i '/cdrom/d' /etc/apt/sources.list 2>/dev/null || true
echo "nameserver 8.8.8.8" > /etc/resolv.conf

# 1. Cập nhật hệ thống & cài đặt Asterisk + msmtp (gửi mail)
echo -e "\n${YELLOW}[1/5] Đang dọn dẹp Asterisk cũ (nếu có) và cài đặt mới...${NC}"
systemctl stop asterisk 2>/dev/null || true
systemctl disable asterisk 2>/dev/null || true
killall -9 asterisk 2>/dev/null || true
apt-get purge -y asterisk asterisk-core-sounds-en asterisk-core-sounds-en-wav asterisk-core-sounds-en-g722 asterisk-modules asterisk-voicemail asterisk-config >/dev/null 2>&1 || true
apt-get autoremove -y >/dev/null 2>&1 || true
apt-get clean >/dev/null 2>&1 || true
rm -rf /etc/asterisk /var/lib/asterisk /var/log/asterisk /var/spool/asterisk /usr/lib/asterisk /var/run/asterisk 2>/dev/null || true

apt-get update -y
apt-get install -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" asterisk asterisk-core-sounds-en-gsm msmtp msmtp-mta mailutils curl net-tools

cat <<EOF > /etc/asterisk/modules.conf
[modules]
autoload=yes
noload => app_voicemail_imap.so
noload => app_voicemail_odbc.so
load => app_voicemail.so
EOF

# 2. Lấy IP hiện tại của Ubuntu
SERVER_IP=$(hostname -I | awk '{print $1}')
echo -e "${GREEN}-> Địa chỉ IP của Server Ubuntu VoIP: ${SERVER_IP}${NC}"

# 3. Cấu hình Asterisk PJSIP (/etc/asterisk/pjsip.conf)
echo -e "\n${YELLOW}[2/5] Cấu hình các tài khoản SIP (101, 102, 103)...${NC}"
cp /etc/asterisk/pjsip.conf /etc/asterisk/pjsip.conf.bak 2>/dev/null || true

# Tự động phát hiện mạng LAN và mạng ngoài (VPN/Bridge)
DEFAULT_IFACE=$(ip route | awk '/default/ {print $5}' | head -n1)
if [ -n "$DEFAULT_IFACE" ]; then
    LOCAL_NET=$(ip route | grep "$DEFAULT_IFACE" | grep -v "default" | awk '{print $1}' | head -n1)
else
    LOCAL_NET="192.168.1.0/24"
fi

EXT_IFACE=$(ip -o link show | awk -F': ' '{print $2}' | grep -vE "lo|$DEFAULT_IFACE" | head -n1)
if [ -n "$EXT_IFACE" ]; then
    EXTERNAL_IP=$(ip -4 addr show $EXT_IFACE | grep -oP '(?<=inet\s)\d+(\.\d+){3}' | head -n 1)
else
    # Nếu máy chỉ có 1 card mạng
    EXTERNAL_IP=$(ip -4 addr show $DEFAULT_IFACE | grep -oP '(?<=inet\s)\d+(\.\d+){3}' | head -n 1)
fi

cat <<EOF > /etc/asterisk/pjsip.conf
[global]
type=global
user_agent=IUH-VoIP-Asterisk
message_context=send-message

[transport-udp]
type=transport
protocol=udp
bind=0.0.0.0:5060
local_net=$LOCAL_NET
external_signaling_address=$EXTERNAL_IP
external_media_address=$EXTERNAL_IP

; --- TEMPLATE CHUNG ---
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
mailboxes=

[auth-template](!)
type=auth
auth_type=userpass

[aor-template](!)
type=aor
max_contacts=2
remove_existing=yes

; --- EXTENSION 101: GIÁM ĐỐC (Win 7 - Máy 1) ---
[101](endpoint-template)
auth=auth-101
aors=101
context=giamdoc-context
mailboxes=101@default

[auth-101](auth-template)
username=101
password=123456

[101](aor-template)

; --- EXTENSION 102: PHÒNG KINH DOANH (Win 7 - Máy 2) ---
[102](endpoint-template)
auth=auth-102
aors=102
context=nhanvien-context

[auth-102](auth-template)
username=102
password=123456

[102](aor-template)

; --- EXTENSION 103: ĐIỆN THOẠI DI ĐỘNG 1 (App Mobile) ---
[103](endpoint-template)
auth=auth-103
aors=103
context=nhanvien-context

[auth-103](auth-template)
username=103
password=123456

[103](aor-template)

; --- EXTENSION 104: ĐIỆN THOẠI BẠN BÈ 1 (App Mobile / Softphone) ---
[104](endpoint-template)
auth=auth-104
aors=104
context=nhanvien-context

[auth-104](auth-template)
username=104
password=123456

[104](aor-template)

; --- EXTENSION 105: ĐIỆN THOẠI BẠN BÈ 2 (App Mobile / Softphone) ---
[105](endpoint-template)
auth=auth-105
aors=105
context=nhanvien-context

[auth-105](auth-template)
username=105
password=123456

[105](aor-template)
EOF

# 4. Cấu hình Modules (/etc/asterisk/modules.conf)
echo -e "\n\${YELLOW}Cấu hình modules.conf (Vô hiệu hóa chan_sip tránh xung đột)...\${NC}"
cat <<EOF > /etc/asterisk/modules.conf
[modules]
autoload=yes
noload => chan_sip.so
noload => app_voicemail_imap.so
noload => app_voicemail_odbc.so
load => app_voicemail.so
EOF

# 4. Cấu hình Extensions (Dialplan) (/etc/asterisk/extensions.conf)
echo -e "\n${YELLOW}[3/5] Cấu hình kịch bản cuộc gọi Dialplan (Ring Group, Blacklist, IVR)...${NC}"
cp /etc/asterisk/extensions.conf /etc/asterisk/extensions.conf.bak 2>/dev/null || true

cat <<EOF > /etc/asterisk/extensions.conf
[general]
static=yes
writeprotect=no
clearglobalvars=no

; ==============================================================================
; CONTEXT XỬ LÝ NHẮN TIN SIP (PJSIP MESSAGE)
; ==============================================================================
[send-message]
; Nhắn tin tới số di động thật của máy 103 (0987214065)
exten => 0987214065,1,NoOp(SIP MESSAGE to 0987214065 -> redirect to 103)
same => n,Set(MESSAGE(to)=sip:103@\${SERVER_IP})
same => n,MessageSend(pjsip:103)
same => n,Hangup()

; Nhắn tin tới số di động thật của máy 104 (0981647882)
exten => 0981647882,1,NoOp(SIP MESSAGE to 0981647882 -> redirect to 104)
same => n,Set(MESSAGE(to)=sip:104@\${SERVER_IP})
same => n,MessageSend(pjsip:104)
same => n,Hangup()

; Nhắn tin qua số extension nội bộ thông thường (_X.)
exten => _X.,1,NoOp(SIP MESSAGE from \${MESSAGE(from)} to \${EXTEN})
same => n,Set(MESSAGE(to)=sip:\${EXTEN}@\${SERVER_IP})
same => n,MessageSend(pjsip:\${EXTEN})
same => n,NoOp(MessageSend result: \${MESSAGE_SEND_STATUS})
same => n,Hangup()

; ==============================================================================
; CONTEXT CHO GIÁM ĐỐC (101): Được gọi tất cả mọi người (101-109 & Số di động thật)
; ==============================================================================
[giamdoc-context]
; Gọi số nội bộ Giám đốc (101)
exten => 101,1,Dial(PJSIP/101,20)
same => n,Voicemail(101@default,u)
same => n,Hangup()

; Gọi số di động thật của máy 103 (0987214065) -> Đổ chuông máy 103
exten => 0987214065,1,NoOp(--- GOI SO DI DONG THAT 0987214065 (MAY 103) ---)
same => n,Dial(PJSIP/103,20)
same => n,Voicemail(103@default,u)
same => n,Hangup()

; Gọi số di động thật của máy 104 (0981647882) -> Đổ chuông máy 104
exten => 0981647882,1,NoOp(--- GOI SO DI DONG THAT 0981647882 (MAY 104) ---)
same => n,Dial(PJSIP/104,20)
same => n,Voicemail(104@default,u)
same => n,Hangup()

; Gọi các số máy nhánh ngắn 102, 103, 104, 105...
exten => _10X,1,Dial(PJSIP/\${EXTEN},20)
same => n,Voicemail(\${EXTEN}@default,u)
same => n,Hangup()

exten => 600,1,Goto(internal-common,600,1)
exten => 100,1,Goto(internal-common,100,1)

; ==============================================================================
; CONTEXT CHO NHÂN VIÊN (102-109): Chặn không cho gọi tới Giám đốc (101)
; ==============================================================================
[nhanvien-context]
; --- YÊU CẦU 4: CHẶN CUỘC GỌI TỚI GIÁM ĐỐC (101) ---
exten => 101,1,NoOp(--- PHÒNG BAN GỌI GIÁM ĐỐC -> BỊ CHẶN ---)
same => n,Answer()
same => n,Playback(ss-noservice)
same => n,Hangup(17)

; --- Gọi số di động thật của máy 103 (0987214065) -> Đổ chuông máy 103 ---
exten => 0987214065,1,NoOp(--- NHAN VIEN GOI SO THAT 0987214065 (MAY 103) ---)
same => n,Dial(PJSIP/103,20)
same => n,Voicemail(103@default,u)
same => n,Hangup()

; --- Gọi số di động thật của máy 104 (0981647882) -> Đổ chuông máy 104 ---
exten => 0981647882,1,NoOp(--- NHAN VIEN GOI SO THAT 0981647882 (MAY 104) ---)
same => n,Dial(PJSIP/104,20)
same => n,Voicemail(104@default,u)
same => n,Hangup()

; --- Cho phép gọi các số ngắn 102, 103, 104, 105... ---
exten => _10[2-9],1,Dial(PJSIP/\${EXTEN},20)
same => n,Voicemail(\${EXTEN}@default,u)
same => n,Hangup()

exten => 600,1,Goto(internal-common,600,1)
exten => 100,1,Goto(internal-common,100,1)


; ==============================================================================
; DỊCH VỤ CHUNG: GỌI NHÓM & TỔNG ĐÀI TỰ ĐỘNG IVR
; ==============================================================================
[internal-common]
; --- YÊU CẦU 1: GỌI NHÓM (Ext 600) - Tất cả các máy cùng reo ---
exten => 600,1,NoOp(--- KÍCH HOẠT GỌI NHÓM 600 ---)
same => n,Answer()
same => n,Dial(PJSIP/101&PJSIP/102&PJSIP/103&PJSIP/104&PJSIP/105,30)
same => n,Hangup()

; --- YÊU CẦU 6: GỌI TỔNG ĐÀI IVR (Ext 100) ---
exten => 100,1,NoOp(--- KÍCH HOẠT TỔNG ĐÀI IVR 100 ---)
same => n,Answer()
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

# 5. Cấu hình Voicemail gửi Email (/etc/asterisk/voicemail.conf)
echo -e "\n${YELLOW}[4/5] Cấu hình Voicemail & Email cuộc gọi nhỡ...${NC}"
cp /etc/asterisk/voicemail.conf /etc/asterisk/voicemail.conf.bak 2>/dev/null || true

cat <<EOF > /etc/asterisk/voicemail.conf
[general]
format=wav
attach=yes
maxmsg=100
maxmessage=300
minmessage=1
emaildateformat=%A, %B %d, %Y at %r

emailsubject=[IUH-VoIP] Cuoc goi nho tu \${VM_CALLERID}
emailbody=Chao \${VM_NAME},\n\nBan co mot cuoc goi nho / loi nhan thoai tu số \${VM_CALLERID} vao lúc \${VM_DATE}.\nFile ghi âm loi nhan duoc dinh kem theo email nay.\n\nTran trong,\nTong dai VoIP IUH.

mailcmd=/usr/bin/msmtp -t

[default]
101 => 1234,Giam Doc IUH,lelong191001@gmail.com
102 => 1234,Phong Kinh Doanh,lelong191001@gmail.com
103 => 1234,Phong Ky Thuat,lelong191001@gmail.com
104 => 1234,Phong Ke Toan,lelong191001@gmail.com
105 => 1234,Phong Nhan Su,lelong191001@gmail.com
EOF

# 6. Cấu hình msmtp cho Gmail (Chỉ tạo mẫu nếu file chưa tồn tại)
if [ ! -f /etc/msmtprc ]; then
cat <<EOF > /etc/msmtprc
defaults
auth           on
tls            on
tls_trust_file /etc/ssl/certs/ca-certificates.crt
logfile        /var/log/msmtp.log

account        gmail
host           smtp.gmail.com
port           587
from           sv.iuh.demo@gmail.com
user           sv.iuh.demo@gmail.com
password       your_app_password_here

account default : gmail
EOF
fi

chmod 640 /etc/msmtprc
chown root:asterisk /etc/msmtprc 2>/dev/null || chown root:root /etc/msmtprc
touch /var/log/msmtp.log
chown asterisk:asterisk /var/log/msmtp.log 2>/dev/null || true
chmod 666 /var/log/msmtp.log


# 7. Restart và Enable Asterisk
echo -e "\n${YELLOW}[5/5] Khởi động lại dịch vụ Asterisk...${NC}"
systemctl restart asterisk
systemctl enable asterisk

echo -e "\n${GREEN}=====================================================${NC}"
echo -e "${GREEN}   HOÀN TẤT CẤU HÌNH TỔNG ĐÀI ASTERISK VOIP!        ${NC}"
echo -e "${GREEN}=====================================================${NC}"
echo -e "${CYAN}Thông tin các tài khoản SIP:${NC}"
echo -e "  - Server IP    : ${GREEN}${SERVER_IP}${NC}"
echo -e "  - Ext 101      : Giám đốc (Pass: 123456)"
echo -e "  - Ext 102      : Phòng KD (Pass: 123456)"
echo -e "  - Ext 103      : Di động 1 / Số thật: 0987214065 (Pass: 123456)"
echo -e "  - Ext 104      : Di động 2 / Số thật: 0981647882 (Pass: 123456)"
echo -e "  - Ext 105      : Di động 3 (Pass: 123456)"
echo -e "  - Số Gọi nhóm  : 600 (Rung tất cả các máy)"
echo -e "  - Số IVR       : 100"

echo -e "\n${YELLOW}Lưu ý: Để gửi email về Gmail thật, hãy mở file /etc/msmtprc và điền App Password Gmail của bạn.${NC}"

