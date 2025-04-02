# traffic_control.py
class TrafficControlService:
    def manage_traffic_lights(self, traffic_system):
        for light in traffic_system.traffic_lights.values():
            if light.state == TrafficLightState.RED:
                light.change_state(TrafficLightState.GREEN)
            elif light.state == TrafficLightState.GREEN:
                light.change_state(TrafficLightState.YELLOW)
            elif light.state == TrafficLightState.YELLOW:
                light.change_state(TrafficLightState.RED)

    def move_vehicles(self, traffic_system):
        for vehicle in traffic_system.vehicles.values():
            vehicle.move_to_next_intersection()