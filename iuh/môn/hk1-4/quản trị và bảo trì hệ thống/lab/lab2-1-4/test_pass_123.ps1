$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)
Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Write-Host "Connected successfully as Administrator with password '123'!"
    # Ensure lockout is 0 and users exist
    net accounts /lockoutthreshold:0
    Get-SmbShare | Select-Object Name, Path
}
