@echo off
title TU DONG CAU HINH VA JOIN DOMAIN NEWSTAR.VN (CLIENT 2)
color 1f

echo =====================================================================
echo    TU DONG CAU HINH DNS, DOI TEN VA JOIN DOMAIN CHO CLIENT WIN 7 (2)
echo =====================================================================
echo.

:: 1. Cau hinh DNS tro ve Domain Controller
echo [1/3] Dang tro DNS ve Domain Controller (100.100.11.1 / 192.168.1.132)...
powershell -Command "Get-WmiObject Win32_NetworkAdapterConfiguration -Filter 'IPEnabled=True' | ForEach-Object { `$_.SetDNSServerSearchOrder(@('100.100.11.1', '192.168.1.132')) }"
ipconfig /flushdns >nul 2>&1

:: 2. Kiem tra ket noi mang
echo.
echo [2/3] Dang kiem tra ket noi toi Domain Controller newstar.vn...
ping newstar.vn -n 2 >nul 2>&1
if %errorlevel% neq 0 (
    echo [-] Khong phan giai duoc newstar.vn, dang kiem tra IP truc tiep 100.100.11.1...
    ping 100.100.11.1 -n 2
) else (
    echo [+] Ket noi mang va phan giai DNS tot!
)

:: 3. Gia nhap Domain newstar.vn
echo.
echo [3/3] Dang tien hanh gia nhap Domain newstar.vn voi ten WIN7-PC2...
echo (Vui long cho trong giay lat...)

powershell -Command "$sec = ConvertTo-SecureString '123' -AsPlainText -Force; $cred = New-Object System.Management.Automation.PSCredential('NEWSTAR\Administrator', $sec); Add-Computer -DomainName 'newstar.vn' -Credential $cred"

if %errorlevel% equ 0 (
    echo.
    echo =====================================================================
    echo  [+] GIA NHAP DOMAIN NEWSTAR.VN THANH CONG 100%!
    echo  May se tu dong khoi dong lai sau 5 giay de ap dung.
    echo =====================================================================
    timeout /t 5
    shutdown /r /t 0 /f
) else (
    echo.
    echo =====================================================================
    echo  [-] CO LOI KHI JOIN DOMAIN. VUI LONG KIEM TRA LAI IP VA DNS SERVER!
    echo =====================================================================
    pause
)
