from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    PERCENTAGE = 0.03
    def __init__(self, name: str):
        super().__init__(name, oxygen_level=540)

    def miss(self, time_to_catch: int):
        if self.oxygen_level < time_to_catch:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= time_to_catch * self.PERCENTAGE
            return round(self.oxygen_level)

    def renew_oxy(self):
        self.oxygen_level = ScubaDiver.oxygen_level