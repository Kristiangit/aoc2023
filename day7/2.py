
f = open("day7/day7.txt")

list = f.read().splitlines()

cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
cards.reverse()
bid_total = 0

hands = []

for line in list:
    line = line.split(" ")
    pair1 = False
    jbool = False
    power_rank = 0

    for i in line[0]:
        #23569, J2987, 35589, 13731, 7J449, JTT88, KK555, 8J444, 

        if line[0] == "JJJJJ":
            power_rank = 600
            break
        elif i == pair1 or i == "J":
            continue

        # pairs = line[0].count(i) + line[0].count("J")
        pairs = line[0].count(i)
        if not pair1 : pairs += line[0].count("J")
        elif (pairs + line[0].count("J") > 2 and not jbool): 
            pairs += line[0].count("J")
            jbool = True
        
        if pairs >= 4:
            power_rank = (pairs + 1) * 100
            break

        elif pairs == 3:
            if pair1:
                if line[0].count(pair1) == 2:
                    power_rank = 400
                    break
            pair1 = i
            power_rank = 300

        # elif pairs > 1 and i != pair1 and line[0].count("J") == 0:
        elif pairs == 2 :

            #et par, to par, fullt hus, et par pga J, fullt hus pga J, IKKE DETTE tre like
            # TT546, 8822A,  QQQKK,      324J8          TTJ33,             45J59

            power_rank += 100
            if pair1:
                break
            pair1 = i
            
    power_rank += (cards.index(line[0][0]) + 1)
    power_rank *= 100
    
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

    if (20000 <= hands[i][0] < 30000 and hands[i][2].count("J") > 0) or (40000 <= hands[i][0] < 50000 and hands[i][2].count("J") > 0):
        print(hands[i])

bid_total += hands[len(hands)-1][1] * len(hands)

print(hands)
print(bid_total)