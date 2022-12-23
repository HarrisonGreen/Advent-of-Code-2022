import numpy as np
from itertools import combinations
from copy import deepcopy

file = open("Data/day16.txt", "r")

# Read in valves and tunnels from file

valves = {}

for line in file:
    line = line.split()
    line = [line[1], int(line[4][5:-1])] + [x[:2] for x in line[9:]]

    valves[line[0]] = {"flow": line[1], "tunnels": {x: 1 for x in line[2:]}}

# Remove valves with zero flow rate

to_remove = []

for valve in valves.keys():
    if valves[valve]["flow"] == 0 and valve != "AA":
        to_remove.append(valve)

for valve in to_remove:
    for valve_one, valve_two in combinations(valves[valve]["tunnels"].items(), 2):

        del valves[valve_one[0]]["tunnels"][valve]
        del valves[valve_two[0]]["tunnels"][valve]

        valves[valve_one[0]]["tunnels"][valve_two[0]] = min(valves[valve_one[0]]["tunnels"].get(valve_two[0], np.inf), valve_one[1] + valve_two[1])
        valves[valve_two[0]]["tunnels"][valve_one[0]] = valves[valve_one[0]]["tunnels"][valve_two[0]]
    
    del valves[valve]

# Add shortest paths between any pair of valves

change = True

while change:
    change = False
    updates = []

    for valve in valves.keys():
        for valve_one, dist_one in valves[valve]["tunnels"].items():
            for valve_two, dist_two in valves[valve_one]["tunnels"].items():

                if valve == valve_two:
                    continue

                if dist_one + dist_two < valves[valve]["tunnels"].get(valve_two, np.inf):
                    updates.append((valve, valve_two, dist_one + dist_two))
                    change = True
    
    for update in updates:
        valves[update[0]]["tunnels"][update[1]] = update[2]

# Find solution to maximise pressure release

positions = [("AA", 30, 0, {x: False for x in valves.keys()})]
current_best = 0
to_search = 3

while positions:
    current, time_left, score, status = positions.pop(0)
    destinations = []

    for valve in valves.keys():
        if valve == current or status[valve]:
            continue

        destinations.append((valve, valves[valve]["flow"] * (time_left - valves[current]["tunnels"][valve] - 1)))
    
    if len(destinations) == 0:
        continue
    
    destinations = sorted(destinations, key = lambda x: x[1], reverse = True)
    
    for i in range(min(len(destinations), to_search)):

        dest, add_score = destinations[i]
        new_time = time_left - valves[current]["tunnels"][dest] - 1

        if new_time <= 0:
            break

        new_status = deepcopy(status)
        new_status[dest] = True

        positions.append((dest, new_time, score + add_score, new_status))
        current_best = max(current_best, score + add_score)

print(f"Part one: {current_best}")

# Find solution for part two

positions = [(("AA", "AA"), (26, 26), 0, {x: False for x in valves.keys()})]
current_best = 0
to_search = 3
checked = {(positions[0][:3])}

while positions:
    current, time_left, score, status = positions.pop(0)
    destinations = []

    for agent in range(2):
        for valve in valves.keys():
            if valve == current[agent] or status[valve]:
                continue

            dist = valves[current[agent]]["tunnels"][valve]
            destinations.append((agent, valve, valves[valve]["flow"] * (time_left[agent] - dist - 1), dist, (valves[valve]["flow"] * (time_left[agent] - dist - 1))/(dist + 1)))
    
    if len(destinations) == 0:
        continue
    
    destinations = sorted(destinations, key = lambda x: x[4], reverse = True)
    
    for i in range(min(len(destinations), to_search)):

        agent, dest, add_score, dist, ranking = destinations[i]
        new_time = list(deepcopy(time_left))
        new_time[agent] -= dist + 1

        if new_time[agent] <= 0:
            break

        new_status = deepcopy(status)
        new_status[dest] = True
        new_pos = list(deepcopy(current))
        new_pos[agent] = dest

        new_time = tuple(new_time)
        new_pos = tuple(new_pos)

        if (new_pos, new_time, score + add_score) in checked:
            continue
        else:
            checked.add((new_pos, new_time, score + add_score))
            positions.append((new_pos, new_time, score + add_score, new_status))
            current_best = max(current_best, score + add_score)

print(f"Part two: {current_best}")
