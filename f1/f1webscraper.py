#IMPORTS
import requests
import json
from bs4 import BeautifulSoup

#URL FROM THE WEBSITE TO GET THE DATA
URL = "https://www.f1calendar.com/"

#GET ALL THE DATA FROM THE WEBSITE
data = requests.get(URL)

#USES HTML5LIB TO GET THE DATA
soup = BeautifulSoup(data.content, 'html5lib')

#FIND EVERY TBODY IN THE WEBPAGE
f1table = soup.find_all('tbody')

#ARRAY FOR THE EVENTS
f1events = []

#RUNS EVERY ROW FOUND IN THE TABLE
for row in f1table:
    #GET EVENT NAME
    columnaSummary = row.find(class_='summary')
    
    #GET EVENT LOCATION
    columnaLocation = row.find(class_='location')
    
    #GET EVENT DATE
    columnaDate = row.find(class_='date-column')
    
    #GET EVENT TIME
    columnaTime = row.find(class_='time-column')

    #OBJECT WITH THE CONTENT OF THE EVENT
    dataEvent = {
        'name': columnaSummary.get_text().strip(),
        'location': columnaLocation.get_text().strip(),
        'hour': columnaTime.get_text().strip(),
        'day': columnaDate.get_text().strip()
    }

    #INSERTS INTO ARRAY
    f1events.append(dataEvent)

#TAKE THE ARRAY INTO A JSON FILE
for event in f1events:
    f1json = json.dumps(event)
    print (f1json)

with open('f1data.json', 'w') as outfile:
    json.dump(f1events, outfile)

