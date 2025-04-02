# cli.py
def main():
    traffic_system = TrafficSystem()
    control_service = TrafficControlService()
    # Add intersections, traffic lights, and vehicles here
    # Example:
    intersection_a = Intersection("A", ["B", "C"])
    traffic_system.add_intersection(intersection_a)
    # Add more entities as needed

    simulation_engine = SimulationEngine(traffic_system, control_service)
    simulation_engine.run(duration=10)

if __name__ == "__main__":
    main()