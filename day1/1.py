
f = open("day1/day1.txt")
num_nums = "123456789"

list = f.read().splitlines()

total = 0

for string in list:

    for i in string:
        if i in num_nums:
            
            nextNum = i
            break
    
    for j in range(len(string)-1, -1, -1):
        if string[j] in num_nums:
            nextNum += string[j]
            break
    

    # print(nextNum)
    total += int(nextNum)
print(total)