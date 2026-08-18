$pass = ConvertTo-SecureString "Longko0!" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)
Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Write-Host "Connected successfully to: $(hostname)"
    Get-WmiObject Win32_OperatingSystem | Select-Object Caption, Version, OSArchitecture
}
