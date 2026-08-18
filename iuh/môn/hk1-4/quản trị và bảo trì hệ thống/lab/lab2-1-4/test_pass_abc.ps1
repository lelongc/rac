$pass = ConvertTo-SecureString "abc@123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)
Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Write-Host "Connected successfully as Administrator with password 'abc@123'!"
    # Reset Administrator password back to Longko0! or whatever user wants
    net user Administrator "Longko0!"
    Write-Host "Reset Administrator password back to Longko0! successfully!"
}
