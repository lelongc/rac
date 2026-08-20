@echo off
:: ==============================================================================
:: SCRIPT TỰ ĐỘNG KHÔI PHỤC IP TĨNH CHO WIN7_A (192.168.5.1) - LAB IUH
:: ==============================================================================
title KHOI PHUC IP TINH WIN7_A
color 0a

:: Tự động yêu cầu quyền Administrator nếu click đúp chuột
net session >nul 2>&1
if %errorlevel% neq 0 (
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

echo ==============================================================================
echo   DANG CAI DAT IP TINH CHO WIN7_A (LAN 1):
echo   - IP Address:       192.168.5.1
echo   - Subnet Mask:      255.255.255.0
echo   - Default Gateway:  192.168.5.2
echo   - DNS Server:       192.168.5.2
echo ==============================================================================

:: Cài đặt IP Tĩnh và DNS chuẩn Windows 7
netsh interface ip set address "Local Area Connection" static 192.168.5.1 255.255.255.0 192.168.5.2
netsh interface ip set dns "Local Area Connection" static 192.168.5.2 primary

echo.
echo ==============================================================================
echo   KET QUA CAI DAT:
echo ==============================================================================
ipconfig /all

echo.
echo ==============================================================================
echo [V] DA KHOI PHUC IP TINH CHO WIN7_A THANH CONG!
echo ==============================================================================
pause
