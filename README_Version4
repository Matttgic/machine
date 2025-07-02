# 🎾 StatsValue_RF20 – Tennis Value Betting Automation

Ce dépôt propose une solution complète de value bet tennis automatisée :
- Normalisation de données historiques ATP/WTA
- Modèle RandomForest sur features différentiels joueurs
- Prédiction et filtrage quotidien des value bets avec cotes réelles
- Envoi automatique via Telegram
- CI/CD via GitHub Actions 🚀

---

## Fonctionnalités
- **Normalisation automatique** des CSV (matchs, stats, format noms)
- **Notebook d’entraînement** du modèle (RandomForest, sklearn)
- **Scripts d’API** : récupération des fixtures et cotes du jour
- **Pipeline automatisé** (daily_run.py) : feature engineering, prédiction, value bet, notification
- **Envoi Telegram** des paris détectés
- **Tests unitaires** (pytest)
- **Logs détaillés** et gestion d’erreurs
- **CI/CD** (lint, test, run) via GitHub Actions

---

## Utilisation rapide

1. Cloner ce repo et placer les CSV bruts dans `data/` :
   - `matchs_atp.csv`
   - `matchs_wta.csv`
   - `stats_atp.csv`
   - `stats_wta.csv`
2. Lancer la normalisation :
    ```bash
    python src/normalize_csv.py
    ```
   Cela créera :
   - `matchs_atp.norm.csv`
   - `matchs_wta.norm.csv`
   - `stats_atp.norm.csv`
   - `stats_wta.norm.csv`
3. Entraîner le modèle :
    ```bash
    jupyter notebook notebooks/EDA_and_model_example.ipynb
    ```
4. Lancer le pipeline quotidien :
    ```bash
    python src/daily_run.py
    ```
5. Pour l’automatisation, ajouter vos secrets API/GITHUB dans `.env` et via les secrets GitHub, le workflow `.github/workflows/daily.yml` fera le reste.

---

## Configuration des secrets

Créer un fichier `.env` à la racine avec :
```
API_TENNIS_KEY=xxx
ODDS_API_KEY=xxx
TELEGRAM_BOT_TOKEN=xxx
TELEGRAM_CHAT_ID=xxx
```

---

## Structure

- `data/` : fichiers CSV bruts et normalisés
- `src/` : scripts Python
- `notebooks/` : notebooks d’EDA, ML
- `tests/` : tests unitaires
- `.github/workflows/` : CI/CD

---

## FAQ, détails, et schéma d’archi : voir `full_project_instructions_RF20.txt`

---

*Repo maintenu par @Matttgic – Contributions bienvenues !*
