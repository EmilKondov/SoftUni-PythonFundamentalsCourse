class Equipment:
    id = 1

    def __init__(self, name: str):
        self.name = name

    def get_next_id(self):
        Equipment.id += 1
        self.id = Equipment.id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"