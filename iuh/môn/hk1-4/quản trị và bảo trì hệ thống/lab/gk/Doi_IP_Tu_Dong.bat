@echo off
chcp 65001 >nul
title TOOL CAU HINH IP NHANH & MO KET NOI REMOTE - GK QTBTHT
color 0A

:: Kiem tra quyen Administrator
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Vui long chay file nay bang chuot phai -^> Run as Administrator!
    echo.
    pause
    exit /b
)

:MENU
cls
echo =====================================================================
echo       TOOL DOI IP NHANH & MO REMOTE PHONG THI GIUA KY QTBTHT
echo =====================================================================
echo.
echo  Chon may can cau hinh:
echo    [1] SERVER 1   - IP: 192.168.1.1  ^| DNS: 127.0.0.1 (Domain nhom1.vn)
echo    [2] CLIENT 1   - IP: 192.168.1.2  ^| Gateway & DNS: 192.168.1.1
echo    [3] CLIENT 2   - IP: 192.168.1.3  ^| Gateway & DNS: 192.168.1.1
echo    [4] TU NHAP IP (Khi de thi cho dai mang khac: 172.16.x.x, ...)
echo    [5] Tra ve IP Dong (DHCP)
echo    [6] Kiem tra IP hien tai & Test Ping
echo    [0] Thoat
echo =====================================================================
set /p opt="Nhap lua chon cua ban [1-6, 0]: "

if "%opt%"=="1" goto SET_SERVER
if "%opt%"=="2" goto SET_CLIENT1
if "%opt%"=="3" goto SET_CLIENT2
if "%opt%"=="4" goto SET_CUSTOM
if "%opt%"=="5" goto SET_DHCP
if "%opt%"=="6" goto TEST_IP
if "%opt%"=="0" exit /b
goto MENU

:DETECT_NIC
:: Tu dong tim ten card mang dang ket noi (Ethernet hoac Local Area Connection)
set "NIC="
for /f "tokens=4*" %%a in ('netsh interface show interface ^| findstr /i "Connected Conectado"') do (
    set "NIC=%%a %%b"
)
:: Loai bo khoang trang thua neu chi co 1 tu (nhu "Ethernet")
if defined NIC (
    for /f "tokens=1*" %%a in ("%NIC%") do (
        if "%%b"=="" (set "NIC=%%a")
    )
)
if not defined NIC (
    :: Fallback mac dinh
    set "NIC=Ethernet"
)
echo [*] Card mang dang su dung: "%NIC%"
goto :eof

:OPEN_SERVICES
echo [*] Dang tat Windows Firewall de PING thong suot 100%%...
netsh advfirewall set allprofiles state off >nul 2>&1

echo [*] Dang bat Remote Desktop (RDP)...
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f >nul 2>&1

echo [*] Dang kich hoat WinRM (Remote Management cho AI / Script)...
call powershell -Command "Enable-PSRemoting -Force -SkipNetworkProfileCheck" >nul 2>&1
goto :eof

:SET_SERVER
call :DETECT_NIC
echo.
echo [*] Dang thiet lap IP cho SERVER 1: 192.168.1.1 ...
netsh interface ip set address name="%NIC%" static 192.168.1.1 255.255.255.0
netsh interface ip set dns name="%NIC%" static 127.0.0.1
call :OPEN_SERVICES
echo.
echo [V] DA CAU HINH XONG SERVER 1!
ipconfig | findstr /i "IPv4 Subnet"
echo.
pause
goto MENU

:SET_CLIENT1
call :DETECT_NIC
echo.
echo [*] Dang thiet lap IP cho CLIENT 1: 192.168.1.2 ...
netsh interface ip set address name="%NIC%" static 192.168.1.2 255.255.255.0 192.168.1.1
netsh interface ip set dns name="%NIC%" static 192.168.1.1
call :OPEN_SERVICES
echo.
echo [V] DA CAU HINH XONG CLIENT 1!
ipconfig | findstr /i "IPv4 Subnet"
echo.
echo [*] Dang thu Ping sang Server 192.168.1.1 ...
ping 192.168.1.1 -n 2
echo.
pause
goto MENU

:SET_CLIENT2
call :DETECT_NIC
echo.
echo [*] Dang thiet lap IP cho CLIENT 2: 192.168.1.3 ...
netsh interface ip set address name="%NIC%" static 192.168.1.3 255.255.255.0 192.168.1.1
netsh interface ip set dns name="%NIC%" static 192.168.1.1
call :OPEN_SERVICES
echo.
echo [V] DA CAU HINH XONG CLIENT 2!
ipconfig | findstr /i "IPv4 Subnet"
echo.
echo [*] Dang thu Ping sang Server 192.168.1.1 ...
ping 192.168.1.1 -n 2
echo.
pause
goto MENU

:SET_CUSTOM
call :DETECT_NIC
echo.
set /p CIP="Nhap dia chi IP (vi du: 172.16.10.1): "
set /p CMS="Nhap Subnet Mask (mac dinh: 255.255.255.0) [Enter de lay mac dinh]: "
if "%CMS%"=="" set "CMS=255.255.255.0"
set /p CGW="Nhap Default Gateway (neu Server de trong thi an Enter): "
set /p CDNS="Nhap DNS Server (Client nhap IP Server, Server nhap 127.0.0.1): "

echo.
echo [*] Dang ap dung IP tuy chinh...
if "%CGW%"=="" (
    netsh interface ip set address name="%NIC%" static %CIP% %CMS%
) else (
    netsh interface ip set address name="%NIC%" static %CIP% %CMS% %CGW%
)

if not "%CDNS%"=="" (
    netsh interface ip set dns name="%NIC%" static %CDNS%
)
call :OPEN_SERVICES
echo.
echo [V] DA AP DUNG IP TUY CHINH XONG!
ipconfig | findstr /i "IPv4 Subnet Gateway"
echo.
pause
goto MENU

:SET_DHCP
call :DETECT_NIC
echo.
echo [*] Dang tra ve che do IP Dong (DHCP)...
netsh interface ip set address name="%NIC%" dhcp
netsh interface ip set dns name="%NIC%" dhcp
echo.
echo [V] DA TRA VE DHCP!
ipconfig /renew >nul 2>&1
ipconfig | findstr /i "IPv4 Subnet"
echo.
pause
goto MENU

:TEST_IP
cls
echo =====================================================================
echo                THONG TIN CARD MANG & TEST KET NOI
echo =====================================================================
ipconfig /all | findstr /i "IPv4 Description Subnet Gateway DNS"
echo.
echo ---------------------------------------------------------------------
set /p test_ip="Nhap dia chi IP can ping thu (vi du 192.168.1.1): "
if not "%test_ip%"=="" (
    echo.
    ping %test_ip%
)
echo.
pause
goto MENU
