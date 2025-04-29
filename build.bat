@echo off

REM Check if venv exists, if not create it
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install requirements if needed
echo Installing requirements...
pip install -r requirements.txt

REM Clean up
echo Preliminary directory clean up...
rmdir /s /q build
rmdir /s /q __pycache__
rmdir /s /q dist\WordCampBadgeGenerator

REM Compilation
echo Compiling...
pyinstaller src/WordCampBadgeGenerator.spec

REM Deactivate virtual environment
call venv\Scripts\deactivate.bat

REM End
echo Compilation complete
pause
