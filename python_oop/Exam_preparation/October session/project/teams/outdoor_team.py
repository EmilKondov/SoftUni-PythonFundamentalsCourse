from teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=1000.0) # Тъй като не искаме някой да може да
        #зададе друг бюджет, ние в super() записваме budget = 1000.0

    def win(self):
        self.advantage += 115
        self.wins += 1