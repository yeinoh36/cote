from collections import Counter
def solution(array):
    answer = 0
    
    counts = list(Counter(array).items())
    counts.sort(key=lambda x: x[1])
    
    if len(counts) == 1:
        return array[0]
    
    if counts[-1][1] != counts[-2][1]:
        answer = counts[-1][0]
    else: answer = -1
    
    return answer