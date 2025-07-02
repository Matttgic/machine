import re
import unicodedata

def format_player_name(raw_name):
    """Format 'Jannik Sinner [ITA]' or 'Sinner Jannik' -> 'Sinner J.'"""
    name = unicodedata.normalize('NFKD', str(raw_name)).encode('ascii', errors='ignore').decode()
    name = re.sub(r"\[.*?\]", "", name).strip().replace("  ", " ")
    parts = name.split()
    if len(parts) >= 2:
        first, last = parts[0], parts[-1]
        if ',' in first:
            last = first.replace(',', '')
            first = parts[1]
        initial = first[0].upper() + "."
        return f"{last.capitalize()} {initial}"
    return name.capitalize()