def solution(s, skip, index):
    answer = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    forward = 0
    for word in skip:
        alpha = alpha.replace(word, "")
    forward = len(alpha)
    for word in s:
        answer += alpha[(alpha.find(word) + index) % forward]
    return answer
s = "aukks"
skip = "wbqd"
index = 5
print(solution(s, skip, index))