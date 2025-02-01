def solution(n):
    tmp = []
    while n > 0:
        r = n % 3
        n = n // 3
        if r == 0:
            r = 4
            n = n - 1
        tmp.append(r)        

    if not tmp:
        return '0'

    tmp.reverse()
    answer = ''.join(map(str, tmp))
    return answer