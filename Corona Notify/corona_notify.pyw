#Imports
import datetime
import time
import requests
from plyer import notification

covidData = None

try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/germany")
except:
    print("No internet connection")

#if data then outputS
if (covidData != None):
    #data to JSON
    data = covidData.json()['Success']
    
    #repeat 
    while(True):
        notification.notify(
            #title
            title = "COVID19 Stats on {}".format(datetime.date.today()),
            #body
            message = "Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
                        totalcases = data['cases'],
                        todaycases = data['todayCases'],
                        todaydeaths = data['todayDeaths'],
                        active = data["active"]),  

            #stay for 50 sec
            timeout  = 50
        )
        #sleep 60sec * 60min * 4 ==> 4h
        time.sleep(60*60*4)