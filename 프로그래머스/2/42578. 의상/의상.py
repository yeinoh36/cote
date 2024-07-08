from collections import Counter
def solution(clothes):
    answer = 1
    type = []
    
    for item in clothes:
        type.append(item[1])
    
    count = Counter(type)
    
    for n in list(count.values()):
        answer *= (n+1)

    answer -= 1
    return answer

