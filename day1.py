
f = open("day1.txt")
nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
num_nums = "123456789"

list = f.read().splitlines()

total = 0

for string in list:
    string = string.replace("one", "o1e").replace("two", "t2o").replace("three", "t3e").replace("four", "f4r").replace("five", "f5e").replace("six", "s6").replace("seven", "s7n").replace("eight", "e8ht").replace("nine", "n9ne")

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