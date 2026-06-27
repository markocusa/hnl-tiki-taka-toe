from django.urls import path
from .views import players, validate_move, play_move

urlpatterns = [
    path('players/', players),
    path('validate-move/', validate_move),
    path('play-move/', play_move),
]