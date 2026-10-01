<#
================================================================================
TOOL CHUI VÀO ĐỔI IP TỰ ĐỘNG THEO ĐỀ BÀI THI GIỮA KỲ QTBTHT
Chạy trực tiếp từ Host hoặc từ Server để điều khiển toàn bộ phòng máy
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
    Write-Host "        TOOL ĐỔI IP TỰ ĐỘNG THEO ĐỀ THI GIỮA KỲ QTBTHT          " -ForegroundColor Yellow
    Write-Host "=================================================================" -ForegroundColor Yellow
    Write-Host " [1] Đề minh họa DHTH18      -> Server: 192.168.1.1  | Client 1: 192.168.1.2" -ForegroundColor Cyan
    Write-Host " [2] Đề File Server Cty ABC  -> Server: 172.16.10.1 | Client 1: 172.16.10.2" -ForegroundColor Cyan
    Write-Host " [3] Đề bài Lab 7 cũ         -> Server: 192.168.11.1 | Client 1: 192.168.11.2" -ForegroundColor Cyan
    Write-Host " [4] Tùy chỉnh Subnet mới    -> Nhập tiền tố mạng (ví dụ 10.0.1.)" -ForegroundColor Cyan
    Write-Host " [5] Chỉ kiểm tra PING thông mạng hiện tại giữa Server và Client 1" -ForegroundColor Green
    Write-Host " [0] Thoát" -ForegroundColor Gray
    Write-Host "=================================================================" -ForegroundColor Yellow
}

function Apply-IPChange($serverIP, $clientIP, $subnetMask = "255.255.255.0") {
    Write-Host "`n[*] Đang chui vào SERVER ($serverHost) để tìm IP hiện tại của Client 1..." -ForegroundColor Cyan
    
    # Tìm IP hiện tại của Client 1 từ Server
    $currentClientIP = Invoke-Command -ComputerName $serverHost -Credential $cred -ScriptBlock {
        # Quét nhanh arp hoặc lấy IP vmnet11
        $currentSubnet = (Get-NetIPAddress -InterfaceAlias "vmnet11" -AddressFamily IPv4).IPAddress
        return $currentSubnet
    }
    Write-Host " -> Subnet hiện tại trên vmnet11 của Server: $currentClientIP" -ForegroundColor Gray

    # Danh sách các IP Client 1 có thể đang giữ
    $possibleClientIPs = @("172.16.10.2", "192.168.11.2", "192.168.1.2")
    $targetClient = $null

    foreach ($ip in $possibleClientIPs) {
        $p = Invoke-Command -ComputerName $serverHost -Credential $cred -ScriptBlock {
            param($target)
            Test-Connection -ComputerName $target -Count 1 -Quiet
        } -ArgumentList $ip

        if ($p) {
            $targetClient = $ip
            break
        }
    }

    if (-not $targetClient) {
        # Nếu chưa tìm ra qua Server, thử ping từ host
        foreach ($ip in $possibleClientIPs) {
            if (Test-Connection -ComputerName $ip -Count 1 -Quiet) {
                $targetClient = $ip
                break
            }
        }
    }

    if ($targetClient) {
        Write-Host " -> Đã phát hiện Client 1 đang hoạt động tại IP: $targetClient" -ForegroundColor Green
        Write-Host "[*] Đang chui vào Client 1 ($targetClient) để đổi sang IP mới: $clientIP ..." -ForegroundColor Cyan
        
        try {
            $cmd = "cmd.exe /c netsh interface ip set address name=""Local Area Connection 2"" static $clientIP $subnetMask $serverIP & netsh interface ip set dns name=""Local Area Connection 2"" static $serverIP & netsh advfirewall set allprofiles state off"
            Invoke-Command -ComputerName $targetClient -Credential $cred -ScriptBlock {
                param($command)
                ([wmiclass]"Win32_Process").Create($command) | Out-Null
            } -ArgumentList $cmd
            Write-Host " -> Đã gửi lệnh cấu hình IP mới thành công cho Client 1!" -ForegroundColor Green
        } catch {
            Write-Host " -> Lưu ý: $($_)" -ForegroundColor Yellow
        }
    } else {
        Write-Host " [!] Cảnh báo: Chưa dò thấy Client 1 qua ping. Sẽ đổi IP trên Server trước." -ForegroundColor Yellow
    }

    Write-Host "`n[*] Đang chui vào SERVER để cập nhật card vmnet11 sang IP: $serverIP ..." -ForegroundColor Cyan
    Invoke-Command -ComputerName $serverHost -Credential $cred -ScriptBlock {
        param($sip, $mask)
        netsh interface ip set address "vmnet11" static $sip $mask
        netsh advfirewall set allprofiles state off
        Get-NetIPAddress -InterfaceAlias "vmnet11" -AddressFamily IPv4 | Select-Object -ExpandProperty IPAddress
    } -ArgumentList $serverIP, $subnetMask

    Write-Host " -> Đang chờ card mạng áp dụng (3 giây)..." -ForegroundColor Gray
    Start-Sleep -Seconds 3

    Write-Host "`n[*] Kiểm tra TEST PING từ Server sang Client 1 ($clientIP)..." -ForegroundColor Cyan
    $pingResult = Invoke-Command -ComputerName $serverHost -Credential $cred -ScriptBlock {
        param($cip)
        ping $cip -n 4
    } -ArgumentList $clientIP

    $pingResult | Out-Host

    if ($pingResult -match "TTL=") {
        Write-Host "`n=================================================================" -ForegroundColor Green
        Write-Host " [THÀNH CÔNG] ĐÃ ĐỔI IP VÀ PING THÔNG 100% GIỮA SERVER VÀ CLIENT!" -ForegroundColor Green
        Write-Host "   - Server IP : $serverIP" -ForegroundColor Green
        Write-Host "   - Client IP : $clientIP" -ForegroundColor Green
        Write-Host "=================================================================" -ForegroundColor Green
    } else {
        Write-Host "`n[!] Ping chưa có phản hồi ngay. Hãy mở màn hình Client 1 gõ 'ping $serverIP' để kiểm tra." -ForegroundColor Yellow
    }
}

# VÒNG LẶP MENU
do {
    Show-Menu
    $choice = Read-Host "Nhập lựa chọn của bạn [1-5, 0]"
    switch ($choice) {
        "1" {
            Apply-IPChange -serverIP "192.168.1.1" -clientIP "192.168.1.2"
            Pause
        }
        "2" {
            Apply-IPChange -serverIP "172.16.10.1" -clientIP "172.16.10.2"
            Pause
        }
        "3" {
            Apply-IPChange -serverIP "192.168.11.1" -clientIP "192.168.11.2"
            Pause
        }
        "4" {
            $prefix = Read-Host "Nhập tiền tố IP (ví dụ: 10.0.1. hoặc 192.168.50.): "
            if ($prefix -match "\.$") {
                $sip = "${prefix}1"
                $cip = "${prefix}2"
                Apply-IPChange -serverIP $sip -clientIP $cip
            } else {
                Write-Host "Định dạng không hợp lệ! Phải kết thúc bằng dấu chấm (ví dụ: 10.0.1.)" -ForegroundColor Red
            }
            Pause
        }
        "5" {
            Write-Host "`n[*] Kiểm tra PING từ Server sang các dải..." -ForegroundColor Cyan
            Invoke-Command -ComputerName $serverHost -Credential $cred -ScriptBlock {
                Write-Host "--- IP Card vmnet11 hiện tại trên Server ---"
                Get-NetIPAddress -InterfaceAlias "vmnet11" -AddressFamily IPv4 | Format-Table IPAddress, InterfaceAlias
                Write-Host "--- Ping thử 172.16.10.2 ---"
                ping 172.16.10.2 -n 2
                Write-Host "--- Ping thử 192.168.1.2 ---"
                ping 192.168.1.2 -n 2
                Write-Host "--- Ping thử 192.168.11.2 ---"
                ping 192.168.11.2 -n 2
            } | Out-Host
            Pause
        }
    }
} while ($choice -ne "0")
