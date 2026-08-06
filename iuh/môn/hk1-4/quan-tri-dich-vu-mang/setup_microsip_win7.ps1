# ==============================================================================
# SCRIPT CHẠY TRÊN WINDOWS 7 - TỰ ĐỘNG TẠO FILE CẤU HÌNH MICROSIP PORTABLE
# ==============================================================================

param (
    [string]$ServerIP = "192.168.1.100",
    [string]$Extension = "101",
    [string]$Password = "123456"
)

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host " Cấu hình MicroSIP cho Windows 7 Client   " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

$MicroSipFolder = "$env:USERPROFILE\Desktop\MicroSIP"
if (-not (Test-Path $MicroSipFolder)) {
    New-Item -ItemType Directory -Path $MicroSipFolder | Out-Null
}

$IniPath = "$MicroSipFolder\microsip.ini"

$IniContent = @"
[Accounts]
Account1_AccountName=IUH Extension $Extension
Account1_Server=$ServerIP
Account1_Proxy=
Account1_Domain=$ServerIP
Account1_Username=$Extension
Account1_AuthID=$Extension
Account1_Password=$Password
Account1_DisplayName=User $Extension
Account1_Publish=1
Account1_KeepAlive=15
Account1_STUN=
Account1_SRTP=0
Account1_DTMF=0

[Settings]
AutoAnswer=0
DenyIncoming=0
VolumeSpeaker=100
VolumeMicrophone=100
"@

Set-Content -Path $IniPath -Value $IniContent -Encoding UTF8

Write-Host "`nDa tao file cau hinh micoSIP tai: $IniPath" -ForegroundColor Green
Write-Host "Dung luong siêu nhe. Ban chi can tai file MicroSIP.exe tha vao thư muc Desktop\MicroSIP la xong!" -ForegroundColor Yellow
