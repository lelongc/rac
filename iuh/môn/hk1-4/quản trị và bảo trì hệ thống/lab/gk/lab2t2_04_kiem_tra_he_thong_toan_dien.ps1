$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Write-Host "==========================================================================" -ForegroundColor Cyan
Write-Host "     KIEM TRA TOAN DIEN HE THONG DOMAIN CONTROLLER & CLIENTS (LAB 2-T2)  " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Import-Module ActiveDirectory

    Write-Host "`n1. THONG TIN DOMAIN CONTROLLER:" -ForegroundColor Yellow
    $domain = Get-ADDomain
    Write-Host "  - Ten mien (Domain Name)       : $($domain.DNSRoot)" -ForegroundColor Green
    Write-Host "  - NetBIOS Name                 : $($domain.NetBIOSName)" -ForegroundColor Green
    Write-Host "  - Domain Mode                  : $($domain.DomainMode)" -ForegroundColor Green
    Write-Host "  - PDC Emulator                 : $($domain.PDCEmulator)" -ForegroundColor Green

    Write-Host "`n2. DANH SACH MAY TINH TRONG ACTIVE DIRECTORY (COMPUTERS):" -ForegroundColor Yellow
    Get-ADComputer -Filter * -Properties DNSHostName, Enabled | 
        Select-Object Name, DNSHostName, Enabled | Format-Table -AutoSize

    Write-Host "3. DANH SACH NGUOI DUNG TRONG DOMAIN (USERS):" -ForegroundColor Yellow
    Get-ADUser -Filter * -Properties DisplayName, UserPrincipalName, Enabled | 
        Select-Object Name, SamAccountName, UserPrincipalName, Enabled | Format-Table -AutoSize

    Write-Host "4. KIEM TRA KENH BAO MAT (SECURE CHANNEL) TU MAY CLIENT:" -ForegroundColor Yellow
    $targets = @(
        @{ IP = "192.168.11.2"; Expected = "WIN7-PC1" },
        @{ IP = "100.100.11.2"; Expected = "WIN7-PC2" }
    )

    foreach ($t in $targets) {
        $ip = $t.IP
        $exp = $t.Expected
        try {
            $localCred = New-Object System.Management.Automation.PSCredential(".\Administrator", (ConvertTo-SecureString "123" -AsPlainText -Force))
            $cs = Get-WmiObject -Class Win32_ComputerSystem -ComputerName $ip -Credential $localCred -ErrorAction Stop
            $sec = Invoke-Command -ComputerName $ip -Credential $localCred -ScriptBlock {
                powershell -Command "Test-ComputerSecureChannel"
            } -ErrorAction SilentlyContinue

            Write-Host "  [+] May $exp ($ip):" -ForegroundColor Cyan
            Write-Host "      - Ten may thuc te : $($cs.Name)" -ForegroundColor Green
            Write-Host "      - Domain ket noi  : $($cs.Domain)" -ForegroundColor Green
            Write-Host "      - PartOfDomain    : $($cs.PartOfDomain)" -ForegroundColor Green
            Write-Host "      - Secure Channel  : $sec" -ForegroundColor Green
        } catch {
            Write-Host "  [-] May $exp ($ip): Khong the ket noi WMI ($($_.Exception.Message))" -ForegroundColor Red
        }
    }
}

Write-Host "`n==========================================================================" -ForegroundColor Cyan
Write-Host "                     KIEM TRA HOAN TAT!                                  " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan
