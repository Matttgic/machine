import requests

def get_odds(api_key=None):
    # Clé API insérée en dur pour usage privé
    api_key = api_key or "3975a5fa068301552ee689f6598d7e6f"
    url = f"https://api.the-odds-api.com/v4/sports/tennis/matches?apiKey={api_key}"
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None 
