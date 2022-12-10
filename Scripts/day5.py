from copy import deepcopy

file = open("Data/day5_stacks.txt", "r")

lines = []
for line in file:
    lines.append(line)

stacks = {int(x): [] for x in lines[-1].split()}
n = max(stacks.keys())

for i in range(len(lines) - 2, -1, -1):
    line = lines[i]

    for j in range(1, len(line), 4):
        char = line[j]
        
        if char != " ":
            stacks[(j + 3)/4].append(char)

file = open("Data/day5_instructions.txt", "r")

instructions = []

for line in file:
    line = line.split()
    instructions.append([int(line[1]), int(line[3]), int(line[5])])

new_stacks = deepcopy(stacks)

for instr in instructions:
    for _ in range(instr[0]):
        new_stacks[instr[2]].append(new_stacks[instr[1]].pop(-1))

print(f"Part one: {''.join(new_stacks[i][-1] for i in range(1, n + 1))}")

new_stacks = deepcopy(stacks)

for instr in instructions:
    new_stacks[instr[2]] += new_stacks[instr[1]][-instr[0]:]
    new_stacks[instr[1]] = new_stacks[instr[1]][:-instr[0]]

print(f"Part two: {''.join(new_stacks[i][-1] for i in range(1, n + 1))}")
