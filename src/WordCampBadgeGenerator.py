import csv
import hashlib
import os
import requests
import xlsxwriter
from PIL import Image
from io import BytesIO
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import threading

def capitalizar(texto):
    return ' '.join([palabra.capitalize() for palabra in texto.strip().lower().split()])

def procesar_csv(csv_path, excel_path, log_callback, progress_callback):
    workbook = xlsxwriter.Workbook(excel_path)
    worksheet = workbook.add_worksheet("Procesado")

    worksheet.write_row("A1", ["First Name", "Last Name", "Gravatar"])

    imagenes_temporales = []

    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = list(csv.reader(csvfile))
        total_filas = len(reader) - 1
        reader = iter(reader)
        next(reader)  # saltar cabecera

        for i, fila in enumerate(reader):
            fila_excel = i + 1 + 1  # +1 por 0-index y +1 por cabecera

            if len(fila) < 5:
                continue

            nombre = capitalizar(fila[2])
            apellidos = capitalizar(fila[3])
            email = fila[4].strip().lower()

            log_callback(f"Processing: {email}")
            progress_callback(i + 1, total_filas)

            hash_obj = hashlib.sha256(email.encode('utf-8'))
            gravatar_hash = hash_obj.hexdigest()
            gravatar_url = f"http://www.gravatar.com/avatar/{gravatar_hash}.png?s=500&default=mp"

            worksheet.write(f"A{fila_excel}", nombre)
            worksheet.write(f"B{fila_excel}", apellidos)

            try:
                response = requests.get(gravatar_url, timeout=10)
                response.raise_for_status()
                img = Image.open(BytesIO(response.content)).convert("RGB")
                img_path = f"temp_avatar_{i}.png"
                img.save(img_path)
                imagenes_temporales.append(img_path)

                worksheet.insert_image(f"C{fila_excel}", img_path, {"x_scale": 1.0, "y_scale": 1.0, "x_offset": 2, "y_offset": 2, "positioning": 1})

            except Exception as e:
                log_callback(f"Error processing {email}: {str(e)}")
                worksheet.write(f"C{fila_excel}", "(Error downloading image)")

    workbook.close()

    for img_path in imagenes_temporales:
        try:
            os.remove(img_path)
        except Exception as e:
            log_callback(f"Coudn't delete {img_path}: {str(e)}")

# GUI

def seleccionar_archivo():
    return filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

def guardar_como():
    return filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

def ejecutar():
    csv_path = seleccionar_archivo()
    if not csv_path:
        return
    excel_path = guardar_como()
    if not excel_path:
        return

    log_area.delete(1.0, tk.END)
    btn.config(state=tk.DISABLED)
    progress_bar['value'] = 0

    def run_proceso():
        try:
            def safe_log(msg):
                log_area.after(0, lambda: log_area.insert(tk.END, msg + "\n") or log_area.see(tk.END))

            def update_progress(current, total):
                percent = int((current / total) * 100)
                progress_bar.after(0, lambda: progress_bar.config(value=percent))

            procesar_csv(csv_path, excel_path, safe_log, update_progress)
            log_area.after(0, lambda: messagebox.showinfo("Success!!", f"File saved in:\n{excel_path}"))
        except Exception as e:
            log_area.after(0, lambda: messagebox.showerror("Error", str(e)))
        finally:
            log_area.after(0, lambda: btn.config(state=tk.NORMAL))

    threading.Thread(target=run_proceso).start()

# Configuración ventana principal
root = tk.Tk()
root.title("WordCamp Badge Generator")
root.geometry("540x400")

frame = tk.Frame(root)
frame.pack(pady=10)

# Instrucciones
label_bold = tk.Label(
    frame,
    text="Download the attendees file from your WordCamp site.",
    justify="left",
    font=("Helvetica", 10, "bold")
)
label_bold.pack(anchor="w", padx=20)

label_normal = tk.Label(
    frame,
    text="Go to Tickets > Tools > Generate Badges > Create Badges with InDesign",
    justify="left",
    font=("Helvetica", 10)
)
label_normal.pack(anchor="w", padx=20, pady=(0, 10))

btn = tk.Button(frame, text="Select Attendee CSV file", command=ejecutar)
btn.pack()

progress_bar = ttk.Progressbar(root, orient="horizontal", length=500, mode="determinate")
progress_bar.pack(padx=(0, 20), pady=10)

log_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=14)
log_area.pack(padx=10, pady=10)

root.mainloop()

