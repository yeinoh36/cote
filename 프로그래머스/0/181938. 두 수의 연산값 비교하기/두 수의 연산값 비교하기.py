def solution(a, b):
    ab2 = 2*a*b
    ab = str(a) + str(b)
    
    return max(ab2, int(ab))