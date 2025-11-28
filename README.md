# H1Z1 Just Survive Anti-AFK Script

This script prevents AFK kicks in H1Z1 Just Survive by simulating periodic player input.

## Important Notice

⚠️ **This script must be run on Windows Python, NOT in WSL2**

The script needs to control keyboard and mouse input for the H1Z1 game running on Windows.

## Setup Instructions

### 1. Switch from WSL to Windows VS Code

If you opened this folder in WSL:
1. Press `Ctrl+Shift+P` in VS Code
2. Select "Reopen Folder in Windows" or "Reopen Folder Locally"
3. Navigate to the folder on your Windows file system

### 2. Run Setup

Double-click `setup-venv.bat` to:
- Create a Python virtual environment
- Install required dependencies (pyautogui, keyboard)

### 3. Run the Script

**IMPORTANT:** The script requires Administrator privileges to capture keyboard input.

1. Right-click `run-anti-afk.bat`
2. Select **"Run as Administrator"**
3. Switch to H1Z1 within 5 seconds
4. The script will run automatically

## How to Stop the Script

- Press **ESC** key to stop gracefully
- Move mouse to **top-left corner** for emergency stop
- Press **Ctrl+C** in the terminal

## Configuration

You can edit `h1z1-anti-afk.py` to change:
- `CHECK_INTERVAL` - Time between actions (default: 120 seconds)
- `MOVEMENT_KEYS` - Which keys to press (default: W, A, S, D)
- `ENABLE_MOUSE_MOVEMENT` - Enable/disable mouse movements
- `ENABLE_KEY_PRESSES` - Enable/disable key presses

## Requirements

- Windows OS
- Python 3.7+
- Administrator privileges
- H1Z1 Just Survive game

## Files

- `h1z1-anti-afk.py` - Main script
- `requirements.txt` - Python dependencies
- `setup-venv.bat` - One-time setup script
- `run-anti-afk.bat` - Launcher (run as admin)
