file = open("Data/day1.txt", "r")

calories = []
items = []

for line in file:
    if line == "\n":
        calories.append(items)
        items = []
    else:
        items.append(int(line))

totals = [sum(x) for x in calories]

print(f"Part one: {max(totals)}")
print(f"Part two: {sum(sorted(totals, reverse = True)[:3])}")
