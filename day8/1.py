
f = open("day8/day8.txt")

list = f.read().splitlines()

node_dict = {}

total_steps = 0

for string in list:
    string = string.split(" ")
    if len(string) < 2:
        if "L" in string[0]:
            recipe = string[0]
            print(recipe, len(recipe))
        continue

    node_dict[string[0]] = [string[2].strip("(").strip(","), string[-1].strip(")")]
    ...

currNode = "AAA"
while currNode != "ZZZ":
    now_step = recipe[total_steps % len(recipe)]
    if now_step == "L":
        now_step = 0
    else: now_step = 1

    print(currNode)
    currNode = node_dict[currNode][now_step]
    total_steps += 1
    ...

print(currNode)
print(total_steps)