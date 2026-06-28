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
    return [p for p in players if p.country.name.lower() == value.lower()]


@register_rule("club")
def club_rule(players, value):
    return [
        p for p in players
        if any(c.name.lower() == value.lower() for c in p.clubs.all())
    ]


@register_rule("confederation")
def conf_rule(players, value):
    return [
        p for p in players
        if p.country.confederation.name.lower() == value.lower()
    ]