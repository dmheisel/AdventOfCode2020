
from utils.input_to_list import input_to_list
from functools import reduce


def parse_report(path):
    return input_to_list(path)


def find_sum(nums, sum, depth, start=0):
    if (depth == 1):
        # if at depth of one, no more recursion is needed
        return [sum] if sum in nums else False
    else:
        for index, num in enumerate(nums):
            # for each number in the list
            if sum - num < 0 or index + 1 == start:
                # if the next number is too big or it's the starting number, skip it
                continue
            found = find_sum(nums, sum-num, depth-1, index + 1)
            if found:
                # if find_sum returns a number, add it and the number into an array and return it
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
