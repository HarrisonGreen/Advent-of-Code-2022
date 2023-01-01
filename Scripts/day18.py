file = open("Data/day18.txt", "r")

cubes = set()

for line in file:
    line = line.strip().split(",")
    line = tuple(int(x) for x in line)
    cubes.add(line)

area = 0

for cube in cubes:

    for direction in [0, 1, 2]:
        for shift in [-1, 1]:

            adjacent = list(cube)
            adjacent[direction] += shift

            if tuple(adjacent) not in cubes:
                area += 1

print(f"Part one: {area}")

dims = [[min(cube[i] for cube in cubes) for i in [0, 1, 2]], [max(cube[i] for cube in cubes) for i in [0, 1, 2]]]

area = 0
to_check = [(dims[0][0] - 1, dims[0][1] - 1, dims[0][2] - 1)]
checked = [(dims[0][0] - 1, dims[0][1] - 1, dims[0][2] - 1)]

while to_check:
    current = to_check.pop(0)

    for direction in [0, 1, 2]:
        for shift in [-1, 1]:

            adjacent = list(current)
            adjacent[direction] += shift

            if adjacent[direction] < dims[0][direction] - 1 or adjacent[direction] > dims[1][direction] + 1:
                continue
            elif tuple(adjacent) in cubes:
                area += 1
            elif tuple(adjacent) in checked:
                continue
            else:
                to_check.append(tuple(adjacent))
                checked.append(tuple(adjacent))

print(f"Part two: {area}")
