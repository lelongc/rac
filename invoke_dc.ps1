$sec = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $sec)

Write-Host "1. DANG CHAY automate_lab5_share_ntfs.ps1 TREN DC..." -ForegroundColor Yellow
Invoke-Command -ComputerName 192.168.1.154 -Credential $cred -ScriptBlock {
    & C:\automate_lab5_share_ntfs.ps1
}

Write-Host "`n2. DANG CHAY verify_lab5.ps1 TREN DC..." -ForegroundColor Yellow
Invoke-Command -ComputerName 192.168.1.154 -Credential $cred -ScriptBlock {
    & C:\verify_lab5.ps1
}
