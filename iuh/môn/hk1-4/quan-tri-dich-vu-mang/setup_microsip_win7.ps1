# ==============================================================================
# SCRIPT CHAY TREN WINDOWS 7 - TU DONG TAI & CAU HINH MICROSIP PORTABLE 100%
# ==============================================================================

param (
    [string]$ServerIP = "192.168.1.100",
    [string]$Extension = "101",
    [string]$Password = "123456"
)

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host " TU DONG CAU HINH MICROSIP TREN WINDOWS 7 " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# 1. Tao thu muc MicroSIP ngoai Desktop
$MicroSipFolder = "$env:USERPROFILE\Desktop\MicroSIP"
if (-not (Test-Path $MicroSipFolder)) {
    New-Item -ItemType Directory -Path $MicroSipFolder | Out-Null
}

# 2. Tu dong tao file microsip.ini chua san tai khoan SIP
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

Set-Content -Path $IniPath -Value $IniContent -Encoding ASCII
Write-Host "[1/2] Da tao xong file cau hinh microsip.ini" -ForegroundColor Green

# 3. Tu dong tai file phan mem MicroSIP.exe tu Ubuntu Server (HTTP port 8000)
$ExePath = "$MicroSipFolder\MicroSIP.exe"
if (-not (Test-Path $ExePath)) {
    Write-Host "[2/2] Dang tai phan mem MicroSIP.exe tu Ubuntu Server ($ServerIP)..." -ForegroundColor Yellow
    $WebClient = New-Object System.Net.WebClient
    
    $LocalUrl = "http://$ServerIP`:8000/MicroSIP.exe"
    try {
        $WebClient.DownloadFile($LocalUrl, $ExePath)
        Write-Host "-> Da tai xong MicroSIP.exe tu Ubuntu Server!" -ForegroundColor Green
    } catch {
        Write-Host "-> Tren Ubuntu vui long chay: python3 -m http.server 8000" -ForegroundColor Red
    }
} else {
    Write-Host "[2/2] MicroSIP.exe da co san!" -ForegroundColor Green
}

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host " HOAN TAT! THU MUC MicroSIP DA CO TREN DESKTOP." -ForegroundColor Green
Write-Host " Mo thu muc Desktop\MicroSIP va chay MicroSIP.exe la ONLINE!" -ForegroundColor Yellow
Write-Host "==========================================" -ForegroundColor Cyan
