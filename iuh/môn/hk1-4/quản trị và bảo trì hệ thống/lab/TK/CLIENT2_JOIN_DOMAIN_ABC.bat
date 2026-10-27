@echo off
chcp 65001 >nul
title CLIENT 2 - TRO DNS VA JOIN DOMAIN abc.com
color 1F

echo ===============================================================================
echo            CLIENT 2: CẤU HÌNH DNS VÀ GIA NHẬP DOMAIN abc.com
echo ===============================================================================
echo.

:: 1. Tim card mang dang ket noi
set "NIC="
for /f "tokens=4*" %%a in ('netsh interface show interface ^| findstr /i "Connected Conectado"') do (
    set "NIC=%%a %%b"
)
if defined NIC (
    for /f "tokens=1*" %%a in ("%NIC%") do (
        if "%%b"=="" (set "NIC=%%a")
    )
)
if not defined NIC set "NIC=Local Area Connection"
echo [*] Card mạng: "%NIC%"

:: 2. Đặt DNS trỏ về Server 1 (20.20.1.2)
echo.
echo [1/3] Đang trỏ DNS về Server 1 (20.20.1.2)...
netsh interface ip set dns name="%NIC%" static 20.20.1.2 primary
ipconfig /flushdns >nul 2>&1
echo   -> Đã trỏ DNS thành công!

:: 3. Kiểm tra kết nối phân giải tên miền abc.com
echo.
echo [2/3] Kiểm tra phân giải tên miền abc.com...
ping abc.com -n 2 >nul 2>&1
if %errorlevel% neq 0 (
    echo [-] CHƯA PHÂN GIẢI ĐƯỢC abc.com!
    echo     Vui lòng đảm bảo Server 1 đã hoàn tất lên Domain Controller và khởi động xong.
    echo     Kiểm tra ping IP Server:
    ping 20.20.1.2 -n 2
    echo.
    pause
    exit /b 1
) else (
    echo [+] Đã kết nối và phân giải tên miền abc.com tốt!
)

:: 4. Tiến hành Join Domain abc.com
echo.
echo [3/3] Đang gia nhập Domain abc.com...
echo (Vui lòng chờ trong giây lát...)
powershell -NoProfile -Command ^
"$sec = ConvertTo-SecureString '123' -AsPlainText -Force; ^
$cred = New-Object System.Management.Automation.PSCredential('abc.com\Administrator', $sec); ^
try { ^
    Add-Computer -DomainName 'abc.com' -Credential $cred -ErrorAction Stop; ^
    Write-Host '  [+] GIA NHAP DOMAIN abc.com THANH CONG 100%!' -ForegroundColor Green; ^
    exit 0; ^
} catch { ^
    $sec2 = ConvertTo-SecureString 'Abc@12345' -AsPlainText -Force; ^
    $cred2 = New-Object System.Management.Automation.PSCredential('abc.com\Administrator', $sec2); ^
    try { ^
        Add-Computer -DomainName 'abc.com' -Credential $cred2 -ErrorAction Stop; ^
        Write-Host '  [+] GIA NHAP DOMAIN abc.com THANH CONG 100% (Password 2)!' -ForegroundColor Green; ^
        exit 0; ^
    } catch { ^
        Write-Host ('  [-] LOI: ' + $_.Exception.Message) -ForegroundColor Red; ^
        exit 1; ^
    } ^
}"

if %errorlevel% equ 0 (
    echo.
    echo ===============================================================================
    echo   GIA NHẬP DOMAIN abc.com THÀNH CÔNG!
    echo   Máy sẽ tự động khởi động lại sau 5 giây để áp dụng.
    echo ===============================================================================
    timeout /t 5
    shutdown /r /t 0 /f
) else (
    echo.
    echo ===============================================================================
    echo   CÓ LỖI XẢY RA KHI JOIN DOMAIN. Vui lòng kiểm tra lại mật khẩu Administrator!
    echo ===============================================================================
    pause
)
