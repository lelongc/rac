@echo off
:: ==============================================================================
:: SCRIPT TỰ ĐỘNG CHUYỂN WINDOWS 7 SANG NHẬN IP ĐỘNG (DHCP) - LAB 3 IUH
:: ==============================================================================
title CHUYEN WINDOWS 7 SANG NHAN IP DONG (DHCP)
color 0b

>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    echo [!] Vui long chay script voi quyen Administrator (Chuot phai -> Run as administrator)
    pause
    exit /b
)

echo ==============================================================================
echo   DANG CHUYEN CARD MANG SANG CHE DO NHAN IP VA DNS TU DONG (DHCP)...
echo ==============================================================================

:: 1. Chuyen sang DHCP
netsh interface ip set address name="Local Area Connection" source=dhcp
netsh interface ip set dnsservers name="Local Area Connection" source=dhcp

echo [*] Dang xin cap phat IP tu DHCP Server Ubuntu 1...
ipconfig /renew

echo ==============================================================================
echo   KET QUA NHAN IP DONG TU DHCP SERVER:
echo ==============================================================================
ipconfig /all

echo ==============================================================================
echo [V] DA CHUYEN SANG DHCP THANH CONG!
echo ==============================================================================
pause
