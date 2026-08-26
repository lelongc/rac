$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Write-Host "==========================================================================" -ForegroundColor Cyan
Write-Host "      KHOI PHUC HE THONG ACTIVE DIRECTORY VE TRANG THAI NGUYEN BAN       " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Import-Module ActiveDirectory

    $domainDN = (Get-ADDomain).DistinguishedName
    $iuhDN = "OU=IUH,$domainDN"
    $usersContainer = "CN=Users,$domainDN"

    Write-Host "`n[1/3] DI CHUYEN TAI KHOAN CHINH hiepdh VE CONTAINER USERS..." -ForegroundColor Yellow
    $hiep = Get-ADUser -Filter "SamAccountName -eq 'hiepdh'" -ErrorAction SilentlyContinue
    if ($hiep) {
        $lab3Groups = @("G_IT_Admin", "G_GiaoVienCNTT", "G_SinhVienCNTT", "G_BanGiamHieu", "G_PhongDaoTao", "G_PhongKeToan")
        foreach ($g in $lab3Groups) {
            Remove-ADGroupMember -Identity $g -Members "hiepdh" -Confirm:$false -ErrorAction SilentlyContinue
        }
        Move-ADObject -Identity $hiep.DistinguishedName -TargetPath $usersContainer -ErrorAction SilentlyContinue
        Write-Host "  [+] Da di chuyen hiepdh an toan ve: $usersContainer" -ForegroundColor Green
    }

    Write-Host "`n[2/3] MO KHOA TINH NANG BAO VE CHONG XOA TREN TAT CA CAC OU LAB 3..." -ForegroundColor Yellow
    if (Get-ADOrganizationalUnit -Filter "DistinguishedName -eq '$iuhDN'" -ErrorAction SilentlyContinue) {
        Get-ADOrganizationalUnit -Filter * -SearchBase $iuhDN | ForEach-Object {
            Set-ADOrganizationalUnit -Identity $_.DistinguishedName -ProtectedFromAccidentalDeletion $false
            Write-Host "  [+] Da mo khoa bao ve xoa cho: $($_.DistinguishedName)" -ForegroundColor Green
        }

        Write-Host "`n[3/3] XOA DE QUY CAY OU=IUH VA CAC DOI TUONG THU NGHIEM LAB 3..." -ForegroundColor Yellow
        Remove-ADOrganizationalUnit -Identity $iuhDN -Recursive -Confirm:$false
        Write-Host "  [+] Da xoa sach OU=IUH cung toan bo Users va Groups cua Lab 3!" -ForegroundColor Green
    } else {
        Write-Host "  [*] OU=IUH khong ton tai. He thong da o trang thai sach." -ForegroundColor Yellow
    }

    Write-Host "`n==========================================================================" -ForegroundColor Cyan
    Write-Host "      HOAN TAC VA KHOI PHUC HE THONG VE TRUOC LAB 3 THANH CONG!          " -ForegroundColor Cyan
    Write-Host "==========================================================================" -ForegroundColor Cyan
}
