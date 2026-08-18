$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    # 1. Tam thoi khoa account U1 tren Server
    net user U1 /active:no
    
    # 2. Xoa toan bo phien ket noi SMB dang gan voi U1
    Get-SmbSession | Close-SmbSession -Force 2>$null
    
    Write-Host "[+] Da vo hieu hoa tai khoan U1 tren Server de buoc Win7 phai hoi tai khoan moi (KT1)!" -ForegroundColor Green
}
