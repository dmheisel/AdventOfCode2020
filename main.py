import utils
from Day1.expense_reporter import report_expenses
from Day2.parse_input import parse_input
from Day2.Pass import Pass
from Day3.toboggan_trajectory import calculate_trajectory

# path = 'Day1\input.txt'
# report_expenses('Day1\input.txt', 2020, 3)

# path = 'Day2\input.txt'
# pass_list = parse_input(path)
# pass_count = [password.validate_count() for password in pass_list].count(True)
# pass_count_revised = [password.validate_position() for password in pass_list].count(True)
# print(pass_count)
# print(pass_count_revised)

path = 'Day3\input.txt'
calculate_trajectory(path, [(3, 1)])
calculate_trajectory(path, [(1,1), (3,1), (5,1), (7,1), (1,2)])