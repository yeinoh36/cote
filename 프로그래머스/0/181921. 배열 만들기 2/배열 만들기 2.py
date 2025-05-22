def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        if all(c in '05' for c in str(num)):
            answer.append(num)
    return answer if answer else [-1]