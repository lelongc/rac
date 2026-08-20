# ==============================================================================
# SCRIPT TỰ ĐỘNG TẠO DOMAIN USER HIEPDH TRÊN ACTIVE DIRECTORY
# ==============================================================================

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "         TAO TAI KHOAN DOMAIN USER (HIEPDH)              " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

Import-Module ActiveDirectory

$userPassword = ConvertTo-SecureString "123" -AsPlainText -Force

# 1. Tạo user hiepdh
$existing = Get-ADUser -Filter "SamAccountName -eq 'hiepdh'" -ErrorAction SilentlyContinue
if (-not $existing) {
    New-ADUser -Name "Hiep Dang" `
               -GivenName "Hiep" `
               -Surname "Dang" `
               -DisplayName "Hiep Dang" `
               -SamAccountName "hiepdh" `
               -UserPrincipalName "hiepdh@newstar.vn" `
               -AccountPassword $userPassword `
               -Enabled $true `
               -PasswordNeverExpires $true `
               -CannotChangePassword $false
    Write-Host "[+] Da tao thanh cong Domain User: hiepdh (Pass: 123)" -ForegroundColor Green
} else {
    Set-ADAccountPassword -Identity "hiepdh" -NewPassword $userPassword -Reset
    Set-ADUser -Identity "hiepdh" -Enabled $true -PasswordNeverExpires $true
    Write-Host "[+] User hiepdh da ton tai, da cap nhat mat khau: 123" -ForegroundColor Green
}

# 2. Tắt độ phức tạp mật khẩu trên Default Domain Policy (để user đặt pass 123 thoải mái)
net accounts /minpwlen:0 /maxpwage:unlimited /minpwage:0 /uniquepw:0
secedit /export /cfg "$env:TEMP\dom_sec.cfg" /quiet
(Get-Content "$env:TEMP\dom_sec.cfg") -replace "PasswordComplexity = 1", "PasswordComplexity = 0" | Set-Content "$env:TEMP\dom_sec.cfg"
secedit /configure /db "$env:TEMP\dom_sec.sdb" /cfg "$env:TEMP\dom_sec.cfg" /quiet
gpupdate /force

Write-Host "[+] Hoan tat tao user va toi uu chinh sach mat khau tren Domain!" -ForegroundColor Green
