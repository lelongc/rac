# ==============================================================================
# SCRIPT TỰ ĐỘNG HÓA CẤU HÌNH BÀI LAB 5 - QUẢN TRỊ CHIA SẺ VÀ PHÂN QUYỀN NTFS
# Áp dụng cho: Windows Server 2012 DC (Domain: newstar.vn)
# ==============================================================================

Write-Host "==========================================================================" -ForegroundColor Cyan
Write-Host "     BAT DAU TU DONG HOA LAB 5: SHARE PERMISSION & ADVANCED NTFS          " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan

Import-Module ActiveDirectory -ErrorAction SilentlyContinue

# 1. TẠO GROUPS VÀ USERS TRÊN DOMAIN newstar.vn
Write-Host "`n1. KHOI TAO GROUPS VA USERS TRONG ACTIVE DIRECTORY:" -ForegroundColor Yellow
$domainName = (Get-ADDomain).DNSRoot

# Groups
$groups = @("KT", "NS")
foreach ($g in $groups) {
    if (-not (Get-ADGroup -Filter "Name -eq '$g'" -ErrorAction SilentlyContinue)) {
        New-ADGroup -Name $g -GroupScope Global -GroupCategory Security
        Write-Host "  [+] Da tao moi Group: $g" -ForegroundColor Green
    } else {
        Write-Host "  [+] Group $g da ton tai." -ForegroundColor Gray
    }
}

# Users
$users = @(
    @{ Name = "KT1"; Group = "KT" },
    @{ Name = "KT2"; Group = "KT" },
    @{ Name = "NS1"; Group = "NS" },
    @{ Name = "NS2"; Group = "NS" }
)

$pass = ConvertTo-SecureString "P@ssword123!" -AsPlainText -Force

foreach ($u in $users) {
    $uName = $u.Name
    $gName = $u.Group
    $usr = Get-ADUser -Filter "SamAccountName -eq '$uName'" -ErrorAction SilentlyContinue
    if (-not $usr) {
        New-ADUser -Name $uName `
                   -SamAccountName $uName `
                   -UserPrincipalName "$uName@$domainName" `
                   -AccountPassword $pass `
                   -Enabled $true `
                   -PasswordNeverExpires $true `
                   -ChangePasswordAtLogon $false
        Write-Host "  [+] Da tao moi user: $uName (Mat khau: P@ssword123!)" -ForegroundColor Green
    } else {
        Set-ADAccountPassword -Identity $uName -NewPassword $pass -Reset
        Set-ADUser -Identity $uName -Enabled $true -PasswordNeverExpires $true -ChangePasswordAtLogon $false
        Write-Host "  [+] User $uName da ton tai. Reset password: P@ssword123!" -ForegroundColor Gray
    }
    # Add to group
    Add-ADGroupMember -Identity $gName -Members $uName -ErrorAction SilentlyContinue
    Write-Host "      -> Da add $uName vao Group $gName" -ForegroundColor Cyan
}

# 2. TẠO CẤU TRÚC CÂY THƯ MỤC TRÊN Ổ C:
Write-Host "`n2. KHOI TAO CAY THU MUC C:\Data:" -ForegroundColor Yellow
$folders = @("C:\Data", "C:\Data\DataChung", "C:\Data\DataKeToan", "C:\Data\DataNhanSu")
foreach ($f in $folders) {
    if (-not (Test-Path $f)) {
        New-Item -Path $f -ItemType Directory -Force | Out-Null
        Write-Host "  [+] Da tao thu muc: $f" -ForegroundColor Green
    } else {
        Write-Host "  [+] Thu muc $f da ton tai." -ForegroundColor Gray
    }
}

# Tạo tập tin Document.txt
$docFile = "C:\Data\Document.txt"
if (-not (Test-Path $docFile)) {
    "Day la tai lieu Document chung cua he thong newstar.vn" | Out-File -FilePath $docFile -Encoding utf8
    Write-Host "  [+] Da tao tap tin: $docFile" -ForegroundColor Green
}

# 3. CHIA SẺ MẠNG SHARE PERMISSION CHO C:\Data
Write-Host "`n3. THIET LAP CHIA SE MANG (SMB SHARE):" -ForegroundColor Yellow
$share = Get-SmbShare -Name "Data" -ErrorAction SilentlyContinue
if (-not $share) {
    New-SmbShare -Name "Data" -Path "C:\Data" -FullAccess "Everyone" | Out-Null
    Write-Host "  [+] Da tao Share 'Data' voi quyen Everyone: Full Control" -ForegroundColor Green
} else {
    Set-SmbShare -Name "Data" -Force | Out-Null
    Grant-SmbShareAccess -Name "Data" -AccountName "Everyone" -AccessRight Full -Force | Out-Null
    Write-Host "  [+] Share 'Data' da ton tai. Da cap nhat quyen Everyone: Full Control" -ForegroundColor Green
}

# 4. CẤU HÌNH NTFS CHO C:\Data
Write-Host "`n4. PHAN QUYEN NTFS CHO THU MUC GOC C:\Data:" -ForegroundColor Yellow
$aclData = Get-Acl "C:\Data"
$aclData.SetAccessRuleProtection($true, $false) # Ngắt kế thừa và không sao chép quyền thừa kế

# Cấp Administrators và SYSTEM: FullControl
$adminRule = New-Object System.Security.AccessControl.FileSystemAccessRule("Administrators", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
$sysRule   = New-Object System.Security.AccessControl.FileSystemAccessRule("SYSTEM", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
$aclData.SetAccessRule($adminRule)
$aclData.SetAccessRule($sysRule)

# Cấp KT và NS: ReadAndExecute
$ktRule = New-Object System.Security.AccessControl.FileSystemAccessRule("newstar\KT", "ReadAndExecute", "ContainerInherit,ObjectInherit", "None", "Allow")
$nsRule = New-Object System.Security.AccessControl.FileSystemAccessRule("newstar\NS", "ReadAndExecute", "ContainerInherit,ObjectInherit", "None", "Allow")
$aclData.SetAccessRule($ktRule)
$aclData.SetAccessRule($nsRule)

Set-Acl -Path "C:\Data" -AclObject $aclData
Write-Host "  [+] Da cau hinh NTFS C:\Data: Administrators (Full), KT (Read), NS (Read)" -ForegroundColor Green

# 5. CẤU HÌNH NTFS CHO C:\Data\DataChung
Write-Host "`n5. PHAN QUYEN NTFS CHO C:\Data\DataChung:" -ForegroundColor Yellow
$aclChung = Get-Acl "C:\Data\DataChung"
$aclChung.SetAccessRuleProtection($true, $false)
$aclChung.SetAccessRule($adminRule)
$aclChung.SetAccessRule($sysRule)
$ktFull = New-Object System.Security.AccessControl.FileSystemAccessRule("newstar\KT", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
$nsFull = New-Object System.Security.AccessControl.FileSystemAccessRule("newstar\NS", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
$aclChung.SetAccessRule($ktFull)
$aclChung.SetAccessRule($nsFull)
Set-Acl -Path "C:\Data\DataChung" -AclObject $aclChung
Write-Host "  [+] Da cau hinh NTFS DataChung: KT (Full), NS (Full)" -ForegroundColor Green

# 6. CẤU HÌNH NTFS CHO C:\Data\DataKeToan (KÈM CHẶN KT1)
Write-Host "`n6. PHAN QUYEN NTFS CHO C:\Data\DataKeToan (CHAN KT1):" -ForegroundColor Yellow
$aclKT = Get-Acl "C:\Data\DataKeToan"
$aclKT.SetAccessRuleProtection($true, $false)
$aclKT.SetAccessRule($adminRule)
$aclKT.SetAccessRule($sysRule)
$aclKT.SetAccessRule($ktFull)

# Cấm riêng KT1: Deny Read, Write, Execute
$kt1Deny = New-Object System.Security.AccessControl.FileSystemAccessRule("newstar\KT1", "FullControl", "ContainerInherit,ObjectInherit", "None", "Deny")
$aclKT.AddAccessRule($kt1Deny)
Set-Acl -Path "C:\Data\DataKeToan" -AclObject $aclKT
Write-Host "  [+] Da cau hinh NTFS DataKeToan: KT (Full), KT1 (DENY FullControl)" -ForegroundColor Green

# 7. CẤU HÌNH NTFS CHO C:\Data\DataNhanSu (NGUYÊN TẮC KHÔNG XÓA DỮ LIỆU NGƯỜI KHÁC)
Write-Host "`n7. PHAN QUYEN NTFS CHO C:\Data\DataNhanSu (NGUYEN TAC KHONG XOA FILE CUA NHAU):" -ForegroundColor Yellow
$aclNS = Get-Acl "C:\Data\DataNhanSu"
$aclNS.SetAccessRuleProtection($true, $false)
$aclNS.SetAccessRule($adminRule)
$aclNS.SetAccessRule($sysRule)

# CREATOR OWNER: FullControl
$creatorRule = New-Object System.Security.AccessControl.FileSystemAccessRule("CREATOR OWNER", "FullControl", "ContainerInherit,ObjectInherit", "InheritOnly", "Allow")
$aclNS.SetAccessRule($creatorRule)

# Group NS: Quyền đọc, ghi, tạo file, tạo folder NHƯNG BỎ Delete và DeleteSubdirectoriesAndFiles
# FileSystemRights tính toán:
# Modify = 1245631 (0x1301BF) bao gồm Delete (65536)
# Bỏ Delete: 1245631 - 65536 = 1180095
$nsRights = [System.Security.AccessControl.FileSystemRights]"ReadAndExecute, Write, ListDirectory, ReadAttributes, ReadExtendedAttributes, CreateFiles, CreateDirectories, WriteAttributes, WriteExtendedAttributes, ReadPermissions"
$nsNoDeleteRule = New-Object System.Security.AccessControl.FileSystemAccessRule("newstar\NS", $nsRights, "ContainerInherit,ObjectInherit", "None", "Allow")
$aclNS.SetAccessRule($nsNoDeleteRule)

Set-Acl -Path "C:\Data\DataNhanSu" -AclObject $aclNS
Write-Host "  [+] Da cau hinh NTFS DataNhanSu: CREATOR OWNER (Full), Group NS (Bo Delete)" -ForegroundColor Green

Write-Host "`n==========================================================================" -ForegroundColor Cyan
Write-Host "          HOAN TAT TU DONG HOA LAB 5: SAN SANG KIEM THU!                  " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan
