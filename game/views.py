from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Player
from .serializer import PlayerSerializer

BOARD = [
    [
        {"rules": [{"field": "country", "value": "Brazil"}], "player": None},
        {"rules": [{"field": "club", "value": "Barcelona"}], "player": None},
        {"rules": [{"field": "country", "value": "Argentina"}], "player": None},
    ],
    [
        {"rules": [{"field": "club", "value": "PSG"}], "player": None},
        {"rules": [{"field": "country", "value": "Croatia"}], "player": None},
        {"rules": [{"field": "club", "value": "Real Madrid"}], "player": None},
    ],
    [
        {"rules": [{"field": "country", "value": "France"}], "player": None},
        {"rules": [{"field": "club", "value": "Juventus"}], "player": None},
        {"rules": [{"field": "country", "value": "Germany"}], "player": None},
    ]
]
def apply_rule(qs, field, value):
    if field == "country":
        return qs.filter(country__name__iexact=value)
    if field == "club":
        return qs.filter(clubs__name__iexact=value)
    if field == "confederation":
        return qs.filter(country__confederation__name__iexact=value)
    return qs

# Create your views here.
@api_view(['GET'])
def players(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def validate_move(request):
    player_name = request.data.get("player_name")
    rules = request.data.get("rules", [])
    player = Player.objects.filter(name__iexact=player_name).first()

    if not player:
        return Response({
            "valid": False,
            "reason": "Player not found"
        })

    qs = Player.objects.filter(id=player.id)
    for rule in rules:
        qs = apply_rule(qs, rule["field"], rule["value"])

    if qs.exists():
        return Response({
            "valid": True,
            "player": player.name
        })

    return Response({
        "valid": False,
        "reason": "Player does not match rules"
    })


@api_view(['POST'])
def play_move(request):
    row = request.data.get("row")
    col = request.data.get("col")
    player_name = request.data.get("player_name")

    cell = BOARD[row][col]
    if cell["player"] is not None:
        return Response({
            "valid": False,
            "reason": "Cell already taken"
        })

    player = Player.objects.filter(name__iexact=player_name).first()
    if not player:
        return Response({
            "valid": False,
            "reason": "Player not found"
        })

    qs = Player.objects.filter(id=player.id)
    for rule in cell["rules"]:
        qs = apply_rule(qs, rule["field"], rule["value"])
    if not qs.exists():
        return Response({
            "valid": False,
            "reason": "Player does not match cell rules"
        })

    cell["player"] = player.name
    return Response({
        "valid": True,
        "board": BOARD
    })
