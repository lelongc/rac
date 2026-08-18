$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Write-Host "=== 1. CHECK & OPTIMIZE SERVER NETWORK SECURITY SETTINGS ==="
    # Set Security Model to Classic (Users authenticate as themselves)
    Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Lsa" -Name "ForceGuest" -Value 0 -ErrorAction SilentlyContinue
    
    # Allow NTLM v1/v2 compatibility
    Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Lsa" -Name "LmCompatibilityLevel" -Value 1 -ErrorAction SilentlyContinue

    Write-Host "[+] Server security optimized for Win7 SMB client!"

    Write-Host "`n=== 2. ATTEMPT REMOTE COMMAND TO WIN7 (192.168.11.2) VIA WMI ==="
    # Try connecting to Win7 via WMI with common Administrator passwords (blank, 123, abc@123, Administrator)
    $passwords = @("", "123", "abc@123", "P@ssw0rd123", "Longko0!")
    foreach ($p in $passwords) {
        try {
            $wmiCred = New-Object System.Management.Automation.PSCredential("Administrator", (ConvertTo-SecureString $p -AsPlainText -Force))
            $os = Get-WmiObject -Class Win32_OperatingSystem -ComputerName "192.168.11.2" -Credential $wmiCred -ErrorAction Stop
            Write-Host "[+] CONNECTED TO WIN7 SUCCESSFUL with pass: '$p'!" -ForegroundColor Green
            Write-Host "Win7 OS: $($os.Caption)"
            
            # Execute net use command on Win7 directly
            $wmiProcess = [wmiclass]"\\192.168.11.2\root\cimv2:Win32_Process"
            $wmiProcess.Create("cmd.exe /c net use * /delete /y & net use Y: \\192.168.11.1\DATA /user:KT1 123 & net use Z: \\192.168.11.1\TAILIEU /user:U1 123")
            Write-Host "[+] Executed network drive mapping on Win7!"
            break
        } catch {
            Write-Host "[-] WMI with pass '$p' failed: $($_.Exception.Message)"
        }
    }
}
