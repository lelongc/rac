$pass = ConvertTo-SecureString "Longko0!" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Write-Host "=== 1. CHECK LANMANSERVER SERVICE (FILE SHARING) ==="
    Get-Service LanmanServer | Select-Object Name, Status, StartType

    Write-Host "`n=== 2. CHECK SMB SHARES ==="
    Get-SmbShare | Select-Object Name, Path

    Write-Host "`n=== 3. CHECK IP ADDRESSES ==="
    Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.InterfaceAlias -ne "Loopback Pseudo-Interface 1" } | Select-Object InterfaceAlias, IPAddress, AddressState

    Write-Host "`n=== 4. CHECK FIREWALL STATE ==="
    Get-NetFirewallProfile | Select-Object Name, Enabled
}
