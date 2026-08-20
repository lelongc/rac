@echo off
title TU DONG JOIN DOMAIN NEWSTAR.VN (CLIENT 1 - VMNET11)
echo ===================================================
echo   DANG CAU HINH TRO DNS VA JOIN DOMAIN NEWSTAR.VN
echo ===================================================

echo [1/3] Dang tro DNS ve Domain Controller (192.168.11.1)...
netsh interface ip set dns name="Local Area Connection" static 192.168.11.1
netsh interface ip set dns name="Ethernet0" static 192.168.11.1 2>nul
netsh interface ip set dns name="Ethernet" static 192.168.11.1 2>nul

echo.
echo [2/3] Dang kiem tra phan giai ten mien newstar.vn...
ping newstar.vn -n 2

echo.
echo [3/3] Dang tien hanh gia nhap Domain newstar.vn...
powershell -Command "Add-Computer -DomainName 'newstar.vn' -Credential (New-Object System.Management.Automation.PSCredential('NEWSTAR\Administrator', (ConvertTo-SecureString '123' -AsPlainText -Force))) -Restart -Force"

echo ===================================================
echo  LENH DA GUI! MAY SE TU DONG KHOI DONG LAI!
echo ===================================================
pause
