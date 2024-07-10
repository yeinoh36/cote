from collections import Counter
def solution(nums):
    answer = 0
    total = len(nums)
    counts = Counter(nums)
    species = len(counts)
    
    if species <= (total/2):
        answer = species
    else:
        answer = total/2
        
    return answer