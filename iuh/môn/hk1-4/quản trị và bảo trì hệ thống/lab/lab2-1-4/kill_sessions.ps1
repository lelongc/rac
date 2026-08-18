$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    # Force close all active SMB sessions from Win7
    Get-SmbSession | Close-SmbSession -Force
    Write-Host "[+] All active SMB sessions from Win7 (including U1) have been TERMINATED from Server!"
}
