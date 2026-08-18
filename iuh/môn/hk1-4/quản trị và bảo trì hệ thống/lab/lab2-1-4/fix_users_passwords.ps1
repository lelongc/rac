# Fix password policy and create all required lab users with both simple pass & strong pass support
$cfgPath = "$env:TEMP\sec_fix.cfg"
$sdbPath = "$env:TEMP\sec_fix.sdb"

$secContent = @"
[Unicode]
Unicode=yes
[System Access]
MinimumPasswordAge = 0
MaximumPasswordAge = 0
MinimumPasswordLength = 0
PasswordComplexity = 0
PasswordHistorySize = 0
LockoutBadCount = 3
ResetLockoutCount = 30
LockoutDuration = 30
[Privilege Rights]
SeSystemtimePrivilege = *S-1-5-32-544,*S-1-5-32-545
SeShutdownPrivilege = *S-1-5-32-544,*S-1-5-32-545
[Version]
signature="`$CHICAGO`$"
DriverVer=03/08/2026,1.0.0.0
"@

[System.IO.File]::WriteAllText($cfgPath, $secContent, [System.Text.Encoding]::Unicode)
secedit /configure /db $sdbPath /cfg $cfgPath /areas SECURITYPOLICY USER_RIGHTS /quiet
net accounts /minpwlen:0 /maxpwage:unlimited /minpwage:0 /uniquepw:0 /lockoutthreshold:3 /lockoutduration:30 /lockoutwindow:30 > $null
gpupdate /force > $null

# Ensure all lab users exist with valid passwords
$labUsers = @(
    @{ Name = "U4"; Pass = "123"; Group = $null },
    @{ Name = "U1"; Pass = "abc@123"; Group = $null },
    @{ Name = "U2"; Pass = "abc@123"; Group = $null },
    @{ Name = "KT1"; Pass = "abc@123"; Group = "KETOAN" },
    @{ Name = "KT2"; Pass = "abc@123"; Group = "KETOAN" },
    @{ Name = "NS1"; Pass = "abc@123"; Group = "NHANSU" },
    @{ Name = "NS2"; Pass = "abc@123"; Group = "NHANSU" }
)

foreach ($u in $labUsers) {
    net user $u.Name 2>$null
    if ($LASTEXITCODE -ne 0) {
        # Try simple pass first, if policy still requires complex, try abc@123
        net user $u.Name $u.Pass /add /passwordchg:no 2>$null
        if ($LASTEXITCODE -ne 0) {
            net user $u.Name "abc@123" /add /passwordchg:no
        }
        wmic useraccount where "name='$($u.Name)'" set passwordexpires=false 2>$null | Out-Null
    }
    if ($u.Group) {
        net localgroup $u.Group $u.Name /add 2>$null
    }
}

Write-Host "`n--- LIST OF ALL LAB USERS CREATED ---" -ForegroundColor Magenta
Get-WmiObject Win32_UserAccount -Filter "LocalAccount=True" | Select-Object Name, FullName, Disabled, PasswordRequired, PasswordExpires
