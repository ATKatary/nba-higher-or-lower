"""
nba url patterns
"""
from django.urls import path
from . import views

urlpatterns = [
    path("players", views.fetch_players, name = "players")
]