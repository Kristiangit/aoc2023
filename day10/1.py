
f = open("day10/day10.txt")

list = f.read().splitlines()

total = 0
grid = [[i for i in line] for line in list ]
steps = 1
nextpipe = []
direction = ""

for i in grid:
    if "S" in i:
        start = [i.index("S"), grid.index(i)]

if grid[start[1]][start[0] +1] == "-" or grid[start[1]][start[0] +1] == "J" or grid[start[1]][start[0] +1] == "7":
    x,y = start[0] + 1, start[1]
    direction = "RIGHT"
elif grid[start[1]][start[0] -1] == "-" or grid[start[1]][start[0] -1] == "L" or grid[start[1]][start[0] -1] == "F":
    x,y = start[0] - 1, start[1]
    direction = "LEFT"
elif grid[start[1]-1][start[0]] == "|" or grid[start[1]-1][start[0]] == "F" or grid[start[1]-1][start[0]] == "7":
    x,y = start[0] , start[1]-1
    direction = "UP"
elif grid[start[1]+1][start[0]] == "|" or grid[start[1]+1][start[0]] == "J" or grid[start[1]+1][start[0]] == "L":
    x,y = start[0], start[1]+1
    direction = "DOWN"

while grid[y][x] != "S":
    match grid[y][x]:
        case "-":
            if direction == "RIGHT":
                x += 1
            elif direction == "LEFT":
                x -= 1
        case "J":
            if direction == "RIGHT":
                direction = "UP"
                y -= 1
            elif direction == "DOWN":
                direction = "LEFT"
                x -= 1
        case "7":
            if direction == "RIGHT":
                direction = "DOWN"
                y += 1
            elif direction == "UP":
                direction = "LEFT"
                x -= 1
        case "L":
            if direction == "DOWN":
                direction = "RIGHT"
                x += 1
            elif direction == "LEFT":
                direction = "UP"
                y -= 1
        case "F":
            if direction == "UP":
                direction = "RIGHT"
                x += 1
            elif direction == "LEFT":
                direction = "DOWN"
                y += 1
        case "|":
            if direction == "DOWN":
                y += 1
            elif direction == "UP":
                y -= 1

    steps += 1

print(grid)
print(steps, steps/2)