# WordCamp Badge Generator

A desktop application to process WordCamp attendee CSV files and generate Excel files with embedded Gravatar images, designed specifically for creating WordCamp badges and participant lists ready to import into Canva Pro.

---

## ✨ Features

- Read a WordCamp site CSV attendee file.
- Extract only name, surname, and email from the file.
- Normalize names and surnames (capitalize correctly).
- Generate Gravatar image URLs from email addresses.
- Download the Gravatar images and embed them directly into Excel cells (500x500 px).
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
│       ├── icono.ico  # Windows icon
│       └── icono.icns # Mac icon
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

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

### Launch the application

```bash
python src/WordCampBadgeGenerator.py
```

---

## 🛠 How to Build Executable

### Windows (.exe)

```bash
python -m pyinstaller src/WordCampBadgeGenerator.spec
```

Make sure you have `icono.ico` in the correct path.

Output: `dist/WordCampBadgeGenerator.exe`

---

### MacOS (.app)

```bash
python3 -m pyinstaller src/WordCampBadgeGenerator.spec
```

Make sure you have `icono.icns` in the correct path.

Output: `dist/WordCampBadgeGenerator.app`

---

## 📌 Notes

- The app is platform-dependent: you must compile on the same OS you intend to run it.
- The generated Excel file is immediately compatible with Canva Pro after this latest version.

---

## ❤️ Credits

Created with ❤️ for the WordCamp community.
