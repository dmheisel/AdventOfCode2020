from utils.input_to_list import input_to_list
from functools import reduce


def find_invalid(path):
    data = input_to_list(path)
    preamble_length = 25
    index = 25
    while check_array(data[index-preamble_length:index], data[index]):
        index += 1
    return (data[index], data[:index+1])


def check_array(array, num):
    return any(x + y == num for y in array for x in array)


def find_contiguous_set(arr, target):
    print(f'looking for {target}')
    target = int(target)
    for index, val in enumerate(arr):
        temp = []
        temp.append(val)
        for y in arr[index+1:]:
            temp.append(y)
            temp_sum = sum(temp)
            if temp_sum == target:
                return temp
            elif temp_sum > target:
                break


def solve(path):
    invalid, encountered = find_invalid(path)
    weak_set = find_contiguous_set(encountered, invalid)
    weak_set.sort()
    return weak_set[0] + weak_set[-1]
