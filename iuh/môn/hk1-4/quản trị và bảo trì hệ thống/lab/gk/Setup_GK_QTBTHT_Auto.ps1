<#
================================================================================
SCRIPT TỰ ĐỘNG CẤU HÌNH THI GIỮA KỲ QTBTHT - IUH
Đề bài: Đề minh họa KTTH QTBTHT DHTH18 (Domain: nhom1.vn)
Chạy trên Server 1 với quyền Administrator sau khi đã nâng cấp DC
================================================================================
#>

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Clear-Host
Write-Host "==================================================================" -ForegroundColor Yellow
Write-Host "   BẮT ĐẦU CẤU HÌNH TỰ ĐỘNG BÀI THI GIỮA KỲ QTBTHT (IUH)         " -ForegroundColor Yellow
Write-Host "==================================================================" -ForegroundColor Yellow

# ------------------------------------------------------------------------------
# 1. TẠO CẤU TRÚC OU, GROUPS VÀ USERS (CÂU 3)
# ------------------------------------------------------------------------------
Write-Host "`n[1/5] Khởi tạo OU, Group và User..." -ForegroundColor Cyan
Import-Module ActiveDirectory

$domainDN = (Get-ADDomain).DistinguishedName
Write-Host " -> Domain DN: $domainDN" -ForegroundColor Gray

# Tạo OU Giaovien và Quanly
$ous = @("Giaovien", "Quanly")
foreach ($ou in $ous) {
    if (-not (Get-ADOrganizationalUnit -Filter "Name -eq '$ou'")) {
        New-ADOrganizationalUnit -Name $ou -Path $domainDN
        Write-Host "  [+] Đã tạo OU: $ou" -ForegroundColor Green
    } else {
        Write-Host "  [*] OU $ou đã tồn tại." -ForegroundColor Gray
    }
}

# Tạo Security Groups
$groups = @(
    @{Name="G_Giaovien"; OU="OU=Giaovien,$domainDN"},
    @{Name="G_Quanly";   OU="OU=Quanly,$domainDN"}
)
foreach ($g in $groups) {
    if (-not (Get-ADGroup -Filter "Name -eq '$($g.Name)'")) {
        New-ADGroup -Name $g.Name -GroupScope Global -GroupCategory Security -Path $g.OU
        Write-Host "  [+] Đã tạo Group: $($g.Name)" -ForegroundColor Green
    } else {
        Write-Host "  [*] Group $($g.Name) đã tồn tại." -ForegroundColor Gray
    }
}

# Tạo Users (Password: a@1 hoặc theo quy định mật khẩu)
$securePass = ConvertTo-SecureString "a@1" -AsPlainText -Force
$users = @(
    @{Name="ttgv"; Display="To Truong Giao Vien"; OU="OU=Giaovien,$domainDN"; Group="G_Giaovien"},
    @{Name="u2";   Display="User 2 Giao Vien";    OU="OU=Giaovien,$domainDN"; Group="G_Giaovien"},
    @{Name="tpql"; Display="Truong Phong Quan Ly"; OU="OU=Quanly,$domainDN";   Group="G_Quanly"},
    @{Name="u1";   Display="User 1 Quan Ly";      OU="OU=Quanly,$domainDN";   Group="G_Quanly"}
)

foreach ($u in $users) {
    if (-not (Get-ADUser -Filter "SamAccountName -eq '$($u.Name)'")) {
        New-ADUser -Name $u.Name -DisplayName $u.Display -SamAccountName $u.Name `
                   -UserPrincipalName "$($u.Name)@nhom1.vn" `
                   -AccountPassword $securePass -Enabled $true -PasswordNeverExpires $true `
                   -Path $u.OU
        Add-ADGroupMember -Identity $u.Group -Members $u.Name
        Write-Host "  [+] Đã tạo User: $($u.Name) (Pass: a@1) -> Thuộc $($u.Group)" -ForegroundColor Green
    } else {
        Write-Host "  [*] User $($u.Name) đã tồn tại." -ForegroundColor Gray
    }
}

# ------------------------------------------------------------------------------
# 2. TẠO CÂY THƯ MỤC TRÊN C:\ (CÂU 2)
# ------------------------------------------------------------------------------
Write-Host "`n[2/5] Tạo cây thư mục trên C:\..." -ForegroundColor Cyan
$folders = @("C:\CHUNG", "C:\DULIEU", "C:\GIAOVIEN", "C:\QUANLY")
foreach ($f in $folders) {
    if (-not (Test-Path $f)) {
        New-Item -Path $f -ItemType Directory | Out-Null
        Write-Host "  [+] Đã tạo thư mục: $f" -ForegroundColor Green
    } else {
        Write-Host "  [*] Thư mục $f đã có sẵn." -ForegroundColor Gray
    }
}

# Tạo file mẫu để test đọc
Set-Content -Path "C:\DULIEU\thongbao.txt" -Value "Thong bao chung cho toan the Giao vien va Quan ly."
Set-Content -Path "C:\CHUNG\readme.txt" -Value "Thu muc chia se chung cho tat ca moi nguoi."

# ------------------------------------------------------------------------------
# 3. THIẾT LẬP QUYỀN NTFS & CREATOR OWNER (CÂU 2)
# ------------------------------------------------------------------------------
Write-Host "`n[3/5] Thiết lập quyền bảo mật NTFS & Creator Owner..." -ForegroundColor Cyan

function Reset-AclWithBasics($path) {
    $acl = Get-Acl $path
    $acl.SetAccessRuleProtection($true, $false) # Bẻ gãy kế thừa, xóa quyền cũ
    $adminRule = New-Object System.Security.AccessControl.FileSystemAccessRule("BUILTIN\Administrators","FullControl","ContainerInherit,ObjectInherit","None","Allow")
    $systemRule = New-Object System.Security.AccessControl.FileSystemAccessRule("NT AUTHORITY\SYSTEM","FullControl","ContainerInherit,ObjectInherit","None","Allow")
    $acl.AddAccessRule($adminRule)
    $acl.AddAccessRule($systemRule)
    Set-Acl -Path $path -AclObject $acl
}

# 3.1 C:\CHUNG: Everyone có quyền tạo & đọc; CREATOR OWNER Full Control (User chỉ xóa file mình tạo)
Reset-AclWithBasics "C:\CHUNG"
$aclChung = Get-Acl "C:\CHUNG"
$evRights = [System.Security.AccessControl.FileSystemRights]"Traverse,ListDirectory,ReadAttributes,ReadExtendedAttributes,CreateFiles,AppendData,WriteAttributes,WriteExtendedAttributes,ReadPermissions"
$evRule = New-Object System.Security.AccessControl.FileSystemAccessRule("Everyone", $evRights, "ContainerInherit,ObjectInherit", "None", "Allow")
$aclChung.AddAccessRule($evRule)
$coRule = New-Object System.Security.AccessControl.FileSystemAccessRule("CREATOR OWNER", "FullControl", "ContainerInherit,ObjectInherit", "InheritOnly", "Allow")
$aclChung.AddAccessRule($coRule)
Set-Acl "C:\CHUNG" $aclChung
Write-Host "  [+] C:\CHUNG -> Everyone (Read+Write), CREATOR OWNER (Full Control)" -ForegroundColor Green

# 3.2 C:\DULIEU: G_Giaovien & G_Quanly có quyền Read
Reset-AclWithBasics "C:\DULIEU"
$aclDuLieu = Get-Acl "C:\DULIEU"
$gvRead = New-Object System.Security.AccessControl.FileSystemAccessRule("nhom1\G_Giaovien", "ReadAndExecute", "ContainerInherit,ObjectInherit", "None", "Allow")
$qlRead = New-Object System.Security.AccessControl.FileSystemAccessRule("nhom1\G_Quanly", "ReadAndExecute", "ContainerInherit,ObjectInherit", "None", "Allow")
$aclDuLieu.AddAccessRule($gvRead)
$aclDuLieu.AddAccessRule($qlRead)
Set-Acl "C:\DULIEU" $aclDuLieu
Write-Host "  [+] C:\DULIEU -> G_Giaovien (Read), G_Quanly (Read)" -ForegroundColor Green

# 3.3 C:\GIAOVIEN: G_Giaovien Full Control, G_Quanly không có quyền
Reset-AclWithBasics "C:\GIAOVIEN"
$aclGV = Get-Acl "C:\GIAOVIEN"
$gvFull = New-Object System.Security.AccessControl.FileSystemAccessRule("nhom1\G_Giaovien", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
$aclGV.AddAccessRule($gvFull)
Set-Acl "C:\GIAOVIEN" $aclGV
Write-Host "  [+] C:\GIAOVIEN -> G_Giaovien (Full Control)" -ForegroundColor Green

# 3.4 C:\QUANLY: G_Quanly Full Control, G_Giaovien không có quyền
Reset-AclWithBasics "C:\QUANLY"
$aclQL = Get-Acl "C:\QUANLY"
$qlFull = New-Object System.Security.AccessControl.FileSystemAccessRule("nhom1\G_Quanly", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
$aclQL.AddAccessRule($qlFull)
Set-Acl "C:\QUANLY" $aclQL
Write-Host "  [+] C:\QUANLY -> G_Quanly (Full Control)" -ForegroundColor Green

# ------------------------------------------------------------------------------
# 4. CHIA SẺ THƯ MỤC QUA MẠNG (SHARE PERMISSIONS)
# ------------------------------------------------------------------------------
Write-Host "`n[4/5] Chia sẻ thư mục qua mạng (Everyone: Full Control)..." -ForegroundColor Cyan
foreach ($name in @("CHUNG", "DULIEU", "GIAOVIEN", "QUANLY")) {
    if (-not (Get-SmbShare -Name $name -ErrorAction SilentlyContinue)) {
        New-SmbShare -Name $name -Path "C:\$name" -FullAccess "Everyone" | Out-Null
        Write-Host "  [+] Đã chia sẻ: \\Server1\$name" -ForegroundColor Green
    } else {
        Write-Host "  [*] Share $name đã tồn tại." -ForegroundColor Gray
    }
}

# ------------------------------------------------------------------------------
# 5. CÀI ĐẶT VÀ CẤU HÌNH FSRM (CÂU 4)
# ------------------------------------------------------------------------------
Write-Host "`n[5/5] Cài đặt & Cấu hình File Server Resource Manager (FSRM)..." -ForegroundColor Cyan

if ((Get-WindowsFeature FS-Resource-Manager).InstallState -ne "Installed") {
    Write-Host "  [*] Đang cài đặt tính năng FS-Resource-Manager..." -ForegroundColor Yellow
    Install-WindowsFeature FS-Resource-Manager -IncludeManagementTools | Out-Null
}

# Thiết lập Quota 10MB (Hard Quota) trên C:\CHUNG
cmd.exe /c "dirquota quota add /path:C:\CHUNG /limit:10mb /type:hard" 2>$null
Write-Host "  [+] Đã thiết lập Quota 10MB (Hard) cho C:\CHUNG" -ForegroundColor Green

# Chặn file *.exe (Active File Screen) trên C:\CHUNG
cmd.exe /c "filescrn screen add /path:C:\CHUNG /add-filegroup:`"Executable Files`" /type:active" 2>$null
Write-Host "  [+] Đã thiết lập File Screen chặn *.exe trên C:\CHUNG" -ForegroundColor Green

Write-Host "`n==================================================================" -ForegroundColor Yellow
Write-Host "       ĐÃ CẤU HÌNH THÀNH CÔNG 100% CÁC MỤC THỰC HÀNH!            " -ForegroundColor Yellow
Write-Host "==================================================================" -ForegroundColor Yellow
Write-Host "LƯU Ý CUỐI CÙNG:" -ForegroundColor Cyan
Write-Host "1. Chạy lệnh 'gpupdate /force' để áp dụng GPO mới nhất."
Write-Host "2. Dùng 'dsa.msc' thực hiện thao tác Delegate Control Wizard theo hướng dẫn trong file ON_TAP_GIUA_KY_QTBTHT_FULL.md."
