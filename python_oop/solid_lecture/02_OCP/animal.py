from abc import ABC, abstractmethod
from typing import  List

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

    def get_species(self):
        return self.__class__.__name__


class Cat(Animal):

    def make_sound(self):
        return "meow"

class Dog(Animal):

    def make_sound(self):
        return "bark"

class Bird(Animal):

    def make_sound(self):
        return "piu piu"


def animal_sound(animals: List[Animal]):
    for animal in animals:
        print(animal.make_sound())

animals = [Cat(), Dog()]

animal_sound(animals)