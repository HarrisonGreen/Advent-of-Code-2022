import numpy as np

file = open("Data/day15.txt", "r")

positions = []
beacons = {}

for line in file:
    line = line.split()
    line = [int(line[2][2:-1]), int(line[3][2:-1]), int(line[8][2:-1]), int(line[9][2:])]
    positions.append(line)

    beacons[line[3]] = beacons.get(line[3], set())
    beacons[line[3]].add(line[2])

blocked = {}

for pos in positions:
    dist = abs(pos[2] - pos[0]) + abs(pos[3] - pos[1])
    
    for y in range(pos[1] - dist, pos[1] + dist + 1):
        i = dist - abs(y - pos[1])
        blocked[y] = blocked.get(y, [])
        blocked[y].append([pos[0] - i, pos[0] + i])

row = 2000000
points = blocked[row]
points = sorted(points, key = lambda x: x[0])

row_total = 0
furthest = -np.inf

for pair in points:
    if pair[1] <= furthest:
        continue
    else:
        pair[0] = max(pair[0], furthest + 1)
        row_total += pair[1] - pair[0] + 1
        furthest = pair[1]

row_total -= len(beacons.get(row, set()))

print(f"Part one: {row_total}")

for row, points in blocked.items():
    if row < 0 or row > 4000000:
        continue

    points = sorted(points, key = lambda x: x[0])

    row_total = 0
    furthest = -1

    for pair in points:
        if pair[1] <= furthest:
            continue
        else:
            pair[0] = max(pair[0], furthest + 1)
            row_total += pair[1] - pair[0] + 1
            furthest = pair[1]
        
        if row_total != furthest + 1:
            print(f"Part two: {4000000 * (pair[0] - 1) + row}")
            break
        