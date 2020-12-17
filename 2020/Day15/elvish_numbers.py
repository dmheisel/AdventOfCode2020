from collections import defaultdict


def numbers_game(end, *starting_nums):
    print(starting_nums)
    turn = 0
    encountered = defaultdict(int)
    last_said = 0

    for num in starting_nums:
        turn += 1
        encountered[num] = turn
        last_said = num

    while turn < end:
        if last_said in encountered:
            next = turn - encountered[last_said]
        else:
            next = 0
        encountered[last_said] = turn
        last_said = next
        turn += 1

    print(last_said)


if __name__ == "__main__":
    numbers_game(30000000, 0, 6, 1, 7, 2, 19, 20)
