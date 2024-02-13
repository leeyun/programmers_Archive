def solution(today, terms, privacies):
    answer = []
    todayL = list(map(int, today.split('.')))
    termsL = {key: int(value) for key, value in (i.split() for i in terms)}
    todayN = todayL[0]*28*12 + todayL[1]*28 + todayL[2]
    isValid = 0
    for i in privacies:
        privacy = list(map(int, i[0:10].split('.')))
        privacy.append(i[-1])
        temp = privacy[1] + termsL[privacy[-1]]
        if temp > 12:
            privacy[1] = temp % 12
            privacy[0] += temp // 12
        else:
            privacy[1] = temp
        privacyN = privacy[0]*28*12 + privacy[1]*28 + privacy[2]
        if privacyN <= todayN:
            answer.append(isValid + 1)
        isValid += 1
    return answer
today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
answer = solution(today, terms, privacies)
print(answer)