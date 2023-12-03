
f = open("day3/day3.txt")

list = f.read().splitlines()
total = 0
couuut = 0

def checkGrid(true_x, true_y):
    counter = 0
    gearratio = 1

    if true_y != 0:
        true_y -= 1
    if true_x != 0:
        true_x -= 1


    for y in range(true_y, true_y+3):
        same_num = False
        for x in range(true_x, true_x+3):

            if same_num: 
                if not list[y][x].isnumeric():
                    same_num = False
                continue

            if list[y][x].isnumeric():
                same_num = True
                print(x+1, y+1, "pos")
                gearratio *= findNumber(x, y)
                counter +=1

            
            if counter == 2:
                return gearratio
    
    return 0

def findNumber(x, y):
    number = ""


    if list[y][x-1].isnumeric():
        if list[y][x-2].isnumeric():
            number = list[y][x-2] + list[y][x-1] + list[y][x]
        elif list[y][x+1].isnumeric():
            number = list[y][x-1] + list[y][x] + list[y][x+1]
        else:
            number = list[y][x-1] + list[y][x]
    
    elif list[y][x+1].isnumeric():
        number = list[y][x] + list[y][x+1]
        if list[y][x+2].isnumeric():
            number += list[y][x+2]
    else:
        number = list[y][x]

    

    print(number)
    return int(number)

    

    

num = False
number = ""
for y in range(len(list)):
    for x in range(len(list[y])):


        if list[y][x] == "*":
            print()
            print(x+1, y+1, list[y][x])
            total += checkGrid(x,y)
            couuut += 1
            print(checkGrid(x,y))




            
print(total)