$pass = "123"
$secPass = ConvertTo-SecureString $pass -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $secPass)

Write-Host "========================================================" -ForegroundColor Yellow
Write-Host "   KIỂM TRA KẾT NỐI & REMOTE 3 MÁY PHÒNG THI QTBTHT     " -ForegroundColor Yellow
Write-Host "========================================================" -ForegroundColor Yellow

# 1. KET NOI SERVER 1
Write-Host "`n[1] Ket noi vao SERVER 1 (192.168.1.151)..." -ForegroundColor Cyan
try {
    $sInfo = Invoke-Command -ComputerName "192.168.1.151" -Credential $cred -ScriptBlock {
        $h = hostname
        $ip = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.IPAddress -notlike "127.*" }).IPAddress -join ", "
        "$h (IPs: $ip)"
    } -ErrorAction Stop
    Write-Host "  -> SUCCESS! Server 1 da ket noi duoc: $sInfo" -ForegroundColor Green
} catch {
    Write-Host "  -> FAILED Server 1: $_" -ForegroundColor Red
}

# 2. TEST PING TU SERVER SANG CLIENT 1 VA CLIENT 2
Write-Host "`n[2] Tu Server 1 test Ping sang Client 1 va Client 2..." -ForegroundColor Cyan
Invoke-Command -ComputerName "192.168.1.151" -Credential $cred -ScriptBlock {
    Write-Host "  * Server ping sang Client 1 (192.168.11.2):"
    ping 192.168.11.2 -n 2 | Out-Host
    
    Write-Host "  * Server ping sang Client 2 (100.100.11.2):"
    ping 100.100.11.2 -n 2 | Out-Host
}

# 3. KET NOI CLIENT 1
Write-Host "`n[3] Ket noi vao CLIENT 1 (192.168.11.2)..." -ForegroundColor Cyan
try {
    $c1Info = Invoke-Command -ComputerName "192.168.11.2" -Credential $cred -ScriptBlock {
        $h = hostname
        $pingS = ping 192.168.11.1 -n 2
        "$h -> Ping ve Server 1: " + ($pingS -match "TTL=").Count + " replies"
    } -ErrorAction Stop
    Write-Host "  -> SUCCESS! Client 1 da ket noi duoc: $c1Info" -ForegroundColor Green
} catch {
    Write-Host "  -> FAILED Client 1: $_" -ForegroundColor Red
}

# 4. KET NOI CLIENT 2
Write-Host "`n[4] Ket noi vao CLIENT 2 (100.100.11.2)..." -ForegroundColor Cyan
try {
    $c2Info = Invoke-Command -ComputerName "100.100.11.2" -Credential $cred -ScriptBlock {
        $h = hostname
        $pingS = ping 100.100.11.1 -n 2
        "$h -> Ping ve Server 1: " + ($pingS -match "TTL=").Count + " replies"
    } -ErrorAction Stop
    Write-Host "  -> SUCCESS! Client 2 da ket noi duoc: $c2Info" -ForegroundColor Green
} catch {
    Write-Host "  -> Chu y Client 2 WinRM: $_" -ForegroundColor Yellow
    # Thu kiem tra Ping tu Host den Client 2
    $p2 = Test-Connection -ComputerName 100.100.11.2 -Count 2 -Quiet
    if ($p2) {
        Write-Host "  -> Tuy nhien PING tu Host sang Client 2: THANH CONG (Thong mang 100%)!" -ForegroundColor Green
    }
}
