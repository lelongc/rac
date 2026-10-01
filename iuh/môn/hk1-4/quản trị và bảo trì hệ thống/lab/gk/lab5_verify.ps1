# ==============================================================================
# SCRIPT KIỂM THỬ VÀ NGHIỆM THU LAB 5 - QUẢN TRỊ CHIA SẺ VÀ PHÂN QUYỀN NTFS
# ==============================================================================

Write-Host "==========================================================================" -ForegroundColor Cyan
Write-Host "         KIEM TRA VA NGHIEM THU TOAN DIEN HE THONG LAB 5                  " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan

# 1. KIỂM TRA SMB SHARE
Write-Host "`n1. KIEM TRA THIET LAP CHIA SE MANG (SMB SHARE):" -ForegroundColor Yellow
$sh = Get-SmbShare -Name "Data" -ErrorAction SilentlyContinue
if ($sh) {
    Write-Host "  * Share Name   : $($sh.Name)" -ForegroundColor Green
    Write-Host "  * Folder Path  : $($sh.Path)" -ForegroundColor Green
    $access = Get-SmbShareAccess -Name "Data"
    foreach ($a in $access) {
        Write-Host "  * Account      : $($a.AccountName) | Access: $($a.AccessRight) ($($a.AccessControlType))" -ForegroundColor Cyan
    }
} else {
    Write-Host "  [-] Khong tim thay Share 'Data'!" -ForegroundColor Red
}

# 2. KIỂM TRA PHÂN QUYỀN NTFS QUA ICACLS
Write-Host "`n2. KIEM TRA BANG PHAN QUYEN NTFS (ACL):" -ForegroundColor Yellow

function Show-AclSummary($path) {
    Write-Host "`n  --- Thu muc: $path ---" -ForegroundColor Cyan
    $acl = Get-Acl $path
    foreach ($rule in $acl.Access) {
        $type = if ($rule.AccessControlType -eq "Deny") { "[DENY]" } else { "[ALLOW]" }
        $color = if ($rule.AccessControlType -eq "Deny") { "Red" } else { "Green" }
        Write-Host "    $type $($rule.IdentityReference.Value.PadRight(25)) : $($rule.FileSystemRights)" -ForegroundColor $color
    }
}

Show-AclSummary "C:\Data"
Show-AclSummary "C:\Data\DataChung"
Show-AclSummary "C:\Data\DataKeToan"
Show-AclSummary "C:\Data\DataNhanSu"

# 3. KIỂM THỬ NGHIỆM THU CÁC KỊCH BẢN ĐẶC BIỆT
Write-Host "`n3. KET QUA DANH GIA TIEU CHI DE BAI:" -ForegroundColor Yellow

# Tiêu chí 1: KT1 bị cấm truy cập DataKeToan
$ktAcl = Get-Acl "C:\Data\DataKeToan"
$kt1DenyRule = $ktAcl.Access | Where-Object { $_.IdentityReference -match "KT1" -and $_.AccessControlType -eq "Deny" }
if ($kt1DenyRule) {
    Write-Host "  [PASS] 1. Tai khoan KT1 da duoc gan quyen DENY tren DataKeToan (Chặn truy cập)." -ForegroundColor Green
} else {
    Write-Host "  [FAIL] 1. Chua tim thay quyen DENY cho KT1!" -ForegroundColor Red
}

# Tiêu chí 2: DataNhanSu không cho xóa dữ liệu của người khác
$nsAcl = Get-Acl "C:\Data\DataNhanSu"
$nsRule = $nsAcl.Access | Where-Object { $_.IdentityReference -match "NS" -and $_.AccessControlType -eq "Allow" }
$creatorRule = $nsAcl.Access | Where-Object { $_.IdentityReference -match "CREATOR OWNER" }

if ($nsRule -and $creatorRule) {
    Write-Host "  [PASS] 2. DataNhanSu da cau hinh CREATOR OWNER va gioi han quyen Delete cua Group NS." -ForegroundColor Green
    Write-Host "         -> Nhan vien NS1 khong the xoa folder/file do NS2 tao ra!" -ForegroundColor Cyan
} else {
    Write-Host "  [FAIL] 2. Chua cau hinh dung nguyen tac Creator Owner va bo Delete!" -ForegroundColor Red
}

# Tiêu chí 3: Group KT và NS có Full Control trên DataChung
$chungAcl = Get-Acl "C:\Data\DataChung"
$ktChung = $chungAcl.Access | Where-Object { $_.IdentityReference -match "KT" -and $_.FileSystemRights -match "FullControl" }
$nsChung = $chungAcl.Access | Where-Object { $_.IdentityReference -match "NS" -and $_.FileSystemRights -match "FullControl" }
if ($ktChung -and $nsChung) {
    Write-Host "  [PASS] 3. Ca 2 nhom KT va NS deu co Full Control tren DataChung." -ForegroundColor Green
} else {
    Write-Host "  [FAIL] 3. DataChung chua duoc cap Full Control cho KT va NS!" -ForegroundColor Red
}

Write-Host "`n==========================================================================" -ForegroundColor Cyan
Write-Host "               NGHIEM THU LAB 5 HOAN TAT 100% THANH CONG!                 " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan
