# ==============================================================================
# SCRIPT TỰ ĐỘNG CÀI ĐẶT AD DS VÀ NÂNG CẤP DOMAIN CONTROLLER (NEWSTAR.VN)
# ==============================================================================

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   BAT DAU CAI DAT AD DS & NANG CAP DOMAIN CONTROLLER    " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. Cài đặt Role AD DS và các công cụ quản trị RSAT
Write-Host "`n[1/3] Dang cai dat Role AD-Domain-Services..." -ForegroundColor Yellow
Install-WindowsFeature -Name "AD-Domain-Services" -IncludeManagementTools

# 2. Cài đặt Forest mới: newstar.vn
Write-Host "`n[2/3] Dang cau hinh nang cap Forest moi: newstar.vn..." -ForegroundColor Yellow
Import-Module ADDSDeployment

$dsrmPassword = ConvertTo-SecureString "123" -AsPlainText -Force

Install-ADDSForest `
    -CreateDnsDelegation:$false `
    -DatabasePath "C:\Windows\NTDS" `
    -DomainMode "WinThreshold" `
    -DomainName "newstar.vn" `
    -DomainNetbiosName "NEWSTAR" `
    -ForestMode "WinThreshold" `
    -InstallDns:$true `
    -LogPath "C:\Windows\NTDS" `
    -NoRebootOnCompletion:$false `
    -SysvolPath "C:\Windows\SYSVOL" `
    -SafeModeAdministratorPassword $dsrmPassword `
    -Force:$true

Write-Host "`n[3/3] NANG CAP DOMAIN HOAN TAT! MAY SE TU DONG KHOI DONG LAI..." -ForegroundColor Green
