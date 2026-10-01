# ==============================================================================
# SCRIPT KIỂM THỬ VÀ NGHIỆM THU TOÀN DIỆN LAB 7 - TRIỂN KHAI PROFILE
# ==============================================================================

Write-Host "==========================================================================" -ForegroundColor Cyan
Write-Host "         KIEM TRA VA NGHIEM THU TOAN DIEN HE THONG PROFILE LAB 7          " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan

Import-Module ActiveDirectory -ErrorAction SilentlyContinue
Import-Module GroupPolicy -ErrorAction SilentlyContinue
Import-Module FileServerResourceManager -ErrorAction SilentlyContinue

$domain = (Get-ADDomain).DNSRoot
$domainDN = (Get-ADDomain).DistinguishedName
$serverHost = $env:COMPUTERNAME
$score = 0
$totalTests = 10

Write-Host "`n[+] Domain kiem tra: $domain ($domainDN)" -ForegroundColor Green
Write-Host "[+] Server kiem tra: $serverHost" -ForegroundColor Green

# ------------------------------------------------------------------------------
# 1. KIỂM TRA CAC THƯ MỤC CHIA SẺ SMB SHARES (5 SHARES)
# ------------------------------------------------------------------------------
Write-Host "`n1. KIEM TRA CAC SMB SHARES CUA LAB 7:" -ForegroundColor Yellow
$requiredShares = @("home", "Nhansu_Chung", "Nhansu_rieng", "Sep_Roaming", "Direction")
$missingShares = @()

foreach ($sh in $requiredShares) {
    $found = Get-SmbShare -Name $sh -ErrorAction SilentlyContinue
    if (-not $found) { $missingShares += $sh }
}

if ($missingShares.Count -eq 0) {
    Write-Host "  [PASS] 1. Tat ca 5 SMB Shares deu ton tai va dang hoat dong:" -ForegroundColor Green
    foreach ($sh in $requiredShares) {
        $info = Get-SmbShare -Name $sh
        Write-Host "         - \\$serverHost\$sh -> $($info.Path)" -ForegroundColor Cyan
    }
    $score++
} else {
    Write-Host "  [FAIL] 1. Cac share sau chua duoc tao: $($missingShares -join ', ')" -ForegroundColor Red
}

# ------------------------------------------------------------------------------
# 2. KIỂM TRA THUỘC TÍNH HOME FOLDER CỦA USER (Z:)
# ------------------------------------------------------------------------------
Write-Host "`n2. KIEM TRA CAU HINH HOME FOLDER CUA USERS (hiepdh, u1, u2):" -ForegroundColor Yellow
$homeUsers = @("hiepdh", "u1", "u2")
$homeOk = $true

foreach ($u in $homeUsers) {
    $usr = Get-ADUser -Filter "SamAccountName -eq '$u'" -Properties HomeDrive, HomeDirectory -ErrorAction SilentlyContinue
    if (-not $usr -or $usr.HomeDrive -ne "Z:" -or $usr.HomeDirectory -notlike "*\home\*") {
        $homeOk = $false
        Write-Host "  [!] User '$u' chua co HomeDrive Z: hoac sai HomeDirectory!" -ForegroundColor Yellow
    }
}

if ($homeOk) {
    Write-Host "  [PASS] 2. Users (hiepdh, u1, u2) da duoc cau hinh HomeDrive 'Z:' va HomeDirectory hop le." -ForegroundColor Green
    $score++
} else {
    Write-Host "  [FAIL] 2. Cau hinh Home Folder tren User attributes chua day du!" -ForegroundColor Red
}

# ------------------------------------------------------------------------------
# 3. KIỂM TRA THƯ MỤC CON HOME FOLDER TRÊN SERVER (C:\home\...)
# ------------------------------------------------------------------------------
Write-Host "`n3. KIEM TRA THU MUC CON CUA TUNG USER TRONG C:\home:" -ForegroundColor Yellow
$foldersOk = $true
foreach ($u in $homeUsers) {
    if (-not (Test-Path "C:\home\$u")) {
        $foldersOk = $false
    }
}

if ($foldersOk) {
    Write-Host "  [PASS] 3. Cac thu muc rieng cho tung user da duoc tao trong C:\home (hiepdh, u1, u2)." -ForegroundColor Green
    $score++
} else {
    Write-Host "  [FAIL] 3. Thieu thu muc con cho user trong C:\home!" -ForegroundColor Red
}

# ------------------------------------------------------------------------------
# 4. KIỂM TRA CƠ CẤU OU VA TAI KHOAN NGUOI DUNG
# ------------------------------------------------------------------------------
Write-Host "`n4. KIEM TRA CO CAU OU VA TAI KHOAN (OU Nhansu, OU Ke Toan):" -ForegroundColor Yellow
$ouNhansu = Get-ADOrganizationalUnit -Filter "Name -eq 'Nhansu'" -ErrorAction SilentlyContinue
$ouKeToan = Get-ADOrganizationalUnit -Filter "Name -eq 'Ke Toan'" -ErrorAction SilentlyContinue
$uNs1 = Get-ADUser -Filter "SamAccountName -eq 'ns1'" -ErrorAction SilentlyContinue
$uNs2 = Get-ADUser -Filter "SamAccountName -eq 'ns2'" -ErrorAction SilentlyContinue
$u11 = Get-ADUser -Filter "SamAccountName -eq 'u11'" -ErrorAction SilentlyContinue

if ($ouNhansu -and $ouKeToan -and $uNs1 -and $uNs2 -and $u11) {
    Write-Host "  [PASS] 4. Cac OU 'Nhansu', 'Ke Toan' va cac user (ns1, ns2, u11) da san sang hop le." -ForegroundColor Green
    $score++
} else {
    Write-Host "  [FAIL] 4. Thieu OU hoac tai khoan nguoi dung can thiet!" -ForegroundColor Red
}

# ------------------------------------------------------------------------------
# 5. KIỂM TRA FSRM QUOTA CHO PHÒNG NHÂN SỰ
# ------------------------------------------------------------------------------
Write-Host "`n5. KIEM TRA FSRM QUOTA CHO C:\Nhansu_Chung (1GB) VA C:\Nhansu_rieng (500MB):" -ForegroundColor Yellow
$qChung = Get-FsrmQuota -Path "C:\Nhansu_Chung" -ErrorAction SilentlyContinue
$qRieng = Get-FsrmQuota -Path "C:\Nhansu_rieng" -ErrorAction SilentlyContinue

$quotaChungOk = $qChung -and ($qChung.Size -eq 1GB -or $qChung.Size -eq 1073741824)
$quotaRiengOk = $qRieng -and ($qRieng.Size -eq 500MB -or $qRieng.Size -eq 524288000)

if ($quotaChungOk -and $quotaRiengOk) {
    Write-Host "  [PASS] 5. FSRM Quota da duoc thiet lap chinh xac:" -ForegroundColor Green
    Write-Host "         - C:\Nhansu_Chung : $([math]::Round($qChung.Size / 1GB, 1)) GB (Hard Limit)" -ForegroundColor Cyan
    Write-Host "         - C:\Nhansu_rieng : $([math]::Round($qRieng.Size / 1MB, 0)) MB (Hard Limit)" -ForegroundColor Cyan
    $score++
} else {
    Write-Host "  [FAIL] 5. Quota chua duoc thiet lap dung dung luong yeu cau (1GB va 500MB)!" -ForegroundColor Red
}

# ------------------------------------------------------------------------------
# 6. KIỂM TRA GPO 'Profile nhansu' VA LIÊN KẾT
# ------------------------------------------------------------------------------
Write-Host "`n6. KIEM TRA GPO 'Profile nhansu' VA LIEN KET OU Nhansu:" -ForegroundColor Yellow
$gpoNhansu = Get-GPO -Name "Profile nhansu" -ErrorAction SilentlyContinue
$nhansuLinks = (Get-GPInheritance -Target "OU=Nhansu,$domainDN" -ErrorAction SilentlyContinue).GpoLinks
$linkNhansu = $nhansuLinks | Where-Object { $_.DisplayName -eq "Profile nhansu" -and $_.Enabled }

if ($gpoNhansu -and $linkNhansu) {
    Write-Host "  [PASS] 6. GPO 'Profile nhansu' ton tai, dang Enabled va da duoc link vao OU Nhansu." -ForegroundColor Green
    $score++
} else {
    Write-Host "  [FAIL] 6. GPO 'Profile nhansu' chua duoc tao hoac chua duoc link vao OU Nhansu!" -ForegroundColor Red
}

# ------------------------------------------------------------------------------
# 7. KIỂM TRA LOGON SCRIPT profile.bat TRONG SYSVOL
# ------------------------------------------------------------------------------
Write-Host "`n7. KIEM TRA KICH BAN DANG NHAP (profile.bat) TRONG SYSVOL:" -ForegroundColor Yellow
if ($gpoNhansu) {
    $guid1 = $gpoNhansu.Id.ToString("B").ToUpper()
    $batPath = "C:\Windows\SYSVOL\sysvol\$domain\Policies\$guid1\User\Scripts\Logon\profile.bat"
    if (Test-Path $batPath) {
        $content = Get-Content $batPath -Raw
        if ($content -match "net use m:" -and $content -match "net use n:") {
            Write-Host "  [PASS] 7. Tep kịch ban profile.bat ton tai va chua day du lenh map M: va N:" -ForegroundColor Green
            Write-Host "         -> Noi dung:`n$content" -ForegroundColor Cyan
            $score++
        } else {
            Write-Host "  [FAIL] 7. profile.bat thieu lenh map o dia M: hoac N:!" -ForegroundColor Red
        }
    } else {
        Write-Host "  [FAIL] 7. Khong tim thay tep profile.bat trong SYSVOL cua GPO!" -ForegroundColor Red
    }
} else {
    Write-Host "  [FAIL] 7. Khong tim thay GPO Profile nhansu!" -ForegroundColor Red
}

# ------------------------------------------------------------------------------
# 8. KIỂM TRA ROAMING PROFILE CHO TÀI KHOẢN 'sep'
# ------------------------------------------------------------------------------
Write-Host "`n8. KIEM TRA ROAMING PROFILE CUA TAI KHOAN 'sep':" -ForegroundColor Yellow
$sepUsr = Get-ADUser -Filter "SamAccountName -eq 'sep'" -Properties ProfilePath -ErrorAction SilentlyContinue
if ($sepUsr -and $sepUsr.ProfilePath -like "*\Sep_Roaming\*") {
    Write-Host "  [PASS] 8. Tai khoan 'sep' da duoc thiet lap Roaming ProfilePath:" -ForegroundColor Green
    Write-Host "         -> ProfilePath: $($sepUsr.ProfilePath)" -ForegroundColor Cyan
    $score++
} else {
    Write-Host "  [FAIL] 8. Tai khoan 'sep' chua duoc thiet lap ProfilePath den \\$serverHost\Sep_Roaming!" -ForegroundColor Red
}

# ------------------------------------------------------------------------------
# 9. KIỂM TRA GPO 'Folder Redirection' VA LIÊN KẾT OU Ke Toan
# ------------------------------------------------------------------------------
Write-Host "`n9. KIEM TRA GPO 'Folder Redirection' VA LIEN KET OU Ke Toan:" -ForegroundColor Yellow
$gpoRedir = Get-GPO -Name "Folder Redirection" -ErrorAction SilentlyContinue
$ouKTLinks = (Get-GPInheritance -Target "OU=Ke Toan,$domainDN" -ErrorAction SilentlyContinue).GpoLinks
$linkRedir = $ouKTLinks | Where-Object { $_.DisplayName -eq "Folder Redirection" -and $_.Enabled }

if ($gpoRedir -and $linkRedir) {
    Write-Host "  [PASS] 9. GPO 'Folder Redirection' ton tai, dang Enabled va da duoc link vao OU Ke Toan." -ForegroundColor Green
    $score++
} else {
    Write-Host "  [FAIL] 9. GPO 'Folder Redirection' chua duoc tao hoac chua duoc link vao OU Ke Toan!" -ForegroundColor Red
}

# ------------------------------------------------------------------------------
# 10. KIỂM TRA CẤU HÌNH REDIRECTION CHO THƯ MỤC DOCUMENTS
# ------------------------------------------------------------------------------
Write-Host "`n10. KIEM TRA THIET LAP REDIRECTION CHO MY DOCUMENTS:" -ForegroundColor Yellow
$redirConfigOk = $false
if ($gpoRedir) {
    $guid2 = $gpoRedir.Id.ToString("B").ToUpper()
    $fdeploy1 = "C:\Windows\SYSVOL\sysvol\$domain\Policies\$guid2\User\Documents & Settings\fdeploy1.ini"
    $fdeploy0 = "C:\Windows\SYSVOL\sysvol\$domain\Policies\$guid2\User\Documents & Settings\fdeploy.ini"
    $regRedir = Get-GPRegistryValue -Name "Folder Redirection" -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" -ErrorAction SilentlyContinue
    $personalVal = $regRedir | Where-Object { $_.ValueName -eq "Personal" -and $_.Value -like "*\Direction\*" }
    
    if ((Test-Path $fdeploy1) -or (Test-Path $fdeploy0) -or $personalVal) {
        $redirConfigOk = $true
    }
}

if ($redirConfigOk) {
    Write-Host "  [PASS] 10. Chinh sach Folder Redirection cho My Documents da duoc cau hinh hop le tro ve \\$serverHost\Direction." -ForegroundColor Green
    $score++
} else {
    Write-Host "  [FAIL] 10. Chua tim thay cau hinh chuyen huong thu muc Documents!" -ForegroundColor Red
}

# ------------------------------------------------------------------------------
# TỔNG KẾT VÀ TỶ LỆ ĐẠT
# ------------------------------------------------------------------------------
Write-Host "`n==========================================================================" -ForegroundColor Cyan
$percent = [math]::Round(($score / $totalTests) * 100, 1)
$color = if ($score -eq $totalTests) { "Green" } else { "Yellow" }
Write-Host "   KET QUA DANH GIA NGHIEM THU LAB 7: $score / $totalTests TIEU CHI DAT ($percent%)" -ForegroundColor $color
Write-Host "==========================================================================" -ForegroundColor Cyan

if ($score -eq $totalTests) {
    Write-Host "[PASS] CHUC MUNG! HE THONG LAB 7 PROFILE DA DAT 100% TAT CA CAC TIEU CHI DE BAI!" -ForegroundColor Green
} else {
    Write-Host "[!] MOT SO TIEU CHI CHUA HOAN TAT, HAY KIEM TRA LAI CAC MUC [FAIL]." -ForegroundColor Red
}
