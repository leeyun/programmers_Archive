def solution(s):
    main = s[0]
    length = len(s)
    syn = 0
    anti = 0
    answer = 0
    for i in range(length):
        if s[i] == main:
            syn += 1
        else:
            anti += 1
        if syn == anti:
            answer += 1
            if i + 1 == length:
                break
            else:
                main = s[i + 1]
    if syn != anti:
        answer += 1
    return answer

