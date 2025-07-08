from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view
from rest_framework.response import Response
from uuid import uuid4
import json

from .models import Player, Game
from .populate_roles import *

fill_missing_roles()

@ensure_csrf_cookie
@api_view(["GET"])
def hello(request):
    """This method will return the CSRF token to the FE"""
    return Response({"status": "Hello from django"})

@api_view(["POST"])
def create_game(request):
    body_data = json.loads(request.body.decode('utf-8'))
    hostname = body_data.get("hostname", str(uuid4()))

    host = Player(name=hostname)
    host.save()
    request.session["player-id"] = host.id
    game = Game()
    game.host = host
    game.save()

    return Response({
        "status": "success",
        "game": game.id
    })

@api_view(["GET"])
def get_open_games(request):
    open_games = Game.objects.filter(state=Game.GameState.LOBBY)
    result = []
    for game in open_games:
        result.append([game.id, game.host.name])
    return Response({"games": result})

@api_view(["POST"])
def start_game(request):
    #TODO: This method should also take care of role assignment
    #TODO: Accept number of mafia and list of special roles
    status = "Unsuccessful"
    body_data = json.loads(request.body.decode("utf-8"))
    game_id = body_data.get("game", -1)

    game = Game.objects.filter(id=game_id).first()
    if game is not None:
        game.state = Game.GameState.STARTED
        game.save()
        status = "Successful"

    return Response({"status": status})

@api_view(["POST"])
def back_to_lobby(request):
    status = "Unsuccessful"
    body_data = json.loads(request.body.decode("utf-8"))
    game_id = body_data.get("game", -1)

    game = Game.objects.filter(id=game_id).first()
    if game is not None:
        game.state = Game.GameState.LOBBY
        game.save()
        status = "Successful"

    return Response({"status": status})

@api_view(["POST"])
def end_game(request):
    status = "Unsuccessful"
    body_data = json.loads(request.body.decode("utf-8"))
    game_id = body_data.get("game", -1)

    game = Game.objects.filter(id=game_id).first()
    if game is not None:
        game.state = Game.GameState.ENDED
        game.save()
        status = "Successful"

    return Response({"status": status})

@api_view(["GET"])
def get_optional_roles(request):
    optionals = Role.objects.filter(playable=True, optional=True)

    result = []
    for role in optionals:
        result.append([role.id, role.name, role.description])

    return Response({"roles": result})

#TODO: All the host actions should search for the game by the host who is performing them
#TODO: Link player identity using session store