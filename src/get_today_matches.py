import requests
from datetime import datetime

def get_today_matches():
    api_key = "64ed4cebbc5e3cadbd15a7d84f879a6f3cd5a77170757298880e40198bb54553"
    today = datetime.now().strftime("%Y-%m-%d")
    url = f"https://api.api-tennis.com/tennis/?method=get_fixtures&APIkey={api_key}&date_start={today}&date_stop={today}"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            print("Réponse API fixtures :", data)
            return data
        else:
            print(f"Erreur API Tennis: {r.status_code} | Message: {r.text}")
            return None
    except requests.RequestException as e:
        print(f"Exception lors de l'appel API Tennis: {e}")
        return None 
