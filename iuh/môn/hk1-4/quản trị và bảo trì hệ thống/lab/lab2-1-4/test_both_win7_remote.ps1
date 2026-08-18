$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    $targets = @("192.168.11.2", "100.100.11.2")
    $opt = New-PSSessionOption -SkipCACheck -SkipCNCheck -SkipRevocationCheck
    $secPass = ConvertTo-SecureString "123" -AsPlainText -Force
    $win7Cred = New-Object System.Management.Automation.PSCredential("Administrator", $secPass)

    foreach ($t in $targets) {
        Write-Host "==========================================================" -ForegroundColor Cyan
        Write-Host "  TESTING REMOTE MANAGEMENT TO WIN7 IP: $t" -ForegroundColor Cyan
        Write-Host "==========================================================" -ForegroundColor Cyan
        
        # 1. Test Ping
        $ping = Test-Connection -ComputerName $t -Count 2 -Quiet
        Write-Host "1. Ping Test: $ping"
        
        # 2. Test SMB (Port 445) & WinRM (Port 5985)
        $p445 = (Test-NetConnection -ComputerName $t -Port 445 -WarningAction SilentlyContinue).TcpTestSucceeded
        $p5985 = (Test-NetConnection -ComputerName $t -Port 5985 -WarningAction SilentlyContinue).TcpTestSucceeded
        Write-Host "2. Port 445 (SMB): $p445 | Port 5985 (WinRM): $p5985"
        
        # 3. Test WinRM Remote Session Execution
        Write-Host "3. Connecting via WinRM..."
        try {
            $info = Invoke-Command -ComputerName $t -Credential $win7Cred -SessionOption $opt -ScriptBlock {
                $comp = hostname
                $user = whoami
                $ip = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.IPAddress -notlike "127.*" -and $_.IPAddress -notlike "169.*" }).IPAddress
                return "SUCCESS -> Hostname: $comp | Current User: $user | Local IPs: $($ip -join ', ')"
            } -ErrorAction Stop
            Write-Host "[+] $info" -ForegroundColor Green
        } catch {
            Write-Host "[-] WinRM Connection failed: $($_.Exception.Message)" -ForegroundColor Yellow
        }
    }
}
