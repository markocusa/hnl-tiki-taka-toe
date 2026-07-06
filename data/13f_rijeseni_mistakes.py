import requests
import json
import os
import sys

with open("data/jsons/all_players_data.json", "r", encoding="utf-8") as f:
    players = json.load(f)

players["511386"]={
    "tm_id": "511386",
    "name": "Andrej Lazarov",
    "citizenship": ["North Macedonia"],
    "nameInHomeCountry": "Andrej Lazarov",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "andrej-lazarov",
    "klubovi": [
      "11083",
      "24575"
    ],
    "treneri": [
      None,
      "6653",
      "65937",
      "4338",
      "103880",
      "21567"
    ],
    "hnl_nastupi": 27,
    "kup_nastupi": 0,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 1,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 0,
    "kup_naslovi": 0,
    "superkup_naslovi": 0
  }
players["27912"]={
    "tm_id": "27912",
    "name": "Nikola Pokrivac",
    "citizenship": ["Croatia"],
    "nameInHomeCountry": "Nikola Pokrivač",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "nikola-pokrivac",
    "klubovi": [
      "144",
      "419",
      "599",
      "918",
      "2362"
    ],
    "treneri": [
      "4756",
      "4303",
      "20637",
      "2711",
      "1519",
      "19966",
      "1562",
      "7971"
    ],
    "hnl_nastupi": 99,
    "kup_nastupi": 5,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 15,
    "hnl_golovi": 10,
    "finale_kupa_nastupi": 1,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 4,
    "kup_naslovi": 4,
    "superkup_naslovi": 0
  }
players["47623"]={
    "tm_id": "47623",
    "name": "Alen Pamic",
    "citizenship": ["Croatia"],
    "nameInHomeCountry": "Alen Pamić",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "alen-pamic",
    "klubovi": [
      "999",
      "144"
    ],
    "treneri": [
      "7199",
      "3423",
      "7933",
      "1836",
      "7856",
      "1911"
    ],
    "hnl_nastupi": 77,
    "kup_nastupi": 0,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 6,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 0,
    "kup_naslovi": 0,
    "superkup_naslovi": 0
  }
players["217097"]={
    "tm_id": "217097",
    "name": "Jakov Jelic",
    "citizenship": ["Croatia"],
    "nameInHomeCountry": "Jakov Jelić",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "jakov-jelic",
    "klubovi": [],
    "treneri": [],
    "hnl_nastupi": 0,
    "kup_nastupi": 0,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 0,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 0,
    "kup_naslovi": 0,
    "superkup_naslovi": 0
  }
players["287798"]={
    "tm_id": "287798",
    "name": "Mile Zelenika",
    "citizenship": ["Croatia"],
    "nameInHomeCountry": "Mile Zelenika",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "mile-zelenika",
    "klubovi": [],
    "treneri": [],
    "hnl_nastupi": 0,
    "kup_nastupi": 0,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 0,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 0,
    "kup_naslovi": 0,
    "superkup_naslovi": 0
  }
players["27856"]={
    "tm_id": "27856",
    "name": "Drazen Govic",
    "citizenship": ["Croatia"],
    "nameInHomeCountry": "Dražen Gović",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "drazen-govic",
    "klubovi": [
      "223"
    ],
    "treneri": [
      "4470",
      "11127",
      "8186",
      "4455",
      "4182"
    ],
    "hnl_nastupi": 63,
    "kup_nastupi": 0,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 12,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 0,
    "kup_naslovi": 0,
    "superkup_naslovi": 0
  }
players["128182"]={
    "tm_id": "128182",
    "name": "Senid Kulacic",
    "citizenship": ["Bosnia-Herzegovina"],
    "nameInHomeCountry": "Senid Kulačić",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "senid-kulacic",
    "klubovi": [
      "223"
    ],
    "treneri": [
      "2892"
    ],
    "hnl_nastupi": 1,
    "kup_nastupi": 0,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 0,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 0,
    "kup_naslovi": 0,
    "superkup_naslovi": 0
  }
players["282029"]={
    "tm_id": "282029",
    "name": "Jordan Diakiese",
    "citizenship": ["France","DR Congo"],
    "nameInHomeCountry": "Jordan Dueni Diakiese",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "jordan-diakiese",
    "klubovi": [],
    "treneri": [],
    "hnl_nastupi": 0,
    "kup_nastupi": 0,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 0,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 0,
    "kup_naslovi": 0,
    "superkup_naslovi": 0
  }
players["27925"]={
    "tm_id": "27925",
    "name": "Zeljko Rumbak",
    "citizenship": ["Croatia"],
    "nameInHomeCountry": "Željko Rumbak",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "zeljko-rumbak",
    "klubovi": [],
    "treneri": [],
    "hnl_nastupi": 0,
    "kup_nastupi": 0,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 0,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 0,
    "kup_naslovi": 0,
    "superkup_naslovi": 0
  }
players["99536"]={
    "tm_id": "99536",
    "name": "Ivo Tomas",
    "citizenship": ["Croatia", "Germany"],
    "nameInHomeCountry": "Ivo Valentino Tomaš",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "ivo-tomas",
    "klubovi": [
      "447"
    ],
    "treneri": [
      "18018"
    ],
    "hnl_nastupi": 7,
    "kup_nastupi": 0,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 0,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 0,
    "kup_naslovi": 1,
    "superkup_naslovi": 0
  }
players["27927"]={
    "tm_id": "27927",
    "name": "Edin Saranovic",
    "citizenship": ["Bosnia-Herzegovina", "Croatia"],
    "nameInHomeCountry": "Edin Šaranović",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "edin-saranovic",
    "klubovi": [
      "6087",
      "2566",
      "2362"
    ],
    "treneri": [
      "2712",
      "4196",
      "7797",
      "1915",
      "4758",
      "22060"
    ],
    "hnl_nastupi": 52,
    "kup_nastupi": 0,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 12,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 0,
    "kup_naslovi": 0,
    "superkup_naslovi": 0
  }
players["24628"]={
    "tm_id": "24628",
    "name": "Ivan Turina",
    "citizenship": ["Croatia"],
    "nameInHomeCountry": "Ivan Turina",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "ivan-turina",
    "klubovi": [
      "419"
    ],
    "treneri": [
      None,
      "1079",
      "2907",
      "4756"
    ],
    "hnl_nastupi": 8,
    "kup_nastupi": 0,
    "superkup_nastupi": 2,
    "A_repka_nastupi": 1,
    "hnl_golovi": 0,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 3,
    "kup_naslovi": 3,
    "superkup_naslovi": 2
  }
players["40728"]={
    "tm_id": "40728",
    "name": "Marko Pavosevic",
    "citizenship": ["Croatia"],
    "nameInHomeCountry": "Marko Pavošević",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "marko-pavosevic",
    "klubovi": [],
    "treneri": [],
    "hnl_nastupi": 0,
    "kup_nastupi": 0,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 0,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 0,
    "kup_naslovi": 0,
    "superkup_naslovi": 0
  }
players["47611"]={
    "tm_id": "47611",
    "name": "Ivan Celikovic",
    "citizenship": ["Croatia"],
    "nameInHomeCountry": "Ivan Čeliković",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "ivan-celikovic",
    "klubovi": [
      "918",
      "11194"
    ],
    "treneri": [
      "2912",
      "20830",
      "7971",
      "88584",
      "63729",
      "19966"
    ],
    "hnl_nastupi": 143,
    "kup_nastupi": 18,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 1,
    "finale_kupa_nastupi": 1,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 0,
    "kup_naslovi": 0,
    "superkup_naslovi": 0
  }
players["315876"]={
    "tm_id": "315876",
    "name": "Bruno Boban",
    "citizenship": ["Croatia"],
    "nameInHomeCountry": "Bruno Boban",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "bruno-boban",
    "klubovi": [
      "5107"
    ],
    "treneri": [
      "20637",
      "26582"
    ],
    "hnl_nastupi": 18,
    "kup_nastupi": 4,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 0,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 0,
    "kup_naslovi": 0,
    "superkup_naslovi": 0
  }
players["1007"]={
    "tm_id": "1007",
    "name": "Mladen Bartolovic",
    "citizenship": ["Bosnia-Herzegovina", "Croatia"],
    "nameInHomeCountry": "Mladen Bartolović",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "mladen-bartolovic",
    "klubovi": [
      "314",
      "447"
    ],
    "treneri": [
      "2903",
      "3423",
      "5051",
      "20637",
      "2912",
      "5915",
      "2914",
      "4182",
      "25136",
      "5410",
      "1912"
    ],
    "hnl_nastupi": 148,
    "kup_nastupi": 2,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 35,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 0,
    "kup_naslovi": 1,
    "superkup_naslovi": 0
  }
players["28611"]={
    "tm_id": "28611",
    "name": "Josip Lukacevic",
    "citizenship": ["Bosnia-Herzegovina", "Croatia"],
    "nameInHomeCountry": "Josip Lukačević",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "josip-lukacevic",
    "klubovi": [
      "327",
      "314"
    ],
    "treneri": [
      "1391",
      "19215",
      "2892",
      "1912"
    ],
    "hnl_nastupi": 78,
    "kup_nastupi": 0,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 6,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 0,
    "kup_naslovi": 0,
    "superkup_naslovi": 0
  }
players["226168"]={
    "tm_id": "226168",
    "name": "Josko Hajder",
    "citizenship": ["Croatia"],
    "nameInHomeCountry": "Joško Hajder",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "josko-hajder",
    "klubovi": [
      "447",
      "999"
    ],
    "treneri": [
      "1836",
      "18018"
    ],
    "hnl_nastupi": 7,
    "kup_nastupi": 0,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 0,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 0,
    "kup_naslovi": 0,
    "superkup_naslovi": 0
  }
players["126415"]={
    "tm_id": "126415",
    "name": "Karolis Chvedukas",
    "citizenship": ["Lithuania"],
    "nameInHomeCountry": "Karolis Chvedukas",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "karolis-chvedukas",
    "klubovi": [
      "420"
    ],
    "treneri": [
      "8186"
    ],
    "hnl_nastupi": 13,
    "kup_nastupi": 1,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 0,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 0,
    "kup_naslovi": 0,
    "superkup_naslovi": 0
  }
players["11"]={
    "tm_id": "11",
    "name": "Georg Koch",
    "citizenship": ["Germany"],
    "nameInHomeCountry": "Georg Koch",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "georg-koch",
    "klubovi": [
      "419"
    ],
    "treneri": [
      "5440",
      "1562"
    ],
    "hnl_nastupi": 25,
    "kup_nastupi": 0,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 0,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 1,
    "kup_naslovi": 1,
    "superkup_naslovi": 0
  }
players["44245"]={
    "tm_id": "44245",
    "name": "Mihael Remenar",
    "citizenship": ["Croatia"],
    "nameInHomeCountry": "Mihael Remenar",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "mihael-remenar",
    "klubovi": [],
    "treneri": [],
    "hnl_nastupi": 0,
    "kup_nastupi": 0,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 0,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 0,
    "kup_naslovi": 0,
    "superkup_naslovi": 0
  }
players["27842"]={
    "tm_id": "27842",
    "name": "Hrvoje Custic",
    "citizenship": ["Croatia"],
    "nameInHomeCountry": "Hrvoje Ćustic",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "hrvoje-custic",
    "klubovi": [
      "2566",
      "5107"
    ],
    "treneri": [
      "4196",
      "1910"
    ],
    "hnl_nastupi": 23,
    "kup_nastupi": 0,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 1,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 0,
    "kup_naslovi": 0,
    "superkup_naslovi": 0
  }
players["47346"]={
    "tm_id": "47346",
    "name": "Domagoj Krajacic",
    "citizenship": ["Croatia"],
    "nameInHomeCountry": "Domagoj Krajačić",
    "isRetired": True,
    "marketValue": 0,
    "player_slug": "domagoj-krajacic",
    "klubovi": [
      "6087",
      "2566"
    ],
    "treneri": [
      "11616",
      "3364"
    ],
    "hnl_nastupi": 11,
    "kup_nastupi": 2,
    "superkup_nastupi": 0,
    "A_repka_nastupi": 0,
    "hnl_golovi": 0,
    "finale_kupa_nastupi": 0,
    "finale_kupa_golovi": 0,
    "superkup_golovi": 0,
    "najbolji_strijelac": 0,
    "hnl_naslovi": 0,
    "kup_naslovi": 0,
    "superkup_naslovi": 0
  }        

with open("data/jsons/all_players_data.json", "w", encoding="utf-8") as f:
    json.dump(players, f, ensure_ascii=False, indent=2)