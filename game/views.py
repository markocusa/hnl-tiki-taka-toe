from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Player, Game, Cell, RowRule, ColRule, Country, Club, Confederation
from .serializer import PlayerSerializer
import random
from functools import partial
from .engine.players import get_all_players
from .engine.rules import apply_rule
from .engine.board import get_board
from .engine.logic import check_win, is_draw

RULE_TYPES = [
    "country",
    "club",
    "confederation"
]

def random_rule():
    field = random.choice(RULE_TYPES)
    if field == "country":
        value = random.choice(list(Country.objects.values_list("name", flat=True)))
    elif field == "club":
        value = random.choice(list(Club.objects.values_list("name", flat=True)))
    elif field == "confederation":
        value = random.choice(list(Confederation.objects.values_list("name", flat=True)))
    return field, value

def create_rules(game):
    RowRule.objects.filter(game=game).delete()
    ColRule.objects.filter(game=game).delete()

    row_rules = []
    col_rules = []
    
    used=set()
    used_fields=set()
    for i in range(3):
        field, value = random_rule()
        while ((field,value) in used):
            field, value = random_rule()
        used.add((field,value))
        if (field!="club"):
            used_fields.add(field)
        row_rules.append((field, value))

    for i in range(3):
        field, value = random_rule()
        while (field in used_fields or (field,value) in used):
            field, value = random_rule()
        used.add((field,value))
        col_rules.append((field, value))

    for i, (field, value) in enumerate(row_rules):
        RowRule.objects.create(game=game, index=i, field=field, value=value)

    for i, (field, value) in enumerate(col_rules):
        ColRule.objects.create(game=game, index=i, field=field, value=value)

def board_is_valid(game):
    players = get_all_players()
    row_rules = list(RowRule.objects.filter(game=game).order_by("index"))
    col_rules = list(ColRule.objects.filter(game=game).order_by("index"))
    for r in range(3):
        for c in range(3):
            filtered = apply_rule(players, row_rules[r].field, row_rules[r].value)
            filtered = apply_rule(filtered, col_rules[c].field, col_rules[c].value)
            if len(filtered) == 0:
                return False
    return True

# Create your views here.
@api_view(['GET'])
def players(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def play_move(request):
    game_id = request.data.get("game_id")
    row = int(request.data.get("row"))
    col = int(request.data.get("col"))
    player_name = request.data.get("player_name")

    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        return Response({"valid": False, "reason": "Game not found"})
    if game.is_finished:
        return Response({"valid": False, "reason": "Game is finished"})
    if row is None or col is None or player_name is None:
        return Response({"valid": False, "reason": "Missing data"})
    if row < 0 or row > 2 or col < 0 or col > 2:
        return Response({"valid": False, "reason": "Invalid board position"})

    player = Player.objects.filter(name=player_name).first()
    if not player:
        return Response({"valid": False, "reason": "Player not found"})
    
    try:
        cell = Cell.objects.get(game=game, row=row, col=col)
    except Cell.DoesNotExist:
        return Response({"valid": False, "reason": "Cell not found"})
    if cell.symbol is not None:
        return Response({"valid": False, "reason": "Cell already taken"})

    qs = Player.objects.filter(id=player.id)
    row_rule = RowRule.objects.get(game=game, index=row)
    col_rule = ColRule.objects.get(game=game, index=col)
    qs = apply_rule(qs, row_rule.field, row_rule.value)
    qs = apply_rule(qs, col_rule.field, col_rule.value)
    valid_move = True
    if not qs:
        valid_move = False
    if valid_move:
        cell.player_name = player.name
        cell.symbol = game.current_turn
        cell.save()

    game.current_turn = "O" if game.current_turn == "X" else "X"
    cells = Cell.objects.filter(game=game)
    board = get_board(cells)
    winner_data = check_win(board)
    if winner_data:
        game.is_finished = True
        game.winner = winner_data["winner"]
        winning_line=winner_data["line"]
    elif is_draw(board):
        game.is_finished = True
        game.winner = "draw"
        winning_line=None
    else:
        winning_line=None
    game.save()

    return Response({
        "valid": valid_move,
        "board": board,
        "current_turn": game.current_turn,
        "is_finished": game.is_finished,
        "winner": game.winner,
        "winning_line": winning_line
    })

@api_view(['POST'])
def create_game(request):
    game = Game.objects.create()
    while True:
        create_rules(game)
        if board_is_valid(game):
            break
        game.row_rules.all().delete()
        game.col_rules.all().delete()
    for r in range(3):
        for c in range(3):
            Cell.objects.create(game=game, row=r, col=c)

    return Response({"game_id": str(game.id)})


@api_view(['GET'])
def get_game(request, game_id):
    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        return Response({
            "error": "Game not found"
        }, status=404)

    cells = Cell.objects.filter(game=game)
    board = get_board(cells)
    return Response({
        "game_id": str(game.id),
        "board": board,
        "row_rules": [
            {"index": r.index, "field": r.field, "value": r.value}
            for r in game.row_rules.all()
        ],
        "col_rules": [
            {"index": c.index, "field": c.field, "value": c.value}
            for c in game.col_rules.all()
        ],
        "current_turn": game.current_turn,
        "is_finished": game.is_finished,
        "winner": game.winner
    })

@api_view(['GET'])
def possible_players(request, game_id):
    row = int(request.GET.get("row"))
    col = int(request.GET.get("col"))
    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        return Response({"error": "Game not found"}, status=404)
    try:
        row_rule = RowRule.objects.get(game=game, index=row)
        col_rule = ColRule.objects.get(game=game, index=col)
    except:
        return Response({"error": "Rules not found"}, status=404)
    players = Player.objects.all()
    players = apply_rule(
        players,
        row_rule.field,
        row_rule.value
     )
    players = apply_rule(
        players,
        col_rule.field,
        col_rule.value
    )
    return Response([
        {
            "name": player.name,
            "name_in_home_country": player.name_in_home_country
        }
        for player in players
    ])
