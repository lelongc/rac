<#
.SYNOPSIS
    Script tự động cài đặt AD DS và nâng cấp Server thành Domain Controller (DC).
.DESCRIPTION
    - Cấu hình IP tĩnh và DNS cho card mạng Server.
    - Cài đặt tính năng Active Directory Domain Services và công cụ quản trị RSAT.
    - Khởi tạo Forest mới với tên miền newstar.vn.
#>

Write-Host "==========================================================================" -ForegroundColor Cyan
Write-Host "     TỰ ĐỘNG CÀI ĐẶT AD DS VÀ NÂNG CẤP DOMAIN CONTROLLER (NEWSTAR.VN)    " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan

# 1. Cài đặt AD DS và công cụ quản lý
Write-Host "`n[1/3] Đang cài đặt Active Directory Domain Services..." -ForegroundColor Yellow
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

# 2. Tạo mật khẩu DSRM (Directory Services Restore Mode)
$dsrmPassword = ConvertTo-SecureString "123" -AsPlainText -Force

# 3. Nâng cấp thành Domain Controller với Forest mới: newstar.vn
Write-Host "`n[2/3] Đang nâng cấp Server lên Domain Controller (newstar.vn)..." -ForegroundColor Yellow
Write-Host "Máy chủ sẽ tự động khởi động lại sau khi hoàn tất cài đặt." -ForegroundColor Cyan

Install-ADDSForest -DomainName "newstar.vn" `
                   -DomainNetbiosName "NEWSTAR" `
                   -DomainMode "Win2012R2" `
                   -ForestMode "Win2012R2" `
                   -InstallDns:$true `
                   -SafeModeAdministratorPassword $dsrmPassword `
                   -Force:$true
