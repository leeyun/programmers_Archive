#카드뭉치
def solution(cards1, cards2, goal):
    cards1Idx = 0
    cards2Idx = 0
    c1 = len(cards1)
    c2 = len(cards2)
    g = len(goal)
    for i in range(g):
        if cards1Idx >= c1:
            for j in range(i, g):
                if cards2[cards2Idx] != goal[j]:
                    return "No"
                cards2Idx += 1
            break
        if cards2Idx >= c2:
            for j in range(i, g):
                if cards1[cards1Idx] != goal[j]:
                    return "No"
                cards1Idx += 1
            break
        if cards1[cards1Idx] == goal[i]:
            cards1Idx += 1
        elif cards2[cards2Idx] == goal[i]:
            cards2Idx += 1
        else:
            return "No"
    return "Yes"
        
cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]	
goal = ["i", "want", "to", "drink", "water"]
# cards1 = list(input().split())
# cards2 = list(input().split())
# goal = list(input().split())
answer = solution(cards1, cards2, goal)
print(answer)