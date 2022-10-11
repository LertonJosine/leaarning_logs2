from multiprocessing import context
from django.shortcuts import render
from .models import Pizza, Topping

# Create your views here.

def home(request):
    return render(request, 'index.html')

def cardapio(request):
    pizzas = Pizza.objects.all()
    context = {
        'pizzas':pizzas
    }
    return render(request, 'cardapio.html', context)

def igredientes(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {
        'pizza': pizza,
        'toppings': toppings
    }
    return render(request, 'igredients.html', context)