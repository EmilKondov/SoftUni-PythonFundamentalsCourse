from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation

class TestRailWayStation(TestCase):
    def test_intialised_correcty(self):
        s = RailwayStation("Sofia")
        self.assertEqual(s.name, "Sofia")
        self.assertEqual(s.arrival_trains, deque())
        self.assertEqual(s.departure_trains, deque())

    def test_less_name_chars_raises(self):
        


if __name__ == "__main__":
    main()