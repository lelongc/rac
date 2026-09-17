@echo off
:: ==============================================================================
:: CAI DAT IP TINH CHO WIN7_1 (LAN 1 - VMnet2) - LAB IUH
:: ==============================================================================
title CAI DAT IP WIN7_1
color 0a

net session >nul 2>&1
if %errorlevel% neq 0 (
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

echo ==============================================================================
echo   DANG CAI DAT IP CHO WIN7_1 (LAN 1):
echo   - IP Address:       192.168.5.1
echo   - Subnet Mask:      255.255.255.0
echo   - Default Gateway:  192.168.5.2 (Ubuntu 1)
echo   - DNS Server:       192.168.5.2
echo ==============================================================================

netsh interface ip set address "Local Area Connection" static 192.168.5.1 255.255.255.0 192.168.5.2
netsh interface ip set dns "Local Area Connection" static 192.168.5.2 primary

echo.
ipconfig /all
echo.
echo [V] DA CAI DAT XONG CHO WIN7_1!
pause
