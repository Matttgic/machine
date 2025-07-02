def compute_diff_features(row, stats_df):
    """
    Calcule les features différentiels entre les deux joueurs à partir des stats globales.
    """
    p1 = stats_df[stats_df["Player"] == row["event_first_player"]]
    p2 = stats_df[stats_df["Player"] == row["event_second_player"]]
    if p1.empty or p2.empty:
        return None
    features = {}
    for col in stats_df.columns:
        if col == "Player":
            continue
        try:
            features[f"diff_{col}"] = float(p1.iloc[0][col]) - float(p2.iloc[0][col])
        except Exception:
            features[f"diff_{col}"] = 0
    return features 
