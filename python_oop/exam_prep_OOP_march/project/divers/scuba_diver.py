from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 540

    def __init__(self, name: str):
        super.__init__(name, self.INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        reduced_amount = round(time_to_catch * 0.3)

        if (self.oxygen_level - time_to_catch) < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= reduced_amount

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN_LEVEL



