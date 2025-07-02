import requests

def send_telegram_message(msg):
    token = "7850560556:AAG9iH9RXyo2maRtIv8RgdJ_N4TStdZQXDg"
    chat_id = "291627358"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": msg,
        "parse_mode": "Markdown"
    }
    try:
        print(f"[Telegram] Envoi du message : {msg}")
        r = requests.post(url, data=payload, timeout=10)
        print(f"[Telegram] Code retour: {r.status_code}")
        print(f"[Telegram] Réponse: {r.text}")
        if r.status_code != 200:
            print("[Telegram] ERREUR lors de l'envoi du message.")
        return r
    except requests.RequestException as e:
        print(f"[Telegram] Exception lors de l'appel API : {e}")
        return None

# Test direct
if __name__ == "__main__":
    send_telegram_message("Test Telegram depuis le script avec token et chat_id en dur !") 
