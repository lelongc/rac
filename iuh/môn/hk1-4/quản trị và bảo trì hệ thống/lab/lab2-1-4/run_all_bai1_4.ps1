# ==============================================================================
# SCRIPT TỰ ĐỘNG CHẠY TOÀN BỘ TỪ BÀI 1 ĐẾN BÀI 4 TRÊN WINDOWS SERVER (192.168.1.132)
# ==============================================================================

param(
    [string]$ServerIP = "192.168.1.132",
    [string]$Username = "Administrator",
    [string]$Password = "Longko0!"
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "==========================================================" -ForegroundColor Green
Write-Host "  BẮT ĐẦU CHẠY TỰ ĐỘNG BÀI LAB 1 ĐẾN 4 TRÊN WINDOWS SERVER" -ForegroundColor Green
Write-Host "  Target IP : $ServerIP" -ForegroundColor Green
Write-Host "  User      : $Username" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Green

$secPass = ConvertTo-SecureString $Password -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential($Username, $secPass)

# 1. Chạy Bài 1
Write-Host "`n>>> [1/4] DANG THUC THI BAI 1: LOCAL USER & GROUP..." -ForegroundColor Yellow
Invoke-Command -ComputerName $ServerIP -Credential $cred -FilePath "$scriptDir\bai1_local_user_group.ps1"

# 2. Chạy Bài 2
Write-Host "`n>>> [2/4] DANG THUC THI BAI 2: LOCAL SECURITY POLICY..." -ForegroundColor Yellow
Invoke-Command -ComputerName $ServerIP -Credential $cred -FilePath "$scriptDir\bai2_local_security_policy.ps1"

# 3. Chạy Bài 3
Write-Host "`n>>> [3/4] DANG THUC THI BAI 3: SHARE PERMISSION..." -ForegroundColor Yellow
Invoke-Command -ComputerName $ServerIP -Credential $cred -FilePath "$scriptDir\bai3_share_permission.ps1"

# 4. Chạy Bài 4
Write-Host "`n>>> [4/4] DANG THUC THI BAI 4: NTFS PERMISSION..." -ForegroundColor Yellow
Invoke-Command -ComputerName $ServerIP -Credential $cred -FilePath "$scriptDir\bai4_ntfs_permission.ps1"

Write-Host "`n==========================================================" -ForegroundColor Green
Write-Host "  DA HOAN THANH CAU HINH TU DONG BAI 1 DEN BAI 4 100%!" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Green
