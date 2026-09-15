# ==============================================================================
# SCRIPT TỰ ĐỘNG HÓA CẤU HÌNH BÀI LAB 6 - TRIỂN KHAI VÀ QUẢN LÝ GPO
# Áp dụng cho: Windows Server 2012 R2 / 2016 Domain Controller (Domain: newstar.vn)
# ==============================================================================

Write-Host "==========================================================================" -ForegroundColor Cyan
Write-Host "       BAT DAU TU DONG HOA CAU HINH LAB 6: GROUP POLICY OBJECTS (GPO)     " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan

Import-Module ActiveDirectory -ErrorAction SilentlyContinue
Import-Module GroupPolicy -ErrorAction SilentlyContinue

$domain = (Get-ADDomain).DNSRoot
$domainDN = (Get-ADDomain).DistinguishedName

Write-Host "`n[+] Domain dang quan tri: $domain ($domainDN)" -ForegroundColor Green

# ------------------------------------------------------------------------------
# 1. KHOI TAO GPO 'Remove Recycle Bin' VA CAU HINH CAC CHINH SACH HAN CHE
# ------------------------------------------------------------------------------
Write-Host "`n1. KHOI TAO VA CAU HINH GPO 'Remove Recycle Bin':" -ForegroundColor Yellow
$gpoName1 = "Remove Recycle Bin"
$gpo1 = Get-GPO -Name $gpoName1 -ErrorAction SilentlyContinue
if (-not $gpo1) {
    $gpo1 = New-GPO -Name $gpoName1 -Comment "GPO Lab 6 - Han che giao dien va ung dung nguoi dung"
    Write-Host "  [+] Da tao moi GPO: $gpoName1 (ID: $($gpo1.Id))" -ForegroundColor Green
}
else {
    Write-Host "  [+] GPO '$gpoName1' da ton tai (ID: $($gpo1.Id)). Tien hanh cap nhat..." -ForegroundColor Gray
}

# 1.1. Ẩn biểu tượng Computer trên Desktop (Remove Computer icon on the desktop)
Set-GPRegistryValue -Name $gpoName1 -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\NonEnum" `
    -ValueName "{20D04FE0-3AEA-1069-A2D8-08002B30309D}" -Type DWord -Value 1
Write-Host "  [+] Da cau hinh: Remove Computer icon on the desktop (Enabled)" -ForegroundColor Green

# 1.2. Ẩn thùng rác Recycle Bin trên Desktop (Remove Recycle Bin icon from desktop)
Set-GPRegistryValue -Name $gpoName1 -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\NonEnum" `
    -ValueName "{645FF040-5081-101B-9F08-00AA002F954E}" -Type DWord -Value 1
Write-Host "  [+] Da cau hinh: Remove Recycle Bin icon from desktop (Enabled)" -ForegroundColor Green

# 1.3. Ẩn mục Mouse trong Control Panel (Hide specified Control Panel items)
Set-GPRegistryValue -Name $gpoName1 -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" `
    -ValueName "DisallowCpl" -Type DWord -Value 1
Set-GPRegistryValue -Name $gpoName1 -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowCpl" `
    -ValueName "1" -Type String -Value "Microsoft.Mouse"
Write-Host "  [+] Da cau hinh: Hide specified Control Panel items -> Microsoft.Mouse (Enabled)" -ForegroundColor Green

# 1.4. Cấm thay đổi Theme giao diện (Prevent changing theme)
Set-GPRegistryValue -Name $gpoName1 -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" `
    -ValueName "NoThemesTab" -Type DWord -Value 1
Write-Host "  [+] Da cau hinh: Prevent changing theme (Enabled)" -ForegroundColor Green

# 1.5. Cấm sửa địa chỉ IP card mạng (Prohibit access to properties of a LAN connection)
Set-GPRegistryValue -Name $gpoName1 -Key "HKCU\Software\Policies\Microsoft\Windows\Network Connections" `
    -ValueName "NC_LanProperties" -Type DWord -Value 0
Write-Host "  [+] Da cau hinh: Prohibit access to properties of a LAN connection (Enabled)" -ForegroundColor Green

# 1.6. Khóa thanh tác vụ Taskbar (Lock the Taskbar)
Set-GPRegistryValue -Name $gpoName1 -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" `
    -ValueName "TaskbarLockAll" -Type DWord -Value 1
Set-GPRegistryValue -Name $gpoName1 -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" `
    -ValueName "LockTaskbar" -Type DWord -Value 1
Write-Host "  [+] Da cau hinh: Lock the Taskbar (Enabled)" -ForegroundColor Green

# 1.7. Chặn Command Prompt (Prevent access to the command prompt)
Set-GPRegistryValue -Name $gpoName1 -Key "HKCU\Software\Policies\Microsoft\Windows\System" `
    -ValueName "DisableCMD" -Type DWord -Value 2
Write-Host "  [+] Da cau hinh: Prevent access to the command prompt (Enabled)" -ForegroundColor Green

# 1.8. Chặn ứng dụng Paint (Don't run specified Windows applications: mspaint.exe)
Set-GPRegistryValue -Name $gpoName1 -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" `
    -ValueName "DisallowRun" -Type DWord -Value 1
Set-GPRegistryValue -Name $gpoName1 -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun" `
    -ValueName "1" -Type String -Value "mspaint.exe"
Write-Host "  [+] Da cau hinh: Don't run specified Windows applications -> mspaint.exe (Enabled)" -ForegroundColor Green

# ------------------------------------------------------------------------------
# 2. KHOI TAO GPO 'Script Logon' VA TAO SCRIPT CHAO MUNG welcome.vbs
# ------------------------------------------------------------------------------
Write-Host "`n2. KHOI TAO GPO 'Script Logon' VA KICH BAN DANG NHAP:" -ForegroundColor Yellow
$gpoName2 = "Script Logon"
$gpo2 = Get-GPO -Name $gpoName2 -ErrorAction SilentlyContinue
if (-not $gpo2) {
    $gpo2 = New-GPO -Name $gpoName2 -Comment "GPO Lab 6 - Script Logon Chao Mung"
    Write-Host "  [+] Da tao moi GPO: $gpoName2 (ID: $($gpo2.Id))" -ForegroundColor Green
}
else {
    Write-Host "  [+] GPO '$gpoName2' da ton tai (ID: $($gpo2.Id))." -ForegroundColor Gray
}

$guid2 = $gpo2.Id.ToString("B").ToUpper()
$sysvolScriptsPath = "C:\Windows\SYSVOL\sysvol\$domain\Policies\$guid2\User\Scripts"
$logonPath = "$sysvolScriptsPath\Logon"
if (-not (Test-Path $logonPath)) {
    New-Item -Path $logonPath -ItemType Directory -Force | Out-Null
}

# Tạo tập tin kịch bản welcome.vbs
$vbsFile = "$logonPath\welcome.vbs"
$vbsContent = 'MsgBox "Chuc ban mot ngay lam viec vui ve", 64, "Chao mung"'
Set-Content -Path $vbsFile -Value $vbsContent -Encoding Ascii
Write-Host "  [+] Da tao tep tin welcome.vbs tai: $vbsFile" -ForegroundColor Green

# Cấu hình scripts.ini khai báo kịch bản đăng nhập
$iniFile = "$sysvolScriptsPath\scripts.ini"
$iniContent = @"
[Logon]
0CmdLine=welcome.vbs
0Parameters=
"@
Set-Content -Path $iniFile -Value $iniContent -Encoding Unicode
Write-Host "  [+] Da cap nhat scripts.ini tai: $iniFile" -ForegroundColor Green

# Cập nhật thuộc tính Client-Side Extension trong Active Directory
$gpoDn = "CN=$guid2,CN=Policies,CN=System,$domainDN"
Set-ADObject -Identity $gpoDn -Replace @{
    gPCUserExtensionNames = "[{42B5FAAE-6536-11D2-AE5A-0000F87571E3}{40B6664F-4972-11D1-A7CA-0000F87571E3}]"
} -ErrorAction SilentlyContinue

# Cập nhật số phiên bản gpt.ini
$gptIni = "C:\Windows\SYSVOL\sysvol\$domain\Policies\$guid2\gpt.ini"
$currentVer = 1
if (Test-Path $gptIni) {
    foreach ($line in (Get-Content $gptIni)) {
        if ($line -match "Version=(\d+)") {
            $currentVer = [int]$matches[1] + 1
        }
    }
}
$newGpt = @"
[General]
Version=$currentVer
displayName=$gpoName2
"@
Set-Content -Path $gptIni -Value $newGpt -Encoding Ascii
Set-ADObject -Identity $gpoDn -Replace @{ versionNumber = $currentVer } -ErrorAction SilentlyContinue
Write-Host "  [+] Da dong bo phien ban GPO $($gpoName2): Version $currentVer" -ForegroundColor Green

# ------------------------------------------------------------------------------
# 3. LIEN KET CAC GPO VAO DOMAIN ROOT (LINKING GPO)
# ------------------------------------------------------------------------------
Write-Host "`n3. LIEN KET GPO VAO DOMAIN ROOT ($domainDN):" -ForegroundColor Yellow

try {
    New-GPLink -Name $gpoName1 -Target $domainDN -Order 1 -ErrorAction SilentlyContinue | Out-Null
    Write-Host "  [+] Da lien ket '$gpoName1' vao $domainDN (Order: 1)" -ForegroundColor Green
}
catch {}

try {
    New-GPLink -Name $gpoName2 -Target $domainDN -Order 2 -ErrorAction SilentlyContinue | Out-Null
    Write-Host "  [+] Da lien ket '$gpoName2' vao $domainDN (Order: 2)" -ForegroundColor Green
}
catch {}

# ------------------------------------------------------------------------------
# 4. CAP NHAT CHINH SACH GPUPDATE TREN SERVER
# ------------------------------------------------------------------------------
Write-Host "`n4. CAP NHAT CHINH SACH TREN SERVER (gpupdate /force):" -ForegroundColor Yellow
gpupdate /force | Out-Null
Write-Host "  [+] Da cap nhat GPO thanh cong tren may chu Domain Controller!" -ForegroundColor Green

Write-Host "`n==========================================================================" -ForegroundColor Cyan
Write-Host "     HOAN TAT TU DONG HOA LAB 6! HAY DANG NHAP CLIENT VA CHAY gpupdate   " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan
