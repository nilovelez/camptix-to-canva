#!/bin/bash

# Clean up
echo "Preliminary directory clean up..."
rm -rf build dist __pycache__

# Compilation
echo "Compiling..."
pyinstaller src/WordCampBadgeGenerator.spec

# End
echo "Compilation complete"
