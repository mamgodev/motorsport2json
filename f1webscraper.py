import requests
import json
from bs4 import BeautifulSoup

URL = "https://www.f1calendar.com/"
datos = requests.get(URL)

soup = BeautifulSoup(datos.content, 'html5lib')
f1table = soup.find_all('tbody')

f1events = []

for row in f1table:
    columnaSummary = row.find(class_='summary')
    columnaLocation = row.find(class_='location')
    columnaDate = row.find(class_='date-column')
    columnaTime = row.find(class_='time-column')

    datos = {
        'nombre': columnaSummary.get_text().strip(),
        'localizacion': columnaLocation.get_text().strip(),
        'hora': columnaTime.get_text().strip(),
        'dia': columnaDate.get_text().strip()
    }
    f1events.append(datos)

for data in f1events:
    f1json = json.dumps(data)
    print (f1json)

with open('f1data.json', 'w') as outfile:
    json.dump(f1events, outfile)