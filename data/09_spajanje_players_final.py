import json

with open("data/jsons/players_data.json", "r", encoding="utf-8") as f:
    players1 = json.load(f)

with open("data/jsons/players_mistakes1_solved.json", "r", encoding="utf-8") as f:
    players2 = json.load(f)

for id,value in players2.items():
    players1[id]=value

#print(len(players1))

with open("data/jsons/players_final.json", "w", encoding="utf-8") as f:
    json.dump(players1, f, ensure_ascii=False, indent=2)