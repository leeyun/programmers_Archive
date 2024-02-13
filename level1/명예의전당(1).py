def solution(k, score):
    answer = []
    hall = []
    length = len(score)
    for i in range(length):
        hall.append(score[i])
        hall.sort(reverse=True)
        answer.append(min(hall[:k]))
    return answer