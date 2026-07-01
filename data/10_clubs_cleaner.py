import json
import requests

with open("data/jsons/players_final.json", "r", encoding="utf-8") as f:
    players = json.load(f)

clubs=set()
for id,value in players.items():
    for c in value["clubs"]:
        clubs.add(c.strip())

clubs=sorted(clubs)
print(len(clubs))


with open("data/jsons/clubs_list.json", "w", encoding="utf-8") as f:
    json.dump(sorted(clubs), f, ensure_ascii=False, indent=2)