file = open("Data/day6.txt", "r")

for line in file:
    datastream = line

def find_marker(datastream, n):
    for i in range(len(datastream) - n + 1):
        if len(datastream[i:i + n]) == len(set(datastream[i:i + n])):
            return i + n

print(f"Part one: {find_marker(datastream, 4)}")
print(f"Part two: {find_marker(datastream, 14)}")
