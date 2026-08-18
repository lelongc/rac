$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    $targetDirs = @("C:\THUCHANH\DULIEU", "C:\TAILIEU")

    # 1. File bật remote
    $bat1 = @"
@echo off
echo ===================================================
echo   1. DANG BAT QUYEN REMOTE WINRM CHO WIN 7...
echo ===================================================
call winrm quickconfig -q
call net user Administrator 123 /active:yes
call netsh advfirewall set allprofiles state off
echo.
echo ===================================================
echo    DA BAT XONG QUYEN REMOTE WIN 7 THANH CONG!
echo ===================================================
pause
"@

    # 2. File đăng nhập KT1 (Kế toán)
    $bat2 = @"
@echo off
echo ===================================================
echo   2. DANG DANG NHAP TAI KHOAN KE TOAN (KT1)...
echo ===================================================
net use * /delete /y
net use Y: \\192.168.11.1\DATA 123 /user:192.168.11.1\KT1
echo.
echo ===================================================
echo  DA DANG NHAP KT1 VA GAN O DIA Y: THANH CONG!
echo  Dang mo thu muc DATA (Y:)...
echo ===================================================
pause
start explorer.exe Y:\
"@

    # 3. File đăng nhập NS1 (Nhân sự)
    $bat3 = @"
@echo off
echo ===================================================
echo   3. DANG DANG NHAP TAI KHOAN NHAN SU (NS1)...
echo ===================================================
net use * /delete /y
net use Y: \\192.168.11.1\DATA 123 /user:192.168.11.1\NS1
echo.
echo ===================================================
echo  DA DANG NHAP NS1 VA GAN O DIA Y: THANH CONG!
echo  Dang mo thu muc DATA (Y:)...
echo ===================================================
pause
start explorer.exe Y:\
"@

    # 4. File đăng nhập U1 (Bài 3)
    $bat4 = @"
@echo off
echo ===================================================
echo   4. DANG DANG NHAP TAI KHOAN USER U1...
echo ===================================================
net use * /delete /y
net use Z: \\192.168.11.1\TAILIEU 123 /user:192.168.11.1\U1
echo.
echo ===================================================
echo  DA DANG NHAP U1 VA GAN O DIA Z: (TAILIEU) THANH CONG!
echo  Dang mo thu muc TAILIEU (Z:)...
echo ===================================================
pause
start explorer.exe Z:\
"@

    foreach ($dir in $targetDirs) {
        $bat1 | Out-File "$dir\1_BAT_REMOTE_WIN7.bat" -Encoding ascii -Force
        $bat2 | Out-File "$dir\2_DANG_NHAP_KETOAN_KT1.bat" -Encoding ascii -Force
        $bat3 | Out-File "$dir\3_DANG_NHAP_NHANSU_NS1.bat" -Encoding ascii -Force
        $bat4 | Out-File "$dir\4_DANG_NHAP_USER_U1.bat" -Encoding ascii -Force
    }

    Write-Host "[+] Da tao xong 4 file script san sang trong ca DULIEU va TAILIEU!" -ForegroundColor Green
}
