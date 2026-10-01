@echo off
chcp 65001 >nul
title TRUNG TAM DIEU KHIEN TU DONG HOA THI GIUA KY ^& LAB QTBTHT - IUH
color 0B

:MAIN_MENU
cls
echo ===============================================================================
echo      TRUNG TÂM ĐIỀU KHIỂN TỰ ĐỘNG HÓA THI GIỮA KỲ ^& LAB QTBTHT (IUH)
echo ===============================================================================
echo.
echo   [0] TOOL ĐỔI IP TỰ ĐỘNG THEO ĐỀ BÀI (Chui vào đổi IP Server ^& Client + Test Ping)
echo.
echo  --- KỊCH BẢN THI GIỮA KỲ CHÍNH THỨC ---
echo   [1] Cấu hình 100%% Đề thi Giữa kỳ (Domain nhom1.vn, GPO, Share, NTFS, FSRM)
echo.
echo  --- KỊCH BẢN TỰ ĐỘNG CÁC BÀI LAB (DỰ PHÒNG KHI ĐỀ RA TRÚNG LAB) ---
echo   [2] Lab 1   : Định tuyến Router Server 2012
echo   [3] Lab 2.1 : Quản trị Local User, Group, Security Policy, Share ^& NTFS
echo   [4] Lab 2.2 : Nâng cấp Domain Controller AD DS ^& Join Domain
echo   [5] Lab 3   : Quản trị Đối tượng AD DS (OU, Group, User, Delegation)
echo   [6] Lab 4   : Bảo mật AD DS ^& Group Policy (Password, Lockout, Audit)
echo   [7] Lab 5   : Quản trị Chia sẻ, Phân quyền NTFS ^& Quota FSRM
echo   [8] Lab 6   : Triển khai quản lý GPO nâng cao
echo   [9] Lab 7   : Triển khai User Profile (Home Folder, Roaming, Redirection, FSRM)
echo.
echo   [T] Mở tài liệu ôn tập lý thuyết ^& hướng dẫn thực hành (Markdown)
echo   [Q] Thoát
echo ===============================================================================
set /p opt="Chọn kịch bản muốn thực thi [0-9, T, Q]: "

if /i "%opt%"=="0" (
    call "%~dp0Doi_IP_Theo_De_Bai.bat"
    goto MAIN_MENU
)

if /i "%opt%"=="1" (
    echo.
    echo [*] Đang thực thi kịch bản Đề thi Giữa Kỳ chính thức...
    powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0Setup_GK_QTBTHT_Auto.ps1"
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="2" (
    powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0lab1_remote_config.ps1"
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="3" (
    powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0lab2_apply_all_server_config.ps1"
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="4" (
    powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0lab2t2_01_cai_dat_adds_va_promote_dc.ps1"
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="5" (
    powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0lab3_01_tu_dong_quan_tri_adds.ps1"
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="6" (
    powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0lab4_automate_gpo.ps1"
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="7" (
    powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0lab5_automate_share_ntfs.ps1"
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="8" (
    powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0lab6_automate_gpo.ps1"
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="9" (
    powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0lab7_automate_profile.ps1"
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="T" (
    start "" notepad.exe "%~dp0ON_TAP_GIUA_KY_QTBTHT_FULL.md"
    goto MAIN_MENU
)

if /i "%opt%"=="Q" exit /b
goto MAIN_MENU
