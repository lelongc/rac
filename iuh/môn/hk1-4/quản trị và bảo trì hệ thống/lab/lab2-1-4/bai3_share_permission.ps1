# ==============================================================================
# BAI 3: TU DONG CAU HINH SHARE PERMISSION (CHIA SE TAI NGUYEN MANG)
# ==============================================================================

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   BAI 3: CAU HINH SHARE PERMISSION & AN SHARE (TU DONG)" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. Tao cac User U1, U2
$shareUsers = @(
    @{ Name = "U1"; Password = "abc@123"; FullName = "User 1 Share" },
    @{ Name = "U2"; Password = "abc@123"; FullName = "User 2 Share" }
)

foreach ($u in $shareUsers) {
    $existing = net user $u.Name 2>$null
    if ($LASTEXITCODE -eq 0) {
        net user $u.Name $u.Password /active:yes
    } else {
        Write-Host "[+] Dang tao User: $($u.Name)..." -ForegroundColor Green
        net user $u.Name $u.Password /add /fullname:$($u.FullName) /passwordchg:no
        wmic useraccount where "name='$($u.Name)'" set passwordexpires=false 2>$null | Out-Null
    }
}

# 2. Tao cau truc thu muc thuc hanh
$dirDulieu = "C:\THUCHANH\DULIEU"
$dirBimat  = "C:\THUCHANH\BIMAT"
$dirTailieu = "C:\TAILIEU"

New-Item -Path $dirDulieu -ItemType Directory -Force | Out-Null
New-Item -Path $dirBimat  -ItemType Directory -Force | Out-Null
New-Item -Path $dirTailieu -ItemType Directory -Force | Out-Null

# Tao file du lieu mau
Set-Content -Path "$dirDulieu\thuchanh.txt" -Value "Day la tai lieu thuc hanh trong thu muc DULIEU" -Force
Set-Content -Path "$dirBimat\thuchanh.txt"  -Value "Day la tai lieu trong thu muc bi mat BIMAT$" -Force
Set-Content -Path "$dirTailieu\huongdan.txt" -Value "Day la tai lieu map o dia mang Z:" -Force

# 3. Tao cac thu muc chia se (SMB Shares)
# 3.1. Share thuong: DULIEU
if (Get-SmbShare -Name "DULIEU" -ErrorAction SilentlyContinue) {
    Remove-SmbShare -Name "DULIEU" -Force
}
New-SmbShare -Name "DULIEU" -Path $dirDulieu -FullAccess "Everyone" | Out-Null
Write-Host "[+] Da chia se thu muc: DULIEU (\\Server\DULIEU)" -ForegroundColor Green

# 3.2. Share an: BIMAT$
if (Get-SmbShare -Name "BIMAT$" -ErrorAction SilentlyContinue) {
    Remove-SmbShare -Name "BIMAT$" -Force
}
New-SmbShare -Name "BIMAT$" -Path $dirBimat -FullAccess "Everyone" | Out-Null
Write-Host "[+] Da chia se an: BIMAT$ (\\Server\BIMAT$)" -ForegroundColor Green

# 3.3. Share 1 thu muc voi nhieu ten: DULIEU_KETOAN
if (Get-SmbShare -Name "DULIEU_KETOAN" -ErrorAction SilentlyContinue) {
    Remove-SmbShare -Name "DULIEU_KETOAN" -Force
}
New-SmbShare -Name "DULIEU_KETOAN" -Path $dirDulieu -Description "Du lieu phong ke toan" -FullAccess "Everyone" | Out-Null
Write-Host "[+] Da tao ten share thu hai: DULIEU_KETOAN (\\Server\DULIEU_KETOAN)" -ForegroundColor Green

# 3.4. Share thu muc TAILIEU de Map Network Drive
if (Get-SmbShare -Name "TAILIEU" -ErrorAction SilentlyContinue) {
    Remove-SmbShare -Name "TAILIEU" -Force
}
New-SmbShare -Name "TAILIEU" -Path $dirTailieu -FullAccess "Everyone" | Out-Null
Write-Host "[+] Da chia se: TAILIEU de map o dia (\\Server\TAILIEU)" -ForegroundColor Green

# 4. Hien thi danh sach cac Share dang hoat dong
Write-Host ""
Write-Host "--- KET QUA BAI 3: DANH SACH CAC SMB SHARE ---" -ForegroundColor Magenta
Get-SmbShare | Where-Object { $_.Name -in @("DULIEU", "BIMAT$", "DULIEU_KETOAN", "TAILIEU") } | Select-Object Name, Path, Description
Write-Host "===> HOAN TAT BAI 3 THANH CONG!" -ForegroundColor Green
Write-Host ""
