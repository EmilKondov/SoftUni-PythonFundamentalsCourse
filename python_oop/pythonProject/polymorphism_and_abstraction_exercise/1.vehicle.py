from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption + 0.9

    # def aircon_fuel(self) -> float:
    #     return self.fuel_consumption + 0.9

    def drive(self, value):
        self.fuel_quantity -= self.fuel_consumption * value

    def refuel(self, value):
        self.fuel_quantity += value



class Truck(Vehicle):
    REFUELING_COEFICENT = 0.95

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption + 1.6

    # def aircon_fuel(self) -> float:
    #     return self.fuel_consumption + 1.6

    def drive(self, value):
        self.fuel_quantity -= self.fuel_consumption * value

    def refuel(self, value):
        self.fuel_quantity += value * Truck.REFUELING_COEFICENT


# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)


# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)

# second zero test
import unittest

class VehiclesTests(unittest.TestCase):
    def test_second_zero(self):
        truck = Truck(100, 15)
        truck.drive(5)
        self.assertEqual(truck.fuel_quantity, 17.0)
        truck.refuel(50)
        self.assertEqual(truck.fuel_quantity, 64.5)

if __name__ == '__main__':
    unittest.main()