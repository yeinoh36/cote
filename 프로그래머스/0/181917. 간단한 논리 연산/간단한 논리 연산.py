def calculatev(x, y):
    if x == False and y == False:
        return False
    else:
        return True

def solution(x1, x2, x3, x4):
    answer = True
    if calculatev(x1, x2) == False or calculatev(x3, x4) == False:
        answer = False
    return answer