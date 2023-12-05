
f = open("day4/day4.txt")

list = f.read().splitlines()
total = 0

for line in list:
    wins = 0
    line = line.split(" ")

    winning = line[2:line.index("|")]
    print(winning)
    for i in line[line.index("|"):]:
        if i in winning:
            if i == "":
                continue
            print(i)
            wins += 1
    if wins > 0:
        total += 2 **(wins -1)
    print(total, 2 **(wins-1), wins)
    
print(total)