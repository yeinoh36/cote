def solution(a, d, included):
    answer = 0
    sum = a
    for i in included:
        sum += d
        if i:answer += sum -d
    return answer