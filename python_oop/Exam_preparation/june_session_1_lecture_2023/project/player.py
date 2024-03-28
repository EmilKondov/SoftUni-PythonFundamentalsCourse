class Player:
    def __init__(self, name: str, age: int, stamina: int):
        self.name = name
        self.age = age
        self.stamina = stamina
        self.need_sustenance = bool

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"



