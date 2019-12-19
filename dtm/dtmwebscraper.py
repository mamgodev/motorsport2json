#IMPORTS
import requests
import json
from bs4 import BeautifulSoup

#URL FROM THE WEBSITE
URL = "https://www.dtm.com/en/events"

#GET ALL THE WEBPAGE
data = requests.get(URL)

#USES HTML5LIB
soup = BeautifulSoup(data.content, 'html5lib')

#FIND THE INFO
dtmCalendar = soup.find_all('div', {"class": "Grid__GridCell-sc-145zbv4-1 eaGeCX"})

#ARRAY FOR THE EVENTS
dtmEvents = []

for content in dtmCalendar:

    #INFO
    name = content.find(class_='Text__Headline-sc-1yppgyo-0 cnFMbM').text
    date = content.find(class_='Text__Subheadline-sc-1yppgyo-2 ebBLBl').text
    circuitSrc = content.find(class_='circuit--light')['src']
    circuitName = content.find(class_='Text__Subheadline-sc-1yppgyo-2 dvRDzu').text

    #OBJECT WITH THE CONTENT OF THE EVENT
    dataEvent = {
        'name': name,
        'date': date,
        'circuitSrc': circuitSrc,
        'circuitName': circuitName
    }

    dtmEvents.append(dataEvent)

#TAKE THE ARRAY INTO A JSON FILE
for event in dtmEvents:
    dtmJson = json.dumps(event)
    print (dtmJson)

#NEEDS ENCODING UTF-8
with open('dtmdata.json', 'w') as outfile:
    json.dump(dtmEvents, outfile)
