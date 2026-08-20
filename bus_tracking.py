import math
import time


class Bus:
    def __init__(self, bus_id, route, speed):
        self.bus_id = bus_id
        self.route = route
        self.speed = speed
        self.position = route[0]
        self.status = "RUNNING"

    def calculate_position(self, progress):
        """
        Calculate the bus position along a polyline route.

        progress must be between 0 and 1.
        """
        if not 0 <= progress <= 1:
            raise ValueError("Progress must be between 0 and 1")

        if len(self.route) < 2:
            return self.route[0]

        # Calculate length of each route segment
        segments = []
        total_distance = 0

        for point_a, point_b in zip(self.route, self.route[1:]):
            distance = math.dist(point_a, point_b)
            segments.append(distance)
            total_distance += distance

        target_distance = progress * total_distance

        for i, segment_distance in enumerate(segments):

            if target_distance <= segment_distance:
                point_a = self.route[i]
                point_b = self.route[i + 1]

                if segment_distance == 0:
                    return point_a

                fraction = target_distance / segment_distance

                x = point_a[0] + fraction * (
                    point_b[0] - point_a[0]
                )

                y = point_a[1] + fraction * (
                    point_b[1] - point_a[1]
                )

                return (x, y)

            target_distance -= segment_distance

        return self.route[-1]

    def update_position(self, progress):
        self.position = self.calculate_position(progress)

    def stop(self):
        self.status = "STOPPED"

    def start(self):
        self.status = "RUNNING"

    def get_status(self):
        return {
            "bus_id": self.bus_id,
            "position": self.position,
            "speed": self.speed,
            "status": self.status
        }


def display_bus(bus):
    data = bus.get_status()

    print(
        f"{data['bus_id']} | "
        f"Location: "
        f"({data['position'][0]:.2f}, "
        f"{data['position'][1]:.2f}) | "
        f"Speed: {data['speed']:.1f} km/h | "
        f"Status: {data['status']}"
    )


def main():
    routes = {
        "B01": [
            (0, 0),
            (2, 1),
            (4, 2),
            (6, 2),
            (8, 3),
            (10, 4)
        ],

        "B02": [
            (10, 0),
            (8, 1),
            (6, 2),
            (4, 3),
            (2, 3),
            (0, 4)
        ],

        "B03": [
            (0, 4),
            (2, 4),
            (4, 3),
            (6, 3),
            (8, 2),
            (10, 1)
        ]
    }

    speeds = {
        "B01": 30.0,
        "B02": 35.0,
        "B03": 28.0
    }

    buses = []

    for bus_id in routes:
        bus = Bus(
            bus_id,
            routes[bus_id],
            speeds[bus_id]
        )
        buses.append(bus)

    print("=" * 65)
    print("              BUS TRACKING SYSTEM")
    print("=" * 65)

    for simulation_time in range(0, 11):

        print(f"\nSimulation Time: {simulation_time} min")
        print("-" * 65)

        for bus in buses:

            # Simulated movement
            progress = (simulation_time / 10) % 1.0

            bus.update_position(progress)

            display_bus(bus)

        time.sleep(0.2)

    print("\nSimulation completed.")


if __name__ == "__main__":
    main()
