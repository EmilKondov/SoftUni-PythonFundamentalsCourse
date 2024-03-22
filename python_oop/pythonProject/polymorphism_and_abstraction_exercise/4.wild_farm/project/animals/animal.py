from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, weight: float, food_eaten: int = 0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten


class Bird(ABC, Animal):
    def __init__(self, wing_size: float):
        self.wing_size = wing_size

class Mammal(ABC, Animal):
    def __init__(self, living_region: str):
        self.living_region = living_region















