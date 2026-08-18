$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Write-Host "=== 1. SERVER PING TO WIN7 (192.168.11.2) ==="
    Test-Connection -ComputerName 192.168.11.2 -Count 2 -Quiet

    Write-Host "`n=== 2. LOCAL ACCESS CHECK TO SHARES ON SERVER ==="
    Get-SmbShare | Where-Object { $_.Name -in @("DULIEU", "BIMAT$", "DULIEU_KETOAN", "TAILIEU", "DATA") } | Select-Object Name, Path
}
