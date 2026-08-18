$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Write-Host "=== 1. CHECK KT1, NS1 USER DETAILS ON SERVER ==="
    net user KT1
    net user NS1

    Write-Host "`n=== 2. ENSURE KT1 PASS IS 123 AND ACTIVE ==="
    net user KT1 123 /active:yes
    net user NS1 123 /active:yes
    net accounts /lockoutthreshold:0
}
