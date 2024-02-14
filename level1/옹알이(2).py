def solution(babbling):
    answer = 0
    pron = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        temp = ""
        word = ""
        for alpha in b:
            temp += alpha
            if temp in pron:
                if word == temp:
                    
                word = temp
            
    return answer
babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(babbling))