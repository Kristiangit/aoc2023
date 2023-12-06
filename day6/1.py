
f = open("day6/day6.txt")

list = [i.split(" ") for i in f.read().splitlines()]
time = []
distance = []
for i in list[0]:
    if i.isnumeric():
        
        time.append(int(i))
for i in list[1]:
    if i.isnumeric():
        
        distance.append(int(i))

total = 1
for race in range(len(time)):
    solv_total = 0
    for raceTime in range(time[race]):
        if raceTime * (time[race] - raceTime) > distance[race]:
            # print(raceTime, raceTime * (time[race] - raceTime), distance[race])
            solv_total += 1
    total *= solv_total


print(total)