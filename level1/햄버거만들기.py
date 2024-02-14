def solution(ingredient):
    answer = 0
    making = []
    for i in ingredient:
        making.append(i)
        if making[-4:] == [1, 2, 3, 1]:
            answer += 1
            del making[-4:]
    return answer
ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))