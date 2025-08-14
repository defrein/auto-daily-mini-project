@echo off
echo Running Daily Mini Project Generator Tests...
echo.

REM Change to script directory
cd /d "%~dp0"

REM Activate virtual environment if it exists
if exist ".venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call .venv\Scripts\activate.bat
)

REM Run the test script
python test.py

echo.
echo Press any key to exit...
pause >nul
