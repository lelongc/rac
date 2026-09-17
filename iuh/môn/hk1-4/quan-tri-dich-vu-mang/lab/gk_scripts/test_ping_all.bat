@echo off
title KIEM TRA KET NOI MANG 4 MAY
color 0e

echo ==============================================================================
echo                 KIEM TRA PING GIUA 4 MAY TRONG HE THONG
echo ==============================================================================

echo [1] Ping Ubuntu 1 (Gateway LAN 1 - 192.168.5.2):
ping -n 2 192.168.5.2
echo.

echo [2] Ping Win 7_1 (LAN 1 - 192.168.5.1):
ping -n 2 192.168.5.1
echo.

echo [3] Ping Ubuntu 1 (Gateway LAN 2 - 192.168.6.3):
ping -n 2 192.168.6.3
echo.

echo [4] Ping Ubuntu 2 (LAN 2 - 192.168.6.2):
ping -n 2 192.168.6.2
echo.

echo [5] Ping Win 7_2 (LAN 2 - 192.168.6.1):
ping -n 2 192.168.6.1
echo.

echo ==============================================================================
echo DA KIEM TRA XONG!
echo ==============================================================================
pause
