from django.urls import path
from .views import players, create_game, play_move, get_game, possible_players

urlpatterns = [
    path('players/', players),
    path('create-game/', create_game),
    path('play-move/', play_move),
    path('game/<uuid:game_id>/', get_game),
    path('game/<uuid:game_id>/possible-players/', possible_players),
]