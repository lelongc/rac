@echo off
chcp 65001 >nul
title TRUNG TAM DIEU KHIEN TU DONG HOA ON THI THUONG KY 10 LAB QTBTHT - IUH
color 0B

:MAIN_MENU
cls
echo ===============================================================================
echo      TRUNG TÂM ĐIỀU KHIỂN TỰ ĐỘNG HÓA ÔN THI THƯỜNG KỲ 10 LAB QTBTHT (IUH)
echo ===============================================================================
echo.
echo   [0] TOOL ĐỔI IP TỰ ĐỘNG THEO ĐỀ BÀI (Chui vào đổi IP Server ^& Client + Test Ping)
echo   [1] KIỂM TRA PING ^& KẾT NỐI 3 MÁY (Test kết nối Host, Server, Client 1, 2)
echo.
echo  --- DANH SÁCH 10 BÀI LAB ÔN THI THƯỜNG KỲ ---
echo   [2]  Lab 1   : Định tuyến Router Server 2012 (RRAS nối 2 mạng LAN)
echo   [3]  Lab 2.1 : Quản trị Local User, Group, Security Policy, Share ^& NTFS
echo   [4]  Lab 2.2 : Nâng cấp Domain Controller AD DS ^& Join Domain máy trạm
echo   [5]  Lab 3   : Quản trị Đối tượng AD DS (OU, Group, User, Delegation)
echo   [6]  Lab 4   : Bảo mật AD DS ^& Group Policy (Password, Lockout, Audit)
echo   [7]  Lab 5   : Quản trị Chia sẻ, Phân quyền NTFS ^& ABE
echo   [8]  Lab 6   : Triển khai quản lý GPO nâng cao (Khóa CP, TaskMgr, CMD, Hình nền)
echo   [9]  Lab 7   : Triển khai User Profile (Home Folder, Roaming, Folder Redirection)
echo   [10] Lab 8   : Quản lý Dung lượng Đĩa (Disk Quota ^& FSRM File Screening)
echo   [11] Lab 9   : Cấu hình Domain đồng cấp (Secondary DC, Chuyển giao 5 FSMO Roles)
echo   [12] Lab 10  : Triển khai Dịch vụ Active Directory hoàn chỉnh (DNS Reverse Zone)
echo.
echo   [M] Mở Cẩm Nang Ôn Tập Toàn Diện 10 Bài Lab (Markdown)
echo   [Q] Thoát
echo ===============================================================================
set /p opt="Chọn bài Lab hoặc công cụ muốn thực thi [0-12, M, Q]: "

if /i "%opt%"=="0" (
    call "%~dp0Doi_IP_Theo_De_Bai.bat"
    goto MAIN_MENU
)

if /i "%opt%"=="1" (
    powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0test_connect_all_3.ps1"
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="2" (
    echo.
    echo [*] Đang thực thi cấu hình Lab 1 (Router RRAS)...
    powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0lab1_remote_config.ps1"
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="3" (
    echo.
    echo [*] Đang thực thi cấu hình Lab 2.1 (Local User, Group, Policy, Share, NTFS)...
    powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0lab2_apply_all_server_config.ps1"
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="4" (
    echo.
    echo [*] Đang thực thi cấu hình Lab 2.2 (Cài đặt AD DS & Promote DC)...
    powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0lab2t2_01_cai_dat_adds_va_promote_dc.ps1"
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="5" (
    echo.
    echo [*] Đang thực thi cấu hình Lab 3 (OU, Group, User, Delegation)...
    powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0lab3_01_tu_dong_quan_tri_adds.ps1"
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="6" (
    echo.
    echo [*] Đang thực thi cấu hình Lab 4 (GPO Security, Password, Lockout, Audit)...
    powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0lab4_automate_gpo.ps1"
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="7" (
    echo.
    echo [*] Đang thực thi cấu hình Lab 5 (Share, NTFS, ABE)...
    powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0lab5_automate_share_ntfs.ps1"
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="8" (
    echo.
    echo [*] Đang thực thi cấu hình Lab 6 (GPO Quản lý)...
    powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0lab6_automate_gpo.ps1"
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="9" (
    echo.
    echo [*] Đang thực thi cấu hình Lab 7 (User Profile, Home Folder, Roaming)...
    powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0lab7_automate_profile.ps1"
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="10" (
    echo.
    echo [*] Hướng dẫn Lab 8 (Disk Quota ^& FSRM):
    echo Mở File Server Resource Manager trên Server hoặc xem file CAM_NANG_10_LAB_THUONG_KY.md
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="11" (
    echo.
    echo [*] Lệnh Demo Lab 9 (Chuyển giao FSMO Roles):
    type "%~dp0LENH_DEMO_LAB9.txt"
    echo.
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="12" (
    echo.
    echo [*] Lệnh Demo Lab 10 (Triển khai Active Directory ^& DNS Reverse Lookup):
    type "%~dp0LENH_DEMO_LAB10.txt"
    echo.
    pause
    goto MAIN_MENU
)

if /i "%opt%"=="M" (
    start "" "%~dp0CAM_NANG_10_LAB_THUONG_KY.md"
    goto MAIN_MENU
)

if /i "%opt%"=="Q" (
    exit /b
)

goto MAIN_MENU
