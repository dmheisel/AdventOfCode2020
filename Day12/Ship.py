class Ship:
    def __init__(self, path=None):
        self.heading = "E"
        self.position = (0, 0)
        self.nav_code = self.parse_nav_code(path) if path else None
        self.compass = {"N": 0, "E": 90, "S": 180, "W": 270}
        self.waypoint = (10, 1)

    def parse_nav_code(self, path):
        with open(path, 'r') as f:
            nav_code = [(line[:1], int(line[1:]))
                        for line in f.read().split("\n")]
            f.close()
        return nav_code

    def move(self, distance=0, dir=None, target="ship"):
        target = self.position if target == "ship" else self.waypoint
        x, y = target
        dir = self.heading if dir in ("F", None) else dir
        if dir == "W" or dir == "S":
            distance = -distance
        if dir in ("W", "E"):
            x += distance
        else:
            y += distance
        return (x, y)

    def move_to_waypoint(self, amt):
        x, y = self.position  # current position
        way_x, way_y = self.waypoint  # waypoint position

        # multiply waypoint position by amt (repeats of move to position)
        x += way_x * amt
        y += way_y * amt

        # return new coords
        return (x, y)

    def turn(self, dir, amt, target="ship"):
        if target == "ship":
            # turn the ship's heading
            curr_heading = self.compass[self.heading]
            if dir == "L":
                amt = -amt
            new_heading = next(
                k for k, v in self.compass.items() if v == (curr_heading + amt) % 360)
            return new_heading
        elif target == "waypoint":
            # turn the waypoint around the ship
            x, y = self.waypoint
            repeats = int(amt/90)
            for repeat in range(repeats):
                if dir == "R":
                    new_y = -x
                    new_x = y
                else:
                    new_y = x
                    new_x = -y
                x, y = new_x, new_y
            return (x, y)

    def run_step(self, step):
        op, amt = step
        if op in ("L", "R"):
            self.heading = self.turn(op, amt)
            return True
        elif op in ["F"] + list(key for key in self.compass.keys()):
            self.position = self.move(amt, op)
            return True
        return True

    def run_way_step(self, step):
        op, amt = step
        if op in list(key for key in self.compass.keys()):
            self.waypoint = self.move(amt, op, "waypoint")
            return True
        elif op in ("L", "R"):
            self.waypoint = self.turn(op, amt, "waypoint")
            return True
        elif op == 'F':
            self.position = self.move_to_waypoint(amt)
            return True
        return False

    def run_nav_code(self, v=1, input=None):
        nav_code = input if input != None else self.nav_code
        step_func = self.run_step if v == 1 else self.run_way_step
        try:
            for step in nav_code:
                step_func(step)
        except:
            print(f"No Nav Code, returning original location")
            pass
        return (self.heading, self.position)

    def get_manhattan_distance(self):
        x, y = self.position
        return abs(x) + abs(y)
