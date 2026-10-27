@echo off
chcp 65001 >nul
title NANG CAP SERVER 1 LEN DOMAIN CONTROLLER (abc.com)
color 0B

echo ===============================================================================
echo       TỰ ĐỘNG CÀI ĐẶT AD DS VÀ NÂNG CẤP SERVER THÀNH DOMAIN CONTROLLER
echo                           TÊN MIỀN: abc.com
echo ===============================================================================
echo.

:: 1. Kiểm tra quyền Administrator
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] VUI LÒNG CHUỘT PHẢI VÀO FILE NÀY VÀ CHỌN "RUN AS ADMINISTRATOR"!
    echo.
    pause
    exit /b 1
)

:: 2. Kiểm tra xem Server đã là DC chưa
powershell -NoProfile -Command "if ((Get-CimInstance Win32_OperatingSystem).ProductType -eq 2) { exit 10 } else { exit 0 }"
if %errorlevel% equ 10 (
    echo [*] Server 1 ĐÃ LÀ Domain Controller rồi! Khong can cai lai.
    echo [*] Tien hanh kiem tra va khoi dong DNS...
    net start DNS >nul 2>&1
    echo.
    echo Vui long chay file: SERVER1_TAO_USER_GROUP_SAU_KHI_LEN_DC.bat de cap nhat User/Group!
    pause
    exit /b 0
)

echo [1/4] Dang tro DNS noi bo tren Server 1 ve 127.0.0.1...
powershell -NoProfile -Command ^
"$nics = Get-NetAdapter | Where-Object { $_.Status -eq 'Up' }; ^
foreach ($nic in $nics) { ^
    netsh interface ip set dns name=$($nic.Name) static 127.0.0.1 primary; ^
}"
echo   -> Da tro DNS xong!

echo.
echo [2/4] Dang cai dat tinh nang Active Directory Domain Services (AD DS)...
powershell -NoProfile -Command "Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools"

echo.
echo [3/4] Dang nang cap Server 1 thanh Domain Controller (Forest: abc.com)...
echo (Qua trinh nay mat khoang 1-2 phut, sau do may se TU DONG KHOI DONG LAI)
echo.

powershell -NoProfile -Command ^
"$sec = ConvertTo-SecureString 'Abc@12345' -AsPlainText -Force; ^
Import-Module ADDSDeployment; ^
Install-ADDSForest -DomainName 'abc.com' `
                   -DomainNetbiosName 'ABC' `
                   -DomainMode 'Win2012R2' `
                   -ForestMode 'Win2012R2' `
                   -InstallDns:$true `
                   -SafeModeAdministratorPassword $sec `
                   -Force:$true"

echo.
echo ===============================================================================
echo Server dang khoi dong lai de hoan tat qua trinh len Domain Controller...
echo ===============================================================================
pause
