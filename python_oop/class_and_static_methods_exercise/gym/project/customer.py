from project.next_id_mixin import NextIdMixin



class Customer(NextIdMixin):
    id = 1

    def __init__(self, name: str, address:str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()   # тук казваме дай ми следващото ID... такъв метод тук няма, но отива да търси в наследения.
        self.increment_id()

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"