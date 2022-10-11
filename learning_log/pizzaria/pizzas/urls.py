from unicodedata import name
from django.urls import path
from .views import cardapio, home, igredientes
urlpatterns = [
    path('', home, name='index'),
    path('cardapio/', cardapio, name='cardapio'),
    path(r'^cardapio(?P<pizza_id>\d+)$', igredientes, name='igredientes'),
]
