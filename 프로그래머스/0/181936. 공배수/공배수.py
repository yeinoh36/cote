def solution(number, n, m):
    answer = 0
    if not(number%n) and not(number%m):
        answer = 1
    return answer