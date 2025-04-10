def solution(number):
    answer = 0
    for a in str(number):
        answer += int(a)
    
    answer = answer%9
    
    return answer