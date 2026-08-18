$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Write-Host "=== TESTING CONNECTION FROM SERVER TO WIN7 (192.168.11.2) ==="
    Test-NetConnection -ComputerName 192.168.11.2 -Port 445
}
