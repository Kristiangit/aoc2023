
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
            z_counter += 1
            zList[i][1].append(total_steps)
            zList[i][0] += 1
    if z_counter >= 1:
        print()
        print(zList)
        if z_counter == len(currNodes):
                all_Z = True



# calculate each node/z thing as a function after length is 3 and find difference and then use math to find intersection between them all


print(zList)
print(total_steps)