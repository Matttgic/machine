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
    # Chargement des modèles et données
    model = joblib.load(MODEL_PATH)
    stats_atp = pd.read_csv(os.path.join(DATA_DIR, "stats_atp.norm.csv"))
    stats_wta = pd.read_csv(os.path.join(DATA_DIR, "stats_wta.norm.csv"))
    matches = get_today_matches()
    odds = get_odds()
    bets = []

    # Envoi la liste des matchs du jour (optionnel)
    if matches and matches.get("result"):
        msg = "📅 Matchs du jour :\n"
        for match in matches["result"]:
            joueur1 = match.get('event_first_player')
            joueur2 = match.get('event_second_player')
            heure = match.get('event_time')
            tournoi = match.get('tournament_name')
            msg += f"- {joueur1} vs {joueur2} ({tournoi}) à {heure}\n"
        send_telegram_message(msg)

    # Détection des value bets
    if matches is None or matches.get("success") != 1 or "result" not in matches or not matches["result"]:
        send_telegram_message("❌ Aucun match trouvé ou erreur API.")
        return

    for match in matches["result"]:
        gender = "M" if "atp" in match.get("event_type_type", "").lower() else "F"
        feats = compute_diff_features(match, stats_atp if gender == "M" else stats_wta)
        if feats is None: continue
        proba = model.predict_proba([list(feats.values())])[0][1]
        odd1 = ... # à compléter selon format API des cotes
        proba_bk = 1/odd1 if odd1 else 0
        value = proba - proba_bk
        if value > THRESH_VALUE and odd1 >= THRESH_ODD:
            bets.append((match, value, proba, odd1))

    # Envoi un message pour chaque pari détecté
    for m, value, proba, odd in bets:
        msg = (
            f"Value bet détecté : {m['event_first_player']} vs {m['event_second_player']}\n"
            f"Cote : {odd}\n"
            f"Value : {value*100:.1f}%\n"
            f"Proba modèle : {proba*100:.1f}%\n"
            f"Mise : {BET_SIZE}€"
        )
        send_telegram_message(msg)

    # Si aucun value bet détecté
    if not bets:
        send_telegram_message("❌ Aucun value bet détecté aujourd'hui.")

if __name__ == "__main__":
    main() 
