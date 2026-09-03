$sec = ConvertTo-SecureString "123" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $sec)

$net = New-Object -ComObject WScript.Network
try {
    $net.MapNetworkDrive("Z:", "\\192.168.1.154\C$", $false, "Administrator", "123")
    Copy-Item -Path "d:\folder\rac\iuh\môn\hk1-4\quản trị và bảo trì hệ thống\lab\lab5\automate_lab5_share_ntfs.ps1" -Destination "Z:\automate_lab5_share_ntfs.ps1" -Force
    Copy-Item -Path "d:\folder\rac\iuh\môn\hk1-4\quản trị và bảo trì hệ thống\lab\lab5\verify_lab5.ps1" -Destination "Z:\verify_lab5.ps1" -Force
    $net.RemoveNetworkDrive("Z:", $true, $true)
    Write-Host "Da copy scripts len Server C:\" -ForegroundColor Green
} catch {
    Write-Host "Loi copy script: $_" -ForegroundColor Red
}

Write-Host "`nDang chay automate_lab5_share_ntfs.ps1 tren DC..." -ForegroundColor Yellow
Invoke-Command -ComputerName 192.168.1.154 -Credential $cred -ScriptBlock {
    & C:\automate_lab5_share_ntfs.ps1
}

Write-Host "`nDang chay verify_lab5.ps1 tren DC..." -ForegroundColor Yellow
Invoke-Command -ComputerName 192.168.1.154 -Credential $cred -ScriptBlock {
    & C:\verify_lab5.ps1
}
