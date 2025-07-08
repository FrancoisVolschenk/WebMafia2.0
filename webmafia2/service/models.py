from django.db import models
from django.utils import timezone

class Role(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    playable = models.BooleanField(default=True)
    optional = models.BooleanField(default=True)

class Player(models.Model):
    name = models.CharField(max_length=50, unique=False)

class Game(models.Model):
    class GameState(models.TextChoices):
        LOBBY = 'lobby', 'Lobby'
        STARTED = 'started', 'Started'
        ENDED = 'ended', 'Ended'
    state = models.CharField(max_length=10,choices=GameState.choices, default=GameState.LOBBY)
    host = models.ForeignKey(Player, on_delete=models.CASCADE)

class PlayerRole(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

