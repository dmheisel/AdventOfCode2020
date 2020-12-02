import utils
from Day1.expense_reporter import report_expenses
from Day2.parse_input import parse_input
from Day2.Pass import Pass
# path = 'Day1\input.txt'
# report_expenses('Day1\input.txt', 2020, 3)

path = 'Day2\input.txt'
pass_list = [Pass(limits, letter, pword) for (limits, letter, pword) in parse_input(path)]
pass_count = [password.validate_count() for password in pass_list].count(True)
pass_count_revised = [password.validate_position() for password in pass_list].count(True)
print(pass_count_revised)