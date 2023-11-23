from django.shortcuts import render
from optimization_methods import geneticOptimization
from models import Player
# Create your views here.
def optimize(request):
    players = Player.objects.all()
    optimized_squad = geneticOptimization(players)
    context = {'Optimized Squad': optimized_squad}
    return render(request, 'optimization_methods/optimize.html', context)