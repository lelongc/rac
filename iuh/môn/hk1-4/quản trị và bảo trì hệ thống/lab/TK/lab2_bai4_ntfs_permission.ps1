# ==============================================================================
# BAI 4: TU DONG CAU HINH NTFS PERMISSION VA SPECIAL PERMISSION
# ==============================================================================

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   BAI 4: CAU HINH NTFS PERMISSION & SPECIAL PERMISSION (TU DONG)" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. Tao cac User KT1, KT2, NS1, NS2 va cac Group KETOAN, NHANSU
$ntfsGroups = @("KETOAN", "NHANSU")
foreach ($g in $ntfsGroups) {
    net localgroup $g 2>$null
    if ($LASTEXITCODE -ne 0) {
        net localgroup $g /add
    }
}

$ntfsUsers = @(
    @{ Name = "KT1"; Password = "abc@123"; Group = "KETOAN" },
    @{ Name = "KT2"; Password = "abc@123"; Group = "KETOAN" },
    @{ Name = "NS1"; Password = "abc@123"; Group = "NHANSU" },
    @{ Name = "NS2"; Password = "abc@123"; Group = "NHANSU" }
)

foreach ($u in $ntfsUsers) {
    net user $u.Name 2>$null
    if ($LASTEXITCODE -eq 0) {
        net user $u.Name $u.Password /active:yes
    } else {
        net user $u.Name $u.Password /add /passwordchg:no
        wmic useraccount where "name='$($u.Name)'" set passwordexpires=false 2>$null | Out-Null
    }
    net localgroup $u.Group $u.Name /add 2>$null
}
Write-Host "[+] Da tao xong cac User KT1, KT2, NS1, NS2 va cac Group KETOAN, NHANSU." -ForegroundColor Green

# 2. Tao cay thu muc C:\DATA
$rootData = "C:\DATA"
$dirChung = "C:\DATA\CHUNG"
$dirKetoan = "C:\DATA\KETOAN"
$dirNhansu = "C:\DATA\NHANSU"

New-Item -Path $rootData -ItemType Directory -Force | Out-Null
New-Item -Path $dirChung  -ItemType Directory -Force | Out-Null
New-Item -Path $dirKetoan -ItemType Directory -Force | Out-Null
New-Item -Path $dirNhansu -ItemType Directory -Force | Out-Null

# Chia se thu muc goc DATA
if (Get-SmbShare -Name "DATA" -ErrorAction SilentlyContinue) {
    Remove-SmbShare -Name "DATA" -Force
}
New-SmbShare -Name "DATA" -Path $rootData -FullAccess "Everyone" | Out-Null
Write-Host "[+] Da chia se thu muc DATA qua mang (\\Server\DATA)" -ForegroundColor Green

# 3. Cau hinh NTFS Permission tren C:\DATA
# Ngat ke thua, xoa quyen nhom Users thuong, cap quyen Read cho KETOAN va NHANSU
Write-Host "[+] Phan quyen tren C:\DATA..." -ForegroundColor Green
icacls "$rootData" /inheritance:d > $null
icacls "$rootData" /remove:g "Users" "BUILTIN\Users" 2>$null > $null
icacls "$rootData" /grant "Administrators:(OI)(CI)F" "SYSTEM:(OI)(CI)F" "KETOAN:(OI)(CI)RX" "NHANSU:(OI)(CI)RX" > $null

# 4. Cau hinh NTFS Permission tren C:\DATA\CHUNG
# Ca 2 nhom KETOAN va NHANSU deu co quyen Full Control
Write-Host "[+] Phan quyen tren C:\DATA\CHUNG (KETOAN & NHANSU Full Control)..." -ForegroundColor Green
icacls "$dirChung" /grant "KETOAN:(OI)(CI)F" "NHANSU:(OI)(CI)F" > $null

# 5. Cau hinh NTFS Permission & Special Permission tren C:\DATA\KETOAN
# Ngat ke thua, xoa quyen NHANSU, cap quyen KETOAN (tru quyen Delete de bao dam chi nguoi tao moi xoa duoc)
Write-Host "[+] Phan quyen tren C:\DATA\KETOAN (Loai bo NHANSU, Special Permission cho KETOAN)..." -ForegroundColor Green
icacls "$dirKetoan" /inheritance:d > $null
icacls "$dirKetoan" /remove "NHANSU" 2>$null > $null
icacls "$dirKetoan" /remove "KETOAN" 2>$null > $null

# Cap quyen cho KETOAN: Doc, Ghi, Sua, Tao file/thu muc nhung BO quyen Delete va Delete Subfolders
icacls "$dirKetoan" /grant:r "KETOAN:(OI)(CI)(RX,WD,AD,WA,WEA,RC)" > $null
# Dam bao CREATOR OWNER co quyen Full Control de chu so huu file van xoa duoc file cua minh
icacls "$dirKetoan" /grant:r "CREATOR OWNER:(OI)(CI)(IO)F" > $null

# 6. Cau hinh NTFS Permission tren C:\DATA\NHANSU
# Ngat ke thua, xoa quyen KETOAN, cap quyen NHANSU Full Control
Write-Host "[+] Phan quyen tren C:\DATA\NHANSU (Loai bo KETOAN, NHANSU Full Control)..." -ForegroundColor Green
icacls "$dirNhansu" /inheritance:d > $null
icacls "$dirNhansu" /remove "KETOAN" 2>$null > $null
icacls "$dirNhansu" /grant "NHANSU:(OI)(CI)F" > $null

# 7. Hien thi bang phan quyen de kiem tra
Write-Host ""
Write-Host "--- KET QUA PHAN QUYEN NTFS (ICACLS) ---" -ForegroundColor Magenta
Write-Host ""
Write-Host "[Quyen tren C:\DATA]:" -ForegroundColor Cyan
icacls "$rootData"
Write-Host ""
Write-Host "[Quyen tren C:\DATA\CHUNG]:" -ForegroundColor Cyan
icacls "$dirChung"
Write-Host ""
Write-Host "[Quyen tren C:\DATA\KETOAN]:" -ForegroundColor Cyan
icacls "$dirKetoan"
Write-Host ""
Write-Host "[Quyen tren C:\DATA\NHANSU]:" -ForegroundColor Cyan
icacls "$dirNhansu"
Write-Host ""
Write-Host "===> HOAN TAT BAI 4 THANH CONG!" -ForegroundColor Green
Write-Host ""
