import numpy as np

file = open("Data/day12.txt", "r")
grid = np.zeros([41, 101], dtype = int)

for i, line in enumerate(file):
    line = line.strip()

    for j, char in enumerate(line):

        if char == "S":
            grid[i, j] = 1
            start = (i, j)
        
        elif char == "E":
            grid[i, j] = 26
            finish = (i, j)
        
        else:
            grid[i, j] = ord(char) - 96

to_process = [start]
processed = []
distances = np.full([41, 101], np.inf)
distances[start] = 0

while to_process:
    current = to_process.pop(0)
    current_height = grid[current]
    neighbours = [(current[0] + 1, current[1]), (current[0] - 1, current[1]), (current[0], current[1] + 1), (current[0], current[1] - 1)]

    for neighbour in neighbours:

        if neighbour[0] < 0 or neighbour[0] > 40 or neighbour[1] < 0 or neighbour[1] > 100:
            continue

        if grid[neighbour] > current_height + 1:
            continue

        distances[neighbour] = min(distances[neighbour], distances[current] + 1)

        if neighbour in processed or neighbour in to_process:
            continue

        to_process.append(neighbour)
    
    processed.append(current)

print(f"Part one: {int(distances[finish])}")

to_process = [finish]
processed = []
distances = np.full([41, 101], np.inf)
distances[finish] = 0

while to_process:
    current = to_process.pop(0)
    current_height = grid[current]
    neighbours = [(current[0] + 1, current[1]), (current[0] - 1, current[1]), (current[0], current[1] + 1), (current[0], current[1] - 1)]

    for neighbour in neighbours:
        
        if neighbour[0] < 0 or neighbour[0] > 40 or neighbour[1] < 0 or neighbour[1] > 100:
            continue

        if grid[neighbour] < current_height - 1:
            continue

        distances[neighbour] = min(distances[neighbour], distances[current] + 1)

        if neighbour in processed or neighbour in to_process:
            continue

        to_process.append(neighbour)
    
    processed.append(current)

closest = np.inf

for i in range(41):
    for j in range(101):
        if grid[i, j] == 1:
            closest = min(closest, distances[i, j])

print(f"Part two: {int(closest)}")
