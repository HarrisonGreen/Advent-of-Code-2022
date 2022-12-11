import numpy as np

file = open("Data/day7.txt", "r")

output = []

for line in file:
    output.append(line.split())

cwd = ("/",)
directories = {cwd: {"subdirs": set(), "files": {}}}

for line in output:

    if line[0] == "$" and line[1] == "cd":

        if line[2] == "/":
            cwd = ("/",)
        elif line[2] == "..":
            cwd = cwd[:-1]
        else:
            cwd += (line[2],)

    elif line[0] == "dir":
        directories[cwd + (line[1],)] = directories.get(cwd + (line[1],), {"subdirs" : set(), "files": {}})
        directories[cwd]["subdirs"].add(line[1])
    
    elif line[0] != "$":
        directories[cwd]["files"][line[1]] = int(line[0])

def calculate_size(directories, dir_name):
    file_total = sum(x for x in directories[dir_name]["files"].values())
    subdir_total = 0

    for subdir in directories[dir_name]["subdirs"]:
        subdir_total += calculate_size(directories, dir_name + (subdir,))

    return file_total + subdir_total

total_size = 0
min_size = calculate_size(directories, ("/",)) - 40000000
delete_size = np.inf

for dir_ in directories.keys():
    dir_size = calculate_size(directories, dir_)

    if dir_size <= 100000:
        total_size += dir_size
    
    if dir_size >= min_size and dir_size <= delete_size:
        delete_size = dir_size

print(f"Part one: {total_size}")
print(f"Part two: {delete_size}")
