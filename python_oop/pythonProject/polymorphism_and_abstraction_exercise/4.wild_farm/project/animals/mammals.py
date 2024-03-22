from project.animals.animal import Mammal
from project.food import Fruit, Vegetable, Meat, Food, Seed


class Mouse(Mammal):

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit]

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food) -> str or None:
        return

    @property
    def gained_weight(self) -> int:
        return 0.10


class Dog(Mammal):

    @property
    def food_that_eats(self):
        return [Meat]

    def make_sound(self):
        return "Woof!"

    @property
    def gained_weight(self) -> int:
        return 0.40


class Cat(Mammal):

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit]

    def make_sound(self):
        return "Meow"

    @property
    def gained_weight(self) -> int:
        return 0.30


class Tiger(Mammal):

    @property
    def food_that_eats(self):
        return [Meat]

    def make_sound(self):
        return "ROAR!!!"

    @property
    def gained_weight(self) -> int:
        return 1.0