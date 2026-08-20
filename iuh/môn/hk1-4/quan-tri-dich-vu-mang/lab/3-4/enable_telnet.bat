@echo off
title MO TELNET SERVER TREN WINDOWS 7
echo ========================================================
echo DANG BAT TELNET SERVER VA TAT TUONG LUA TREN WINDOWS 7...
echo ========================================================

:: 1. Bat tinh nang Telnet Server tren Windows 7
echo [1/5] Dang kich hoat Windows Feature TelnetServer...
dism /online /enable-feature /featurename:TelnetServer /NoRestart
pkgmgr /iu:"TelnetServer" /quiet

:: 2. Cau hinh Telnet Service chay tu dong va khoi dong
echo [2/5] Dang bat dich vu TlntSvr (Telnet Service)...
sc config TlntSvr start= auto
net start TlntSvr

:: 3. Chinh che do xac thuc cho phep mat khau (Khong bat buoc NTLM)
echo [3/5] Cau hinh Telnet chap nhan Password login...
tlntadmn config sec = -NTLM +passwd
tlntadmn config mode = console

:: 4. Mo Port 23 va Tat tuong lua Windows Firewall
echo [4/5] Dang mo Port 23 va Tat tuong lua...
netsh advfirewall firewall add rule name="Telnet Port 23" dir=in action=allow protocol=TCP localport=23
netsh advfirewall set allprofiles state off

:: 5. Tao tai khoan telnetadmin mat khau 123456
echo [5/5] Tao tai khoan phu telnetadmin / 123456...
net user telnetadmin 123456 /add
net localgroup Administrators telnetadmin /add
net localgroup "TelnetClients" telnetadmin /add 2>nul
net localgroup "TelnetClients" %USERNAME% /add 2>nul

echo ========================================================
echo DA MO XONG TELNET SERVER TREN WINDOWS 7!
echo IP cua may:
ipconfig | findstr /i "IPv4"
echo Tai khoan Telnet: telnetadmin  ^| Mat khau: 123456
echo ========================================================
pause
