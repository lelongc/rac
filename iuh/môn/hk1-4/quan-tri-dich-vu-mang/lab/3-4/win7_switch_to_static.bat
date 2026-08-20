@echo off
:: ==============================================================================
:: SCRIPT TỰ ĐỘNG KHÔI PHỤC IP TĨNH CHO WINDOWS 7 - LAB 1, 2, 3 IUH
:: ==============================================================================
title KHOI PHUC IP TINH CHO WINDOWS 7
color 0a

>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    echo [!] Vui long chay script voi quyen Administrator (Chuot phai -> Run as administrator)
    pause
    exit /b
)

echo ==============================================================================
echo   CHON MAY WINDOWS 7 CAN KHOI PHUC IP TINH:
echo ==============================================================================
echo   [1] May Win7_A (LAN 1): IP 192.168.5.1  ^| Gateway 192.168.5.2 ^| DNS 192.168.5.2
echo   [2] May Win7_B (LAN 2): IP 192.168.6.1  ^| Gateway 192.168.6.3 ^| DNS 192.168.5.2
echo ==============================================================================
set /p opt="Nhap lua chon cua ban (1 hoac 2): "

if "%opt%"=="1" (
    echo [*] Dang cai dat IP Tinh cho Win7_A (192.168.5.1)...
    netsh interface ip set address name="Local Area Connection" static 192.168.5.1 255.255.255.0 192.168.5.2 1
    netsh interface ip set dnsservers name="Local Area Connection" static 192.168.5.2 primary
) else if "%opt%"=="2" (
    echo [*] Dang cai dat IP Tinh cho Win7_B (192.168.6.1)...
    netsh interface ip set address name="Local Area Connection" static 192.168.6.1 255.255.255.0 192.168.6.3 1
    netsh interface ip set dnsservers name="Local Area Connection" static 192.168.5.2 primary
) else (
    echo [!] Lua chon khong hop le.
    pause
    exit /b
)

echo ==============================================================================
echo   KET QUA CAI DAT IP TINH:
echo ==============================================================================
ipconfig /all

echo ==============================================================================
echo [V] DA KHOI PHUC IP TINH CHUAN XAC THANH CONG!
echo ==============================================================================
pause
