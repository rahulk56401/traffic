# test_traffic_system.py
import unittest
from models import TrafficLight, TrafficLightState, Intersection
from traffic_system import TrafficSystem

class TestTrafficSystem(unittest.TestCase):

    def setUp(self):
        self.traffic_system = TrafficSystem()
        self.intersection = Intersection("A", ["B", "C"])
        self.traffic_light = TrafficLight("TL1", TrafficLightState.RED, self.intersection)
        self.traffic_system.add_intersection(self.intersection)
        self.traffic_system.add_traffic_light(self.traffic_light)

    def test_traffic_light_initial_state(self):
        self.assertEqual(self.traffic_light.state, TrafficLightState.RED)

    def test_traffic_light_state_change(self):
        self.traffic_light.change_state(TrafficLightState.GREEN)
        self.assertEqual(self.traffic_light.state, TrafficLightState.GREEN)

    def test_add_intersection(self):
        self.assertIn("A", self.traffic_system.intersections)

    def test_add_traffic_light(self):
        self.assertIn("TL1", self.traffic_system.traffic_lights)

if __name__ == "__main__":
    unittest.main()