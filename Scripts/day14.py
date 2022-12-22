import numpy as np

file = open("Data/day14.txt", "r")

height = 200
width = 400
grid = np.zeros([height, width], dtype = int)
max_depth = 0

for line in file:
    line = line.strip("\n").split(" -> ")
    line = [x.split(",") for x in line]
    line = [(int(x[0]), int(x[1])) for x in line]
    
    for i in range(len(line) - 1):
        if line[i][0] == line[i + 1][0]:
            grid[min(line[i][1], line[i + 1][1]):max(line[i][1], line[i + 1][1] + 1), line[i][0] - (500 - width//2)] = 1
        else:
            grid[line[i][1], (min(line[i][0], line[i + 1][0]) - (500 - width//2)):(max(line[i][0], line[i + 1][0]) - (500 - width//2) + 1)] = 1
        
        max_depth = max(max_depth, line[i][1], line[i + 1][1])

def add_sand(grid):
    pos = [0, width//2]

    while pos[0] < height - 1:

        if grid[pos[0] + 1, pos[1]] == 0:
            pos[0] += 1

        elif grid[pos[0] + 1, pos[1] - 1] == 0:
            pos[0] += 1
            pos[1] -= 1

        elif grid[pos[0] + 1, pos[1] + 1] == 0:
            pos[0] += 1
            pos[1] += 1

        else:
            grid[pos[0], pos[1]] = 2
            return grid, True

    return grid, False

count = 0
while True:
    grid, successful = add_sand(grid)

    if successful:
        count += 1
    else:
        break

print(f"Part one : {count}")

grid[max_depth + 2, :] = 1

while grid[0, width//2] == 0:
    grid, successful = add_sand(grid)
    count += 1

print(f"Part two: {count}")
