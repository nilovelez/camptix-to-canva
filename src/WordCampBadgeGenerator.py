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
    try:
        workbook = xlsxwriter.Workbook(excel_path)
        worksheet = workbook.add_worksheet("Procesado")

        # Configurar el formato de las celdas
        header_format = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter'})
        cell_format = workbook.add_format({'align': 'left', 'valign': 'vcenter'})

        # Escribir las cabeceras
        worksheet.write_row("A1", ["First Name", "Last Name", "Gravatar", "QR Gravatar"], header_format)

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
                gravatar_profile_url = f"https://api.gravatar.com/v3/qr-code/{gravatar_hash}?version=1&type=blank&size=500"

                worksheet.write(f"A{fila_excel}", nombre, cell_format)
                worksheet.write(f"B{fila_excel}", apellidos, cell_format)

                # Procesar imagen de Gravatar
                try:
                    response = requests.get(gravatar_url, timeout=10)
                    response.raise_for_status()
                    img_data = BytesIO(response.content)
                    worksheet.insert_image(f"C{fila_excel}", img_data, {"x_scale": 1.0, "y_scale": 1.0, "x_offset": 2, "y_offset": 2, "positioning": 1})
                except Exception as e:
                    log_callback(f"Error processing Gravatar for {email}: {str(e)}")
                    worksheet.write(f"C{fila_excel}", "(Error downloading image)", cell_format)

                # Procesar código QR de Gravatar
                try:
                    response = requests.get(gravatar_profile_url, timeout=10)
                    response.raise_for_status()
                    img_data = BytesIO(response.content)
                    worksheet.insert_image(f"D{fila_excel}", img_data, {"x_scale": 1.0, "y_scale": 1.0, "x_offset": 2, "y_offset": 2, "positioning": 1})
                except Exception as e:
                    log_callback(f"Error processing QR for {email}: {str(e)}")
                    worksheet.write(f"D{fila_excel}", "(Error downloading QR)", cell_format)

        # Ajustar el ancho de las columnas
        worksheet.set_column('A:A', 20)
        worksheet.set_column('B:B', 20)
        worksheet.set_column('C:D', 15)

        # Cerrar el workbook
        workbook.close()
        
        log_callback(f"Excel file saved successfully: {excel_path}")
        return True
    except Exception as e:
        log_callback(f"Error creating Excel file: {str(e)}")
        return False

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

            success = procesar_csv(csv_path, excel_path, safe_log, update_progress)
            if success:
                log_area.after(0, lambda: messagebox.showinfo("Success!!", f"File saved in:\n{excel_path}"))
            else:
                log_area.after(0, lambda: messagebox.showerror("Error", "Failed to create Excel file. Check the log for details."))
        except Exception as e:
            log_area.after(0, lambda: messagebox.showerror("Error", str(e)))
        finally:
            log_area.after(0, lambda: btn.config(state=tk.NORMAL))

    threading.Thread(target=run_proceso).start()

# Configuración ventana principal
root = tk.Tk()
root.title("WordCamp Badge Generator")
root.geometry("540x400")

# Establecer el icono de la ventana
try:
    # Intentar cargar el icono desde la ruta relativa
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "icon.ico")
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)
    else:
        # Si no se encuentra, intentar cargar desde la ruta absoluta
        root.iconbitmap("src/assets/icon.ico")
except Exception as e:
    print(f"No se pudo cargar el icono: {e}")

frame = tk.Frame(root)
frame.pack(pady=10, fill=tk.X, padx=20)

# Instrucciones
label_bold = tk.Label(
    frame,
    text="1. Download the attendees file from your WordCamp site.",
    justify="left",
    font=("Helvetica", 10, "bold"),
    wraplength=500
)
label_bold.pack(anchor="w", fill=tk.X, pady=(0, 5))

label_normal = tk.Label(
    frame,
    text="Go to Tickets > Tools > Generate Badges > Create Badges with InDesign",
    justify="left",
    font=("Helvetica", 10),
    wraplength=500
)
label_normal.pack(anchor="w", fill=tk.X, pady=(0, 10))

btn = tk.Button(frame, text="2. Select Attendee CSV file", command=ejecutar)
btn.pack(pady=10)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=500, mode="determinate")
progress_bar.pack(padx=(0, 20), pady=10)

log_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=14)
log_area.pack(padx=10, pady=10)

root.mainloop()

