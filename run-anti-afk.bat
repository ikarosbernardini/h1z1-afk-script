@echo off
REM H1Z1 Anti-AFK Script Launcher
REM Right-click this file and select "Run as Administrator"

echo ===================================================
echo H1Z1 Anti-AFK Script Launcher
echo ===================================================
echo.
echo Checking for virtual environment...

if not exist "venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Please run setup-venv.bat first
    pause
    exit /b 1
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Starting anti-AFK script...
echo.
python h1z1-anti-afk.py

echo.
echo Script has ended.
pause
