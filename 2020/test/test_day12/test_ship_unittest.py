import unittest
from Day12.Ship import Ship


test_nav_path = 'test/test_day12/test_input.txt'
test_nav_code = [('F', 10), ('N', 3), ('F', 7), ('R', 90), ('F', 11)]


class InitTests(unittest.TestCase):
    def setUp(self):
        self.ship = Ship()

    def tearDown(self):
        del self.ship

    def test_class(self):
        self.assertIsInstance(self.ship, Ship)

    def test_heading(self):
        self.assertEqual(self.ship.heading, "E",
                         "Ship heading should begin at 'E'")

    def test_position(self):
        self.assertTupleEqual(self.ship.position, (0, 0),
                              "Ship position should begin at (0,0)")

    def test_nav_code(self):
        self.assertEqual(self.ship.nav_code, None,
                         "Ship should have nav_code as None if not passed a path")

    def test_compass(self):
        self.assertEqual(self.ship.compass, {
                         "N": 0, "E": 90, "S": 180, "W": 270}, "compass props")

    def test_waypoint(self):
        self.assertEqual(self.ship.waypoint, (10, 1),
                         "ship should have a waypoint")

    def test_nav_with_path_on_init(self):
        self.new_ship = Ship(test_nav_path)
        self.assertEqual(self.new_ship.nav_code, test_nav_code,
                         "Ship should process nav code on init if created with a path")


class NavCodeTests(unittest.TestCase):
    def setUp(self):
        self.ship = Ship()

    def tearDown(self):
        del self.ship

    def test_nav_parse(self):
        nav_code = self.ship.parse_nav_code(test_nav_path)
        self.assertListEqual(nav_code, test_nav_code,
                             f"{nav_code} should have matched {test_nav_code}")


class MoveTests(unittest.TestCase):
    def setUp(self):
        self.ship = Ship()

    def tearDown(self) -> None:
        del self.ship

    def test_move_exists(self) -> None:
        self.assertTrue(hasattr(self.ship, "move"))

    def test_move_returns_coords(self):
        self.assertEqual(self.ship.move(), (0, 0))

    def test_move_moves_coords(self):
        result = self.ship.move(1)
        self.assertEqual(result, (1, 0), "default move should be to East")

    def test_move_distance(self):
        self.assertEqual(self.ship.move(3), (3, 0),
                         "Distance should move in coords correctly")
        self.ship.position = (1, 0)
        self.assertEqual(self.ship.move(-3), (-2, 0),
                         "Ship should move from current position")

    def test_move_along_heading(self):
        self.assertEqual(self.ship.move(2, "W"), (-2, 0),
                         "West should move negative on X")
        self.assertEqual(self.ship.move(3, "N"), (0, 3),
                         "N should move positive on Y")
        self.assertEqual(self.ship.move(2, "S"), (0, -2),
                         "S should move negative on Y")

    def test_move_waypoint(self):
        result = self.ship.move(1, 'E', 'waypoint')
        self.assertEqual(
            result, (11, 1), 'waypoint param should move the waypoint and not the ship')

    def test_move_to_waypoint_exists(self):
        self.assertTrue(hasattr(self.ship, "move_to_waypoint"))

    def test_move_to_waypoint_returns_new_ship_coords(self):
        result = self.ship.move_to_waypoint(1)
        self.assertEqual(result, (10, 1))


class TurnTests(unittest.TestCase):
    def setUp(self):
        self.ship = Ship()

    def tearDown(self) -> None:
        del self.ship

    def test_turn_exists(self):
        self.assertTrue(hasattr(self.ship, 'turn'),
                        "Ship should have turn method")

    def test_turn_returns_facing(self):
        self.assertEqual(self.ship.turn("L", 0), "E",
                         "Ship should not turn from original facing with 0 amt")

    def test_left_turn(self):
        self.assertEqual(self.ship.turn("L", 90), "N",
                         "90 degree left should be to N")

    def test_turn_past_north(self):
        self.assertEqual(self.ship.turn("L", 180), "W",
                         "180 degree turn should turn to West")

    def test_turn_right(self):
        self.assertEqual(self.ship.turn("R", 270), "N",
                         "270 degree right turn should turn to N")

    def test_turn_with_way_target(self):
        result = self.ship.turn("R", 90, "waypoint")
        self.assertEqual(result, (1, -10),
                         "Waypoint should move 90 degrees to right")

    def test_left_way_turn(self):
        result = self.ship.turn("L", 90, "waypoint")
        self.assertEqual(result, (-1, 10))

    def test_180_way_turn(self):
        result = self.ship.turn("R", 180, "waypoint")
        self.assertEqual(result, (-10, -1))

    def test_270_way_turn(self):
        left_result = self.ship.turn("L", 270, "waypoint")
        right_result = self.ship.turn("R", 270, "waypoint")
        self.assertEqual((left_result, right_result), ((1, -10), (-1, 10)))


class RunNavTests(unittest.TestCase):
    def setUp(self):
        self.ship = Ship()

    def tearDown(self) -> None:
        del self.ship

    def test_run_step(self):
        self.assertTrue(hasattr(self.ship, 'run_step'))

    def test_run_step_updates_heading_on_turn(self):
        self.ship.run_step(("L", 90))
        self.assertEqual(self.ship.heading, "N")
        self.ship.run_step(("R", 270))
        self.assertEqual(self.ship.heading, "W")

    def test_run_step_updates_coords_on_move(self):
        self.ship.run_step(("F", 3))
        self.assertEqual(self.ship.position, (3, 0))
        self.ship.run_step(("S", 5))
        self.assertEqual(self.ship.position, (3, -5))
        self.assertEqual(self.ship.heading, "E")


class RunWayStepTests(unittest.TestCase):
    def setUp(self):
        self.ship = Ship()

    def tearDown(self) -> None:
        del self.ship

    def test_way_step_exists(self):
        self.assertTrue(hasattr(self.ship, "run_way_step"))

    def test_way_step_moves_waypoint(self):
        self.ship.run_way_step(("N", 4))
        self.assertEqual(self.ship.waypoint, (10, 5),
                         "Waystep moves waypoint north by 4 on N 4 ")

    def test_way_step_moves_ship(self):
        self.ship.run_way_step(("F", 1))
        self.assertEqual(self.ship.position, (10, 1),
                         "Waystep moves ship to waypoint")

    def test_way_step_turn(self):
        self.ship.run_way_step(("R", 90))
        self.assertEqual(self.ship.waypoint, (1, -10),
                         "Waystep should turn the waypoint")


class RunNavCodeTests(unittest.TestCase):
    def setUp(self):
        self.ship = Ship()

    def tearDown(self) -> None:
        del self.ship

    def test_run_nav_code(self):
        self.assertTrue(hasattr(self.ship, 'run_nav_code'))
        self.assertEqual(self.ship.run_nav_code(), ("E", (0, 0)),
                         "Should return (facing, coords)")

    def test_run_nav_code_updates(self):
        result = self.ship.run_nav_code(1, test_nav_code)
        self.assertEqual(result, ("S", (17, -8)))

    def test_run_nav_code_v2(self):
        result = self.ship.run_nav_code(2, test_nav_code)
        self.assertEqual(result, ("E", (214, -72)),
                         "V2 result should be 214E, 72S")


class ManhattanDistanceTests(unittest.TestCase):
    def setUp(self):
        self.ship = Ship()

    def tearDown(self) -> None:
        del self.ship

    def test_manhattan_distance(self):
        self.assertTrue(hasattr(self.ship, "get_manhattan_distance"))

    def test_returns_zero_on_start(self):
        self.assertEqual(self.ship.get_manhattan_distance(), 0)

    def test_returns_accurate_result(self):
        self.ship.run_nav_code(1, test_nav_code)
        self.assertEqual(self.ship.get_manhattan_distance(), 25)

    def test_v2_returns_accurate_result(self):
        self.ship.run_nav_code(2, test_nav_code)
        self.assertEqual(self.ship.get_manhattan_distance(), 286)
