from game.models import Player

def get_all_players():
    return list(
        Player.objects.all().prefetch_related(
            "clubs",
            "countries",
            "countries__confederation"
        )
    )