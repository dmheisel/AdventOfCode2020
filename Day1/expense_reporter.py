
from utils.input_to_list import input_to_list
from functools import reduce

def parse_report(path):
    return input_to_list(path)

def find_sum(nums, sum, depth, start = 0):
    if (depth == 1):
        return [sum] if sum in nums else False
    else:
        for index, num in enumerate(nums):
            if sum - num < 0:
                continue
            if index + 1 == start:
                continue
            found = find_sum(nums, sum-num, depth-1, index + 1)
            if found:
                return [num, *found]
            else:
                continue
        return False

def report_expenses(path, target, depth):
    print("Parsing report...")
    report = parse_report(path)
    print(f"Finding {depth} entries to sum total {target}")
    answer = find_sum(report, target, depth)
    print(f"Found entries: {answer}")
    expense = reduce((lambda x, y: x * y), answer)
    print(f"total expense: {expense}")