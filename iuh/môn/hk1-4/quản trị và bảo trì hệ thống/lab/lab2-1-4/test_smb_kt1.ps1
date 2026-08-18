$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Write-Host "=== TEST LOCAL SMB CONNECTION WITH USER KT1 AND PASS 123 ==="
    net use * /delete /y 2>$null
    net use T: \\127.0.0.1\DATA /user:KT1 123
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[+] SMB Connection to \\Server\DATA with user KT1: SUCCESSFUL!" -ForegroundColor Green
        dir T:\
        net use T: /delete /y > $null
    } else {
        Write-Host "[-] Failed connecting with KT1" -ForegroundColor Red
    }
}
