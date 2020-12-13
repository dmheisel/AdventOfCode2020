from functools import cache
from copy import deepcopy


def create_board(filepath):
    with open(path, 'r') as f:
        data = [list(line) for line in f.read().split("\n")]
        f.close()
    return data


path = 'Day11/input.txt'
board = create_board(path)


@cache
def in_bounds(row, col):
    return 0 <= row <= len(board)-1 and 0 <= col <= len(board[row])-1


@cache
def get_neighbors(row, col):
    neighbors = [(x, y) for
                 y in [col - 1, col, col + 1] for
                 x in [row - 1, row, row + 1]
                 if (x, y) != (row, col) and in_bounds(x, y)]
    return neighbors


@cache
def get_visible(row, col):
    directions = [(i, j) for j in range(-1, 2) for i in range(-1, 2)
                  if (i, j) != (0, 0)]
    visible = list()
    for x, y in directions:
        next_row = row
        next_col = col
        while True:
            next_row += x
            next_col += y
            if in_bounds(next_row, next_col):
                if board[next_row][next_col] != '.':
                    visible.append((next_row, next_col))
                    break
            else:
                break
    return visible


def run_cycle(board, round):
    new_board = deepcopy(board)
    for x, row in enumerate(board):
        for y, seat in enumerate(row):
            if seat == ".":
                continue
            func = get_neighbors if round == 1 else get_visible
            tolerance = 4 if round == 1 else 5
            total_neighbors = sum(
                [1 for (i, j) in func(x, y) if board[i][j] == "#"])
            if total_neighbors == 0:
                new_board[x][y] = "#"
            elif total_neighbors >= tolerance:
                new_board[x][y] = "L"
    return new_board


def run_cycles(board, round):
    this_board = None
    cycle = 0
    next_board = deepcopy(board)
    while(this_board != next_board):
        this_board = deepcopy(next_board)
        next_board = run_cycle(this_board, round)
        cycle += 1
        print(f'Incrementing cycle to {cycle}')
    occupied = sum([row.count("#") for row in this_board])
    print(f"Total occupied seats: {occupied}")
    return occupied


print("Running Part One...")
part_one_results = run_cycles(board, 1)


print(f"Running Part Two")
part_two_results = run_cycles(board, 2)

print(f"Results from part one: {part_one_results}")
print(f"Results from part two: {part_two_results}")
