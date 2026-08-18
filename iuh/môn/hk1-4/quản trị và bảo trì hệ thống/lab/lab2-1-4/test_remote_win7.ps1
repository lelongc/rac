$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Write-Host "=== TEST WINRM REMOTING TO WIN7 (192.168.11.2) ==="
    
    # Enable TrustedHosts on Server
    Set-Item WSMan:\localhost\Client\TrustedHosts -Value * -Force
    
    $win7Cred = New-Object System.Management.Automation.PSCredential("Administrator", (ConvertTo-SecureString "123" -AsPlainText -Force))
    try {
        $result = Invoke-Command -ComputerName "192.168.11.2" -Credential $win7Cred -ScriptBlock {
            Write-Host "HELLO FROM INSIDE WINDOWS 7!"
            hostname
            whoami
            ipconfig
        } -ErrorAction Stop
        Write-Host "[+] REMOTE CONNECTION TO WIN7 SUCCESSFUL 100%!" -ForegroundColor Green
        $result
    } catch {
        Write-Host "[-] Connection error: $($_.Exception.Message)" -ForegroundColor Red
    }
}
