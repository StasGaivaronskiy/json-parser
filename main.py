#Imports
import requests
import json
from constants import URL_UPCOMING_EVENTS, URL_EVENTS_ODDS

#main func
def main():
    #Get upcoming events id 
    events_id = get_upcoming_events()

    #Get odds upcoming events
    oddsEvents = get_odds_upcoming_events(events_id)
    print (oddsEvents) 

def  get_upcoming_events():
    response = requests.get(URL_UPCOMING_EVENTS)
    if response.status_code != 200:
        logging.error('unable to get response from url: ' + URL_UPCOMING_EVENTS)
        return
    upcomingEvents = response.json()
    resultsUpcomingEvents = upcomingEvents['results']
    lengthOfList = len (resultsUpcomingEvents)
    events_id = []
    for i in range  (0,lengthOfList):
        event_id = resultsUpcomingEvents[i]['id']
        events_id.append(event_id)
    return events_id

#Get odds upcoming events
def get_odds_upcoming_events(events_id):
    oddsEvents = [] 
    for event_id in events_id:
        URL_GET_EVENTS_ODDS = URL_EVENTS_ODDS  + str(event_id)
        response = requests.get(URL_GET_EVENTS_ODDS)
        if response.status_code != 200:
            logging.error('unable to get response from url: ' + URL_EVENTS_ODDS)
            return
        jsonResponseOddsEvents = response.json()
        oddsEvents.append(jsonResponseOddsEvents)
    return oddsEvents
  
#start program
main()
