# 📄 CSV to Excel Converter with Embedded Gravatar Images

This project is a simple GUI tool written in Python that:

- Reads a CSV file
- Extracts the 3rd, 4th, and 5th columns (Name, Last Name, and Email)
- Capitalizes names and last names
- Generates a SHA256-based Gravatar image for each email
- Downloads and embeds the Gravatar image into an Excel (.xlsx) file
- Saves the processed output, ready for tools like Canva Pro that require images to be embedded in cells

---

## 🖥️ Features

- User-friendly interface (no command line needed)
- Embedded Gravatar images in Excel (not just links)
- Compatible with **Windows** and **macOS**
- Clean output ideal for graphic design platforms like Canva

---

## 🧰 Requirements

Before running the script or compiling, install dependencies:

```bash
pip install openpyxl requests pillow
```

If you plan to build the executable:

```bash
pip install pyinstaller
```

---

## ▶️ How to Run (Development Mode)

Just run the script directly:

```bash
python gravatar_excel_gui.py
```

A window will pop up:
1. Select your `.csv` file
2. Choose where to save the resulting `.xlsx`

---

## ⚙️ How to Build Executables

### 🪟 Windows

```bash
pyinstaller --noconfirm --onefile --windowed gravatar_excel_gui.py
```

Output file:  
`dist/gravatar_excel_gui.exe`

---

### 🍏 macOS

```bash
pyinstaller --noconfirm --windowed gravatar_excel_gui.py
```

Output file:  
`dist/gravatar_excel_gui.app`

> Optional: Convert `.app` into a `.dmg` if needed using tools like `create-dmg`.

---

## 📂 Project Structure

```
.
├── gravatar_excel_gui.py       # Main script
├── README.md
└── requirements.txt            # Optional: pip freeze > requirements.txt
```

---

## 📌 Notes

- The app uses the standar attendee csv from camptix
- Images are resized to 50x50 pixels inside the Excel file.

---

## 📥 Example camptix CSV Format

| Attendee ID | Ticket Type | First Name | Last Name  | E-mail Address   |
|-------------|-------------|------------|------------|------------------|
| 1234        | General     | john       | doe        | john@example.com |

---

## 📃 License

MIT License
