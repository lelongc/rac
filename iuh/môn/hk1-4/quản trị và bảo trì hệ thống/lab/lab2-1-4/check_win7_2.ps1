$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Write-Host "=== 1. CHECK SERVER IP ADAPTERS ==="
    Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.IPAddress -like "192.168.11.*" -or $_.IPAddress -like "100.100.11.*" } | Select-Object IPAddress, InterfaceAlias

    Write-Host "`n=== 2. PING TEST FROM SERVER TO WIN7-2 (100.100.11.2) ==="
    Test-Connection -ComputerName 100.100.11.2 -Count 2 -Quiet
}
