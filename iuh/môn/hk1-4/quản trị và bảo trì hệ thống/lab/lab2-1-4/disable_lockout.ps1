$pass = ConvertTo-SecureString "Longko0!" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Write-Host "=== DISABLING ACCOUNT LOCKOUT & UNLOCKING ALL ACCOUNTS PERMANENTLY ==="
    
    # 1. Tat hoan toan tinh nang khoa tai khoan de khong bao gio bi lock nua
    net accounts /lockoutthreshold:0

    # 2. Unlock toan bo tai khoan
    $users = @("Administrator", "Guest", "U1", "U2", "U4", "KT1", "KT2", "NS1", "NS2", "SV1", "SV2", "SV3", "GV1", "GV2")
    foreach ($u in $users) {
        net user $u /active:yes 2>$null
        # Dat mat khau dong bo: ca '123' va 'abc@123'
        net user $u "abc@123" 2>$null
    }
    net user U1 123 2>$null
    net user U2 123 2>$null

    Write-Host "`n=== STATUS OF ALL USERS ==="
    Get-WmiObject Win32_UserAccount -Filter "LocalAccount=True" | Select-Object Name, Disabled, Lockout
}
