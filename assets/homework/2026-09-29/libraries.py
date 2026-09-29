# CODE_RUNNER: 3.14 Homework - UESL season statistics
import json
import statistics
from datetime import date

def summarize_season(season):
    """Summarize games without modifying the input.

    Parameters:
        season: list of dictionaries with date (ISO string), opponent (string),
                and points (nonnegative number; goals in this simulated season).
    Returns:
        dict containing total_points, average_points rounded to one decimal,
        best_game (largest points value), and points_by_opponent totals.
        An empty season returns total 0, mean None, best None, and an empty map.
    """
    points = [game["points"] for game in season]
    by_opponent = {}
    for game in season:
        opponent = game["opponent"]
        by_opponent[opponent] = by_opponent.get(opponent, 0) + game["points"]
    return {
        "total_points": sum(points),
        "average_points": round(statistics.mean(points), 1) if points else None,
        "best_game": max(points) if points else None,
        "points_by_opponent": by_opponent,
    }

games = [
    {"date": "2026-09-10", "opponent": "Comets", "points": 6},
    {"date": "2026-09-14", "opponent": "Falcons", "points": 4},
    {"date": "2026-09-18", "opponent": "Comets", "points": 8},
    {"date": "2026-09-22", "opponent": "Meteors", "points": 7},
    {"date": "2026-09-26", "opponent": "Falcons", "points": 5},
]
as_of = date(2026, 9, 29)
next_game = date(2026, 10, 10)
report = summarize_season(games)
report["sport"] = "Rocket League (simulated goals)"
report["report_date"] = as_of.isoformat()
report["next_game"] = next_game.isoformat()
report["days_until_next_game"] = (next_game - as_of).days
print(json.dumps(report, indent=2, sort_keys=True))
requirements_txt = """# Hypothetical full app: table processing and Flask scoreboard.
# json, datetime, and statistics come with Python and are not pip packages.
pandas
Flask==3.1.3
"""
print("requirements.txt:")
print(requirements_txt)
