$sec = ConvertTo-SecureString '123' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential('Administrator', $sec)
try {
    $res = Invoke-Command -ComputerName '192.168.1.151' -Credential $cred -ScriptBlock { hostname; ipconfig } -ErrorAction Stop
    Write-Host "SUCCESS: $res"
} catch {
    Write-Host "ERROR: $($_.Exception.Message)"
}
