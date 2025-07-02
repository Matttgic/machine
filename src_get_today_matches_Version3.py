import os
import requests

def get_today_matches(api_key=None):
    api_key = api_key or os.getenv("API_TENNIS_KEY")
    url = "https://api-tennis.com/v1/matches?date=today"
    headers = {"X-API-KEY": api_key}
    r = requests.get(url, headers=headers)
    return r.json() if r.status_code == 200 else None