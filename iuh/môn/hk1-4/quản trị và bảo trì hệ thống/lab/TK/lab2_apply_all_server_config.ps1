$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Write-Host "==========================================================" -ForegroundColor Cyan
    Write-Host "       CHAY TOAN BO CAU HINH LAB 1 - 4 TREN SERVER        " -ForegroundColor Cyan
    Write-Host "==========================================================" -ForegroundColor Cyan

    # --- 1. LOCAL USERS & GROUPS (BAI 1 & BAI 4) ---
    Write-Host "`n[+] 1. Cau hinh Users va Groups..." -ForegroundColor Yellow
    $groups = @("SINHVIEN", "GIAOVIEN", "KETOAN", "NHANSU")
    foreach ($g in $groups) {
        net localgroup $g 2>$null
        if ($LASTEXITCODE -ne 0) { net localgroup $g /add > $null }
    }

    $allUsers = @(
        @{ Name="SV1"; Group="SINHVIEN" },
        @{ Name="SV2"; Group="SINHVIEN" },
        @{ Name="SV3"; Group="SINHVIEN" },
        @{ Name="GV1"; Group="GIAOVIEN" },
        @{ Name="GV2"; Group="GIAOVIEN" },
        @{ Name="U1";  Group="Users" },
        @{ Name="U2";  Group="Users" },
        @{ Name="U4";  Group="Users" },
        @{ Name="KT1"; Group="KETOAN" },
        @{ Name="KT2"; Group="KETOAN" },
        @{ Name="NS1"; Group="NHANSU" },
        @{ Name="NS2"; Group="NHANSU" }
    )

    foreach ($u in $allUsers) {
        net user $u.Name 123 /active:yes 2>$null
        if ($LASTEXITCODE -ne 0) {
            net user $u.Name 123 /add /passwordchg:no > $null
        }
        wmic useraccount where "name='$($u.Name)'" set passwordexpires=false 2>$null | Out-Null
        if ($u.Group -ne "Users") {
            net localgroup $u.Group $u.Name /add 2>$null
        }
    }
    Write-Host "    -> Da tao va dong bo toan bo 12 User voi mat khau la: 123" -ForegroundColor Green

    # --- 2. LOCAL SECURITY POLICY (BAI 2) ---
    Write-Host "`n[+] 2. Cau hinh Local Security Policy..." -ForegroundColor Yellow
    $secContent = @"
[Unicode]
Unicode=yes
[System Access]
MinimumPasswordAge = 0
MaximumPasswordAge = 0
MinimumPasswordLength = 0
PasswordComplexity = 0
PasswordHistorySize = 0
LockoutBadCount = 0
[Privilege Rights]
SeSystemtimePrivilege = *S-1-5-32-544,*S-1-5-32-545
SeShutdownPrivilege = *S-1-5-32-544,*S-1-5-32-545
[Version]
signature="`$CHICAGO`$"
Revision=1
"@
    $cfg = "$env:TEMP\sec.cfg"
    $sdb = "$env:TEMP\sec.sdb"
    $secContent | Out-File -FilePath $cfg -Encoding ascii
    secedit /configure /db $sdb /cfg $cfg /quiet
    Remove-Item $cfg, $sdb -Force -ErrorAction SilentlyContinue
    gpupdate /force > $null
    Write-Host "    -> Da cau hinh Password Policy, Quyen Tat May & Chinh gio cho Users" -ForegroundColor Green

    # --- 3. SHARES (BAI 3 & BAI 4) ---
    Write-Host "`n[+] 3. Cau hinh Share Permission..." -ForegroundColor Yellow
    New-Item -Path "C:\THUCHANH\DULIEU" -ItemType Directory -Force | Out-Null
    New-Item -Path "C:\THUCHANH\BIMAT" -ItemType Directory -Force | Out-Null
    New-Item -Path "C:\TAILIEU" -ItemType Directory -Force | Out-Null
    New-Item -Path "C:\DATA\CHUNG" -ItemType Directory -Force | Out-Null
    New-Item -Path "C:\DATA\KETOAN" -ItemType Directory -Force | Out-Null
    New-Item -Path "C:\DATA\NHANSU" -ItemType Directory -Force | Out-Null

    "Day la tai lieu thuc hanh" | Out-File "C:\THUCHANH\DULIEU\thuchanh.txt" -Encoding utf8 -Force
    "Day la tai lieu bi mat" | Out-File "C:\THUCHANH\BIMAT\thuchanh.txt" -Encoding utf8 -Force
    "Day la tai lieu share" | Out-File "C:\TAILIEU\tailieu.txt" -Encoding utf8 -Force

    $shares = @(
        @{ Name="DULIEU"; Path="C:\THUCHANH\DULIEU" },
        @{ Name="BIMAT$"; Path="C:\THUCHANH\BIMAT" },
        @{ Name="DULIEU_KETOAN"; Path="C:\THUCHANH\DULIEU" },
        @{ Name="TAILIEU"; Path="C:\TAILIEU" },
        @{ Name="DATA"; Path="C:\DATA" }
    )
    foreach ($s in $shares) {
        if (-not (Get-SmbShare -Name $s.Name -ErrorAction SilentlyContinue)) {
            New-SmbShare -Name $s.Name -Path $s.Path -FullAccess "Everyone" | Out-Null
        }
    }
    Write-Host "    -> Da tao va share: DULIEU, BIMAT$, DULIEU_KETOAN, TAILIEU, DATA" -ForegroundColor Green

    # --- 4. NTFS PERMISSION & SPECIAL PERMISSIONS (BAI 4) ---
    Write-Host "`n[+] 4. Cau hinh NTFS Permission & Special Permissions tren C:\DATA..." -ForegroundColor Yellow
    # C:\DATA: Cho phep Users, KETOAN, NHANSU doc thu muc
    icacls "C:\DATA" /inheritance:d > $null
    icacls "C:\DATA" /grant "Users:(OI)(CI)RX" "KETOAN:(OI)(CI)RX" "NHANSU:(OI)(CI)RX" "Administrators:(OI)(CI)F" "SYSTEM:(OI)(CI)F" > $null

    # C:\DATA\CHUNG: KETOAN & NHANSU Full Control
    icacls "C:\DATA\CHUNG" /grant "KETOAN:(OI)(CI)F" "NHANSU:(OI)(CI)F" > $null

    # C:\DATA\KETOAN: Chi KETOAN va CREATOR OWNER
    icacls "C:\DATA\KETOAN" /inheritance:d > $null
    icacls "C:\DATA\KETOAN" /remove:g "Users" "NHANSU" 2>$null > $null
    icacls "C:\DATA\KETOAN" /grant:r "KETOAN:(OI)(CI)(RX,WD,AD,WA,WEA,RC)" > $null
    icacls "C:\DATA\KETOAN" /grant:r "CREATOR OWNER:(OI)(CI)(IO)F" > $null
    icacls "C:\DATA\KETOAN" /grant "Administrators:(OI)(CI)F" > $null

    # C:\DATA\NHANSU: Chi NHANSU va CREATOR OWNER
    icacls "C:\DATA\NHANSU" /inheritance:d > $null
    icacls "C:\DATA\NHANSU" /remove:g "Users" "KETOAN" 2>$null > $null
    icacls "C:\DATA\NHANSU" /grant:r "NHANSU:(OI)(CI)F" > $null
    icacls "C:\DATA\NHANSU" /grant:r "CREATOR OWNER:(OI)(CI)(IO)F" > $null
    icacls "C:\DATA\NHANSU" /grant "Administrators:(OI)(CI)F" > $null
    Write-Host "    -> Da phan quyen NTFS chuan cho KETOAN, NHANSU, CHUNG, Special Permissions!" -ForegroundColor Green

    # --- 5. RESET SESSIONS ---
    Get-SmbSession | Close-SmbSession -Force 2>$null
    Write-Host "`n[+] 5. Da don dep toan bo phien ket noi SMB cu tren Server!" -ForegroundColor Green

    Write-Host "`n==========================================================" -ForegroundColor Cyan
    Write-Host "       TAT CA CAU HINH BAI 1 - 4 DA HOAN TAT 100%!        " -ForegroundColor Cyan
    Write-Host "==========================================================" -ForegroundColor Cyan
}
