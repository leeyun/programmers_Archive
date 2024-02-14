def solution(food):
    answer = ''
    for f in range(1, len(food)):
        if food[f] % 2 != 0:
            answer += f'{f}'*int((food[f] - 1)/2)
        else:
            answer += f'{f}'*int(food[f]/2)
    answer += '0'
    temp = list(answer)
    temp.reverse()
    answer += ''.join(temp[1:])
    return answer
food = [1, 3, 4, 6]
print(solution(food))