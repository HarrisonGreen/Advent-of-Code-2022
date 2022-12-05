file = open("Data/day3.txt", "r")

rucksacks = []

for line in file:
    line = line.strip()
    n = len(line)//2
    rucksacks.append([line[:n], line[n:]])

priorities = 0

for rucksack in rucksacks:
    item = list(set(rucksack[0]).intersection(set(rucksack[1])))[0]
    
    if ord(item) > 90:
        priorities += ord(item) - 96
    else:
        priorities += ord(item) - 38

print(f"Part one: {priorities}")

priorities = 0

for i in range(len(rucksacks)//3):
    rucksack_one = rucksacks[3 * i]
    rucksack_two = rucksacks[3 * i + 1]
    rucksack_three = rucksacks[3 * i + 2]

    rucksack_one = set(rucksack_one[0]).union(set(rucksack_one[1]))
    rucksack_two = set(rucksack_two[0]).union(set(rucksack_two[1]))
    rucksack_three = set(rucksack_three[0]).union(set(rucksack_three[1]))

    item = list(rucksack_one.intersection(rucksack_two).intersection(rucksack_three))[0]

    if ord(item) > 90:
        priorities += ord(item) - 96
    else:
        priorities += ord(item) - 38

print(f"Part two: {priorities}")
