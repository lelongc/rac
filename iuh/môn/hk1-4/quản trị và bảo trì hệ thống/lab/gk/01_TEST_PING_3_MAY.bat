@echo off
chcp 65001 >nul
title KIEM TRA KET NOI VA TEST PING 3 MAY - GK QTBTHT
color 0A
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0test_connect_all_3.ps1"
pause
