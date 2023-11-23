from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('hill_climb/', views.hill_climb_view, name='hill_climb'),
    path('genetic_algorithm/', views.genetic_algorithm_view, name='genetic_algorithm'),
]