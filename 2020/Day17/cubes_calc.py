from functools import cache
from itertools import product
from rich import print
import time
import sys
from collections import Counter
dirs = list(product(range(-1, 2), repeat=4))
dirs.remove((0, 0, 0, 0))


def chart_init_positions(path, dims=3):
    with open(path, 'r') as f:
        data = f.read().split("\n")
        f.close()
    maps = {(0, 0, r, c) for r, line in enumerate(data) for c, char in enumerate(line)
            if char == "#"}
    return maps


@cache
def get_neighboring_points(i):
    neighbors = [tuple(v + dir[k] for k, v in enumerate(i))for dir in dirs]
    return neighbors


def update_maps(points):
    counts = Counter()
    for i in points:
        counts.update(get_neighboring_points(i))
    new_map = {k for k, v in counts.items() if (k not in points and v == 3) or (
        k in points and v in [2, 3])}
    return new_map


def round_one(path, rounds=6):
    counter = 1
    START = time.perf_counter_ns()
    old_map = new_map = chart_init_positions(path)
    while counter <= rounds:
        new_map = update_maps(old_map)
        print(len(new_map))
        counter += 1
        old_map = new_map
    print(f'Completed {rounds} rounds! Total active cubes: {len(new_map)}')
    END = time.perf_counter_ns()
    print(f"Part 2 took {END - START} nanoseconds")
    return len(new_map)


if __name__ == "__main__":
    chart = chart_init_positions(sys.argv[1])
    round_one(sys.argv[1])
