# WordCamp Badge Generator

A desktop application to process WordCamp attendee CSV files and generate Excel files with embedded Gravatar images and QR codes, designed specifically for creating WordCamp badges and participant lists ready to import into Canva Pro.

---

## ✨ Features

- Read a WordCamp site CSV attendee file.
- Extract only name, surname, and email from the file.
- Normalize names and surnames (capitalize correctly).
- Generate Gravatar image URLs from email addresses.
- Download the Gravatar images and embed them directly into Excel cells (500x500 px).
- Generate QR codes linking to each attendee's Gravatar profile.
- Real-time logging and progress bar during processing.
- Simple desktop application with GUI (Tkinter).
- Ready to export and import directly into Canva Pro.

---

## 📂 Project Structure

```bash
WordCampBadgeGenerator/
├── src/
│   ├── WordCampBadgeGenerator.py
│   ├── WordCampBadgeGenerator.spec
├── └── assets/
│       ├── icon.ico  # Windows icon
│       └── icon.icns # Mac icon
├── .gitignore
├── build.bat
├── build.sh
├── LICENSE
├── README.md
└── requirements.txt
```

---

## ⚙️ Requirements

- Python 3.8+
- Recommended: Use a virtual environment
- Dependencies (from requirements.txt):
  - pillow
  - requests
  - openpyxl
  - pyinstaller
  - xlsxwriter
  - qrcode
  - tkinter

### Installing Tkinter

#### Windows
Tkinter usually comes included with the standard Python installation. However, if it's not installed:

1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, make sure to check the "tcl/tk and IDLE" box
3. Alternatively, you can install it using:
```bash
python -m pip install tk
```

#### macOS
Tkinter comes included with Python on macOS. If you need to install it manually:

1. Using Homebrew:
```bash
brew install python-tk
```

2. Or using the Python installer from [python.org](https://www.python.org/downloads/)

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

### Using a Virtual Environment (Recommended)

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python src/WordCampBadgeGenerator.py

# When finished, deactivate the virtual environment
deactivate
```

### Launch the application (without virtual environment)

```bash
python src/WordCampBadgeGenerator.py
```

---

## 🛠 How to Build Executable

### Windows (.exe)

```bash
python -m pyinstaller src/WordCampBadgeGenerator.spec
```

Make sure you have `icon.ico` in the correct path.

Output: `dist/WordCampBadgeGenerator.exe`

---

### MacOS (.app)

Before building, ensure PyInstaller is installed:
```bash
pip install pyinstaller
```

Then run:
```bash
python3 -m PyInstaller src/WordCampBadgeGenerator.spec
```

Make sure you have `icon.icns` in the correct path.

Output: `dist/WordCampBadgeGenerator.app`

---

## 📌 Notes

- The app is platform-dependent: you must compile on the same OS you intend to run it.
- The generated Excel file is immediately compatible with Canva Pro after this latest version.
- Gravatar images are automatically downloaded using attendee email addresses.
- QR codes link to each attendee's public Gravatar profile.
- Processing time may vary depending on the number of attendees.
- Real-time progress is shown during processing.

---

## ❤️ Credits

Created with ❤️ by for the WordCamp community.
