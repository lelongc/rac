$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Write-Host "=== SCAN OPEN PORTS ON WIN7 (192.168.11.2) ==="
    $ports = @(23, 135, 139, 445, 3389, 5985)
    foreach ($p in $ports) {
        $res = Test-NetConnection -ComputerName 192.168.11.2 -Port $p -WarningAction SilentlyContinue
        Write-Host "Port $p : $($res.TcpTestSucceeded)"
    }
}
