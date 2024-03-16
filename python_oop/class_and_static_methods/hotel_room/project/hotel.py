from typing import List
from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)


    def take_room(self, room_number: int, people: int) -> None:
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except IndexError:
            return

        result = room.take_room(people)

        if not result:
            self.guests += people

        """
        Тъй като метода take_room от class Room връща None, в случай че стаята е свободна
        и хората са настанени, то ние шравим тази проверка If not result, за да добавим хората
        в самия хотел. Те вече са добавени в стаята, а сега ги добавяме и в самия хотел.  
        """


    def free_room(self, room_number) -> None:
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except IndexError:
            return

        people = room.guests # -> тук ще знаем колко хора е имало в стаята преди да ги изгоним
        result = room.free_room()

        if not result:    # -> ако тук сме получили None то това означава, че стаята Е заета вмомента и ще трябва да изгоним гостите, зад а я освободим.
            self.guests -= people # така ако успешно изгоним хората, знаем колко са били, за да ги премахнем и от хотела, а не само от стаята.

    def status(self) -> str:
        return f"Hotel {self.name} has {self.guests} total guests\n"\
               f"Free rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}\n"\
               f"Taken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}"