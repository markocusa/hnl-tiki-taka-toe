import json

with open("data/jsons/all_players_data.json", "r", encoding="utf-8") as f:
    players = json.load(f)

dupli = []

for tm_id in list(players.keys()):
    for tm_id2 in list(players.keys()):
        if (players[tm_id]["name"]==players[tm_id2]["name"] and tm_id!=tm_id2):
            dupli.append(players[tm_id]["name"])

with open("data/jsons/duplicates.json", "w", encoding="utf-8") as f:
    json.dump(sorted(dupli)[::2], f, ensure_ascii=False, indent=2)