@echo off
chcp 65001 >nul
title TAO USER, GROUP VA PHAN QUYEN DOMAIN (ABC.COM) - CAU 2 & 3
color 0A

echo ===============================================================================
echo        TẠO USER, GROUP VÀ PHÂN QUYỀN DOMAIN TRÊN DOMAIN CONTROLLER (abc.com)
echo ===============================================================================
echo.

:: 1. TẠO CÁC NHÓM TRÊN DOMAIN
echo [1/6] Tạo 3 Nhóm Domain: nhanvien, ketoan, nhansu...
powershell -NoProfile -Command ^
"Import-Module ActiveDirectory; ^
foreach ($g in @('nhanvien', 'ketoan', 'nhansu')) { ^
    if (-not (Get-ADGroup -Filter {Name -eq $g} -ErrorAction SilentlyContinue)) { ^
        New-ADGroup -Name $g -GroupScope Global -GroupCategory Security; ^
        Write-Host ('  + Da tao nhom Domain: ' + $g); ^
    } else { ^
        Write-Host ('  * Nhom ' + $g + ' da ton tai.'); ^
    } ^
}"

:: 2. TẠO CÁC USER TRÊN DOMAIN VỚI PASSWORD Abc@12345
echo.
echo [2/6] Tạo 6 User Domain: nv1, nv2, kt1, kt2, ns1, ns2 (Password: Abc@12345)...
powershell -NoProfile -Command ^
"Import-Module ActiveDirectory; ^
$sec = ConvertTo-SecureString 'Abc@12345' -AsPlainText -Force; ^
$users = @( ^
    @{Name='nv1'; Group='nhanvien'}, ^
    @{Name='nv2'; Group='nhanvien'}, ^
    @{Name='kt1'; Group='ketoan'}, ^
    @{Name='kt2'; Group='ketoan'}, ^
    @{Name='ns1'; Group='nhansu'}, ^
    @{Name='ns2'; Group='nhansu'} ^
); ^
foreach ($u in $users) { ^
    if (-not (Get-ADUser -Filter {SamAccountName -eq $u.Name} -ErrorAction SilentlyContinue)) { ^
        New-ADUser -Name $u.Name -SamAccountName $u.Name -AccountPassword $sec -Enabled $true -PasswordNeverExpires $true; ^
        Write-Host ('  + Da tao user Domain: ' + $u.Name); ^
    } else { ^
        Set-ADAccountPassword -Identity $u.Name -NewPassword $sec -Reset; ^
        Set-ADUser -Identity $u.Name -Enabled $true -PasswordNeverExpires $true; ^
        Write-Host ('  * User ' + $u.Name + ' da ton tai, da reset password.'); ^
    }; ^
    Add-ADGroupMember -Identity $u.Group -Members $u.Name -ErrorAction SilentlyContinue; ^
    Write-Host ('  -> Da add ' + $u.Name + ' vao nhom ' + $u.Group); ^
}"

:: 3. TẠO THƯ MỤC C:\DATACONGTY VÀ CÁC THƯ MỤC CON
echo.
echo [3/6] Tạo thư mục C:\DATACONGTY và các thư mục con...
if not exist "C:\DATACONGTY" md "C:\DATACONGTY"
if not exist "C:\DATACONGTY\DATANHANVIEN" md "C:\DATACONGTY\DATANHANVIEN"
if not exist "C:\DATACONGTY\DATAKETOAN" md "C:\DATACONGTY\DATAKETOAN"
if not exist "C:\DATACONGTY\DATANHANSU" md "C:\DATACONGTY\DATANHANSU"

echo Du lieu Nhan Vien (Domain abc.com) > "C:\DATACONGTY\DATANHANVIEN\tailieu_nv.txt"
echo Du lieu Ke Toan (Domain abc.com) > "C:\DATACONGTY\DATAKETOAN\baocao_kt.txt"
echo Du lieu Nhan Su (Domain abc.com) > "C:\DATACONGTY\DATANHANSU\hoso_ns.txt"

net share DATACONGTY="C:\DATACONGTY" /grant:Everyone,FULL >nul 2>&1
echo   -> Da chia se thu muc C:\DATACONGTY ra mang!

:: 4. PHÂN QUYỀN NTFS (ICACLS CHUẨN MICROSOFT)
echo.
echo [4/6] Phân quyền NTFS chi tiết cho các nhóm Domain...

:: DATACONGTY gốc:
icacls "C:\DATACONGTY" /inheritance:r /grant:r Administrators:(OI)(CI)F /grant:r SYSTEM:(OI)(CI)F /grant:r "ABC\nhanvien":(OI)(CI)R /grant:r "ABC\ketoan":(OI)(CI)R /grant:r "ABC\nhansu":(OI)(CI)R >nul 2>&1

:: DATANHANVIEN:
:: nhanvien: F, nhansu: F, ketoan: M nhung DENY DE
icacls "C:\DATACONGTY\DATANHANVIEN" /inheritance:r /grant:r Administrators:(OI)(CI)F /grant:r SYSTEM:(OI)(CI)F /grant:r "ABC\nhanvien":(OI)(CI)F /grant:r "ABC\nhansu":(OI)(CI)F /grant:r "ABC\ketoan":(OI)(CI)M /deny "ABC\ketoan":(OI)(CI)DE >nul 2>&1

:: DATAKETOAN:
:: ketoan: F, nhansu: RX, nhanvien: DENY F
icacls "C:\DATACONGTY\DATAKETOAN" /inheritance:r /grant:r Administrators:(OI)(CI)F /grant:r SYSTEM:(OI)(CI)F /grant:r "ABC\ketoan":(OI)(CI)F /grant:r "ABC\nhansu":(OI)(CI)RX /deny "ABC\nhanvien":(OI)(CI)F >nul 2>&1

:: DATANHANSU:
:: nhansu: F, ketoan: RX, nhanvien: DENY F
icacls "C:\DATACONGTY\DATANHANSU" /inheritance:r /grant:r Administrators:(OI)(CI)F /grant:r SYSTEM:(OI)(CI)F /grant:r "ABC\nhansu":(OI)(CI)F /grant:r "ABC\ketoan":(OI)(CI)RX /deny "ABC\nhanvien":(OI)(CI)F >nul 2>&1

echo   -> Da phan quyen NTFS xong 100%!

:: 5. CHÍNH SÁCH MẬT KHẨU & ACCOUNT LOCKOUT (CÂU 3)
echo.
echo [5/6] Cấu hình Password Policy & Account Lockout...
net accounts /minpwlen:8 /lockoutthreshold:5 /lockoutduration:5 /lockoutwindow:5 >nul

:: 6. CHÍNH SÁCH ALLOW / DENY LOGON LOCALLY
echo.
echo [6/6] Cấu hình quyền đăng nhập Allow/Deny Logon Locally...
secedit /export /cfg "C:\sec_tk.inf" /quiet
powershell -NoProfile -Command ^
"$inf = Get-Content 'C:\sec_tk.inf'; ^
$inf = $inf -replace 'PasswordComplexity\s*=.*', 'PasswordComplexity = 1'; ^
if ($inf -notmatch 'PasswordComplexity\s*=') { $inf = $inf -replace '\[System Access\]', '[System Access]`r`nPasswordComplexity = 1' }; ^
if ($inf -notmatch '\[Privilege Rights\]') { $inf += '`r`n[Privilege Rights]' }; ^
if ($inf -match 'SeInteractiveLogonRight\s*=') { $inf = $inf -replace 'SeInteractiveLogonRight\s*=.*', 'SeInteractiveLogonRight = *S-1-5-32-544,nv1,kt1,ns1' } else { $inf = $inf -replace '\[Privilege Rights\]', '[Privilege Rights]`r`nSeInteractiveLogonRight = *S-1-5-32-544,nv1,kt1,ns1' }; ^
if ($inf -match 'SeDenyInteractiveLogonRight\s*=') { $inf = $inf -replace 'SeDenyInteractiveLogonRight\s*=.*', 'SeDenyInteractiveLogonRight = nv2,kt2,ns2' } else { $inf = $inf -replace '\[Privilege Rights\]', '[Privilege Rights]`r`nSeDenyInteractiveLogonRight = nv2,kt2,ns2' }; ^
Set-Content -Path 'C:\sec_tk.inf' -Value $inf -Encoding Ascii"

secedit /configure /db "C:\sec_tk.sdb" /cfg "C:\sec_tk.inf" /areas SECURITYPOLICY USER_RIGHTS /quiet
gpupdate /force >nul 2>&1

echo.
echo ===============================================================================
echo   HOÀN THÀNH TOÀN BỘ CẤU HÌNH DOMAIN abc.com CHO CÂU 2 VÀ CÂU 3!
echo ===============================================================================
pause
