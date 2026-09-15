# ==============================================================================
# SCRIPT TỰ ĐỘNG HÓA CẤU HÌNH TOÀN DIỆN BÀI LAB 7 - TRIỂN KHAI PROFILE
# Áp dụng cho: Windows Server 2012 R2 / 2016 / 2019 Domain Controller (Domain: newstar.vn)
# ==============================================================================

Write-Host "==========================================================================" -ForegroundColor Cyan
Write-Host "         BAT DAU TU DONG HOA CAU HINH LAB 7: TRIEN KHAI PROFILE           " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan

Import-Module ActiveDirectory -ErrorAction SilentlyContinue
Import-Module GroupPolicy -ErrorAction SilentlyContinue

$domain = (Get-ADDomain).DNSRoot
$domainDN = (Get-ADDomain).DistinguishedName
$serverHost = $env:COMPUTERNAME

Write-Host "`n[+] Domain dang quan tri: $domain ($domainDN)" -ForegroundColor Green
Write-Host "[+] May chu Domain Controller: $serverHost" -ForegroundColor Green

# ------------------------------------------------------------------------------
# 1. KHOI TAO CO CAU TO CHUC OU VA TAI KHOAN NGUOI DUNG LAB 7
# ------------------------------------------------------------------------------
Write-Host "`n1. KHOI TAO CAC OU VA TAI KHOAN NGUOI DUNG:" -ForegroundColor Yellow

# 1.1. OU Nhansu
$ouNhansuDN = "OU=Nhansu,$domainDN"
if (-not (Get-ADOrganizationalUnit -Filter "DistinguishedName -eq '$ouNhansuDN'" -ErrorAction SilentlyContinue)) {
    New-ADOrganizationalUnit -Name "Nhansu" -Path $domainDN -ProtectedFromAccidentalDeletion $false
    Write-Host "  [+] Da tao moi OU: Nhansu ($ouNhansuDN)" -ForegroundColor Green
} else {
    Write-Host "  [+] OU 'Nhansu' da ton tai." -ForegroundColor Gray
}

# 1.2. OU Ke Toan
$ouKeToanDN = "OU=Ke Toan,$domainDN"
if (-not (Get-ADOrganizationalUnit -Filter "DistinguishedName -eq '$ouKeToanDN'" -ErrorAction SilentlyContinue)) {
    New-ADOrganizationalUnit -Name "Ke Toan" -Path $domainDN -ProtectedFromAccidentalDeletion $false
    Write-Host "  [+] Da tao moi OU: Ke Toan ($ouKeToanDN)" -ForegroundColor Green
} else {
    Write-Host "  [+] OU 'Ke Toan' da ton tai." -ForegroundColor Gray
}

# Hàm tiện ích tạo tài khoản nếu chưa tồn tại
$secPass = ConvertTo-SecureString "123" -AsPlainText -Force

function Ensure-User {
    param($Username, $DisplayName, $TargetOU)
    $existing = Get-ADUser -Filter "SamAccountName -eq '$Username'" -ErrorAction SilentlyContinue
    if (-not $existing) {
        New-ADUser -Name $DisplayName -SamAccountName $Username -UserPrincipalName "$Username@$domain" `
            -AccountPassword $secPass -Enabled $true -PasswordNeverExpires $true -Path $TargetOU
        Write-Host "  [+] Da tao nguoi dung: $Username ($DisplayName) tai $TargetOU" -ForegroundColor Green
    } else {
        # Nếu đã có, di chuyển vào đúng OU yêu cầu nếu cần
        if ($existing.DistinguishedName -notlike "*$TargetOU*") {
            Move-ADObject -Identity $existing.DistinguishedName -TargetPath $TargetOU -ErrorAction SilentlyContinue
            Write-Host "  [+] Da di chuyen $Username ve $TargetOU" -ForegroundColor Cyan
        } else {
            Write-Host "  [+] Nguoi dung '$Username' da ton tai hop le tai $TargetOU." -ForegroundColor Gray
        }
        Set-ADUser -Identity $Username -Enabled $true -PasswordNeverExpires $true
    }
}

Ensure-User "ns1" "Nhan Su 1" $ouNhansuDN
Ensure-User "ns2" "Nhan Su 2" $ouNhansuDN
Ensure-User "u11" "User 11 Ke Toan" $ouKeToanDN
Ensure-User "sep" "Sep Giam Doc" $domainDN
Ensure-User "u1" "User 1" $domainDN
Ensure-User "u2" "User 2" $domainDN

# ------------------------------------------------------------------------------
# 2. TAO VA CHIA SE CAC THU MUC DUNG TRONG LAB 7 (SHARE & NTFS FULL CONTROL)
# ------------------------------------------------------------------------------
Write-Host "`n2. TAO THU MUC VA CHIA SE MANG (SMB SHARES):" -ForegroundColor Yellow

$sharesToCreate = @(
    @{ Name = "home";         Path = "C:\home";         Desc = "Home Directory Share" },
    @{ Name = "Nhansu_Chung"; Path = "C:\Nhansu_Chung"; Desc = "Phong Nhan Su - Dung chung" },
    @{ Name = "Nhansu_rieng"; Path = "C:\Nhansu_rieng"; Desc = "Phong Nhan Su - Dung rieng" },
    @{ Name = "Sep_Roaming";  Path = "C:\Sep_Roaming";  Desc = "Roaming Profile cua Sep" },
    @{ Name = "Direction";    Path = "C:\Direction";    Desc = "Folder Redirection Share" }
)

foreach ($sh in $sharesToCreate) {
    if (-not (Test-Path $sh.Path)) {
        New-Item -Path $sh.Path -ItemType Directory -Force | Out-Null
        Write-Host "  [+] Da tao thu muc vat ly: $($sh.Path)" -ForegroundColor Green
    }
    
    # Phân quyền NTFS: Everyone / Authenticated Users Full Control để Client truy cập thông suốt
    $acl = Get-Acl $sh.Path
    $ruleEveryone = New-Object System.Security.AccessControl.FileSystemAccessRule("Everyone", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
    $ruleAuth = New-Object System.Security.AccessControl.FileSystemAccessRule("Authenticated Users", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
    $acl.SetAccessRule($ruleEveryone)
    $acl.AddAccessRule($ruleAuth)
    Set-Acl -Path $sh.Path -AclObject $acl
    
    # Tạo SMB Share
    $existingShare = Get-SmbShare -Name $sh.Name -ErrorAction SilentlyContinue
    if (-not $existingShare) {
        New-SmbShare -Name $sh.Name -Path $sh.Path -FullAccess "Everyone", "Authenticated Users" -Description $sh.Desc | Out-Null
        Write-Host "  [+] Da tao SMB Share: \\$serverHost\$($sh.Name) (Full Control Everyone)" -ForegroundColor Green
    } else {
        Grant-SmbShareAccess -Name $sh.Name -AccountName "Everyone" -AccessRight Full -Force -ErrorAction SilentlyContinue | Out-Null
        Write-Host "  [+] SMB Share '$($sh.Name)' da ton tai. Da cap nhat quyen Full Control." -ForegroundColor Gray
    }
}

# ------------------------------------------------------------------------------
# 3. CAU HINH PHAN 1: HOME PROFILE (HOME FOLDER) TREN USER ATTRIBUTES
# ------------------------------------------------------------------------------
Write-Host "`n3. CAU HINH PHAN 1: HOME FOLDER (CONNECT Z: TO \\$serverHost\home\%username%):" -ForegroundColor Yellow

$homeUsers = @("hiepdh", "u1", "u2")
foreach ($u in $homeUsers) {
    $adUser = Get-ADUser -Filter "SamAccountName -eq '$u'" -ErrorAction SilentlyContinue
    if ($adUser) {
        $userHomePath = "\\$serverHost\home\$u"
        Set-ADUser -Identity $u -HomeDrive "Z:" -HomeDirectory $userHomePath
        Write-Host "  [+] Da gan Home Folder cho user '$u': Z: -> $userHomePath" -ForegroundColor Green
        
        # Đảm bảo thư mục con của user tồn tại trong C:\home
        $localUserHome = "C:\home\$u"
        if (-not (Test-Path $localUserHome)) {
            New-Item -Path $localUserHome -ItemType Directory -Force | Out-Null
            $uAcl = Get-Acl $localUserHome
            $uRule = New-Object System.Security.AccessControl.FileSystemAccessRule($u, "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
            $uAcl.AddAccessRule($uRule)
            Set-Acl -Path $localUserHome -AclObject $uAcl
            Write-Host "      -> Da khoi tao thu muc con: $localUserHome" -ForegroundColor Cyan
        }
    }
}

# ------------------------------------------------------------------------------
# 4. CAU HINH PHAN 2: FSRM QUOTA (HAN NGẠCH LUU TRU CHO PHONG NHAN SU)
# ------------------------------------------------------------------------------
Write-Host "`n4. CAU HINH PHAN 2: FSRM QUOTA CHO C:\Nhansu_Chung VA C:\Nhansu_rieng:" -ForegroundColor Yellow

# Kiểm tra cài đặt tính năng File Server Resource Manager
$fsrmFeature = Get-WindowsFeature -Name FS-Resource-Manager
if (-not $fsrmFeature.Installed) {
    Write-Host "  [+] Dang cai dat tinh nang FS-Resource-Manager..." -ForegroundColor Cyan
    Install-WindowsFeature -Name FS-Resource-Manager -IncludeManagementTools | Out-Null
    Write-Host "  [+] Cai dat FS-Resource-Manager thanh cong!" -ForegroundColor Green
}

Import-Module FileServerResourceManager -ErrorAction SilentlyContinue

# Cấu hình Quota 1 GB cho C:\Nhansu_Chung
try {
    $qChung = Get-FsrmQuota -Path "C:\Nhansu_Chung" -ErrorAction SilentlyContinue
    if (-not $qChung) {
        New-FsrmQuota -Path "C:\Nhansu_Chung" -Size 1GB -Description "Quota 1GB Hard cho Nhansu_Chung" | Out-Null
        Write-Host "  [+] Da tao FSRM Quota cho 'C:\Nhansu_Chung': 1 GB (Hard Limit)" -ForegroundColor Green
    } else {
        Set-FsrmQuota -Path "C:\Nhansu_Chung" -Size 1GB | Out-Null
        Write-Host "  [+] Da cap nhat FSRM Quota cho 'C:\Nhansu_Chung': 1 GB" -ForegroundColor Gray
    }
} catch {
    Write-Host "  [!] Chu y: $($_.Exception.Message)" -ForegroundColor Yellow
}

# Cấu hình Quota 500 MB cho C:\Nhansu_rieng
try {
    $qRieng = Get-FsrmQuota -Path "C:\Nhansu_rieng" -ErrorAction SilentlyContinue
    if (-not $qRieng) {
        New-FsrmQuota -Path "C:\Nhansu_rieng" -Size 500MB -Description "Quota 500MB Hard cho Nhansu_rieng" | Out-Null
        Write-Host "  [+] Da tao FSRM Quota cho 'C:\Nhansu_rieng': 500 MB (Hard Limit)" -ForegroundColor Green
    } else {
        Set-FsrmQuota -Path "C:\Nhansu_rieng" -Size 500MB | Out-Null
        Write-Host "  [+] Da cap nhat FSRM Quota cho 'C:\Nhansu_rieng': 500 MB" -ForegroundColor Gray
    }
} catch {
    Write-Host "  [!] Chu y: $($_.Exception.Message)" -ForegroundColor Yellow
}

# ------------------------------------------------------------------------------
# 5. CAU HINH PHAN 2: GPO 'Profile nhansu' (LOGON SCRIPT MAP M: VA N:)
# ------------------------------------------------------------------------------
Write-Host "`n5. CAU HINH GPO 'Profile nhansu' VA KICH BAN DANG NHAP (profile.bat):" -ForegroundColor Yellow

$gpoNhansuName = "Profile nhansu"
$gpoNhansu = Get-GPO -Name $gpoNhansuName -ErrorAction SilentlyContinue
if (-not $gpoNhansu) {
    $gpoNhansu = New-GPO -Name $gpoNhansuName -Comment "GPO Lab 7 - Logon Script map o dia Nhan Su"
    Write-Host "  [+] Da tao moi GPO: $gpoNhansuName (ID: $($gpoNhansu.Id))" -ForegroundColor Green
} else {
    Write-Host "  [+] GPO '$gpoNhansuName' da ton tai." -ForegroundColor Gray
}

# Tạo tập tin profile.bat trong thư mục SYSVOL của GPO
$guidNhansu = $gpoNhansu.Id.ToString("B").ToUpper()
$nhansuScriptsDir = "C:\Windows\SYSVOL\sysvol\$domain\Policies\$guidNhansu\User\Scripts\Logon"
if (-not (Test-Path $nhansuScriptsDir)) {
    New-Item -Path $nhansuScriptsDir -ItemType Directory -Force | Out-Null
}

$profileBatFile = "$nhansuScriptsDir\profile.bat"
$batContent = @"
net use m: \\$serverHost\Nhansu_Chung
net use n: \\$serverHost\Nhansu_rieng
"@
Set-Content -Path $profileBatFile -Value $batContent -Encoding Ascii
Write-Host "  [+] Da tao tep kịch ban: $profileBatFile" -ForegroundColor Green

# Cấu hình scripts.ini khai báo kịch bản logon
$nhansuIni = "C:\Windows\SYSVOL\sysvol\$domain\Policies\$guidNhansu\User\Scripts\scripts.ini"
$iniContent = @"
[Logon]
0CmdLine=profile.bat
0Parameters=
"@
Set-Content -Path $nhansuIni -Value $iniContent -Encoding Unicode

# Đăng ký Client-Side Extension cho Scripts trong Active Directory
$gpoNhansuDN = "CN=$guidNhansu,CN=Policies,CN=System,$domainDN"
Set-ADObject -Identity $gpoNhansuDN -Replace @{
    gPCUserExtensionNames = "[{42B5FAAE-6536-11D2-AE5A-0000F87571E3}{40B6664F-4972-11D1-A7CA-0000F87571E3}]"
} -ErrorAction SilentlyContinue

# Đồng bộ số phiên bản gpt.ini
$gptIni1 = "C:\Windows\SYSVOL\sysvol\$domain\Policies\$guidNhansu\gpt.ini"
$ver1 = 1
if (Test-Path $gptIni1) {
    foreach ($line in (Get-Content $gptIni1)) {
        if ($line -match "Version=(\d+)") { $ver1 = [int]$matches[1] + 1 }
    }
}
Set-Content -Path $gptIni1 -Value "[General]`r`nVersion=$ver1`r`ndisplayName=$gpoNhansuName`r`n" -Encoding Ascii
Set-ADObject -Identity $gpoNhansuDN -Replace @{ versionNumber = $ver1 } -ErrorAction SilentlyContinue

# Liên kết GPO 'Profile nhansu' vào OU 'Nhansu'
try {
    New-GPLink -Name $gpoNhansuName -Target $ouNhansuDN -Order 1 -ErrorAction SilentlyContinue | Out-Null
    Write-Host "  [+] Da lien ket GPO '$gpoNhansuName' vao $ouNhansuDN" -ForegroundColor Green
} catch {}

# ------------------------------------------------------------------------------
# 6. CAU HINH PHAN 3: ROAMING PROFILE CHO TAI KHOAN 'sep'
# ------------------------------------------------------------------------------
Write-Host "`n6. CAU HINH PHAN 3: ROAMING PROFILE CHO SEP (\\$serverHost\Sep_Roaming\%username%):" -ForegroundColor Yellow

$sepUser = Get-ADUser -Filter "SamAccountName -eq 'sep'" -ErrorAction SilentlyContinue
if ($sepUser) {
    $sepProfilePath = "\\$serverHost\Sep_Roaming\%username%"
    Set-ADUser -Identity "sep" -ProfilePath $sepProfilePath
    Write-Host "  [+] Da cau hinh ProfilePath cho user 'sep': $sepProfilePath" -ForegroundColor Green
}

# ------------------------------------------------------------------------------
# 7. CAU HINH PHAN 4: FOLDER REDIRECTION GPO CHO MY DOCUMENTS
# ------------------------------------------------------------------------------
Write-Host "`n7. CAU HINH PHAN 4: GPO 'Folder Redirection' CHO MY DOCUMENTS:" -ForegroundColor Yellow

$gpoRedirName = "Folder Redirection"
$gpoRedir = Get-GPO -Name $gpoRedirName -ErrorAction SilentlyContinue
if (-not $gpoRedir) {
    $gpoRedir = New-GPO -Name $gpoRedirName -Comment "GPO Lab 7 - Chuyen huong thu muc My Documents ve Server"
    Write-Host "  [+] Da tao moi GPO: $gpoRedirName (ID: $($gpoRedir.Id))" -ForegroundColor Green
} else {
    Write-Host "  [+] GPO '$gpoRedirName' da ton tai." -ForegroundColor Gray
}

$guidRedir = $gpoRedir.Id.ToString("B").ToUpper()
$redirSysvolDir = "C:\Windows\SYSVOL\sysvol\$domain\Policies\$guidRedir\User\Documents & Settings"
if (-not (Test-Path $redirSysvolDir)) {
    New-Item -Path $redirSysvolDir -ItemType Directory -Force | Out-Null
}

# Cấu hình fdeploy1.ini (MS-GPFR Version 1 cho Win 7 / 8 / 10 / Server)
# GUID Document: {FDD39AD0-238F-46AF-ADB4-6C85480369C7}
# Flags: 0x00001231 (Redirect to FullPath, Move Contents, Grant Exclusive Rights, Redirect back on removal)
$fdeploy1Content = @"
[Version]
VersionNumber=100

[Folder_Redirection]
{FDD39AD0-238F-46AF-ADB4-6C85480369C7}=S-1-1-0;

[{FDD39AD0-238F-46AF-ADB4-6C85480369C7}_S-1-1-0]
Flags=0x00001231
FullPath=\\$serverHost\Direction\%USERNAME%\Documents
"@
Set-Content -Path "$redirSysvolDir\fdeploy1.ini" -Value $fdeploy1Content -Encoding Unicode

# Cấu hình fdeploy.ini (MS-GPFR Version 0 tương thích ngược)
$fdeployContent = @"
[Folder Redirect]
My Documents=1

[My Documents]
Flags=0x00001231
FullPath=\\$serverHost\Direction\%USERNAME%\Documents
"@
Set-Content -Path "$redirSysvolDir\fdeploy.ini" -Value $fdeployContent -Encoding Unicode
Write-Host "  [+] Da khoi tao fdeploy.ini va fdeploy1.ini tai: $redirSysvolDir" -ForegroundColor Green

# Đăng ký CSE Folder Redirection trong Active Directory
# CSE Folder Redirection: [{25537BA6-77A8-11D2-9B6C-0000F87571E3}{88E72808-52F0-11D2-80E6-0000F87571E3}]
$gpoRedirDN = "CN=$guidRedir,CN=Policies,CN=System,$domainDN"
Set-ADObject -Identity $gpoRedirDN -Replace @{
    gPCUserExtensionNames = "[{25537BA6-77A8-11D2-9B6C-0000F87571E3}{88E72808-52F0-11D2-80E6-0000F87571E3}]"
} -ErrorAction SilentlyContinue

# Đồng thời cấu hình trực tiếp User Shell Folders qua Registry GPO để đảm bảo tương thích 100%
Set-GPRegistryValue -Name $gpoRedirName -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" `
    -ValueName "Personal" -Type ExpandString -Value "\\$serverHost\Direction\%USERNAME%\Documents"

# Cập nhật số phiên bản gpt.ini
$gptIni2 = "C:\Windows\SYSVOL\sysvol\$domain\Policies\$guidRedir\gpt.ini"
$ver2 = 1
if (Test-Path $gptIni2) {
    foreach ($line in (Get-Content $gptIni2)) {
        if ($line -match "Version=(\d+)") { $ver2 = [int]$matches[1] + 1 }
    }
}
Set-Content -Path $gptIni2 -Value "[General]`r`nVersion=$ver2`r`ndisplayName=$gpoRedirName`r`n" -Encoding Ascii
Set-ADObject -Identity $gpoRedirDN -Replace @{ versionNumber = $ver2 } -ErrorAction SilentlyContinue

# Liên kết GPO 'Folder Redirection' vào OU 'Ke Toan'
try {
    New-GPLink -Name $gpoRedirName -Target $ouKeToanDN -Order 1 -ErrorAction SilentlyContinue | Out-Null
    Write-Host "  [+] Da lien ket GPO '$gpoRedirName' vao $ouKeToanDN" -ForegroundColor Green
} catch {}

# Liên kết thêm vào OU PhongKeToan (nếu có trong cây OU IUH)
$phongKT = "OU=PhongKeToan,OU=IUH,$domainDN"
if (Get-ADOrganizationalUnit -Filter "DistinguishedName -eq '$phongKT'" -ErrorAction SilentlyContinue) {
    try {
        New-GPLink -Name $gpoRedirName -Target $phongKT -Order 1 -ErrorAction SilentlyContinue | Out-Null
        Write-Host "  [+] Da lien ket GPO '$gpoRedirName' vao $phongKT" -ForegroundColor Green
    } catch {}
}

# ------------------------------------------------------------------------------
# 8. CAP NHAT CHINH SACH GPUPDATE TREN SERVER
# ------------------------------------------------------------------------------
Write-Host "`n8. DONG BO CHINH SACH (gpupdate /force):" -ForegroundColor Yellow
gpupdate /force | Out-Null
Write-Host "  [+] Da cap nhat GPO thanh cong tren Domain Controller!" -ForegroundColor Green

Write-Host "`n==========================================================================" -ForegroundColor Cyan
Write-Host "     HOAN TAT TU DONG HOA LAB 7! CAC CHINH SACH PROFILE DA SAN SANG.      " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan
