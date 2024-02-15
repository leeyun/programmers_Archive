def solution(a, b, n):
    answer = 0
    remain = 0
    while n >= 2:
        n, remain = divmod(n, a)
        answer += n
        if n == 1:
            n += remain
    if n == 1:
        answer += 1
    return answer
a = 3
b = 1
n = 20
print(solution(a, b, n))