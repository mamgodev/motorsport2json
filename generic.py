#IMPORTS
import requests
import json
from bs4 import BeautifulSoup

#URL FROM THE WEBSITE
URL = "url"

#GET ALL THE WEBPAGE
data = requests.get(URL)

#USES HTML5LIB
soup = BeautifulSoup(data.content, 'html5lib')

#FIND THE INFO
infoEvent = soup.find_all('div', {"class": "calendar-event-content"})

#ARRAY FOR THE EVENTS
array = []

for content in array:

    #INFO
    name = content.find(class_='content')

    #OBJECT WITH THE CONTENT OF THE EVENT
    object = {
        'name': name,
    }

    array.append(object)

#TAKE THE ARRAY INTO A JSON FILE
for event in array:
    arrayJson = json.dumps(event)
    print (arrayJson)

with open('generic.json', 'w') as outfile:
    json.dump(array, outfile)
