import numpy as np

file = open("Data/day8.txt", "r")
grid = np.zeros([99, 99])

for i, line in enumerate(file):
    line = line.strip()

    for j, height in enumerate(line):
        grid[i, j] = height

visible = 0

for i in range(99):
    for j in range(99):
        
        if i in (0, 98) or j in (0, 98):
            visible += 1
            continue

        height = grid[i, j]
        
        up = max(grid[:i, j])
        if up < height:
            visible += 1
            continue

        down = max(grid[i + 1:, j])
        if down < height:
            visible += 1
            continue

        left = max(grid[i, :j])
        if left < height:
            visible += 1
            continue

        right = max(grid[i, j + 1:])
        if right < height:
            visible += 1
            continue

print(f"Part one: {visible}")

scenic = 0

for i in range(99):
    for j in range(99):
        
        if i in (0, 98) or j in (0, 98):
            continue

        height = grid[i, j]
        
        up = grid[:i, j]
        for k in range(len(up)):
            if up[- 1 - k] >= height:
                up_score = k + 1
                break
            elif k == len(up) - 1:
                up_score = k + 1
        
        down = grid[i + 1:, j]
        for k in range(len(down)):
            if down[k] >= height:
                down_score = k + 1
                break
            elif k == len(down) - 1:
                down_score = k + 1
        
        left = grid[i, :j]
        for k in range(len(left)):
            if left[- 1 - k] >= height:
                left_score = k + 1
                break
            elif k == len(left) - 1:
                left_score = k + 1
        
        right = grid[i, j + 1:]
        for k in range(len(right)):
            if right[k] >= height:
                right_score = k + 1
                break
            elif k == len(right) - 1:
                right_score = k + 1
        
        scenic = max(scenic, up_score * down_score * left_score * right_score)

print(f"Part two: {scenic}")
