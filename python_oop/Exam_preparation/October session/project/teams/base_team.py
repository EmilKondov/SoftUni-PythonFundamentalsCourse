import math
from abc import ABC, abstractmethod
from typing import List

from equipment.base_equipment import BaseEquipment


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment: List[BaseEquipment] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        average_protection = math.floor(sum(p.protection for p in self.equipment) / len(self.equipment)
                                        ) if self.equipment else 0
        return (f"Name: {self.name}"
               f"Country: {self.country}"
               f"Advantage: {self.advantage} points"
               f"Budget: {self.budget}EUR"
               f"Wins: {self.wins}"
               f"Total Equipment Price: {sum(e.price for e in self.equipment)}"
               f"Average Protection: {average_protection}")





