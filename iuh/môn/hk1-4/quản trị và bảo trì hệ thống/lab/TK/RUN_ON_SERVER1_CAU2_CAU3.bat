@echo off
chcp 65001 >nul
title CAU HINH TOAN BO CAU 2 VA CAU 3 TREN SERVER 1
color 0A

echo ===============================================================================
echo            CẤU HÌNH TỰ ĐỘNG CÂU 2 & CÂU 3 (100%% CHUẨN ĐỀ BÀI)
echo ===============================================================================
echo.

:: 1. TẠO CÁC NHÓM
echo [1/6] Tạo 3 Nhóm: nhanvien, ketoan, nhansu...
net localgroup nhanvien /add >nul 2>&1
net localgroup ketoan /add >nul 2>&1
net localgroup nhansu /add >nul 2>&1
echo   -> Đã tạo 3 nhóm thành công!

:: 2. TẠO CÁC USER VỚI PASSWORD CHUẨN Abc@12345
echo.
echo [2/6] Tạo 6 User: nv1, nv2, kt1, kt2, ns1, ns2 (Password: Abc@12345)...
net user nv1 Abc@12345 /add /passwordchg:no >nul 2>&1 || net user nv1 Abc@12345
net user nv2 Abc@12345 /add /passwordchg:no >nul 2>&1 || net user nv2 Abc@12345
net user kt1 Abc@12345 /add /passwordchg:no >nul 2>&1 || net user kt1 Abc@12345
net user kt2 Abc@12345 /add /passwordchg:no >nul 2>&1 || net user kt2 Abc@12345
net user ns1 Abc@12345 /add /passwordchg:no >nul 2>&1 || net user ns1 Abc@12345
net user ns2 Abc@12345 /add /passwordchg:no >nul 2>&1 || net user ns2 Abc@12345

:: Đặt không bao giờ hết hạn
wmic useraccount where "Name='nv1' or Name='nv2' or Name='kt1' or Name='kt2' or Name='ns1' or Name='ns2'" set PasswordExpires=FALSE >nul 2>&1

:: Thêm User vào Nhóm
net localgroup nhanvien nv1 /add >nul 2>&1
net localgroup nhanvien nv2 /add >nul 2>&1
net localgroup ketoan kt1 /add >nul 2>&1
net localgroup ketoan kt2 /add >nul 2>&1
net localgroup nhansu ns1 /add >nul 2>&1
net localgroup nhansu ns2 /add >nul 2>&1
echo   -> Đã thêm User vào Nhóm tương ứng!

:: 3. TẠO THƯ MỤC C:\DATACONGTY VÀ 3 THƯ MỤC CON
echo.
echo [3/6] Tạo thư mục C:\DATACONGTY và các thư mục con...
if not exist "C:\DATACONGTY" md "C:\DATACONGTY"
if not exist "C:\DATACONGTY\DATANHANVIEN" md "C:\DATACONGTY\DATANHANVIEN"
if not exist "C:\DATACONGTY\DATAKETOAN" md "C:\DATACONGTY\DATAKETOAN"
if not exist "C:\DATACONGTY\DATANHANSU" md "C:\DATACONGTY\DATANHANSU"

:: Tạo file dữ liệu mẫu bên trong
echo Du lieu Nhan Vien > "C:\DATACONGTY\DATANHANVIEN\tailieu_nv.txt"
echo Du lieu Ke Toan > "C:\DATACONGTY\DATAKETOAN\baocao_kt.txt"
echo Du lieu Nhan Su > "C:\DATACONGTY\DATANHANSU\hoso_ns.txt"

:: Chia sẻ thư mục DATACONGTY ra mạng
net share DATACONGTY="C:\DATACONGTY" /grant:Everyone,FULL >nul 2>&1
echo   -> Đã tạo và Share thư mục C:\DATACONGTY thành công!

:: 4. PHÂN QUYỀN NTFS (ICACLS CHUẨN MICROSOFT)
echo.
echo [4/6] Đang phân quyền NTFS cho từng thư mục...

:: Thư mục gốc DATACONGTY: Tắt kế thừa, gán quyền cho Admin, SYSTEM và các nhóm được mở xem
icacls "C:\DATACONGTY" /inheritance:r /grant:r Administrators:(OI)(CI)F /grant:r SYSTEM:(OI)(CI)F /grant:r nhanvien:(OI)(CI)R /grant:r ketoan:(OI)(CI)R /grant:r nhansu:(OI)(CI)R >nul

:: DATANHANVIEN:
:: - nhanvien: Toàn quyền (F)
:: - nhansu: Toàn quyền (F)
:: - ketoan: Thay đổi (M) nhưng CẤM XÓA (Deny DE - Delete)
icacls "C:\DATACONGTY\DATANHANVIEN" /inheritance:r /grant:r Administrators:(OI)(CI)F /grant:r SYSTEM:(OI)(CI)F /grant:r nhanvien:(OI)(CI)F /grant:r nhansu:(OI)(CI)F /grant:r ketoan:(OI)(CI)M /deny ketoan:(OI)(CI)DE >nul

:: DATAKETOAN:
:: - ketoan: Toàn quyền (F)
:: - nhansu: Chỉ đọc (RX)
:: - nhanvien: Cấm truy cập (Deny F)
icacls "C:\DATACONGTY\DATAKETOAN" /inheritance:r /grant:r Administrators:(OI)(CI)F /grant:r SYSTEM:(OI)(CI)F /grant:r ketoan:(OI)(CI)F /grant:r nhansu:(OI)(CI)RX /deny nhanvien:(OI)(CI)F >nul

:: DATANHANSU:
:: - nhansu: Toàn quyền (F)
:: - ketoan: Chỉ đọc (RX)
:: - nhanvien: Cấm truy cập (Deny F)
icacls "C:\DATACONGTY\DATANHANSU" /inheritance:r /grant:r Administrators:(OI)(CI)F /grant:r SYSTEM:(OI)(CI)F /grant:r nhansu:(OI)(CI)F /grant:r ketoan:(OI)(CI)RX /deny nhanvien:(OI)(CI)F >nul

echo   -> Đã phân quyền NTFS chi tiết từng thư mục xong!

:: 5. CẤU HÌNH PASSWORD POLICY & ACCOUNT LOCKOUT (CÂU 3)
echo.
echo [5/6] Cấu hình Password Policy & Account Lockout...
net accounts /minpwlen:8 /lockoutthreshold:5 /lockoutduration:5 /lockoutwindow:5 >nul

:: 6. CẤU HÌNH USER RIGHTS ASSIGNMENT (ALLOW/DENY LOGON LOCALLY)
echo.
echo [6/6] Cấu hình User Rights (Allow/Deny Login Locally)...
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
echo        TẤT CẢ CÂU 2 VÀ CÂU 3 ĐÃ ĐƯỢC CẤU HÌNH HOÀN THIỆN 100%%!
echo ===============================================================================
echo.
echo --- KIỂM TRA KẾT QUẢ THƯ MỤC C:\DATACONGTY ---
dir "C:\DATACONGTY"
echo.
pause
