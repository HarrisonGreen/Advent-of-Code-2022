file = open("Data/day4.txt", "r")

assignments = []

for line in file:
    line = line.strip().split(sep = ",")
    line = line[0].split("-") + line[1].split("-")
    line = [int(x) for x in line]

    assignments.append(line)

count = 0

for pair in assignments:
    if pair[0] <= pair[2] and pair[1] >= pair[3]:
        count += 1
    elif pair[0] >= pair[2] and pair[1] <= pair[3]:
        count += 1

print(f"Part one: {count}")

count = 0

for pair in assignments:
    if pair[0] <= pair[2] and pair[1] >= pair[2]:
        count += 1
    elif pair[0] >= pair[2] and pair[0] <= pair[3]:
        count += 1

print(f"Part two: {count}")
