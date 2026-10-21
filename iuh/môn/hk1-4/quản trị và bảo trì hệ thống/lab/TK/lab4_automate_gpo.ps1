# ==============================================================================
# SCRIPT TỰ ĐỘNG HÓA CẤU HÌNH BÀI LAB 4 - QUẢN TRỊ BẢO MẬT ADDS VÀ PASSWORD POLICY
# Áp dụng cho: Windows Server 2012 DC (Domain: newstar.vn)
# ==============================================================================

Write-Host "==========================================================================" -ForegroundColor Cyan
Write-Host "       BAT DAU TU DONG HOA CAU HINH LAB 4 (GPO & PASSWORD POLICY)         " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan

# 1. KIỂM TRA VÀ TẠO TÀI KHOẢN NGƯỜI DÙNG TEST u1
Write-Host "`n1. KHOI TAO TAI KHOAN USER TEST u1:" -ForegroundColor Yellow
try {
    Import-Module ActiveDirectory -ErrorAction Stop
    $domainName = (Get-ADDomain).DNSRoot
    Write-Host "  [+] Ten mien hien tai: $domainName" -ForegroundColor Green

    $user = Get-ADUser -Filter "SamAccountName -eq 'u1'" -ErrorAction SilentlyContinue
    if (-not $user) {
        $initPassword = ConvertTo-SecureString "P@ssword123!" -AsPlainText -Force
        New-ADUser -Name "User u1" `
                   -SamAccountName "u1" `
                   -UserPrincipalName "u1@$domainName" `
                   -AccountPassword $initPassword `
                   -Enabled $true `
                   -PasswordNeverExpires $false `
                   -ChangePasswordAtLogon $false
        Write-Host "  [+] Da tao moi thanh cong user 'u1' voi mat khau ban dau: P@ssword123!" -ForegroundColor Green
    } else {
        Set-ADAccountPassword -Identity "u1" -NewPassword (ConvertTo-SecureString "P@ssword123!" -AsPlainText -Force) -Reset
        Set-ADUser -Identity "u1" -Enabled $true -PasswordNeverExpires $false -ChangePasswordAtLogon $false
        Write-Host "  [+] User 'u1' da ton tai. Da reset mat khau ve: P@ssword123!" -ForegroundColor Green
    }
} catch {
    Write-Host "  [-] Loi xu ly Active Directory User: $_" -ForegroundColor Red
}

# 2. CẤU HÌNH CHÍNH SÁCH MẬT KHẨU TOÀN MIỀN (DEFAULT DOMAIN PASSWORD POLICY)
Write-Host "`n2. THIET LAP CHINH SACH MAT KHAU (PASSWORD POLICY) TRONG DOMAIN:" -ForegroundColor Yellow
try {
    # Yêu cầu đề bài:
    # - Lưu lịch sử: 2 mật khẩu
    # - Tuổi thọ tối đa (Max Age): 10 ngày
    # - Tuổi thọ tối thiểu (Min Age): 1 ngày
    # - Độ dài tối thiểu: 7 ký tự
    # - Bắt buộc độ phức tạp: Enabled
    Set-ADDefaultDomainPasswordPolicy -Identity $domainName `
        -ComplexityEnabled $true `
        -MinPasswordLength 7 `
        -PasswordHistoryCount 2 `
        -MaxPasswordAge (New-TimeSpan -Days 10) `
        -MinPasswordAge (New-TimeSpan -Days 1) `
        -LockoutDuration (New-TimeSpan -Minutes 30) `
        -LockoutObservationWindow (New-TimeSpan -Minutes 30) `
        -LockoutThreshold 5 `
        -ErrorAction Stop

    Write-Host "  [+] Da cap nhat Default Domain Password Policy thanh cong:" -ForegroundColor Green
    $policy = Get-ADDefaultDomainPasswordPolicy
    Write-Host "      - Enforce password history        : $($policy.PasswordHistoryCount) passwords remembered" -ForegroundColor Cyan
    Write-Host "      - Maximum password age            : $($policy.MaxPasswordAge.Days) days" -ForegroundColor Cyan
    Write-Host "      - Minimum password age            : $($policy.MinPasswordAge.Days) days" -ForegroundColor Cyan
    Write-Host "      - Minimum password length         : $($policy.MinPasswordLength) characters" -ForegroundColor Cyan
    Write-Host "      - Password complexity enabled     : $($policy.ComplexityEnabled)" -ForegroundColor Cyan
    # Cấu hình riêng cho Administrator (PSO - Fine-Grained Password Policy):
    # Cho phép Administrator dùng mật khẩu ngắn "123", không bắt buộc độ phức tạp, không hết hạn
    $existingPSO = Get-ADFineGrainedPasswordPolicy -Filter "Name -eq 'AdminPasswordPolicy'" -ErrorAction SilentlyContinue
    if (-not $existingPSO) {
        New-ADFineGrainedPasswordPolicy -Name "AdminPasswordPolicy" `
            -Precedence 1 `
            -ComplexityEnabled $false `
            -LockoutThreshold 0 `
            -MaxPasswordAge ([TimeSpan]::Zero) `
            -MinPasswordAge ([TimeSpan]::Zero) `
            -MinPasswordLength 1 `
            -PasswordHistoryCount 0 `
            -ErrorAction SilentlyContinue
        Add-ADFineGrainedPasswordPolicySubject -Identity "AdminPasswordPolicy" -Subjects "Administrator" -ErrorAction SilentlyContinue
    }
    Set-ADUser -Identity "Administrator" -PasswordNeverExpires $true -CannotChangePassword $false -ChangePasswordAtLogon $false -ErrorAction SilentlyContinue
    Set-ADAccountPassword -Identity "Administrator" -NewPassword (ConvertTo-SecureString "123" -AsPlainText -Force) -Reset -ErrorAction SilentlyContinue
    Write-Host "      - Dac quyen rieng cho Administrator: Mat khau 123 khong bao gio het han" -ForegroundColor Magenta
} catch {
    Write-Host "  [-] Loi thiet lap Password Policy: $_" -ForegroundColor Red
}

# 3. CẤU HÌNH QUYỀN ĐĂNG NHẬP LOCAL TRÊN DC (ALLOW LOG ON LOCALLY)
Write-Host "`n3. PHAN QUYEN DANG NHAP LOCAL TREN DOMAIN CONTROLLER (SeInteractiveLogonRight):" -ForegroundColor Yellow
try {
    # Xuất cấu hình security hiện tại bằng secedit
    $tempCfg = "$env:TEMP\sec_current.inf"
    $tempSdb = "$env:TEMP\sec_current.sdb"
    if (Test-Path $tempCfg) { Remove-Item $tempCfg -Force }
    if (Test-Path $tempSdb) { Remove-Item $tempSdb -Force }

    secedit /export /cfg $tempCfg /areas USER_RIGHTS | Out-Null

    if (Test-Path $tempCfg) {
        $content = Get-Content $tempCfg
        $foundRight = $false
        $newContent = @()

        foreach ($line in $content) {
            if ($line -match "^SeInteractiveLogonRight\s*=\s*(.*)") {
                $foundRight = $true
                $currentSIDs = $matches[1].Trim()
                # *S-1-5-32-545 là SID chuẩn của BUILTIN\Users
                # Thêm *S-1-5-32-545 và u1 nếu chưa có
                $items = $currentSIDs.Split(',') | ForEach-Object { $_.Trim() }
                if ($items -notcontains "*S-1-5-32-545") { $items += "*S-1-5-32-545" }
                if ($items -notcontains "u1") { $items += "u1" }
                $newLine = "SeInteractiveLogonRight = " + ($items -join ",")
                $newContent += $newLine
                Write-Host "  [+] Cap nhat SeInteractiveLogonRight kem nhóm Users va user u1" -ForegroundColor Green
            } else {
                $newContent += $line
            }
        }

        if (-not $foundRight) {
            # Nếu chưa có thì thêm vào section [Privilege Rights]
            $newContent = @()
            $inPriv = $false
            foreach ($line in $content) {
                $newContent += $line
                if ($line -match "\[Privilege Rights\]") {
                    $newContent += "SeInteractiveLogonRight = *S-1-5-32-544,*S-1-5-32-545,u1"
                }
            }
        }

        Set-Content -Path $tempCfg -Value $newContent -Encoding Ascii

        # Áp dụng cấu hình quyền vào local policy của DC
        secedit /configure /db $tempSdb /cfg $tempCfg /areas USER_RIGHTS | Out-Null
        Write-Host "  [+] Da ap dung quyen Allow log on locally vao he thong thanh cong!" -ForegroundColor Green
    }
} catch {
    Write-Host "  [-] Loi phan quyen Allow log on locally: $_" -ForegroundColor Red
}

# 4. ĐỒNG BỘ GROUP POLICY TỨC THÌ
Write-Host "`n4. DONG BO GROUP POLICY (gpupdate /force):" -ForegroundColor Yellow
$gpResult = gpupdate /force
Write-Host "  [+] Ket qua dong bo Group Policy:" -ForegroundColor Green
$gpResult | ForEach-Object { Write-Host "      $_" -ForegroundColor Gray }

Write-Host "`n==========================================================================" -ForegroundColor Cyan
Write-Host "           HOAN TAT 100% CAU HINH LAB 4 - SAN SANG KIEM THU!              " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan
