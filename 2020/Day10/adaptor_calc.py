from utils.input_to_list import input_to_list
import numpy as np


def adaptor_list(path):
    # returns a sorted list of adaptors including the outlet (0) and device (max + 3)
    adaptors = [0] + sorted(input_to_list(path))
    adaptors.append(max(adaptors) + 3)
    return adaptors


def find_adaptor_spread(path):
    # returns the total amount of 1-jolt adaptors * the total amount of 3-jolt adapters
    adaptors = adaptor_list(path)
    diffs = list(np.diff(adaptors))
    print(adaptors)
    print(diffs)
    single_jolt_adaptors = diffs.count(1)
    three_jolt_adaptors = diffs.count(3)
    return single_jolt_adaptors * three_jolt_adaptors


def build_paths(path):
    # creates a dict of all possible paths from each adaptor - {adaptor: [adaptor, adaptor]}
    adaptors = adaptor_list(path)
    paths = {}
    for adaptor in adaptors:
        potential = [adaptor + x for x in range(1, 4)]
        paths[adaptor] = [pot for pot in potential if pot in adaptors]
    return paths


def count_paths(paths):
    # counts total paths available at each point (at each adaptor)
    all_paths = {0: 1}
    for adaptor, neighbors in paths.items():
        for neighbor in neighbors:
            if neighbor in all_paths:
                all_paths[neighbor] += all_paths[adaptor]
            else:
                all_paths[neighbor] = all_paths[adaptor]
    return all_paths
