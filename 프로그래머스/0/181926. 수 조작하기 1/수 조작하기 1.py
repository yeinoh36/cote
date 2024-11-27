def solution(n, controls):
    answer = n
    control_dict = {
        "w" : 1,
        "s" : -1,
        "d" : 10,
        "a" : -10
    }
    
    for control in controls:
        answer += control_dict[control]
    
    return answer