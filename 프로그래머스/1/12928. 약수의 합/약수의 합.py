def solution(n: int) -> int:
    s = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            s += i
            j = n // i
            if j != i:
                s += j
        i += 1
    return s