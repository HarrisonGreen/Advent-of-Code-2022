import numpy as np

file = open("Data/day9.txt", "r")
motions = []

for line in file:
    line = line.split()
    line[1] = int(line[1])
    motions.append(line)

def count_positions(motions, knots):
    dim = 1000
    grid = np.zeros([dim, dim], dtype = int)
    pos = [[dim//2, dim//2] for _ in range(knots)]
    grid[dim//2, dim//2] = 1

    for motion in motions:
        for _ in range(motion[1]):

            if motion[0] == "U":
                pos[0][0] -= 1
            elif motion[0] == "D":
                pos[0][0] += 1
            elif motion[0] == "L":
                pos[0][1] -= 1
            elif motion[0] == "R":
                pos[0][1] += 1
            
            for i in range(1, knots):
                x = pos[i - 1][0] - pos[i][0]
                y = pos[i - 1][1] - pos[i][1]

                if abs(x) == 2:
                    pos[i][0] += x//2
                    if abs(y) == 1:
                        pos[i][1] += y
                    elif abs(y) == 2:
                        pos[i][1] += y//2
                elif abs(y) == 2:
                    pos[i][1] += y//2
                    if abs(x) == 1:
                        pos[i][0] += x
                
            grid[pos[-1][0], pos[-1][1]] = 1

    return np.sum(grid)
        
print(f"Part one: {count_positions(motions, 2)}")
print(f"Part two: {count_positions(motions, 10)}")
