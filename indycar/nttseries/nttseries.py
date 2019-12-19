#IMPORTS
import requests
import json
from bs4 import BeautifulSoup

#URL FROM THE WEBSITE
URL = "https://www.indycar.com/Schedule"

#GET ALL THE WEBPAGE
data = requests.get(URL)

#USES HTML5LIB
soup = BeautifulSoup(data.content, 'html5lib')

#FIND THE INFO
infoEvent = soup.find_all('li', {"class": "schedule-list__item"})

#ARRAY FOR THE EVENTS
nttEvents = []

for content in infoEvent:

    #INFO
    divLogoRace = content.find(class_='panel-trigger schedule-list__logo')
    logoRaceImgSrc = divLogoRace.find('img')['src']

    #RACE DATE
    divDateRace = content.find(class_='schedule-list__date')
    spanDateRace = divDateRace.find_all('span')
    monthDateRace = spanDateRace[0].text
    dayDateRace = spanDateRace[1].text

    #EVENT DESCRIPTION
    divEventDescription = content.find(class_='schedule-list__description')
    eventRaceTitle = divEventDescription.find(class_='panel-trigger schedule-list__title').text
    spanRacePlace = divEventDescription.find_all('span')
    eventRaceCircuit = spanRacePlace[0].text
    eventRacePlace = spanRacePlace[1].text
    eventRaceTime = divEventDescription.find(class_='timeEst').text
    
    #IMG CIRCUIT
    circuitRaceImgSrc = content.find(class_='schedule-list__track').find('img')['src']

    #OBJECT WITH THE CONTENT OF THE EVENT
    nntSeriesObject = {
        'title': eventRaceTitle,
        'place' : eventRacePlace,
        'circuit' : eventRaceCircuit,
        'circuitSrcImg' : circuitRaceImgSrc,
        'time' : eventRaceTime,
        'month' : monthDateRace,
        'day' : dayDateRace,
        'logoSrcImg' : logoRaceImgSrc,
    }

    nttEvents.append(nntSeriesObject)

#TAKE THE ARRAY INTO A JSON FILE
for event in nttEvents:
    nttSeriesJson = json.dumps(event)
    print (nttSeriesJson)

#NEEDS ENCODING UTF-8
with open('nttSeriesData.json', 'w') as outfile:
    json.dump(nttEvents, outfile)
