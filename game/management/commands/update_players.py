import json
from django.core.management.base import BaseCommand
from game.models import Player
from unidecode import unidecode
import cyrtranslit
import re


class Command(BaseCommand):
    help = "Update player search names"

    def handle(self, *args, **kwargs):

        for player in Player.objects.all():

            latin_name = player.name_in_home_country
            if (player.country and player.country.name== "Serbia"):
                latin_name=cyrtranslit.to_latin(latin_name, "sr")
            elif (player.country and player.country.name== "Montenegro"):
                latin_name=cyrtranslit.to_latin(latin_name, "me")
            elif (player.country and player.country.name== "North Macedonia"):
                latin_name=cyrtranslit.to_latin(latin_name, "mk")
            if re.search(r"[čćšžđČĆŠŽĐ]", latin_name):
                player.search_name = latin_name
            else:
                player.search_name = player.name

            player.save(update_fields=["search_name"])

        self.stdout.write(
            self.style.SUCCESS("Updated search names.")
        )