# WordCamp Badge Generator

A desktop application to process CSV files and generate Excel files with embedded Gravatar images, designed specifically for creating WordCamp badges and participant lists ready to import into Canva Pro.

---

## ✨ Features

- Read a CSV file with participant data.
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
│   └── app.py
├── icons/
│   ├── icono.ico  # Windows icon
│   └── icono.icns # Mac icon
├── WordCampBadgeGenerator.spec
├── README.md
└── .gitignore
```

---

## ⚙️ Requirements

- Python 3.8+
- Recommended: Use a virtual environment

### Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have `requirements.txt`, manually install:

```bash
pip install openpyxl requests pillow pyinstaller
```

---

## 🚀 How to Run

### Launch the application

```bash
python src/app.py
```

---

## 🛠 How to Build Executable

### Windows (.exe)

```bash
python -m pyinstaller WordCampBadgeGenerator.spec
```

Make sure you have `icono.ico` in the correct path.

Output: `dist/WordCampBadgeGenerator/WordCampBadgeGenerator.exe`

---

### MacOS (.app)

```bash
python3 -m pyinstaller WordCampBadgeGenerator.spec
```

Make sure you have `icono.icns` in the correct path.

Output: `dist/WordCampBadgeGenerator/WordCampBadgeGenerator.app`

---

## 📌 Notes

- Windows requires `.ico` icons, MacOS requires `.icns` icons.
- The app is platform-dependent: you must compile on the same OS you intend to run it.
- The generated Excel file is immediately compatible with Canva Pro after this latest version.

---

## ❤️ Credits

Created with ❤️ for the WordCamp community.
