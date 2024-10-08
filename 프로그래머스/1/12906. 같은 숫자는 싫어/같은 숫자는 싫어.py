def solution(arr):
    answer = []
    bf = -1
    
    for num in arr:
        now = num
        if bf != now:
            answer.append(now)
        bf = now
        
    return answer