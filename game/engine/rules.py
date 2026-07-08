RULE_HANDLERS = {}

def register_rule(name):
    def wrapper(func):
        RULE_HANDLERS[name] = func
        return func
    return wrapper


def apply_rule(players, field, value):
    handler = RULE_HANDLERS.get(field)
    if not handler:
        return players
    return handler(players, value)


@register_rule("country")
def country_rule(players, value):
    return players.filter(
        country__name__iexact=value
    )


@register_rule("club")
def club_rule(players, value):
    return players.filter(
        clubs__name__iexact=value
    ).distinct()


@register_rule("confederation")
def conf_rule(players, value):
    return players.filter(
        country__confederation__name__iexact=value
    )


@register_rule("coach")
def coach_rule(players, value):
    return players.filter(
        coaches__name__iexact=value
    ).distinct()


@register_rule("hnl_nastupi")
def hnl_nastupi_rule(players, value):
    return players.filter(
        hnl_nastupi__gte=int(value)
    )


@register_rule("hnl_golovi")
def hnl_golovi_rule(players, value):
    return players.filter(
        hnl_golovi__gte=int(value)
    )