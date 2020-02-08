#IMPORTS
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from bs4 import BeautifulSoup

#URL FROM THE WEBSITE
URL = "https://www.wrc.com/en/championship/calendar/wrc/"

#WEBDRIVER (NECESSARY BECAUSE WRC WONT GIVE ANYTHING)
driver = webdriver.Firefox(executable_path="./geckodriver")

#GET ALL THE WEBPAGE
driver.get(URL)

#USES HTML5LIB
#DRIVER.PAGE_SOURCE GIVES THE HTML
soup = BeautifulSoup(driver.page_source, 'html5lib')

#CLOSE BROWSER
driver.quit()

#GET THE TABLE
wrcTable = soup.find('tbody')

#GET ALL THE TR FROM THE TABLE
wrcTableTrs = wrcTable.find_all('tr')


#ARRAY FOR THE EVENTS
wrcEvents = []

for td in wrcTableTrs:

    nameEvent = td.find('a').text.replace('\n', '').strip()
    imgEvent = td.find(class_="flag")['src']
    tdTr = td.find_all('td')
    dateEvent = tdTr[2].text

    #OBJECT WITH THE CONTENT OF THE EVENT
    dataEvent = {
        'imgSrc': imgEvent,
        'name': nameEvent,
        'date': dateEvent,
    }
    wrcEvents.append(dataEvent)

#TAKE THE ARRAY INTO A JSON FILE
for event in wrcEvents:
    wrcJson = json.dumps(event)
    print (wrcJson)

with open('wrcdata.json', 'w') as outfile:
    json.dump(wrcEvents, outfile)
