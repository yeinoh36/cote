def solution(brown, yellow):
    xplusy = int(brown/2 - 2)
    for x in range(1, xplusy):
        if x * (xplusy - x) == yellow:
            w = max(x+2, xplusy-x+2)
            h = min(x+2, xplusy-x+2)
            answer = [w, h]
            break
    return answer