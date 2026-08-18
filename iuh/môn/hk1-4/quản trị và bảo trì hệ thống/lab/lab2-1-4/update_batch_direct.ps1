$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    $targetDirs = @("C:\THUCHANH\DULIEU", "C:\TAILIEU")

    # File 2: Đăng nhập KT1
    $bat2 = @"
@echo off
title DANG NHAP KE TOAN KT1
echo ===================================================
echo   DANG XOA KET NOI CU VA DANG NHAP BANG KT1...
echo ===================================================
net use * /delete /y
net use \\192.168.11.1\DATA 123 /user:KT1
net use Y: \\192.168.11.1\DATA 123 /user:KT1
echo.
echo ===================================================
echo   DA KET NOI THANH CONG VOI TAI KHOAN KT1!
echo   Dang mo thu muc \\192.168.11.1\DATA...
echo ===================================================
explorer.exe \\192.168.11.1\DATA
pause
"@

    # File 3: Đăng nhập NS1
    $bat3 = @"
@echo off
title DANG NHAP NHAN SU NS1
echo ===================================================
echo   DANG XOA KET NOI CU VA DANG NHAP BANG NS1...
echo ===================================================
net use * /delete /y
net use \\192.168.11.1\DATA 123 /user:NS1
net use Y: \\192.168.11.1\DATA 123 /user:NS1
echo.
echo ===================================================
echo   DA KET NOI THANH CONG VOI TAI KHOAN NS1!
echo   Dang mo thu muc \\192.168.11.1\DATA...
echo ===================================================
explorer.exe \\192.168.11.1\DATA
pause
"@

    # File 4: Đăng nhập U1
    $bat4 = @"
@echo off
title DANG NHAP USER U1
echo ===================================================
echo   DANG XOA KET NOI CU VA DANG NHAP BANG U1...
echo ===================================================
net use * /delete /y
net use \\192.168.11.1\TAILIEU 123 /user:U1
net use Z: \\192.168.11.1\TAILIEU 123 /user:U1
echo.
echo ===================================================
echo   DA KET NOI THANH CONG VOI TAI KHOAN U1!
echo   Dang mo thu muc \\192.168.11.1\TAILIEU...
echo ===================================================
explorer.exe \\192.168.11.1\TAILIEU
pause
"@

    foreach ($dir in $targetDirs) {
        $bat2 | Out-File "$dir\2_DANG_NHAP_KETOAN_KT1.bat" -Encoding ascii -Force
        $bat3 | Out-File "$dir\3_DANG_NHAP_NHANSU_NS1.bat" -Encoding ascii -Force
        $bat4 | Out-File "$dir\4_DANG_NHAP_USER_U1.bat" -Encoding ascii -Force
    }

    Write-Host "[+] Updated batch files with direct UNC explorer opening!" -ForegroundColor Green
}
