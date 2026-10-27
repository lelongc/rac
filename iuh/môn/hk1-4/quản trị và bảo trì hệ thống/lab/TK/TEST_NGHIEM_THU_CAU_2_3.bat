@echo off
chcp 65001 >nul
title KIEM TRA NGHIEM THU CAU 2 VA CAU 3 - DE THI THUONG KY
color 0B

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
"$sec = ConvertTo-SecureString '123' -AsPlainText -Force; ^
$cred = New-Object System.Management.Automation.PSCredential('Administrator', $sec); ^
Invoke-Command -ComputerName '192.168.1.151' -Credential $cred -ScriptBlock { ^
    Write-Host '================================================================' -ForegroundColor Yellow; ^
    Write-Host '          KET QUA NGHIEM THU CAU 2 & CAU 3 TREN SERVER 1        ' -ForegroundColor Yellow; ^
    Write-Host '================================================================' -ForegroundColor Yellow; ^
    Write-Host '`n--- CAU 2: NHOM VA USER ---' -ForegroundColor Cyan; ^
    foreach ($g in @('nhanvien', 'ketoan', 'nhansu')) { ^
        Write-Host ('[*] Nhom: ' + $g); ^
        net localgroup $g | Select-String -Pattern 'nv|kt|ns'; ^
    }; ^
    Write-Host '`n--- CAU 2: PHAN QUYEN NTFS THU MUC ---' -ForegroundColor Cyan; ^
    foreach ($d in @('DATANHANVIEN', 'DATAKETOAN', 'DATANHANSU')) { ^
        Write-Host ('`n[+] Thu muc: C:\DATACONGTY\' + $d) -ForegroundColor Green; ^
        (Get-Acl ('C:\DATACONGTY\' + $d)).Access | Select-Object IdentityReference, FileSystemRights, AccessControlType | Format-Table -AutoSize; ^
    }; ^
    Write-Host '`n--- CAU 3: PASSWORD POLICY & ACCOUNT LOCKOUT ---' -ForegroundColor Cyan; ^
    net accounts; ^
    Write-Host '`n--- CAU 3: USER RIGHTS ASSIGNMENT ---' -ForegroundColor Cyan; ^
    $inf = Get-Content 'C:\check_ur.inf'; ^
    $inf | Select-String -Pattern 'SeInteractiveLogonRight|SeDenyInteractiveLogonRight'; ^
}"

echo.
pause
