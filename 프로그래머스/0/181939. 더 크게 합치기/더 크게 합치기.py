def solution(a, b):
    answer = 0
    stra = str(a)
    strb = str(b)
    
    ab = ''
    ab += stra + strb
    ba = ''
    ba += strb + stra
    
    if ab > ba:
        answer = int(ab)
    else:
        answer = int(ba)

    return answer