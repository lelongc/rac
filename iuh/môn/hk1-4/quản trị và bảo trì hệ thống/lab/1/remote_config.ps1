$password = ConvertTo-SecureString "Longko0!" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $password)

Write-Host "=== ENABLING ROUTING & REMOTE ACCESS SERVICE (RRAS) ON SERVER ==="

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    # Check if RemoteAccess service is installed
    $rras = Get-Service RemoteAccess -ErrorAction SilentlyContinue
    if ($rras) {
        Set-Service RemoteAccess -StartupType Automatic
        Start-Service RemoteAccess -ErrorAction SilentlyContinue
        Write-Host "RemoteAccess Service Status: " (Get-Service RemoteAccess).Status
    } else {
        Write-Host "RemoteAccess service is being configured."
    }

    # Enable IPv4 Forwarding across all interfaces
    Set-NetIPInterface -Forwarding Enabled
    Write-Host "IPv4 Forwarding status on all interfaces: ENABLED"
}
