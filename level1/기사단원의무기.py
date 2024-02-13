def solution(number, limit, power):
    answer = 0
    temp = 0
    for knight in range(1, number+1):
        for i in range(1, int(knight**(1/2) + 1)):
            if knight % i == 0:
                temp += 1
                if i**2 != knight:
                    temp += 1
        if temp > limit:
            answer += power
        else:
            answer += temp
        temp = 0

    return answer
number = 10
limit = 3
power = 2
print(solution(number, limit, power))