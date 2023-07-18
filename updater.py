import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
import csv
import os

file_path = os.path.join(os.path.dirname(__file__), 'data.csv')

def seleccionar_valores():
    seleccionados = []
    for combo in combos:
        valor = combo.get()
        if valor:
            seleccionados.append(valor)

    if len(set(seleccionados)) != len(seleccionados):
        messagebox.showwarning("Error", "No podes repetir jugadores.")
        return
    # if len(seleccionados) != 10:
    #     messagebox.showwarning("Error", "Debes seleccionar exactamente 10 valores.")
    #     return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        data = list(csv.reader(file))
        for row in data:
            if check_var.get() and row[0] in seleccionados:
                row[2] = int(row[2]) + 1
            if not check_var.get() and row[0] in seleccionados[:5]:
                row[1] = int(row[1]) + 1
            if not check_var.get() and row[0] in seleccionados[5:]:
                row[3] = int(row[3]) + 1
    
    with open(file_path, 'w', encoding='utf-8') as file:
        escritor_csv = csv.writer(file)
        escritor_csv.writerows(data)
    messagebox.showinfo("Guardado Exitoso", "Se guardó el resultado del partido")
    return

def agregar_jugador():
    
    def guardar_valor():
        valor = entry_valor.get()
        
        with open(file_path, 'r', encoding='utf-8') as file:
            data = list(csv.reader(file))
            for row in data:
                if valor == row[0]:
                    messagebox.showwarning("Error", "Este jugador ya existe.")
                    return
        
        with open(file_path, 'a', newline='\n') as file:
            escritor_csv = csv.writer(file)
            escritor_csv.writerow([valor, 0, 0, 0])
        
        lista_valores = cargar_valores()
        for combo in combos:
            combo['values'] = lista_valores
        messagebox.showinfo("Nuevo jugador guardado", f"{valor} se guardó como nuevo jugador.")
        ventana_nueva.destroy()

    ventana_nueva = tk.Toplevel(root)
    ventana_nueva.title("Agregar jugador")
    ventana_nueva.configure(padx=20, pady=20)

    label = tk.Label(ventana_nueva, text="Ingresa un nuevo jugador:")
    label.pack()

    entry_valor = tk.Entry(ventana_nueva)
    entry_valor.pack()

    btn_guardar = tk.Button(ventana_nueva, text="Guardar", command=guardar_valor)
    btn_guardar.pack()
    return

def cargar_valores():
    with open(file_path, 'r', encoding='utf-8') as file:
        return [fila[0] for fila in list(csv.reader(file))]

lista_valores = cargar_valores()
root = tk.Tk()

combos = []

font = Font(weight="bold")
label_col1 = tk.Label(root, text="Equipo Ganador", font=font)
label_col1.grid(row=0, column=0, padx=10, pady=5)
label_col2 = tk.Label(root, text="Equipo Perdedor", font=font)
label_col2.grid(row=0, column=1, padx=10, pady=5)

for i in range(5):
    combo = ttk.Combobox(root, values=lista_valores, state="readonly", width=20)
    combo.grid(row=i+1, column=0, padx=10, pady=10)
    combos.append(combo)

for i in range(5):
    combo = ttk.Combobox(root, values=lista_valores, state="readonly", width=20)
    combo.grid(row=i+1, column=1, padx=10, pady=10)
    combos.append(combo)

check_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(root, text="Hubo empate", variable=check_var)
checkbutton.grid(row=7, columnspan=2, padx=10, pady=10)

btn_seleccionar = tk.Button(root, text="Guardar", command=seleccionar_valores)
btn_seleccionar.grid(row=8, columnspan=2, padx=10, pady=10)

btn_agregar_jugador = tk.Button(root, text="Agregar Jugador", command=agregar_jugador)
btn_agregar_jugador.grid(row=9, columnspan=2, padx=10, pady=10)

root.mainloop()

