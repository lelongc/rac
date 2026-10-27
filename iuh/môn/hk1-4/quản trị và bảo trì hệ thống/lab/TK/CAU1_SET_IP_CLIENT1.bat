@echo off
chcp 65001 >nul
title CAU HINH IP CLIENT 1 - DE THI THUONG KY
color 0A

echo =======================================================
echo    DANG CAU HINH IP CHO CLIENT 1 THEO DE BAI
echo    IP: 192.168.1.1 ^| Mask: 255.255.255.0 ^| Gateway: 192.168.1.2
echo =======================================================
echo.

:: Tim ten card mang dang ket noi
set "NIC="
for /f "tokens=4*" %%a in ('netsh interface show interface ^| findstr /i "Connected Conectado"') do (
    set "NIC=%%a %%b"
)
if defined NIC (
    for /f "tokens=1*" %%a in ("%NIC%") do (
        if "%%b"=="" (set "NIC=%%a")
    )
)
if not defined NIC set "NIC=Local Area Connection 2"

echo [*] Ten card mang tim thay: "%NIC%"

netsh interface ip set address name="%NIC%" static 192.168.1.1 255.255.255.0 192.168.1.2
netsh advfirewall set allprofiles state off

echo.
echo =======================================================
echo [*] CAU HINH HOAN TAT! DANG KIEM TRA PING VE SERVER:
echo =======================================================
ipconfig | findstr /i "IPv4 Subnet Gateway"
echo.
ping 192.168.1.2 -n 2
echo.
pause
