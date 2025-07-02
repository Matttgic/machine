import pandas as pd
from utils import format_player_name
import os

DATA_DIR = "data"

def normalize_matchs_csv(file_in, file_out):
    df = pd.read_csv(file_in)
    for c in ["Winner", "winner"]:
        if c in df.columns: df = df.rename(columns={c: "Player 1"})
    for c in ["Looser", "looser", "Loser"]:
        if c in df.columns: df = df.rename(columns={c: "Player 2"})
    df["Player 1"] = df["Player 1"].apply(format_player_name)
    df["Player 2"] = df["Player 2"].apply(format_player_name)
    df.to_csv(file_out, index=False)

def normalize_stats_csv(file_in, file_out):
    df = pd.read_csv(file_in)
    df["Player"] = df["Player"].apply(format_player_name)
    df.to_csv(file_out, index=False)

if __name__ == "__main__":
    os.makedirs(DATA_DIR, exist_ok=True)
    # Utilise les vrais noms de fichiers
    normalize_matchs_csv(os.path.join(DATA_DIR, "matchs_atp.csv"), os.path.join(DATA_DIR, "matchs_atp.norm.csv"))
    normalize_matchs_csv(os.path.join(DATA_DIR, "matchs_wta.csv"), os.path.join(DATA_DIR, "matchs_wta.norm.csv"))
    normalize_stats_csv(os.path.join(DATA_DIR, "stats_atp.csv"), os.path.join(DATA_DIR, "stats_atp.norm.csv"))
    normalize_stats_csv(os.path.join(DATA_DIR, "stats_wta.csv"), os.path.join(DATA_DIR, "stats_wta.norm.csv"))
    print("CSV normalization done.")