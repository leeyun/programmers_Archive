def solution(s):
    answer = []
    alpha = {chr(alphabet):-1 for alphabet in range(97, 123)}
    for index, word in enumerate(s):
        if alpha[word] == -1:
            answer.append(-1)
            alpha[word] = index
        else:
            answer.append(index -alpha[word])
            alpha[word] = index
    return answer