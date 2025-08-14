@echo off
echo Generating Daily Mini Project NOW...
echo.

REM Change to script directory
cd /d "%~dp0"

REM Activate virtual environment if it exists
if exist ".venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call .venv\Scripts\activate.bat
)

REM Run the main script with --now flag
python daily_project_generator.py --now

REM Keep window open to see results
echo.
echo Press any key to exit...
pause >nul
