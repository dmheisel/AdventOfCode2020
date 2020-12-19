import sys
import time
from rich import print


def create_equations(path):
    with open(path, 'r') as f:
        data = [[char for char in line.replace(
            " ", "")]for line in f.read().split("\n")]
        f.close()
    return data


def process_all_equations(maths):
    acc = 0
    for equation in maths:
        acc += newest_math(equation)
    return acc


def resolve(ops, vals):
    this_val = vals.pop()
    op = ops.pop()
    next_val = vals.pop()
    result = int()
    if op == "*":
        # multiplication
        result = this_val * next_val
    elif op == "+":
        # addition
        result = this_val + next_val
    elif op == "🎄":
        # average rounding down
        result = (this_val + next_val) // 2
    return vals.append(result)


def newest_math(equation, priorities=None):
    priorities = {
        "🎄": 2,
        "+": 1,
        "*": 0
    }
    nums = list()
    ops = list()
    index = 0

    while len(equation):
        val = equation.pop(0)
        # print(f'processing value {val}')
        index += 1
        try:  # try to handle it like an int, if this fails, it's an op or paren
            nums.append(int(val))
        except:
            if val == "(":
                # Handle parenthesis/bracketed equations, resolve them first
                paren_result = newest_math(equation)  # recursion!
                nums.append(paren_result)
            elif val == ")":
                # We've hit the end of the parenthesis, time to return the value
                break
            else:
                # Only other option is that we found an operator!
                if any([priorities[op] >= priorities[val] for op in ops]):
                    # if there are higher priorities than this in the stack, flush it
                    while len(ops) > 0 and any([priorities[op] >= priorities[val] for op in ops]):
                        resolve(ops, nums)
                # finally add this into the operators bucket.
                ops.append(val)
    # equation is done, resolve anything left
    while len(ops) > 0:
        resolve(ops, nums)
    return nums.pop()


if __name__ == "__main__":
    maths = create_equations(sys.argv[1])

    result = process_all_equations(maths)
    # result = new_new_new_math(maths[360])
    print(f"final result of all equations summed: {result}")
