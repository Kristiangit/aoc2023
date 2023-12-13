
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
# print(currNodes)
all_Z = False

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

    if z_counter == len(currNodes):
            all_Z = True



print(total_steps)