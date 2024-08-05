from abc import ABC, abstractmethod
from typing import List


from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    #TODO which is the abstract
    def __init__(self, name: str, oxygen_level: float, catch: list, competition_points: float, has_health_issue: bool):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch: List[BaseFish] = []
        self.__competition_points = 0.0
        self.has_health_issue = False

        @property
        def competition_points(self) -> float:
            return round(competition_points, 1)


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



    @abstractmethod
    def miss(time_to_catch: int):
        pass


    def renew_oxy(self):
        pass

    def hit(self, fish: BaseFish):
        if self.oxygen_level < fish.time_to_catch:
            self.oxygen_level = 0
        else:
            self.catch.append(fish)
            self.__competition_points += fish.points
            self.oxygen_level -= fish.time_to_catch

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue


    def __str__(self):
        return f"{class.__name}: [Name: {name}, Oxygen level left: {oxygen_level}, Fish caught: {count of caught fish}, Points earned: {competition_points}]"

