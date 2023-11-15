import numpy as np
import requests
from io import StringIO
import csv

url = 'https://raw.githubusercontent.com/javidelrojoo/javidelrojoo.github.io/main/data.csv'

r = requests.get(url)
text = r.iter_lines()
reader = np.genfromtxt(text, delimiter=',', dtype=None)

for row in reader:
    print(str(row[0]))