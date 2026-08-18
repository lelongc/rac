$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    $targetDirs = @("C:\THUCHANH\DULIEU", "C:\TAILIEU")

    # 1. File Đăng nhập KT1
    $batKT1 = @"
@echo off
title DANG NHAP KE TOAN 1 (KT1)
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

    # 2. File Đăng nhập KT2
    $batKT2 = @"
@echo off
title DANG NHAP KE TOAN 2 (KT2)
echo ===================================================
echo   DANG XOA KET NOI CU VA DANG NHAP BANG KT2...
echo ===================================================
net use * /delete /y
net use \\192.168.11.1\DATA 123 /user:KT2
net use Y: \\192.168.11.1\DATA 123 /user:KT2
echo.
echo ===================================================
echo   DA KET NOI THANH CONG VOI TAI KHOAN KT2!
echo   Dang mo thu muc \\192.168.11.1\DATA...
echo ===================================================
explorer.exe \\192.168.11.1\DATA
pause
"@

    # 3. File Đăng nhập NS1
    $batNS1 = @"
@echo off
title DANG NHAP NHAN SU 1 (NS1)
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

    # 4. File Đăng nhập NS2
    $batNS2 = @"
@echo off
title DANG NHAP NHAN SU 2 (NS2)
echo ===================================================
echo   DANG XOA KET NOI CU VA DANG NHAP BANG NS2...
echo ===================================================
net use * /delete /y
net use \\192.168.11.1\DATA 123 /user:NS2
net use Y: \\192.168.11.1\DATA 123 /user:NS2
echo.
echo ===================================================
echo   DA KET NOI THANH CONG VOI TAI KHOAN NS2!
echo   Dang mo thu muc \\192.168.11.1\DATA...
echo ===================================================
explorer.exe \\192.168.11.1\DATA
pause
"@

    foreach ($dir in $targetDirs) {
        $batKT1 | Out-File "$dir\2A_DANG_NHAP_KETOAN_KT1.bat" -Encoding ascii -Force
        $batKT2 | Out-File "$dir\2B_DANG_NHAP_KETOAN_KT2.bat" -Encoding ascii -Force
        $batNS1 | Out-File "$dir\3A_DANG_NHAP_NHANSU_NS1.bat" -Encoding ascii -Force
        $batNS2 | Out-File "$dir\3B_DANG_NHAP_NHANSU_NS2.bat" -Encoding ascii -Force
    }

    Write-Host "[+] Da tao xong cac file dang nhap KT1, KT2, NS1, NS2!" -ForegroundColor Green
}
