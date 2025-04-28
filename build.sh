#!/bin/bash

# Check if venv exists, if not create it
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install requirements if needed
echo "Installing requirements..."
pip install -r requirements.txt

# Clean up
echo "Preliminary directory clean up..."
rm -rf build dist __pycache__

# Compilation
echo "Compiling..."
pyinstaller src/WordCampBadgeGenerator.spec

# Deactivate virtual environment
deactivate

# End
echo "Compilation complete"
