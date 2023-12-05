
f = open("day5/day5.txt")

list = f.read().splitlines()

seeds = [[[int(i)], False] for i in list[0].split(" ")[1:]]


for line in list:
    if line == "":
        for i in range(len(seeds)):
            seeds[i][1] = False
        continue

    elif line[0].isnumeric():
        line = line.split(" ")
        dest_start = int(line[0])
        seed_start = int(line[1])
        range_len = int(line[2])
    
    else:
        print(line)
        continue

    ...
    for i in range(len(seeds)):

        if seeds[i][0] [-1] in range(seed_start, seed_start + range_len):
            
            if not seeds[i][1]:
            # endre seeden til destination 
            # seeds[i] - seed_start + dest_start
                print()
                print(seeds[i][0][-1], line, i, )
                print(seeds[i][0][-1] - seed_start + dest_start)
                
                seeds[i][0].append(seeds[i][0][-1] - seed_start + dest_start)
                seeds[i][1] = True
            # print(seeds[i])

    ...
print()
# print(seeds)
lasts = [i[0][-1] for i in seeds]
print(lasts)
print(min(lasts))

