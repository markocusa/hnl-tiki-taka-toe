from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Player
from .serializer import PlayerSerializer

# Create your views here.

@api_view(['GET'])
def players(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def validate_move(request):
    rules = request.data.get("rules", [])

    qs = Player.objects.all()

    for rule in rules:
        field = rule.get("field")
        value = rule.get("value")

        if field == "country":
            qs = qs.filter(country__name__iexact=value)

        elif field == "club":
            qs = qs.filter(clubs__name__iexact=value)

        elif field == "confederation":
            qs = qs.filter(country__confederation__name__iexact=value)

        else:
            return Response({
                "valid": False,
                "error": f"Unknown field: {field}"
            })

    players = list(qs.values("id", "name"))

    if players:
        return Response({
            "valid": True,
            "matches": players,
            "count": len(players)
        })

    return Response({
        "valid": False,
        "reason": "No matching player"
    })
