@echo off
echo Starting Daily Mini Project Generator...
echo.

REM Change to script directory
cd /d "%~dp0"

REM Activate virtual environment if it exists
if exist ".venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call .venv\Scripts\activate.bat
)

REM Run the main script
python daily_project_generator.py

REM Keep window open if there's an error
if errorlevel 1 (
    echo.
    echo An error occurred. Press any key to exit...
    pause >nul
)
