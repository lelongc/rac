# ==============================================================================
# BAI 2: TU DONG CAU HINH LOCAL SECURITY POLICY (CHINH SACH BAO MAT CUC BO)
# ==============================================================================

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   BAI 2: CAU HINH LOCAL SECURITY POLICY (TU DONG)" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

$cfgPath = "$env:TEMP\local_sec.cfg"
$sdbPath = "$env:TEMP\local_sec.sdb"

# 1. Export chinh sach bao mat hien tai
secedit /export /cfg $cfgPath /quiet

# 2. Doc file va sua cac gia tri Password & Lockout Policy
$content = Get-Content -Path $cfgPath

# Thay the PasswordComplexity = 0
$content = $content -replace "PasswordComplexity\s*=\s*\d+", "PasswordComplexity = 0"
$content = $content -replace "MinimumPasswordLength\s*=\s*\d+", "MinimumPasswordLength = 0"
$content = $content -replace "PasswordHistorySize\s*=\s*\d+", "PasswordHistorySize = 0"
$content = $content -replace "MaximumPasswordAge\s*=\s*\d+", "MaximumPasswordAge = 0"
$content = $content -replace "MinimumPasswordAge\s*=\s*\d+", "MinimumPasswordAge = 0"
$content = $content -replace "LockoutBadCount\s*=\s*\d+", "LockoutBadCount = 3"
$content = $content -replace "ResetLockoutCount\s*=\s*\d+", "ResetLockoutCount = 30"
$content = $content -replace "LockoutDuration\s*=\s*\d+", "LockoutDuration = 30"

# User Rights Assignment
if ($content -notmatch "SeSystemtimePrivilege") {
    $content += "`nSeSystemtimePrivilege = *S-1-5-32-544,*S-1-5-32-545"
} else {
    $content = $content -replace "SeSystemtimePrivilege\s*=.*", "SeSystemtimePrivilege = *S-1-5-32-544,*S-1-5-32-545"
}

if ($content -notmatch "SeShutdownPrivilege") {
    $content += "`nSeShutdownPrivilege = *S-1-5-32-544,*S-1-5-32-545"
} else {
    $content = $content -replace "SeShutdownPrivilege\s*=.*", "SeShutdownPrivilege = *S-1-5-32-544,*S-1-5-32-545"
}

Set-Content -Path $cfgPath -Value $content -Encoding Unicode

# 3. Apply chinh sach lai vao he thong
Write-Host "[+] Dang nap lai Security Policy bang SecEdit..." -ForegroundColor Green
secedit /configure /db $sdbPath /cfg $cfgPath /areas SECURITYPOLICY USER_RIGHTS /quiet

net accounts /minpwlen:0 /maxpwage:unlimited /minpwage:0 /uniquepw:0 /lockoutthreshold:3 /lockoutduration:30 /lockoutwindow:30 > $null
gpupdate /force > $null

# 4. Tao User U4 voi mat khau don gian '123'
Write-Host "[+] Tao User U4 voi mat khau don gian '123'..." -ForegroundColor Green
$existingU4 = net user U4 2>$null
if ($LASTEXITCODE -eq 0) {
    net user U4 123 /active:yes
} else {
    net user U4 123 /add /fullname:"User 4 Kiem Tra Policy" /passwordchg:no
    wmic useraccount where "name='U4'" set passwordexpires=false 2>$null | Out-Null
}

Write-Host ""
Write-Host "--- KET QUA BAI 2 ---" -ForegroundColor Magenta
Write-Host "[Thong so Net Accounts hien tai]:" -ForegroundColor Cyan
net accounts
Write-Host ""
Write-Host "[Tai khoan kiem chung U4]:" -ForegroundColor Cyan
net user U4 | Select-String "User name|Full Name|Account active|Password last set|Password expires"
Write-Host "===> HOAN TAT BAI 2 THANH CONG!" -ForegroundColor Green
Write-Host ""
