from django.contrib import admin
from .models import Pokemon

# Register your models here.
class PokemonAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "type",
        "dexNum",
        "gen",
       
    )

admin.site.register(Pokemon, PokemonAdmin)