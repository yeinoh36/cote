import itertools
def solution(numbers, target):
    answer = 0
    length = len(numbers)
    signs = itertools.product([-1, +1], repeat=length)
    
    for sign in signs:
        result = 0
        for i, num in enumerate(numbers):
            result += sign[i]*num
            
        if result == target:
            answer += 1
        
    return answer