class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight


# setter and getter for flour_type
    @property
    def flour_types(self):
        return self.flour_type

    @flour_types.setter
    def flour_types(self, value):
        if value == None:
            raise ValueError("The flour type cannot be an empty string")
        self.flour_type = value

# setter and getter for baking_technique

    @property
    def baking_technique(self):
        return self.baking_technique

    @baking_technique.setter
    def baking_technique(self, value):
        if value == None:
            raise ValueError("The baking technique cannot be an empty string")
        self.baking_technique = value

#setter and getter for weigh

    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.weight = value


