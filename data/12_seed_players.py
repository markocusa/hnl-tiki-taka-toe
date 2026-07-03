import json
from django.core.management.base import BaseCommand
from game.models import Player, Club, Country


class Command(BaseCommand):
    help = "Seed players from JSON"

    def handle(self, *args, **kwargs):

        with open("data/jsons/players_only_needed_clubs.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        for player_id, value in data.items():
            name = value.get("name")
            clubs = value.get("clubs", [])
            countries = value.get("citizenship", [])

            if not name:
                continue

            player, created_flag = Player.objects.get_or_create(name=name)

            for club_name in clubs:
                club = Club.objects.filter(name__iexact=club_name).first()
                if club:
                    player.clubs.add(club)

            for country_name in countries:
                country = Country.objects.filter(name__iexact=country_name).first()
                if country:
                    player.countries.add(country)

            if created_flag:
                created += 1

        self.stdout.write(self.style.SUCCESS(f"Done. Created {created} players"))