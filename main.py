from itertools import count
from utils.input_to_list import input_to_list
from Day1.expense_reporter import report_expenses
from Day2.parse_input import parse_input
from Day2.Pass import Pass
from Day3.toboggan_trajectory import calculate_trajectory
from Day4.passport_validator import validate_all, parse_input
from Day5.seat_parser import parse_row, parse_column, get_seat_ID, get_all_seats, get_missing_seat
from Day6.customs_count import parse_input, count_group, count_all_groups
from Day7.bag_finder import parse_rules, find_containers
from Day8.handheld_runner import parse_code, Handheld
# path = 'Day1\input.txt'
# report_expenses('Day1\input.txt', 2020, 3)

# path = 'Day2\input.txt'
# pass_list = parse_input(path)
# pass_count = [password.validate_count() for password in pass_list].count(True)
# pass_count_revised = [password.validate_position() for password in pass_list].count(True)
# print(pass_count)
# print(pass_count_revised)

# path = 'Day3\input.txt'
# calculate_trajectory(path, [(3, 1)])
# calculate_trajectory(path, [(1,1), (3,1), (5,1), (7,1), (1,2)])

# path = 'Day4/input.txt'
# valid = validate_all(path)
# print(valid)

# path = 'Day5/input.txt'
# data = input_to_list(path, False)
# seats = get_all_seats(data)
# print(seats)
# missing = get_missing_seat(seats)
# print(missing)

# path = 'Day6/input.txt'
# groups = parse_input(path)
# print(count_all_groups(groups))

# path = 'Day7/input.txt'
# rules = parse_rules(path)

# (contains, contained_in) = parse_rules(path)
# containers = find_containers('shiny gold', contained_in)

# print(contains['dim lavender'])
# containing = count_containing('shiny gold', contains)
# print(containing)
# total = 0
# for bag in containing:
#     total += containing[bag]
# print(total)

path = 'Day8/input.txt'
instructions = parse_code(path)
# print(instructions)
handheld = Handheld(instructions)
handheld.process_code(None)
# handheld.debug_instructions()
