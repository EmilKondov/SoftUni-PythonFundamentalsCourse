from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_TYPE_CLIMBERS = {
        "ArcticClimber": ArcticClimber,
        "SummitClimber": SummitClimber
    }

    VALID_PEAK_TYPES = {
        "ArcticPeak": ArcticPeak,
        "SummitPeak": SummitPeak
    }

    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

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


    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        try:
            peak = self.VALID_PEAK_TYPES[peak_type](peak_name, peak_elevation)
        except KeyError:
            return f"{peak_type} is an unknown type of peak."

        self.peaks.append(peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."


    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        cimber = next(filter(lambda c: c.name == climber_name, self.climbers))
        peak = next(filter(lambda p: p.name == peak_name, self.peaks))

        if peak.get_recommended_gear() == gear:
            return f"{climber_name} is prepared to climb {peak_name}."
        else:
            cimber.is_prepared = False
            return f"{climber_name} is not prepared to climb {peak_name}. " \
                   f"Missing gear:" \
                   f" {', '.join(g for g in sorted(peak.get_recommended_gear()) if g not in gear)}"
        