@echo off
REM Setup script for H1Z1 Anti-AFK
REM Run this first to set up the virtual environment

echo ===================================================
echo H1Z1 Anti-AFK Setup
echo ===================================================
echo.

echo Checking for Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from python.org
    pause
    exit /b 1
)

echo Creating virtual environment...
python -m venv venv

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo ===================================================
echo Setup complete!
echo ===================================================
echo.
echo To run the anti-AFK script:
echo 1. Right-click "run-anti-afk.bat"
echo 2. Select "Run as Administrator"
echo.
pause
