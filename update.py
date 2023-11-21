import csv
import os
from js import document

def actualizar_csv(winners, losers, draw = False):
    file_path = 'data.csv'
    with open(file_path, 'r', encoding='utf-8') as file:
        data = list(csv.reader(file))
        for row in data:
            if draw and row[0] in winners + losers:
                row[2] = int(row[2]) + 1
            if not draw and row[0] in winners:
                row[1] = int(row[1]) + 1
            if not draw and row[0] in losers:
                row[3] = int(row[3]) + 1
    
    with open(file_path, 'w', encoding='utf-8', newline='\n') as file:
        escritor_csv = csv.writer(file)
        escritor_csv.writerows(data)

def get_players():
    for i in range(6):
        winner = document.getElementById(f'winner{i}').getElementsByTagName('select')
        print(winner.value)

with open('data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    puntuaciones = list(reader)

names_options = [f'<option>{x[0]}</option>' for x in puntuaciones]
select_text = f'<select class="form-control"><option>Seleccionar jugador</option>{"".join(names_options)}</select>'

form = document.getElementById('form')

for i in range(6):

    newRow = form.appendChild(document.createElement('div'))
    newRow.className = 'row mark'
    
    newCol = newRow.appendChild(document.createElement('div'))
    newCol.className = 'col'
    newCol.innerHTML = select_text
    newCol.setAttribute('id', f'winner{i}')
    
    newCol = newRow.appendChild(document.createElement('div'))
    newCol.className = 'col'
    newCol.innerHTML = select_text
    newCol.setAttribute('id', f'loser{i}')

get_players()