#Imports
import requests
import json
from constants import URL_UPCOMING_EVENTS, URL_EVENTS_ODDS

#Main func
def main():
    #Get upcoming events id 
    events_ids = get_upcoming_events_ids()

    #Get odds upcoming events
    odds_events = get_odds_upcoming_events(events_ids)
    print (odds_events) 

#Get upcoming events ids 
def  get_upcoming_events_ids():
    response = requests.get(URL_UPCOMING_EVENTS)
    if response.status_code != 200:
        logging.error('unable to get response from url: ' + URL_UPCOMING_EVENTS)
        return
    upcoming_events = response.json()
    results_upcoming_events = upcoming_events['results']
    length_of_list = len(results_upcoming_events)
    events_ids = []
    for item in range  (0,length_of_list):
        event_id = results_upcoming_events[item]['id']
        events_ids.append(event_id)
    return events_ids

#Get odds upcoming events
def get_odds_upcoming_events(events_ids):
    odds_events = [] 
    for event_id in events_ids:
        URL_GET_EVENTS_ODDS = URL_EVENTS_ODDS  + str(event_id)
        response = requests.get(URL_GET_EVENTS_ODDS)
        if response.status_code != 200:
            logging.error('unable to get response from url: ' + URL_EVENTS_ODDS)
            return
        json_response_odds_events = response.json()
        odds_events.append(json_response_odds_events['results']['odds'])
    return odds_events
  
#Start program
main()
