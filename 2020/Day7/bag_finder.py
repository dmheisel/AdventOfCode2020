import re
import collections
from functools import reduce


def parse_rules(path):
    with open(path, "r") as f:
        lines = f.read().split("\n")
        # dict with lists of what each color contains
        contains = collections.defaultdict(list)
        # dict with sets of what each color is contained in
        contained_in = collections.defaultdict(set)

        for line in lines:
            bag_color = re.match(r'(.+?) bags contain', line)[1]
            # bag_color is the words before 'bags contain'
            inner_bags = re.findall(r'(\d+) (.+?) bags?[,.]', line)
            # inner_bags is tuples of num, color of the bags inside the bag_color bag
            for num, col in inner_bags:
                contained_in[col].add(bag_color)
                # add of each inner bag to the contained_in set for this bag
                contains[bag_color].append((col, int(num)))
                # add the (color, number) of each inner bag to the contained list for this bag.

        f.close()
        return (contains, contained_in)


def find_containers(color, contained_in_set, found_set=set()):
    # for each bag that contains this color, check to see what bag contains that
    # call recursively on each bag and keep adding to found_set
    for bag in contained_in_set[color]:
        found_set.add(bag)
        next_set = find_containers(bag, contained_in_set, found_set)
        for next_bag in next_set:
            found_set.add(next_bag)
    return found_set


def find_containing(color, contains_set, amt=1, found_set=collections.defaultdict(int)):
    # for the bag of the color, find what it *must* contain from the contains_set
    # call recursively on each bag in found_set
    for bag, amount in contains_set[color]:
        print(bag, amount)
        multiplier = amount * amt
        found_set[bag] += multiplier
        found_set = find_containing(bag, contains_set, multiplier, found_set)
    return found_set
