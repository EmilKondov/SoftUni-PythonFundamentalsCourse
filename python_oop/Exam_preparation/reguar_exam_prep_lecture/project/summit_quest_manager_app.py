from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.base_peak import BasePeak


class SummitQuestManagerApp:
    VALID_TYPE_CLIMBERS = {
        "ArcticClimber": ArcticClimber,
        "SummitClimber": SummitClimber
    }

    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peak: List[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):
        try:
            climber = self.VALID_TYPE_CLIMBERS[climber_type](climber_name)
        except KeyError:
            return f"{climber_type} doesn't exist in our register."

        try:
            next(filter(lambda c: c.name == climber_name, self.climbers))
            return f"{climber_name} has been already registered."
        except StopIteration:
            self.climbers.append(climber)
            return f"{climber_name} is successfully registered as a {climber_type}."

        