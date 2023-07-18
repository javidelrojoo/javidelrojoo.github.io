# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_frozen import Freezer
import csv
import os
import shutil

app = Flask(__name__)
freezer = Freezer(app)
# freezer.app.config['FREEZER_DESTINATION'] = '.'

file_path = os.path.join(os.path.dirname(__file__), 'data.csv')
def obtener_puntuaciones():
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        puntuaciones = list(reader)
    return sorted(puntuaciones, key=lambda x: (float(x[1])*3+float(x[2]), 1/3 * (float(x[1])*3+float(x[2]))/(float(x[1]) + float(x[2]) + float(x[3])) ), reverse=True)

@app.route('/')
def index():
    puntuaciones = obtener_puntuaciones()
    return render_template('index.html', puntuaciones=puntuaciones)

@freezer.register_generator
def index():
    yield '/'

if __name__ == '__main__':
    freezer.freeze()
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    shutil.copy('./build/index.html', './index.html')