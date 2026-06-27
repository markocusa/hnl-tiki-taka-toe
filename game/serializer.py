from rest_framework import serializers
from .models import Player, Country, Club, Confederation


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'