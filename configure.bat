@echo off
echo Daily Mini Project Generator - Configuration
echo ============================================
echo.

REM Change to script directory
cd /d "%~dp0"

REM Activate virtual environment if it exists
if exist ".venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call .venv\Scripts\activate.bat
    echo.
)

REM Run the configuration script
python configure.py

echo.
echo Press any key to exit...
pause >nul
