# ==============================================================================
# BAI 1: TU DONG TAO LOCAL USER ACCOUNT & GROUP ACCOUNT
# ==============================================================================

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   BAI 1: TAO LOCAL USER VA LOCAL GROUP (TU DONG)" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. Tao cac tai khoan User
$users = @(
    @{ Name = "SV1"; FullName = "Nguyen Van Nam"; Description = "Lop Truong"; Password = "abc@123" },
    @{ Name = "SV2"; FullName = "Sinh Vien 2"; Description = "Thanh Vien"; Password = "abc@123" },
    @{ Name = "SV3"; FullName = "Sinh Vien 3"; Description = "Thanh Vien"; Password = "abc@123" },
    @{ Name = "GV1"; FullName = "Giao Vien 1"; Description = "Giang Vien"; Password = "abc@123" },
    @{ Name = "GV2"; FullName = "Giao Vien 2"; Description = "Giang Vien"; Password = "abc@123" }
)

foreach ($u in $users) {
    $existing = net user $u.Name 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[+] User $($u.Name) da ton tai. Cap nhat mat khau..." -ForegroundColor Yellow
        net user $u.Name $u.Password /active:yes
    } else {
        Write-Host "[+] Dang tao User: $($u.Name) ($($u.FullName))..." -ForegroundColor Green
        net user $u.Name $u.Password /add /fullname:$($u.FullName) /comment:$($u.Description) /passwordchg:no
        wmic useraccount where "name='$($u.Name)'" set passwordexpires=false 2>$null | Out-Null
    }
}

# 2. Tao cac Local Group
$groups = @("SINHVIEN", "GIAOVIEN")
foreach ($g in $groups) {
    $existingGroup = net localgroup $g 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[+] Dang tao Group: $g..." -ForegroundColor Green
        net localgroup $g /add
    } else {
        Write-Host "[+] Group $g da ton tai." -ForegroundColor Yellow
    }
}

# 3. Them User vao Group tuong ung
Write-Host "[+] Them SV1, SV2, SV3 vao Group SINHVIEN..." -ForegroundColor Green
net localgroup SINHVIEN SV1 /add 2>$null
net localgroup SINHVIEN SV2 /add 2>$null
net localgroup SINHVIEN SV3 /add 2>$null

Write-Host "[+] Them GV1, GV2 vao Group GIAOVIEN..." -ForegroundColor Green
net localgroup GIAOVIEN GV1 /add 2>$null
net localgroup GIAOVIEN GV2 /add 2>$null

# 4. Hien thi ket qua kiem tra
Write-Host ""
Write-Host "--- KET QUA BAI 1 ---" -ForegroundColor Magenta
Write-Host "[Thanh vien Group SINHVIEN]:" -ForegroundColor Cyan
net localgroup SINHVIEN
Write-Host "[Thanh vien Group GIAOVIEN]:" -ForegroundColor Cyan
net localgroup GIAOVIEN
Write-Host "===> HOAN TAT BAI 1 THANH CONG!" -ForegroundColor Green
Write-Host ""
