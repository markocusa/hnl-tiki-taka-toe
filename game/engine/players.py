from game.models import Player

def get_all_players():
    return Player.objects.all().prefetch_related(
            "clubs",
            "coaches"
            ).select_related(
                "country",
                "country__confederation"
            )