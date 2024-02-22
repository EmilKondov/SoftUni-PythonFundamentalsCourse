class Cup:
    """
    Тук на тази индентация се намират атрибути на класа
    Class attributes
    """




    def __init__(self, size: int, quantity: int):
        """ Това са атрибути на инстанцията, които са
        вид data attributes. Това са всички атрибути,
        които са закачени на инстанцията. Тях ги достъпваме само
        чрез инстанция, която е вдигната от съответния клас
        Двата реда отдолу са атрибути на инстанцията.
        Instance attributes
        """
        self.size = size
        self.quantity = quantity

    def fill(self, quantity: int) -> None:
        if self.quantity + quantity <= self.size:
            self.quantity += quantity

    def status(self) -> int:
        return self.size - self.quantity

cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())