from project.dough import Dough
from project.topping import Topping


class Pizza(Dough):
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int, toppings: dict):
        self.name = name
        self.dough = dough    #Dough ??? Not sure how to declare it here
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = toppings
# setter and getter for name
    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        if value == None:
            raise ValueError("The name cannot be an empty string")
        self.name = value

# setter and getter for dough
    @property
    def dough(self):
        return self.dough
    
    @dough.setter
    def dough(self, value):
        if value == None:
            raise ValueError("You should add dough to the pizza")
        self.dough = value


# setter and getter for max_number ....

    @property
    def max_number_of_toppings(self):
        return self.max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.max_number_of_toppings = value

# # setter and getter for toppings
#
#     @property
#     def toppings(self):
#         return self.toppings
#
#     @toppings.setter
#     def toppings(self, value):
#         if


# Methods of this class

    def add_topping(self, topping: Topping):
        self.toppings[topping] = topping
        if len(self.toppings) > self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")
        elif topping in self.toppings:
            topping.weight += self ### Не е довършено


    def calculate_total_weight(self):
        return (Dough.weight + Topping.weight)