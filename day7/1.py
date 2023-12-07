
f = open("day7/day7.txt")

list = f.read().splitlines()

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
cards.reverse()
bid_total = 0

hands = []

for line in list:
    line = line.split(" ")
    pair1 = False
    power_rank = 0

    for i in line[0]:
        if i == pair1:
            continue

        pairs = line[0].count(i)
        
        if pairs >= 4:
            power_rank = (pairs + 1) * 100
            break

        elif pairs == 3:
            if pair1:
                power_rank = 400
                break
            pair1 = i
            power_rank = 300

        elif pairs > 1 and i != pair1:
            power_rank += 100
            if pair1 :
                break
            pair1 = i
        else:
            ...
            
    power_rank += (cards.index(line[0][0]) + 2)
    power_rank *= 10
    
    hands.append([power_rank, int(line[1]), line[0]])

hands.sort()

for i in range(len(hands)-1):
    # print(hands[i], hands[i+1])
    while hands[i][0] == hands[i+1][0]:
        if hands[i][0] == hands[i+1][0] :
            for index in range(len(hands[i][2])):
                if cards.index(hands[i][2][index]) > cards.index(hands[i+1][2][index]):
                    hands[i][0] += 1
                    break
                elif cards.index(hands[i][2][index]) < cards.index(hands[i+1][2][index]):
                    hands[i+1][0] += 1
                    break
            hands.sort()
    bid_total += hands[i][1] * (i+1)
    # print(hands[i][1], hands[i][1] * (i+1), i, bid_total)

bid_total += hands[len(hands)-1][1] * len(hands)

# print(hands)
print(bid_total)