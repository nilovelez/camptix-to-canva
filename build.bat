@echo off

REM Clean up
echo Preliminary directory clean up...
rmdir /s /q build
rmdir /s /q dist
rmdir /s /q __pycache__

REM Compilation
echo Compiling...
pyinstaller src/WordCampBadgeGenerator.spec

REM End
echo Compilation complete
pause
