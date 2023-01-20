from math import ceil
from copy import deepcopy

file = open("Data/day19.txt", "r")

blueprints = {}

for line in file:
    line = line.split()
    blueprints[int(line[1][:-1])] = {0: (int(line[6]), 0, 0), 1: (int(line[12]), 0, 0), 2: (int(line[18]), int(line[21]), 0), 3: (int(line[27]), 0, int(line[30]))}

def count_geodes(blueprint, materials, robots, time, max_reqs):
    possibles = []

    if robots[0] < max_reqs[0]:
        ore_wait = max(0, ceil((blueprint[0][0] - materials[0])/robots[0]))

        if ore_wait <= time - 3:
            new_materials = deepcopy(materials)
            new_materials = [new_materials[i] + (ore_wait + 1) * robots[i] for i in range(4)]
            new_materials[0] -= blueprint[0][0]

            new_robots = deepcopy(robots)
            new_robots[0] += 1

            possibles.append((new_materials, new_robots, time - (ore_wait + 1)))
    
    if robots[1] < max_reqs[1]:
        clay_wait = max(0, ceil((blueprint[1][0] - materials[0])/robots[0]))

        if clay_wait <= time - 4:
            new_materials = deepcopy(materials)
            new_materials = [new_materials[i] + (clay_wait + 1) * robots[i] for i in range(4)]
            new_materials[0] -= blueprint[1][0]

            new_robots = deepcopy(robots)
            new_robots[1] += 1

            possibles.append((new_materials, new_robots, time - (clay_wait + 1)))

    if robots[2] < max_reqs[2] and robots[1] > 0:
        obsidian_wait = max(0, ceil((blueprint[2][0] - materials[0])/robots[0]), ceil((blueprint[2][1] - materials[1])/robots[1]))

        if obsidian_wait <= time - 3:
            new_materials = deepcopy(materials)
            new_materials = [new_materials[i] + (obsidian_wait + 1) * robots[i] for i in range(4)]
            new_materials[0] -= blueprint[2][0]
            new_materials[1] -= blueprint[2][1]

            new_robots = deepcopy(robots)
            new_robots[2] += 1

            possibles.append((new_materials, new_robots, time - (obsidian_wait + 1)))
    
    if robots[2] > 0:
        geode_wait = max(0, ceil((blueprint[3][0] - materials[0])/robots[0]), ceil((blueprint[3][2] - materials[2])/robots[2]))

        if geode_wait <= time - 2:
            new_materials = deepcopy(materials)
            new_materials = [new_materials[i] + (geode_wait + 1) * robots[i] for i in range(4)]
            new_materials[0] -= blueprint[3][0]
            new_materials[2] -= blueprint[3][2]

            new_robots = deepcopy(robots)
            new_robots[3] += 1

            possibles.append((new_materials, new_robots, time - (geode_wait + 1)))
    
    if len(possibles) == 0:
        new_materials = deepcopy(materials)
        new_materials = [new_materials[i] + time * robots[i] for i in range(4)]

        possibles.append((new_materials, robots, 0))
    
    return possibles

def main():
    total = 0

    for n, blueprint in blueprints.items():

        max_reqs = [max(blueprint[i][j] for i in range(4)) for j in range(3)]
        to_check = [([0, 0, 0, 0], [1, 0, 0, 0], 24)]
        checked = set(((0, 0, 0, 0), (1, 0, 0, 0), 24))
        current_best = 0

        while to_check:
            state = to_check.pop(0)
            new_states = count_geodes(blueprint, state[0], state[1], state[2], max_reqs)

            for new_state in new_states:
                if new_state[2] == 0:
                    current_best = max(current_best, new_state[0][3])
                elif (tuple(new_state[0]), tuple(new_state[1]), new_state[2]) not in checked:
                    to_check.append(new_state)
                    checked.add((tuple(new_state[0]), tuple(new_state[1]), new_state[2]))
        
        total += n * current_best
    
    print(f"Part one: {total}")

    total = 1

    for n, blueprint in blueprints.items():
        if n > 3:
            continue

        max_reqs = [max(blueprint[i][j] for i in range(4)) for j in range(3)]
        to_check = [([0, 0, 0, 0], [1, 0, 0, 0], 32)]
        checked = set(((0, 0, 0, 0), (1, 0, 0, 0), 32))
        current_best = 0

        while to_check:
            state = to_check.pop(0)
            new_states = count_geodes(blueprint, state[0], state[1], state[2], max_reqs)

            for new_state in new_states:
                if new_state[2] == 0:
                    current_best = max(current_best, new_state[0][3])
                elif (tuple(new_state[0]), tuple(new_state[1]), new_state[2]) not in checked:
                    to_check.append(new_state)
                    checked.add((tuple(new_state[0]), tuple(new_state[1]), new_state[2]))
        
        total *= current_best
    
    print(f"Part two: {total}")

main()
