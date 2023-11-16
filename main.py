import numpy as np
import csv
import os
from js import document

file_path = 'data.csv'

def obtener_puntuaciones():
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        puntuaciones = list(reader)
    return sorted(puntuaciones, key=lambda x: (float(x[1])*3+float(x[2]), 1/3 * (float(x[1])*3+float(x[2]))/(float(x[1]) + float(x[2]) + float(x[3])) ), reverse=True)

puntuaciones = [x for x in obtener_puntuaciones() if float(x[1]) + float(x[2]) + float(x[3]) >= 3]
puntos = [float(x[1])*3+float(x[2]) for x in puntuaciones]
effs = [(float(x[1])*3+float(x[2]))/(float(x[1]) + float(x[2]) + float(x[3])) for x in puntuaciones]
PJs = [float(x[1]) + float(x[2]) + float(x[3]) for x in puntuaciones]

max_eff = [i for i,x in enumerate(effs) if x == max(effs)]
max_PJ = [i for i,x in enumerate(PJs) if x == max(PJs)]

tabla = document.getElementById('tabla')

for i in range(len(puntuaciones)):
    
    row = tabla.insertRow(i+1)
    
    cell0 = row.insertCell(0)
    cell0.className = "name"
    cell0.innerHTML = puntuaciones[i][0]
    
    cell1 = row.insertCell(1)
    cell1.innerHTML = f'<b>{int(puntos[i])}</b>'
    
    cell2 = row.insertCell(2)
    cell2.appendChild(document.createTextNode(PJs[i]))
    
    cell3 = row.insertCell(3)
    cell3.appendChild(document.createTextNode(puntuaciones[i][1]))
    
    cell4 = row.insertCell(4)
    cell4.appendChild(document.createTextNode(puntuaciones[i][2]))
    
    cell5 = row.insertCell(5)
    cell5.appendChild(document.createTextNode(puntuaciones[i][3]))
    
    cell6 = row.insertCell(6)
    cell6.appendChild(document.createTextNode(f'{round(effs[i]*100/3, 2)}%'))
    
    if i in max_eff:
        row.className = "table-primary"
    
    if i in max_PJ:
        row.className = "table-warning"
    
    if i == 0:
        row.className = "table-success"
    
    if i == len(puntuaciones)-1:
        row.className = "table-danger"