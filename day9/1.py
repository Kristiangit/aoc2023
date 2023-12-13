
f = open("day9/day9.txt")

list = f.read().splitlines()
total = 0

for line in list:
    all_0 = False

    line = [int(i) for i in line.split(" ")]
    diff_lists = [line]
    curr_diff = 0
    nextNum = 0

    
    while all_0 == False:
        count0 = 0
        diff_lists.append([])
        for i in range(len(diff_lists[curr_diff])-1):
            diff = diff_lists[curr_diff][i+1] - diff_lists[curr_diff][i]
            diff_lists[curr_diff+1].append(diff)
            if diff == 0:
                count0 += 1
        if count0 == len(diff_lists[curr_diff])-1:
            all_0 = True

        curr_diff += 1
    
    diff_lists[curr_diff].append(0)

    for i in range(len(diff_lists)-2, -1, -1):
        nextNum += (diff_lists[i][-1])
        ...
    # print(nextNum, diff_lists[0])
    total += nextNum
print(total)