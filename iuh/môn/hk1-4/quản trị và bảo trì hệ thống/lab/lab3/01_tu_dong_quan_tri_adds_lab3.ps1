$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Write-Host "==========================================================================" -ForegroundColor Cyan
Write-Host "     TU DONG CAU HINH BAI THUC HANH LAB 3 - QUAN TRI DOI TUONG AD DS     " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Import-Module ActiveDirectory

    $domainDN = (Get-ADDomain).DistinguishedName
    $defaultPass = ConvertTo-SecureString "123" -AsPlainText -Force

    Write-Host "`n[1/5] CAU HINH CHINH SACH MAT KHAU CHO DOMAIN..." -ForegroundColor Yellow
    try {
        Set-ADDefaultDomainPasswordPolicy -Identity "newstar.vn" `
                                          -ComplexityEnabled $false `
                                          -MinPasswordLength 0 `
                                          -PasswordHistoryCount 0 `
                                          -MinPasswordAge (New-TimeSpan) `
                                          -MaxPasswordAge (New-TimeSpan)
        Write-Host "  [+] Da tat PasswordComplexity & MinPasswordLength (Cho phep dat pass '123')!" -ForegroundColor Green
    } catch {
        Write-Host "  [-] Loi cau hinh Policy: $($_.Exception.Message)" -ForegroundColor Red
    }

    Write-Host "`n[2/5] KHOI TAO CAY CAU TRUC ORGANIZATIONAL UNIT (OU)..." -ForegroundColor Yellow
    $iuhDN = "OU=IUH,$domainDN"
    if (-not (Get-ADOrganizationalUnit -Filter "DistinguishedName -eq '$iuhDN'" -ErrorAction SilentlyContinue)) {
        New-ADOrganizationalUnit -Name "IUH" -Path $domainDN -ProtectedFromAccidentalDeletion $true
        Write-Host "  [+] Da tao OU cha: OU=IUH" -ForegroundColor Green
    }

    $subOUs = @("BanGiamHieu", "KhoaCNTT", "PhongDaoTao", "PhongKeToan")
    foreach ($ouName in $subOUs) {
        $subDN = "OU=$ouName,$iuhDN"
        if (-not (Get-ADOrganizationalUnit -Filter "DistinguishedName -eq '$subDN'" -ErrorAction SilentlyContinue)) {
            New-ADOrganizationalUnit -Name $ouName -Path $iuhDN -ProtectedFromAccidentalDeletion $true
            Write-Host "  [+] Da tao OU con: OU=$ouName,OU=IUH" -ForegroundColor Green
        }
    }

    Write-Host "`n[3/5] KHOI TAO CAC SECURITY GROUPS..." -ForegroundColor Yellow
    $groups = @(
        @{ Name = "G_BanGiamHieu"; OU = "OU=BanGiamHieu,$iuhDN" },
        @{ Name = "G_GiaoVienCNTT"; OU = "OU=KhoaCNTT,$iuhDN" },
        @{ Name = "G_SinhVienCNTT"; OU = "OU=KhoaCNTT,$iuhDN" },
        @{ Name = "G_PhongDaoTao"; OU = "OU=PhongDaoTao,$iuhDN" },
        @{ Name = "G_PhongKeToan"; OU = "OU=PhongKeToan,$iuhDN" },
        @{ Name = "G_IT_Admin"; OU = "OU=KhoaCNTT,$iuhDN" }
    )

    foreach ($g in $groups) {
        $gName = $g.Name
        $gPath = $g.OU
        $exist = Get-ADGroup -Filter "SamAccountName -eq '$gName'" -ErrorAction SilentlyContinue
        if (-not $exist) {
            New-ADGroup -Name $gName -GroupScope Global -GroupCategory Security -Path $gPath
            Write-Host "  [+] Da tao Group: $gName (Scope: Global, Path: $gPath)" -ForegroundColor Green
        } else {
            Move-ADObject -Identity $exist.DistinguishedName -TargetPath $gPath -ErrorAction SilentlyContinue
            Write-Host "  [*] Group $gName da ton tai." -ForegroundColor Yellow
        }
    }

    Write-Host "`n[4/5] KHOI TAO CAC USERS VA CAU HINH CHINH SACH MAT KHAU KIEM THU..." -ForegroundColor Yellow
    $users = @(
        @{
            Sam = "bgh_user1"; Name = "BGH User 1"; OU = "OU=BanGiamHieu,$iuhDN";
            Group = "G_BanGiamHieu"; Desc = "Tai khoan Ban Giam Hieu";
            PwdNeverExpires = $true; ChangeAtLogon = $false; CannotChange = $false; Enabled = $true
        },
        @{
            Sam = "gv_cntt1"; Name = "Giao Vien CNTT 1"; OU = "OU=KhoaCNTT,$iuhDN";
            Group = "G_GiaoVienCNTT"; Desc = "Tai khoan Giang vien CNTT";
            PwdNeverExpires = $true; ChangeAtLogon = $false; CannotChange = $false; Enabled = $true
        },
        @{
            Sam = "sv_cntt1"; Name = "Sinh Vien CNTT 1"; OU = "OU=KhoaCNTT,$iuhDN";
            Group = "G_SinhVienCNTT"; Desc = "Tai khoan Sinh vien CNTT";
            PwdNeverExpires = $true; ChangeAtLogon = $false; CannotChange = $false; Enabled = $true
        },
        @{
            Sam = "user_doipass"; Name = "User Bat Buoc Doi Pass"; OU = "OU=KhoaCNTT,$iuhDN";
            Group = "G_SinhVienCNTT"; Desc = "Tinh huong 1: Bat buoc doi pass lan dau";
            PwdNeverExpires = $false; ChangeAtLogon = $true; CannotChange = $false; Enabled = $true
        },
        @{
            Sam = "user_khongdoipass"; Name = "User Khong Cho Doi Pass"; OU = "OU=PhongDaoTao,$iuhDN";
            Group = "G_PhongDaoTao"; Desc = "Tinh huong 2: Khong cho tu doi pass";
            PwdNeverExpires = $true; ChangeAtLogon = $false; CannotChange = $true; Enabled = $true
        },
        @{
            Sam = "user_vohieuhoa"; Name = "User Bi Vo Hieu Hoa"; OU = "OU=PhongKeToan,$iuhDN";
            Group = "G_PhongKeToan"; Desc = "Tinh huong 5: Tai khoan bi vo hieu hoa";
            PwdNeverExpires = $true; ChangeAtLogon = $false; CannotChange = $false; Enabled = $false
        }
    )

    foreach ($u in $users) {
        $sam = $u.Sam
        $name = $u.Name
        $uPath = $u.OU
        $uGroup = $u.Group

        $existingUser = Get-ADUser -Filter "SamAccountName -eq '$sam'" -ErrorAction SilentlyContinue
        if ($existingUser) {
            Remove-ADUser -Identity $sam -Confirm:$false -ErrorAction SilentlyContinue
        }

        New-ADUser -Name $name `
                   -DisplayName $name `
                   -SamAccountName $sam `
                   -UserPrincipalName "$sam@newstar.vn" `
                   -Path $uPath `
                   -AccountPassword $defaultPass `
                   -Description $u.Desc `
                   -Enabled $u.Enabled `
                   -PasswordNeverExpires $u.PwdNeverExpires `
                   -ChangePasswordAtLogon $u.ChangeAtLogon `
                   -CannotChangePassword $u.CannotChange

        Add-ADGroupMember -Identity $uGroup -Members $sam -ErrorAction SilentlyContinue
        Write-Host "  [+] Da tao User $sam ($($u.Desc)) -> Gan vao $uGroup" -ForegroundColor Green
    }

    Write-Host "`n[5/5] CAP NHAT TAI KHOAN CHINH hiepdh..." -ForegroundColor Yellow
    $hiep = Get-ADUser -Filter "SamAccountName -eq 'hiepdh'" -ErrorAction SilentlyContinue
    if ($hiep) {
        Move-ADObject -Identity $hiep.DistinguishedName -TargetPath "OU=KhoaCNTT,$iuhDN" -ErrorAction SilentlyContinue
        Add-ADGroupMember -Identity "G_IT_Admin" -Members "hiepdh" -ErrorAction SilentlyContinue
        Add-ADGroupMember -Identity "G_GiaoVienCNTT" -Members "hiepdh" -ErrorAction SilentlyContinue
        Write-Host "  [+] Da chuyen hiepdh vao OU=KhoaCNTT va gan vao nhom G_IT_Admin, G_GiaoVienCNTT!" -ForegroundColor Green
    }

    Write-Host "`n==========================================================================" -ForegroundColor Cyan
    Write-Host "     CAU HINH TU DONG BAI LAB 3 DA HOAN TAT THANH CONG 100%!             " -ForegroundColor Cyan
    Write-Host "==========================================================================" -ForegroundColor Cyan
}
