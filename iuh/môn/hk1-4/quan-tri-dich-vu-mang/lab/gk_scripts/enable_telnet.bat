@echo off
title MO TELNET SERVER TREN WINDOWS 7
color 0a

:: TU DONG XIN QUYEN ADMINISTRATOR (UAC)
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [*] Dang yeu cau quyen Administrator...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

echo ========================================================
echo DANG BAT TELNET SERVER VA TAT TUONG LUA TREN WINDOWS 7...
echo ========================================================

:: 1. Tat tuong lua ngay lap tuc
echo [1/6] Tat tuong lua Windows Firewall...
netsh advfirewall set allprofiles state off

:: 2. Bat tinh nang Telnet Server tren Windows 7
echo [2/6] Dang kich hoat Windows Feature TelnetServer...
dism /online /enable-feature /featurename:TelnetServer /NoRestart
pkgmgr /iu:"TelnetServer" /quiet

:: 3. Chinh che do xac thuc cho phep mat khau (Khong bat buoc NTLM)
echo [3/6] Cau hinh Telnet chap nhan Password login (Tat NTLM)...
tlntadmn config sec = -NTLM +passwd
tlntadmn config mode = console

:: 4. Cau hinh Telnet Service chay tu dong va khoi dong lai
echo [4/6] Khoi dong dich vu Telnet (TlntSvr)...
sc config TlntSvr start= auto
net stop TlntSvr >nul 2>&1
net start TlntSvr

:: 5. Tao tai khoan telnetadmin mat khau 123456 & cap quyen TelnetClients
echo [5/6] Tao tai khoan phu telnetadmin / 123456...
net user telnetadmin 123456 /add >nul 2>&1
net localgroup Administrators telnetadmin /add >nul 2>&1
net localgroup TelnetClients /add >nul 2>&1
net localgroup TelnetClients telnetadmin /add >nul 2>&1
net localgroup TelnetClients Administrator /add >nul 2>&1
net localgroup TelnetClients %USERNAME% /add >nul 2>&1

:: 6. Mo port 23
netsh advfirewall firewall add rule name="Telnet Port 23" dir=in action=allow protocol=TCP localport=23

echo ========================================================
echo [V] DA MO XONG TELNET SERVER TREN WINDOWS 7!
echo IP cua may:
ipconfig | findstr /i "IPv4"
echo Tai khoan Telnet: telnetadmin  ^| Mat khau: 123456
echo ========================================================
pause
