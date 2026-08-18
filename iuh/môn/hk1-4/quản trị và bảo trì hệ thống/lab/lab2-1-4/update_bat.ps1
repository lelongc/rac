$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    $batContent = @"
@echo off
echo Dang cau hinh toan bo quyen Remote WinRM cho Win 7...
winrm quickconfig -q
powershell -Command "Set-Item WSMan:\localhost\Client\TrustedHosts -Value * -Force"
winrm set winrm/config/service/auth @{Basic="true"}
winrm set winrm/config/service @{AllowUnencrypted="true"}
winrm set winrm/config/client @{AllowUnencrypted="true"}
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f
net user Administrator 123 /active:yes
netsh advfirewall firewall set rule group="Windows Remote Management" new enable=yes
echo ===================================================
echo DA CAU HINH XONG TOAN DIEN QUYEN CHO WIN 7!
echo ===================================================
pause
"@

    $batContent | Out-File "C:\THUCHANH\DULIEU\enable_remote_win7.bat" -Encoding ascii -Force
    $batContent | Out-File "C:\TAILIEU\enable_remote_win7.bat" -Encoding ascii -Force
    Write-Host "[+] Updated enable_remote_win7.bat with complete Workgroup Remote policies!" -ForegroundColor Green
}
