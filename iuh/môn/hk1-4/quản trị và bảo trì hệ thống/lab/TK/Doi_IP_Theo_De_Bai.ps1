<#
================================================================================
TOOL CHUI VÀO ĐỔI IP TỰ ĐỘNG THEO ĐỀ BÀI THI GIỮA KỲ QTBTHT
Tự động đồng bộ và giữ vững Domain (fit.iuh.edu.vn) cho cả Server, Client 1 và Client 2
================================================================================
#>

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Clear-Host

$serverHost = "192.168.1.151"
$pass = "123"
$secPass = ConvertTo-SecureString $pass -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $secPass)

function Show-Menu {
    Write-Host "=================================================================" -ForegroundColor Yellow
    Write-Host "        TOOL ĐỔI IP TỰ ĐỘNG & ĐỒNG BỘ DOMAIN GIỮA KỲ QTBTHT       " -ForegroundColor Yellow
    Write-Host "=================================================================" -ForegroundColor Yellow
    Write-Host " [1] Đề 1 (Chuẩn Lab 7)      -> Server: 192.168.11.1 | C1: 192.168.11.2 | C2: 100.100.11.2" -ForegroundColor Cyan
    Write-Host " [2] Đề File Server Cty ABC  -> Server: 172.16.10.1  | C1: 172.16.10.2  | C2: 100.100.11.2" -ForegroundColor Cyan
    Write-Host " [3] Đề DHTH18 (Dải 192.168) -> Server: 192.168.1.1   | C1: 192.168.1.2   | C2: 100.100.11.2" -ForegroundColor Cyan
    Write-Host " [4] Tùy chỉnh Subnet mới    -> Nhập Subnet cho C1 và C2" -ForegroundColor Cyan
    Write-Host " [5] Kiểm tra PING và Kênh bảo mật Domain (Secure Channel) 3 máy" -ForegroundColor Green
    Write-Host " [0] Thoát" -ForegroundColor Gray
    Write-Host "=================================================================" -ForegroundColor Yellow
}

function Apply-FullIPChange($sIpC1, $c1Ip, $sIpC2 = "100.100.11.1", $c2Ip = "100.100.11.2", $mask = "255.255.255.0") {
    Write-Host "`n=================================================================" -ForegroundColor Cyan
    Write-Host "   BẮT ĐẦU ĐỔI IP & ĐỒNG BỘ DOMAIN CONTROLLER FIT.IUH.EDU.VN    " -ForegroundColor Cyan
    Write-Host "=================================================================" -ForegroundColor Cyan
    Write-Host " [*] Cấu hình mới:" -ForegroundColor Yellow
    Write-Host "     + Server 1 (Card vmnet11 - C1) : $sIpC1" -ForegroundColor Yellow
    Write-Host "     + Client 1                    : $c1Ip" -ForegroundColor Yellow
    Write-Host "     + Server 1 (Card vmnet12 - C2) : $sIpC2" -ForegroundColor Yellow
    Write-Host "     + Client 2                    : $c2Ip" -ForegroundColor Yellow

    # 1. DÒ TÌM IP HIỆN TẠI CỦA CLIENT 1 VÀ CLIENT 2
    Write-Host "`n[1/4] Dò tìm IP hiện tại của Client 1 và Client 2..." -ForegroundColor Cyan
    $possibleIPsC1 = @("192.168.11.2", "172.16.10.2", "192.168.1.2", $c1Ip)
    $targetC1 = $null
    foreach ($ip in $possibleIPsC1) {
        if (Test-Connection -ComputerName $ip -Count 1 -Quiet) {
            $targetC1 = $ip
            break
        }
    }
    if ($targetC1) { Write-Host " -> Client 1 đang ở IP: $targetC1" -ForegroundColor Green }
    else { Write-Host " -> Chưa ping thấy Client 1 (sẽ gửi lệnh cấu hình sau khi đổi IP Server)" -ForegroundColor Yellow }

    $possibleIPsC2 = @("100.100.11.2", $c2Ip)
    $targetC2 = $null
    foreach ($ip in $possibleIPsC2) {
        if (Test-Connection -ComputerName $ip -Count 1 -Quiet) {
            $targetC2 = $ip
            break
        }
    }
    if ($targetC2) { Write-Host " -> Client 2 đang ở IP: $targetC2" -ForegroundColor Green }

    # 2. ĐỔI IP TRÊN CLIENT 1 VÀ CLIENT 2 (NẾU ĐANG KẾT NỐI ĐƯỢC)
    if ($targetC1) {
        Write-Host "`n[2/4] Gửi lệnh đổi IP & trỏ DNS về Server cho Client 1 ($targetC1 -> $c1Ip)..." -ForegroundColor Cyan
        try {
            $cmd1 = "cmd.exe /c netsh interface ip set address name=""Local Area Connection 2"" static $c1Ip $mask $sIpC1 & netsh interface ip set dns name=""Local Area Connection 2"" static $sIpC1 & ipconfig /flushdns & ipconfig /registerdns & netsh advfirewall set allprofiles state off"
            Invoke-Command -ComputerName $targetC1 -Credential $cred -ScriptBlock {
                param($command)
                ([wmiclass]"Win32_Process").Create($command) | Out-Null
            } -ArgumentList $cmd1
            Write-Host " -> Đã gửi lệnh thành công cho Client 1!" -ForegroundColor Green
        } catch {
            Write-Host " -> Lưu ý gửi lệnh Client 1: $_" -ForegroundColor Yellow
        }
    }

    if ($targetC2) {
        Write-Host "`n[2/4b] Gửi lệnh đổi IP & trỏ DNS về Server cho Client 2 ($targetC2 -> $c2Ip)..." -ForegroundColor Cyan
        try {
            $cmd2 = "cmd.exe /c netsh interface ip set address name=""Local Area Connection"" static $c2Ip $mask $sIpC2 & netsh interface ip set dns name=""Local Area Connection"" static $sIpC2 & ipconfig /flushdns & ipconfig /registerdns & netsh advfirewall set allprofiles state off"
            Invoke-Command -ComputerName $targetC2 -Credential $cred -ScriptBlock {
                param($command)
                ([wmiclass]"Win32_Process").Create($command) | Out-Null
            } -ArgumentList $cmd2
            Write-Host " -> Đã gửi lệnh thành công cho Client 2!" -ForegroundColor Green
        } catch {
            Write-Host " -> Lưu ý gửi lệnh Client 2: $_" -ForegroundColor Yellow
        }
    }

    # 3. ĐỔI IP VÀ CẬP NHẬT DNS SERVER TRÊN SERVER 1
    Write-Host "`n[3/4] Cập nhật IP và DNS Server trên Server 1..." -ForegroundColor Cyan
    Invoke-Command -ComputerName $serverHost -Credential $cred -ScriptBlock {
        param($sip1, $sip2, $m)
        # Cập nhật card vmnet11
        netsh interface ip set address "vmnet11" static $sip1 $m
        netsh interface ip set dns "vmnet11" static 127.0.0.1
        
        # Cập nhật card vmnet12
        netsh interface ip set address "vmnet12" static $sip2 $m
        netsh interface ip set dns "vmnet12" static 127.0.0.1
        
        # Tắt tường lửa & đăng ký lại DNS trong AD
        netsh advfirewall set allprofiles state off
        ipconfig /registerdns
        nltest /dsregdns | Out-Null
        
        Write-Host "    * Đã áp dụng IP $sip1 (vmnet11) và $sip2 (vmnet12) trên Server 1!"
    } -ArgumentList $sIpC1, $sIpC2, $mask

    Write-Host " -> Đang chờ các card mạng ổn định (5 giây)..." -ForegroundColor Gray
    Start-Sleep -Seconds 5

    # 4. KIỂM TRA PING VÀ XÁC NHẬN DOMAIN
    Write-Host "`n[4/4] Kiểm tra PING và Kênh kết nối Domain..." -ForegroundColor Cyan
    $pingTest = Invoke-Command -ComputerName $serverHost -Credential $cred -ScriptBlock {
        param($c1, $c2)
        $p1 = ping $c1 -n 2
        $p2 = ping $c2 -n 2
        [PSCustomObject]@{
            PingClient1 = ($p1 -match "TTL=").Count -gt 0
            PingClient2 = ($p2 -match "TTL=").Count -gt 0
        }
    } -ArgumentList $c1Ip, $c2Ip

    Write-Host "  * Ping Server -> Client 1 ($c1Ip): $(if($pingTest.PingClient1){'THÀNH CÔNG'}else{'CHƯA THÔNG'})" -ForegroundColor $(if($pingTest.PingClient1){'Green'}else{'Yellow'})
    Write-Host "  * Ping Server -> Client 2 ($c2Ip): $(if($pingTest.PingClient2){'THÀNH CÔNG'}else{'CHƯA THÔNG'})" -ForegroundColor $(if($pingTest.PingClient2){'Green'}else{'Yellow'})

    # Kiểm tra Secure Channel từ Client về DC
    try {
        $sc1 = Invoke-Command -ComputerName $c1Ip -Credential $cred -ScriptBlock {
            Test-ComputerSecureChannel
        } -ErrorAction SilentlyContinue
        Write-Host "  * Kênh bảo mật Domain Client 1 -> DC: $(if($sc1){'KẾT NỐI TỐT (TRUE)'}else{'ĐANG CHỜ'})" -ForegroundColor Green
    } catch {}

    try {
        $sc2 = Invoke-Command -ComputerName $c2Ip -Credential $cred -ScriptBlock {
            Test-ComputerSecureChannel
        } -ErrorAction SilentlyContinue
        Write-Host "  * Kênh bảo mật Domain Client 2 -> DC: $(if($sc2){'KẾT NỐI TỐT (TRUE)'}else{'ĐANG CHỜ'})" -ForegroundColor Green
    } catch {}

    Write-Host "`n=================================================================" -ForegroundColor Green
    Write-Host " ĐÃ HOÀN TẤT ĐỔI IP VÀ ĐỒNG BỘ DOMAIN FIT.IUH.EDU.VN!" -ForegroundColor Green
    Write-Host "=================================================================" -ForegroundColor Green
}

# VÒNG LẶP MENU
do {
    Show-Menu
    $choice = Read-Host "Nhập lựa chọn của bạn [1-5, 0]"
    switch ($choice) {
        "1" {
            Apply-FullIPChange -sIpC1 "192.168.11.1" -c1Ip "192.168.11.2" -sIpC2 "100.100.11.1" -c2Ip "100.100.11.2"
            Pause
        }
        "2" {
            Apply-FullIPChange -sIpC1 "172.16.10.1" -c1Ip "172.16.10.2" -sIpC2 "100.100.11.1" -c2Ip "100.100.11.2"
            Pause
        }
        "3" {
            Apply-FullIPChange -sIpC1 "192.168.1.1" -c1Ip "192.168.1.2" -sIpC2 "100.100.11.1" -c2Ip "100.100.11.2"
            Pause
        }
        "4" {
            $s1 = Read-Host "Nhập IP Server cho nhánh Client 1 (ví dụ 10.0.1.1): "
            $c1 = Read-Host "Nhập IP Client 1 (ví dụ 10.0.1.2): "
            $s2 = Read-Host "Nhập IP Server cho nhánh Client 2 (mặc định 100.100.11.1): "
            if (-not $s2) { $s2 = "100.100.11.1" }
            $c2 = Read-Host "Nhập IP Client 2 (mặc định 100.100.11.2): "
            if (-not $c2) { $c2 = "100.100.11.2" }
            Apply-FullIPChange -sIpC1 $s1 -c1Ip $c1 -sIpC2 $s2 -c2Ip $c2
            Pause
        }
        "5" {
            Write-Host "`n[*] Đang kiểm tra PING và Kênh kết nối Domain..." -ForegroundColor Cyan
            & "$PSScriptRoot\test_connect_all_3.ps1"
            Pause
        }
    }
} while ($choice -ne "0")
