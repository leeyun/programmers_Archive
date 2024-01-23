def solution(today, terms, privacies):
    answer = []
    keys = []
    values = []
    todayL = list(today.split('.'))
    print(todayL)

    for term in terms:
        k, v = term.split(' ')
        keys.append(k)
        values.append(v)
    print(keys)
    print(values)

    termsL = {key: value for key, value in terms.split(' ')}
    print(termsL)
    return answer
today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
answer = solution(today, terms, privacies)