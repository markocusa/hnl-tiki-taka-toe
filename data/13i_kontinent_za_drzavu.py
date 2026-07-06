import json

with open("data/jsons/all_countries.json", "r", encoding="utf-8") as f:
    countries = json.load(f)
with open("data/jsons/countries_with_confederations.json", "r", encoding="utf-8") as f:
    countries_with_conf = json.load(f)

for c in countries:
    if c not in countries_with_conf.keys():
        print(c)