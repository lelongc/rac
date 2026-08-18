$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    # Set all lab user passwords to 123
    $allUsers = @("U1", "U2", "U4", "KT1", "KT2", "NS1", "NS2", "SV1", "SV2", "SV3", "GV1", "GV2")
    foreach ($u in $allUsers) {
        net user $u 123 /active:yes 2>$null
    }
    net accounts /lockoutthreshold:0 > $null
    Write-Host "All lab users (U1, U2, U4, KT1, KT2, NS1, NS2, SV1..SV3, GV1..GV2) passwords set to: 123"
}
