def solution(n):
    answer = []

    for i in range(n//2 + n%2):
        answer.append(2*i+1)
        
    return answer