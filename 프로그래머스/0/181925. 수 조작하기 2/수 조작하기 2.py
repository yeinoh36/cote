def solution(numLog):
    answer = ''
    bf = numLog[0]
    for aft in numLog[1:]:
        if aft-bf == 1:
            answer += "w"
        elif aft-bf == -1:
            answer += "s"
        elif aft-bf == 10:
            answer += "d"
        elif aft-bf == -10:
            answer += "a"
        bf = aft
    
    return answer