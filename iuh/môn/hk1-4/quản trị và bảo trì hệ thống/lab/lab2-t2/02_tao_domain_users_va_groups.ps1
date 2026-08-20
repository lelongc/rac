<#
.SYNOPSIS
    Script tự động tạo tài khoản Domain User và cấu hình quyền hạn trên Domain Controller.
.DESCRIPTION
    - Tạo Organizational Unit (OU) nếu cần.
    - Tạo tài khoản người dùng mẫu 'hiepdh' với mật khẩu '123'.
    - Thiết lập thuộc tính PasswordNeverExpires, CannotChangePassword.
#>

Import-Module ActiveDirectory

Write-Host "==========================================================================" -ForegroundColor Cyan
Write-Host "       TỰ ĐỘNG TẠO TÀI KHOẢN DOMAIN USER TRÊN NEWSTAR.VN                  " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan

$domainName = "newstar.vn"
$defaultPassword = ConvertTo-SecureString "123" -AsPlainText -Force

# 1. Tạo tài khoản mẫu hiepdh
$username = "hiepdh"
$userCheck = Get-ADUser -Filter "SamAccountName -eq '$username'" -ErrorAction SilentlyContinue

if (-not $userCheck) {
    Write-Host "`n[+] Đang tạo tài khoản Domain User: $username..." -ForegroundColor Yellow
    New-ADUser -Name "Hiep Dang" `
               -GivenName "Hiep" `
               -Surname "Dang" `
               -DisplayName "Hiep Dang" `
               -SamAccountName $username `
               -UserPrincipalName "$username@$domainName" `
               -AccountPassword $defaultPassword `
               -Enabled $true `
               -PasswordNeverExpires $true `
               -CannotChangePassword $false `
               -ChangePasswordAtLogon $false
    Write-Host "[+] Tạo tài khoản $username thành công 100%!" -ForegroundColor Green
} else {
    Write-Host "`n[*] Tài khoản $username đã tồn tại. Đang cập nhật trạng thái..." -ForegroundColor Yellow
    Set-ADUser -Identity $username -Enabled $true -PasswordNeverExpires $true
    Set-ADAccountPassword -Identity $username -NewPassword $defaultPassword -Reset
    Write-Host "[+] Cập nhật tài khoản $username thành công!" -ForegroundColor Green
}

# 2. Hiển thị danh sách người dùng trên Domain
Write-Host "`n=== DANH SÁCH DOMAIN USERS ĐANG HOẠT ĐỘNG ===" -ForegroundColor Cyan
Get-ADUser -Filter * -Properties DisplayName, UserPrincipalName, Enabled | Select-Object Name, SamAccountName, UserPrincipalName, Enabled | Format-Table -AutoSize
