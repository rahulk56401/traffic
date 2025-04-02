# simulator.py
import time

class SimulationEngine:
    def __init__(self, traffic_system, control_service):
        self.traffic_system = traffic_system
        self.control_service = control_service

    def run(self, duration):
        for _ in range(duration):
            self.control_service.manage_traffic_lights(self.traffic_system)
            self.control_service.move_vehicles(self.traffic_system)
            self.print_status()
            time.sleep(1)

    def print_status(self):
        for vehicle in self.traffic_system.vehicles.values():
            position = vehicle.current_position.id if vehicle.current_position else "unknown"
            print(f"Vehicle {vehicle.id} at {position}")