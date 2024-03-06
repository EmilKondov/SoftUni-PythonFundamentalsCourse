class Food:
    def __init__(self, expiration_date: str):
        self.expiration_date = expiration_date

class Fruit(Food):
    def __init__(self, name, expiration_date):
        super().__init__(expiration_date)
        self.name = name