
f = open("day6/day6.txt")

list = [i.split(" ") for i in f.read().splitlines()]
time, distance = "", ""

for i in list[0]:

    if i.isnumeric():
        time += (i)

for i in list[1]:

    if i.isnumeric():
        distance += (i)

time, distance = int(time), int(distance) 

total = 0
for raceTime in range(time):
    if raceTime * (time - raceTime) > distance:
        # print(raceTime, raceTime * (time - raceTime), distance)
        total += 1


print(total)