
f = open("day2/day2.txt")

list = f.read().splitlines()

gametotal = 0

for line in list:
    max_R, max_G, max_B = 0, 0, 0
    cont = False
    line = line.split(" ")
    for i in range(len(line)):
        if "red" in line[i] and int(line[i-1]) > max_R: max_R = int(line[i-1])
        if "green" in line[i] and int(line[i-1]) > max_G: max_G = int(line[i-1])
        if "blue" in line[i] and int(line[i-1]) > max_B: max_B = int(line[i-1])

    power = max_B * max_G * max_R
    gametotal += power
            
print(gametotal)
