# traffic_system.py
class TrafficSystem:
    def __init__(self):
        self.intersections = {}
        self.traffic_lights = {}
        self.vehicles = {}

    def add_intersection(self, intersection):
        self.intersections[intersection.id] = intersection

    def add_traffic_light(self, traffic_light):
        self.traffic_lights[traffic_light.id] = traffic_light

    def add_vehicle(self, vehicle):
        self.vehicles[vehicle.id] = vehicle