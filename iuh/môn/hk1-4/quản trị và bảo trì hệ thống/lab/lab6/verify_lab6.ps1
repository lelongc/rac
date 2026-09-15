# ==============================================================================
# SCRIPT KIỂM THỬ VÀ NGHIỆM THU LAB 6 - TRIỂN KHAI VÀ QUẢN LÝ GPO
# ==============================================================================

Write-Host "==========================================================================" -ForegroundColor Cyan
Write-Host "         KIEM TRA VA NGHIEM THU TOAN DIEN HE THONG GPO LAB 6              " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan

Import-Module ActiveDirectory -ErrorAction SilentlyContinue
Import-Module GroupPolicy -ErrorAction SilentlyContinue

$domain = (Get-ADDomain).DNSRoot
$domainDN = (Get-ADDomain).DistinguishedName
$score = 0
$totalTests = 10

Write-Host "`n[+] Domain kiem tra: $domain ($domainDN)" -ForegroundColor Green

# ------------------------------------------------------------------------------
# 1. KIỂM TRA SỰ TỒN TẠI VÀ TRẠNG THÁI GPO
# ------------------------------------------------------------------------------
Write-Host "`n1. KIEM TRA CAC GROUP POLICY OBJECTS (GPO):" -ForegroundColor Yellow

$gpo1 = Get-GPO -Name "Remove Recycle Bin" -ErrorAction SilentlyContinue
if ($gpo1 -and $gpo1.GpoStatus -eq "AllSettingsEnabled") {
    Write-Host "  [PASS] GPO 'Remove Recycle Bin' ton tai va dang kich hoat (ID: $($gpo1.Id))" -ForegroundColor Green
    $score++
} else {
    Write-Host "  [FAIL] GPO 'Remove Recycle Bin' khong ton tai hoac bi disable!" -ForegroundColor Red
}

$gpo2 = Get-GPO -Name "Script Logon" -ErrorAction SilentlyContinue
if ($gpo2 -and $gpo2.GpoStatus -eq "AllSettingsEnabled") {
    Write-Host "  [PASS] GPO 'Script Logon' ton tai va dang kich hoat (ID: $($gpo2.Id))" -ForegroundColor Green
    $score++
} else {
    Write-Host "  [FAIL] GPO 'Script Logon' khong ton tai hoac bi disable!" -ForegroundColor Red
}

# ------------------------------------------------------------------------------
# 2. KIỂM TRA LIÊN KẾT GPO (LINK STATUS)
# ------------------------------------------------------------------------------
Write-Host "`n2. KIEM TRA LIEN KET GPO VAO DOMAIN ROOT:" -ForegroundColor Yellow
$links = (Get-GPInheritance -Target $domainDN).GpoLinks
$link1 = $links | Where-Object { $_.DisplayName -eq "Remove Recycle Bin" -and $_.Enabled }
$link2 = $links | Where-Object { $_.DisplayName -eq "Script Logon" -and $_.Enabled }

if ($link1 -and $link2) {
    Write-Host "  [PASS] Ca 2 GPO deu duoc lien ket va kich hoat tren Domain Root:" -ForegroundColor Green
    Write-Host "         - $($link1.DisplayName) (Order: $($link1.Order))" -ForegroundColor Cyan
    Write-Host "         - $($link2.DisplayName) (Order: $($link2.Order))" -ForegroundColor Cyan
    $score++
} else {
    Write-Host "  [FAIL] Mot trong hai GPO chua duoc link vao Domain Root!" -ForegroundColor Red
}

# ------------------------------------------------------------------------------
# 3. KIỂM TRA CHI TIẾT CÁC THIẾT LẬP CHÍNH SÁCH TRONG GPO 'Remove Recycle Bin'
# ------------------------------------------------------------------------------
Write-Host "`n3. KIEM TRA GIA TRI CHINH SACH (REGISTRY POLICY SETTINGS):" -ForegroundColor Yellow

# 3.1. Desktop Icons: Computer & Recycle Bin
$nonEnum = Get-GPRegistryValue -Name "Remove Recycle Bin" -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\NonEnum" -ErrorAction SilentlyContinue
$cIcon = $nonEnum | Where-Object { $_.ValueName -eq "{20D04FE0-3AEA-1069-A2D8-08002B30309D}" -and $_.Value -eq 1 }
$rIcon = $nonEnum | Where-Object { $_.ValueName -eq "{645FF040-5081-101B-9F08-00AA002F954E}" -and $_.Value -eq 1 }

if ($cIcon -and $rIcon) {
    Write-Host "  [PASS] 1. An icon Desktop: Computer & Recycle Bin da duoc cau hinh (Value=1)." -ForegroundColor Green
    $score++
} else {
    Write-Host "  [FAIL] 1. Thieu cau hinh an Computer hoac Recycle Bin tren Desktop!" -ForegroundColor Red
}

# 3.2. Control Panel: Mouse
$expl = Get-GPRegistryValue -Name "Remove Recycle Bin" -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" -ErrorAction SilentlyContinue
$disCpl = Get-GPRegistryValue -Name "Remove Recycle Bin" -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowCpl" -ErrorAction SilentlyContinue
$hasDisCpl = $expl | Where-Object { $_.ValueName -eq "DisallowCpl" -and $_.Value -eq 1 }
$hasMouse = $disCpl | Where-Object { $_.Value -match "Microsoft.Mouse" }

if ($hasDisCpl -and $hasMouse) {
    Write-Host "  [PASS] 2. An item Control Panel: Da an 'Microsoft.Mouse' thanh cong." -ForegroundColor Green
    $score++
} else {
    Write-Host "  [FAIL] 2. Chua cau hinh dung DisallowCpl hoac Microsoft.Mouse!" -ForegroundColor Red
}

# 3.3. Personalization: Prevent changing theme
$noTheme = $expl | Where-Object { $_.ValueName -eq "NoThemesTab" -and $_.Value -eq 1 }
if ($noTheme) {
    Write-Host "  [PASS] 3. Cam doi Theme: NoThemesTab da duoc kich hoat (Value=1)." -ForegroundColor Green
    $score++
} else {
    Write-Host "  [FAIL] 3. Chua cau hinh Prevent changing theme!" -ForegroundColor Red
}

# 3.4. Network Connections: Prohibit LAN properties
$netConn = Get-GPRegistryValue -Name "Remove Recycle Bin" -Key "HKCU\Software\Policies\Microsoft\Windows\Network Connections" -ErrorAction SilentlyContinue
$noLanProp = $netConn | Where-Object { $_.ValueName -eq "NC_LanProperties" -and $_.Value -eq 0 }
if ($noLanProp) {
    Write-Host "  [PASS] 4. Khong cho sua IP: NC_LanProperties da duoc cau hinh (Value=0 - Prohibited)." -ForegroundColor Green
    $score++
} else {
    Write-Host "  [FAIL] 4. Chua cau hinh Prohibit access to properties of a LAN connection!" -ForegroundColor Red
}

# 3.5. Taskbar: Lock the Taskbar
$lockTask = $expl | Where-Object { ($_.ValueName -eq "TaskbarLockAll" -or $_.ValueName -eq "LockTaskbar") -and $_.Value -eq 1 }
if ($lockTask) {
    Write-Host "  [PASS] 5. Khoa Taskbar: TaskbarLockAll / LockTaskbar da duoc kich hoat (Value=1)." -ForegroundColor Green
    $score++
} else {
    Write-Host "  [FAIL] 5. Chua cau hinh Lock the Taskbar!" -ForegroundColor Red
}

# 3.6. System: DisableCMD & DisallowRun mspaint.exe
$sysPol = Get-GPRegistryValue -Name "Remove Recycle Bin" -Key "HKCU\Software\Policies\Microsoft\Windows\System" -ErrorAction SilentlyContinue
$disCmd = $sysPol | Where-Object { $_.ValueName -eq "DisableCMD" -and ($_.Value -eq 1 -or $_.Value -eq 2) }
$disRun = Get-GPRegistryValue -Name "Remove Recycle Bin" -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun" -ErrorAction SilentlyContinue
$paintBlocked = $disRun | Where-Object { $_.Value -match "mspaint.exe" }

if ($disCmd -and $paintBlocked) {
    Write-Host "  [PASS] 6. Chan ung dung: Da chan CMD (DisableCMD) va chan Paint (mspaint.exe)." -ForegroundColor Green
    $score++
} else {
    Write-Host "  [FAIL] 6. Chua chan thanh cong CMD hoac Paint!" -ForegroundColor Red
}

# ------------------------------------------------------------------------------
# 4. KIỂM TRA GPO LOGON SCRIPT TRONG SYSVOL
# ------------------------------------------------------------------------------
Write-Host "`n4. KIEM TRA TEP KICH BAN LOGON SCRIPT TRONG SYSVOL:" -ForegroundColor Yellow
$guid2 = $gpo2.Id.ToString("B").ToUpper()
$sysvolLogon = "C:\Windows\SYSVOL\sysvol\$domain\Policies\$guid2\User\Scripts\Logon\welcome.vbs"
$sysvolIni = "C:\Windows\SYSVOL\sysvol\$domain\Policies\$guid2\User\Scripts\scripts.ini"

if ((Test-Path $sysvolLogon) -and (Test-Path $sysvolIni)) {
    $scriptContent = Get-Content $sysvolLogon -Raw
    Write-Host "  [PASS] 7. Tep kịch bản welcome.vbs ton tai trong SYSVOL:" -ForegroundColor Green
    Write-Host "         -> Noi dung: $scriptContent" -ForegroundColor Cyan
    $score++
} else {
    Write-Host "  [FAIL] 7. Khong tim thay welcome.vbs hoac scripts.ini trong SYSVOL cua GPO!" -ForegroundColor Red
}

# ------------------------------------------------------------------------------
# 5. TỔNG KẾT KẾT QUẢ NGHIỆM THU
# ------------------------------------------------------------------------------
Write-Host "`n==========================================================================" -ForegroundColor Cyan
$percent = [math]::Round(($score / $totalTests) * 100, 1)
$resultColor = if ($score -eq $totalTests) { "Green" } else { "Yellow" }
Write-Host "   KET QUA DANH GIA NGHIEM THU LAB 6: $score / $totalTests TIEU CHI DAT ($percent%)" -ForegroundColor $resultColor
Write-Host "==========================================================================" -ForegroundColor Cyan

if ($score -eq $totalTests) {
    Write-Host "[PASS] CHUC MUNG! HE THONG LAB 6 GPO DA DAT 100% TAT CA CAC TIEU CHI DE BAI!" -ForegroundColor Green
} else {
    Write-Host "[!] MOT SO TIEU CHI CHUA HOAN TAT, HAY KIEM TRA LAI CAC MUC [FAIL]." -ForegroundColor Red
}
