from game.models import Player

def get_all_players():
    return list(
        Player.objects.all()
        .select_related("country", "country__confederation")
        .prefetch_related("clubs")
    )