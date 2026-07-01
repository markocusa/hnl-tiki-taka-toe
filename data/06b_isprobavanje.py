import json
import requests
import time

BASE_URL = "https://transfermarkt-api.fly.dev"

player_id="24628"

response = requests.get(f"{BASE_URL}/players/{player_id}/transfers",timeout=10)
response.raise_for_status()
data = response.json()
print("Transferi:")
print(data)
response = requests.get(f"{BASE_URL}/players/{player_id}/profile",timeout=10)
response.raise_for_status()
data = response.json()
print("Profil:")
print(data)