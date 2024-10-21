import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer = numer1*denom2 + numer2*denom1
    denom = denom1*denom2
    answer.append(numer/math.gcd(numer, denom))
    answer.append(denom/math.gcd(numer, denom))
    
    return answer