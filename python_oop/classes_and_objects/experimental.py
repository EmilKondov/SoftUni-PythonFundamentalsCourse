class MyCar():
    def __init__(self, brand: str, model: str, engine: str, power: int):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.power = power

    def the_car(self):
        return f"My car is {self.brand}, model {self.model}, with engine:{self.engine} and power output of {self.power} hp"


car1 = MyCar("bmw", "e36", "m50b20", 210)
car2 = MyCar("Audi", "A80", "1.9tdi", 90)

print(car1.the_car())
print(car2.the_car())
print(car2.engine)
print(f"The engine of my first car is {car1.engine}")
