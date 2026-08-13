# Change Host VMnet11 IP from 192.168.11.1 to 192.168.11.254 so it stops conflicting with Windows Server VM!
$hostAdapter = Get-NetIPAddress -IPAddress "192.168.11.1" -ErrorAction SilentlyContinue
if ($hostAdapter) {
    Write-Host "Host machine has IP 192.168.11.1 on $($hostAdapter.InterfaceAlias). Changing Host IP to 192.168.11.254..."
    Remove-NetIPAddress -InterfaceAlias $hostAdapter.InterfaceAlias -IPAddress "192.168.11.1" -Confirm:$false
    New-NetIPAddress -InterfaceAlias $hostAdapter.InterfaceAlias -IPAddress "192.168.11.254" -PrefixLength 24 -ErrorAction SilentlyContinue
    Write-Host "Host IP updated to 192.168.11.254 successfully!"
} else {
    Write-Host "No host IP conflict found."
}
