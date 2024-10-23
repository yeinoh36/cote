def solution(slice, n):
    answer = n//slice
    if n%slice:
        answer += 1
    return answer