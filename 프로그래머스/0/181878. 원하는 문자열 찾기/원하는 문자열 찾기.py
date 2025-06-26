def solution(myString, pat):
    answer, i = 0, 0

    for s in myString:
        if s == pat[i].lower() or s == pat[i].upper():
            i += 1
            if i == len(pat):
                answer = 1
                break
        else:
            i = 0
        
    return answer