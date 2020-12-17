import fileinput
from itertools import product
from collections import defaultdict


def parse_bitmasking_code(code):
    cleaned = [line.strip() for line in list(code)]
    parsed = list()
    command = {
        "ops": list()
    }
    for line in cleaned:
        if 'mask' in line:
            if "mask" in command.keys():
                parsed.append(command)
                command = {
                    "ops": list()
                }
            command["mask"] = line.split(" = ")[1]
        else:
            loc, val = line.split(" = ")
            addr = int(loc[4:-1])
            val = int(val)
            command["ops"].append((addr, val))
    parsed.append(command)
    return parsed


class Mask:
    def __init__(self, mask):
        self.or_mask = int(mask.replace('X', '0'), 2)
        self.and_mask = int(mask.replace('X', '1'), 2)

    def apply(self, val):
        val |= self.or_mask
        val &= self.and_mask
        return val


class AddressDecoder:
    def __init__(self, mask):
        self.masks = []
        self.or_mask = int(mask.replace('X', '0'), 2)
        template = mask.replace('X', '{}').replace('0', 'X').replace('1', 'X')
        variations = mask.count('X')
        for perm in product('01', repeat=variations):
            self.masks.append(Mask(template.format(*perm)))

    def apply(self, val):
        to_write = []
        val |= self.or_mask
        for mask in self.masks:
            to_write.append(mask.apply(val))
        return to_write


def part1(code):
    memory = defaultdict(lambda: 0)
    mask = None
    for chunk in code:
        mask = Mask(chunk["mask"])
        for addr, val in chunk["ops"]:
            val = mask.apply(val)
            memory[addr] = val

    return sum(memory.values())


def part2(code):
    memory = defaultdict(lambda: 0)
    decoder = None
    for chunk in code:
        decoder = AddressDecoder(chunk["mask"])
        for addr, val in chunk["ops"]:
            for idx in decoder.apply(addr):
                memory[idx] = val
    return sum(memory.values())


if __name__ == "__main__":
    # do something here
    code = parse_bitmasking_code(fileinput.input())
    part_one = part1(code)
    print(part_one)
    part_two = part2(code)
    print(part_two)
    # part_one = apply_bitmask(code)
    # print(part_one)
    # part_two = decode_address(code)
