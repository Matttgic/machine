import os
import requests

def send_telegram_message(msg, token=None, chat_id=None):
    token = token or os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = chat_id or os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("[Telegram] Token ou chat_id manquant !")
        return None
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": msg,
        "parse_mode": "Markdown"
    }
    try:
        print(f"[Telegram] Tentative d'envoi du message : {msg}")
        r = requests.post(url, data=payload, timeout=10)
        print(f"[Telegram] Code retour: {r.status_code}")
        print(f"[Telegram] Réponse: {r.text}")
        if r.status_code != 200:
            print("[Telegram] ERREUR lors de l'envoi du message.")
        return r
    except requests.RequestException as e:
        print(f"[Telegram] Exception lors de l'appel API : {e}")
        return None

# Pour tester directement :
if __name__ == "__main__":
    send_telegram_message("Test Telegram depuis le script !") 
