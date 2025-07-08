from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name = "get-csrf"), # Must be called by front end to get CSRF token
    path("create-game/", views.create_game, name = "create-game"), # Allows a player to open a new game. Expects a hostname in the request bopy
    path("get-open-games", views.get_open_games, name = "get-open-games"), # Returns a list of all the games that are in lobby state so that players can join
    path("start-game", views.start_game, name = "start-game"), # Allows the host to start a game and kick off role assignment. Expects the body to contain the number of mafia, as well as a list of selected special roles.
    path("reset-game", views.back_to_lobby, name = "reset-game"), # Allows the host to set the game back to lobby, all roles will be unassigned
    path("end-game", views.end_game, name = "end-game"), # Allows the host to terminate a game completely, at which point the players will be deleted
    path("get-optional-roles", views.get_optional_roles, name = "get-optional-roles"), # Returns a list of special roles that can be added to a game, this is to allow the host to set up the game before it starts
]