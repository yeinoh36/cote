def solution(a, b, c):
    answer = 0
    if a == b and b == c:
        return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    elif a != b and b != c and c != a:
        return a+b+c
    answer = (a+b+c)*(a**2+b**2+c**2)
    return answer