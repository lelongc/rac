$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    # Grant Users Read permission on C:\DATA (so any user like U1 can open DATA to see the 3 subfolders)
    icacls "C:\DATA" /grant "Users:(OI)(CI)RX" > $null
    
    # Ensure KETOAN folder is strictly for KETOAN and CREATOR OWNER (Users/NHANSU blocked)
    icacls "C:\DATA\KETOAN" /inheritance:d > $null
    icacls "C:\DATA\KETOAN" /remove:g "Users" "NHANSU" 2>$null > $null
    icacls "C:\DATA\KETOAN" /grant:r "KETOAN:(OI)(CI)(RX,WD,AD,WA,WEA,RC)" > $null
    icacls "C:\DATA\KETOAN" /grant:r "CREATOR OWNER:(OI)(CI)(IO)F" > $null

    # Ensure NHANSU folder is strictly for NHANSU (Users/KETOAN blocked)
    icacls "C:\DATA\NHANSU" /inheritance:d > $null
    icacls "C:\DATA\NHANSU" /remove:g "Users" "KETOAN" 2>$null > $null
    icacls "C:\DATA\NHANSU" /grant:r "NHANSU:(OI)(CI)F" > $null

    Write-Host "[+] Updated C:\DATA: Users can now open DATA folder, but KETOAN and NHANSU remain strictly protected!" -ForegroundColor Green
    
    Write-Host "`n=== CURRENT ACL ON C:\DATA ==="
    icacls "C:\DATA"
    Write-Host "`n=== CURRENT ACL ON C:\DATA\KETOAN ==="
    icacls "C:\DATA\KETOAN"
    Write-Host "`n=== CURRENT ACL ON C:\DATA\NHANSU ==="
    icacls "C:\DATA\NHANSU"
}
