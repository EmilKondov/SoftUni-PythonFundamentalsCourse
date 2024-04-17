from abc import ABC, abstractmethod

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

Animal("cat")
print

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
