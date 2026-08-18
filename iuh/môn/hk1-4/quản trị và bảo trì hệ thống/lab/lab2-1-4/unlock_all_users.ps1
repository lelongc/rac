$pass = ConvertTo-SecureString "Longko0!" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Write-Host "=== UNLOCKING ALL USER ACCOUNTS AND RESETTING PASSWORDS ==="
    
    # Lay danh sach tat ca user va unlock
    $allUsers = @("U1", "U2", "U4", "KT1", "KT2", "NS1", "NS2", "SV1", "SV2", "SV3", "GV1", "GV2", "Administrator", "Guest")
    foreach ($u in $allUsers) {
        net user $u /active:yes 2>$null
        # Unlock account
        net user $u /active:yes /expires:never 2>$null
        # Set password to 123
        net user $u 123 2>$null
        if ($LASTEXITCODE -ne 0) {
            net user $u "abc@123" 2>$null
        }
    }

    # Reset lockout counters via net accounts
    net accounts /lockoutthreshold:0 > $null
    net accounts /lockoutthreshold:3 /lockoutduration:30 /lockoutwindow:30 > $null

    Write-Host "All accounts have been UNLOCKED successfully!"
    Get-WmiObject Win32_UserAccount -Filter "LocalAccount=True" | Select-Object Name, Disabled, Lockout
}
