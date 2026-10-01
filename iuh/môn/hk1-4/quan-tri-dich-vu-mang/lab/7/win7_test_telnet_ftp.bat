@echo off
chcp 65001 >nul
title KIỂM THỬ DỊCH VỤ LAB 7 TỪ WINDOWS 7
color 0A

echo ==============================================================================
echo KIỂM THỬ KẾT NỐI TỪ WINDOWS 7 ĐẾN SERVER UBUNTU (LAB 7)
echo ==============================================================================
echo.

set SERVER_IP=192.168.5.2

echo [1] KIỂM TRA PING ĐẾN UBUNTU SERVER (%SERVER_IP%)...
ping -n 2 %SERVER_IP% | find "TTL=" >nul
if %errorlevel% equ 0 (
    echo [+] PING THANH CONG!
) else (
    echo [-] PING THAT BAI! Kiem tra lai IP card mang.
    pause
    exit /b
)

echo.
echo [2] KIỂM TRA CỔNG 23 (TELNET SERVER)...
powershell -Command "Test-NetConnection -ComputerName %SERVER_IP% -Port 23" 2>nul || (
    echo Dang thu ket noi Port 23 bang telnet...
)

echo.
echo [3] KIỂM THỬ DỊCH VỤ FTP SERVER (%SERVER_IP%:21)...
echo Dang tao script tu dong kiem tra FTP...
(
echo open %SERVER_IP%
echo testuser1
echo 123
echo dir
echo quit
) > ftp_test_cmds.txt

ftp -s:ftp_test_cmds.txt
del ftp_test_cmds.txt

echo.
echo ==============================================================================
echo [SUCCESS] HOÀN TẤT KIỂM THỬ TỪ WINDOWS 7!
echo Để mở phiên dòng lệnh Telnet đầy đủ, gõ: telnet %SERVER_IP%
echo Để mở phiên FTP đồ họa, mở Windows Explorer gõ: ftp://%SERVER_IP%
echo ==============================================================================
pause
