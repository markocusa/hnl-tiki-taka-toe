from django.contrib import admin
from .models import Confederation, Country, Club, Player

# Register your models here.
admin.site.register(Confederation)
admin.site.register(Country)
admin.site.register(Club)
admin.site.register(Player)