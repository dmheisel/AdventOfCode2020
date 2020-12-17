from Computer import *
from itertools import permutations


class AmpCircuit(object):
    def __init__(self, code_in=None):
        self.code_in = list(code_in)
        self.num_amps = 5
        self.amps = {num: Computer(self.code_in)
                     for num in range(self.num_amps)}
        # print(self.amps)

    def run_amp(self, amp, inp):
        return

    def run_circuit(self, *phase_settings):
        # calibrate amp computers and set phase settings
        print(f'running circuit with {phase_settings}')
        for i, phase in enumerate(phase_settings):
            print(f'Setting phase on amp {i} to {phase}')
            amp = self.amps[i]
            amp.reset()
            amp.I.append(phase)

        curr_i = 0
        curr_amp = self.amps[curr_i]
        out = 0
        while not curr_amp.halted:
            print(f"Output of {out} added to input params for amp {curr_i}")
            curr_amp.I.append(out)
            out = curr_amp.run()
            print(f"Amp {curr_i} ouputs {out}")
            curr_i = (curr_i + 1) % self.num_amps
            curr_amp = self.amps[curr_i]
        return out

    def run_array(self, *phases):
        input = 0
        phases = list(phases)
        for i in range(self.num_amps):
            amp = self.amps[i]
            amp.reset()
            amp.I.append(phases.pop(0))
            amp.I.append(input)
            input = amp.run()
        return input

    def calculate_optimal_array(self, amp_range=None):
        amp_range = amp_range if amp_range != None else range(self.num_amps)
        possible_configurations = permutations(amp_range)
        results = [self.run_circuit(*perm) for perm in possible_configurations]
        results.sort(reverse=True)
        return results[0]


if __name__ == "__main__":
    print('running!')
    amp = AmpCircuit(fileinput.input())
    # print(list(permutations(range(5))))
    print(amp.calculate_optimal_array(range(5, 10)))
    # print(amp.run_circuit([9, 7, 8, 5, 6]))
