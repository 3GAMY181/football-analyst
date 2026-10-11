import os

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.football-data.org/v4"


def get_matches(competition="PL", status="FINISHED"):
    """بتجيب المباريات من الـ API وترجّعها كقايمة dicts مبسّطة"""
    token = os.getenv("FOOTBALL_DATA_TOKEN")
    url = f"{BASE_URL}/competitions/{competition}/matches?status={status}"

    response = requests.get(url, headers={"X-Auth-Token": token})
    response.raise_for_status()
    data = response.json()

    matches = []
    for match in data["matches"]:
        matches.append({
            "id": match["id"],
            "date": match["utcDate"],
            "matchday": match["matchday"],
            "home": match["homeTeam"]["name"],
            "away": match["awayTeam"]["name"],
            "home_goals": match["score"]["fullTime"]["home"],
            "away_goals": match["score"]["fullTime"]["away"],
        })
    return matches


if __name__ == "__main__":
    matches = get_matches()
    print(len(matches), "matches")
    print(matches[0])