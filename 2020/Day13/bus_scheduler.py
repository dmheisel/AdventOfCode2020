def build_schedule(path):
    with open(path, 'r') as f:
        time, buses = f.read().split("\n")
        notes = (int(time), [bus
                             for bus in buses.split(",")])
        f.close()
    return notes


def find_soonest_bus(notes):
    curr_time, buses = notes
    wait_times = [(int(bus) - curr_time % int(bus), bus)
                  for bus in buses if bus != "x"]
    wait_times.sort(key=lambda x: x[0])
    return wait_times[0]


def find_bus_sequence(schedule):
    buses = schedule[1]
    time = 0
    cycle_step = 1  # cycle_step starts at 1, updates once each overlap is found
    for i, bus in enumerate(buses):
        # index, bus
        if bus == 'x':
            continue
        bus = int(bus)

        # bus repeat time minus minute it departs, modulo the time to repeat (bus number)
        # this will get the offset from 0 this bus's repeat cycle is on
        offset = (bus - i) % bus
        while time % bus - offset != 0:
            # while diff between the time and bus (on the offset) is not 0, increase the time by the cycle_step
            time += cycle_step
        print(f"Repeat found at {time}")
        print(f"Updated cycle step to {cycle_step}")
        # the new cycle_step is the repeat cycle for this bus, each next bus will have to meet this repeat cycle
        # only need to check the spots where the known buses overlap and see where the new bus overlaps with them
        cycle_step = cycle_step * bus

    print(f"Final interval time is {time}")
    return time


path = 'Day13/input.txt'

notes = build_schedule(path)
wait, bus_num = find_soonest_bus(notes)
print(
    f" wait time to depart on bus {bus_num} is {wait}, answer is {wait * int(bus_num)}")

find_bus_sequence(notes)
