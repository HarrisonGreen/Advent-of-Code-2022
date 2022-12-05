file = open("Data/day2.txt", "r")

rounds = []

for line in file:
    line = line.split()
    line[0] = ord(line[0]) - 65
    line[1] = ord(line[1]) - 88

    rounds.append(line)

score = 0

for round in rounds:
    score += round[1] + 1
    score += ((((round[1] + 1) % 3) - round[0]) % 3) * 3

print(f"Part one: {score}")

score = 0

for round in rounds:
    score += 3 * round[1]
    score += ((round[0] + round[1] - 1) % 3) + 1

print(f"Part two: {score}")
