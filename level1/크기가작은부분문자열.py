def solution(t, p):
    answer = 0
    start = 0
    end = len(p)
    intP = int(p)
    while end <= len(t):
        if int(t[start:end]) <= intP:
            answer += 1
        start += 1
        end += 1
    return answer
t = "3141592"
p = "271"
answer = solution(t, p)
print(answer)