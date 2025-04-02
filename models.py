# models.py
from enum import Enum

class TrafficLightState(Enum):
    RED = "RED"
    GREEN = "GREEN"
    YELLOW = "YELLOW"

class Intersection:
    def __init__(self, id, connected_roads):
        self.id = id
        self.connected_roads = connected_roads

class TrafficLight:
    def __init__(self, id, state, intersection):
        self.id = id
        self.state = state
        self.intersection = intersection

    def change_state(self, new_state):
        self.state = new_state

class Vehicle:
    def __init__(self, id, type, speed, current_route):
        self.id = id
        self.type = type
        self.speed = speed
        self.current_route = current_route
        self.current_position = None

    def move_to_next_intersection(self):
        if self.current_route:
            self.current_position = self.current_route.pop(0)