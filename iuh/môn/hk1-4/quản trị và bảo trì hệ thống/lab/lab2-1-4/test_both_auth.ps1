$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Write-Host "=== TEST CONNECTION TO WIN7 (192.168.11.2) ==="
    
    # Try with Basic auth
    $opt = New-PSSessionOption -SkipCACheck -SkipCNCheck -SkipRevocationCheck
    $secPass = ConvertTo-SecureString "123" -AsPlainText -Force
    $win7Cred = New-Object System.Management.Automation.PSCredential("WIN-RKVRS24A9VK\Administrator", $secPass)
    
    try {
        $res = Invoke-Command -ComputerName "192.168.11.2" -Credential $win7Cred -Authentication Basic -SessionOption $opt -ScriptBlock {
            hostname
            whoami
        } -ErrorAction Stop
        Write-Host "[+] CONNECTED SUCCESSFULLY VIA BASIC AUTH!" -ForegroundColor Green
        $res
    } catch {
        Write-Host "[-] Basic auth: $($_.Exception.Message)"
        try {
            $win7Cred2 = New-Object System.Management.Automation.PSCredential("Administrator", $secPass)
            $res2 = Invoke-Command -ComputerName "192.168.11.2" -Credential $win7Cred2 -SessionOption $opt -ScriptBlock {
                hostname
                whoami
            } -ErrorAction Stop
            Write-Host "[+] CONNECTED SUCCESSFULLY VIA NEGOTIATE!" -ForegroundColor Green
            $res2
        } catch {
            Write-Host "[-] Negotiate auth: $($_.Exception.Message)"
        }
    }
}
