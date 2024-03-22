from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):

    def make_sound(self) -> str:
        return "Hoot Hoot"

    @property
    def gained_weight(self) -> int:
        return 0.25

    @property
    def food_that_eats(self):
        return [Meat]


class Hen(Bird):

    def make_sound(self) -> str:
        return "Cluck"

    @property
    def gained_weight(self) -> int:
        return 0.35

    @property
    def food_that_eats(self):
        return [Vegetable, Meat, Fruit, Seed]

