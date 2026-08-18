$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    # Configure Server client to allow unencrypted and basic auth
    winrm set winrm/config/client "@{AllowUnencrypted=`"true`"}"
    winrm set winrm/config/client/auth "@{Basic=`"true`"}"
    
    $opt = New-PSSessionOption -SkipCACheck -SkipCNCheck -SkipRevocationCheck
    $secPass = ConvertTo-SecureString "123" -AsPlainText -Force
    $win7Cred = New-Object System.Management.Automation.PSCredential("Administrator", $secPass)
    
    try {
        $res = Invoke-Command -ComputerName "192.168.11.2" -Credential $win7Cred -Authentication Basic -SessionOption $opt -ScriptBlock {
            Write-Host ">>> YOU ARE INSIDE WINDOWS 7 <<<"
            hostname
            whoami
        } -ErrorAction Stop
        Write-Host "[+] REMOTE CONNECTION TO WIN7 SUCCESSFUL 100%!" -ForegroundColor Green
        $res
    } catch {
        Write-Host "[-] Error: $($_.Exception.Message)" -ForegroundColor Red
    }
}
