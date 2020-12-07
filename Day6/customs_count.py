from functools import reduce


def parse_input(path):
    with open(path, "r") as f:
        groups = [x.split("\n") for x in f.read().split("\n\n")]
        f.close()
    return groups


def count_group(group):
    total_yeses = set((letter for form in group for letter in form))
    total_all_yeses = set(filter(lambda x: all(
        x in form for form in group), total_yeses))
    return (len(total_yeses), len(total_all_yeses))


def count_all_groups(input):
    group_counts = [count_group(group) for group in input]
    total_counts = reduce(
        (lambda x, y: (x[0] + y[0], x[1] + y[1])), group_counts)
    print(
        f"Total of all questions answered 'yes': {total_counts[0]} \nTotal of all questions answered 'yes' by whole group: {total_counts[1]}")
    return total_counts
