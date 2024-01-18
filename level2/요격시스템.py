def solution(targets):
    answer = 1
    targets.sort(key=lambda x:x[0])
    limit_s = targets[0][0]
    limit_e = targets[0][1]
    for t in range(1, len(targets)):
        norm = targets[t][0]
        if limit_s == targets[t][0]:
            limit_s = targets[t][0]
            limit_e = targets[t][1]
            continue
        elif limit_s < norm and limit_e > norm:
            limit_s = norm
            if limit_e > targets[t][1]:
                limit_e = targets[t][1]
        else:
            limit_s = targets[t][0]
            limit_e = targets[t][1]
            answer += 1
    return answer
# def solution(targets):
#     answer = 1
#     targets.sort(key=lambda x:x[1])
#     print(targets)
#     limit_e = targets[0][1]
#     for t in range(1, len(targets)):
#         if limit_e <= targets[t][0]:
#             answer += 1
#             limit_e = targets[t][1]
            
#     return answer

targets = [[1, 10], [2, 3], [3, 7], [4, 5], [10, 11], [1, 2], [3, 4]]
print(solution(targets))
