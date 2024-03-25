from typing import List

from equipment.base_equipment import BaseEquipment
from equipment.elbow_pad import ElbowPad
from equipment.knee_pad import KneePad
from teams.base_team import BaseTeam
from teams.indoor_team import IndoorTeam
from teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPE = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TYPES_OF_TEAM = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
       if not value.isalnum():
           raise ValueError("Tournament name should contain letters and digits only!")
       self.__name = value


    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT_TYPE:
            raise Exception("Invalid equipment type!")
        equipment = self.VALID_EQUIPMENT_TYPE[equipment_type]()
        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."


    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TYPES_OF_TEAM:
            raise Exception("Invalid team type!")
        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."
        team = self.VALID_TYPES_OF_TEAM[team_type](team_name, country, advantage)
        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        # """"
        # Тук използайки името тип на оборудване и името на отбор, който ни дават,
        # използвайки генератор ние всъщност трябва да октирем съответния обект(инстанция)
        # на обтор носещ това име, както и оборудване.
        # Намирайки тези обекти ние ще достъпим съответно бюджета на отбора и цената на
        # това оборудване, за да ги сравним
        # """
        team = next((t for t in self.teams if t.name == team_name), None)
        equipment = next((e for e in reversed(self.equipment) if e.__class__.__name__ == equipment_type), None)

        # """
        # Тъй като BaseEquipment class-a няма име ние взимаме името на класа и чрез reversed сме сигурни,
        # че ще вземем последната екипировка(инстанция) от този клас.
        # """
        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = next((t for t in self.teams if t.name == team_name), None)
        # """ Този генератор проверя дали този отбор е в лист и отдолу не е нужно
        # да го проверяваме втори път, ако не е ще имаме None.
        # """
        if team is None:
            raise Exception("No such team!")
        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        number_of_changed_equipment = 0
        for e in self.equipment:
            if e.__class__.__name__ == equipment_type:
                e.increase_price()
                number_of_changed_equipment += 1
        return f"Successfully changed {number_of_changed_equipment}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next((t for t in self.teams if t.name == team_name1), None)
        team2 = next((t for t in self.teams if t.name == team_name2), None)

        if not team1.name != team2.name:
            raise Exception("Game cannot start! Team types mismatch!")
        team1_points = self.get_team_points(team1)
        team2_points = self.get_team_points(team2)
        # """
        # Тук следва да съберем advantage с total protection: което е
        # сбора от protection на всяка една екипировка, която имат
        # в този отбор. За целта създаваме допълнителен метод(static method),
        # в който правим sum() на списъка от всички стойности,
        # които събираме чрез for loop comprehension през team.equipment
        # """
        winner = team1 if team1_points > team2_points else team2 if team2_points > team1_points else None
        if winner is None:
            return "No winner in this game."
        winner.win()
        return f"The winner is {winner.name}."

    def get_statistics(self):
        teams = sorted(self.teams, key= lambda t: t.wins, reverse=True)
        result = [f"Tournament: {self.name}",
                  f"Number of Teams: {len(self.teams)}",
                  f"Teams:"]
        [result.append(t.get_statistics()) for t in teams]
        return "\n".join(result)


    @staticmethod
    def get_team_points(team: BaseTeam):
        return team.advantage + sum(e.protection for e in team.equipment)



