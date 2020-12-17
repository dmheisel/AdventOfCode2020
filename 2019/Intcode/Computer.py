import fileinput
import argparse
from Op.Op import *
from Ops import *
from Constants import *
from int_display import Display
import time


def delayed(iter, delay=.05):
    for item in iter:
        yield item
        time.sleep(delay)


class Computer(object):
    def __init__(self, code_in=None, inp=None):
        self.code_in = None if code_in == None else list(code_in)
        self.int_code = self.parse_input() if self.code_in != None else None
        self.pointer = 0
        self.relative_base = 0
        self.halted = False
        self.debug = False
        self.debug_log = list()
        self.I, self.O = (list([inp]) if inp != None else list(), list())
        self.ops = ops

    def parse_input(self, code_in=None):
        code_in = code_in if code_in != None else self.code_in
        return [int(char) for line in code_in for char in line.split(",")]

    def request_input(self):
        if len(self.I):
            return self.I.pop(0)
        else:
            new_input = input(
                "Int Code requesting input, none in program.  Please provide input to proceed:")
            return int(new_input)

    def debug_msg(self, *message):
        self.debug_log.append(message)
        if self.debug == True:
            print(*message)
        else:
            return True

    def access_int_code(self, indx=None):
        indx = indx if indx != None else self.pointer
        if indx >= len(self.int_code):
            diff = indx - len(self.int_code) + 1
            self.int_code += [0] * diff

        self.debug_msg(
            f"Accessed int code value {self.int_code[indx]} from index {indx}")
        return self.int_code[indx]

    def update_pointer(self, amt=1, jmp=False):
        self.debug_msg(
            f"Updating pointer at {self.pointer} by {amt}. Jumping: {jmp}")
        if jmp:
            self.pointer = amt
        else:
            self.pointer += amt
        # self.display.highlight(self.pointer)
        time.sleep(.05)
        return True

    def update_base(self, amt=0):
        self.debug_msg(
            f"Updating relative base {self.relative_base} by {amt}")
        self.relative_base += amt
        return True

    def mod(self, indx, val):
        self.debug_msg(f"Modifying int code value at {indx} to {val}")
        if indx >= len(self.int_code):
            diff = indx - len(self.int_code) + 1
            self.int_code += [0] * diff
        try:
            self.int_code[indx] = val
            return True
        except:
            self.debug_msg(f"Unable to modify int code at {indx}")
            return False

    def run_op(self, op, *args):
        op = self.ops[op]
        return op(self, *args)

    def parse_code(self):
        code = self.access_int_code()
        self.update_pointer()
        return code

    def parse_code_params(self, code):
        code = str(code).zfill(5)  # pad left to length 4 with zeroes
        op_code = int(code[-2:])  # last two digs are op code
        op = self.ops[op_code]
        # first two digits are mode codes, in reverse
        modes = list(reversed([int(mode) for mode in code[:-2]]))
        # modes.reverse()
        params = list()
        for i in range(op.params):
            tmp_val = self.access_int_code(self.pointer + i)
            mode = modes[i]
            if mode == POS:
                if op.write and i + 1 == op.params:
                    self.debug_msg(
                        f"Positional mode overridden for write, keeping {tmp_val}")
                    params.append(tmp_val)
                else:
                    self.debug_msg(f"Positional mode, parameter updating...")
                    params.append(self.access_int_code(tmp_val))
            elif mode == IMM:
                params.append(tmp_val)
            elif mode == REL:
                rel_val = self.relative_base + tmp_val
                if op.write and i + 1 == op.params:
                    self.debug_msg(
                        f"Rel mode updated for write, keeping {rel_val}")
                    params.append(rel_val)
                else:
                    self.debug_msg(
                        f'Relative Mode: {rel_val}, {self.relative_base}, {tmp_val}')
                    self.debug_msg(f"Pointer at {self.pointer + i}")
                    params.append(self.access_int_code(rel_val))
        self.update_pointer(op.params)
        return op_code, params

    def run(self):
        # self.display.boot(self.int_code)
        code = None
        while not self.halted:
            raw_code = self.parse_code()
            code, args = self.parse_code_params(raw_code)
            self.debug_msg(
                f"Next code run from raw code: {raw_code} with args: {args}")
            if self.run_op(code, *args) == False:
                self.debug_msg("Op run error!  See debug log...")
                return False
        # self.display.display("Int Code Run Complete")
        # self.display.display(f"{self.O}")
        return self.O

    def halt(self):
        self.halted = True
        return True

    def trace_input(self, target=None):
        for noun in range(100):
            for verb in range(100):
                self.int_code[1] = noun
                self.int_code[2] = verb
                result = self.run()[0]
                if result == target:
                    print(
                        f"Input trace complete, target found with 100 * {noun} + {verb}")
                    self.O.append(100 * noun + verb)
                    return 100 * noun + verb
                else:
                    self.reset()

    def reset(self):
        self.int_code = self.parse_input()
        self.pointer = 0
        self.halted = False
        self.I, self.O = (list(), list())
        return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Intcode computer")
    parser.add_argument("input", metavar="f")
    parser.add_argument("--fn", default="run")
    parser.add_argument('--arg', type=int)
    args = parser.parse_args()
    print(args)
    # print(args.arg)
    com = Computer(fileinput.input(args.input))
    print(f"Running {args.fn} with argument: {args.arg}")
    output = getattr(com, args.fn)() if args.arg == None else getattr(
        com, args.fn)(args.arg)
    # print(f"Output is {output}")
