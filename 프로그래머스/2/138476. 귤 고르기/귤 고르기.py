from collections import Counter, deque

def solution(k, tangerine):
    answer, summ = 0, 0
    counts = deque(sorted(list(Counter(tangerine).values())))

    while True :
        summ += counts.pop()
        answer += 1
        
        if summ >= k:
            break
    
    return answer