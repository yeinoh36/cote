from collections import Counter

def solution(participant, completion):
    counter_p = Counter(participant)
    counter_c = Counter(completion)
    
    diff = counter_p - counter_c
    answer = list(diff.keys())[0]
    
    return answer