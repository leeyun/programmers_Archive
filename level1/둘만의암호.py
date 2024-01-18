def solution(s, skip, index):
    answer = ""
    for word in s:
        if word in skip:
            continue
        change = ord(word)+index
        answer += (chr(change))

    return answer
s = "aukks"
skip = "wbqd"
index = 5
print(solution(s, skip, index))