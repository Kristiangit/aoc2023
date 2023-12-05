
f = open("day2/day2.txt")

list = f.read().splitlines()

gametotal = 0

for line in list:
    cont = False
    line = line.split(" ")
    for i in range(len(line)):
        if "red" in line[i] and int(line[i-1]) > 12: cont = True
        if "green" in line[i] and int(line[i-1]) > 13: cont = True
        if "blue" in line[i] and int(line[i-1]) > 14: cont = True

    if cont: continue
    gametotal += int(line[1].strip(":"))
            
print(gametotal)
