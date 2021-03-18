#Import
import requests
import json

# BET365 voleyball token
TOKEN = "76705-1xWfJDXyWYMoV5"

# Upcoming events url
URL_UPCOMING_EVENTS = "https://api.b365api.com/v2/events/upcoming?sport_id=91&" + "&" + "token=" + TOKEN 

# Odds event url without event_id
URL_EVENTS_ODDS = "https://api.b365api.com/v2/event/odds" + "?" + "token=" + TOKEN + "&" + "event_id=" 