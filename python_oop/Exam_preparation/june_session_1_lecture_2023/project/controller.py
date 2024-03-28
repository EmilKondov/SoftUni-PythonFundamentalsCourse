from typing import List, Tuple

from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *players: Tuple[Player]) -> str :
        players_added = []
        