$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Write-Host "=== 1. CHECK & GRANT FULL NTFS PERMISSIONS ON LAB 3 FOLDERS ==="
    # Grant Everyone & Users Full NTFS access on C:\THUCHANH and C:\TAILIEU
    icacls "C:\THUCHANH" /grant "Everyone:(OI)(CI)F" "Users:(OI)(CI)F" > $null
    icacls "C:\THUCHANH\DULIEU" /grant "Everyone:(OI)(CI)F" "Users:(OI)(CI)F" > $null
    icacls "C:\THUCHANH\BIMAT" /grant "Everyone:(OI)(CI)F" "Users:(OI)(CI)F" > $null
    icacls "C:\TAILIEU" /grant "Everyone:(OI)(CI)F" "Users:(OI)(CI)F" > $null

    Write-Host "[+] Granted Full NTFS Permissions to Everyone & Users on DULIEU, BIMAT, TAILIEU!" -ForegroundColor Green

    Write-Host "`n=== 2. VERIFY NTFS ACLS ==="
    icacls "C:\THUCHANH\DULIEU"
    icacls "C:\TAILIEU"
}
