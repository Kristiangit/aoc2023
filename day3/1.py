
f = open("day3/day3.txt")

list = f.read().splitlines()
total = 0

def checkGrid(number, x, y):
    if y != 0:
        y -= 1
    for _ in range(3):
        for i in range(len(number)+2):
            if y == len(list) or x+i == 0 or x+i == len(list[y]): continue
            if list[y][x+i] != "." and not list[y][x+i].isnumeric():
                return True
        y += 1
    
    return False
num = False
number = ""
for y in range(len(list)):
    for x in range(len(list[y])):
        if list[y][x].isnumeric() and not list[y][x-1].isnumeric(): num = True

        if num:
            number += list[y][x]

        if x == len(list[y])-1 or (list[y][x].isnumeric() and not list[y][x+1].isnumeric()):
            print(number)
            if checkGrid(number, x-len(number), y): total += int(number)
            
            num = False
            number = ""
            
print(total)