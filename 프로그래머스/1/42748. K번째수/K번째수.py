def solution(array, commands):
    answer = []
    
    for s, e, i in commands:
        tmp = sorted(array[s-1:e])
        answer.append(tmp[i-1])
        
    return answer