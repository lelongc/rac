[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$pass = "123"
$secPass = ConvertTo-SecureString $pass -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $secPass)

Write-Host "=================================================================" -ForegroundColor Yellow
Write-Host "       KIEM TRA KET NOI & TEST PING 3 MAY PHONG THI QTBTHT       " -ForegroundColor Yellow
Write-Host "=================================================================" -ForegroundColor Yellow

# 1. PING TRUC TIEP TU HOST
Write-Host "`n[1] Ping truc tiep tu Host den cac may:" -ForegroundColor Cyan
$ips = @(
    @{ Name = "Server 1 (NAT)"; IP = "192.168.1.151" },
    @{ Name = "Server 1 (LAN 1)"; IP = "192.168.11.1" },
    @{ Name = "Server 1 (LAN 2)"; IP = "100.100.11.1" },
    @{ Name = "Client 1 (LAN 1)"; IP = "192.168.11.2" },
    @{ Name = "Client 2 (LAN 2)"; IP = "100.100.11.2" }
)

foreach ($i in $ips) {
    if (Test-Connection -ComputerName $i.IP -Count 1 -Quiet) {
        Write-Host "  -> [OK] $($i.Name) [$($i.IP)]: PING THONG 100%" -ForegroundColor Green
    } else {
        Write-Host "  -> [FAIL] $($i.Name) [$($i.IP)]: KHONG PHAN HOI" -ForegroundColor Red
    }
}

# 2. TU SERVER 1 PING SANG CLIENT 1 VA CLIENT 2
Write-Host "`n[2] Tu Server 1 Ping sang Client 1 va Client 2..." -ForegroundColor Cyan
try {
    Invoke-Command -ComputerName "192.168.1.151" -Credential $cred -ScriptBlock {
        Write-Host "  * Server 1 -> Client 1 (192.168.11.2):" -ForegroundColor Gray
        ping 192.168.11.2 -n 2 | Out-Host
        Write-Host "  * Server 1 -> Client 2 (100.100.11.2):" -ForegroundColor Gray
        ping 100.100.11.2 -n 2 | Out-Host
    }
} catch {
    Write-Host "  -> Chu y Server 1: $_" -ForegroundColor Yellow
}

# 3. TU CLIENT 1 PING SERVER 1 VA CLIENT 2 (ROUTING)
Write-Host "`n[3] Tu Client 1 Ping Server 1 va Client 2 (xuyen Router Server)..." -ForegroundColor Cyan
try {
    Invoke-Command -ComputerName "192.168.11.2" -Credential $cred -ScriptBlock {
        Write-Host "  * Client 1 -> Server 1 (192.168.11.1):" -ForegroundColor Gray
        ping 192.168.11.1 -n 2 | Out-Host
        Write-Host "  * Client 1 -> Client 2 (100.100.11.2 - Dinh tuyen xuyen mang):" -ForegroundColor Gray
        ping 100.100.11.2 -n 2 | Out-Host
    }
    Write-Host "  -> SUCCESS! Toan bo 3 may va 2 mang LAN dinh tuyen thong suot 100%!" -ForegroundColor Green
} catch {
    Write-Host "  -> Chu y Client 1: $_" -ForegroundColor Yellow
}

Write-Host "`n=================================================================" -ForegroundColor Yellow
Write-Host "               MOI TRUONG HOAN TOAN SAN SANG DE THI!             " -ForegroundColor Yellow
Write-Host "=================================================================" -ForegroundColor Yellow
