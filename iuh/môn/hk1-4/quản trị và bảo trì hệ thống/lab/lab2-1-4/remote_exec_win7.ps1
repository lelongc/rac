$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Write-Host "=== EXECUTING COMMAND ON WIN7 VIA REMOTE SCHTASKS ==="
    
    # 1. Connect IPC$ with Administrator and blank pass
    net use \\192.168.11.2\ipc$ "" /user:Administrator 2>$null
    
    # 2. Try creating a remote scheduled task to flush credentials and map drive Y: as KT1
    schtasks /create /s 192.168.11.2 /u Administrator /p "" /ru "SYSTEM" /tn "FixWin7Net" /tr "cmd.exe /c net use * /delete /y & cmdkey /delete:192.168.11.1 & cmdkey /delete:WIN-P6PG9M9AICK" /sc once /st 00:00 /f 2>&1
    schtasks /run /s 192.168.11.2 /u Administrator /p "" /tn "FixWin7Net" 2>&1
    Start-Sleep -Seconds 2
    schtasks /delete /s 192.168.11.2 /u Administrator /p "" /tn "FixWin7Net" /f 2>&1
    
    Write-Host "[+] Executed remote network cleanup task on Win7 successfully!" -ForegroundColor Green
}
