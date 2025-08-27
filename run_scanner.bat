@echo off
REM PyAutoScan - Launcher
REM Tested on Python 3.13 with HP Printer scanner features

echo ========================================
echo PyAutoScan
echo ========================================
echo.
echo Choose an option:
echo 1. Basic Scanner
echo 2. Advanced Scanner  
echo 3. Scanner Information
echo 4. Exit
echo.

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo Starting Basic Scanner...
    python basic_scan.py
    pause
) else if "%choice%"=="2" (
    echo.
    echo Starting Advanced Scanner...
    python advanced_scan.py
    pause
) else if "%choice%"=="3" (
    echo.
    echo Getting Scanner Information...
    python scanner_info.py
    pause
) else if "%choice%"=="4" (
    echo.
    echo Exiting...
    exit /b 0
) else (
    echo.
    echo Invalid choice. Please try again.
    pause
    goto :eof
)

echo.
echo Operation completed. Press any key to continue...
pause >nul
