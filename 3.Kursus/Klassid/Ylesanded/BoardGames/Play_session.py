from Player import Player
from Game import Game

class PlaySession:
    def __init__(self, game: Game):
        self.__results : dict[Player, GameResult] = {}
        self.__game : Game = game