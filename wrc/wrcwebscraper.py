#IMPORTS
import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup

#URL FROM THE WEBSITE
URL = "https://www.wrc.com/es/"

#GET ALL THE WEBPAGE
data = requests.get(URL)

#USES HTML5LIB
soup = BeautifulSoup(data.content, 'html5lib')

#FIND THE DIV WITH THE CLASS CALENDAR-EVENT-CONTENT WHICH HAS ALL THE INFORMATION
wrcDivCalendar = soup.find_all('div', {"class": "calendar-event-content"})

#ARRAY FOR THE EVENTS
wrcEvents = []

for divEvent in wrcDivCalendar:

    #GET IMG FROM THE EVENT
    #HELP -- FIND THE CLASS WITH RALLY-LOGO AND GET THE CONTENT WITHIN SRC
    imgEvent = divEvent.find(class_='rally-logo')['src']

    #GET NAME EVENT
    nameEvent = divEvent.find(class_='rally-name').text

    #GET DATE EVENT
    dateEvent = divEvent.find('time').text

    #GET TIME (IT IS A TIMESTAMP SO NEEDS TO BE CONVERTED)
    timestampEvent = divEvent.find(class_='calendar-countdown-identifier')['data-timestamp']

    #CONVERTS TIMESTAMP TO DATA-TIME AND TRANSFORMS IT INTO STRING
    dataTimeEvent = datetime.fromtimestamp(int(timestampEvent)).strftime("%Y-%m-%d %H:%M:%S")

    #OBJECT WITH THE CONTENT OF THE EVENT
    dataEvent = {
        'imgSrc': imgEvent,
        'name': nameEvent,
        'date': dateEvent,
        'timestamp': timestampEvent,
        'dateTime': dataTimeEvent
    }

    wrcEvents.append(dataEvent)

#TAKE THE ARRAY INTO A JSON FILE
for event in wrcEvents:
    wrcJson = json.dumps(event)
    print (wrcJson)

with open('wrcdata.json', 'w') as outfile:
    json.dump(wrcEvents, outfile)
