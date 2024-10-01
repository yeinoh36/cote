from collections import Counter
def solution(citations):
    answer = 0
    citations = sorted(citations)
    counts = Counter(citations)
    sum = len(citations)
    
    for i in range(len(citations)+1):
        if sum >= i:
            answer = max(answer, i)
        sum -= counts[i]
           
    return answer