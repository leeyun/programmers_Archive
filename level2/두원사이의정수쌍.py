#두 원 사이의 정수 쌍
import math
def solution(r1, r2):
    answer = 0
    for i in range(r1, r2):
        answer += int(math.sqrt(r2**2 - i**2)) - int(math.sqrt(r1**2 - i**2 -1))
    return answer
r1 = 2
r2 = 5
print(solution(r1, r2))