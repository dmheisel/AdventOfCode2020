from utils.input_to_list import input_to_list
from Day1.expense_reporter import report_expenses
from Day2.parse_input import parse_input
from Day2.Pass import Pass
from Day3.toboggan_trajectory import calculate_trajectory
from Day4.passport_validator import validate_all, parse_input
from Day5.seat_parser import parse_row, parse_column, get_seat_ID, get_all_seats, get_missing_seat
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

path = 'Day5/input.txt'
data = input_to_list(path, False)
seats = get_all_seats(data)
print(seats)
missing = get_missing_seat(seats)
print(missing)
