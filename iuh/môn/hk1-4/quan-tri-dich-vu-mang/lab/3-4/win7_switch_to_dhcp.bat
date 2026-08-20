@echo off
:: ==============================================================================
:: SCRIPT TỰ ĐỘNG CHUYỂN WINDOWS 7 SANG NHẬN IP ĐỘNG (DHCP) - LAB 3 IUH
:: ==============================================================================
title CHUYEN WINDOWS 7 SANG NHAN IP DONG (DHCP)
color 0b

:: Tự động yêu cầu quyền Administrator nếu người dùng chỉ click đúp chuột
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [*] Dang yeu cau quyen Administrator...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
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
