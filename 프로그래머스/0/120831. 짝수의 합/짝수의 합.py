def solution(n):
    answer = 0
    for i in range(1, n+1):
        if not(i%2):
            answer += i
    return answer