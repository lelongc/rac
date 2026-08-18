$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    # 1. Bat lai tai khoan U1
    net user U1 /active:yes
    Write-Host "[+] Da bat lai tai khoan U1 tren Server!" -ForegroundColor Green

    # 2. Tao file batch enable_remote_win7.bat trong cac thu muc share
    $batContent = @"
@echo off
echo Dang bat ket noi tu xa WinRM va cau hinh Win7...
winrm quickconfig -q
powershell -Command "Set-Item WSMan:\localhost\Client\TrustedHosts -Value * -Force"
net user Administrator 123 /active:yes
netsh advfirewall firewall set rule group="Windows Remote Management" new enable=yes
echo ===================================================
echo DA BAT XONG QUYEN DIEU KHIEN TU XA CHO WIN 7!
echo ===================================================
pause
"@

    $batContent | Out-File "C:\THUCHANH\DULIEU\enable_remote_win7.bat" -Encoding ascii -Force
    $batContent | Out-File "C:\TAILIEU\enable_remote_win7.bat" -Encoding ascii -Force
    $batContent | Out-File "C:\DATA\enable_remote_win7.bat" -Encoding ascii -Force
    
    Write-Host "[+] Da tao file enable_remote_win7.bat trong thu muc DULIEU, TAILIEU va DATA!" -ForegroundColor Green
}
