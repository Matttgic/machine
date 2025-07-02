import os
import requests

def send_telegram_message(msg, token=None, chat_id=None):
    token = token or os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = chat_id or os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": msg, "parse_mode": "Markdown"}
    r = requests.post(url, data=payload)
    if r.status_code != 200:
        print("Telegram error:", r.text)
    return r
