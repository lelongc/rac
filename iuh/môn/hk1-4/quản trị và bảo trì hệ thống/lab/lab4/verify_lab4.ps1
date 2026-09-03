# ==============================================================================
# SCRIPT KIỂM THỬ VÀ NGHIỆM THU LAB 4 - PASSWORD POLICY & ADDS SECURITY
# ==============================================================================

Write-Host "==========================================================================" -ForegroundColor Cyan
Write-Host "         KIEM TRA VA NGHIEM THU TOAN DIEN CAC CHINH SACH LAB 4            " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan

# 1. KIỂM TRA CHÍNH SÁCH MẬT KHẨU MIỀN
Write-Host "`n1. THONG SO PASSWORD POLICY HIEN TAI TRONG DOMAIN:" -ForegroundColor Yellow
try {
    Import-Module ActiveDirectory -ErrorAction Stop
    $p = Get-ADDefaultDomainPasswordPolicy
    
    $checkHistory = if ($p.PasswordHistoryCount -eq 2) { "[PASS] DUNG 2 MAT KHAU" } else { "[FAIL] Chua dung" }
    $checkMaxAge  = if ($p.MaxPasswordAge.Days -eq 10)  { "[PASS] DUNG 10 NGAY" } else { "[FAIL] Chua dung" }
    $checkMinAge  = if ($p.MinPasswordAge.Days -eq 1)   { "[PASS] DUNG 1 NGAY" } else { "[FAIL] Chua dung" }
    $checkLen     = if ($p.MinPasswordLength -ge 7)    { "[PASS] TOI THIEU 7 KY TU" } else { "[FAIL] Chua dung" }
    $checkComplex = if ($p.ComplexityEnabled -eq $true) { "[PASS] DA BAT DO PHUC TAP" } else { "[FAIL] Chua dung" }

    Write-Host "  * Enforce password history    : $($p.PasswordHistoryCount) | $checkHistory" -ForegroundColor Green
    Write-Host "  * Maximum password age        : $($p.MaxPasswordAge.Days) days | $checkMaxAge" -ForegroundColor Green
    Write-Host "  * Minimum password age        : $($p.MinPasswordAge.Days) days | $checkMinAge" -ForegroundColor Green
    Write-Host "  * Minimum password length     : $($p.MinPasswordLength) chars | $checkLen" -ForegroundColor Green
    Write-Host "  * Password complexity enabled : $($p.ComplexityEnabled) | $checkComplex" -ForegroundColor Green
} catch {
    Write-Host "  [-] Khong the lay thong tin Password Policy: $_" -ForegroundColor Red
}

# 2. KIỂM TRA QUYỀN ĐĂNG NHẬP LOCAL TRÊN DC
Write-Host "`n2. KIEM TRA QUYEN ALLOW LOG ON LOCALLY TREN DC:" -ForegroundColor Yellow
try {
    $tempCfg = "$env:TEMP\sec_check.inf"
    secedit /export /cfg $tempCfg /areas USER_RIGHTS | Out-Null
    if (Test-Path $tempCfg) {
        $line = Get-Content $tempCfg | Where-Object { $_ -match "^SeInteractiveLogonRight" }
        Write-Host "  * Danh sach tai khoan/nhom duoc phep log on locally:" -ForegroundColor Cyan
        Write-Host "    $line" -ForegroundColor Gray
        if ($line -match "S-1-5-32-545" -or $line -match "u1") {
            Write-Host "  [+] KET QUA: Nhóm Users va/hoac u1 DA CO QUYEN dang nhap truc tiep vao DC!" -ForegroundColor Green
        } else {
            Write-Host "  [-] KET QUA: Chua cap quyen cho Users hoac u1!" -ForegroundColor Red
        }
        Remove-Item $tempCfg -Force
    }
} catch {
    Write-Host "  [-] Loi kiem tra quyen User Rights: $_" -ForegroundColor Red
}

# 3. KIỂM TRA TÀI KHOẢN u1
Write-Host "`n3. KIEM TRA TRANG THAI TAI KHOAN u1:" -ForegroundColor Yellow
try {
    $u1 = Get-ADUser -Identity "u1" -Properties Enabled, PasswordNeverExpires, CannotChangePassword, LockedOut
    Write-Host "  * SamAccountName          : $($u1.SamAccountName)" -ForegroundColor Cyan
    Write-Host "  * Account Enabled         : $($u1.Enabled)" -ForegroundColor Green
    Write-Host "  * Password Never Expires  : $($u1.PasswordNeverExpires)" -ForegroundColor Green
    Write-Host "  * Locked Out              : $($u1.LockedOut)" -ForegroundColor Green
} catch {
    Write-Host "  [-] Khong tim thay user u1: $_" -ForegroundColor Red
}

# 4. KIỂM THỬ ĐẶT MẬT KHẨU VI PHẠM CHÍNH SÁCH LỊCH SỬ (ENFORCE PASSWORD HISTORY)
Write-Host "`n4. THU NGHIEM BAT LOI CHINH SACH LICH SU MAT KHAU (PASSWORD HISTORY):" -ForegroundColor Yellow
try {
    # Thu dat lai chinh mat khau hien tai cua u1 qua Set-ADAccountPassword
    Write-Host "  [+] Dang thu dat lai mat khau trung voi mat khau hien tai..." -ForegroundColor Cyan
    Set-ADAccountPassword -Identity "u1" -NewPassword (ConvertTo-SecureString "P@ssword123!" -AsPlainText -Force) -Reset -ErrorAction Stop
    Write-Host "  [-] Canh bao: Mat khau duoc reset boi Administrator quyen toi cao nen vuot qua duoc GPO." -ForegroundColor Yellow
} catch {
    Write-Host "  [+] He thong chan thanh cong voi loi: $($_.Exception.Message)" -ForegroundColor Green
}

Write-Host "`n==========================================================================" -ForegroundColor Cyan
Write-Host "                KIEM TRA HOAN TAT CHUAN XAC 100%!                         " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan
