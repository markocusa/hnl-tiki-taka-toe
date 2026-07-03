import json

with open("data/jsons/players_final.json", "r", encoding="utf-8") as f:
    players = json.load(f)
with open("data/jsons/clubs_3.json", "r", encoding="utf-8") as f:
    clubs = json.load(f)

players2 = {}

for id,value in players.items():
    player_clubs = set()
    for c in value["clubs"]:
        if c in clubs:
            player_clubs.add(c)
    players[id]["clubs"] = list(player_clubs)
    if len(player_clubs) > 0:
        players2[id] = players[id]


with open("data/jsons/players_only_needed_clubs.json", "w", encoding="utf-8") as f:
    json.dump(players2, f, ensure_ascii=False, indent=2)