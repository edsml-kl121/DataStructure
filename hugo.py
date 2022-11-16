# def bestHand(ranks, suits):
    
#     for i in range(len(ranks)):
#         if suits.count(suits[0]) != 5 and ranks.count(ranks[i]) == 1:
#             return "High Card"
#         elif ranks.count(ranks[i]) >= 3 and suits.count(suits[0]) != 5:
#             return "Three of a Kind"
        
#         elif ranks.count(ranks[i]) == 2 and suits.count(suits[0]) != 5:
#             return "Pair"
#         else:
#             return "Flush"

def bestHand(ranks, suits):
    numSuits = 0
    firstSuit = suits[0]
    for suit in suits:
        if firstSuit == suit:
            numSuits += 1
    
    rankDict = {}
    maxNum = 0
    for rank in ranks:
        if rank not in rankDict:
            rankDict[rank] = 1
        else:
            rankDict[rank] += 1
        maxNum = max(maxNum, rankDict[rank])
    print(maxNum)
    if numSuits == 5:
        return "Flush"
    elif maxNum >= 3:
        return "Three of a Kind"
    elif maxNum == 2:
        return "Pair"
    else:
        return "High Card"



ranks = [4,4,2,4,4]
suits = ["d","a","a","b","c"]
# ranks = [9,2,13,1,2]
# suits = ["b","d","d","b","c"]

print(bestHand(ranks, suits))
