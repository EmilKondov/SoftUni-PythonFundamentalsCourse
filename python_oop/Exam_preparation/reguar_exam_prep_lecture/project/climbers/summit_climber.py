from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, strength=150)


    def can_climb(self) -> bool:
        self.strength >= 75

    def climb(self, peak : BasePeak):
        if peak.difficulty_level == "Advanced":
            self.strength = (self.strength - 30) * 1.3
        self.strength = (self.strength - 30) * 2.5

        self.conquered_peaks.append(self.name)