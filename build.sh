#!/bin/bash

# Limpieza previa
echo "Limpiando directorios previos..."
rm -rf build dist __pycache__

# Compilación
echo "Compilando..."
pyinstaller WordCampBadgeGenerator.spec

# Fin
echo "¡Compilación terminada!"
