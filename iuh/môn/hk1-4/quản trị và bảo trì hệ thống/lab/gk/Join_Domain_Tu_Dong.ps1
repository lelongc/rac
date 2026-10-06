<#
================================================================================
KỊCH BẢN TỰ ĐỘNG GIA NHẬP DOMAIN CHO 3 MÁY PHÒNG THI QTBTHT
Mặc định: Domain fit.iuh.edu.vn (Có thể đổi linh hoạt bằng tham số)
Hỗ trợ: Giữ nguyên Domain hoạt động bình thường khi đổi dải IP
================================================================================
#>

[CmdletBinding()]
param(
    [string]$DomainName = "fit.iuh.edu.vn",
    [string]$NetbiosName = "FIT",
    [string]$AdminPass = "123",
    [string]$DsrmPass = "Admin@123",
    [string]$ServerHost = "192.168.1.151",
    [string]$ServerIP_VMnet11 = "192.168.11.1",
    [string]$ServerIP_VMnet12 = "100.100.11.1",
    [string]$Client1IP = "192.168.11.2",
    [string]$Client2IP = "100.100.11.2"
)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ErrorActionPreference = "Continue"

$secPass = ConvertTo-SecureString $AdminPass -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $secPass)

Write-Host "=================================================================" -ForegroundColor Yellow
Write-Host "   QUÁ TRÌNH THIẾT LẬP VÀ GIA NHẬP DOMAIN $DomainName           " -ForegroundColor Yellow
Write-Host "=================================================================" -ForegroundColor Yellow

# ------------------------------------------------------------------------------
# BƯỚC 1: KIỂM TRA VÀ NÂNG CẤP SERVER 1 THÀNH DOMAIN CONTROLLER (DC)
# ------------------------------------------------------------------------------
Write-Host "`n[1/5] Kiểm tra trạng thái Domain Controller trên Server 1..." -ForegroundColor Cyan

$isDC = Invoke-Command -ComputerName $ServerHost -Credential $cred -ScriptBlock {
    (Get-CimInstance Win32_OperatingSystem).ProductType -eq 2
}

if (-not $isDC) {
    Write-Host " -> Server 1 chưa phải là DC. Bắt đầu cài đặt AD DS và nâng cấp Domain..." -ForegroundColor Yellow
    
    # Cài đặt tính năng AD DS nếu chưa có
    Invoke-Command -ComputerName $ServerHost -Credential $cred -ScriptBlock {
        if (-not (Get-WindowsFeature AD-Domain-Services).Installed) {
            Write-Host "    * Đang cài đặt Windows Feature AD-Domain-Services..."
            Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools | Out-Null
        }
    }

    # Nâng cấp thành DC
    Write-Host " -> Đang khởi tạo Forest mới: $DomainName (NetBIOS: $NetbiosName)..." -ForegroundColor Cyan
    Invoke-Command -ComputerName $ServerHost -Credential $cred -ScriptBlock {
        param($dName, $nbName, $dsrm)
        Import-Module ADDSDeployment
        $secDsrm = ConvertTo-SecureString $dsrm -AsPlainText -Force
        
        Install-ADDSForest -DomainName $dName `
                           -DomainNetbiosName $nbName `
                           -DomainMode "Win2012R2" `
                           -ForestMode "Win2012R2" `
                           -InstallDns:$true `
                           -SafeModeAdministratorPassword $secDsrm `
                           -Force:$true
    } -ArgumentList $DomainName, $NetbiosName, $DsrmPass

    Write-Host " -> Server 1 đang tự động khởi động lại sau khi nâng cấp DC." -ForegroundColor Yellow
    Write-Host " -> Đang chờ Server 1 khởi động lại hoàn tất (khoảng 60-90 giây)..." -ForegroundColor Gray
    
    Start-Sleep -Seconds 20
    $online = $false
    for ($i = 1; $i -le 40; $i++) {
        if (Test-Connection -ComputerName $ServerHost -Count 1 -Quiet) {
            try {
                $check = Invoke-Command -ComputerName $ServerHost -Credential $cred -ScriptBlock { hostname } -ErrorAction Stop
                if ($check) {
                    $online = $true
                    Write-Host " -> Server 1 đã khởi động lại và WinRM đã sẵn sàng!" -ForegroundColor Green
                    break
                }
            } catch {
                # Chờ dịch vụ WinRM khởi động xong
            }
        }
        Write-Host "    ... Đang chờ Server 1 khởi động lại ($($i * 5)s)" -ForegroundColor Gray
        Start-Sleep -Seconds 5
    }

    if (-not $online) {
        Write-Host " [X] Lỗi: Server 1 mất kết nối quá lâu. Vui lòng kiểm tra lại VM Server." -ForegroundColor Red
        return
    }
} else {
    Write-Host " -> Server 1 đã là Domain Controller!" -ForegroundColor Green
}

# ------------------------------------------------------------------------------
# BƯỚC 2: CẤU HÌNH DNS TRÊN SERVER 1 ĐỂ SẴN SÀNG PHỤC VỤ CLIENTS
# ------------------------------------------------------------------------------
Write-Host "`n[2/5] Đảm bảo cấu hình DNS trên Server 1..." -ForegroundColor Cyan
Invoke-Command -ComputerName $ServerHost -Credential $cred -ScriptBlock {
    param($sip11, $sip12)
    # Trỏ DNS card vmnet11 và vmnet12 về 127.0.0.1
    netsh interface ip set dns name="vmnet11" static 127.0.0.1
    netsh interface ip set dns name="vmnet12" static 127.0.0.1
    ipconfig /registerdns
    Write-Host "    * Đã đăng ký bản ghi DNS và trỏ DNS nội bộ của Server."
} -ArgumentList $ServerIP_VMnet11, $ServerIP_VMnet12

# ------------------------------------------------------------------------------
# BƯỚC 3: CẤU HÌNH CLIENT 1 VÀ GIA NHẬP DOMAIN
# ------------------------------------------------------------------------------
Write-Host "`n[3/5] Cấu hình Client 1 ($Client1IP) gia nhập Domain $DomainName..." -ForegroundColor Cyan

# Trỏ DNS Client 1 về Server 1 (vmnet11)
Invoke-Command -ComputerName $Client1IP -Credential $cred -ScriptBlock {
    param($dnsServer)
    $nic = (Get-NetAdapter | Where-Object { $_.Status -eq "Up" } | Select-Object -First 1).Name
    if (-not $nic) { $nic = "Local Area Connection 2" }
    netsh interface ip set dns name="$nic" static $dnsServer
    ipconfig /flushdns
    Write-Host "    * Client 1 đã trỏ DNS về: $dnsServer"
} -ArgumentList $ServerIP_VMnet11

# Join Domain Client 1
$c1Joined = Invoke-Command -ComputerName $Client1IP -Credential $cred -ScriptBlock {
    param($dName, $pwd)
    $domainUser = "$dName\Administrator"
    $secP = ConvertTo-SecureString $pwd -AsPlainText -Force
    $dCred = New-Object System.Management.Automation.PSCredential($domainUser, $secP)
    
    $currentDomain = (Get-WmiObject Win32_ComputerSystem).Domain
    if ($currentDomain -eq $dName) {
        return "ALREADY_JOINED"
    }

    try {
        Add-Computer -DomainName $dName -Credential $dCred -Restart -Force -ErrorAction Stop
        return "SUCCESS"
    } catch {
        return "ERROR: " + $_.Exception.Message
    }
} -ArgumentList $DomainName, $AdminPass

Write-Host " -> Kết quả Join Domain Client 1: $c1Joined" -ForegroundColor Green

# ------------------------------------------------------------------------------
# BƯỚC 4: CẤU HÌNH CLIENT 2 VÀ GIA NHẬP DOMAIN
# ------------------------------------------------------------------------------
Write-Host "`n[4/5] Cấu hình Client 2 ($Client2IP) gia nhập Domain $DomainName..." -ForegroundColor Cyan

# Trỏ DNS Client 2 về Server 1 (vmnet12)
Invoke-Command -ComputerName $Client2IP -Credential $cred -ScriptBlock {
    param($dnsServer)
    $nic = (Get-NetAdapter | Where-Object { $_.Status -eq "Up" } | Select-Object -First 1).Name
    if (-not $nic) { $nic = "Local Area Connection" }
    netsh interface ip set dns name="$nic" static $dnsServer
    ipconfig /flushdns
    Write-Host "    * Client 2 đã trỏ DNS về: $dnsServer"
} -ArgumentList $ServerIP_VMnet12

# Join Domain Client 2
$c2Joined = Invoke-Command -ComputerName $Client2IP -Credential $cred -ScriptBlock {
    param($dName, $pwd)
    $domainUser = "$dName\Administrator"
    $secP = ConvertTo-SecureString $pwd -AsPlainText -Force
    $dCred = New-Object System.Management.Automation.PSCredential($domainUser, $secP)
    
    $currentDomain = (Get-WmiObject Win32_ComputerSystem).Domain
    if ($currentDomain -eq $dName) {
        return "ALREADY_JOINED"
    }

    try {
        Add-Computer -DomainName $dName -Credential $dCred -Restart -Force -ErrorAction Stop
        return "SUCCESS"
    } catch {
        return "ERROR: " + $_.Exception.Message
    }
} -ArgumentList $DomainName, $AdminPass

Write-Host " -> Kết quả Join Domain Client 2: $c2Joined" -ForegroundColor Green

# ------------------------------------------------------------------------------
# BƯỚC 5: CHỜ CÁC CLIENT KHỞI ĐỘNG LẠI VÀ KIỂM TRA NGHIỆM THU
# ------------------------------------------------------------------------------
Write-Host "`n[5/5] Kiểm tra nghiệm thu sau khi hoàn tất..." -ForegroundColor Cyan
Write-Host " -> Đang chờ các Client khởi động lại (30 giây)..." -ForegroundColor Gray
Start-Sleep -Seconds 30

# Chờ Client 1 online
for ($j = 1; $j -le 20; $j++) {
    if (Test-Connection -ComputerName $Client1IP -Count 1 -Quiet) {
        try {
            $dom1 = Invoke-Command -ComputerName $Client1IP -Credential $cred -ScriptBlock { (Get-WmiObject Win32_ComputerSystem).Domain } -ErrorAction Stop
            Write-Host "  [+] Client 1 ($Client1IP) đã online! Domain hiện tại: $dom1" -ForegroundColor Green
            break
        } catch {}
    }
    Start-Sleep -Seconds 3
}

# Chờ Client 2 online
for ($k = 1; $k -le 20; $k++) {
    if (Test-Connection -ComputerName $Client2IP -Count 1 -Quiet) {
        try {
            $dom2 = Invoke-Command -ComputerName $Client2IP -Credential $cred -ScriptBlock { (Get-WmiObject Win32_ComputerSystem).Domain } -ErrorAction Stop
            Write-Host "  [+] Client 2 ($Client2IP) đã online! Domain hiện tại: $dom2" -ForegroundColor Green
            break
        } catch {}
    }
    Start-Sleep -Seconds 3
}

Write-Host "`n=================================================================" -ForegroundColor Yellow
Write-Host "     HOÀN TẤT THIẾT LẬP DOMAIN CHO TOÀN BỘ 3 MÁY!                " -ForegroundColor Yellow
Write-Host "=================================================================" -ForegroundColor Yellow
