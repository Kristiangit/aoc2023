
f = open("day4/day4.txt")

list = f.read().splitlines()

copy_dict = {i+1:1 for i in range(len(list))}


for line in list:
    wins = 0
    line = line.split(" ")
    print(line)
    while line[1] == "":
        line.pop(1)
    currGame = int(line[1].strip(":".strip(" ")))

    winning = line[2:line.index("|")]
    # print(winning)
    for i in line[line.index("|"):]:
        if i in winning:
            if i == "":
                continue
            # print(i)
            wins += 1
    if wins > 0:
        for i in range(currGame + 1, wins + currGame + 1):
            copy_dict[i] += (1 * copy_dict[currGame])
            
            
            ...
print(copy_dict)
total = sum(copy_dict.values())
    
print(total)