import os
import requests

def get_odds(api_key=None):
    api_key = api_key or os.getenv("ODDS_API_KEY")
    url = "https://api.the-odds-api.com/v4/sports/tennis/matches?apiKey=" + api_key
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None