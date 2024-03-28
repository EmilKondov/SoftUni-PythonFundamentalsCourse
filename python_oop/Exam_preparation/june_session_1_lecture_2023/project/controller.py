from typing import List

from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self, players: list, supplies: list):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, player1: Player, player2: Player, … playerN: Player)
