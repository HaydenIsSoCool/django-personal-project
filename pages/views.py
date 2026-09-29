from django.views.generic import ListView, DetailView
from .models import Pokemon

# Create your views here.

class DexList(ListView):
    model = Pokemon
    template_name = 'home.html'

class PokemonDetail(DetailView):
    model = Pokemon
    template_name = 'pokemon_detail.html'




