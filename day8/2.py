
f = open("day8/day8.txt")

list = f.read().splitlines()

node_dict = {}

total_steps = 0
currNodes = []

for string in list:
    string = string.split(" ")
    if len(string) < 2:
        if "L" in string[0]: recipe = string[0]

        continue

    node_dict[string[0]] = [string[2].strip("(").strip(","), string[-1].strip(")")]
    if string[0][-1] == "A":
        currNodes.append(string[0])
    ...
print(currNodes)
all_Z = False
zList = [[0, []] for _ in currNodes]
while not all_Z:
    z_counter = 0
    now_step = recipe[total_steps % len(recipe)]
    if now_step == "L":
        now_step = 0
    else: now_step = 1
    total_steps += 1

    for i in range(len(currNodes)):

        currNodes[i] = node_dict[currNodes[i]][now_step]
        if (currNodes[i])[-1] == "Z":
            zList[i][1].append(total_steps)
            zList[i][0] += 1
        if zList[i][0] >= 3:
            z_counter += 1
    if z_counter >= 3:
        # print(z_counter, zList)
        if z_counter == len(currNodes):
                all_Z = True


print(zList)

for i in range(len(zList)-1,):
    for j in range(len(zList)):
        for a in range(len(zList)):
            for b in range(len(zList)):
                for c in range(len(zList)):
                    counter = 0
                    answer = zList[i][1][0] * zList[j][1][0] * zList[a][1][0] * zList[b][1][0] * zList[c][1][0]
                    for k in range( len(zList)):
                        if answer % zList[k][1][0] != 0:
                            # print(answer)
                            counter += 1
                            break
                        else:
                            counter += 1
                    if counter == 4: break
                if counter == 4: break
            if counter == 4: break
        if counter == 4: break
    if counter == 4: break

# calculate each node/z thing as a function after length is 3 and find difference and then use math to find intersection between them all

# print(zList)
print(answer, counter)