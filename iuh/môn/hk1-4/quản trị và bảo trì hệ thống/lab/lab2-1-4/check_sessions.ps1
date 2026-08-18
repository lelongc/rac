$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Write-Host "=== ACTIVE SESSIONS CONNECTED FROM CLIENTS ==="
    Get-SmbSession | Select-Object ClientComputerName, ClientUserName, NumOpens
    
    Write-Host "`n=== NTFS ACLS ON C:\DATA ==="
    Get-Acl C:\DATA | Format-List
}
