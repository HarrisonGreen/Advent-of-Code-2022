import numpy as np
import matplotlib.pyplot as plt

file = open("Data/day10.txt", "r")
instructions = []

for line in file:
    line = line.split()
    instructions.append(line)

values = []
value = 1

for instr in instructions:
    if instr[0] == "noop":
        values.append(value)
    else:
        values.append(value)
        values.append(value)
        value += int(instr[1])

print(f"Part one: {sum(i * values[i - 1] for i in range(20, 240, 40))}")

screen = np.zeros([6, 40])

for i, value in enumerate(values):
    if abs((i % 40) - value) <= 1:
        screen[i//40, i%40] = 1

plt.imshow(screen)
plt.show()
