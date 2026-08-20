import unittest

from bus_tracking import Bus


class TestBusTracking(unittest.TestCase):

    def setUp(self):
        self.route = [
            (0, 0),
            (5, 0),
            (10, 0)
        ]

        self.bus = Bus(
            "B01",
            self.route,
            30.0
        )

    def test_bus_id(self):
        self.assertEqual(
            self.bus.bus_id,
            "B01"
        )

    def test_speed(self):
        self.assertEqual(
            self.bus.speed,
            30.0
        )

    def test_initial_position(self):
        self.assertEqual(
            self.bus.position,
            (0, 0)
        )

    def test_position_at_start(self):
        position = self.bus.calculate_position(0)

        self.assertEqual(
            position,
            (0, 0)
        )

    def test_position_at_middle(self):
        position = self.bus.calculate_position(0.5)

        self.assertAlmostEqual(
            position[0],
            5.0
        )

        self.assertAlmostEqual(
            position[1],
            0.0
        )

    def test_position_at_end(self):
        position = self.bus.calculate_position(1)

        self.assertEqual(
            position,
            (10, 0)
        )

    def test_invalid_progress(self):
        with self.assertRaises(ValueError):
            self.bus.calculate_position(1.5)

    def test_stop_bus(self):
        self.bus.stop()

        self.assertEqual(
            self.bus.status,
            "STOPPED"
        )

    def test_start_bus(self):
        self.bus.stop()
        self.bus.start()

        self.assertEqual(
            self.bus.status,
            "RUNNING"
        )


if __name__ == "__main__":
    unittest.main()
