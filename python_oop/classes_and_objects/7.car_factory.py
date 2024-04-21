class CarOrder:
    def __init__(self, brand: str, model: str, type_of_engine: str, chassis_config: str):
        self.brand = brand
        self.model = model
        self.type_of_engine = type_of_engine
        self.chassis_config = chassis_config

    def create_car(self):
        return f"The car is {self.brand} {self.model} with {self.type_of_engine} engine and it is a {self.chassis_config}"

list_of_cars_for_prodution = []
while len(list_of_cars_for_prodution) < 2:
    desired_brand = input(f"What type of car do you want: ")
    desired_model = input(f"What model: ")
    desired_engine = input(f"What engine: ")
    desired_chassis = input(f"What configuration of the chasis: ")

    car = CarOrder(desired_brand, desired_model, desired_engine, desired_chassis)
    list_of_cars_for_prodution.append(car)

for i in list_of_cars_for_prodution:
    print(i.create_car())




