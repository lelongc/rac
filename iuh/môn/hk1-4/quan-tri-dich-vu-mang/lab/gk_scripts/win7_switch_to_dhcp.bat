@echo off
:: ==============================================================================
:: CHUYEN WIN 7 SANG NHAN IP DONG (DHCP) - LAB IUH
:: ==============================================================================
title CHUYEN SANG DHCP
color 0b

net session >nul 2>&1
if %errorlevel% neq 0 (
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

echo Dang chuyen card mang sang DHCP...
netsh interface ip set address "Local Area Connection" dhcp
netsh interface ip set dns "Local Area Connection" dhcp
ipconfig /renew
ipconfig /all
echo.
echo [V] DA CHUYEN SANG DHCP THANH CONG!
pause
