from utils.input_to_list import input_to_list
from Day2.Pass import Pass

def parse_input(path):
    parsed = [parse_line(line.split(" ")) for line in input_to_list(path, False)]
    return [Pass(limits, letter, pword) for (limits, letter, pword) in parsed]

def parse_line(line):
    limits = line[0].split("-")
    letter = line[1].replace(":", "")
    pword = line[2]
    return (limits, letter, pword)