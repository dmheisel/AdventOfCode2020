from utils.input_to_list import input_to_list

def parse_input(path):
    parsed = [line.split(" ") for line in input_to_list(path, False)]
    return [parse_line(line) for line in parsed]

def parse_line(line):
    limits = line[0].split("-")
    letter = line[1].replace(":", "")
    pword = line[2]
    return (limits, letter, pword)