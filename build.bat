@echo off

REM Limpieza previa
echo Limpiando directorios previos...
rmdir /s /q build
rmdir /s /q dist
rmdir /s /q __pycache__

REM Compilación
echo Compilando...
pyinstaller WordCampBadgeGenerator.spec

REM Fin
echo ¡Compilación terminada!
pause
