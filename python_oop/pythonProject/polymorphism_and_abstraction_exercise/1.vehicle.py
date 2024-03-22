from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        pass


class Car(Vehicle):
    CONDITIONER_ON: float = 0.9

    def drive(self, distance: float) -> None:
        consumption = (self.fuel_consumption + self.CONDITIONER_ON) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONDITIONER_ON: float = 1.6
    REFUELING_COEFICENT: float = 0.95

    def drive(self, distance: float) -> None:
        consumption = (self.fuel_consumption + self.CONDITIONER_ON) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel * self.REFUELING_COEFICENT


# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

# second zero test
# import unittest
#
# class VehiclesTests(unittest.TestCase):
#     def test_second_zero(self):
#         truck = Truck(100, 15)
#         truck.drive(5)
#         self.assertEqual(truck.fuel_quantity, 17.0)
#         truck.refuel(50)
#         self.assertEqual(truck.fuel_quantity, 64.5)
#
# if __name__ == '__main__':
#     unittest.main()