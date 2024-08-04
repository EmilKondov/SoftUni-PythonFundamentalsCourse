from abc import ABC, abstractmethod
from typing import List


from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    #TODO which is the abstract
    def __init__(self, name: str, oxygen_level: float, catch: list, competition_points: float, has_health_issue: bool):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch: List[BaseFish] = []
        self.competition_points = 0
        self.has_health_issue = has_health_issue

        #setter and getter for name
        @property
        def name(self):
            return self.__name

        @name.setter
        def name(self, value):
            if value.strip() == "":
                raise ValueError("Diver name cannot be null or empty!")
            self.__name = value


        #setter and getter for the oxygen level
        @property
        def oxygen_level(self):
            return self.__oxygen_level

        @oxygen_level.setter
        def oxygen_level(self, value):
            if value < 0:
                raise ValueError("Cannot create diver with negative oxygen level!")
            self.__oxygen_level = value








    def miss(time_to_catch: int):
        pass

    def renew_oxy(self):
        pass

    def hit(fish: BaseFish):
        pass

    def update_health_status(self):
        pass


    def __str__(self):
        pass

