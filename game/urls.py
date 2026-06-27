from django.urls import path
from .views import players, validate_move

urlpatterns = [
    path('players/', players),
    path('validate-move/', validate_move),
]