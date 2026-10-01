$pass = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $pass)

Write-Host "==========================================================================" -ForegroundColor Cyan
Write-Host "          KIEM TRA NGHIEM THU KET QUA CAU HINH BAI THUC HANH LAB 3        " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan

Invoke-Command -ComputerName "192.168.1.132" -Credential $cred -ScriptBlock {
    Import-Module ActiveDirectory

    $domainDN = (Get-ADDomain).DistinguishedName
    $iuhDN = "OU=IUH,$domainDN"

    Write-Host "`n1. DANH SACH CAC ORGANIZATIONAL UNIT (OU):" -ForegroundColor Yellow
    if (Get-ADOrganizationalUnit -Filter "DistinguishedName -eq '$iuhDN'" -ErrorAction SilentlyContinue) {
        Get-ADOrganizationalUnit -Filter * -SearchBase $iuhDN | 
            Select-Object Name, DistinguishedName | Format-Table -AutoSize
    } else {
        Write-Host "  [-] Chua tim thay OU=IUH. Hay chay script 01 de khoi tao!" -ForegroundColor Red
    }

    Write-Host "2. DANH SACH CAC GROUPS VA THANH VIEN (MEMBERSHIP):" -ForegroundColor Yellow
    $lab3Groups = @("G_BanGiamHieu", "G_GiaoVienCNTT", "G_SinhVienCNTT", "G_PhongDaoTao", "G_PhongKeToan", "G_IT_Admin")
    foreach ($gName in $lab3Groups) {
        $g = Get-ADGroup -Filter "SamAccountName -eq '$gName'" -ErrorAction SilentlyContinue
        if ($g) {
            $members = (Get-ADGroupMember -Identity $gName | Select-Object -ExpandProperty SamAccountName) -join ", "
            if (-not $members) { $members = "(Chua co thanh vien)" }
            Write-Host "  [+] Nhom: $($g.Name) [Scope: $($g.GroupScope)]" -ForegroundColor Green
            Write-Host "      -> Thanh vien: $members" -ForegroundColor Cyan
        }
    }

    Write-Host "`n3. DANH SACH USERS VA CAC THUOC TINH CHINH SACH MAT KHAU:" -ForegroundColor Yellow
    if (Get-ADOrganizationalUnit -Filter "DistinguishedName -eq '$iuhDN'" -ErrorAction SilentlyContinue) {
        Get-ADUser -Filter * -SearchBase $iuhDN -Properties DisplayName, Description, PasswordNeverExpires, CannotChangePassword, Enabled |
            Select-Object SamAccountName, DisplayName, Enabled, PasswordNeverExpires, CannotChangePassword, Description |
            Format-Table -AutoSize
    }

    Write-Host "==========================================================================" -ForegroundColor Cyan
    Write-Host "                  KIEM TRA NGHIEM THU LAB 3 HOAN TAT!                    " -ForegroundColor Cyan
    Write-Host "==========================================================================" -ForegroundColor Cyan
}
