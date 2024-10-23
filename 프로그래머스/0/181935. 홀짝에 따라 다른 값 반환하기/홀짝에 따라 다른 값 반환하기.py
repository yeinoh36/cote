def solution(n):
    answer = 0
    if n%2: # 홀수
        answer = ((n+1)/2)*(n//2+1)
    else: # 짝수
        answer = (4*(n/2)*(n/2+1)*(n+1))/6
        
    return answer