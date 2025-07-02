import os
import pandas as pd
import joblib
from dotenv import load_dotenv
from get_today_matches import get_today_matches
from get_tennis_odds import get_odds
from features import compute_diff_features
from send_telegram import send_telegram_message

load_dotenv()

MODEL_PATH = "statsvalue_rf20_model.pkl"
DATA_DIR = "data"
THRESH_VALUE = 0.10
THRESH_ODD = 1.80
BET_SIZE = 20

def main():
    # Utilisation des vrais noms des fichiers normalisés
    model = joblib.load(MODEL_PATH)
    stats_atp = pd.read_csv(os.path.join(DATA_DIR, "stats_atp.norm.csv"))
    stats_wta = pd.read_csv(os.path.join(DATA_DIR, "stats_wta.norm.csv"))
    matches = get_today_matches()
    odds = get_odds()
    bets = []
    for match in matches.get("matches", []):
        # Format/normalize player names (à adapter selon retour API)
        # ...
        # Find odds for this match
        # ...
        feats = compute_diff_features(match, stats_atp if match.get("gender", "M") == "M" else stats_wta)
        if feats is None: continue
        proba = model.predict_proba([list(feats.values())])[0][1]
        odd1 = ... # à compléter selon format API
        proba_bk = 1/odd1 if odd1 else 0
        value = proba - proba_bk
        if value > THRESH_VALUE and odd1 >= THRESH_ODD:
            bets.append((match, value, proba, odd1))
    for m, value, proba, odd in bets:
        msg = f"Value bet détecté : {m['player1']} vs {m['player2']}\nCote : {odd}\nValue : {value*100:.1f}%\nProba modèle : {proba*100:.1f}%\nMise : {BET_SIZE}€"
        send_telegram_message(msg)

if __name__ == "__main__":
    main()
