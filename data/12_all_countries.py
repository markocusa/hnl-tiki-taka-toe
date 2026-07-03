import json
import requests

with open("data/jsons/players_only_needed_clubs.json", "r", encoding="utf-8") as f:
    players = json.load(f)

countries = set() 

for id, value in players.items():
    for country in value["citizenship"]:
        countries.add(country)

with open("data/jsons/all_countries.json", "w", encoding="utf-8") as f:
    json.dump(sorted(countries), f, ensure_ascii=False, indent=2)

print("TOTAL COUNTRIES:", len(countries))