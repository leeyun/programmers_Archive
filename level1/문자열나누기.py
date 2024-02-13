def solution(s):
    answer = 0
    criterion = s[0]
    correct = 1
    incorrect = 0
    for i in range(1, len(s)):
        if correct == incorrect:
            criterion = s[i]
            answer += 1
            correct = 0
            incorrect = 0
        if criterion == s[i]:
            correct += 1
        else:
            incorrect += 1
    if correct == incorrect:
        answer += 1
    if criterion == s[-1]:
        answer += 1
    return answer
s = "aaabbaccccabbaaaaa"
print(solution(s))

