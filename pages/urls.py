from django.urls import path
from .views import *

### <int:pk> for individual stuff
urlpatterns = [
   path('', DexList.as_view(), name='home'),
   path('pokemon/<int:pk>/', PokemonDetail.as_view(), name='pokemon_detail'),
]