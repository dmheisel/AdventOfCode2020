def parse_code(path):
    with open(path, "r") as f:
        data = [(line.split(" ")[0], int(line.split(" ")[1]))
                for line in f.read().split("\n")]
        f.close()
    return data


class Handheld:

    def __init__(self, boot_code):
        self.boot_code = boot_code  # our instructions
        self.accumulator = 0  # eventual output
        self.pointer = 0  # points at next instruction

    def reset(self, acc, pointer, boot_code):
        # function to reset state to specific settings
        print(f"Resetting state to acc:{acc}, ptr: {pointer}")
        self.accumulator = acc
        self.pointer = pointer
        self.boot_code = boot_code.copy()

    def process_step(self, op, amount):
        # processes one set of instructions
        if op == 'dead':
            # 'killed' code, already processed once
            print(f'Found dead code at {self.pointer}, terminating...')
            return False
        if op == 'jmp':
            # jump ahead to amount
            self.pointer += amount
            return True
        elif op == 'acc':
            # accumulate to output
            self.accumulator += amount
        # acc and nop both increment pointer by one
        self.pointer += 1
        return True

    def process_code(self, boot_code=None, alt_run=False):
        # default bootcode is boot_code from init
        if boot_code is None:
            boot_code = self.boot_code

        # continue running while the pointer is within the range of the bootcode
        while self.pointer in range(len(self.boot_code)):
            # set working commands, kill version in boot_code index
            op, amount = step = boot_code[self.pointer]
            boot_code[self.pointer] = ("dead", None)

            # if not in a alternate run and hitting a jmp or nop, do this
            if (not alt_run) and (op in ['jmp', 'nop']):
                # take a snapshot of the current state for coming back to
                state = (self.accumulator, self.pointer,
                         boot_code.copy())
                # create new boot_code with swapped command
                new_op = 'jmp' if op == 'nop' else 'nop'
                new_code = boot_code.copy()
                new_code[self.pointer] = (new_op, amount)
                print(f'Attempting code swap at pointer {self.pointer}.')

                # see if process on swapped command is a success
                end_code = self.process_code(new_code, True)
                if not end_code:
                    print(
                        f"Swap failed, reverting state.")
                    self.reset(*state)
                else:
                    return end_code

            if not self.process_step(*step):
                # returns false on finding a dead command, prevents loops
                return False

        print("Finished processing code")
        print(f"Final accumulator value is: {self.accumulator}")
        return self.accumulator
