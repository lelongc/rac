@echo off
echo ================================
echo   REMOVE HYPER-V COMPLETELY
echo ================================

echo.
echo [1] Disabling Hyper-V features...
dism.exe /Online /Disable-Feature:Microsoft-Hyper-V-All /NoRestart
dism.exe /Online /Disable-Feature:Microsoft-Hyper-V /NoRestart
dism.exe /Online /Disable-Feature:VirtualMachinePlatform /NoRestart
dism.exe /Online /Disable-Feature:WindowsHypervisorPlatform /NoRestart
dism.exe /Online /Disable-Feature:Containers /NoRestart

echo.
echo [2] Turning off hypervisor...
bcdedit /set hypervisorlaunchtype off

echo.
echo [3] Removing Hyper-V services...
sc stop vmcompute >nul 2>&1
sc stop vmms >nul 2>&1
sc delete vmcompute >nul 2>&1
sc delete vmms >nul 2>&1

echo.
echo [4] Removing Hyper-V drivers (if found)...
for /f "tokens=1*" %%i in ('pnputil /enum-drivers ^| findstr /i "hv vmswitch vmnet"') do (
echo Removing driver %%i
pnputil /delete-driver %%i /uninstall /force >nul 2>&1
)

echo.
echo [5] Done. System will reboot in 5 seconds...
timeout /t 5

shutdown /r /t 0
