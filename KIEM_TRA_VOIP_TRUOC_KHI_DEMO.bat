@echo off
chcp 65001 >nul
title KIỂM TRA HỆ THỐNG VOIP TRƯỚC KHI DEMO
python "%~dp0check_voip_health.py"
echo.
pause
