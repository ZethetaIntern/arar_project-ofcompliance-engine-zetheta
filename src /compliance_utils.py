# src/compliance_utils.py
from rapidfuzz import fuzz

def check_watchlist(client_name: str, watchlist: list) -> tuple:
    """
    Compare un nom de client avec une liste de noms sanctionnés.
    Retourne True si une ressemblance est détectée (score > 85).
    """
    for entry in watchlist:
        # score de 0 à 100
        score = fuzz.token_sort_ratio(client_name.lower(), entry.lower())
        if score > 85:
            return True, score
    return False, 0
