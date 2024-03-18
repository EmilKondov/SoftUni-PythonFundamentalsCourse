class Category:
    def __repr__(self, _id: int, name: str):
        self.id = _id
        self.name = name


    def edit(self, new_name: str):
        self.name = new_name

    def __repr__(self) -> str:
        return f"Category {self.id}: {self.name}"
