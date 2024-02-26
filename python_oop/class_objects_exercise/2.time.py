class Time:
    max_hours = 23     # в реални условия бихмеги изписали с главни букви, тъй като са константи
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}" # чрез 02d казваме добави 0-ли отлява до 2 знака.

    def next_second(self) -> str:
        self.seconds += 1
        if self.seconds >= Time.max_seconds:
            self.seconds = 00
            self.minutes += 1
            if self.minutes >= Time.max_minutes:
                self.minutes = 00
                self.hours += 1
                if self.hours >= Time.max_hours:
                    self.hours = 00
        return self.get_time()

time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())