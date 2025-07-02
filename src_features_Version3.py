def compute_diff_features(row, stats_df):
    """
    Calcule les features différentiels entre Player 1 et Player 2 à partir des stats globales.
    """
    p1 = stats_df[stats_df["Player"] == row["Player 1"]]
    p2 = stats_df[stats_df["Player"] == row["Player 2"]]
    if p1.empty or p2.empty:
        return None
    features = {}
    for col in stats_df.columns:
        if col == "Player": continue
        try:
            features[f"diff_{col}"] = float(p1.iloc[0][col]) - float(p2.iloc[0][col])
        except:
            features[f"diff_{col}"] = 0
    return features