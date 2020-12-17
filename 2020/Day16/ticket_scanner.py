import fileinput
import sys
from functools import reduce


def parse_notes(file):
    with open(file, 'r') as f:
        data = [line.split("\n")for line in f.read().split("\n\n")]
        f.close()
    # rules = {key: val for line.split(":") for key, val in line in data[0]}
    notes = {
        'rules': {},
        'own_ticket': [int(num) for num in data[1][1].split(",")],
        'nearby_tickets': [[int(num) for num in line.split(",")] for line in data[2][1:]]
    }
    for line in data[0]:
        name, rules = line.split(": ")
        notes["rules"][name] = list()
        for rule in rules.split(" or "):
            low, high = rule.split("-")
            notes["rules"][name].append((range(int(low), int(high)+1)))
    return notes


def validate_ticket(rules, ticket):
    invalid = [num for num in ticket if not any(
        [num in limit for limits in rules.values() for limit in limits])]

    return invalid


def validate_all_tickets(notes):
    rules, own_ticket, tickets = notes.values()
    for ticket in tickets:
        print(sum(validate_ticket(rules, ticket)))
    total_invalid = sum([sum(validate_ticket(rules, ticket))
                         for ticket in tickets])
    print(total_invalid)


def update_notes(notes):
    notebook = notes.copy()
    tickets = notes["nearby_tickets"]
    filtered = [ticket for ticket in tickets if len(
        validate_ticket(notes["rules"], ticket)) == 0]
    notebook["nearby_tickets"] = filtered
    return notebook


def parse_ticket_rules(notes):
    rules = notes["rules"]
    tickets = notes["nearby_tickets"]
    ticket_length = max(len(ticket) for ticket in tickets)

    possible = {}
    for name in rules.keys():
        possible[name] = list()
    for rule, limits in rules.items():
        for i in range(ticket_length):
            if all([any([ticket[i] in limit for limit in limits]) for ticket in tickets]):
                possible[rule].append(i)

    for n, el in sorted(possible.items(), key=lambda x: len(x[1])):
        el = el[0]
        possible[n] = el
        for x, y in possible.items():
            if x != n:
                if isinstance(y, list) and el in y:
                    y.remove(el)
    return possible


def apply_to_ticket(indices, ticket):
    answer = reduce(lambda x, y: x * y, [ticket[val]
                                         for name, val in indices.items() if 'departure' in name])
    print(answer)


if __name__ == "__main__":
    notebook = parse_notes(sys.argv[1])
    updated = update_notes(notebook)
    rules = parse_ticket_rules(updated)
    apply_to_ticket(rules, updated["own_ticket"])
