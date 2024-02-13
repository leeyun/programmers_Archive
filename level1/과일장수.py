def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    slicing = 0
    for _ in range(len(score)//m):
        answer += min(score[slicing:slicing+m])*m
        slicing += m
    return answer
k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print(solution(k, m, score))