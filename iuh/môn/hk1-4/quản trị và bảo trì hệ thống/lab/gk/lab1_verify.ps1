$password = ConvertTo-SecureString "Longko0!" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $password)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    # Remove any leftover APIPA
    Get-NetIPAddress -InterfaceAlias "vmnet11" -AddressFamily IPv4 | Where-Object { $_.IPAddress -like '169.254*' } | Remove-NetIPAddress -Confirm:$false -ErrorAction SilentlyContinue

    # Ensure 192.168.11.1 is assigned
    $hasIP = Get-NetIPAddress -InterfaceAlias "vmnet11" -IPAddress "192.168.11.1" -ErrorAction SilentlyContinue
    if (-not $hasIP) {
        New-NetIPAddress -InterfaceAlias "vmnet11" -IPAddress "192.168.11.1" -PrefixLength 24 -ErrorAction SilentlyContinue
    }

    Write-Host "`n=== VMNET11 CURRENT IP ADDRESSES ==="
    Get-NetIPAddress -InterfaceAlias "vmnet11" -AddressFamily IPv4 | Select-Object InterfaceAlias, IPAddress, PrefixLength, AddressState
}
